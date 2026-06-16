"""
Gaming Intelligence — Regulatory Filing Monitor (with ticker filter)
Runs every 6 hours via GitHub Actions (free).
Scrapes ESRB, PEGI, USPTO. Keeps ONLY filings that map to a publicly
traded company via ticker_map.py. Sends email alerts for new entries.
"""

import json
import os
import smtplib
import time
import urllib.request
import urllib.parse
import re
from datetime import datetime, timezone
from email.mime.text import MIMEText
from pathlib import Path

# Import the verified ticker map (same repo, same folder)
from ticker_map import enrich, is_tradeable, resolve, TICKER_MAP

# ── Configuration ────────────────────────────────────────────────────────────
GMAIL_USER        = os.environ.get("GMAIL_USER", "")
GMAIL_APP_PASSWORD= os.environ.get("GMAIL_APP_PASSWORD", "")
ALERT_TO          = os.environ.get("ALERT_EMAIL", GMAIL_USER)

DATA_FILE = Path("data/regulatory_filings.json")
SEEN_FILE = Path("data/seen_titles.json")

# Build reverse-lookup: all known keywords for fast regex matching
ALL_KEYWORDS = sorted(TICKER_MAP.keys(), key=len, reverse=True)  # longest first
KEYWORD_PATTERN = re.compile(
    r'\b(' + '|'.join(re.escape(k) for k in ALL_KEYWORDS) + r')\b',
    re.IGNORECASE
)

def fetch_url(url, headers=None, data=None, method="GET", timeout=15):
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers=headers or {"User-Agent": "Mozilla/5.0 (compatible; GamingIntelBot/1.0)"}
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  fetch error {url[:60]}: {e}")
        return ""

def load_json(path, default):
    try:
        return json.loads(path.read_text()) if path.exists() else default
    except Exception:
        return default

def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False))

def text_mentions_tradeable(text: str) -> dict | None:
    """Scan arbitrary text for any tradeable keyword. Returns info dict or None."""
    if not text:
        return None
    m = KEYWORD_PATTERN.search(text)
    if m:
        return resolve(m.group(0))
    return None

def apply_filter(filing: dict) -> dict:
    """
    Enrich filing with ticker data. Returns enriched dict.
    Sets _tradeable=True only if at least one field resolves to a listed company.
    Scans title + publisher + detail for any tradeable keyword.
    """
    # Try structured fields first
    enriched = enrich(filing)
    if enriched.get("_tradeable"):
        return enriched

    # Fallback: scan detail text for any keyword mention
    combined = " ".join([
        filing.get("title", ""),
        filing.get("publisher", ""),
        filing.get("detail", ""),
    ])
    info = text_mentions_tradeable(combined)
    if info:
        filing["_tradeable"]   = True
        filing["_parent"]      = info["parent"]
        filing["_ticker"]      = info["ticker"]
        filing["_exchange"]    = info["exchange"]
        filing["_alt_tickers"] = info.get("alt_tickers", [])
    else:
        filing["_tradeable"] = False
    return filing

# ── ESRB scraper ────────────────────────────────────────────────────────────
def scrape_esrb():
    print("Scraping ESRB...")
    filings = []
    try:
        payload = urllib.parse.urlencode({
            "action":        "get_ratings_search_page",
            "searchKeyword": "",
            "paged":         "1",
            "sortBy":        "date-desc",
        }).encode()
        raw = fetch_url(
            "https://www.esrb.org/wp-admin/admin-ajax.php",
            headers={
                "User-Agent":       "Mozilla/5.0",
                "Content-Type":     "application/x-www-form-urlencoded",
                "X-Requested-With": "XMLHttpRequest",
            },
            data=payload,
            method="POST",
        )
        try:
            data  = json.loads(raw)
            games = data.get("ratings", []) or data.get("data", {}).get("ratings", [])
        except Exception:
            games = []

        for g in games[:40]:
            title     = g.get("title", "")
            publisher = g.get("publisher", "") or g.get("company", "")
            rating    = g.get("rating", "")    or g.get("ratingSymbol", "")
            date_str  = g.get("releaseDate", "")or g.get("date", "")
            if not title:
                continue
            filing = apply_filter({
                "title":      title,
                "publisher":  publisher,
                "source":     "ESRB",
                "detail":     f"Rated {rating}" if rating else "New ESRB rating",
                "date":       date_str,
                "scraped_at": datetime.now(timezone.utc).isoformat(),
            })
            if filing["_tradeable"]:
                filing["significance"] = "high" if filing.get("_ticker") else "medium"
                filings.append(filing)

    except Exception as e:
        print(f"  ESRB error: {e}")

    print(f"  {len(filings)} tradeable ESRB entries (filtered from 40 candidates)")
    return filings

