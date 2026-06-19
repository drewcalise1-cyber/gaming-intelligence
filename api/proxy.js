// api/proxy.js — Vercel serverless function
// Routes: target:'rawg' → RAWG API · target:'rss' → server-side RSS fetch (avoids CORS) · default → Anthropic API

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    res.status(405).json({ error: 'Method not allowed' });
    return;
  }

  const body = req.body || {};

  // ── RAWG passthrough ──────────────────────────────────────────────
  if (body.target === 'rawg') {
    try {
      const endpoint = body.endpoint || 'games';
      const params = new URLSearchParams(body.params || {});
      params.set('key', process.env.RAWG_API_KEY);
      const url = `https://api.rawg.io/api/${endpoint}?${params.toString()}`;
      const r = await fetch(url);
      const data = await r.json();
      res.status(r.status).json(data);
    } catch (e) {
      res.status(500).json({ error: String(e) });
    }
    return;
  }

  // ── RSS passthrough (server-side fetch avoids browser CORS) ───────
  if (body.target === 'rss') {
    try {
      const feedUrl = body.url;
      if (!feedUrl || !/^https?:\/\//i.test(feedUrl)) {
        res.status(400).json({ error: 'Missing or invalid url' });
        return;
      }
      const r = await fetch(feedUrl, {
        headers: {
          'User-Agent': 'Mozilla/5.0 (compatible; GamingIntelDashboard/1.0; +https://vercel.app)',
          'Accept': 'application/rss+xml, application/xml, text/xml, */*',
        },
      });
      if (!r.ok) {
        res.status(200).json({ items: [], error: `Feed returned ${r.status}` });
        return;
      }
      const xml = await r.text();
      const items = parseRss(xml);
      res.status(200).json({ items: items.slice(0, 40) });
    } catch (e) {
      res.status(200).json({ items: [], error: String(e) });
    }
    return;
  }

  // ── SEC EDGAR passthrough ───────────────────────────────────────────
  // SEC requires a descriptive User-Agent (name + contact) on every request,
  // or it returns 403. Also enforces a combined 10 req/sec rate limit across
  // all EDGAR endpoints — callers should space out requests, not fire bursts.
  if (body.target === 'edgar') {
    const SEC_USER_AGENT = 'GamingIntelligenceDashboard contact@gaming-intelligence-dashboard.app';
    try {
      let url;
      if (body.edgarType === 'fulltext') {
        // Full-text search across all EDGAR filings since 2001
        const params = new URLSearchParams(body.params || {});
        url = `https://efts.sec.gov/LATEST/search-index?${params.toString()}`;
      } else if (body.edgarType === 'submissions') {
        // Per-company filing history, e.g. CIK0000789019.json
        const cik = String(body.cik || '').padStart(10, '0');
        url = `https://data.sec.gov/submissions/CIK${cik}.json`;
      } else {
        res.status(400).json({ error: 'edgarType must be "fulltext" or "submissions"' });
        return;
      }
      const r = await fetch(url, {
        headers: {
          'User-Agent': SEC_USER_AGENT,
          'Accept': 'application/json',
        },
      });
      const data = await r.json();
      res.status(r.status).json(data);
    } catch (e) {
      res.status(500).json({ error: String(e) });
    }
    return;
  }

  // ── Alpha Vantage passthrough ───────────────────────────────────────
  // Free tier: 25 requests/day total, 5/minute, shared across every feature
  // using this key (earnings calendar AND backtester price history both
  // draw from the same budget) — callers should cache aggressively client-side.
  if (body.target === 'alphavantage') {
    try {
      const apiKey = process.env.ALPHA_VANTAGE_API_KEY;
      if (!apiKey) {
        res.status(200).json({ error: 'ALPHA_VANTAGE_API_KEY missing in Vercel environment variables' });
        return;
      }
      const fn = body.avFunction;
      if (fn !== 'EARNINGS_CALENDAR' && fn !== 'TIME_SERIES_DAILY') {
        res.status(400).json({ error: 'avFunction must be "EARNINGS_CALENDAR" or "TIME_SERIES_DAILY"' });
        return;
      }
      const params = new URLSearchParams(body.params || {});
      params.set('function', fn);
      params.set('apikey', apiKey);
      const url = `https://www.alphavantage.co/query?${params.toString()}`;
      const r = await fetch(url);

      if (fn === 'EARNINGS_CALENDAR') {
        // This endpoint returns CSV (unlike most Alpha Vantage endpoints, which
        // return JSON) — parse server-side so the client always gets JSON back.
        const csvText = await r.text();
        const rows = parseCsv(csvText);
        res.status(200).json({ rows });
      } else {
        const data = await r.json();
        res.status(200).json(data);
      }
    } catch (e) {
      res.status(500).json({ error: String(e) });
    }
    return;
  }

  // ── Default: Anthropic API ─────────────────────────────────────────
  try {
    const r = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': process.env.ANTHROPIC_API_KEY,
        'anthropic-version': '2023-06-01',
      },
      body: JSON.stringify(body),
    });
    const data = await r.json();
    res.status(r.status).json(data);
  } catch (e) {
    res.status(500).json({ error: { message: String(e) } });
  }
}

