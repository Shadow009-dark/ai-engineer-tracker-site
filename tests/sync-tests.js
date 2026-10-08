/* sync-tests.js — tests for github-sync.js against a mocked GitHub Contents API. */
(function () {
  "use strict";

  var G = window.GitHubSync;
  var results = [];
  var visited = [];

  function assert(name, cond, detail) {
    results.push({ name: name, ok: !!cond, detail: detail || "" });
  }

  function b64(text) { return G.utf8ToBase64(text); }

  /* ---------- fake GitHub server ---------- */

  function fakeResponse(status, data, headers) {
    return {
      ok: status >= 200 && status < 300,
      status: status,
      headers: { get: function (k) { return (headers || {})[k.toLowerCase()] || null; } },
      json: function () { return Promise.resolve(data); },
    };
  }

  /**
   * Mock server. Behavior switches let a test simulate 401/403/offline/conflict.
   * files: { "path": {sha, content(base64), message} }
   */
  function makeMockGithub(initialFiles) {
    var files = {};
    Object.keys(initialFiles || {}).forEach(function (p) {
      files[p] = { sha: initialFiles[p].sha, content: b64(initialFiles[p].text || ""), lastMessage: null,
                   commits: initialFiles[p].commits || 1 };
    });
    var server = {
      files: files,
      calls: [],
      failNext: null,       // {status: 409} style forced failure
      offline: false,
      conflictOnce: {},     // path -> true
      shaCounter: 100,
      reset: function () { server.calls = []; server.failNext = null; server.offline = false; }
    };

    server.fetch = function (url, opts) {
      opts = opts || {};
      var method = opts.method || "GET";
      var path = url.replace(G.API + "/repos/Shadow009-dark/ai-engineer-tracker/contents/", "").split("?")[0];
      var call = { method: method, url: url, path: path, body: opts.body ? JSON.parse(opts.body) : null,
                   auth: (opts.headers || {}).Authorization || null };
      server.calls.push(call);
      visited.push(path + " " + method);

      if (server.offline) return Promise.reject(new TypeError("Failed to fetch"));

      if (path === "user" || url.indexOf("/user") >= 0) {
        return Promise.resolve(fakeResponse(200, { login: "Shadow009-dark" }));
      }
      if (server.failNext) {
        var f = server.failNext;
        server.failNext = null;
        return Promise.resolve(fakeResponse(f.status, { message: f.message || "forced" }, f.headers));
      }

      if (method === "GET") {
        if (!files[path]) return Promise.resolve(fakeResponse(404, { message: "Not Found" }));
        return Promise.resolve(fakeResponse(200, { sha: files[path].sha, content: files[path].content, size: 10 }));
      }

      if (method === "PUT") {
        var body = call.body || {};
        var existing = files[path];
        if (existing && body.sha !== existing.sha) {
          return Promise.resolve(fakeResponse(409, { message: "sha does not match" }));
        }
        if (!existing && body.sha) {
          return Promise.resolve(fakeResponse(422, { message: "sha given but file does not exist" }));
        }
        server.shaCounter += 1;
        var sha = "sha" + server.shaCounter;
        files[path] = existing || { commits: 0 };
        files[path].sha = sha;
        files[path].content = body.content;
        files[path].lastMessage = body.message;
        files[path].branch = body.branch;
        files[path].commits = (existing ? existing.commits : 0) + 1;
        return Promise.resolve(fakeResponse(201, { content: { sha: sha }, commit: { sha: "c" + server.shaCounter } }));
      }
      return Promise.resolve(fakeResponse(405, { message: "method not allowed" }));
    };
    return server;
  }

  function clientFor(server, opts) {
    var storage = G.memoryStorage();
    if (opts && opts.token) storage.setItem(G.KEYS.token, opts.token);
    return G.createClient({
      fetchImpl: server.fetch,
      storage: storage,
      repo: "Shadow009-dark/ai-engineer-tracker",
      token: (opts && opts.token) || undefined,
    });
  }

  /* ---------- fixtures ---------- */

  var dayPlan = {
    day: 12,
    date: "2026-10-19",
    week: 2,
    phaseId: 2,
    phaseTitle: "Data analizi",
    topic: "Pandas basics",
    learn: ["DataFrame", "groupby"],
    videos: [{ title: "Pandas Tutorial", channel: "Keith Galli", duration: "1s 30d", url: "https://www.youtube.com/results?search_query=pandas" }],
    reading: [{ title: "Pandas docs", source: "pandas.pydata.org", url: "https://pandas.pydata.org/docs/" }],
    tasks: ["Tapşırıq bir", "Tapşırıq iki", "Tapşırıq üç", "Tapşırıq dörd", "Tapşırıq beş"],
    deliverable: "Notebook",
    mustKnow: ["Sual bir?", "Sual iki?", "Sual üç?"],
  };

  function localProgress() {
    return {
      version: 1,
      repo: "Shadow009-dark/ai-engineer-tracker",
      startDate: "2026-10-08",
      days: {
        "12": {
          status: "partial",
          items: ["d12-t1", "d12-t2", "d12-t3", "d12-t4"],
          minutes: 180,
          note: "Groupby çətin idi",
          reflection: { learned: "Pandas groupby", hard: "merge", tomorrow: "merge təkrarı" },
        },
      },
      activity: { "2026-10-19": 4 },
      planOverrides: { removed: [], added: [], order: {} },
    };
  }

  /* ---------- tests ---------- */

  function testEncoding() {
    var text = "Əli ğşöüçı — Gün 12: Beynəlxalq Mühit 🚀";
    var round = G.base64ToUtf8(G.utf8ToBase64(text));
    assert("UTF-8/base64 round-trip (Azərbaycan hərfləri)", round === text, round);
    assert("base64 çıxışı ASCII-dir", /^[A-Za-z0-9+/=]+$/.test(G.utf8ToBase64(text)));
    var long = new Array(5000).join("salam ə ");
    assert("Böyük mətn chunked encode (>=64KB)", G.base64ToUtf8(G.utf8ToBase64(long)) === long);
  }

  function testHelpers() {
    assert("parseRepo düzgün", JSON.stringify(G.parseRepo("Shadow009-dark/ai-engineer-tracker")) ===
      JSON.stringify({ owner: "Shadow009-dark", name: "ai-engineer-tracker" }));
    assert("parseRepo URL ilə", G.parseRepo("https://github.com/Shadow009-dark/ai-engineer-tracker.git").name === "ai-engineer-tracker");
    assert("parseRepo yanlış format -> null", G.parseRepo("shadow") === null);
    assert("commit mesajı formatı",
      G.buildCommitMessage(12, 4, 5, "Pandas basics") === "Day 12: completed 4/5 tasks - Pandas basics",
      G.buildCommitMessage(12, 4, 5, "Pandas basics"));
    assert("log commit mesajı", G.buildLogCommitMessage(12, "Pandas basics", "2026-10-19").indexOf("Day 12:") === 0);
  }

  function testLogMarkdown() {
    var md = G.buildLogMarkdown(dayPlan, localProgress().days["12"], localProgress().days["12"].items);
    assert("log faylında başlıq var", md.indexOf("# Gün 12 — 2026-10-19") === 0);
    assert("log: status sətri", md.indexOf("**Status:** 🟡 Qismən (4/5 tapşırıq)") > 0, "status sətri tapılmadı");
    assert("log: vaxt qeydi", md.indexOf("**Vaxt:** 180 dəqiqə") > 0);
    assert("log: tamamlanmış tapşırıqlar [x]", (md.match(/- \[x\] /g) || []).length >= 4);
    assert("log: tamamlanmamış tapşırıq [ ]", md.indexOf("- [ ] Tapşırıq beş") > 0);
    assert("log: qeydlər bölməsi", md.indexOf("## Qeydlər") > 0 && md.indexOf("Groupby çətin idi") > 0);
    assert("log: refleksiya sualları",
      md.indexOf("Bu gün nə öyrəndim?") > 0 && md.indexOf("Nə çətin oldu?") > 0 && md.indexOf("Sabah nə edəcəm?") > 0);
  }

  function testMerge() {
    var remote = {
      repo: "Shadow009-dark/ai-engineer-tracker",
      startDate: "2026-09-01",
      days: { "12": { status: "done", items: ["d12-t1", "d12-v1"], minutes: 120, completedAt: "2026-10-19T10:00:00Z" } },
      activity: { "2026-10-19": 2, "2026-10-18": 5 },
      log: [{ at: "a", action: "x" }],
    };
    var local = localProgress();
    var merged = G.mergeProgress(remote, local);
    assert("merge: tapşırıqlar birləşir", merged.days["12"].items.join(",") === "d12-t1,d12-t2,d12-t3,d12-t4,d12-v1",
      merged.days["12"].items.join(","));
    assert("merge: daha irəli status saxlanılır (done)", merged.days["12"].status === "done", merged.days["12"].status);
    assert("merge: maksimum vaxt", merged.days["12"].minutes === 180);
    assert("merge: lokal refleksiya qorunur", merged.days["12"].reflection.hard === "merge");
    assert("merge: activity maksimum", merged.activity["2026-10-19"] === 4 && merged.activity["2026-10-18"] === 5);
    assert("merge: startDate lokal üstünlük", merged.startDate === "2026-10-08", merged.startDate);
    assert("merge: bitişiklik qorunur (lokal done)", G.mergeDayRecord({ status: "pending" }, { status: "done" }).status === "done");
    assert("merge: heç bir tamamlanmış tapşırıq itmir",
      G.mergeProgress({ days: { "5": { status: "pending", items: ["d5-t1"] } } },
        { days: { "5": { status: "pending", items: ["d5-t2"] } } }).days["5"].items.length === 2);
  }

  function testPutNewFile(server, done) {
    var client = clientFor(server, { token: "tok" });
    var path = "logs/2026-11-15.md";
    assert("fayl hələ mövcud deyil (test ön şərti)", !server.files[path]);
    client.uploadFile(path, "# Gün 39 — Azərbaycan mətni ə", "Day 39: daily log").then(function (res) {
      assert("yeni fayl yaradılır (created=true)", res.created === true);
      var put = server.calls.filter(function (c) { return c.method === "PUT"; })[0];
      assert("yeni faylda sha göndərilmir", !put.body.sha, JSON.stringify(put.body).slice(0, 80));
      assert("PUT gövdəsində branch var", put.body.branch === "main");
      assert("PUT gövdəsi base64-dir", /^[A-Za-z0-9+/=]+$/.test(put.body.content));
      assert("PUT Authorization başlığı", put.auth === "Bearer tok");
      assert("mətn düzgün yazılıb",
        G.base64ToUtf8(server.files[path].content).indexOf("Azərbaycan") > 0);
      done();
    }).catch(function (e) { assert("yeni fayl testi gözlənilməz xəta: " + e.message, false); done(); });
  }

  function testPutExistingFile(server, done) {
    var client = clientFor(server, { token: "tok" });
    var path = "logs/2026-10-19.md";
    var shaBefore = server.files[path].sha;
    var commitsBefore = server.files[path].commits;
    client.uploadFile(path, "# Gün 12 — yeniləndi", "Day 12: daily log updated").then(function (res) {
      assert("mövcud fayl yenilənir (created=false)", res.created === false);
      var puts = server.calls.filter(function (c) { return c.method === "PUT"; });
      var put = puts[puts.length - 1];
      assert("mövcud faylda sha göndərilir", !!put.body.sha, JSON.stringify(put.body.sha));
      assert("göndərilən sha update-dən əvvəlki sha-dır", put.body.sha === shaBefore,
        String(put.body.sha) + " != " + shaBefore);
      assert("commit sayı bir artır", server.files[path].commits === commitsBefore + 1,
        String(server.files[path].commits));
      done();
    }).catch(function (e) { assert("mövcud fayl testi xətası: " + e.message, false); done(); });
  }

  function testConflictRetry(server, done) {
    var client = clientFor(server, { token: "tok" });
    var putsBefore = server.calls.filter(function (c) { return c.method === "PUT"; }).length;
    // simulate someone else committing between our GET and PUT
    var realFetch = server.fetch;
    var first = true;
    var wrapped = function (url, opts) {
      if (first && opts && opts.method === "PUT") {
        first = false;
        server.files["data/progress.json"] = { sha: "shaCHANGED", content: b64("{}"), commits: 1 };
        return Promise.resolve(fakeResponse(409, { message: "sha does not match" }));
      }
      return realFetch(url, opts);
    };
    var c2 = G.createClient({
      fetchImpl: wrapped,
      storage: G.memoryStorage(),
      repo: "Shadow009-dark/ai-engineer-tracker",
      token: "tok",
    });
    c2.syncProgress(localProgress(), { message: "Day 12: completed 4/5 tasks - Pandas basics" }).then(function (res) {
      var puts = server.calls.filter(function (c) { return c.method === "PUT"; });
      assert("konflikt (409) sonra retry uğurlu olur", res.ok === true, JSON.stringify(res).slice(0, 120));
      assert("konflikt sonrası yeni sha ilə təkrar PUT edildi", puts.length >= putsBefore + 1);
      var last = puts[puts.length - 1];
      assert("retry yeni sha ilə gedib", last.body.sha === "shaCHANGED", String(last.body.sha));
      assert("progress.json commit mesajı düzgündür",
        server.files["data/progress.json"].lastMessage === "Day 12: completed 4/5 tasks - Pandas basics");
      assert("progress.json-da lokal tapşırıqlar var",
        G.base64ToUtf8(server.files["data/progress.json"].content).indexOf("d12-t4") > 0);
      done();
    }).catch(function (e) { assert("konflikt retry testi xətası: " + e.message, false); done(); });
  }

  function testOfflineQueue(server, done) {
    var client = clientFor(server, { token: "tok" });
    server.offline = true;
    client.syncProgress(localProgress(), { message: "offline" }).then(function (res) {
      assert("offline halda sıraya salınır", res.ok === false && res.queued === true, JSON.stringify(res));
      assert("növbədə 1 əməliyyat var", client.queue().length === 1);
      assert("status 'pending' göstərir", client.status().pending === 1);
      // log da offline sıraya düşür
      return client.syncLog("2026-10-19", "# Gün 12", "Day 12: daily log");
    }).then(function () {
      assert("log da növbəyə düşdü", client.queue().length === 2, JSON.stringify(client.queue().map(function (o) { return o.type; })));
      server.offline = false;
      return client.flush({ getLocalProgress: localProgress });
    }).then(function (res) {
      assert("online olanda flush növbəni boşaldır", res.ok === true && res.remaining === 0, JSON.stringify(res));
      assert("progress.json yazıldı", !!server.files["data/progress.json"]);
      assert("logs/2026-10-19.md yazıldı", !!server.files["logs/2026-10-19.md"]);
      assert("flush sonrası növbə boşdur", client.queue().length === 0);
      assert("status yenidən 'idle'", client.status().state === "idle", client.status().state);
      done();
    }).catch(function (e) { assert("offline növbə testi xətası: " + e.message, false); done(); });
  }

  function testAuthErrors(server, done) {
    var client = clientFor(server, { token: "bad" });
    server.failNext = { status: 401 };
    client.syncProgress(localProgress(), {}).then(function (res) {
      assert("401 -> auth xətası (ok=false)", res.ok === false && res.type === "auth", JSON.stringify(res));
      assert("401 halda əməliyyat növbəyə salınır", client.queue().length >= 1);
      server.failNext = { status: 403, message: "rate limit", headers: { "x-ratelimit-remaining": "0", "x-ratelimit-reset": "1800000000" } };
      return client.syncProgress(localProgress(), {});
    }).then(function (res) {
      assert("rate limit ayrıca tanınır", res.type === "rate-limit", String(res.type));
      server.reset();
      var empty = clientFor(server, {});
      return empty.testConnection();
    }).then(function (conn) {
      assert("token yoxdursa test uğursuz olur", conn.ok === false && conn.type === "no-token", JSON.stringify(conn));
      var noTok = clientFor(server, {});
      noTok.enqueue({ type: "progress" });
      return noTok.flush({});
    }).then(function (res) {
      assert("tokensiz flush 'token yoxdur' qaytarır", res.ok === false && /Token/.test(res.error || ""), JSON.stringify(res));
      assert("tokensiz flush növbəni saxlayır", res.remaining === 1, JSON.stringify(res));
      server.reset();
      var good = clientFor(server, { token: "good" });
      return good.testConnection();
    }).then(function (conn2) {
      assert("yaxşı token ilə bağlantı testi keçir", conn2.ok === true && conn2.user === "Shadow009-dark", JSON.stringify(conn2));
      done();
    }).catch(function (e) { assert("auth testi xətası: " + e.message, false); done(); });
  }

  function testSyncAll(server, done) {
    var client = clientFor(server, { token: "tok" });
    var payload = [{
      date: "2026-12-01",
      markdown: "# Gün 55 — gündəlik qeyd",
      message: "Day 55: daily log updated (2026-12-01) - Pandas basics",
    }, {
      date: "2026-12-02",
      markdown: "# Gün 56 — gündəlik qeyd",
      message: "Day 56: daily log updated (2026-12-02) - NumPy II",
    }];
    client.syncAll(localProgress(), payload, { message: "Sync all" }).then(function (res) {
      assert("syncAll progress yazdı", res.progress && res.progress.ok === true);
      assert("syncAll 2 log yazdı", res.logs.length === 2, JSON.stringify(res.logs));
      assert("hər log faylı bir commit oldu",
        server.files["logs/2026-12-01.md"].commits === 1 && server.files["logs/2026-12-02.md"].commits === 1);
      assert("log commit mesajları düzgün",
        server.files["logs/2026-12-02.md"].lastMessage.indexOf("Day 56: daily log updated") === 0);
      done();
    }).catch(function (e) { assert("syncAll testi xətası: " + e.message, false); done(); });
  }

  /* ---------- runner ---------- */

  function chain(tasks, index, done) {
    if (index >= tasks.length) return done();
    tasks[index](function () { chain(tasks, index + 1, done); });
  }

  function run() {
    var server = makeMockGithub({
      "data/progress.json": { sha: "shaPROGRESS", text: '{"version":1,"days":{},"activity":{}}' },
      "logs/2026-10-19.md": { sha: "shaLOG", text: "# köhnə qeyd" },
    });
    testEncoding();
    testHelpers();
    testLogMarkdown();
    testMerge();
    chain([
      function (next) { testPutNewFile(server, next); },
      function (next) { testPutExistingFile(server, next); },
      function (next) { testConflictRetry(server, next); },
      function (next) { testOfflineQueue(server, next); },
      function (next) { testAuthErrors(server, next); },
      function (next) { testSyncAll(server, next); },
    ], 0, function () {
      var passed = results.filter(function (r) { return r.ok; }).length;
      var failed = results.filter(function (r) { return !r.ok; });
      var list = document.getElementById("results");
      var summary = document.getElementById("summary");
      results.forEach(function (r) {
        var li = document.createElement("li");
        li.className = r.ok ? "ok" : "fail";
        li.textContent = (r.ok ? "PASS " : "FAIL ") + r.name + (r.ok ? "" : "  >>> " + r.detail);
        list.appendChild(li);
      });
      summary.textContent = failed.length === 0
        ? "HAMISI KEÇDİ: " + passed + "/" + results.length
        : "UĞURSUZ: " + passed + "/" + results.length + " keçdi, " + failed.length + " uğursuz";
      summary.className = failed.length ? "fail" : "ok";
      window.SYNC_TEST_RESULTS = { passed: passed, total: results.length, failed: failed };
      document.title = (failed.length ? "FAIL " : "PASS ") + passed + "/" + results.length;
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
  else run();
})();
