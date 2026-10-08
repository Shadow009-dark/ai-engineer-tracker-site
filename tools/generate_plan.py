"""Generate data/plan.json (180-day AI Engineer roadmap) from the curriculum modules.

Usage:
    python tools/generate_plan.py            # writes data/plan.json
    python tools/generate_plan.py --start 2026-11-01

Every 7th day is a review/rest day generated automatically from that week's topics
and its weekly project step, so the curriculum modules only author study days.
"""

import argparse
import datetime as dt
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools" / "curriculum"))

from notes import reading_note, video_note  # noqa: E402
from phase1 import PHASE as P1  # noqa: E402
from phase2 import PHASE as P2  # noqa: E402
from phase3 import PHASE as P3  # noqa: E402
from phase4 import PHASE as P4  # noqa: E402
from phase5 import PHASE as P5  # noqa: E402
from phase6 import PHASE as P6  # noqa: E402
from phase7 import PHASE as P7  # noqa: E402
from phase8 import PHASE as P8  # noqa: E402
from phase9 import PHASE as P9  # noqa: E402

PHASES = [P1, P2, P3, P4, P5, P6, P7, P8, P9]
TOTAL_DAYS = 180
STUDY_PER_WEEK = 6
REVIEW_MINUTES = 120


def review_day(week_no, focus, quiz, project, week_topics, date_iso):
    """Build the automatic weekly review/rest day."""
    sample = ", ".join(week_topics[:3])
    return {
        "type": "review",
        "date": date_iso,
        "topic": "Həftə %d təkrarı: %s" % (week_no, focus),
        "learn": [
            "Təkrar: %s" % sample,
            "Həftənin 6 mövzusunu bir-bir izah etməyə çalış (aktiv xatırlama)",
            "Anki və ya spaced repetition kartları yarat (ən azı 10 kart)",
        ],
        "videos": [
            {
                "title": "Həftə %d təkrarı üçün video (özet)" % week_no,
                "channel": "Krish Naik / StatQuest",
                "duration": "20-40 dəq",
                "url": "https://www.youtube.com/results?search_query=" + focus.replace(" ", "+"),
                "note": video_note("Krish Naik / StatQuest"),
            }
        ],
        "reading": [
            {
                "title": "Həftə %d üzrə əlavə oxu materialı" % week_no,
                "source": "Google / rəsmi sənədlər",
                "url": "https://www.google.com/search?q=" + focus.replace(" ", "+") + "+tutorial",
                "note": reading_note("Google / rəsmi sənədlər", "https://www.google.com/search?q=x"),
            }
        ],
        "tasks": [
            "Həftənin bütün 'Bilməli olduğunuz' suallarını səsli cavablandır",
            "Quiz: %s" % quiz,
            "Bu həftə gecikən tapşırıqları tamamla",
            "Həftəlik layihə addımı: %s" % project,
            "Növbəti həftənin planını nəzərdən keçir və 3 hədəf yaz",
        ],
        "deliverable": project,
        "mustKnow": [
            "Həftənin mövzularını kimsə sorsa izah edə bilirsənmi?",
            "Quiz-də 10 sualdan neçəsinə düzgün cavab verdin?",
            "Həftənin ən çətin mövzusu hansı idi və niyə?",
            "Növbəti həftə nəyi fərqli edəcəksən?",
        ],
        "minutes": REVIEW_MINUTES,
    }


