from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
IMG = ROOT / "assets" / "images"
HTML = ROOT / "index.html"
IMG.mkdir(parents=True, exist_ok=True)

images = [
    ("expo-hall.jpg", "https://images.unsplash.com/photo-1761195696518-6384573549ea?auto=format&fit=crop&fm=jpg&q=80&w=1600"),
    ("business-networking.jpg", "https://images.unsplash.com/photo-1761195689615-9469b65dac01?auto=format&fit=crop&fm=jpg&q=80&w=1600"),
    ("nepal-gathering.jpg", "https://images.unsplash.com/photo-1728018848512-724893d96299?auto=format&fit=crop&fm=jpg&q=80&w=1600"),
]

for name, url in images:
    target = IMG / name
    print(f"Downloading {name}...")
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=45) as response:
        target.write_bytes(response.read())

text = HTML.read_text(encoding="utf-8")
for name, url in images:
    text = text.replace(url.replace("w=1600", "w=1400"), f"assets/images/{name}")
    text = text.replace(url, f"assets/images/{name}")
HTML.write_text(text, encoding="utf-8")
print("Done. index.html now references local image files.")
