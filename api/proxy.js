// api/proxy.js — Vercel serverless function
// Routes: rawg · rss · edgar · alphavantage · kv · default→Anthropic

export default async function handler(req, res) {
  if (req.method !== 'POST') { res.status(405).json({ error: 'Method not allowed' }); return; }
  const body = req.body || {};

  // ── RAWG ──────────────────────────────────────────────────────────
  if (body.target === 'rawg') {
    try {
      const endpoint = body.endpoint || 'games';
      const params = new URLSearchParams(body.params || {});
      params.set('key', process.env.RAWG_API_KEY);
      const url = `https://api.rawg.io/api/${endpoint}?${params.toString()}`;
      const r = await fetch(url);
      const data = await r.json();
      res.status(r.status).json(data);
    } catch (e) { res.status(500).json({ error: String(e) }); }
    return;
  }

  // ── RSS ───────────────────────────────────────────────────────────
  if (body.target === 'rss') {
    try {
      const feedUrl = body.url;
      if (!feedUrl || !/^https?:\/\//i.test(feedUrl)) { res.status(400).json({ error: 'Missing or invalid url' }); return; }
      const r = await fetch(feedUrl, {
        headers: {
          'User-Agent': 'Mozilla/5.0 (compatible; TradingIntelDashboard/1.0; +https://vercel.app)',
          'Accept': 'application/rss+xml, application/xml, text/xml, */*',
        },
      });
      if (!r.ok) { res.status(200).json({ items: [], error: `Feed returned ${r.status}` }); return; }
      const xml = await r.text();
      res.status(200).json({ items: parseRss(xml).slice(0, 40) });
    } catch (e) { res.status(200).json({ items: [], error: String(e) }); }
    return;
  }

  // ── SEC EDGAR ─────────────────────────────────────────────────────
  // Requires a descriptive User-Agent or returns 403. Rate limit: 10 req/sec combined.
  if (body.target === 'edgar') {
    const SEC_UA = 'TradingIntelligenceDashboard contact@trading-intelligence-dashboard.app';
    try {
      let url;
      if (body.edgarType === 'fulltext') {
        const params = new URLSearchParams(body.params || {});
        url = `https://efts.sec.gov/LATEST/search-index?${params.toString()}`;
      } else if (body.edgarType === 'submissions') {
        const cik = String(body.cik || '').padStart(10, '0');
        url = `https://data.sec.gov/submissions/CIK${cik}.json`;
      } else if (body.edgarType === 'filing') {
        // Fetch an individual filing document (e.g. Form 4 XML) by direct URL
        url = body.url;
        if (!url || !url.startsWith('https://www.sec.gov/')) {
          res.status(400).json({ error: 'edgarType:filing requires a valid sec.gov URL' }); return;
        }
      } else {
        res.status(400).json({ error: 'edgarType must be fulltext | submissions | filing' }); return;
      }
      const r = await fetch(url, { headers: { 'User-Agent': SEC_UA, 'Accept': '*/*' } });
      const ct = r.headers.get('content-type') || '';
      if (ct.includes('json')) {
        res.status(r.status).json(await r.json());
      } else {
        // Form 4 and similar filings return XML — pass through as text
        res.status(r.status).json({ text: await r.text() });
      }
    } catch (e) { res.status(500).json({ error: String(e) }); }
    return;
  }

  // ── Alpha Vantage ─────────────────────────────────────────────────
  // Free tier: 25 requests/day total, shared across all features.
  const AV_FUNCTIONS = ['EARNINGS_CALENDAR','TIME_SERIES_DAILY','BALANCE_SHEET','CASH_FLOW','INCOME_STATEMENT'];
  if (body.target === 'alphavantage') {
    try {
      const apiKey = process.env.ALPHA_VANTAGE_API_KEY;
      if (!apiKey) { res.status(200).json({ error: 'ALPHA_VANTAGE_API_KEY missing in Vercel environment variables' }); return; }
      const fn = body.avFunction;
      if (!AV_FUNCTIONS.includes(fn)) {
        res.status(400).json({ error: `avFunction must be one of: ${AV_FUNCTIONS.join(', ')}` }); return;
      }
      const params = new URLSearchParams(body.params || {});
      params.set('function', fn);
      params.set('apikey', apiKey);
      const url = `https://www.alphavantage.co/query?${params.toString()}`;
      const r = await fetch(url);
      if (fn === 'EARNINGS_CALENDAR') {
        res.status(200).json({ rows: parseCsv(await r.text()) });
      } else {
        res.status(200).json(await r.json());
      }
    } catch (e) { res.status(500).json({ error: String(e) }); }
    return;
  }

  // ── Upstash KV (Redis REST API) ───────────────────────────────────
  // Used for persistent balance-sheet archive across sessions/devices.
  // Env vars KV_REST_API_URL and KV_REST_API_TOKEN are injected automatically
  // by Vercel when the Upstash Redis store is connected to this project.
  if (body.target === 'kv') {
    try {
      const kvUrl = process.env.KV_REST_API_URL;
      const kvToken = process.env.KV_REST_API_TOKEN;
      if (!kvUrl || !kvToken) {
        res.status(200).json({ error: 'KV_REST_API_URL / KV_REST_API_TOKEN not set — Upstash store not yet connected' });
        return;
      }
      const { op, key, value } = body;
      let url, method = 'GET';
      if (op === 'get') {
        url = `${kvUrl}/get/${encodeURIComponent(key)}`;
      } else if (op === 'set') {
        url = `${kvUrl}/set/${encodeURIComponent(key)}/${encodeURIComponent(JSON.stringify(value))}`;
        method = 'POST';
      } else if (op === 'del') {
        url = `${kvUrl}/del/${encodeURIComponent(key)}`;
        method = 'POST';
      } else {
        res.status(400).json({ error: 'kv op must be get | set | del' }); return;
      }
      const r = await fetch(url, { method, headers: { Authorization: `Bearer ${kvToken}` } });
      const data = await r.json();
      // Upstash wraps results in { result: ... }; unwrap and parse if it's a stored JSON string
      let result = data.result;
      if (op === 'get' && typeof result === 'string') {
        try { result = JSON.parse(result); } catch {}
      }
      res.status(200).json({ result });
    } catch (e) { res.status(500).json({ error: String(e) }); }
    return;
  }

  // ── Default: Anthropic API ────────────────────────────────────────
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
  } catch (e) { res.status(500).json({ error: { message: String(e) } }); }
}