def build(start_date):
    """Walk weeks: 6 study days then 1 generated review day."""
    queue = []
    for ph in PHASES:
        for d in ph["days"]:
            queue.append((ph, d))

    plan_phases = []
    for ph in PHASES:
        plan_phases.append(
            {
                "id": ph["id"],
                "title": ph["title"],
                "goal": ph["goal"],
                "hours": ph["hours"],
                "weeks": [
                    {"week": i + 1, "focus": w["focus"], "project": w["project"],
                     "quiz": w["quiz"]}
                    for i, w in enumerate(ph["weeks"])
                ],
                "days": [],
            }
        )

    phase_of_week = []
    for ph in PHASES:
        phase_of_week.extend([ph["id"]] * len(ph["weeks"]))
    assert len(phase_of_week) == 26, "expected 26 weeks, got %d" % len(phase_of_week)

    week_plan = {}
    day_no = 0
    study_count = 0

    for week_no in range(1, 27):
        phase_id = phase_of_week[week_no - 1]
        phase = [p for p in PHASES if p["id"] == phase_id][0]
        week_meta = phase["weeks"][week_no - 1 - sum(len(p["weeks"]) for p in PHASES if p["id"] < phase_id)]

        week_topics = []
        for _ in range(STUDY_PER_WEEK):
            if not queue:
                break
            ph, d = queue.pop(0)
            day_no += 1
            study_count += 1
            week_topics.append(d["topic"])
            day = dict(d)
            # attach a short Azerbaijani note to every English resource
            day["videos"] = [dict(v, note=video_note(v["channel"])) for v in d["videos"]]
            day["reading"] = [dict(r, note=reading_note(r.get("source", ""), r["url"])) for r in d["reading"]]
            day["day"] = day_no
            day["id"] = "d%d" % day_no
            day["week"] = week_no
            day["phaseId"] = ph["id"]
            day["phaseTitle"] = ph["title"]
            day["date"] = (start_date + dt.timedelta(days=day_no - 1)).isoformat()
            for k, v in [("learn", []), ("videos", []), ("reading", []),
                         ("tasks", []), ("mustKnow", [])]:
                assert len(day.get(k, [])) > 0, "day %d missing %s" % (day_no, k)
            assert day["type"] == "study"
            target = [p for p in plan_phases if p["id"] == ph["id"]][0]
            target["days"].append(day)

        # weekly review day
        day_no += 1
        rev = review_day(
            week_no,
            week_meta["focus"],
            week_meta["quiz"],
            week_meta["project"],
            week_topics,
            (start_date + dt.timedelta(days=day_no - 1)).isoformat(),
        )
        rev["day"] = day_no
        rev["id"] = "d%d" % day_no
        rev["week"] = week_no
        rev["phaseId"] = phase_id
        rev["phaseTitle"] = phase["title"]
        target = [p for p in plan_phases if p["id"] == phase_id][0]
        target["days"].append(rev)

    assert day_no == TOTAL_DAYS, "expected %d days, got %d" % (TOTAL_DAYS, day_no)
    assert not queue, "unused study days left: %d" % len(queue)

    total_minutes = sum(
        d["minutes"] for p in plan_phases for d in p["days"]
    )
    meta = {
        "title": "180 Günlük AI Engineer Yol Xəritəsi",
        "description": "Sıfırdan AI Engineer səviyyəsinə aparan 6 aylıq gündəlik plan.",
        "totalDays": TOTAL_DAYS,
        "startDate": start_date.isoformat(),
        "hoursPerDay": "2-4 saat",
        "totalHours": round(total_minutes / 60),
        "repo": "Shadow009-dark/ai-engineer-tracker",
        "githubUser": "Shadow009-dark",
        "language": "az",
        "generatedBy": "tools/generate_plan.py",
        "note": "Tarixlər başlanğıc tarixindən avtomatik hesablanır; sayt içindən dəyişdirilə bilər.",
    }
    stats = {
        "phases": len(plan_phases),
        "weeks": 26,
        "studyDays": study_count,
        "reviewDays": TOTAL_DAYS - study_count,
        "tasks": sum(len(d["tasks"]) for p in plan_phases for d in p["days"]),
        "videos": sum(len(d["videos"]) for p in plan_phases for d in p["days"]),
        "readings": sum(len(d["reading"]) for p in plan_phases for d in p["days"]),
        "mustKnow": sum(len(d["mustKnow"]) for p in plan_phases for d in p["days"]),
        "totalMinutes": total_minutes,
    }
    return {"meta": meta, "stats": stats, "phases": plan_phases}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", default="2026-10-08", help="start date (YYYY-MM-DD)")
    ap.add_argument("--out", default=str(ROOT / "data" / "plan.json"))
    args = ap.parse_args()

    start = dt.date.fromisoformat(args.start)
    plan = build(start)

    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    size_kb = out.stat().st_size / 1024
    print("wrote %s (%.0f KB)" % (out, size_kb))
    print("days=%d study=%d review=%d tasks=%d videos=%d readings=%d mustKnow=%d" % (
        plan["meta"]["totalDays"], plan["stats"]["studyDays"], plan["stats"]["reviewDays"],
        plan["stats"]["tasks"], plan["stats"]["videos"], plan["stats"]["readings"],
        plan["stats"]["mustKnow"]))
    print("hours~%d" % plan["meta"]["totalHours"])


if __name__ == "__main__":
    main()
