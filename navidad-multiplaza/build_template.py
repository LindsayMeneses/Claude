"""Genera la página Elementor de Navidad Multiplaza 2026 (v3: línea editorial con fotografía).

Uso:  python3 build_template.py         ->  navidad-multiplaza-elementor.json (plantilla importable)
      python3 build_template.py --page  ->  page-elementor-data.json (meta _elementor_data de la página)
Textos en copy.json (basados en el deck); estilos y recorrido en fx/ (se incrustan en un widget HTML);
fotos CC0 ya subidas a Medios (ver FOTOS).
"""
import html as H
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
PAGE = "--page" in sys.argv
COPY = json.loads((HERE / "copy.json").read_text(encoding="utf-8"))
C = "globals/colors?id="
T = "globals/typography?id="
MAIL = "mailto:contacto@lindsaymeneses.com?subject=Navidad%20Multiplaza%202026"
UP = "https://lindsaymeneses.com/wp-content/uploads/2026/09/"

# Fotos CC0 (Unsplash vía Wikimedia Commons) en la biblioteca de medios: nombre -> [(ancho, archivo)]
FOTOS = {
    "portada": [(768, "nm-rojo-dorado-768x432.jpg"), (1536, "nm-rojo-dorado-1536x864.jpg"), (2048, "nm-rojo-dorado-2048x1152.jpg")],
    "cascabeles": [(768, "nm-c03-768x539.jpg"), (1536, "nm-c03-1536x1077.jpg"), (2048, "nm-c03-2048x1436.jpg")],
    "luces": [(768, "nm-c13-768x513.jpg"), (1536, "nm-c13-1536x1026.jpg"), (1920, "nm-c13.jpg")],
    "esferas": [(768, "nm-esferas-navidad-768x512.jpg"), (1536, "nm-esferas-navidad-1536x1024.jpg"), (2048, "nm-esferas-navidad-2048x1365.jpg")],
    "arbol": [(768, "nm-c12-768x512.jpg"), (1536, "nm-c12-1536x1024.jpg"), (1920, "nm-c12.jpg")],
    "pino": [(768, "nm-c05-768x512.jpg"), (1536, "nm-c05-1536x1024.jpg"), (2048, "nm-c05-2048x1365.jpg")],
    "copo": [(768, "nm-c06-768x509.jpg"), (1536, "nm-c06-1536x1017.jpg"), (2048, "nm-c06-2048x1356.jpg")],
    "chispa": [(768, "nm-c01-768x512.jpg"), (1536, "nm-c01-1536x1024.jpg"), (2048, "nm-c01-2048x1365.jpg")],
    "adornos": [(768, "nm-adornos-arbol-768x512.jpg"), (1536, "nm-adornos-arbol-1536x1024.jpg")],
    "estrella": [(769, "nm-estrella-769x1024.jpg"), (1153, "nm-estrella-1153x1536.jpg")],
    "campana": [(768, "nm-esfera-768x512.jpg"), (1536, "nm-esfera-1536x1025.jpg")],
    "arbolblanco": [(768, "nm-arbol-festivo-768x488.jpg"), (1536, "nm-arbol-festivo-1536x976.jpg")],
}

# Clips de 6 s generados con IA (ver VIDEOS-IA.md). Clave de FOTOS -> URL del .mp4 en Medios.
# Mientras una clave no tenga video, se muestra la foto; cuando lo tenga, el clip entra en fundido sobre ella.
VIDEOS = {}

_seq = iter(range(1, 10**6))


def uid():
    return f"n{next(_seq):06x}"


def px(v, unit="px"):
    return {"unit": unit, "size": v}


def pad(t, r=None, b=None, l=None):
    r = t if r is None else r
    return {"unit": "px", "top": t, "right": r, "bottom": t if b is None else b, "left": r if l is None else l, "isLinked": False}


def gap(n):
    return {"unit": "px", "size": n, "column": str(n), "row": str(n)}


def container(children, settings=None, inner=True):
    s = {"content_width": "full", "flex_direction": "column", "padding": pad(0)}
    s.update(settings or {})
    return {"id": uid(), "elType": "container", "isInner": inner, "settings": s, "elements": children}


