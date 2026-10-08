#!/usr/bin/env python3
"""Regenerate the progress block in README.md from data/plan.json + data/progress.json.

Runs inside GitHub Actions on every commit (and daily) and refreshes the block
between the PROGRESS markers: "Day 45/180, 25% done, 12-day streak".

Usage:
    python scripts/update_readme.py
    python scripts/update_readme.py --today 2026-12-01   # override the date (tests)
"""

import argparse
import datetime as dt
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
START_MARK = "<!-- PROGRESS:START -->"
END_MARK = "<!-- PROGRESS:END -->"


def item_ids(day):
    ids = []
    for prefix, key in (("t", "tasks"), ("v", "videos"), ("r", "reading"), ("m", "mustKnow")):
        for i in range(len(day.get(key) or [])):
            ids.append("d%d-%s%d" % (day["day"], prefix, i + 1))
    return ids


def planned_days(plan, progress):
    """plan.json + progress.planOverrides -> ordered day list (same logic as app.js)."""
    ov = progress.get("planOverrides") or {}
    removed = {str(x) for x in (ov.get("removed") or [])}
    patched = ov.get("patched") or {}
    order_map = ov.get("order") or {}

    days, index = [], 0
    for phase in plan["phases"]:
        for d in phase.get("days") or []:
            index += 1
            if str(d["id"]) in removed:
                continue
            merged = dict(d)
            merged.update(patched.get(d["id"]) or {})
            merged["_order"] = order_map.get(d["id"], index)
            days.append(merged)
    for i, d in enumerate(ov.get("added") or []):
        merged = dict(d)
        merged["_order"] = order_map.get(d["id"], index + i + 1)
        days.append(merged)
    days.sort(key=lambda d: d["_order"])
    return days


def compute(plan, progress, today):
    start = progress.get("startDate") or plan["meta"]["startDate"]
    start_date = dt.date.fromisoformat(start)
    days = planned_days(plan, progress)

    for i, d in enumerate(days):
        planned = start_date + dt.timedelta(days=d["_order"] - 1)
        rec = (progress.get("days") or {}).get(str(d["day"])) or {}
        d["_planned"] = planned
        d["_effective"] = dt.date.fromisoformat(rec["reschedule"]) if rec.get("reschedule") else planned
        d["_ids"] = item_ids(d)
        d["_done"] = {i for i in (rec.get("items") or [])}
        d["_status"] = rec.get("status") or "pending"
        d["_minutes"] = rec.get("minutes") or 0

    total_items = sum(len(d["_ids"]) for d in days)
    done_items = sum(len([x for x in d["_ids"] if x in d["_done"]]) for d in days)
    done_days = sum(1 for d in days if d["_status"] == "done")
    skipped_days = sum(1 for d in days if d["_status"] == "skipped")
    minutes = sum(d["_minutes"] for d in days)

    # focus day: the day closest to today
    current = None
    for d in days:
        if d["_effective"] == today:
            current = d
            break
    if current is None:
        upcoming = [d for d in days if d["_effective"] > today]
        past = [d for d in days if d["_effective"] <= today]
        current = (upcoming[0] if upcoming else (past[-1] if past else (days[0] if days else None)))

    # streak: derived from the activity map
    activity = progress.get("activity") or {}
    cursor = today
    if not activity.get(cursor.isoformat()):
        cursor -= dt.timedelta(days=1)
    streak = 0
    while activity.get(cursor.isoformat()):
        streak += 1
        cursor -= dt.timedelta(days=1)

    phases = []
    for phase in plan["phases"]:
        pdays = [d for d in days if d.get("phaseId") == phase["id"]]
        p_total = sum(len(d["_ids"]) for d in pdays)
        p_done = sum(len([x for x in d["_ids"] if x in d["_done"]]) for d in pdays)
        phases.append({
            "id": phase["id"],
            "title": phase["title"],
            "done": p_done,
            "total": p_total,
            "percent": round(p_done / p_total * 100) if p_total else 0,
            "doneDays": sum(1 for d in pdays if d["_status"] == "done"),
            "days": len(pdays),
        })

    return {
        "startDate": start,
        "today": today,
        "currentDay": current["day"] if current else 0,
        "currentTopic": current["topic"] if current else "—",
        "totalDays": plan["meta"]["totalDays"],
        "totalItems": total_items,
        "doneItems": done_items,
        "percent": round(done_items / total_items * 100) if total_items else 0,
        "doneDays": done_days,
        "skippedDays": skipped_days,
        "minutes": minutes,
        "hours": round(minutes / 60),
        "streak": streak,
        "phases": phases,
    }


