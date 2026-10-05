#!/usr/bin/env python3
"""Descarga el directorio oficial de Multiplaza Escazú y Curridabat (multiplaza.com)
y guarda los datos de cada local (nombre, logo, descripción, ubicación, horario,
teléfono, correo, redes, categorías) en datos/multiplaza/.

Se ejecuta desde GitHub Actions (ver .github/workflows/scrape-multiplaza.yml).
"""
import json, os, re, sys, time, io, hashlib
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
from PIL import Image

BASE = "https://multiplaza.com"
MALLS = ["escazu", "curridabat"]
OUT = "datos/multiplaza"
RAW = f"{OUT}/raw"
LOGOS = f"{OUT}/logos"
DELAY = 0.4
S = requests.Session()
S.headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36 (directorio-locales; contacto: lynconcept.cr@gmail.com)",
                  "Accept-Language": "es-CR,es;q=0.9"})

def get(url, tries=3):
    for i in range(tries):
        try:
            r = S.get(url, timeout=40)
            if r.status_code == 200:
                return r
            print("HTTP", r.status_code, url, file=sys.stderr)
            if r.status_code in (403, 404, 410):
                return r
        except Exception as e:
            print("ERR", url, e, file=sys.stderr)
        time.sleep(2 * (i + 1))
    return None

def main_area(soup):
    for sel in ("main", "#main", ".main", "section", "body"):
        el = soup.select_one(sel)
        if el:
            return el
    return soup

def store_links(soup, mall):
    pat = re.compile(rf"^https?://(www\.)?multiplaza\.com/{mall}/(tiendas|restaurantes|tienda|restaurante)/([^/?#]+)/?$")
    found = {}
    for a in soup.find_all("a", href=True):
        href = urljoin(BASE, a["href"].strip())
        m = pat.match(href)
        if m:
            found[href.rstrip("/")] = (m.group(2), m.group(3))
    return found

def is_store_slug(slug, mall):
    return slug.endswith(f"-multiplaza-{mall}")

def text(el):
    return re.sub(r"\s+", " ", el.get_text(" ", strip=True)) if el else ""

def parse_store(html, url, mall):
    soup = BeautifulSoup(html, "html.parser")
    d = {"url": url, "mall": mall}
    t = soup.find("title")
    d["title"] = text(t)
    og = soup.find("meta", property="og:title")
    d["og_title"] = og["content"].strip() if og and og.get("content") else ""
    md = soup.find("meta", attrs={"name": "description"})
    d["meta_description"] = md["content"].strip() if md and md.get("content") else ""
    main = main_area(soup)
    # encabezados
    d["headings"] = [text(h) for h in main.find_all(["h1", "h2", "h3"])][:10]
    # imágenes candidatas a logo (excluir logo de Multiplaza y assets genéricos)
    imgs = []
    for img in main.find_all("img"):
        src = img.get("src") or img.get("data-src") or ""
        if not src:
            continue
        src = urljoin(BASE, src)
        low = src.lower()
        if "assets/images/logo" in low or "multiplaza-og" in low or "home-slide" in low or low.endswith(".svg") and "logo/multiplaza" in low:
            continue
        imgs.append({"src": src, "alt": (img.get("alt") or "").strip(), "class": " ".join(img.get("class", []))})
    d["images"] = imgs[:15]
    # párrafos (descripción = el más largo)
    ps = [text(p) for p in main.find_all("p")]
    ps = [p for p in ps if len(p) > 40]
    d["paragraphs"] = ps[:8]
    d["description"] = max(ps, key=len) if ps else ""
    # elementos con icono (font awesome u otros): icono -> texto / href
    icon_items = []
    for i in main.find_all(["i", "svg", "span"], class_=True):
        cls = " ".join(i.get("class", []))
        if not re.search(r"\bfa[srlb]?-|icon", cls):
            continue
        parent = i.parent
        for _ in range(3):
            if parent is None:
                break
            tx = text(parent)
            if tx and tx.lower() not in ("", "home", "información", "blog", "contacto", "mia"):
                break
            parent = parent.parent
        a = parent if parent and parent.name == "a" else (parent.find("a", href=True) if parent else None)
        if parent is None:
            continue
        icon_items.append({"icon": cls, "text": text(parent)[:200], "href": urljoin(BASE, a["href"]) if a and a.get("href") else ""})
    # quitar duplicados
    seen = set(); d["icon_items"] = []
    for it in icon_items:
        k = (it["icon"], it["text"], it["href"])
        if k not in seen and len(d["icon_items"]) < 40:
            seen.add(k); d["icon_items"].append(it)
    # enlaces externos / contacto
    links = {"mailto": [], "tel": [], "facebook": [], "instagram": [], "tiktok": [], "whatsapp": [], "web": [], "interno": []}
    for a in main.find_all("a", href=True):
        h = a["href"].strip()
        hl = h.lower()
        if hl.startswith("mailto:"):
            links["mailto"].append(h[7:].split("?")[0])
        elif hl.startswith("tel:"):
            links["tel"].append(h[4:])
        elif "facebook.com" in hl or "fb.com" in hl:
            links["facebook"].append(h)
        elif "instagram.com" in hl:
            links["instagram"].append(h)
        elif "tiktok.com" in hl:
            links["tiktok"].append(h)
        elif "wa.me" in hl or "whatsapp" in hl:
            links["whatsapp"].append(h)
        elif hl.startswith("http") and "multiplaza.com" not in hl:
            links["web"].append(h)
        elif "multiplaza.com" in hl or h.startswith("/"):
            links["interno"].append(urljoin(BASE, h))
    for k in links:
        links[k] = sorted(set(links[k]))[:10]
    d["links"] = links
    # texto plano del área principal (recortado) para heurísticas posteriores
    body_text = text(main)
    d["phones_in_text"] = sorted(set(re.findall(r"(?:\+?506[\s-]?)?\b\d{4}[\s-]\d{4}\b", body_text)))[:10]
    d["hours_in_text"] = sorted(set(re.findall(r"[LMKJVSD][\-–a-zA-Z\.: ]{0,14}\d{1,2}(?::\d{2})?\s?(?:AM|PM|a\.m\.|p\.m\.)[^.|]{0,60}", body_text, flags=re.I)))[:6]
    d["main_text"] = body_text[:3000]
    return d

