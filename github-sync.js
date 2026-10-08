/* github-sync.js — GitHub Contents API sync for the AI Engineer Tracker.
 *
 * Design notes:
 *  - The Personal Access Token lives ONLY in localStorage (key below). It is never committed.
 *  - Every write first reads the file to obtain its `sha`; the Contents API rejects an
 *    update without the current sha, so all updates go through getFile() -> putFile().
 *  - If GitHub is unreachable (offline, no token, rate limit) the operation is queued
 *    locally and replayed later by flush() — the site stays usable offline.
 *  - The module works in the browser (window/globalThis.GitHubSync) and in Node
 *    (module.exports) so the sync logic can be unit-tested with a mocked fetch.
 */
(function (root, factory) {
  var api = factory();
  if (typeof module === "object" && module.exports) module.exports = api;
  if (root) root.GitHubSync = api;
})(typeof globalThis !== "undefined" ? globalThis : this, function () {
  "use strict";

  var API = "https://api.github.com";
  var API_VERSION = "2022-11-28";
  var DEFAULT_REPO = "Shadow009-dark/ai-engineer-tracker";
  var DEFAULT_BRANCH = "main";
  var PROGRESS_PATH = "data/progress.json";
  var LOG_DIR = "logs";

  var KEYS = {
    token: "aiTracker.github.token",
    repo: "aiTracker.github.repo",
    branch: "aiTracker.github.branch",
    queue: "aiTracker.sync.queue",
    status: "aiTracker.sync.status",
  };

  /* ------------------------------------------------------------------ *
   * Base64 <-> UTF-8 (Azerbaijani characters must survive the round trip)
   * ------------------------------------------------------------------ */

  function toBytes(str) {
    if (typeof TextEncoder !== "undefined") return new TextEncoder().encode(str);
    var out = [];
    for (var i = 0; i < str.length; i++) {
      var c = str.charCodeAt(i);
      if (c < 0x80) out.push(c);
      else if (c < 0x800) out.push(0xc0 | (c >> 6), 0x80 | (c & 0x3f));
      else out.push(0xe0 | (c >> 12), 0x80 | ((c >> 6) & 0x3f), 0x80 | (c & 0x3f));
    }
    return out;
  }

  function fromBytes(bytes) {
    if (typeof TextDecoder !== "undefined") {
      var arr = bytes instanceof Uint8Array ? bytes : Uint8Array.from(bytes);
      return new TextDecoder("utf-8").decode(arr);
    }
    return String.fromCharCode.apply(null, bytes);
  }

  function b64encode(str) {
    var bytes = toBytes(str);
    if (typeof btoa === "function") {
      var binary = "";
      var chunk = 0x8000;
      for (var i = 0; i < bytes.length; i += chunk) {
        binary += String.fromCharCode.apply(null, bytes.slice(i, i + chunk));
      }
      return btoa(binary);
    }
    return Buffer.from(bytes).toString("base64"); // Node fallback
  }

  function b64decode(b64) {
    var clean = String(b64 || "").replace(/[\r\n\s]/g, "");
    if (typeof atob === "function") {
      var binary = atob(clean);
      var bytes = new Uint8Array(binary.length);
      for (var i = 0; i < binary.length; i++) bytes[i] = binary.charCodeAt(i);
      return fromBytes(bytes);
    }
    return Buffer.from(clean, "base64").toString("utf-8"); // Node fallback
  }

  function utf8ToBase64(str) {
    return b64encode(str);
  }

  function base64ToUtf8(b64) {
    return b64decode(b64);
  }

  /* ------------------------------------------------------------------ *
   * Formatting helpers (pure — easy to unit test)
   * ------------------------------------------------------------------ */

  /** "Shadow009-dark/ai-engineer-tracker" -> {owner, name} */
  function parseRepo(repo) {
    var parts = String(repo || "").trim().replace(/^https?:\/\/github\.com\//, "").replace(/\.git$/, "").split("/");
    if (parts.length < 2 || !parts[0] || !parts[1]) return null;
    return { owner: parts[0], name: parts[1] };
  }

  /** 180 -> "Day 12: completed 4/5 tasks - Pandas basics" */
  function buildCommitMessage(day, doneTasks, totalTasks, topic) {
    var n = day && typeof day === "object" ? day.day : day;
    var t = topic || (day && day.topic) || "";
    return "Day " + n + ": completed " + doneTasks + "/" + totalTasks + " tasks - " + t;
  }

  function buildLogCommitMessage(day, topic, dateIso) {
    var n = day && typeof day === "object" ? day.day : day;
    var t = topic || (day && day.topic) || "";
    return "Day " + n + ": daily log updated (" + dateIso + ") - " + t;
  }

  function statusLabel(itemStatus, doneCount, totalCount) {
    if (itemStatus === "done") return "✅ Tamamlandı (" + doneCount + "/" + totalCount + " tapşırıq)";
    if (itemStatus === "skipped") return "⏭️ Keçildi";
    if (itemStatus === "partial") return "🟡 Qismən (" + doneCount + "/" + totalCount + " tapşırıq)";
    return "⬜ Başlanmayıb (" + doneCount + "/" + totalCount + " tapşırıq)";
  }

  function checkbox(flag) {
    return flag ? "- [x] " : "- [ ] ";
  }

  /**
   * Build the Markdown body of logs/YYYY-MM-DD.md for one day.
   * dayPlan: the day object from plan.json
   * record:  the progress record for that day
   * doneIds: array of completed item ids
   */
  function buildLogMarkdown(dayPlan, record, doneIds) {
    record = record || {};
    doneIds = doneIds || [];
    var done = function (id) { return doneIds.indexOf(id) >= 0; };
    var taskIds = (dayPlan.tasks || []).map(function (_, i) { return "d" + dayPlan.day + "-t" + (i + 1); });
    var doneTasks = taskIds.filter(done).length;
    var lines = [];

    lines.push("# Gün " + dayPlan.day + " — " + dayPlan.date);
    lines.push("");
    lines.push("**Mövzu:** " + dayPlan.topic);
    lines.push("**Faza:** " + dayPlan.phaseId + ". " + dayPlan.phaseTitle);
    lines.push("**Status:** " + statusLabel(record.status, doneTasks, taskIds.length));
    lines.push("**Vaxt:** " + (record.minutes || 0) + " dəqiqə" + (record.completedAt ? " · tamamlanma: " + record.completedAt : ""));
    lines.push("");

    lines.push("## Nə öyrəndim");
    (dayPlan.learn || []).forEach(function (item) { lines.push("- " + item); });
    lines.push("");

    lines.push("## Tapşırıqlar");
    (dayPlan.tasks || []).forEach(function (task, i) {
      lines.push(checkbox(done(taskIds[i])) + task);
    });
    lines.push("");

    var videoIds = (dayPlan.videos || []).map(function (_, i) { return "d" + dayPlan.day + "-v" + (i + 1); });
    lines.push("## Videolar");
    (dayPlan.videos || []).forEach(function (v, i) {
      lines.push(checkbox(done(videoIds[i])) + v.title + " — " + v.channel + " (" + v.duration + ")" +
        (v.note ? " — " + v.note : "") + "  <" + v.url + ">");
    });
    lines.push("");

    var readIds = (dayPlan.reading || []).map(function (_, i) { return "d" + dayPlan.day + "-r" + (i + 1); });
    lines.push("## Oxu materialları");
    (dayPlan.reading || []).forEach(function (r, i) {
      lines.push(checkbox(done(readIds[i])) + r.title + " — " + r.source +
        (r.note ? " — " + r.note : "") + "  <" + r.url + ">");
    });
    lines.push("");

    lines.push("## Bilməli olduğun suallar");
    var mustIds = (dayPlan.mustKnow || []).map(function (_, i) { return "d" + dayPlan.day + "-m" + (i + 1); });
    (dayPlan.mustKnow || []).forEach(function (q, i) {
      lines.push(checkbox(done(mustIds[i])) + q);
    });
    lines.push("");

    lines.push("## Günün nəticəsi (deliverable)");
    lines.push(dayPlan.deliverable);
    lines.push("");

    if (record.note) {
      lines.push("## Qeydlər");
      lines.push(record.note);
      lines.push("");
    }

    var refl = record.reflection || {};
    lines.push("## Refleksiya");
    lines.push("- **Bu gün nə öyrəndim?** " + (refl.learned || "—"));
    lines.push("- **Nə çətin oldu?** " + (refl.hard || "—"));
    lines.push("- **Sabah nə edəcəm?** " + (refl.tomorrow || "—"));
    lines.push("");

    if (record.reschedule) {
      lines.push("> Bu günün qalan hissəsi " + record.reschedule + " tarixinə köçürüldü.");
      lines.push("");
    }
    lines.push("<sub>Avtomatik yaradıldı: AI Engineer Tracker (github-sync.js)</sub>");
    return lines.join("\n");
  }

  var STATUS_RANK = { pending: 0, partial: 1, skipped: 2, done: 3 };

  function mergeDayRecord(a, b) {
    a = a || {};
    b = b || {};
    var items = {};
    (a.items || []).concat(b.items || []).forEach(function (id) { items[id] = true; });
    var rankA = STATUS_RANK[a.status] === undefined ? 0 : STATUS_RANK[a.status];
    var rankB = STATUS_RANK[b.status] === undefined ? 0 : STATUS_RANK[b.status];
    var status = rankA >= rankB ? (a.status || "pending") : b.status;
    var reflA = a.reflection || {};
    var reflB = b.reflection || {};
    return {
      status: status,
      items: Object.keys(items).sort(),
      minutes: Math.max(a.minutes || 0, b.minutes || 0),
      completedAt: a.completedAt || b.completedAt || null,
      note: (b.note && b.note.trim()) ? b.note : (a.note || ""),
      reflection: {
        learned: reflB.learned || reflA.learned || "",
        hard: reflB.hard || reflA.hard || "",
        tomorrow: reflB.tomorrow || reflA.tomorrow || "",
      },
      reschedule: b.reschedule || a.reschedule || null,
      updatedAt: b.updatedAt || a.updatedAt || null,
    };
  }

  /** Merge remote and local progress without losing any completed item. */
  function mergeProgress(remote, local) {
    remote = remote || {};
    local = local || {};
    var out = {
      version: 1,
      repo: local.repo || remote.repo || DEFAULT_REPO,
      branch: local.branch || remote.branch || DEFAULT_BRANCH,
      startDate: local.startDate || remote.startDate || null,
      updatedAt: local.updatedAt || remote.updatedAt || null,
      days: {},
      activity: {},
      planOverrides: {
        removed: [],
        added: [],
        order: {},
      },
      sync: local.sync || remote.sync || { lastSync: null, lastError: null, pending: 0 },
      log: [],
    };
    var dayKeys = {};
    Object.keys(remote.days || {}).forEach(function (k) { dayKeys[k] = true; });
    Object.keys(local.days || {}).forEach(function (k) { dayKeys[k] = true; });
    Object.keys(dayKeys).sort(function (x, y) { return Number(x) - Number(y); }).forEach(function (k) {
      out.days[k] = mergeDayRecord((remote.days || {})[k], (local.days || {})[k]);
    });
    var dateKeys = {};
    Object.keys(remote.activity || {}).forEach(function (k) { dateKeys[k] = true; });
    Object.keys(local.activity || {}).forEach(function (k) { dateKeys[k] = true; });
    Object.keys(dateKeys).sort().forEach(function (k) {
      out.activity[k] = Math.max((remote.activity || {})[k] || 0, (local.activity || {})[k] || 0);
    });
    var removed = {};
    ((remote.planOverrides || {}).removed || []).concat((local.planOverrides || {}).removed || [])
      .forEach(function (n) { removed[n] = true; });
    out.planOverrides.removed = Object.keys(removed).map(Number).sort(function (x, y) { return x - y; });
    var added = {};
    ((remote.planOverrides || {}).added || []).concat((local.planOverrides || {}).added || [])
      .forEach(function (d) { if (d && d.topic) added[JSON.stringify(d)] = d; });
    out.planOverrides.added = Object.keys(added).map(function (k) { return added[k]; });
    out.planOverrides.order = Object.assign(
      {}, (remote.planOverrides || {}).order || {}, (local.planOverrides || {}).order || {}
    );
    var seen = {};
    ((remote.log || []).concat(local.log || [])).forEach(function (entry) {
      var key = JSON.stringify(entry);
      if (!seen[key]) { seen[key] = true; out.log.push(entry); }
    });
    out.log = out.log.slice(-500);
    return out;
  }

  /* ------------------------------------------------------------------ *
   * Storage adapters
   * ------------------------------------------------------------------ */

  function memoryStorage() {
    var data = {};
    return {
      getItem: function (k) { return Object.prototype.hasOwnProperty.call(data, k) ? data[k] : null; },
      setItem: function (k, v) { data[k] = String(v); },
      removeItem: function (k) { delete data[k]; },
    };
  }

  function defaultStorage() {
    try {
      if (typeof localStorage !== "undefined") {
        localStorage.setItem("__probe__", "1");
        localStorage.removeItem("__probe__");
        return localStorage;
      }
    } catch (e) { /* private mode or disabled */ }
    return memoryStorage();
  }

  /* ------------------------------------------------------------------ *
   * Sync client
   * ------------------------------------------------------------------ */

  function syncError(type, message, extra) {
    var err = new Error(message);
    err.type = type;
    if (extra) Object.assign(err, extra);
    return err;
  }

  function createClient(options) {
    options = options || {};
    var storage = options.storage || defaultStorage();
    var fetchImpl = options.fetchImpl || (typeof fetch !== "undefined" ? fetch.bind(globalThis) : null);
    var onStatus = options.onStatus || function () {};
    var state = {
      token: options.token !== undefined ? options.token : storage.getItem(KEYS.token),
      repo: options.repo || storage.getItem(KEYS.repo) || DEFAULT_REPO,
      branch: options.branch || storage.getItem(KEYS.branch) || DEFAULT_BRANCH,
      lastSync: null,
      lastError: null,
      syncing: false,
      requests: 0,
    };

    function readJSON(key, fallback) {
      try {
        var raw = storage.getItem(key);
        return raw ? JSON.parse(raw) : fallback;
      } catch (e) { return fallback; }
    }

    function writeJSON(key, value) {
      try { storage.setItem(key, JSON.stringify(value)); } catch (e) { /* quota */ }
    }

    function queue() { return readJSON(KEYS.queue, []); }
    function saveQueue(list) { writeJSON(KEYS.queue, list.slice(-200)); }

    function readStatus() {
      var persisted = readJSON(KEYS.status, {});
      return {
        lastSync: persisted.lastSync || null,
        lastError: persisted.lastError || null,
        pending: queue().length,
        state: options.token === undefined && !state.token && !persisted.lastSync
          ? "no-token"
          : (persisted.lastError ? "error" : (queue().length ? "pending" : "idle")),
      };
    }

    function emitStatus(extra) {
      var s = Object.assign(readStatus(), extra || {});
      s.pending = queue().length;
      if (s.lastError) s.state = s.state === "idle" ? "error" : s.state;
      writeJSON(KEYS.status, { lastSync: s.lastSync, lastError: s.lastError });
      onStatus(s);
      return s;
    }

    function setToken(token) {
      state.token = token || null;
      if (token) storage.setItem(KEYS.token, token);
      else storage.removeItem(KEYS.token);
      return emitStatus();
    }

    function setRepo(repo) {
      var parsed = parseRepo(repo);
      if (!parsed) throw syncError("config", "Repo formatı yanlışdır. Nümunə: Shadow009-dark/ai-engineer-tracker");
      state.repo = parsed.owner + "/" + parsed.name;
      storage.setItem(KEYS.repo, state.repo);
      return state.repo;
    }

    function setBranch(branch) {
      state.branch = branch || DEFAULT_BRANCH;
      storage.setItem(KEYS.branch, state.branch);
      return state.branch;
    }

    function headers() {
      var h = {
        Accept: "application/vnd.github+json",
        "X-GitHub-Api-Version": API_VERSION,
      };
      if (state.token) h.Authorization = "Bearer " + state.token;
      return h;
    }

    /** One API call with typed errors. */
    function request(path, opts) {
      opts = opts || {};
      if (!fetchImpl) return Promise.reject(syncError("offline", "fetch mövcud deyil"));
      state.requests += 1;
      return fetchImpl(API + path, {
        method: opts.method || "GET",
        headers: Object.assign(headers(), opts.headers || {}),
        body: opts.body ? JSON.stringify(opts.body) : undefined,
      }).then(function (res) {
        var remaining = res.headers && res.headers.get ? res.headers.get("x-ratelimit-remaining") : null;
        var reset = res.headers && res.headers.get ? res.headers.get("x-ratelimit-reset") : null;
        if (res.status === 204) return { status: 204, data: null };
        return res.json().catch(function () { return null; }).then(function (data) {
          if (res.ok) return { status: res.status, data: data };
          if (res.status === 401) throw syncError("auth", "Token etibarsızdır və ya vaxtı bitib (401).");
          if (res.status === 403 || res.status === 429) {
            if (remaining === "0") {
              var when = reset ? new Date(Number(reset) * 1000).toLocaleString("az-AZ") : "bir neçə dəqiqə sonra";
              throw syncError("rate-limit", "GitHub limiti bitdi. Yenidən cəhd: " + when);
            }
            throw syncError("auth", "İcazə yoxdur (403). Token-də 'Contents: Read and write' icazəsi var?");
          }
          if (res.status === 404) {
            throw syncError("not-found",
              "Repo və ya fayl tapılmadı (404): " + path +
              ". Repo adını, branch-ı və token icazəsini ('Contents: Read and write') yoxlayın.");
          }
          if (res.status === 409 || res.status === 422) {
            throw syncError("conflict", "Fayl konflikti (sha uyğun deyil).", { apiMessage: data && data.message });
          }
          throw syncError("server", "GitHub xətası (" + res.status + "): " + ((data && data.message) || ""));
        });
      }).catch(function (err) {
        if (err && err.type) throw err;
        throw syncError("offline", "İnternet bağlantısı yoxdur və ya GitHub əlçatmazdır.");
      });
    }

    /** Read a file; resolves {exists, sha, text} (missing file is not an error). */
    function getFile(path) {
      return request("/repos/" + state.repo + "/contents/" + path + "?ref=" + encodeURIComponent(state.branch))
        .then(function (res) {
          var data = res.data || {};
          var text = "";
          if (data.content) text = base64ToUtf8(data.content);
          return { exists: true, sha: data.sha, text: text, size: data.size };
        })
        .catch(function (err) {
          if (err.type === "not-found") return { exists: false, sha: null, text: "" };
          throw err;
        });
    }

    /** Create/update one file. Pass sha to update an existing file. Retries once on conflict. */
    function putFile(path, text, message, sha, attempt) {
      attempt = attempt || 0;
      var body = {
        message: message,
        content: utf8ToBase64(text),
        branch: state.branch,
      };
      if (sha) body.sha = sha;
      return request("/repos/" + state.repo + "/contents/" + path, {
        method: "PUT",
        body: body,
      }).catch(function (err) {
        if (err.type === "conflict" && attempt < 1) {
          // someone else changed the file: refetch the current sha and retry once
          return getFile(path).then(function (fresh) {
            return putFile(path, text, message, fresh.exists ? fresh.sha : null, attempt + 1);
          });
        }
        throw err;
      });
    }

    /** Upload a file with automatic sha resolution (read -> write). */
    function uploadFile(path, text, message) {
      return getFile(path).then(function (current) {
        return putFile(path, text, message, current.exists ? current.sha : null).then(function (res) {
          return { created: !current.exists, status: res.status, path: path };
        });
      });
    }

    function withToken(ok, message, extra) {
      return Object.assign({ ok: ok, message: message }, extra || {});
    }

    /** Verify the token and repository (used by the Settings page). */
    function testConnection() {
      if (!state.token) {
        return Promise.resolve(withToken(false, "Token yoxdur. Zəhmət olmasa token əlavə edin.", { type: "no-token" }));
      }
      return request("/user").then(function (res) {
        var login = res.data && res.data.login;
        return getFile(PROGRESS_PATH).then(function (file) {
          return withToken(true,
            "Bağlantı uğurludur. İstifadəçi: " + login + " · repo: " + state.repo + " · " + PROGRESS_PATH +
            (file.exists ? " tapıldı." : " hələ yoxdur (ilk sync yaradacaq)."),
            { user: login, hasProgress: file.exists });
        });
      }).catch(function (err) {
        return withToken(false, err.message, { type: err.type });
      });
    }

    /** Push progress.json and (optionally) one day log; queue on failure. */
    function syncProgress(localProgress, meta) {
      meta = meta || {};
      var payload = JSON.stringify(localProgress, null, 2) + "\n";
      var message = meta.message || "Progress yeniləndi (" + new Date().toISOString().slice(0, 10) + ")";
      emitStatus({ state: "syncing" });
      return getFile(PROGRESS_PATH).then(function (current) {
        var remote = {};
        try { remote = current.text ? JSON.parse(current.text) : {}; } catch (e) { remote = {}; }
        var merged = mergeProgress(remote, localProgress);
        merged.updatedAt = new Date().toISOString();
        merged.sync = Object.assign({}, merged.sync, {
          lastSync: new Date().toISOString(),
          lastError: null,
          pending: queue().length,
        });
        var body = JSON.stringify(merged, null, 2) + "\n";
        return putFile(PROGRESS_PATH, body, message, current.exists ? current.sha : null).then(function (res) {
          state.lastSync = new Date().toISOString();
          state.lastError = null;
          emitStatus({ state: queue().length ? "pending" : "idle", lastSync: state.lastSync, lastError: null });
          return { ok: true, created: !current.exists, merged: merged, status: res.status };
        });
      }).catch(function (err) {
        enqueue({ type: "progress" });
        state.lastError = err.message;
        emitStatus({ state: err.type === "auth" ? "error" : "offline", lastError: err.message });
        return { ok: false, queued: true, error: err.message, type: err.type };
      });
    }

    function logPath(dateIso) { return LOG_DIR + "/" + dateIso + ".md"; }

    /** Push one logs/YYYY-MM-DD.md file. */
    function syncLog(dateIso, markdown, message) {
      emitStatus({ state: "syncing" });
      var path = logPath(dateIso);
      return getFile(path).then(function (current) {
        return putFile(path, markdown, message || ("Gündəlik qeyd: " + dateIso), current.exists ? current.sha : null)
          .then(function (res) {
            state.lastSync = new Date().toISOString();
            emitStatus({ state: queue().length ? "pending" : "idle", lastSync: state.lastSync, lastError: null });
            return { ok: true, created: !current.exists, status: res.status, path: path };
          });
      }).catch(function (err) {
        enqueue({ type: "log", date: dateIso, markdown: markdown, message: message });
        emitStatus({ state: err.type === "auth" ? "error" : "offline", lastError: err.message });
        return { ok: false, queued: true, error: err.message, type: err.type };
      });
    }

    /** Push everything: progress.json + one log file per recorded day. */
    function syncAll(localProgress, dayPayloads, meta) {
      meta = meta || {};
      var results = { progress: null, logs: [], failed: [] };
      return syncProgress(localProgress, { message: meta.message }).then(function (pr) {
        results.progress = pr;
        if (!pr.ok) {
          (dayPayloads || []).forEach(function (p) {
            enqueue({ type: "log", date: p.date, markdown: p.markdown, message: p.message });
          });
          return results;
        }
        var chain = Promise.resolve();
        (dayPayloads || []).forEach(function (p) {
          chain = chain.then(function () {
            return syncLog(p.date, p.markdown, p.message).then(function (r) {
              if (r.ok) results.logs.push(r.path);
              else results.failed.push({ date: p.date, error: r.error });
            });
          });
        });
        return chain.then(function () { return results; });
      });
    }

    /* --------------- offline queue --------------- */

    function enqueue(op) {
      var list = queue();
      var key = op.type === "log" ? "log:" + op.date : "progress";
      list = list.filter(function (o) {
        return (o.type === "log" ? "log:" + o.date : "progress") !== key;
      });
      list.push(Object.assign({ createdAt: new Date().toISOString() }, op));
      saveQueue(list);
      return list.length;
    }

    function flush(handlers) {
      handlers = handlers || {};
      var list = queue();
      if (!list.length) {
        return Promise.resolve({ ok: true, processed: 0, remaining: 0 });
      }
      if (!state.token) {
        emitStatus({ state: "no-token", lastError: null });
        return Promise.resolve({ ok: false, processed: 0, remaining: list.length, error: "Token yoxdur." });
      }
      var processed = 0;
      var remaining = list.slice();
      var chain = Promise.resolve();
      list.forEach(function (op) {
        chain = chain.then(function () {
          if (!remaining.length) return null;
          if (op.type === "log") {
            if (!op.markdown) { remaining.shift(); processed += 1; return null; }
            return getFile(logPath(op.date))
              .then(function (cur) {
                return putFile(logPath(op.date), op.markdown, op.message || ("Gündəlik qeyd: " + op.date),
                  cur.exists ? cur.sha : null);
              })
              .then(function () {
                remaining.shift();
                processed += 1;
                saveQueue(remaining);
              })
              .catch(function (err) {
                if (err.type === "offline" || err.type === "rate-limit") throw err;
                remaining.shift(); // auth/conflict errors would repeat forever: drop the op
                saveQueue(remaining);
                throw err;
              });
          }
          return getFile(PROGRESS_PATH).then(function (cur) {
            var remote = {};
            try { remote = cur.text ? JSON.parse(cur.text) : {}; } catch (e) { remote = {}; }
            var local = handlers.getLocalProgress ? handlers.getLocalProgress() : {};
            var merged = mergeProgress(remote, local);
            merged.updatedAt = new Date().toISOString();
            return putFile(PROGRESS_PATH, JSON.stringify(merged, null, 2) + "\n",
              op.message || "Progress sinxronlaşdırıldı", cur.exists ? cur.sha : null);
          }).then(function () {
            remaining.shift();
            processed += 1;
            saveQueue(remaining);
          }).catch(function (err) {
            if (err.type === "offline" || err.type === "rate-limit") throw err;
            remaining.shift();
            saveQueue(remaining);
            throw err;
          });
        });
      });
      return chain.then(function () {
        state.lastSync = new Date().toISOString();
        return emitStatus({ state: remaining.length ? "pending" : "idle", lastSync: state.lastSync, lastError: null });
      }).then(function () {
        if (handlers.onFlushed) handlers.onFlushed(processed);
        return { ok: remaining.length === 0, processed: processed, remaining: remaining.length };
      }).catch(function (err) {
        emitStatus({ state: "offline", lastError: err.message });
        return { ok: false, processed: processed, remaining: remaining.length, error: err.message, type: err.type };
      });
    }

    return {
      KEYS: KEYS,
      PROGRESS_PATH: PROGRESS_PATH,
      get repo() { return state.repo; },
      get branch() { return state.branch; },
      get token() { return state.token; },
      setToken: setToken,
      setRepo: setRepo,
      setBranch: setBranch,
      status: readStatus,
      emitStatus: emitStatus,
      request: request,
      getFile: getFile,
      putFile: putFile,
      uploadFile: uploadFile,
      testConnection: testConnection,
      syncProgress: syncProgress,
      syncLog: syncLog,
      syncAll: syncAll,
      enqueue: enqueue,
      queue: queue,
      saveQueue: saveQueue,
      flush: flush,
      logPath: logPath,
    };
  }

  return {
    KEYS: KEYS,
    API: API,
    DEFAULT_REPO: DEFAULT_REPO,
    DEFAULT_BRANCH: DEFAULT_BRANCH,
    PROGRESS_PATH: PROGRESS_PATH,
    LOG_DIR: LOG_DIR,
    createClient: createClient,
    memoryStorage: memoryStorage,
    utf8ToBase64: utf8ToBase64,
    base64ToUtf8: base64ToUtf8,
    parseRepo: parseRepo,
    buildCommitMessage: buildCommitMessage,
    buildLogCommitMessage: buildLogCommitMessage,
    buildLogMarkdown: buildLogMarkdown,
    mergeProgress: mergeProgress,
    mergeDayRecord: mergeDayRecord,
    statusLabel: statusLabel,
  };
});