def widget(kind, settings):
    return {"id": uid(), "elType": "widget", "widgetType": kind, "isInner": False, "settings": settings, "elements": []}


def html(markup, cls=""):
    s = {"html": markup}
    if cls:
        s["_css_classes"] = cls
    return widget("html", s)


def fx_widget():
    css = re.sub(r"/\*.*?\*/", "", (HERE / "fx/fx.css").read_text(), flags=re.S)
    css = re.sub(r"\s*\n\s*", "", css)
    js = (HERE / "fx/tour.js").read_text()
    js = "\n".join(l.strip() for l in js.splitlines() if l.strip() and not l.strip().startswith(("//", "/*")))
    return html(f'<div class="nm-bokeh" aria-hidden="true"></div><canvas class="nm-snow" aria-hidden="true"></canvas>'
                f'<style>{css}</style><script>{js}</script>', "nm-fx")


def img(key, alt, sizes="100vw", eager=False):
    f = FOTOS[key]
    srcset = ", ".join(f"{UP}{n} {w}w" for w, n in f)
    return (f'<img src="{UP}{f[1][1] if len(f) > 1 else f[0][1]}" srcset="{srcset}" sizes="{sizes}" alt="{H.escape(alt)}" '
            + ('fetchpriority="high">' if eager else 'loading="lazy" decoding="async">'))


def vid(key):
    url = VIDEOS.get(key)
    return f'<video class="nm-vid" muted loop playsinline preload="none" data-src="{url}" aria-hidden="true"></video>' if url else ""


def photo_bg(key, alt, ov="left", eager=False):
    """Foto a sangre como fondo de la diapositiva: entra desenfocada, enfoca y deriva lentamente."""
    return html(f'<div class="nm-ph {ov}"><div class="nm-kb">{img(key, alt, eager=eager)}{vid(key)}</div></div><div class="nm-ov {ov}"></div>', "nm-bgw")


def photo(key, alt, size="tall", sizes="(max-width:767px) 100vw, 50vw"):
    """Foto enmarcada con filete dorado desplazado."""
    return html(f'<figure class="nm-frame {size}"><div class="nm-ph"><div class="nm-kb">{img(key, alt, sizes)}{vid(key)}</div></div></figure>',
                "nm-frame-w")


def eyebrow(num, text, color="accent", align="left"):
    return widget("heading", {
        "title": f"{num} &nbsp;{text}" if num else text, "header_size": "p", "align": align,
        "_css_classes": "nm-eyebrow" + (" nm-c" if align == "center" else ""),
        "__globals__": {"title_color": C + color, "typography_typography": T + "accent"},
    })


def heading(text, size="h2", color="primary", align="left", fs=None, cls="", typo="primary"):
    s = {"title": text, "header_size": size, "align": align, "_css_classes": ("nm-t " + cls).strip(),
         "__globals__": {"title_color": C + color, "typography_typography": T + typo}}
    if fs:
        s["typography_font_size"] = px(fs)
        s["typography_font_size_tablet"] = px(round(fs * .8))
        s["typography_font_size_mobile"] = px(max(round(fs * .58), 20))
    return widget("heading", s)


def text(markup, color="text", align="left", maxw=None, cls=""):
    s = {"editor": markup, "align": align, "__globals__": {"text_color": C + color, "typography_typography": T + "text"}}
    if cls:
        s["_css_classes"] = cls
    if maxw:
        s["_element_width"] = "initial"
        s["_element_custom_width"] = px(maxw)
        s["_element_custom_width_mobile"] = px(100, "%")
    return widget("text-editor", s)


def buttons(items, align="left"):
    a = "".join(f'<a class="nm-btn{" ghost" if ghost else ""}" href="{H.escape(url)}">{label}</a>' for label, url, ghost in items)
    return html(f'<div class="nm-btns {align}">{a}</div>')


def line(color="accent", width=72, center=False):
    return widget("divider", {"width": px(width), "weight": px(1), "align": "center" if center else "left",
                              "_css_classes": "nm-line" + (" nm-c" if center else ""), "__globals__": {"color": C + color}})


