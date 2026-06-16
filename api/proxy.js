// api/proxy.js
// Routes requests to either Anthropic or RAWG based on the 'target' field.

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { target, ...body } = req.body || {};

  // ── RAWG Video Games Database ─────────────────────────────────────────────
  if (target === 'rawg') {
    const rawgKey = process.env.RAWG_API_KEY;
    if (!rawgKey) {
      return res.status(500).json({ error: 'RAWG_API_KEY not configured on server' });
    }
    try {
      const params = new URLSearchParams({ ...body.params, key: rawgKey });
      const url = `https://api.rawg.io/api/${body.endpoint}?${params}`;
      const r = await fetch(url, { headers: { 'User-Agent': 'GamingIntelligence/1.0' } });
      const data = await r.json();
      return res.status(r.status).json(data);
    } catch (err) {
      return res.status(500).json({ error: err.message });
    }
  }

  // ── Anthropic Claude ──────────────────────────────────────────────────────
  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (!apiKey) {
    return res.status(500).json({ error: 'ANTHROPIC_API_KEY not configured on server' });
  }
  try {
    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type':      'application/json',
        'x-api-key':         apiKey,
        'anthropic-version': '2023-06-01',
      },
      body: JSON.stringify(body),
    });
    const data = await response.json();
    return res.status(response.status).json(data);
  } catch (err) {
    return res.status(500).json({ error: err.message });
  }
}