def render(stats):
    pct = stats["percent"]
    if stats["doneItems"] and pct == 0:
        pct_label = "<1%"
    else:
        pct_label = "%d%%" % pct
    bar_len = 30
    filled = int(round(bar_len * stats["percent"] / 100))
    bar = "█" * filled + "░" * (bar_len - filled)

    lines = [START_MARK]
    lines.append("")
    lines.append("### 📊 Gedişat (avtomatik yenilənir)")
    lines.append("")
    badge = (
        "![Progress](https://img.shields.io/badge/"
        "Gün_%d%%2F%d-%s-green?style=flat-square)"
        % (stats["currentDay"], stats["totalDays"], pct_label.replace("%", "%25"))
    )
    lines.append(badge)
    lines.append("")
    lines.append("**Gün %d/%d · %s tamamlandı · %d günlük streak**"
                 % (stats["currentDay"], stats["totalDays"], pct_label, stats["streak"]))
    lines.append("")
    lines.append("`%s`" % bar)
    lines.append("")
    lines.append("| Göstərici | Dəyər |")
    lines.append("| --- | --- |")
    lines.append("| Bugünkü mövzu | Gün %d — %s |" % (stats["currentDay"], stats["currentTopic"]))
    lines.append("| Tamamlanmış gün | %d (keçilmiş: %d) |" % (stats["doneDays"], stats["skippedDays"]))
    lines.append("| Tamamlanmış element | %d / %d |" % (stats["doneItems"], stats["totalItems"]))
    lines.append("| Ümumi öyrənmə vaxtı | %d saat |" % stats["hours"])
    lines.append("| Başlanğıc tarixi | %s |" % stats["startDate"])
    lines.append("| Son yenilənmə | %s |" % stats["today"].isoformat())
    lines.append("")
    lines.append("#### Faza gedişatı")
    lines.append("")
    lines.append("| Faza | Gedişat | Günlər |")
    lines.append("| --- | --- | --- |")
    for p in stats["phases"]:
        lines.append("| %d. %s | %d%% (%d/%d) | %d/%d |" % (
            p["id"], p["title"], p["percent"], p["done"], p["total"], p["doneDays"], p["days"]))
    lines.append("")
    lines.append(END_MARK)
    return "\n".join(lines)


def main():
    # Windows consoles may use cp1254/cp1252: force UTF-8 output
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", default=str(ROOT / "data" / "plan.json"))
    ap.add_argument("--progress", default=str(ROOT / "data" / "progress.json"))
    ap.add_argument("--readme", default=str(ROOT / "README.md"))
    ap.add_argument("--today", default=None, help="test üçün tarix (YYYY-MM-DD)")
    args = ap.parse_args()

    plan = json.loads(pathlib.Path(args.plan).read_text(encoding="utf-8"))
    progress = json.loads(pathlib.Path(args.progress).read_text(encoding="utf-8"))
    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()

    stats = compute(plan, progress, today)
    block = render(stats)

    readme_path = pathlib.Path(args.readme)
    readme = readme_path.read_text(encoding="utf-8")
    if START_MARK in readme and END_MARK in readme:
        head, rest = readme.split(START_MARK, 1)
        _, tail = rest.split(END_MARK, 1)
        new_readme = head + block + tail
    else:
        new_readme = readme.rstrip() + "\n\n" + block + "\n"

    if new_readme != readme:
        readme_path.write_text(new_readme, encoding="utf-8")
        print("README.md yeniləndi: Gün %d/%d, %s, %d gün streak"
              % (stats["currentDay"], stats["totalDays"], stats["percent"], stats["streak"]))
    else:
        print("README.md dəyişmədi.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
