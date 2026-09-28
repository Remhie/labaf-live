"""Construit une version autonome (aperçu) du site, avec les données et le logo intégrés."""
import base64, json, pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
docs = root / "docs"
html = (docs / "index.html").read_text(encoding="utf8")

data = {"index.json": json.loads((docs / "data" / "index.json").read_text(encoding="utf8"))}
for f in (docs / "data" / "t").glob("*.json"):
    data["t/" + f.name] = json.loads(f.read_text(encoding="utf8"))
logo = "data:image/webp;base64," + base64.b64encode((docs / "logo.webp").read_bytes()).decode()

html = html.replace('const LOGO = "logo.webp";', 'const LOGO = "' + logo + '";')
html = html.replace('<link rel="icon" href="logo.webp">', "")
inject = "<script>window.__LABAF_DATA__ = " + json.dumps(data, ensure_ascii=False) + ";</script>\n"
html = html.replace("<script>\n(function(){", inject + "<script>\n(function(){", 1)

# L'aperçu est enveloppé automatiquement : on retire doctype/html/head/body.
html = re.sub(r"<!doctype html>\s*", "", html, flags=re.I)
html = re.sub(r"</?html[^>]*>|</?head>|</?body>", "", html)
html = re.sub(r'<meta charset="utf-8">\s*|<meta name="viewport"[^>]*>\s*', "", html)

out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else root / "preview.html")
out.write_text(html, encoding="utf8")
print(out, len(html))