// ── CSV parser (Alpha Vantage EARNINGS_CALENDAR returns CSV not JSON) ─
function parseCsv(text) {
  const lines = text.trim().split(/\r?\n/).map(l => l.replace(/\r$/, ''));
  if (!lines.length) return [];
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
  const out = []; let cur = '', inQuotes = false;
  for (let i = 0; i < line.length; i++) {
    const c = line[i];
    if (c === '"') { inQuotes = !inQuotes; continue; }
    if (c === ',' && !inQuotes) { out.push(cur.trim()); cur = ''; continue; }
    cur += c;
  }
  out.push(cur.trim());
  return out;
}

// ── RSS/Atom parser (regex-based, no dependencies) ───────────────────
function parseRss(xml) {
  const items = [];
  const rssM = xml.matchAll(/<item[\s>][\s\S]*?<\/item>/gi);
  for (const m of rssM) items.push(extractFields(m[0]));
  if (!items.length) {
    const atomM = xml.matchAll(/<entry[\s>][\s\S]*?<\/entry>/gi);
    for (const m of atomM) items.push(extractFields(m[0], true));
  }
  return items.filter(i => i.title);
}
function extractFields(block, isAtom) {
  const get = (tag) => {
    const r = block.match(new RegExp(`<${tag}[^>]*>([\\s\\S]*?)<\\/${tag}>`, 'i'));
    if (!r) return '';
    let v = r[1].trim();
    const cd = v.match(/<!--\[CDATA\[([\s\S]*?)\]\]-->/);
    const cdata = v.match(/<!\[CDATA\[([\s\S]*?)\]\]>/);
    if (cdata) v = cdata[1].trim(); else if (cd) v = cd[1].trim();
    return v.replace(/<[^>]+>/g, '').trim();
  };
  let link = get('link');
  if (isAtom && !link) { const lm = block.match(/<link[^>]*href=["']([^"']+)["']/i); if (lm) link = lm[1]; }
  return {
    title: decodeEntities(get('title')),
    link: link || get('guid'),
    pubDate: get('pubDate') || get('pubdate') || get('published') || get('updated') || get('dc:date'),
    description: decodeEntities(get('description') || get('summary')).slice(0, 200),
  };
}
function decodeEntities(s) {
  return (s||'').replace(/&amp;/g,'&').replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&quot;/g,'"').replace(/&#0?39;/g,"'").replace(/&apos;/g,"'");
}
