import json
import urllib.request
from pathlib import Path

HANDLE = "mahajanram_15"
OUT = Path("assets/codechef-stats.svg")
URL = f"https://cp-rating-api.vercel.app/codechef/{HANDLE}"

req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=30) as response:
    data = json.loads(response.read().decode("utf-8"))

def get(*keys):
    for key in keys:
        if data.get(key) not in (None, ""):
            return data[key]
    return "—"

def fmt(value):
    try:
        return f"{int(value):,}"
    except Exception:
        return str(value)

rating = fmt(get("rating"))
stars = get("stars", "star")
problems = fmt(get("problemsSolved", "problems_solved"))
contests = get("participation", "contestsCount")
if contests == "—" and isinstance(data.get("contests"), list):
    contests = len(data["contests"])
contests = fmt(contests)
global_rank = fmt(get("globalRank", "global_rank"))
country_rank = fmt(get("countryRank", "country_rank"))

svg = """<svg xmlns="http://www.w3.org/2000/svg" width="500" height="330" viewBox="0 0 500 330">
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#111318"/><stop offset="100%" stop-color="#191c24"/></linearGradient></defs>
<rect x="1" y="1" width="498" height="328" rx="12" fill="url(#bg)" stroke="#30343d" stroke-width="2"/>
<text x="250" y="43" text-anchor="middle" font-family="Arial,sans-serif" font-size="24" font-weight="700" fill="#f2f4f7">CodeChef</text>
<text x="250" y="70" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" fill="#b7bdc9">mahajanram_15</text>
<line x1="32" y1="88" x2="468" y2="88" stroke="#30343d"/>
<text x="70" y="125" font-family="Arial,sans-serif" font-size="13" fill="#8f96a3">RATING</text>
<text x="70" y="153" font-family="Arial,sans-serif" font-size="25" font-weight="700" fill="#f6a800">__RATING__</text>
<text x="70" y="175" font-family="Arial,sans-serif" font-size="14" fill="#f6a800">&#9733; __STARS__ Star</text>
<text x="250" y="125" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" fill="#8f96a3">PROBLEMS SOLVED</text>
<text x="250" y="153" text-anchor="middle" font-family="Arial,sans-serif" font-size="25" font-weight="700" fill="#f2f4f7">__PROBLEMS__</text>
<text x="430" y="125" text-anchor="end" font-family="Arial,sans-serif" font-size="13" fill="#8f96a3">CONTESTS</text>
<text x="430" y="153" text-anchor="end" font-family="Arial,sans-serif" font-size="25" font-weight="700" fill="#f2f4f7">__CONTESTS__</text>
<line x1="32" y1="195" x2="468" y2="195" stroke="#30343d"/>
<text x="70" y="225" font-family="Arial,sans-serif" font-size="13" fill="#8f96a3">GLOBAL RANK</text>
<text x="70" y="251" font-family="Arial,sans-serif" font-size="20" font-weight="700" fill="#f2f4f7">__GLOBAL__</text>
<text x="430" y="225" text-anchor="end" font-family="Arial,sans-serif" font-size="13" fill="#8f96a3">COUNTRY RANK</text>
<text x="430" y="251" text-anchor="end" font-family="Arial,sans-serif" font-size="20" font-weight="700" fill="#f2f4f7">__COUNTRY__</text>
<a href="https://www.codechef.com/users/mahajanram_15"><rect x="150" y="274" width="200" height="34" rx="7" fill="#5b4638"/><text x="250" y="296" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="600" fill="#ffffff">View CodeChef Profile</text></a>
</svg>"""

svg = (svg.replace("__RATING__", rating)
          .replace("__STARS__", str(stars))
          .replace("__PROBLEMS__", problems)
          .replace("__CONTESTS__", contests)
          .replace("__GLOBAL__", global_rank)
          .replace("__COUNTRY__", country_rank))

OUT.write_text(svg, encoding="utf-8")