def ul(cls, items):
    return f'<ul class="{cls}">' + "".join(items) + "</ul>"


def stats(pairs, cls=""):
    return ul(("nm-stats " + cls).strip(), (f"<li><b>{a}</b>{b}</li>" for a, b in pairs))


def row(children, g=48, mobile="column", wrap=False, align="center", tablet=None):
    s = {"flex_direction": "row", "flex_wrap": "wrap" if wrap else "nowrap", "flex_direction_mobile": mobile,
         "gap": gap(g), "flex_align_items": align}
    if tablet:
        s["flex_direction_tablet"] = tablet
    return container(children, s)


def col(children, width, g=22, justify="center", tablet=None):
    s = {"width": px(width, "%"), "width_mobile": px(100, "%"), "flex_justify_content": justify, "gap": gap(g)}
    if tablet:
        s["width_tablet"] = px(tablet, "%")
    return container(children, s)


def card(children, basis=23, cls="nm-card", tablet=46, g=14):
    return container(children, {"width": px(basis, "%"), "width_tablet": px(tablet, "%"), "width_mobile": px(100, "%"),
                                "flex_grow": 1, "gap": gap(g), "css_classes": cls})


def slide(children, bg, extra=None, cls="", eid=None):
    s = {"content_width": "boxed", "boxed_width": px(1200), "flex_direction": "column", "flex_justify_content": "center",
         "min_height": px(100, "vh"), "padding": pad(120, 56), "padding_tablet": pad(96, 40), "padding_mobile": pad(84, 22),
         "gap": gap(26), "background_background": "classic", "__globals__": {"background_color": C + bg},
         "css_classes": ("nm-slide " + cls).strip()}
    if eid:
        s["_element_id"] = eid
    s.update(extra or {})
    return container(children, s, inner=False)


K = COPY
alt = lambda s: s  # noqa: E731

# 1 · Portada — foto a sangre, texto a la izquierda
p = K["portada"]
hero = slide([
    fx_widget(),
    photo_bg("portada", "Esferas rojas y doradas en un pino de Navidad", "left", eager=True),
    col([
        eyebrow("", p["eyebrow"], "accent"),
        heading(p["titulo_html"], "h1", "blanco", fs=88, cls="nm-hero-t"),
        line("accent", 90),
        text(f"<p>{p['bajada']}</p>", "oroclaro", maxw=560),
        text(stats(p["datos"], "sm on-dark three"), "blanco"),
        buttons([(p["cta_primario"], "#recorrido", False), (p["cta_secundario"], "#curridabat", True)]),
    ], 62, g=24, tablet=80),
], "noche", cls="nm-hero nm-has-bg nm-dark", eid="inicio")

# 2 · El recorrido — índice de zonas
p = K["recorrido"]
zonas_e = ul("nm-zones", (f"<li>{z}</li>" for z in p["escazu"]))
zonas_c = ul("nm-zones", (f"<li>{z}</li>" for z in p["curridabat"]))
recorrido = slide([
    row([
        col([eyebrow("01", p["eyebrow"], "secondary"), heading(p["titulo"], "h2", "primary", fs=56), line(),
             text(f"<p>{p['texto']}</p>", maxw=440)], 36, tablet=100),
        col([row([
            col([heading("Escazú", "h3", "primary", fs=26, typo="secondary"), text(zonas_e, "text")], 54, g=10, justify="flex-start"),
            col([heading("Curridabat", "h3", "primary", fs=26, typo="secondary"), text(zonas_c, "text"),
                 text('<p class="nm-note">Plaza Cinemark, Plaza Kolbi y Plaza Old Navy retoman diseños de Escazú.</p>', "text")],
                42, g=10, justify="flex-start"),
        ], g=40, align="flex-start")], 60, tablet=100),
    ], g=64, align="center", tablet="column"),
], "marfil", eid="recorrido")