# ── PEGI scraper ─────────────────────────────────────────────────────────────
def scrape_pegi():
    print("Scraping PEGI...")
    filings = []
    try:
        html = fetch_url(
            "https://pegi.info/search-pegi?q=&filter-platform=&filter-age="
            "&filter-descriptor=&filter-publisher=&filter-release-year=&page=1"
        )
        if not html:
            return []

        titles  = re.findall(r'class=["\']game[_-]title["\'][^>]*>([^<]+)<', html, re.I)
        pubs    = re.findall(r'class=["\']publisher["\'][^>]*>([^<]+)<',      html, re.I)
        ratings = re.findall(r'class=["\']age[_-]?rating["\'][^>]*>([^<]+)<', html, re.I)
        dates   = re.findall(r'class=["\']release[_-]?date["\'][^>]*>([^<]+)<',html, re.I)

        for i, title in enumerate(titles[:30]):
            title = title.strip()
            if not title:
                continue
            publisher = pubs[i].strip()   if i < len(pubs)    else ""
            rating    = ratings[i].strip()if i < len(ratings)  else ""
            date_str  = dates[i].strip()  if i < len(dates)    else ""
            filing = apply_filter({
                "title":      title,
                "publisher":  publisher,
                "source":     "PEGI",
                "detail":     f"Rated PEGI {rating}" if rating else "New PEGI rating",
                "date":       date_str,
                "scraped_at": datetime.now(timezone.utc).isoformat(),
            })
            if filing["_tradeable"]:
                filing["significance"] = "high"
                filings.append(filing)

    except Exception as e:
        print(f"  PEGI error: {e}")

    print(f"  {len(filings)} tradeable PEGI entries")
    return filings

# ── USPTO trademark scraper ──────────────────────────────────────────────────
def scrape_uspto():
    print("Scraping USPTO trademarks (Class 41 — entertainment)...")
    filings = []
    try:
        url  = (
            "https://efts.uspto.gov/LATEST/search-index"
            "?q=%22video+game%22+%22computer+game%22"
            "&dateRangeField=filing_date&dateRange=custom"
            "&df=2025-01-01&dt=2026-12-31"
            "&type=trademark&rows=30"
        )
        raw  = fetch_url(url)
        try:
            data = json.loads(raw)
            hits = (
                data.get("hits", {}).get("hits", [])
                or data.get("results", [])
                or []
            )
        except Exception:
            hits = []

        for h in hits[:30]:
            src   = h.get("_source", h)
            title = (
                src.get("wordMark")
                or src.get("markIdentification")
                or src.get("mark_identification")
                or src.get("name", "")
            ).strip()
            owner = (src.get("ownerName") or src.get("owner_name") or "").strip()
            filed = (src.get("filingDate") or src.get("filing_date") or "").strip()
            if not title:
                continue
            filing = apply_filter({
                "title":      title,
                "publisher":  owner,
                "source":     "USPTO",
                "detail":     "Trademark application, Class 41 (entertainment / games)",
                "date":       filed,
                "scraped_at": datetime.now(timezone.utc).isoformat(),
            })
            if filing["_tradeable"]:
                filing["significance"] = "high"
                filings.append(filing)

    except Exception as e:
        print(f"  USPTO error: {e}")

    print(f"  {len(filings)} tradeable USPTO entries")
    return filings

# ── Diff & alert ─────────────────────────────────────────────────────────────
def find_new(all_filings, seen_titles):
    new = []
    for f in all_filings:
        key = f["title"].lower().strip()
        if key and key not in seen_titles:
            new.append(f)
            seen_titles.add(key)
    return new

def send_alert(new_filings):
    if not GMAIL_USER or not GMAIL_APP_PASSWORD:
        print("  Email not configured — skipping alert")
        return
    try:
        lines = [f"Gaming Intelligence — {len(new_filings)} new tradeable filing(s)\n"]
        for f in new_filings:
            ticker  = f.get("_ticker", "?")
            parent  = f.get("_parent", "?")
            exchange= f.get("_exchange", "?")
            alts    = ", ".join(f.get("_alt_tickers", []))
            lines.append(f"[{f['source']}] {f['title']}")
            lines.append(f"   Listed parent : {parent}")
            lines.append(f"   Primary ticker: {ticker} ({exchange})")
            if alts:
                lines.append(f"   Also trades as: {alts}")
            lines.append(f"   {f['detail']}")
            if f.get("date"):
                lines.append(f"   Filed: {f['date']}")
            lines.append("")

        msg = MIMEText("\n".join(lines))
        msg["Subject"] = f"[Gaming Intel] {len(new_filings)} new tradeable filing(s)"
        msg["From"]    = GMAIL_USER
        msg["To"]      = ALERT_TO

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(GMAIL_USER, GMAIL_APP_PASSWORD)
            smtp.send_message(msg)
        print(f"  Alert sent to {ALERT_TO}")
    except Exception as e:
        print(f"  Email error: {e}")

# ── Main ─────────────────────────────────────────────────────────────────────
def main():
    print(f"\n=== Gaming Intel (ticker-filtered) — {datetime.now(timezone.utc).isoformat()} ===\n")

    existing  = load_json(DATA_FILE, [])
    seen_set  = set(load_json(SEEN_FILE, []))

    fresh = []
    fresh += scrape_esrb();  time.sleep(2)
    fresh += scrape_pegi();  time.sleep(2)
    fresh += scrape_uspto()

    print(f"\nTotal tradeable filings this run: {len(fresh)}")
    new_filings = find_new(fresh, seen_set)
    print(f"New (not seen before): {len(new_filings)}")

    merged = new_filings + existing
    merged = merged[:300]

    save_json(DATA_FILE, merged)
    save_json(SEEN_FILE, list(seen_set))

    if new_filings:
        send_alert(new_filings)
    else:
        print("  No new tradeable filings — no alert sent")

    print("\nDone.\n")

if __name__ == "__main__":
    main()
