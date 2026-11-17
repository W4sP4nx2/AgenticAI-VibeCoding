import sys
from datetime import date
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from build_calendar import day_cell, sanitize_calendar_url


@pytest.mark.parametrize(
    ("url", "field", "expected"),
    [
        ("", "teams_url", ""),
        ("   ", "form_url", ""),
        (
            "https://events.teams.microsoft.com/event/123?id=abc&lang=en",
            "teams_url",
            "https://events.teams.microsoft.com/event/123?id=abc&amp;lang=en",
        ),
        (
            "https://forms.cloud.microsoft/r/xyz987",
            "form_url",
            "https://forms.cloud.microsoft/r/xyz987",
        ),
        (
            "https://forms.cloud.microsoft:443/r/xyz987",
            "form_url",
            "https://forms.cloud.microsoft:443/r/xyz987",
        ),
    ],
)
def test_accepts_valid_and_empty_urls(url, field, expected):
    assert sanitize_calendar_url(url, field) == expected


@pytest.mark.parametrize(
    ("bad_url", "field"),
    [
        ("http://events.teams.microsoft.com/event/123", "teams_url"),
        ("javascript:alert(1)", "teams_url"),
        ("data:text/html,<script>alert(1)</script>", "form_url"),
        ("https://events.teams.microsoft.com.evil.tld/phish", "teams_url"),
        ("https://evil.tld/https://forms.cloud.microsoft", "form_url"),
        ("https://user:pass@forms.cloud.microsoft/r/xyz", "form_url"),
        ("https://forms.cloud.microsoft:8443/r/xyz", "form_url"),
        ("https://forms.cloud.microsoft/r/xyz\r\nSet-Cookie:a=b", "form_url"),
        ("\nhttps://forms.cloud.microsoft/r/xyz", "form_url"),
        ("https://forms.cloud.microsoft/r/xyz\t", "form_url"),
        ("https://forms.cloud.microsoft/r/xy z", "form_url"),
        ("https://forms.cloud.microsoft:not-a-port/r/xyz", "form_url"),
        ("https://events.teams.microsoft.com/event/123", "form_url"),
    ],
)
def test_rejects_malicious_or_unapproved_urls(bad_url, field):
    with pytest.raises(ValueError):
        sanitize_calendar_url(bad_url, field)


def test_day_cell_rejects_an_unapproved_session_link():
    row = {
        "day": date(2026, 11, 17),
        "time": "18:30",
        "title": "Example session",
        "session_url": "https://evil.example/session",
        "form_url": "",
    }

    with pytest.raises(ValueError, match="Unapproved host"):
        day_cell(row["day"], row, "session")
