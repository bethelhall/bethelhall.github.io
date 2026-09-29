"""Render the complete-policy repair comparison from CloudFix, Table III."""
from html import escape
from pathlib import Path

SOURCE = 'https://arxiv.org/html/2512.09957v2#S5.T3'
# Published percentages, not request-level classification accuracy.
ROWS = [(10, 48.2, 84.0), (20, 52.8, 60.3), (30, 22.3, 54.3), (50, 0.0, 2.5)]
X0, SCALE = 180, 8.4
parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="600" viewBox="0 0 1200 600" role="img" aria-labelledby="title desc">
  <title id="title">Complete policy repair rates</title>
  <desc id="desc">282 AWS policies. Baseline versus CloudFix: 10 requests, 48.2% versus 84.0%; 20 requests, 52.8% versus 60.3%; 30 requests, 22.3% versus 54.3%; 50 requests, 0.0% versus 2.5%. Complete repair means satisfying every supplied request specification. Source: CloudFix, Table III.</desc>
  <metadata>Source: {escape(SOURCE)}. Percent of 282 policies completely repaired in each request-size experiment.</metadata>
  <rect width="1200" height="600" fill="white"/>
  <g font-family="Arial, sans-serif" fill="#171717">
    <text x="30" y="44" font-size="32" font-weight="bold">Complete policy repair rates</text>
    <text x="30" y="82" font-size="24" fill="#4a4a4a">282 AWS policies; all supplied requests satisfied</text>
    <rect x="800" y="25" width="26" height="22" fill="#d6dfe7" stroke="#6b7b89"/>
    <text x="838" y="44" font-size="24">Baseline</text>
    <rect x="978" y="25" width="26" height="22" fill="#0077b6"/>
    <text x="1016" y="44" font-size="24">CloudFix</text>
    <text x="145" y="127" text-anchor="end" font-size="22" fill="#4a4a4a">Requests</text>''']
for tick in [0, 25, 50, 75, 100]:
    x = X0 + tick * SCALE
    parts.append(f'    <line x1="{x}" y1="138" x2="{x}" y2="515" stroke="#e3e0da"/>')
    parts.append(f'    <text x="{x}" y="551" text-anchor="middle" font-size="23" fill="#4a4a4a">{tick}%</text>')
for index, (requests, baseline, cloudfix) in enumerate(ROWS):
    y = 150 + index * 94
    parts.append(f'    <text x="145" y="{y + 32}" text-anchor="end" font-size="28">{requests}</text>')
    for offset, value, color, stroke in [(0, baseline, '#d6dfe7', '#6b7b89'), (34, cloudfix, '#0077b6', '#0077b6')]:
        bar_y = y + offset
        if value:
            parts.append(f'    <rect x="{X0}" y="{bar_y}" width="{value * SCALE:.2f}" height="24" fill="{color}" stroke="{stroke}"/>')
        parts.append(f'    <text x="{X0 + value * SCALE + 12:.2f}" y="{bar_y + 21}" font-size="25">{value:.1f}%</text>')
parts.append('''    <text x="30" y="589" font-size="21" fill="#4a4a4a">Source: CloudFix, Table III (arXiv:2512.09957v2)</text>
  </g>
</svg>
''')
output = Path(__file__).resolve().parents[1] / 'images/web_fig/cloudfix_repair_rates.svg'
output.write_text('\n'.join(parts))
print(output)