def save_logo(url, name):
    r = get(url)
    if not r or r.status_code != 200 or not r.content:
        return ""
    try:
        im = Image.open(io.BytesIO(r.content))
        im.load()
        if im.mode not in ("RGB", "RGBA"):
            im = im.convert("RGBA")
        w, h = im.size
        scale = min(1.0, 320 / max(w, 1), 320 / max(h, 1))
        if scale < 1:
            im = im.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.LANCZOS)
        path = f"{LOGOS}/{name}.png"
        im.save(path, "PNG", optimize=True)
        return path
    except Exception as e:
        print("LOGO ERR", url, e, file=sys.stderr)
        return ""

def main():
    os.makedirs(RAW, exist_ok=True); os.makedirs(LOGOS, exist_ok=True)
    result = {"generado": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()), "malls": {}}
    raw_saved = 0
    for mall in MALLS:
        listing_pages = [f"{BASE}/{mall}/tiendas", f"{BASE}/{mall}/restaurantes"]
        all_links = {}
        for lp in listing_pages:
            r = get(lp)
            if not r or r.status_code != 200:
                continue
            open(f"{RAW}/{mall}-{lp.rsplit('/',1)[1]}.html", "w", encoding="utf-8").write(r.text)
            all_links.update(store_links(BeautifulSoup(r.text, "html.parser"), mall))
            time.sleep(DELAY)
        # separar categorías (páginas sin sufijo -multiplaza-<mall>) y locales
        cats = {u: s for u, (tipo, s) in all_links.items() if not is_store_slug(s, mall)}
        stores = {u: (tipo, s) for u, (tipo, s) in all_links.items() if is_store_slug(s, mall)}
        print(mall, "categorías:", len(cats), "locales en listado:", len(stores), file=sys.stderr)
        cat_map = {}
        cat_names = {}
        for cu, cslug in sorted(cats.items()):
            r = get(cu)
            time.sleep(DELAY)
            if not r or r.status_code != 200:
                continue
            csoup = BeautifulSoup(r.text, "html.parser")
            h = csoup.find(["h1", "h2"])
            cat_names[cslug] = text(h) if h else cslug
            for su, (tipo, sslug) in store_links(csoup, mall).items():
                if is_store_slug(sslug, mall):
                    stores.setdefault(su, (tipo, sslug))
                    cat_map.setdefault(su, []).append(cslug)
        locales = []
        for i, (su, (tipo, sslug)) in enumerate(sorted(stores.items())):
            r = get(su)
            time.sleep(DELAY)
            if not r or r.status_code != 200:
                locales.append({"url": su, "mall": mall, "error": r.status_code if r else "sin respuesta"})
                continue
            if raw_saved < 4:
                open(f"{RAW}/muestra-{mall}-{sslug}.html", "w", encoding="utf-8").write(r.text); raw_saved += 1
            d = parse_store(r.text, su, mall)
            d["tipo_listado"] = tipo
            d["slug"] = sslug
            d["categorias_slug"] = cat_map.get(su, [])
            d["categorias"] = [cat_names.get(c, c) for c in d["categorias_slug"]]
            # logo: primera imagen candidata
            d["logo_url"] = d["images"][0]["src"] if d["images"] else ""
            d["logo_local"] = save_logo(d["logo_url"], f"{mall}-{sslug}") if d["logo_url"] else ""
            locales.append(d)
            if i % 20 == 0:
                print(mall, i, "/", len(stores), file=sys.stderr)
        result["malls"][mall] = {"categorias": cat_names, "locales": locales}
    json.dump(result, open(f"{OUT}/locales.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("listo:", {m: len(v["locales"]) for m, v in result["malls"].items()}, file=sys.stderr)

if __name__ == "__main__":
    main()