// ── Minimal RSS/Atom parser (regex-based, no dependencies) ──────────
// ── Minimal CSV parser (for Alpha Vantage EARNINGS_CALENDAR, the one
// endpoint on that API that returns CSV instead of JSON) ────────────
function parseCsv(text) {
  const lines = text.trim().split(/\r?\n/);
  if (lines.length < 1) return [];
  const headers = splitCsvLine(lines[0]);
  const rows = [];
  for (let i = 1; i < lines.length; i++) {
    if (!lines[i].trim()) continue;
    const fields = splitCsvLine(lines[i]);
    const row = {};
    headers.forEach((h, idx) => { row[h] = fields[idx] !== undefined ? fields[idx] : ''; });
    rows.push(row);
  }
  return rows;
}
function splitCsvLine(line) {
  // Basic quoted-field handling — company names can contain commas (e.g. "Take-Two Interactive, Inc.")
  const out = [];
  let cur = '', inQuotes = false;
  for (let i = 0; i < line.length; i++) {
    const c = line[i];
    if (c === '"') { inQuotes = !inQuotes; continue; }
    if (c === ',' && !inQuotes) { out.push(cur); cur = ''; continue; }
    cur += c;
  }
  out.push(cur);
  return out;
}

function parseRss(xml) {
  const items = [];
  const rssMatches = xml.matchAll(/<item[\s>][\s\S]*?<\/item>/gi);
  for (const m of rssMatches) {
    items.push(extractFields(m[0]));
  }
  if (items.length === 0) {
    const atomMatches = xml.matchAll(/<entry[\s>][\s\S]*?<\/entry>/gi);
    for (const m of atomMatches) {
      items.push(extractFields(m[0], true));
    }
  }
  return items.filter(i => i.title);
}

function extractFields(block, isAtom) {
  const get = (tag) => {
    const r = block.match(new RegExp(`<${tag}[^>]*>([\\s\\S]*?)<\\/${tag}>`, 'i'));
    if (!r) return '';
    let v = r[1].trim();
    const cdata = v.match(/<!\[CDATA\[([\s\S]*?)\]\]>/);
    if (cdata) v = cdata[1].trim();
    return v.replace(/<[^>]+>/g, '').trim();
  };
  let link = get('link');
  if (isAtom && !link) {
    const linkTag = block.match(/<link[^>]*href=["']([^"']+)["']/i);
    if (linkTag) link = linkTag[1];
  }
  const pubDate = get('pubDate') || get('pubdate') || get('published') || get('updated') || get('dc:date');
  return {
    title: decodeEntities(get('title')),
    link: link || get('guid'),
    pubDate,
    source: get('source') || '',
    description: decodeEntities(get('description') || get('summary')).slice(0, 200),
  };
}

function decodeEntities(s) {
  return (s || '')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#0?39;/g, "'")
    .replace(/&apos;/g, "'");
}
