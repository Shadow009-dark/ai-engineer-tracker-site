/* app.js — AI Engineer Tracker (vanilla JS, no build step)
 *
 * Sections:
 *   1. Small utilities (DOM, dates, text)
 *   2. State + plan/progress models
 *   3. Statistics (streak, percentages, weekly/monthly)
 *   4. Renderers (dashboard, plan, calendar, stats, mentor, settings)
 *   5. Actions (mark tasks, skip, reschedule, notes, reflection, plan editing)
 *   6. Charts (canvas) and heatmap
 *   7. GitHub sync (via github-sync.js)
 *   8. Keyboard shortcuts and init
 */
(function () {
  "use strict";

  var SYNC = window.GitHubSync;

  var KEYS = {
    progress: "aiTracker.progress.v1",
    plan: "aiTracker.plan.edited.v1",
    settings: "aiTracker.settings.v1",
    theme: "aiTracker.theme.v1",
    mentor: "aiTracker.mentor.cache",
  };

  var AZ_MONTHS = ["yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul",
    "avqust", "sentyabr", "oktyabr", "noyabr", "dekabr"];
  var AZ_DAYS = ["bazar", "bazar ertəsi", "çərşənbə axşamı", "çərşənbə",
    "cümə axşamı", "cümə", "şənbə"];
  var WEEKDAY_SHORT = ["B.e", "Ç.a", "Ç", "C.a", "C", "Ş", "B"];

  /* ================================================================== *
   * 1. Utilities
   * ================================================================== */

  function $(sel, root) { return (root || document).querySelector(sel); }
  function $$(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }

  var esc = function (s) {
    return String(s === undefined || s === null ? "" : s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;").replace(/'/g, "&#39;");
  };

  var clamp = function (v, a, b) { return Math.max(a, Math.min(b, v)); };

  function todayISO() {
    var d = new Date();
    var m = String(d.getMonth() + 1).padStart(2, "0");
    var day = String(d.getDate()).padStart(2, "0");
    return d.getFullYear() + "-" + m + "-" + day;
  }

  function parseISO(iso) {
    var p = String(iso || "").split("-");
    return new Date(Date.UTC(Number(p[0]), Number(p[1]) - 1, Number(p[2])));
  }

  function toISO(date) {
    var m = String(date.getUTCMonth() + 1).padStart(2, "0");
    var d = String(date.getUTCDate()).padStart(2, "0");
    return date.getUTCFullYear() + "-" + m + "-" + d;
  }

  function addDays(iso, n) {
    var d = parseISO(iso);
    d.setUTCDate(d.getUTCDate() + n);
    return toISO(d);
  }

  function daysBetween(a, b) {
    return Math.round((parseISO(b) - parseISO(a)) / 86400000);
  }

  function weekdayMon(iso) { var w = parseISO(iso).getUTCDay(); return w === 0 ? 7 : w; }

  function formatAZ(iso, withWeekday) {
    var d = parseISO(iso);
    var s = d.getUTCDate() + " " + AZ_MONTHS[d.getUTCMonth()] + " " + d.getUTCFullYear();
    if (withWeekday) s += ", " + AZ_DAYS[d.getUTCDay()];
    return s;
  }

  function weekStart(iso) { return addDays(iso, -(weekdayMon(iso) - 1)); }

  function weekOfPlan(iso, startDate) {
    return Math.floor(daysBetween(startDate, iso) / 7) + 1;
  }

  function readJSON(key, fallback) {
    try {
      var raw = localStorage.getItem(key);
      return raw ? JSON.parse(raw) : fallback;
    } catch (e) { return fallback; }
  }

  function writeJSON(key, value) {
    try { localStorage.setItem(key, JSON.stringify(value)); return true; }
    catch (e) { toast("Yaddaşa yazmaq mümkün olmadı (localStorage dolu?).", "err"); return false; }
  }

  var toastTimer = null;
  function toast(msg, kind) {
    var el = $("#toast");
    el.textContent = msg;
    el.className = "toast " + (kind || "");
    el.hidden = false;
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { el.hidden = true; }, kind === "err" ? 6000 : 3200);
  }

  function download(filename, text, mime) {
    var blob = new Blob([text], { type: (mime || "text/plain") + ";charset=utf-8" });
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    setTimeout(function () { URL.revokeObjectURL(url); }, 1500);
  }

  /* ================================================================== *
   * 2. State and models
   * ================================================================== */

  var S = {
    plan: null,
    days: [],          // planlaşdırılmış günlər (override-lar tətbiq olunmuş)
    progress: null,
    settings: { startDate: null, dailyMinutes: 180, name: "" },
    view: "dashboard",
    planEdit: false,
    calendarMonth: null,
    mentor: null,
    filters: { q: "", phase: "", status: "", type: "" },
    saveTimer: null,
  };

  function blankRecord() {
    return {
      status: "pending",
      items: [],
      minutes: 0,
      note: "",
      reflection: { learned: "", hard: "", tomorrow: "" },
      completedAt: null,
      reschedule: null,
      lastDate: null,
      updatedAt: null,
    };
  }

  function blankProgress() {
    return {
      version: 1,
      repo: SYNC.DEFAULT_REPO,
      branch: SYNC.DEFAULT_BRANCH,
      startDate: null,
      updatedAt: null,
      days: {},
      activity: {},
      planOverrides: { removed: [], patched: {}, added: [], order: {} },
      sync: { lastSync: null, lastError: null, pending: 0 },
      log: [],
    };
  }

  function rec(dayNo) { return S.progress.days[String(dayNo)] || blankRecord(); }

  function ensureRec(dayNo) {
    var key = String(dayNo);
    if (!S.progress.days[key]) S.progress.days[key] = blankRecord();
    return S.progress.days[key];
  }

  function startDate() {
    return S.settings.startDate || (S.progress && S.progress.startDate) ||
      (S.plan && S.plan.meta && S.plan.meta.startDate) || todayISO();
  }

  /** All plan days with overrides applied, sorted by their order index. */
  function buildDays() {
    if (!S.plan) { S.days = []; return; }
    var ov = S.progress.planOverrides || { removed: [], patched: {}, added: [], order: {} };
    var removed = {};
    (ov.removed || []).forEach(function (n) { removed[String(n)] = true; });

    var all = [];
    var index = 0;
    S.plan.phases.forEach(function (phase) {
      (phase.days || []).forEach(function (d) {
        index += 1;
        if (removed[String(d.id)]) return;
        var patch = (ov.patched || {})[d.id];
        var day = Object.assign({}, d, patch || {});
        day._order = (ov.order && ov.order[d.id]) || index;
        day._sortKey = day._order;
        all.push(day);
      });
    });
    (ov.added || []).forEach(function (d, i) {
      var day = Object.assign({}, d);
      day._order = (ov.order && ov.order[d.id]) || (index + i + 1);
      day._sortKey = day._order;
      all.push(day);
    });
    all.sort(function (a, b) { return a._sortKey - b._sortKey; });

    var sd = startDate();
    S.days = all.map(function (d) {
      var planned = addDays(sd, d._sortKey - 1);
      var record = S.progress.days[String(d.day)] || null;
      return Object.assign({}, d, {
        plannedDate: planned,
        date: planned,
        effectiveDate: (record && record.reschedule) || planned,
      });
    });
  }

  function dayByNumber(n) {
    for (var i = 0; i < S.days.length; i++) if (S.days[i].day === n) return S.days[i];
    return null;
  }

  function itemIds(day, kind) {
    var list, prefix;
    if (kind === "t") { list = day.tasks || []; prefix = "t"; }
    else if (kind === "v") { list = day.videos || []; prefix = "v"; }
    else if (kind === "r") { list = day.reading || []; prefix = "r"; }
    else { list = day.mustKnow || []; prefix = "m"; }
    var out = [];
    for (var i = 0; i < list.length; i++) out.push("d" + day.day + "-" + prefix + (i + 1));
    return out;
  }

  function allItemIds(day) {
    return itemIds(day, "t").concat(itemIds(day, "v"), itemIds(day, "r"), itemIds(day, "m"));
  }

  function isDone(dayNo, id) {
    var r = S.progress.days[String(dayNo)];
    return !!(r && r.items && r.items.indexOf(id) >= 0);
  }

  function computeStatus(record, day) {
    var ids = allItemIds(day);
    var done = ids.filter(function (id) { return record.items.indexOf(id) >= 0; }).length;
    if (record.status === "skipped" && done === 0) return "skipped";
    if (ids.length && done === ids.length) return "done";
    if (done > 0) return "partial";
    return record.status === "skipped" ? "skipped" : "pending";
  }

  function dayStats(day) {
    var record = rec(day.day);
    var ids = allItemIds(day);
    var done = ids.filter(function (id) { return record.items.indexOf(id) >= 0; }).length;
    var taskIds = itemIds(day, "t");
    var doneTasks = taskIds.filter(function (id) { return record.items.indexOf(id) >= 0; }).length;
    return {
      ids: ids,
      done: done,
      total: ids.length,
      percent: ids.length ? Math.round((done / ids.length) * 100) : 0,
      doneTasks: doneTasks,
      totalTasks: taskIds.length,
      status: computeStatus(record, day),
      record: record,
      isOverdue: day.effectiveDate < todayISO() && ["pending", "partial"].indexOf(computeStatus(record, day)) >= 0,
    };
  }

  /** Calendar status of a day: done|partial|missed|upcoming|skipped. */
  function calendarStatus(day, todayIso) {
    var st = dayStats(day);
    if (st.status === "done") return "done";
    if (day.effectiveDate === todayIso) return st.status === "skipped" ? "skipped" : "partial";
    if (day.effectiveDate < todayIso) return st.status === "skipped" || st.status === "done" ? st.status : "missed";
    return st.status === "skipped" ? "skipped" : "upcoming";
  }

  /* ================================================================== *
   * 3. Statistika
   * ================================================================== */

  function stats() {
    var todayIso = todayISO();
    var totalItems = 0, doneItems = 0, totalMinutes = 0, doneDays = 0, skippedDays = 0;
    S.days.forEach(function (day) {
      var st = dayStats(day);
      totalItems += st.total;
      doneItems += st.done;
      totalMinutes += st.record.minutes || 0;
      if (st.status === "done") doneDays += 1;
      if (st.status === "skipped") skippedDays += 1;
    });

    var pick = pickFocusDay(todayIso);
    var focusDay = pick.day;
    var focusIsToday = pick.isToday;

    var todayLeft = focusDay ? dayStats(focusDay).total - dayStats(focusDay).done : 0;
    if (focusDay && !focusIsToday) todayLeft = 0;

    var ws = weekStart(todayIso), weekEnd = addDays(ws, 6);
    var weekLeft = 0;
    S.days.forEach(function (day) {
      if (day.effectiveDate >= ws && day.effectiveDate <= weekEnd) {
        var st = dayStats(day);
        weekLeft += st.total - st.done;
      }
    });

    var overdue = S.days.filter(function (d) { return dayStats(d).isOverdue; });

    return {
      todayIso: todayIso,
      focusDay: focusDay,
      focusIsToday: focusIsToday,
      todayLeft: todayLeft,
      weekLeft: weekLeft,
      overdue: overdue,
      totalItems: totalItems,
      doneItems: doneItems,
      overallPct: totalItems ? Math.round((doneItems / totalItems) * 100) : 0,
      overallPctLabel: totalItems
        ? (doneItems > 0 && doneItems / totalItems < 0.01 ? "<1%" : Math.round((doneItems / totalItems) * 100) + "%")
        : "0%",
      totalMinutes: totalMinutes,
      doneDays: doneDays,
      skippedDays: skippedDays,
      remainingItems: totalItems - doneItems,
      streak: streak(),
      phaseStats: phaseStats(),
    };
  }

  /**
   * Pick the focus day for "today":
   *   1) a day scheduled (or rescheduled) for today, preferring unfinished ones;
   *   2) the nearest unfinished day after today (by date, not by array position);
   *   3) otherwise the last day of the plan.
   */
  function pickFocusDay(todayIso) {
    var isPending = function (d) {
      var s = dayStats(d).status;
      return s !== "done" && s !== "skipped";
    };
    var byDate = function (a, b) {
      if (a.effectiveDate !== b.effectiveDate) return a.effectiveDate < b.effectiveDate ? -1 : 1;
      return a.day - b.day;
    };
    var todays = S.days.filter(function (d) { return d.effectiveDate === todayIso; });
    if (todays.length) return { day: todays.filter(isPending)[0] || todays[0], isToday: true };

    var future = S.days.filter(function (d) { return d.effectiveDate > todayIso; }).sort(byDate);
    if (future.length) return { day: future.filter(isPending)[0] || future[0], isToday: false };

    var past = S.days.filter(function (d) { return d.effectiveDate <= todayIso; }).sort(byDate);
    var lastPending = past.filter(isPending);
    return {
      day: lastPending.length ? lastPending[0] : (past[past.length - 1] || S.days[S.days.length - 1] || null),
      isToday: false,
    };
  }

  function activityLevel(count) {
    if (!count) return 0;
    if (count <= 2) return 1;
    if (count <= 5) return 2;
    if (count <= 9) return 3;
    return 4;
  }

  function streak() {
    var act = S.progress.activity || {};
    var cur = todayISO();
    var count = 0;
    if (!act[cur]) cur = addDays(cur, -1);
    while (act[cur] && act[cur] > 0) {
      count += 1;
      cur = addDays(cur, -1);
    }
    return count;
  }

  function phaseStats() {
    var byPhase = {};
    S.days.forEach(function (day) {
      var key = day.phaseId;
      if (!byPhase[key]) byPhase[key] = { id: key, title: day.phaseTitle, done: 0, total: 0, days: 0, doneDays: 0 };
      var st = dayStats(day);
      byPhase[key].done += st.done;
      byPhase[key].total += st.total;
      byPhase[key].days += 1;
      if (st.status === "done") byPhase[key].doneDays += 1;
    });
    return Object.keys(byPhase).sort(function (a, b) { return Number(a) - Number(b); })
      .map(function (k) {
        var p = byPhase[k];
        p.percent = p.total ? Math.round((p.done / p.total) * 100) : 0;
        return p;
      });
  }

  /** All "must know" questions scheduled up to a given date. */
  function cumulativeMustKnow(limitIso) {
    var out = [];
    var todayIso = limitIso || todayISO();
    S.days.forEach(function (day) {
      if (day.effectiveDate > todayIso) return;
      var ids = itemIds(day, "m");
      (day.mustKnow || []).forEach(function (q, i) {
        out.push({ day: day, id: ids[i], text: q, done: isDone(day.day, ids[i]) });
      });
    });
    return out;
  }

  /* ================================================================== *
   * 4. Render
   * ================================================================== */

  function statusBadgeText(status) {
    return { done: "✅ Tamamlandı", partial: "🟡 Qismən", pending: "⬜ Başlanmayıb", skipped: "⏭️ Keçildi" }[status] || status;
  }

  function progressBar(percent, extraClass) {
    return '<div class="bar ' + (extraClass || "") + '"><i style="width:' + clamp(percent, 0, 100) + '%"></i></div>';
  }

  function itemHTML(id, text, done, meta) {
    return '<label class="item' + (done ? " done" : "") + '" data-item="' + esc(id) + '">' +
      '<input type="checkbox" data-check="' + esc(id) + '"' + (done ? " checked" : "") + ' />' +
      '<span class="item-text">' + esc(text) + (meta ? '<span class="item-meta">' + meta + "</span>" : "") + "</span>" +
      "</label>";
  }

  function linkItemHTML(id, entry, done, kind) {
    var badge = kind === "v"
      ? '<span class="badge video">' + esc(entry.channel || "video") + " · " + esc(entry.duration || "") + "</span>"
      : '<span class="badge read">' + esc(entry.source || "") + "</span>";
    // AZ note explains what this English resource gives you
    var note = entry.note ? '<span class="item-meta">🇦🇿 ' + esc(entry.note) + "</span>" : "";
    return '<div class="link-item' + (done ? " done" : "") + '">' +
      '<input type="checkbox" data-check="' + esc(id) + '"' + (done ? " checked" : "") + " />" +
      "<div style=\"flex:1\"><a href=\"" + esc(entry.url) + "\" target=\"_blank\" rel=\"noopener noreferrer\">" +
      esc(entry.title) + "</a> " + badge + note + "</div></div>";
  }

  function dayBodyHTML(day, opts) {
    opts = opts || {};
    var st = dayStats(day);
    var tIds = itemIds(day, "t"), vIds = itemIds(day, "v");
    var rIds = itemIds(day, "r"), mIds = itemIds(day, "m");
    var html = "";

    html += '<div class="row-between"><span class="pill">' + statusBadgeText(st.status) +
      " · " + st.done + "/" + st.total + " element</span>" +
      '<span class="pill">⏱️ ' + (st.record.minutes || day.minutes) + " dəqiqə</span>" +
      '<span class="pill">📅 ' + esc(day.effectiveDate) + "</span>" +
      '<span class="pill">Faza ' + day.phaseId + "</span></div>";
    html += progressBar(st.percent, "wide");

    if (day._custom) html += '<div class="note-box">✏️ Bu gün sizin əlavə etdiyiniz xüsusi gündür.</div>';

    html += '<div><div class="day-section-title">Nə öyrənməliyəm</div><ul class="learn-list">';
    (day.learn || []).forEach(function (l) { html += "<li>" + esc(l) + "</li>"; });
    html += "</ul></div>";

    html += '<div><div class="day-section-title">Günün tapşırıqları (' +
      st.doneTasks + "/" + st.totalTasks + ")</div><div class=\"list-body\">";
    (day.tasks || []).forEach(function (task, i) {
      html += itemHTML(tIds[i], task, isDone(day.day, tIds[i]));
    });
    html += "</div></div>";

    html += '<div><div class="day-section-title">Videolar (' + (day.videos || []).length +
      ")</div><div class=\"link-list\">";
    (day.videos || []).forEach(function (v, i) {
      html += linkItemHTML(vIds[i], v, isDone(day.day, vIds[i]), "v");
    });
    html += "</div></div>";

    html += '<div><div class="day-section-title">Oxu materialları (' + (day.reading || []).length +
      ")</div><div class=\"link-list\">";
    (day.reading || []).forEach(function (r, i) {
      html += linkItemHTML(rIds[i], r, isDone(day.day, rIds[i]), "r");
    });
    html += "</div></div>";

    html += '<div class="note-box"><b>🎯 Günün nəticəsi:</b> ' + esc(day.deliverable || "—") + "</div>";

    html += '<div><div class="day-section-title">Bilməli olduğum suallar</div><div class="list-body">';
    (day.mustKnow || []).forEach(function (q, i) {
      html += itemHTML(mIds[i], q, isDone(day.day, mIds[i]));
    });
    html += "</div></div>";

    if (!opts.compact) {
      html += '<div><div class="day-section-title">Qeydlər</div>' +
        '<textarea id="day-note" rows="3" placeholder="Bu günlə bağlı qeydlər, linklər, fikirlər...">' +
        esc(st.record.note || "") + "</textarea>" +
        '<div class="row-between" style="margin-top:6px"><span class="muted small">Qeyd progress.json-a və log faylına düşür.</span>' +
        '<button class="btn btn-primary btn-sm" id="btn-save-note" type="button">💾 Qeydi saxla</button></div></div>';

      html += '<div class="row-between"><span class="muted small">Klaviatura: <kbd>D</kbd> tapşırıq, <kbd>S</kbd> keç, <kbd>R</kbd> köçür, <kbd>N</kbd> qeyd</span>' +
        '<button class="btn btn-ghost btn-sm" data-day-action="open" data-day="' + day.day + '" type="button">🔎 Tam günü aç</button></div>';
    }
    return html;
  }

  function renderDashboard() {
    var st = stats();
    var day = st.focusDay;

    if (!day) {
      $("#hero-topic").textContent = "Plan yüklənməyib";
      $("#hero-day").textContent = "—";
      $("#today-body").innerHTML = '<div class="empty">Plan faylı yüklənə bilmədi. ' +
        "Layihəni `python -m http.server` ilə açın və ya GitHub Pages-də yerləşdirin.</div>";
      return;
    }

    $("#hero-day").textContent = "Gün " + day.day + "/" + (S.plan ? S.plan.meta.totalDays : 180) +
      (st.focusIsToday ? "" : " (növbəti)");
    $("#hero-topic").textContent = day.topic;
    $("#hero-date").textContent = "📅 " + formatAZ(day.effectiveDate, true);
    $("#hero-phase").textContent = "Faza " + day.phaseId + ": " + day.phaseTitle;
    $("#hero-type").textContent = day.type === "review" ? "🔁 Təkrar günü" : "📘 Öyrənmə günü";
    $("#hero-minutes").textContent = "⏱️ " + day.minutes + " dəq";
    var dstats = dayStats(day);
    $("#today-pct").textContent = dstats.percent + "%";
    $("#today-ring").style.setProperty("--p", dstats.percent);

    $("#stat-streak").textContent = st.streak;
    $("#stat-done-days").textContent = st.doneDays;
    $("#stat-overall").textContent = st.overallPctLabel;
    $("#stat-today-left").textContent = st.todayLeft;
    $("#stat-week-left").textContent = st.weekLeft;
    $("#stat-hours").textContent = Math.round(st.totalMinutes / 60);

    $("#today-body").innerHTML = dayBodyHTML(day);

    // overdue days
    $("#overdue-count").textContent = st.overdue.length;
    if (!st.overdue.length) {
      $("#overdue-body").innerHTML = '<div class="empty">Gecikmiş tapşırıq yoxdur — əla gedişat! 🎉</div>';
    } else {
      $("#overdue-body").innerHTML = st.overdue.map(function (d) {
        var s = dayStats(d);
        var late = daysBetween(d.effectiveDate, todayISO());
        return '<div class="row-between" style="border-bottom:1px dashed var(--border);padding-bottom:6px">' +
          '<div><b>Gün ' + d.day + "</b> — " + esc(d.topic) +
          '<div class="item-meta">' + formatAZ(d.effectiveDate) + " · " + late + " gün gecikmə · " +
          s.done + "/" + s.total + " element</div></div>" +
          '<div class="item-actions">' +
          '<button class="btn btn-ghost btn-sm" data-day-action="open" data-day="' + d.day + '" type="button">Aç</button>' +
          '<button class="btn btn-primary btn-sm" data-day-action="reschedule" data-day="' + d.day + '" type="button">📆 Köçür</button>' +
          "</div></div>";
      }).join("");
    }

    // cumulative must know
    var mk = cumulativeMustKnow();
    $("#mustknow-count").textContent = mk.filter(function (m) { return !m.done; }).length + " açıq";
    $("#mustknow-body").innerHTML = mk.length
      ? mk.slice().reverse().map(function (m) {
        return itemHTML(m.id, m.text, m.done, "Gün " + m.day.day + " · " + esc(m.day.topic.slice(0, 42)));
      }).join("")
      : '<div class="empty">Hələ keçmiş gün yoxdur.</div>';

    // refleksiya
    var refl = dstats.record.reflection || {};
    $("#refl-learned").value = refl.learned || "";
    $("#refl-hard").value = refl.hard || "";
    $("#refl-tomorrow").value = refl.tomorrow || "";
    $("#refl-status").textContent = "Refleksiya Gün " + day.day + " üçün saxlanılır və logs/" + todayISO() + ".md faylına göndərilir.";

    $("#tip-text").textContent = weeklyTip();

    renderPhaseBars($("#phase-bars"));
    drawCharts();
    renderHeatmap($("#heatmap"));

    $("#btn-day-done").disabled = false;
    $("#btn-day-skip").disabled = false;
    $("#btn-day-reschedule").disabled = false;
  }

  function weeklyTip() {
    var tips = (S.mentor && S.mentor.weeklyTips) || [];
    if (!tips.length) return "Mentor məsləhətləri yüklənir...";
    var idx = Math.abs(weekOfPlan(todayISO(), startDate()) - 1) % tips.length;
    return tips[idx];
  }

  function renderPhaseBars(container) {
    if (!container) return;
    var list = stats().phaseStats;
    container.innerHTML = list.map(function (p) {
      return '<div class="phase-row"><div class="phase-row-top"><b>Faza ' + p.id + ": " + esc(p.title) +
        "</b><span>" + p.done + "/" + p.total + " element · " + p.doneDays + "/" + p.days + " gün · " + p.percent + "%</span></div>" +
        progressBar(p.percent) + "</div>";
    }).join("");
  }

  function renderPlan() {
    var phases = S.plan ? S.plan.phases : [];
    var sel = $("#filter-phase");
    if (sel && sel.options.length <= 1) {
      phases.forEach(function (p) {
        var o = document.createElement("option");
        o.value = String(p.id);
        o.textContent = "Faza " + p.id + ": " + p.title;
        sel.appendChild(o);
      });
    }

    var f = S.filters;
    var q = f.q.trim().toLowerCase();
    var results = S.days.filter(function (day) {
      var st = dayStats(day);
      if (f.phase && String(day.phaseId) !== String(f.phase)) return false;
      if (f.type && day.type !== f.type) return false;
      if (f.status) {
        if (f.status === "overdue") { if (!st.isOverdue) return false; }
        else if (st.status !== f.status) return false;
      }
      if (q) {
        var hay = [day.topic, day.phaseTitle, day.deliverable, (day.learn || []).join(" "),
          (day.tasks || []).join(" "), (day.mustKnow || []).join(" "),
          (day.videos || []).map(function (v) { return v.title + " " + v.channel; }).join(" ")]
          .join(" ").toLowerCase();
        if (hay.indexOf(q) < 0) return false;
      }
      return true;
    });

    $("#plan-count").textContent = results.length + " gün göstərilir (cəmi " + S.days.length + ")";
    $("#plan-list").innerHTML = results.length ? results.map(function (day) {
      var st = dayStats(day);
      return '<article class="plan-day" data-day-card="' + day.day + '">' +
        '<div class="plan-day-head">' +
        '<div class="plan-day-title"><b>Gün ' + day.day + "</b><span>" + esc(day.topic) + "</span></div>" +
        '<div class="plan-day-meta">' +
        '<span class="pill">' + formatAZ(day.effectiveDate) + "</span>" +
        '<span class="pill">' + statusBadgeText(st.status) + "</span>" +
        '<span class="pill">Faza ' + day.phaseId + "</span>" +
        (st.isOverdue ? '<span class="pill" style="border-color:var(--danger);color:var(--danger)">Gecikmiş</span>' : "") +
        '<span class="mini-bar">' + progressBar(st.percent) + "</span>" +
        '<button class="btn btn-ghost btn-sm" data-plan-toggle="' + day.day + '" type="button">Aç/bağla</button>' +
        (S.planEdit ? '<button class="btn btn-ghost btn-sm" data-plan-edit="' + day.day + '" type="button">✏️</button>' +
          '<button class="btn btn-ghost btn-sm" data-plan-up="' + day.day + '" type="button">↑</button>' +
          '<button class="btn btn-ghost btn-sm" data-plan-down="' + day.day + '" type="button">↓</button>' +
          '<button class="btn btn-danger btn-sm" data-plan-del="' + day.day + '" type="button">🗑️</button>' : "") +
        "</div></div>" +
        '<div class="plan-day-body">' + dayBodyHTML(day, { compact: true }) +
        '<div class="row-wrap"><button class="btn btn-primary btn-sm" data-day-action="open" data-day="' + day.day + '" type="button">Tam günü aç və işarələ</button></div>' +
        "</div></article>";
    }).join("") : '<div class="empty">Axtarışa uyğun gün tapılmadı.</div>';
  }

  function renderCalendar() {
    var todayIso = todayISO();
    if (!S.calendarMonth) {
      var d = parseISO(todayIso);
      S.calendarMonth = { year: d.getUTCFullYear(), month: d.getUTCMonth() };
    }
    var cm = S.calendarMonth;
    var first = new Date(Date.UTC(cm.year, cm.month, 1));
    var daysInMonth = new Date(Date.UTC(cm.year, cm.month + 1, 0)).getUTCDate();
    var startPad = (first.getUTCDay() + 6) % 7; // bazar ertəsi ilk gün
    $("#cal-label").textContent = AZ_MONTHS[cm.month] + " " + cm.year;

    var byDate = {};
    S.days.forEach(function (day) { byDate[day.effectiveDate] = day; });

    var html = "";
    ["B.e", "Ç.a", "Ç", "C.a", "C", "Ş", "B"].forEach(function (w) {
      html += '<div class="cal-head">' + w + "</div>";
    });
    for (var i = 0; i < startPad; i++) html += '<div class="cal-cell empty-cell"></div>';
    for (var dd = 1; dd <= daysInMonth; dd++) {
      var iso = cm.year + "-" + String(cm.month + 1).padStart(2, "0") + "-" + String(dd).padStart(2, "0");
      var day = byDate[iso];
      if (!day) {
        html += '<div class="cal-cell"><div class="cal-date">' + dd + "</div>" +
          '<div class="cal-topic muted">—</div></div>';
        continue;
      }
      var cls = calendarStatus(day, todayIso);
      var st = dayStats(day);
      html += '<div class="cal-cell sw-' + cls + (iso === todayIso ? " is-today" : "") + '" data-day-action="open" data-day="' + day.day + '">' +
        '<div class="cal-date"><span>' + dd + "</span><span>" + st.done + "/" + st.total + "</span></div>" +
        '<div class="cal-topic">' + esc(day.topic) + "</div>" +
        '<div class="row-wrap">' +
        (day.type === "review" ? '<span class="cal-badge">təkrar</span>' : "") +
        (st.record.reschedule ? '<span class="cal-badge">köçürülüb</span>' : "") +
        "</div></div>";
    }
    $("#calendar").innerHTML = html;
  }

  function renderStats() {
    var st = stats();
    var items = [
      ["Gün " + (st.focusDay ? st.focusDay.day : 0) + "/" + (S.plan ? S.plan.meta.totalDays : 180), "Plan üzrə mövqe"],
      [st.overallPctLabel, "Ümumi gedişat"],
      [st.doneItems + "/" + st.totalItems, "Tamamlanmış element"],
      [st.streak, "Ardıcıl gün (streak)"],
      [st.doneDays, "Tam bitmiş gün"],
      [st.skippedDays, "Keçilmiş gün"],
      [Math.round(st.totalMinutes / 60) + " saat", "Ümumi öyrənmə vaxtı"],
      [st.remainingItems, "Qalan element"],
      [st.overdue.length, "Gecikmiş gün"],
      [(S.plan ? S.plan.stats.tasks : 0), "Plandaki tapşırıq"],
      [(S.plan ? S.plan.stats.videos : 0), "Plandaki video"],
      [(S.plan ? S.plan.stats.weeks : 0), "Həftə"],
    ];
    $("#stats-grid").innerHTML = items.map(function (it) {
      return '<div class="stat card"><span class="stat-value">' + it[0] + '</span><span class="stat-label">' + it[1] + "</span></div>";
    }).join("");
    renderHeatmap($("#heatmap-stats"));
    renderPhaseBars($("#phase-bars-2"));
    drawCharts();
  }

  function renderMentor() {
    var m = S.mentor;
    if (!m) {
      $("#mentor-body").innerHTML = '<div class="empty">Mentor məsləhətləri (data/mentor.json) yüklənmədi.</div>';
      return;
    }
    $("#mentor-body").innerHTML = (m.sections || []).map(function (sec) {
      return '<section class="mentor-section"><h3>' + (sec.icon || "•") + " " + esc(sec.title) + "</h3>" +
        (sec.items || []).map(function (it) {
          return '<div class="mentor-item"><b>' + esc(it.title) + "</b><p>" + esc(it.body) + "</p></div>";
        }).join("") + "</section>";
    }).join("");
    $("#mentor-tips").innerHTML = (m.weeklyTips || []).map(function (t, i) {
      return '<div class="mentor-item"><b>Həftə ' + (i + 1) + "</b><p>" + esc(t) + "</p></div>";
    }).join("");
  }

  function renderSettings() {
    $("#set-start").value = startDate();
    $("#set-daily").value = S.settings.dailyMinutes || 180;
    $("#set-name").value = S.settings.name || "";
    var client = syncClient();
    $("#set-repo").value = (S.progress.repo || SYNC.DEFAULT_REPO);
    $("#set-branch").value = (S.progress.branch || SYNC.DEFAULT_BRANCH);
    $("#set-token").placeholder = client.token ? "•••••••• (token saxlanılır)" : "github_pat_...";
    updateSyncChip();
    $("#footer-info").textContent = "AI Engineer Tracker · " + (S.settings.name || "Shadow009-dark") +
      " · " + S.days.length + " gün · " + Math.round(stats().totalMinutes / 60) + " saat";
  }

  /* ================================================================== *
   * 5. Actions
   * ================================================================== */

  var pendingSync = null;

  function scheduleSync(reason, dayNo) {
    if (!syncClient().token) return;
    clearTimeout(pendingSync);
    pendingSync = setTimeout(function () { syncNow(reason, dayNo); }, 2500);
  }

  function markItem(dayNo, id, done) {
    var day = dayByNumber(dayNo);
    if (!day) return;
    var record = ensureRec(dayNo);
    var idx = record.items.indexOf(id);
    if (done && idx < 0) record.items.push(id);
    if (!done && idx >= 0) record.items.splice(idx, 1);
    var todayIso = todayISO();
    record.lastDate = todayIso;
    record.updatedAt = new Date().toISOString();

    // activity map (streak + heatmap)
    var act = S.progress.activity || (S.progress.activity = {});
    if (done) act[todayIso] = (act[todayIso] || 0) + 1;
    else if (act[todayIso]) act[todayIso] = Math.max(0, act[todayIso] - 1);

    var status = computeStatus(record, day);
    if (status === "done" && !record.completedAt) record.completedAt = todayIso;
    if (status !== "done") record.completedAt = null;
    record.status = status === "done" ? "done" : (status === "skipped" ? "skipped" : status);

    // if a modal is open, preserve its unsaved note before re-rendering
    var modalNote = $("#modal-day-body #day-note");
    if (modalNote) record.note = modalNote.value;

    S.progress.log.push({ at: new Date().toISOString(), action: done ? "item-done" : "item-undo", day: dayNo, id: id });
    saveProgress();
    renderDayViews();
    refreshModalBody(dayNo);
    scheduleSync(done ? "tapşırıq işarələndi" : "işarə geri alındı", dayNo);
  }

  function markDayDone(dayNo) {
    var day = dayByNumber(dayNo);
    if (!day) return;
    var record = ensureRec(dayNo);
    allItemIds(day).forEach(function (id) {
      if (record.items.indexOf(id) < 0) record.items.push(id);
    });
    record.status = "done";
    record.completedAt = record.completedAt || todayISO();
    record.lastDate = todayISO();
    record.updatedAt = new Date().toISOString();
    var act = S.progress.activity || (S.progress.activity = {});
    act[todayISO()] = (act[todayISO()] || 0) + allItemIds(day).length;
    S.progress.log.push({ at: new Date().toISOString(), action: "day-done", day: dayNo });
    saveProgress();
    renderDayViews();
    toast("Gün " + dayNo + " tamamlandı olaraq işarələndi. 🎉", "ok");
    syncDayLog(dayNo);
    scheduleSync("gün tamamlandı", dayNo);
  }

  function skipDay(dayNo) {
    var day = dayByNumber(dayNo);
    if (!day) return;
    var record = ensureRec(dayNo);
    record.status = "skipped";
    record.lastDate = todayISO();
    record.updatedAt = new Date().toISOString();
    S.progress.log.push({ at: new Date().toISOString(), action: "day-skip", day: dayNo });
    saveProgress();
    renderDayViews();
    toast("Gün " + dayNo + " keçildi kimi işarələndi.", "ok");
    syncDayLog(dayNo);
    scheduleSync("gün keçildi", dayNo);
  }

  function openReschedule(dayNo) {
    var day = dayByNumber(dayNo);
    if (!day) return;
    var def = addDays(todayISO(), 1);
    openModal("📆 Günü köçür — Gün " + dayNo + ": " + esc(day.topic),
      '<p class="muted small">Bu günün qalan elementləri seçdiyiniz tarixə keçir. Gedişat itmir, yalnız tarix dəyişir.</p>' +
      '<label class="field"><span>Yeni tarix</span><input type="date" id="reschedule-date" value="' +
      esc(day.effectiveDate && day.effectiveDate > todayISO() ? day.effectiveDate : def) + '" /></label>',
      [
        { label: "İmtina", cls: "btn-ghost" },
        {
          label: "📆 Köçür", cls: "btn-primary", onClick: function () {
            var val = $("#reschedule-date").value;
            if (!val) { toast("Tarix seçilmədi.", "err"); return false; }
            var record = ensureRec(dayNo);
            record.reschedule = val;
            record.updatedAt = new Date().toISOString();
            S.progress.log.push({ at: new Date().toISOString(), action: "day-reschedule", day: dayNo, to: val });
            saveProgress();
            buildDays(); // tarixlər yenidən hesablanmalıdır
            renderDayViews();
            toast("Gün " + dayNo + " " + formatAZ(val) + " tarixinə köçürüldü.", "ok");
            scheduleSync("gün köçürüldü", dayNo);
            return true;
          }
        },
      ]);
  }

  function saveNote(dayNo) {
    var el = $("#day-note");
    if (!el) return;
    var record = ensureRec(dayNo);
    record.note = el.value;
    record.lastDate = todayISO();
    record.updatedAt = new Date().toISOString();
    S.progress.log.push({ at: new Date().toISOString(), action: "note", day: dayNo });
    saveProgress();
    toast("Qeyd yadda saxlanıldı.", "ok");
    syncDayLog(dayNo);
    scheduleSync("qeyd əlavə edildi", dayNo);
  }

  function saveReflection() {
    var st = stats();
    if (!st.focusDay) return;
    var dayNo = st.focusDay.day;
    var record = ensureRec(dayNo);
    record.reflection = {
      learned: $("#refl-learned").value,
      hard: $("#refl-hard").value,
      tomorrow: $("#refl-tomorrow").value,
    };
    record.lastDate = todayISO();
    record.updatedAt = new Date().toISOString();
    S.progress.log.push({ at: new Date().toISOString(), action: "reflection", day: dayNo });
    saveProgress();
    toast("Refleksiya yadda saxlanıldı və log faylı göndərilir.", "ok");
    syncDayLog(dayNo);
    scheduleSync("refleksiya", dayNo);
  }

  /** Merge every day touched on a date into one logs/YYYY-MM-DD.md file. */
  function buildDailyLog(dateIso) {
    var parts = [];
    var todayItems = [];
    S.days.forEach(function (day) {
      var record = S.progress.days[String(day.day)];
      if (!record) return;
      var touchedToday = record.lastDate === dateIso;
      var plannedToday = day.effectiveDate === dateIso;
      if (!touchedToday && !plannedToday) return;
      if (!record.items.length && !record.note && !(record.reflection && record.reflection.learned) && record.status === "pending") return;
      var st = dayStats(day);
      todayItems.push({ day: day, st: st, record: record });
      parts.push(SYNC.buildLogMarkdown(
        Object.assign({}, day, { date: dateIso }), record, record.items
      ));
    });
    if (!parts.length) return null;
    var totalTasks = todayItems.reduce(function (a, x) { return a + x.st.totalTasks; }, 0);
    var doneTasks = todayItems.reduce(function (a, x) { return a + x.st.doneTasks; }, 0);
    var minutes = todayItems.reduce(function (a, x) { return a + (x.record.minutes || 0); }, 0);
    var header = "# " + dateIso + " — gündəlik jurnal\n\n" +
      "> " + todayItems.length + " gün · " + doneTasks + "/" + totalTasks + " tapşırıq · " +
      minutes + " dəqiqə\n\n" +
      "**Günlər:** " + todayItems.map(function (x) { return "Gün " + x.day.day + " (" + x.day.topic + ")"; }).join("; ") + "\n\n---\n\n";
    return {
      markdown: header + parts.join("\n\n---\n\n"),
      summary: {
        days: todayItems.map(function (x) { return x.day.day; }),
        doneTasks: doneTasks, totalTasks: totalTasks, minutes: minutes,
      },
    };
  }

  function syncDayLog(dayNo, silent) {
    var client = syncClient();
    var daily = buildDailyLog(todayISO());
    if (!daily) return;
    if (!client.token) {
      // Without a token no network request is made: everything stays local.
      if (!silent) toast("Log yerli saxlanıldı. GitHub üçün Ayarlar → token əlavə edin.", "ok");
      return;
    }
    var day = dayByNumber(dayNo);
    var msg = day
      ? SYNC.buildLogCommitMessage(dayNo, day.topic, todayISO())
      : "Gündəlik qeyd (" + todayISO() + ")";
    client.syncLog(todayISO(), daily.markdown, msg).then(function (res) {
      updateSyncChip();
      if (silent) return;
      if (res.ok) toast("logs/" + todayISO() + ".md GitHub-a göndərildi.", "ok");
      else {
        toast("Log yerli saxlanıldı və növbəyə düşdü (sonra sinxronlanacaq). " + (res.error || ""), "err");
      }
    });
  }

  function syncNow(reason, dayNo) {
    var client = syncClient();
    if (!client.token) {
      updateSyncChip();
      return;
    }
    var day = dayNo ? dayByNumber(dayNo) : stats().focusDay;
    var message = "Progress yeniləndi (" + todayISO() + ")";
    if (day) {
      var st = dayStats(day);
      message = SYNC.buildCommitMessage(day.day, st.doneTasks, st.totalTasks, day.topic);
    }
    $("#sync-text").textContent = "Sinxronlaşır...";
    client.syncProgress(S.progress, { message: message }).then(function (res) {
      updateSyncChip();
      if (res.ok) {
        if (res.merged) {
          S.progress = Object.assign(S.progress, {
            activity: res.merged.activity, log: res.merged.log,
          });
          S.progress.days = res.merged.days;
          buildDays();
          writeJSON(KEYS.progress, S.progress);
        }
        if (reason) toast("GitHub-a göndərildi: " + reason, "ok");
        if (dayNo) syncDayLog(dayNo, true);
        renderDayViews();
      } else {
        toast("Sinxronizasiya alınmadı, yerli saxlanıldı: " + (res.error || ""), "err");
      }
    });
  }

  function syncAll() {
    var client = syncClient();
    if (!client.token) { toast("Əvvəlcə token əlavə edin.", "err"); return; }
    var payloads = [];
    var seen = {};
    S.days.forEach(function (day) {
      var record = S.progress.days[String(day.day)];
      if (!record) return;
      if (!record.items.length && !record.note && !(record.reflection && record.reflection.learned) && record.status === "pending") return;
      var dateIso = record.lastDate || day.effectiveDate;
      if (!dateIso || seen[dateIso]) {
        if (!dateIso) return;
      }
      seen[dateIso] = true;
    });
    Object.keys(seen).sort().forEach(function (dateIso) {
      var daily = buildDailyLog(dateIso);
      if (daily) {
        payloads.push({
          date: dateIso,
          markdown: daily.markdown,
          message: "Gündəlik qeyd (" + dateIso + "): " + daily.summary.days.length + " gün, " +
            daily.summary.doneTasks + "/" + daily.summary.totalTasks + " tapşırıq",
        });
      }
    });
    $("#sync-text").textContent = "Hamısı göndərilir...";
    client.syncAll(S.progress, payloads, { message: "Tam sinxronizasiya (" + todayISO() + ")" }).then(function (res) {
      updateSyncChip();
      renderDayViews();
      if (res.progress && res.progress.ok) {
        toast("Progress + " + res.logs.length + " log faylı göndərildi.", "ok");
      } else {
        toast("Sinxronizasiya alınmadı — növbəyə salındı.", "err");
      }
    });
  }

  function flushQueue() {
    var client = syncClient();
    var q = client.queue();
    if (!q.length) { toast("Növbə boşdur — hər şey sinxronlaşdırılıb.", "ok"); return; }
    client.flush({ getLocalProgress: function () { return S.progress; } }).then(function (res) {
      updateSyncChip();
      if (res.ok) toast(res.processed + " əməliyyat sinxronlaşdırıldı.", "ok");
      else toast("Növbə tam boşalmadı: " + (res.error || res.remaining + " əməliyyat qaldı"), "err");
    });
  }

  /* ---------------- plan editing ---------------- */

  function editDay(dayNo) {
    var day = dayByNumber(dayNo);
    if (!day) return;
    openModal("✏️ Gün " + dayNo + " redaktəsi",
      '<label class="field"><span>Mövzu</span><input type="text" id="edit-topic" value="' + esc(day.topic) + '" /></label>' +
      '<label class="field"><span>Nə öyrənməli (hər sətir bir element)</span><textarea id="edit-learn" rows="4">' +
      esc((day.learn || []).join("\n")) + "</textarea></label>" +
      '<label class="field"><span>Tapşırıqlar (hər sətir bir tapşırıq)</span><textarea id="edit-tasks" rows="5">' +
      esc((day.tasks || []).join("\n")) + "</textarea></label>" +
      '<label class="field"><span>Bilməli olduğum suallar (hər sətir bir sual)</span><textarea id="edit-must" rows="4">' +
      esc((day.mustKnow || []).join("\n")) + "</textarea></label>" +
      '<label class="field"><span>Günün nəticəsi (deliverable)</span><input type="text" id="edit-deliv" value="' +
      esc(day.deliverable) + '" /></label>' +
      '<label class="field"><span>Təxmini vaxt (dəqiqə)</span><input type="number" id="edit-minutes" min="30" max="600" step="15" value="' +
      (day.minutes || 180) + '" /></label>',
      [
        { label: "İmtina", cls: "btn-ghost" },
        {
          label: "💾 Yadda saxla", cls: "btn-primary", onClick: function () {
            var lines = function (v) {
              return v.split("\n").map(function (s) { return s.trim(); }).filter(Boolean);
            };
            var patch = {
              topic: $("#edit-topic").value.trim() || day.topic,
              learn: lines($("#edit-learn").value),
              tasks: lines($("#edit-tasks").value),
              mustKnow: lines($("#edit-must").value),
              deliverable: $("#edit-deliv").value.trim(),
              minutes: Number($("#edit-minutes").value) || day.minutes,
            };
            S.progress.planOverrides.patched = S.progress.planOverrides.patched || {};
            S.progress.planOverrides.patched[day.id] = patch;
            saveProgress();
            buildDays();
            renderPlan();
            renderDayViews();
            toast("Gün " + dayNo + " redaktə edildi (yerli olaraq saxlanır).", "ok");
            return true;
          }
        },
      ]);
  }

  function deleteDay(dayNo) {
    var day = dayByNumber(dayNo);
    if (!day) return;
    openModal("🗑️ Günü sil — Gün " + dayNo,
      '<p>Bu gün plandan çıxarılacaq: <b>' + esc(day.topic) + "</b></p>" +
      '<p class="muted small">Gedişat qeydləri silinmir, lakin gün plandan çıxdığı üçün sonrakı günlərin tarixləri bir gün irəli sürüşür.</p>',
      [
        { label: "İmtina", cls: "btn-ghost" },
        {
          label: "🗑️ Sil", cls: "btn-danger", onClick: function () {
            if (day._custom) {
              S.progress.planOverrides.added = (S.progress.planOverrides.added || [])
                .filter(function (d) { return d.id !== day.id; });
            } else {
              S.progress.planOverrides.removed = (S.progress.planOverrides.removed || []).concat([day.id]);
            }
            saveProgress();
            buildDays();
            renderPlan();
            renderDayViews();
            toast("Gün " + dayNo + " plandan çıxarıldı.", "ok");
            return true;
          }
        },
      ]);
  }

  function addDay() {
    var options = (S.plan.phases || []).map(function (p) {
      return '<option value="' + p.id + '">Faza ' + p.id + ": " + esc(p.title) + "</option>";
    }).join("");
    openModal("➕ Yeni gün əlavə et",
      '<label class="field"><span>Faza</span><select id="add-phase">' + options + "</select></label>" +
      '<label class="field"><span>Mövzu</span><input type="text" id="add-topic" placeholder="Məsələn: RAG layihəsi üzərində iş" /></label>' +
      '<label class="field"><span>Nə öyrənməli (hər sətir bir element)</span><textarea id="add-learn" rows="3"></textarea></label>' +
      '<label class="field"><span>Tapşırıqlar (hər sətir bir tapşırıq)</span><textarea id="add-tasks" rows="4"></textarea></label>' +
      '<label class="field"><span>Nəticə (deliverable)</span><input type="text" id="add-deliv" /></label>',
      [
        { label: "İmtina", cls: "btn-ghost" },
        {
          label: "➕ Əlavə et", cls: "btn-primary", onClick: function () {
            var topic = $("#add-topic").value.trim();
            if (!topic) { toast("Mövzu boşdur.", "err"); return false; }
            var lines = function (v) { return v.split("\n").map(function (s) { return s.trim(); }).filter(Boolean); };
            var maxDay = S.days.reduce(function (a, d) { return Math.max(a, d.day || 0); }, 0);
            var phaseId = Number($("#add-phase").value);
            var phase = (S.plan.phases || []).filter(function (p) { return p.id === phaseId; })[0];
            var newDay = {
              id: "custom" + (maxDay + 1),
              day: maxDay + 1,
              type: "study",
              week: null,
              phaseId: phaseId,
              phaseTitle: phase ? phase.title : "",
              topic: topic,
              learn: lines($("#add-learn").value),
              videos: [],
              reading: [],
              tasks: lines($("#add-tasks").value),
              deliverable: $("#add-deliv").value.trim(),
              mustKnow: [],
              minutes: 180,
              date: null,
              _custom: true,
            };
            S.progress.planOverrides.added = (S.progress.planOverrides.added || []).concat([newDay]);
            saveProgress();
            buildDays();
            renderPlan();
            renderDayViews();
            toast("Yeni gün əlavə edildi (plan sonunda).", "ok");
            return true;
          }
        },
      ]);
  }

  function moveDay(dayNo, dir) {
    var idx = -1;
    for (var i = 0; i < S.days.length; i++) if (S.days[i].day === dayNo) idx = i;
    if (idx < 0) return;
    var target = dir < 0 ? idx - 1 : idx + 1;
    if (target < 0 || target >= S.days.length) return;
    var a = S.days[idx], b = S.days[target];
    var ov = S.progress.planOverrides.order || (S.progress.planOverrides.order = {});
    var aOrder = a._order, bOrder = b._order;
    ov[a.id] = bOrder;
    ov[b.id] = aOrder;
    saveProgress();
    buildDays();
    renderPlan();
    renderDayViews();
    toast("Gün " + a.day + " " + (dir < 0 ? "yuxarı" : "aşağı") + " köçürüldü.", "ok");
  }

  function saveProgress() {
    S.progress.updatedAt = new Date().toISOString();
    S.progress.sync = S.progress.sync || {};
    writeJSON(KEYS.progress, S.progress);
  }

  function renderDayViews() {
    var active = S.view;
    if (active === "dashboard") renderDashboard();
    else if (active === "plan") renderPlan();
    else if (active === "calendar") renderCalendar();
    else if (active === "stats") renderStats();
    else if (active === "settings") renderSettings();
    updateSyncChip();
  }

  /* ================================================================== *
   * 6. Modal
   * ================================================================== */

  function openModal(title, bodyHTML, actions) {
    var root = $("#modal-root");
    root.innerHTML = '<div class="modal-backdrop"><div class="modal">' +
      "<h2>" + title + "</h2>" + bodyHTML +
      '<div class="modal-actions"></div></div></div>';
    var actionsEl = $(".modal-actions", root);
    (actions || [{ label: "Bağla", cls: "btn-ghost" }]).forEach(function (act) {
      var b = document.createElement("button");
      b.type = "button";
      b.className = "btn " + (act.cls || "btn-ghost");
      b.textContent = act.label;
      b.addEventListener("click", function () {
        // onClick returning false means validation failed: keep the modal open.
        // Otherwise the modal closes after the action.
        var failed = act.onClick ? act.onClick() === false : false;
        if (!failed) closeModal();
      });
      actionsEl.appendChild(b);
    });
    $(".modal-backdrop", root).addEventListener("click", function (e) {
      if (e.target === this) closeModal();
    });
  }

  function closeModal() { $("#modal-root").innerHTML = ""; S.modalDay = null; }

  function refreshModalBody(dayNo) {
    var host = $("#modal-day-body");
    if (!host || S.modalDay !== dayNo) return;
    var d = dayByNumber(dayNo);
    if (d) host.innerHTML = dayBodyHTML(d, { compact: false });
  }

  function openDayModal(dayNo) {
    var day = dayByNumber(dayNo);
    if (!day) return;
    S.modalDay = dayNo;
    var st = dayStats(day);
    openModal("Gün " + day.day + " · " + esc(day.topic),
      '<div class="day-nav"><span class="pill">' + formatAZ(day.effectiveDate, true) + "</span>" +
      '<span class="pill">Faza ' + day.phaseId + "</span>" +
      '<span class="pill">' + (day.type === "review" ? "Təkrar günü" : "Öyrənmə günü") + "</span>" +
      '<span class="pill">' + statusBadgeText(st.status) + "</span></div>" +
      '<div id="modal-day-body" class="day-body" style="margin-top:12px">' + dayBodyHTML(day, { compact: false }) + "</div>",
      [
        { label: "⏭️ Keç", cls: "btn-ghost", onClick: function () { skipDay(day.day); } },
        // returns false: openReschedule opens its own modal, replacing this one
        { label: "📆 Köçür", cls: "btn-ghost", onClick: function () { openReschedule(day.day); return false; } },
        { label: "✅ Tamamlandı", cls: "btn-primary", onClick: function () { markDayDone(day.day); } },
        { label: "Bağla", cls: "btn-ghost" },
      ]);
  }

  /* ================================================================== *
   * 7. Charts and heatmap
   * ================================================================== */

  function cssVar(name) {
    return getComputedStyle(document.documentElement).getPropertyValue(name).trim() || "#888";
  }

  function prepCanvas(canvas) {
    if (!canvas || !canvas.clientWidth) return null;
    var dpr = window.devicePixelRatio || 1;
    var w = canvas.clientWidth, h = Number(canvas.getAttribute("height")) || 220;
    canvas.width = Math.round(w * dpr);
    canvas.height = Math.round(h * dpr);
    canvas.style.height = h + "px";
    var ctx = canvas.getContext("2d");
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, w, h);
    return { ctx: ctx, w: w, h: h };
  }

  function seriesFor(range) {
    var out = [];
    var today = todayISO();
    var act = (S.progress && S.progress.activity) || {};
    for (var i = range - 1; i >= 0; i--) {
      var iso = addDays(today, -i);
      out.push({ date: iso, value: act[iso] || 0 });
    }
    return out;
  }

  function drawBars(canvas, data) {
    var c = prepCanvas(canvas);
    if (!c) return;
    var ctx = c.ctx;
    var pad = { l: 30, r: 8, t: 12, b: 24 };
    var plotW = c.w - pad.l - pad.r, plotH = c.h - pad.t - pad.b;
    var max = Math.max(4, Math.max.apply(null, data.map(function (d) { return d.value; })));
    var accent = cssVar("--accent"), muted = cssVar("--muted"), border = cssVar("--border");

    ctx.strokeStyle = border;
    ctx.fillStyle = muted;
    ctx.font = "11px " + cssVar("--sans");
    for (var g = 0; g <= 3; g++) {
      var y = pad.t + (plotH / 3) * g;
      ctx.beginPath();
      ctx.moveTo(pad.l, y + 0.5);
      ctx.lineTo(c.w - pad.r, y + 0.5);
      ctx.stroke();
      ctx.fillText(String(Math.round(max - (max / 3) * g)), 4, y + 4);
    }
    var bw = plotW / data.length;
    data.forEach(function (d, i) {
      var h = (d.value / max) * plotH;
      var x = pad.l + i * bw + bw * 0.18;
      var y = pad.t + plotH - h;
      ctx.fillStyle = d.value ? accent : border;
      ctx.globalAlpha = d.value ? 0.85 : 0.5;
      ctx.beginPath();
      var w = bw * 0.64, r = Math.min(4, w / 2);
      ctx.moveTo(x, y + r);
      ctx.arcTo(x, y, x + w, y, r);
      ctx.arcTo(x + w, y, x + w, y + h, r);
      ctx.arcTo(x + w, y + h, x, y + h, r);
      ctx.arcTo(x, y + h, x, y, r);
      ctx.closePath();
      ctx.fill();
      ctx.globalAlpha = 1;
      if (d.value) {
        ctx.fillStyle = muted;
        ctx.fillText(String(d.value), x + w / 2 - 4, y - 3);
      }
      if (data.length <= 10 || i % Math.ceil(data.length / 8) === 0) {
        ctx.fillStyle = muted;
        ctx.fillText(d.date.slice(5), x - 2, c.h - 7);
      }
    });
  }

  function drawLine(canvas, data) {
    var c = prepCanvas(canvas);
    if (!c) return;
    var ctx = c.ctx;
    var pad = { l: 30, r: 10, t: 12, b: 24 };
    var plotW = c.w - pad.l - pad.r, plotH = c.h - pad.t - pad.b;
    var max = Math.max(4, Math.max.apply(null, data.map(function (d) { return d.value; })));
    var accent = cssVar("--accent"), muted = cssVar("--muted"), border = cssVar("--border");
    var stepX = plotW / Math.max(1, data.length - 1);

    ctx.strokeStyle = border;
    ctx.fillStyle = muted;
    ctx.font = "11px " + cssVar("--sans");
    for (var g = 0; g <= 3; g++) {
      var y = pad.t + (plotH / 3) * g;
      ctx.beginPath(); ctx.moveTo(pad.l, y + 0.5); ctx.lineTo(c.w - pad.r, y + 0.5); ctx.stroke();
      ctx.fillText(String(Math.round(max - (max / 3) * g)), 4, y + 4);
    }
    var pts = data.map(function (d, i) {
      return { x: pad.l + i * stepX, y: pad.t + plotH - (d.value / max) * plotH, v: d.value, date: d.date };
    });
    var grad = ctx.createLinearGradient(0, pad.t, 0, pad.t + plotH);
    grad.addColorStop(0, accent + "66");
    grad.addColorStop(1, accent + "00");
    ctx.beginPath();
    ctx.moveTo(pts[0].x, pad.t + plotH);
    pts.forEach(function (p) { ctx.lineTo(p.x, p.y); });
    ctx.lineTo(pts[pts.length - 1].x, pad.t + plotH);
    ctx.closePath();
    ctx.fillStyle = grad;
    ctx.fill();

    ctx.beginPath();
    pts.forEach(function (p, i) { i ? ctx.lineTo(p.x, p.y) : ctx.moveTo(p.x, p.y); });
    ctx.strokeStyle = accent;
    ctx.lineWidth = 2;
    ctx.stroke();
    ctx.lineWidth = 1;
    pts.forEach(function (p) {
      ctx.beginPath();
      ctx.arc(p.x, p.y, 2.5, 0, Math.PI * 2);
      ctx.fillStyle = accent;
      ctx.fill();
    });
    [0, Math.floor(pts.length / 2), pts.length - 1].forEach(function (i) {
      ctx.fillStyle = muted;
      var label = pts[i].date.slice(5);
      ctx.fillText(label, clamp(pts[i].x - 12, 2, c.w - 34), c.h - 7);
    });
  }

  function drawCharts() {
    drawBars($("#chart-week"), seriesFor(7));
    drawLine($("#chart-month"), seriesFor(30));
    drawBars($("#chart-week-2"), seriesFor(7));
    drawLine($("#chart-month-2"), seriesFor(30));
  }

  function renderHeatmap(container) {
    if (!container || !S.progress) return;
    var act = S.progress.activity || {};
    var today = todayISO();
    var start = weekStart(addDays(today, -7 * 25)); // son 26 həftə
    var cells = [];
    for (var i = 0; i < 26 * 7; i++) {
      var iso = addDays(start, i);
      var count = act[iso] || 0;
      var level = activityLevel(count);
      var inRange = iso >= startDate();
      cells.push('<div class="hm-cell l' + level + (inRange ? "" : " off") + (iso === today ? " today" : "") +
        '" title="' + iso + ": " + count + ' element"></div>');
    }
    container.innerHTML = cells.join("");
  }

  /* ================================================================== *
   * 8. Sync integration
   * ================================================================== */

  var _client = null;
  function syncClient() {
    if (!_client) {
      _client = SYNC.createClient({
        repo: (S.progress && S.progress.repo) || SYNC.DEFAULT_REPO,
        branch: (S.progress && S.progress.branch) || SYNC.DEFAULT_BRANCH,
        onStatus: function () { updateSyncChip(); },
      });
    }
    return _client;
  }

  function updateSyncChip() {
    var client = syncClient();
    var st = client.status();
    var dot = $("#sync-dot"), text = $("#sync-text");
    if (!dot || !text) return;
    var label, state;
    if (!client.token) { state = "no-token"; label = "Yerli rejim (token yoxdur)"; }
    else if (st.pending > 0) { state = "pending"; label = st.pending + " gözləyən sinxronizasiya"; }
    else if (st.lastError) { state = "error"; label = "Sync xətası"; }
    else if (st.lastSync) {
      state = "idle";
      label = "Sinxron: " + new Date(st.lastSync).toLocaleString("az-AZ", { hour: "2-digit", minute: "2-digit", day: "2-digit", month: "2-digit" });
    }
    else { state = "idle"; label = "Hazır (sinxron olunmayıb)"; }
    dot.className = "dot state-" + state;
    text.textContent = label;
    var gh = $("#gh-status");
    if (gh) gh.textContent = label;
  }

  /* ================================================================== *
   * 9. Export / import
   * ================================================================== */

  function exportProgress() {
    download("progress.json", JSON.stringify(S.progress, null, 2) + "\n", "application/json");
    toast("progress.json yüklənir.", "ok");
  }

  function exportMarkdown() {
    var st = stats();
    var lines = [];
    lines.push("# AI Engineer Tracker — hesabat (" + todayISO() + ")");
    lines.push("");
    lines.push("- Ümumi gedişat: **" + st.overallPctLabel + "** (" + st.doneItems + "/" + st.totalItems + " element)");
    lines.push("- Tamamlanmış gün: **" + st.doneDays + "** · Keçilmiş: " + st.skippedDays);
    lines.push("- Ardıcıl gün (streak): **" + st.streak + "**");
    lines.push("- Ümumi öyrənmə vaxtı: **" + Math.round(st.totalMinutes / 60) + " saat**");
    lines.push("- Gecikmiş gün: **" + st.overdue.length + "**");
    lines.push("");
    lines.push("## Faza gedişatı");
    st.phaseStats.forEach(function (p) {
      lines.push("- Faza " + p.id + " (" + p.title + "): " + p.done + "/" + p.total + " element — " + p.percent + "% · " +
        p.doneDays + "/" + p.days + " gün tamamlandı");
    });
    lines.push("");
    lines.push("## Günlər");
    lines.push("");
    lines.push("| Gün | Tarix | Mövzu | Status | Tapşırıq | Dəqiqə |");
    lines.push("| --- | --- | --- | --- | --- | --- |");
    S.days.forEach(function (day) {
      var s = dayStats(day);
      lines.push("| " + day.day + " | " + day.effectiveDate + " | " + (day.topic || "").replace(/\|/g, "/") +
        " | " + statusBadgeText(s.status) + " | " + s.doneTasks + "/" + s.totalTasks + " | " + (s.record.minutes || 0) + " |");
    });
    lines.push("");
    lines.push("## Refleksiyalar");
    S.days.forEach(function (day) {
      var r = S.progress.days[String(day.day)];
      if (!r || !r.reflection || !(r.reflection.learned || r.reflection.hard || r.reflection.tomorrow)) return;
      lines.push("");
      lines.push("### Gün " + day.day + " — " + day.topic);
      lines.push("- **Bu gün nə öyrəndim?** " + (r.reflection.learned || "—"));
      lines.push("- **Nə çətin oldu?** " + (r.reflection.hard || "—"));
      lines.push("- **Sabah nə edəcəm?** " + (r.reflection.tomorrow || "—"));
    });
    download("ai-engineer-hesabat-" + todayISO() + ".md", lines.join("\n") + "\n", "text/markdown");
    toast("Markdown hesabat yüklənir.", "ok");
  }

  function exportPlan() {
    var out = JSON.parse(JSON.stringify({ meta: S.plan.meta, stats: S.plan.stats, phases: S.plan.phases }));
    var ov = S.progress.planOverrides || {};
    var removed = {};
    (ov.removed || []).forEach(function (id) { removed[String(id)] = true; });
    out.phases.forEach(function (p) {
      p.days = (p.days || []).filter(function (d) { return !removed[String(d.id)]; })
        .map(function (d) {
          var patch = (ov.patched || {})[d.id];
          return Object.assign({}, d, patch || {});
        });
    });
    (ov.added || []).forEach(function (d) {
      var p = out.phases.filter(function (ph) { return ph.id === d.phaseId; })[0] || out.phases[out.phases.length - 1];
      p.days.push(d);
    });
    download("plan.json", JSON.stringify(out, null, 2) + "\n", "application/json");
    toast("Redaktə olunmuş plan.json yüklənir — repo-daki data/plan.json ilə əvəz edə bilərsən.", "ok");
  }

  function importProgress(file) {
    var reader = new FileReader();
    reader.onload = function () {
      try {
        var incoming = JSON.parse(String(reader.result));
        var merged = SYNC.mergeProgress(incoming, S.progress);
        S.progress = Object.assign(blankProgress(), merged);
        writeJSON(KEYS.progress, S.progress);
        buildDays();
        renderDayViews();
        toast("Progress idxal edildi və birləşdirildi (heç bir tamamlanmış element itmədi).", "ok");
      } catch (e) {
        toast("Fayl oxuna bilmədi: " + e.message, "err");
      }
    };
    reader.readAsText(file);
  }

  /* ================================================================== *
   * 10. Events and init
   * ================================================================== */

  function switchView(view) {
    S.view = view;
    $$(".tab").forEach(function (t) { t.classList.toggle("is-active", t.dataset.view === view); });
    $$(".view").forEach(function (v) { v.hidden = v.id !== "view-" + view; });
    renderDayViews();
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    $("#btn-theme").textContent = theme === "dark" ? "🌙" : "☀️";
    localStorage.setItem(KEYS.theme, theme);
    if (S.plan) drawCharts();
  }

  function toggleTheme() {
    applyTheme(document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark");
  }

  function nextTodoItem() {
    var day = stats().focusDay;
    if (!day) return null;
    var ids = itemIds(day, "t");
    for (var i = 0; i < ids.length; i++) if (!isDone(day.day, ids[i])) return { day: day, id: ids[i], index: i };
    return null;
  }

  function bindEvents() {
    $$(".tab").forEach(function (t) {
      t.addEventListener("click", function () { switchView(t.dataset.view); });
    });

    $("#btn-theme").addEventListener("click", toggleTheme);
    $("#btn-help").addEventListener("click", function () {
      openModal("⌨️ Klaviatura qısayolları",
        '<div class="keys">' + $("#view-settings .keys").innerHTML + "</div>",
        [{ label: "Bağla", cls: "btn-primary" }]);
    });
    $("#sync-chip").addEventListener("click", function () { switchView("settings"); });
    $("#btn-sync-now").addEventListener("click", function () { syncNow("əl ilə"); });

    document.addEventListener("change", function (e) {
      var t = e.target;
      if (t && t.dataset && t.dataset.check) {
        var id = t.dataset.check;
        var m = /^d(\d+)-/.exec(id);
        if (m) markItem(Number(m[1]), id, t.checked);
      }
    });

    document.addEventListener("click", function (e) {
      if (e.target && e.target.id === "btn-save-note") {
        var noteDay = S.modalDay || (stats().focusDay && stats().focusDay.day);
        if (noteDay) saveNote(noteDay);
        return;
      }
      var el = e.target.closest ? e.target.closest("[data-plan-toggle],[data-day-action],[data-plan-edit],[data-plan-del],[data-plan-up],[data-plan-down]") : null;
      if (!el) return;
      var d = el.dataset;

      if (d.planToggle) {
        var card = $('[data-day-card="' + d.planToggle + '"]');
        if (card) card.classList.toggle("open");
        return;
      }
      if (d.planEdit) { editDay(Number(d.planEdit)); return; }
      if (d.planDel) { deleteDay(Number(d.planDel)); return; }
      if (d.planUp) { moveDay(Number(d.planUp), -1); return; }
      if (d.planDown) { moveDay(Number(d.planDown), 1); return; }
      if (d.dayAction === "open") { openDayModal(Number(d.day)); return; }
      if (d.dayAction === "reschedule") { openReschedule(Number(d.day)); return; }
    });

    $("#today-card").addEventListener("click", function (e) {
      var day = stats().focusDay;
      if (!day) return;
      if (e.target.id === "btn-save-note") { saveNote(day.day); return; }
      var btn = e.target.closest ? e.target.closest("[data-day-action]") : null;
      if (btn) {
        if (btn.dataset.dayAction === "open") openDayModal(day.day);
        if (btn.dataset.dayAction === "reschedule") openReschedule(day.day);
      }
    });

    $("#btn-day-done").addEventListener("click", function () {
      var day = stats().focusDay;
      if (day) markDayDone(day.day);
    });
    $("#btn-day-skip").addEventListener("click", function () {
      var day = stats().focusDay;
      if (day) skipDay(day.day);
    });
    $("#btn-day-note").addEventListener("click", function () {
      switchView("dashboard");
      var note = $("#today-body #day-note");
      if (note) { note.focus(); note.scrollIntoView({ behavior: "smooth", block: "center" }); }
    });
    $("#btn-day-reschedule").addEventListener("click", function () {
      var day = stats().focusDay;
      if (day) openReschedule(day.day);
    });
    $("#btn-save-reflection").addEventListener("click", saveReflection);

    ["#filter-q", "#filter-phase", "#filter-status", "#filter-type"].forEach(function (sel) {
      var el = $(sel);
      if (!el) return;
      var evt = sel === "#filter-q" ? "input" : "change";
      el.addEventListener(evt, function () {
        S.filters = {
          q: $("#filter-q").value,
          phase: $("#filter-phase").value,
          status: $("#filter-status").value,
          type: $("#filter-type").value,
        };
        renderPlan();
      });
    });

    $("#btn-plan-edit-toggle").addEventListener("click", function () {
      S.planEdit = !S.planEdit;
      this.classList.toggle("is-active", S.planEdit);
      this.textContent = S.planEdit ? "✏️ Redaktə rejimi aktiv (➕ gün əlavə et)" : "✏️ Planı redaktə et";
      if (S.planEdit) {
        var bar = document.createElement("div");
        bar.className = "row-wrap";
        bar.innerHTML = '<button class="btn btn-primary btn-sm" id="btn-add-day" type="button">➕ Yeni gün əlavə et</button>' +
          '<span class="muted small">✏️ redaktə · 🗑️ sil · ↑↓ yerini dəyiş</span>';
        $("#plan-list").parentNode.insertBefore(bar, $("#plan-list"));
        $("#btn-add-day").addEventListener("click", addDay);
      } else {
        var existing = $("#btn-add-day");
        if (existing) existing.parentNode.remove();
      }
      renderPlan();
    });

    $("#cal-prev").addEventListener("click", function () {
      S.calendarMonth.month -= 1;
      if (S.calendarMonth.month < 0) { S.calendarMonth.month = 11; S.calendarMonth.year -= 1; }
      renderCalendar();
    });
    $("#cal-next").addEventListener("click", function () {
      S.calendarMonth.month += 1;
      if (S.calendarMonth.month > 11) { S.calendarMonth.month = 0; S.calendarMonth.year += 1; }
      renderCalendar();
    });

    $("#btn-export-json").addEventListener("click", exportProgress);
    $("#btn-export-md").addEventListener("click", exportMarkdown);
    $("#btn-export-plan").addEventListener("click", exportPlan);
    $("#import-file").addEventListener("change", function (e) {
      if (e.target.files && e.target.files[0]) importProgress(e.target.files[0]);
      e.target.value = "";
    });

    $("#btn-save-settings").addEventListener("click", function () {
      S.settings.startDate = $("#set-start").value || startDate();
      S.settings.dailyMinutes = Number($("#set-daily").value) || 180;
      S.settings.name = $("#set-name").value.trim();
      S.progress.startDate = S.settings.startDate;
      writeJSON(KEYS.settings, S.settings);
      saveProgress();
      buildDays();
      renderDayViews();
      toast("Ayarlar saxlanıldı. Bütün tarixlər yeni başlanğıc tarixinə görə hesablandı.", "ok");
    });

    $("#btn-token-save").addEventListener("click", function () {
      var token = $("#set-token").value.trim();
      var repo = $("#set-repo").value.trim();
      var branch = $("#set-branch").value.trim() || SYNC.DEFAULT_BRANCH;
      try {
        syncClient().setRepo(repo);
        syncClient().setBranch(branch);
      } catch (err) { toast(err.message, "err"); return; }
      if (token) {
        syncClient().setToken(token);
        syncClient().emitStatus({ state: "idle", lastError: null }); // yeni token köhnə xətanı sıfırlayır
      }
      S.progress.repo = syncClient().repo;
      S.progress.branch = syncClient().branch;
      saveProgress();
      $("#set-token").value = "";
      $("#set-token").placeholder = "•••••••• (token saxlanılır)";
      toast("Token yalnız bu brauzerdə saxlanıldı (localStorage).", "ok");
      updateSyncChip();
    });

    $("#btn-test-conn").addEventListener("click", function () {
      $("#conn-result").textContent = "Yoxlanılır...";
      syncClient().testConnection().then(function (res) {
        $("#conn-result").textContent = (res.ok ? "✅ " : "❌ ") + res.message;
        if (res.ok) syncClient().emitStatus({ state: "idle", lastError: null });
      });
    });

    $("#btn-sync-progress").addEventListener("click", function () { syncNow("əl ilə"); });
    $("#btn-sync-all").addEventListener("click", syncAll);
    $("#btn-flush").addEventListener("click", flushQueue);
    $("#btn-token-clear").addEventListener("click", function () {
      syncClient().setToken(null);
      $("#set-token").placeholder = "github_pat_...";
      toast("Token silindi.", "ok");
      updateSyncChip();
    });

    $("#btn-reset-local").addEventListener("click", function () {
      openModal("🧨 Yerli progress-i sıfırla",
        "<p>Brauzerdəki bütün gedişat silinəcək. GitHub-daki fayllar toxunulmaz qalır.</p>",
        [{ label: "İmtina", cls: "btn-ghost" }, {
          label: "Sıfırla", cls: "btn-danger", onClick: function () {
            S.progress = blankProgress();
            saveProgress();
            buildDays();
            renderDayViews();
            toast("Yerli progress sıfırlandı.", "ok");
            return true;
          }
        }]);
    });

    $("#btn-clear-queue").addEventListener("click", function () {
      syncClient().saveQueue([]);
      updateSyncChip();
      toast("Sync növbəsi təmizləndi.", "ok");
    });

    document.addEventListener("keydown", function (e) {
      var tag = (e.target.tagName || "").toLowerCase();
      if (["input", "textarea", "select"].indexOf(tag) >= 0) {
        if (e.key === "Escape") e.target.blur();
        return;
      }
      if (e.ctrlKey && e.key.toLowerCase() === "s") { e.preventDefault(); syncNow("qısayol"); return; }
      if (e.key === "?") { $("#btn-help").click(); return; }
      if (e.key === "/") { e.preventDefault(); switchView("plan"); $("#filter-q").focus(); return; }
      if (e.key.toLowerCase() === "t") { toggleTheme(); return; }
      if (["1", "2", "3", "4", "5", "6"].indexOf(e.key) >= 0) {
        var views = ["dashboard", "plan", "calendar", "stats", "mentor", "settings"];
        switchView(views[Number(e.key) - 1]);
        return;
      }
      var day = stats().focusDay;
      if (!day) return;
      var k = e.key.toLowerCase();
      if (k === "d") {
        var next = nextTodoItem();
        if (next) {
          markItem(next.day.day, next.id, true);
          toast("Tapşırıq " + (next.index + 1) + " tamamlandı olaraq işarələndi.", "ok");
          switchView("dashboard");
        } else {
          markDayDone(day.day);
        }
      } else if (k === "s") { skipDay(day.day); }
      else if (k === "r") { openReschedule(day.day); }
      else if (k === "n") {
        switchView("dashboard");
        var note = $("#today-body #day-note") || $("#day-note");
        if (note) { note.focus(); note.scrollIntoView({ behavior: "smooth", block: "center" }); }
      }
    });

    var resizeTimer = null;
    window.addEventListener("resize", function () {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(drawCharts, 200);
    });

    window.addEventListener("online", function () {
      toast("İnternet bərpa olundu — növbə sinxronlaşdırılır.", "ok");
      flushQueue();
    });
  }

  function loadMentor() {
    if (S.mentor) { renderMentor(); return; }
    fetch("data/mentor.json", { cache: "no-store" })
      .then(function (r) { if (!r.ok) throw new Error("mentor.json: " + r.status); return r.json(); })
      .then(function (data) { S.mentor = data; renderMentor(); $("#tip-text").textContent = weeklyTip(); })
      .catch(function () {
        $("#mentor-body").innerHTML = '<div class="empty">Mentor məsləhətləri yüklənmədi. ' +
          "Saytı `python -m http.server` ilə və ya GitHub Pages-də açın.</div>";
      });
  }

  function init() {
    var theme = localStorage.getItem(KEYS.theme) ||
      (window.matchMedia && window.matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark");
    applyTheme(theme);

    S.settings = Object.assign({ startDate: null, dailyMinutes: 180, name: "" }, readJSON(KEYS.settings, {}));
    S.progress = Object.assign(blankProgress(), readJSON(KEYS.progress, {}));
    S.progress.planOverrides = Object.assign({ removed: [], patched: {}, added: [], order: {} }, S.progress.planOverrides);
    syncClient().setRepo(S.progress.repo || SYNC.DEFAULT_REPO);
    syncClient().setBranch(S.progress.branch || SYNC.DEFAULT_BRANCH);

    // plan.json həmişə şəbəkədən oxunur (fayl yenilənəndə köhnə kopya qalmasın);
    // localStorage kopyası yalnız offline halda ehtiyat variant kimi istifadə olunur.
    var planPromise = fetch("data/plan.json", { cache: "no-store" })
      .then(function (r) { if (!r.ok) throw new Error("plan.json: HTTP " + r.status); return r.json(); })
      .then(function (p) { writeJSON(KEYS.plan, p); return p; })
      .catch(function () { return readJSON(KEYS.plan, null); });

    // progress.json from the repo is the starting point (only when local state is empty)
    var remotePromise = (!Object.keys(S.progress.days).length)
      ? fetch("data/progress.json", { cache: "no-store" })
        .then(function (r) { return r.ok ? r.json() : null; })
        .catch(function () { return null; })
      : Promise.resolve(null);

    Promise.all([planPromise, remotePromise]).then(function (res) {
      var plan = res[0], remote = res[1];
      if (!plan) {
        $("#hero-topic").textContent = "Plan faylı yüklənmədi";
        $("#today-body").innerHTML = '<div class="note-box">⚠️ <b>data/plan.json</b> oxuna bilmədi.<br>' +
          "Səbəb: saytı birbaşa fayl kimi açmaq (file://) brauzer tərəfindən bloklanır.<br>" +
          "Həll: layihə qovluğunda <code>python -m http.server 8000</code> işə salın və " +
          "<code>http://localhost:8000</code> açın, ya da GitHub Pages-də yerləşdirin.</div>";
        bindEvents();
        updateSyncChip();
        return;
      }
      S.plan = plan;
      if (remote) {
        var merged = SYNC.mergeProgress(remote, S.progress);
        S.progress = Object.assign(blankProgress(), merged);
        writeJSON(KEYS.progress, S.progress);
      }
      buildDays();
      bindEvents();
      renderDayViews();
      loadMentor();
      var client = syncClient();
      if (client.token && client.queue().length) flushQueue();
      updateSyncChip();
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