# 3 · Fachadas e identidad — foto enmarcada + paleta
p = K["fachadas"]
pal = ul("nm-pal", (f'<li><i style="--c:{c}"></i><span><b>{n}</b>{d}</span></li>' for c, n, d in p["paleta"]))
fachadas = slide([
    row([
        col([photo("cascabeles", "Cascabeles rojos y blancos con una estrella navideña", "tall")], 46, tablet=100),
        col([eyebrow("02", p["eyebrow"], "secondary"), heading(p["titulo"], "h2", "primary", fs=50), line(),
             text(f"<p>{p['texto']}</p>", maxw=500), text(pal, "text"), text(f'<p class="nm-note">{p["nota"]}</p>', "text")],
            48, tablet=100),
    ], g=72, tablet="column"),
], "blanco")

# 4 · Plaza Starbucks — túnel de luz
p = K["starbucks"]
claves = ul("nm-keys", (f"<li>{c}</li>" for c in p["claves"]))
starbucks = slide([
    photo_bg("luces", "Árbol envuelto en luces cálidas", "left"),
    col([eyebrow("03", p["eyebrow"], "accent"), heading(p["titulo_html"], "h2", "blanco", fs=60, cls="nm-shine"), line(),
         text(f"<p>{p['texto']}</p>", "oroclaro", maxw=500), text(claves, "blanco")], 56, tablet=80),
], "noche", cls="nm-has-bg nm-dark")

# 5 · Zona familiar — Casa de Santa y Plaza Tukis
p = K["familia"]
familia = slide([
    row([
        col([eyebrow("04", p["eyebrow"], "secondary"), heading(p["titulo"], "h2", "primary", fs=50), line(),
             text(f'<p><strong>Casa de Santa.</strong> {p["santa"]}</p><p><strong>Plaza Tukis.</strong> {p["tukis"]}</p>', maxw=520,
                  cls="nm-prose"),
             text(stats(p["datos"], "sm"), "text")], 50, tablet=100),
        col([photo("esferas", "Esferas navideñas pintadas a mano", "tall")], 44, tablet=100),
    ], g=72, tablet="column"),
], "marfil")

# 6 · Plaza Brunos — escena protagonista
p = K["brunos"]
piezas = ul("nm-specs", (f"<li><b>{a}</b>{b}</li>" for a, b in p["piezas"]))
brunos = slide([
    row([
        col([eyebrow("05", p["eyebrow"], "accent"), heading(p["titulo_html"], "h2", "blanco", fs=56, cls="nm-shine"), line(),
             text(f"<p>{p['texto']}</p>", "oroclaro", maxw=560), text(stats(p["datos"], "sm on-dark"), "blanco"),
             text(piezas, "oroclaro")], 58, tablet=100),
        col([photo("arbol", "Árbol de Navidad monumental entre palmeras", "tall", "(max-width:767px) 100vw, 40vw")], 36, tablet=100),
    ], g=64, align="center", tablet="column"),
], "noche", cls="nm-dark")

# 7 · Pasillos y plazas de Escazú
p = K["escazu"]
FOTO_TARJETA = {"guirnalda": ("adornos", "Adornos y cascabeles en un pino"), "estrella": ("estrella", "Estrella dorada"),
                "esferas": ("campana", "Campana navideña plateada"), "copo": ("arbolblanco", "Árbol de Navidad decorado")}
escazu = slide([
    eyebrow("06", p["eyebrow"], "secondary", "center"),
    heading(p["titulo"], "h2", "primary", "center", fs=50),
    row([card([photo(*FOTO_TARJETA[k], "card", "(max-width:767px) 100vw, 25vw"), heading(t, "h3", "primary", fs=24),
               text(f"<p>{d}</p>")], basis=23) for t, d, k in p["items"]], g=24, wrap=True, align="stretch"),
], "blanco")

# 8 · Curridabat — espejos y cielo de cables
p = K["curridabat"]
espejos = ul("nm-mirror", (f"<li><b>{a}</b>{b}</li>" for a, b in p["espejos"]))
curridabat = slide([
    photo_bg("pino", "Pino con luces blancas y nieve", "full"),
    col([eyebrow("07", p["eyebrow"], "accent"), heading(p["titulo_html"], "h2", "blanco", fs=60, cls="nm-shine"), line(),
         text(f"<p>{p['texto']}</p>", "oroclaro", maxw=560), text(espejos, "blanco"),
         heading("Plaza Santo Katrin", "h3", "blanco", fs=24, typo="secondary"),
         text(stats(p["katrin"], "sm on-dark"), "blanco")], 64, tablet=90),
], "noche", cls="nm-has-bg nm-dark", eid="curridabat")

