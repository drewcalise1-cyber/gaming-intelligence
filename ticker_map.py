"""
TICKER_MAP — single source of truth for all files.
Every studio/subsidiary maps to its listed parent.
Add entries here; the filter logic imports this dict.

Structure:
  "search keyword (lowercase)" : {
      "parent": "Full legal parent name",
      "ticker": "PRIMARY ticker (most liquid)",
      "exchange": "Exchange name",
      "alt_tickers": ["ADR or secondary tickers"],
  }

Keywords should cover:
  - The studio's own name
  - Common abbreviations / short forms
  - Major franchise names that uniquely identify the parent
"""

TICKER_MAP = {

    # ── MICROSOFT / XBOX (MSFT) ─────────────────────────────────────────────
    # Parent is Microsoft Corp, NASDAQ: MSFT
    "microsoft":        {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "xbox":             {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "xbox game studios":{"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    # ZeniMax / Bethesda umbrella
    "zenimax":          {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "bethesda":         {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "bethesda softworks":{"parent":"Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "bethesda game studios":{"parent":"Microsoft Corp",  "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "id software":      {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "arkane":           {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "arkane studios":   {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "machine games":    {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "machinegames":     {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "obsidian":         {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "obsidian entertainment":{"parent":"Microsoft Corp", "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "inxile":           {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "inxile entertainment":{"parent":"Microsoft Corp",   "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "ninja theory":     {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "playground games": {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "turn 10":          {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "rare":             {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "rare ltd":         {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "double fine":      {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "343 industries":   {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "the coalition":    {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "compulsion games": {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "world's edge":     {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    # Activision Blizzard umbrella (acquired Oct 2023)
    "activision":       {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "activision blizzard":{"parent":"Microsoft Corp",    "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "blizzard":         {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "blizzard entertainment":{"parent":"Microsoft Corp", "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "king":             {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "king.com":         {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    # Franchise keywords uniquely tied to Microsoft
    "halo":             {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "forza":            {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "call of duty":     {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "world of warcraft":{"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "diablo":           {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "starcraft":        {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "overwatch":        {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "elder scrolls":    {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "fallout":          {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "doom":             {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "quake":            {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "candy crush":      {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "sea of thieves":   {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "grounded":         {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "hi-fi rush":       {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},
    "indiana jones":    {"parent": "Microsoft Corp",     "ticker": "MSFT", "exchange": "NASDAQ", "alt_tickers": []},

    # ── SONY GROUP (SONY / 6758.T) ──────────────────────────────────────────
    "sony":             {"parent": "Sony Group Corp",    "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    "sony group":       {"parent": "Sony Group Corp",    "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    "sony interactive entertainment": {"parent":"Sony Group Corp","ticker":"SONY","exchange":"NYSE","alt_tickers":["6758.T"]},
    "playstation":      {"parent": "Sony Group Corp",    "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    "playstation studios":{"parent":"Sony Group Corp",   "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    "sie":              {"parent": "Sony Group Corp",    "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    "naughty dog":      {"parent": "Sony Group Corp",    "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    "insomniac":        {"parent": "Sony Group Corp",    "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    "insomniac games":  {"parent": "Sony Group Corp",    "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    "guerrilla games":  {"parent": "Sony Group Corp",    "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    "guerrilla":        {"parent": "Sony Group Corp",    "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    "santa monica studio":{"parent":"Sony Group Corp",   "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    "polyphony digital":{"parent": "Sony Group Corp",    "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    "sucker punch":     {"parent": "Sony Group Corp",    "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    "sucker punch productions":{"parent":"Sony Group Corp","ticker":"SONY","exchange":"NYSE","alt_tickers":["6758.T"]},
    "housemarque":      {"parent": "Sony Group Corp",    "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    "team asobi":       {"parent": "Sony Group Corp",    "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    "bungie":           {"parent": "Sony Group Corp",    "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    "firesprite":       {"parent": "Sony Group Corp",    "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    # Franchise keywords
    "the last of us":   {"parent": "Sony Group Corp",    "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    "god of war":       {"parent": "Sony Group Corp",    "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    "spider-man":       {"parent": "Sony Group Corp",    "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    "horizon":          {"parent": "Sony Group Corp",    "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    "gran turismo":     {"parent": "Sony Group Corp",    "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    "ghost of tsushima":{"parent": "Sony Group Corp",    "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    "uncharted":        {"parent": "Sony Group Corp",    "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    "astro bot":        {"parent": "Sony Group Corp",    "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    "destiny":          {"parent": "Sony Group Corp",    "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    "helldivers":       {"parent": "Sony Group Corp",    "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},
    "intergalactic":    {"parent": "Sony Group Corp",    "ticker": "SONY", "exchange": "NYSE",   "alt_tickers": ["6758.T"]},

    # ── TAKE-TWO INTERACTIVE (TTWO) ─────────────────────────────────────────
    "take-two":         {"parent": "Take-Two Interactive","ticker":"TTWO", "exchange": "NASDAQ", "alt_tickers": []},
    "take two":         {"parent": "Take-Two Interactive","ticker":"TTWO", "exchange": "NASDAQ", "alt_tickers": []},
    "take-two interactive":{"parent":"Take-Two Interactive","ticker":"TTWO","exchange":"NASDAQ","alt_tickers":[]},
    "rockstar":         {"parent": "Take-Two Interactive","ticker":"TTWO", "exchange": "NASDAQ", "alt_tickers": []},
    "rockstar games":   {"parent": "Take-Two Interactive","ticker":"TTWO", "exchange": "NASDAQ", "alt_tickers": []},
    "2k":               {"parent": "Take-Two Interactive","ticker":"TTWO", "exchange": "NASDAQ", "alt_tickers": []},
    "2k games":         {"parent": "Take-Two Interactive","ticker":"TTWO", "exchange": "NASDAQ", "alt_tickers": []},
    "2k sports":        {"parent": "Take-Two Interactive","ticker":"TTWO", "exchange": "NASDAQ", "alt_tickers": []},
    "zynga":            {"parent": "Take-Two Interactive","ticker":"TTWO", "exchange": "NASDAQ", "alt_tickers": []},
    "ghost story games":{"parent": "Take-Two Interactive","ticker":"TTWO", "exchange": "NASDAQ", "alt_tickers": []},
    "hangar 13":        {"parent": "Take-Two Interactive","ticker":"TTWO", "exchange": "NASDAQ", "alt_tickers": []},
    "firaxis":          {"parent": "Take-Two Interactive","ticker":"TTWO", "exchange": "NASDAQ", "alt_tickers": []},
    "firaxis games":    {"parent": "Take-Two Interactive","ticker":"TTWO", "exchange": "NASDAQ", "alt_tickers": []},
    "gearbox":          {"parent": "Take-Two Interactive","ticker":"TTWO", "exchange": "NASDAQ", "alt_tickers": []},
    "gearbox software": {"parent": "Take-Two Interactive","ticker":"TTWO", "exchange": "NASDAQ", "alt_tickers": []},
    "turtle rock":      {"parent": "Take-Two Interactive","ticker":"TTWO", "exchange": "NASDAQ", "alt_tickers": []},
    # Franchises
    "grand theft auto": {"parent": "Take-Two Interactive","ticker":"TTWO", "exchange": "NASDAQ", "alt_tickers": []},
    "gta":              {"parent": "Take-Two Interactive","ticker":"TTWO", "exchange": "NASDAQ", "alt_tickers": []},
    "red dead":         {"parent": "Take-Two Interactive","ticker":"TTWO", "exchange": "NASDAQ", "alt_tickers": []},
    "nba 2k":           {"parent": "Take-Two Interactive","ticker":"TTWO", "exchange": "NASDAQ", "alt_tickers": []},
    "bioshock":         {"parent": "Take-Two Interactive","ticker":"TTWO", "exchange": "NASDAQ", "alt_tickers": []},
    "borderlands":      {"parent": "Take-Two Interactive","ticker":"TTWO", "exchange": "NASDAQ", "alt_tickers": []},
    "civilization":     {"parent": "Take-Two Interactive","ticker":"TTWO", "exchange": "NASDAQ", "alt_tickers": []},
    "mafia":            {"parent": "Take-Two Interactive","ticker":"TTWO", "exchange": "NASDAQ", "alt_tickers": []},
    "xcom":             {"parent": "Take-Two Interactive","ticker":"TTWO", "exchange": "NASDAQ", "alt_tickers": []},

    # ── ELECTRONIC ARTS (EA) ────────────────────────────────────────────────
    "electronic arts":  {"parent": "Electronic Arts",   "ticker": "EA",   "exchange": "NASDAQ", "alt_tickers": []},
    "ea":               {"parent": "Electronic Arts",   "ticker": "EA",   "exchange": "NASDAQ", "alt_tickers": []},
    "ea sports":        {"parent": "Electronic Arts",   "ticker": "EA",   "exchange": "NASDAQ", "alt_tickers": []},
    "respawn":          {"parent": "Electronic Arts",   "ticker": "EA",   "exchange": "NASDAQ", "alt_tickers": []},
    "respawn entertainment":{"parent":"Electronic Arts", "ticker": "EA",  "exchange": "NASDAQ", "alt_tickers": []},
    "bioware":          {"parent": "Electronic Arts",   "ticker": "EA",   "exchange": "NASDAQ", "alt_tickers": []},
    "dice":             {"parent": "Electronic Arts",   "ticker": "EA",   "exchange": "NASDAQ", "alt_tickers": []},
    "ea dice":          {"parent": "Electronic Arts",   "ticker": "EA",   "exchange": "NASDAQ", "alt_tickers": []},
    "maxis":            {"parent": "Electronic Arts",   "ticker": "EA",   "exchange": "NASDAQ", "alt_tickers": []},
    "criterion":        {"parent": "Electronic Arts",   "ticker": "EA",   "exchange": "NASDAQ", "alt_tickers": []},
    "codemasters":      {"parent": "Electronic Arts",   "ticker": "EA",   "exchange": "NASDAQ", "alt_tickers": []},
    "ea tiburon":       {"parent": "Electronic Arts",   "ticker": "EA",   "exchange": "NASDAQ", "alt_tickers": []},
    "cliffhanger games":{"parent": "Electronic Arts",   "ticker": "EA",   "exchange": "NASDAQ", "alt_tickers": []},
    # Franchises
    "fifa":             {"parent": "Electronic Arts",   "ticker": "EA",   "exchange": "NASDAQ", "alt_tickers": []},
    "ea fc":            {"parent": "Electronic Arts",   "ticker": "EA",   "exchange": "NASDAQ", "alt_tickers": []},
    "madden":           {"parent": "Electronic Arts",   "ticker": "EA",   "exchange": "NASDAQ", "alt_tickers": []},
    "apex legends":     {"parent": "Electronic Arts",   "ticker": "EA",   "exchange": "NASDAQ", "alt_tickers": []},
    "star wars jedi":   {"parent": "Electronic Arts",   "ticker": "EA",   "exchange": "NASDAQ", "alt_tickers": []},
    "dragon age":       {"parent": "Electronic Arts",   "ticker": "EA",   "exchange": "NASDAQ", "alt_tickers": []},
    "mass effect":      {"parent": "Electronic Arts",   "ticker": "EA",   "exchange": "NASDAQ", "alt_tickers": []},
    "the sims":         {"parent": "Electronic Arts",   "ticker": "EA",   "exchange": "NASDAQ", "alt_tickers": []},
    "battlefield":      {"parent": "Electronic Arts",   "ticker": "EA",   "exchange": "NASDAQ", "alt_tickers": []},
    "need for speed":   {"parent": "Electronic Arts",   "ticker": "EA",   "exchange": "NASDAQ", "alt_tickers": []},
    "f1":               {"parent": "Electronic Arts",   "ticker": "EA",   "exchange": "NASDAQ", "alt_tickers": []},

    # ── ROBLOX (RBLX) ───────────────────────────────────────────────────────
    "roblox":           {"parent": "Roblox Corp",       "ticker": "RBLX", "exchange": "NYSE",   "alt_tickers": []},
    "roblox corporation":{"parent":"Roblox Corp",        "ticker": "RBLX", "exchange": "NYSE",   "alt_tickers": []},

    # ── UBISOFT (UBI.PA) ────────────────────────────────────────────────────
    "ubisoft":          {"parent": "Ubisoft Entertainment","ticker":"UBI.PA","exchange":"Euronext Paris","alt_tickers":["UBSFY"]},
    "ubi":              {"parent": "Ubisoft Entertainment","ticker":"UBI.PA","exchange":"Euronext Paris","alt_tickers":["UBSFY"]},
    "ubisoft montreal": {"parent": "Ubisoft Entertainment","ticker":"UBI.PA","exchange":"Euronext Paris","alt_tickers":["UBSFY"]},
    "ubisoft paris":    {"parent": "Ubisoft Entertainment","ticker":"UBI.PA","exchange":"Euronext Paris","alt_tickers":["UBSFY"]},
    # Franchises
    "assassin's creed": {"parent": "Ubisoft Entertainment","ticker":"UBI.PA","exchange":"Euronext Paris","alt_tickers":["UBSFY"]},
    "assassins creed":  {"parent": "Ubisoft Entertainment","ticker":"UBI.PA","exchange":"Euronext Paris","alt_tickers":["UBSFY"]},
    "far cry":          {"parent": "Ubisoft Entertainment","ticker":"UBI.PA","exchange":"Euronext Paris","alt_tickers":["UBSFY"]},
    "rainbow six":      {"parent": "Ubisoft Entertainment","ticker":"UBI.PA","exchange":"Euronext Paris","alt_tickers":["UBSFY"]},
    "ghost recon":      {"parent": "Ubisoft Entertainment","ticker":"UBI.PA","exchange":"Euronext Paris","alt_tickers":["UBSFY"]},
    "the division":     {"parent": "Ubisoft Entertainment","ticker":"UBI.PA","exchange":"Euronext Paris","alt_tickers":["UBSFY"]},
    "watch dogs":       {"parent": "Ubisoft Entertainment","ticker":"UBI.PA","exchange":"Euronext Paris","alt_tickers":["UBSFY"]},
    "prince of persia": {"parent": "Ubisoft Entertainment","ticker":"UBI.PA","exchange":"Euronext Paris","alt_tickers":["UBSFY"]},
    "just dance":       {"parent": "Ubisoft Entertainment","ticker":"UBI.PA","exchange":"Euronext Paris","alt_tickers":["UBSFY"]},

    # ── CD PROJEKT (CDR.WA) ─────────────────────────────────────────────────
    "cd projekt":       {"parent": "CD Projekt SA",     "ticker": "CDR.WA","exchange":"Warsaw SE","alt_tickers":["OTGLF","OTGLY"]},
    "cd projekt red":   {"parent": "CD Projekt SA",     "ticker": "CDR.WA","exchange":"Warsaw SE","alt_tickers":["OTGLF","OTGLY"]},
    "cdpr":             {"parent": "CD Projekt SA",     "ticker": "CDR.WA","exchange":"Warsaw SE","alt_tickers":["OTGLF","OTGLY"]},
    "the witcher":      {"parent": "CD Projekt SA",     "ticker": "CDR.WA","exchange":"Warsaw SE","alt_tickers":["OTGLF","OTGLY"]},
    "cyberpunk":        {"parent": "CD Projekt SA",     "ticker": "CDR.WA","exchange":"Warsaw SE","alt_tickers":["OTGLF","OTGLY"]},

    # ── EMBRACER GROUP (EMBRAC-B.ST) ────────────────────────────────────────
    "embracer":         {"parent": "Embracer Group AB", "ticker":"EMBRAC-B.ST","exchange":"Nasdaq Stockholm","alt_tickers":[]},
    "embracer group":   {"parent": "Embracer Group AB", "ticker":"EMBRAC-B.ST","exchange":"Nasdaq Stockholm","alt_tickers":[]},
    "thq nordic":       {"parent": "Embracer Group AB", "ticker":"EMBRAC-B.ST","exchange":"Nasdaq Stockholm","alt_tickers":[]},
    "crystal dynamics": {"parent": "Embracer Group AB", "ticker":"EMBRAC-B.ST","exchange":"Nasdaq Stockholm","alt_tickers":[]},
    "eidos":            {"parent": "Embracer Group AB", "ticker":"EMBRAC-B.ST","exchange":"Nasdaq Stockholm","alt_tickers":[]},
    "eidos montreal":   {"parent": "Embracer Group AB", "ticker":"EMBRAC-B.ST","exchange":"Nasdaq Stockholm","alt_tickers":[]},
    "plaion":           {"parent": "Embracer Group AB", "ticker":"EMBRAC-B.ST","exchange":"Nasdaq Stockholm","alt_tickers":[]},
    "saber interactive":{"parent": "Embracer Group AB", "ticker":"EMBRAC-B.ST","exchange":"Nasdaq Stockholm","alt_tickers":[]},
    "dark horse":       {"parent": "Embracer Group AB", "ticker":"EMBRAC-B.ST","exchange":"Nasdaq Stockholm","alt_tickers":[]},
    "deca games":       {"parent": "Embracer Group AB", "ticker":"EMBRAC-B.ST","exchange":"Nasdaq Stockholm","alt_tickers":[]},
    # Franchises
    "tomb raider":      {"parent": "Embracer Group AB", "ticker":"EMBRAC-B.ST","exchange":"Nasdaq Stockholm","alt_tickers":[]},
    "lara croft":       {"parent": "Embracer Group AB", "ticker":"EMBRAC-B.ST","exchange":"Nasdaq Stockholm","alt_tickers":[]},
    "deus ex":          {"parent": "Embracer Group AB", "ticker":"EMBRAC-B.ST","exchange":"Nasdaq Stockholm","alt_tickers":[]},
    "metro":            {"parent": "Embracer Group AB", "ticker":"EMBRAC-B.ST","exchange":"Nasdaq Stockholm","alt_tickers":[]},
    "saints row":       {"parent": "Embracer Group AB", "ticker":"EMBRAC-B.ST","exchange":"Nasdaq Stockholm","alt_tickers":[]},

    # ── NINTENDO (7974.T) ───────────────────────────────────────────────────
    "nintendo":         {"parent": "Nintendo Co Ltd",   "ticker":"7974.T","exchange":"TSE","alt_tickers":["NTDOY"]},
    "nintendo co":      {"parent": "Nintendo Co Ltd",   "ticker":"7974.T","exchange":"TSE","alt_tickers":["NTDOY"]},
    "nintendo epd":     {"parent": "Nintendo Co Ltd",   "ticker":"7974.T","exchange":"TSE","alt_tickers":["NTDOY"]},
    # Franchises (uniquely Nintendo)
    "mario":            {"parent": "Nintendo Co Ltd",   "ticker":"7974.T","exchange":"TSE","alt_tickers":["NTDOY"]},
    "zelda":            {"parent": "Nintendo Co Ltd",   "ticker":"7974.T","exchange":"TSE","alt_tickers":["NTDOY"]},
    "the legend of zelda":{"parent":"Nintendo Co Ltd",  "ticker":"7974.T","exchange":"TSE","alt_tickers":["NTDOY"]},
    "pokemon":          {"parent": "Nintendo Co Ltd",   "ticker":"7974.T","exchange":"TSE","alt_tickers":["NTDOY"]},
    "pokémon":          {"parent": "Nintendo Co Ltd",   "ticker":"7974.T","exchange":"TSE","alt_tickers":["NTDOY"]},
    "metroid":          {"parent": "Nintendo Co Ltd",   "ticker":"7974.T","exchange":"TSE","alt_tickers":["NTDOY"]},
    "splatoon":         {"parent": "Nintendo Co Ltd",   "ticker":"7974.T","exchange":"TSE","alt_tickers":["NTDOY"]},
    "animal crossing":  {"parent": "Nintendo Co Ltd",   "ticker":"7974.T","exchange":"TSE","alt_tickers":["NTDOY"]},
    "kirby":            {"parent": "Nintendo Co Ltd",   "ticker":"7974.T","exchange":"TSE","alt_tickers":["NTDOY"]},
    "donkey kong":      {"parent": "Nintendo Co Ltd",   "ticker":"7974.T","exchange":"TSE","alt_tickers":["NTDOY"]},
    "super smash bros": {"parent": "Nintendo Co Ltd",   "ticker":"7974.T","exchange":"TSE","alt_tickers":["NTDOY"]},
    "fire emblem":      {"parent": "Nintendo Co Ltd",   "ticker":"7974.T","exchange":"TSE","alt_tickers":["NTDOY"]},
    "xenoblade":        {"parent": "Nintendo Co Ltd",   "ticker":"7974.T","exchange":"TSE","alt_tickers":["NTDOY"]},
    "switch":           {"parent": "Nintendo Co Ltd",   "ticker":"7974.T","exchange":"TSE","alt_tickers":["NTDOY"]},
    "nintendo switch":  {"parent": "Nintendo Co Ltd",   "ticker":"7974.T","exchange":"TSE","alt_tickers":["NTDOY"]},

    # ── CAPCOM (9697.T) ─────────────────────────────────────────────────────
    "capcom":           {"parent": "Capcom Co Ltd",     "ticker":"9697.T","exchange":"TSE","alt_tickers":["CCOEY","CCOEF"]},
    "resident evil":    {"parent": "Capcom Co Ltd",     "ticker":"9697.T","exchange":"TSE","alt_tickers":["CCOEY","CCOEF"]},
    "monster hunter":   {"parent": "Capcom Co Ltd",     "ticker":"9697.T","exchange":"TSE","alt_tickers":["CCOEY","CCOEF"]},
    "devil may cry":    {"parent": "Capcom Co Ltd",     "ticker":"9697.T","exchange":"TSE","alt_tickers":["CCOEY","CCOEF"]},
    "street fighter":   {"parent": "Capcom Co Ltd",     "ticker":"9697.T","exchange":"TSE","alt_tickers":["CCOEY","CCOEF"]},
    "dragon's dogma":   {"parent": "Capcom Co Ltd",     "ticker":"9697.T","exchange":"TSE","alt_tickers":["CCOEY","CCOEF"]},
    "dragons dogma":    {"parent": "Capcom Co Ltd",     "ticker":"9697.T","exchange":"TSE","alt_tickers":["CCOEY","CCOEF"]},
    "mega man":         {"parent": "Capcom Co Ltd",     "ticker":"9697.T","exchange":"TSE","alt_tickers":["CCOEY","CCOEF"]},
    "ace attorney":     {"parent": "Capcom Co Ltd",     "ticker":"9697.T","exchange":"TSE","alt_tickers":["CCOEY","CCOEF"]},

    # ── KONAMI (9766.T) ─────────────────────────────────────────────────────
    "konami":           {"parent": "Konami Holdings",   "ticker":"9766.T","exchange":"TSE","alt_tickers":["KNMCY"]},
    "metal gear":       {"parent": "Konami Holdings",   "ticker":"9766.T","exchange":"TSE","alt_tickers":["KNMCY"]},
    "silent hill":      {"parent": "Konami Holdings",   "ticker":"9766.T","exchange":"TSE","alt_tickers":["KNMCY"]},
    "castlevania":      {"parent": "Konami Holdings",   "ticker":"9766.T","exchange":"TSE","alt_tickers":["KNMCY"]},
    "pro evolution soccer":{"parent":"Konami Holdings", "ticker":"9766.T","exchange":"TSE","alt_tickers":["KNMCY"]},
    "efootball":        {"parent": "Konami Holdings",   "ticker":"9766.T","exchange":"TSE","alt_tickers":["KNMCY"]},
    "yu-gi-oh":         {"parent": "Konami Holdings",   "ticker":"9766.T","exchange":"TSE","alt_tickers":["KNMCY"]},

    # ── SQUARE ENIX (9684.T) ────────────────────────────────────────────────
    "square enix":      {"parent": "Square Enix Holdings","ticker":"9684.T","exchange":"TSE","alt_tickers":["SQNXF"]},
    "squareenix":       {"parent": "Square Enix Holdings","ticker":"9684.T","exchange":"TSE","alt_tickers":["SQNXF"]},
    "final fantasy":    {"parent": "Square Enix Holdings","ticker":"9684.T","exchange":"TSE","alt_tickers":["SQNXF"]},
    "kingdom hearts":   {"parent": "Square Enix Holdings","ticker":"9684.T","exchange":"TSE","alt_tickers":["SQNXF"]},
    "dragon quest":     {"parent": "Square Enix Holdings","ticker":"9684.T","exchange":"TSE","alt_tickers":["SQNXF"]},
    "nier":             {"parent": "Square Enix Holdings","ticker":"9684.T","exchange":"TSE","alt_tickers":["SQNXF"]},
    "octopath":         {"parent": "Square Enix Holdings","ticker":"9684.T","exchange":"TSE","alt_tickers":["SQNXF"]},
    "life is strange":  {"parent": "Square Enix Holdings","ticker":"9684.T","exchange":"TSE","alt_tickers":["SQNXF"]},

    # ── SEGA SAMMY (6460.T) ─────────────────────────────────────────────────
    "sega":             {"parent": "Sega Sammy Holdings","ticker":"6460.T","exchange":"TSE","alt_tickers":["SGAMY"]},
    "sega sammy":       {"parent": "Sega Sammy Holdings","ticker":"6460.T","exchange":"TSE","alt_tickers":["SGAMY"]},
    "atlus":            {"parent": "Sega Sammy Holdings","ticker":"6460.T","exchange":"TSE","alt_tickers":["SGAMY"]},
    "ryu ga gotoku":    {"parent": "Sega Sammy Holdings","ticker":"6460.T","exchange":"TSE","alt_tickers":["SGAMY"]},
    "sonic":            {"parent": "Sega Sammy Holdings","ticker":"6460.T","exchange":"TSE","alt_tickers":["SGAMY"]},
    "persona":          {"parent": "Sega Sammy Holdings","ticker":"6460.T","exchange":"TSE","alt_tickers":["SGAMY"]},
    "yakuza":           {"parent": "Sega Sammy Holdings","ticker":"6460.T","exchange":"TSE","alt_tickers":["SGAMY"]},
    "like a dragon":    {"parent": "Sega Sammy Holdings","ticker":"6460.T","exchange":"TSE","alt_tickers":["SGAMY"]},
    "total war":        {"parent": "Sega Sammy Holdings","ticker":"6460.T","exchange":"TSE","alt_tickers":["SGAMY"]},
    "two point":        {"parent": "Sega Sammy Holdings","ticker":"6460.T","exchange":"TSE","alt_tickers":["SGAMY"]},
    "football manager": {"parent": "Sega Sammy Holdings","ticker":"6460.T","exchange":"TSE","alt_tickers":["SGAMY"]},

    # ── BANDAI NAMCO (7832.T) ───────────────────────────────────────────────
    "bandai namco":     {"parent": "Bandai Namco Holdings","ticker":"7832.T","exchange":"TSE","alt_tickers":["BNDIY"]},
    "bandainamco":      {"parent": "Bandai Namco Holdings","ticker":"7832.T","exchange":"TSE","alt_tickers":["BNDIY"]},
    "bandai namco entertainment":{"parent":"Bandai Namco Holdings","ticker":"7832.T","exchange":"TSE","alt_tickers":["BNDIY"]},
    "tekken":           {"parent": "Bandai Namco Holdings","ticker":"7832.T","exchange":"TSE","alt_tickers":["BNDIY"]},
    "pac-man":          {"parent": "Bandai Namco Holdings","ticker":"7832.T","exchange":"TSE","alt_tickers":["BNDIY"]},
    "elden ring":       {"parent": "Bandai Namco Holdings","ticker":"7832.T","exchange":"TSE","alt_tickers":["BNDIY"]},
    "dark souls":       {"parent": "Bandai Namco Holdings","ticker":"7832.T","exchange":"TSE","alt_tickers":["BNDIY"]},
    "sekiro":           {"parent": "Bandai Namco Holdings","ticker":"7832.T","exchange":"TSE","alt_tickers":["BNDIY"]},
    "tales":            {"parent": "Bandai Namco Holdings","ticker":"7832.T","exchange":"TSE","alt_tickers":["BNDIY"]},
    "ace combat":       {"parent": "Bandai Namco Holdings","ticker":"7832.T","exchange":"TSE","alt_tickers":["BNDIY"]},
    "gundam":           {"parent": "Bandai Namco Holdings","ticker":"7832.T","exchange":"TSE","alt_tickers":["BNDIY"]},
    "little nightmares":{"parent": "Bandai Namco Holdings","ticker":"7832.T","exchange":"TSE","alt_tickers":["BNDIY"]},

    # ── KOEI TECMO (3635.T) ─────────────────────────────────────────────────
    "koei tecmo":       {"parent": "Koei Tecmo Holdings","ticker":"3635.T","exchange":"TSE","alt_tickers":["KTCMY"]},
    "koeitecmo":        {"parent": "Koei Tecmo Holdings","ticker":"3635.T","exchange":"TSE","alt_tickers":["KTCMY"]},
    "team ninja":       {"parent": "Koei Tecmo Holdings","ticker":"3635.T","exchange":"TSE","alt_tickers":["KTCMY"]},
    "ninja gaiden":     {"parent": "Koei Tecmo Holdings","ticker":"3635.T","exchange":"TSE","alt_tickers":["KTCMY"]},
    "nioh":             {"parent": "Koei Tecmo Holdings","ticker":"3635.T","exchange":"TSE","alt_tickers":["KTCMY"]},
    "dead or alive":    {"parent": "Koei Tecmo Holdings","ticker":"3635.T","exchange":"TSE","alt_tickers":["KTCMY"]},
    "dynasty warriors": {"parent": "Koei Tecmo Holdings","ticker":"3635.T","exchange":"TSE","alt_tickers":["KTCMY"]},
    "wo long":          {"parent": "Koei Tecmo Holdings","ticker":"3635.T","exchange":"TSE","alt_tickers":["KTCMY"]},

    # ── KADOKAWA / FROM SOFTWARE (9468.T) ───────────────────────────────────
    # FromSoftware is private but wholly owned by Kadokawa Corp
    "from software":    {"parent": "Kadokawa Corp",     "ticker":"9468.T","exchange":"TSE","alt_tickers":["KDKWY"]},
    "fromsoftware":     {"parent": "Kadokawa Corp",     "ticker":"9468.T","exchange":"TSE","alt_tickers":["KDKWY"]},
    "kadokawa":         {"parent": "Kadokawa Corp",     "ticker":"9468.T","exchange":"TSE","alt_tickers":["KDKWY"]},
    "armored core":     {"parent": "Kadokawa Corp",     "ticker":"9468.T","exchange":"TSE","alt_tickers":["KDKWY"]},
    "nightreign":       {"parent": "Kadokawa Corp",     "ticker":"9468.T","exchange":"TSE","alt_tickers":["KDKWY"]},
}


def resolve(name: str) -> dict | None:
    """
    Given any string (studio name, franchise, keyword),
    return its parent company info dict or None if not tradeable.
    Case-insensitive. Tries exact match first, then substring scan.
    """
    key = name.lower().strip()
    if key in TICKER_MAP:
        return TICKER_MAP[key]
    # Substring: check if any known keyword appears inside the input string
    for kw, info in TICKER_MAP.items():
        if kw in key:
            return info
    return None


def is_tradeable(name: str) -> bool:
    """Returns True if the name maps to a publicly traded parent."""
    return resolve(name) is not None


def enrich(filing: dict) -> dict:
    """
    Add ticker/parent info to a filing dict.
    Checks 'title', 'publisher', and 'detail' fields.
    Returns the same dict with added keys:
      _tradeable (bool), _parent, _ticker, _exchange, _alt_tickers
    """
    for field in ("title", "publisher", "detail"):
        val = filing.get(field, "")
        info = resolve(val)
        if info:
            filing["_tradeable"]   = True
            filing["_parent"]      = info["parent"]
            filing["_ticker"]      = info["ticker"]
            filing["_exchange"]    = info["exchange"]
            filing["_alt_tickers"] = info.get("alt_tickers", [])
            return filing
    filing["_tradeable"] = False
    return filing
