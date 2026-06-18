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