# 9 · Plaza Reebok — árboles de espejo
p = K["reebok"]
claves = ul("nm-keys", (f"<li>{c}</li>" for c in p["claves"]))
reebok = slide([
    row([
        col([photo("copo", "Copo de nieve decorativo colgando", "tall")], 46, tablet=100),
        col([eyebrow("08", p["eyebrow"], "secondary"), heading(p["titulo"], "h2", "primary", fs=56), line(),
             text(f"<p>{p['texto']}</p>", maxw=480), text(claves, "primary"), text(f'<p class="nm-note">{p["nota"]}</p>', "text")],
            46, tablet=100),
    ], g=72, tablet="column"),
], "marfil")

# 10 · En cifras — fondo de luces desenfocadas
p = K["cifras"]
cifras = slide([
    photo_bg("luces", "", "blur"),
    eyebrow("09", p["eyebrow"], "accent", "center"),
    heading(p["titulo"], "h2", "blanco", "center", fs=56),
    line("accent", 90, center=True),
    text(stats(p["items"], "big c on-dark"), "oroclaro"),
], "noche", cls="nm-has-bg nm-dark")

# 11 · Cierre
p = K["cierre"]
cierre = slide([
    photo_bg("chispa", "Luz de bengala encendida", "center"),
    eyebrow("10", p["eyebrow"], "oroclaro", "center"),
    heading(p["titulo"], "h2", "blanco", "center", fs=72),
    line("oroclaro", 90, center=True),
    text(f"<p>{p['texto']}</p>", "oroclaro", "center", maxw=560),
    buttons([(p["cta"], MAIL, False)], "center"),
], "noche", cls="nm-has-bg nm-dark nm-center", extra={"flex_align_items": "center"})

# Pie de página
pie = container([
    row([
        col([heading("Multiplaza", "p", "blanco", fs=30), heading("Grupo Roble", "p", "accent", typo="accent")], 32, g=6),
        col([heading(K["pie"]["frase"], "p", "oroclaro", "center", fs=20, typo="secondary")], 32, g=6),
        col([heading("Contacto", "p", "accent", "right", typo="accent", cls="nm-r"),
             text(f'<p><a href="{MAIL}" style="color:inherit">contacto@lindsaymeneses.com</a></p>', "oroclaro", "right", cls="nm-r")],
            32, g=6),
    ], g=24, wrap=True),
    line("accent", 100),
    text(f"<p>{K['pie']['credito']} · Fotografías de referencia CC0 (Unsplash).</p>", "salvia", "center", cls="nm-note"),
], {"content_width": "boxed", "boxed_width": px(1200), "padding": pad(64, 56, 40), "padding_mobile": pad(48, 22, 110),
    "gap": gap(28), "background_background": "classic", "__globals__": {"background_color": C + "noche"},
    "css_classes": "nm-footer"}, inner=False)

CONTENT = [hero, recorrido, fachadas, starbucks, familia, brunos, escazu, curridabat, reebok, cifras, cierre, pie]
template = {"version": "0.4", "title": "Navidad Multiplaza 2026", "type": "page",
            "page_settings": {"hide_title": "yes", "template": "elementor_canvas"}, "content": CONTENT}

if __name__ == "__main__":
    if PAGE:
        data = json.dumps(CONTENT, ensure_ascii=False, separators=(",", ":"))
        (HERE / "page-elementor-data.json").write_text(data, encoding="utf-8")
        print("ok page-elementor-data.json", len(data), "bytes")
    else:
        (HERE / "navidad-multiplaza-elementor.json").write_text(json.dumps(template, ensure_ascii=False, indent=1), encoding="utf-8")
        print("ok", len(CONTENT), "bloques")
