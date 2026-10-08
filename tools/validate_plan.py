"""Validate data/plan.json: structure, counts, links and Azerbaijani content rules.

Usage:
    python tools/validate_plan.py
"""

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PLAN = ROOT / "data" / "plan.json"
MINUTES_MIN, MINUTES_MAX = 100, 300
REQUIRED = ["id", "day", "week", "phaseId", "phaseTitle", "type", "date", "topic",
            "learn", "videos", "reading", "tasks", "deliverable", "mustKnow", "minutes"]

errors = []
warnings = []


def check(cond, msg):
    if not cond:
        errors.append(msg)


def main():
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    meta, stats, phases = plan["meta"], plan["stats"], plan["phases"]

    check(meta["totalDays"] == 180, "meta.totalDays != 180")
    check(len(phases) == 9, "expected 9 phases, got %d" % len(phases))
    check(stats["weeks"] == 26, "expected 26 weeks")

    days = [d for p in phases for d in p["days"]]
    check(len(days) == 180, "expected 180 days, got %d" % len(days))
    check([d["day"] for d in days] == list(range(1, 181)), "day numbers are not 1..180 in order")

    video_urls, reading_urls, search_hosts = set(), set(), {}
    total_videos, total_readings = 0, 0
    # review days are the last day of every week: 7, 14, ... 175 and day 180
    review_days = set(range(7, 176, 7)) | {180}
    for d in days:
        n = d["day"]
        for key in REQUIRED:
            check(key in d, "day %d missing key %s" % (n, key))
        check(d["type"] in ("study", "review"), "day %d bad type" % n)
        check(MINUTES_MIN <= d["minutes"] <= MINUTES_MAX, "day %d minutes out of range" % n)
        check(len(d["topic"]) >= 5, "day %d topic too short" % n)
        check(3 <= len(d["learn"]) <= 6, "day %d learn count %d" % (n, len(d["learn"])))
        check(1 <= len(d["videos"]) <= 3, "day %d videos count %d" % (n, len(d["videos"])))
        check(1 <= len(d["reading"]) <= 3, "day %d reading count %d" % (n, len(d["reading"])))
        check(3 <= len(d["tasks"]) <= 6, "day %d tasks count %d" % (n, len(d["tasks"])))
        check(3 <= len(d["mustKnow"]) <= 5, "day %d mustKnow count %d" % (n, len(d["mustKnow"])))
        check(bool(d["deliverable"].strip()), "day %d empty deliverable" % n)
        check(bool(re.search(r"[a-zA-ZəğıöşüçƏĞİÖŞÜÇ]", d["topic"])), "day %d topic not text" % n)
        for item in d["learn"] + d["tasks"] + d["mustKnow"]:
            check(bool(item.strip()), "day %d has empty text item" % n)
            check(not re.search(r"[А-Яа-я]", item), "day %d contains cyrillic text" % n)
        for v in d["videos"]:
            check(v["url"].startswith("https://www.youtube.com/results?search_query="),
                  "day %d video is not a search link: %s" % (n, v["url"]))
            check(" " not in v["url"], "day %d video url contains raw spaces" % n)
            video_urls.add(v["url"])
            total_videos += 1
            check(bool(v["title"]) and bool(v["channel"]) and bool(v["duration"]),
                  "day %d video missing metadata" % n)
            check(len(v.get("note", "")) > 20, "day %d video missing Azerbaijani note" % n)
        for r in d["reading"]:
            check(r["url"].startswith("http"), "day %d reading url not http: %s" % (n, r["url"]))
            check(" " not in r["url"], "day %d reading url contains raw spaces" % n)
            check(len(r.get("note", "")) > 20, "day %d reading missing Azerbaijani note" % n)
            reading_urls.add(r["url"])
            total_readings += 1
            host = r["url"].split("/")[2]
            search_hosts[host] = search_hosts.get(host, 0) + 1
            check(not r["url"].endswith(" "), "day %d reading url has trailing space" % n)
        # weekly review days are the last day of each week
        check((d["type"] == "review") == (n in review_days),
              "day %d has wrong type for its position" % n)

    # phase/date sanity
    check(len(set(d["date"] for d in days)) == 180, "duplicate dates found")
    check(days[0]["date"] == meta["startDate"], "first day date != meta.startDate")
    check(sum(len(d["tasks"]) for d in days) == stats["tasks"], "task stat mismatch")
    check(total_videos == stats["videos"], "video stat mismatch")
    check(total_readings == stats["readings"], "reading stat mismatch")
    check(sum(len(d["mustKnow"]) for d in days) == stats["mustKnow"], "mustKnow stat mismatch")

    # every reading link must be either a Google search link or a real doc page on a
    # domain with a dot in it and no whitespace
    for url in reading_urls:
        check(url.startswith("https://"), "reading url not https: %s" % url)
        check("." in url.split("/")[2], "reading url has no dot in host: %s" % url)
        check("youtube.com" not in url, "video links must not appear in reading: %s" % url)

    # plausible duration strings for videos
    for p in phases:
        for d in p["days"]:
            for v in d["videos"]:
                check(len(v["duration"]) <= 12, "day %d duration too long: %s" % (d["day"], v["duration"]))

    print("days=%d phases=%d" % (len(days), len(phases)))
    print("unique videos=%d unique readings=%d" % (len(video_urls), len(reading_urls)))
    print("reading hosts:", ", ".join(sorted(search_hosts)))
    per_phase = [(p["id"], len(p["days"]), sum(1 for d in p["days"] if d["type"] == "review"))
                 for p in phases]
    print("phase days (total, review):", per_phase)
    if warnings:
        print("\nWARNINGS:")
        for w in warnings:
            print(" -", w)
    if errors:
        print("\nERRORS (%d):" % len(errors))
        for e in errors[:60]:
            print(" -", e)
        return 1
    print("\nOK: plan.json passed all structural checks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
