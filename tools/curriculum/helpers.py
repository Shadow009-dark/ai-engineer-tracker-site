"""Shared helpers for authoring the 180-day AI Engineer curriculum.

Rules:
- Never invent a video URL: every YouTube entry is a search link (100% valid).
- Reading links point only to well-known stable documentation pages.
  When we are not certain of an exact article URL we use a search link.
"""

from urllib.parse import quote_plus


def yt(title, channel, duration, query):
    """A YouTube entry. Always a search link, never a guessed video id."""
    return {
        "title": title,
        "channel": channel,
        "duration": duration,
        "url": "https://www.youtube.com/results?search_query=" + quote_plus(query),
    }


def doc(title, source, url):
    """A reading entry pointing at a stable, well-known documentation page."""
    return {"title": title, "source": source, "url": url}


def gq(title, source, query):
    """A reading entry where the exact URL is not guaranteed: use a search link."""
    return {"title": title, "source": source, "url": "https://www.google.com/search?q=" + quote_plus(query)}


def day(topic, learn, videos, reading, tasks, deliverable, must, minutes=180, kind="study"):
    """One curriculum day (a study day; review days are generated automatically)."""
    return {
        "type": kind,
        "topic": topic,
        "learn": learn,
        "videos": videos,
        "reading": reading,
        "tasks": tasks,
        "deliverable": deliverable,
        "mustKnow": must,
        "minutes": minutes,
    }


def phase(pid, title, goal, hours, weeks, days):
    """A phase: metadata + ordered study days + one weekly project per week."""
    return {
        "id": pid,
        "title": title,
        "goal": goal,
        "hours": hours,
        "weeks": weeks,
        "days": days,
    }
