"""Genera la página Elementor de Navidad Multiplaza 2026 (v2: recorrido guiado).

Uso:  python3 build_template.py         ->  navidad-multiplaza-elementor.json (plantilla importable)
      python3 build_template.py --page  ->  page-elementor-data.json (meta _elementor_data de la página)
Textos en copy.json; efectos, ilustraciones y recorrido en fx/ (se incrustan en un widget HTML).
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
PAGE = "--page" in sys.argv
COPY = json.loads((HERE / "copy.json").read_text(encoding="utf-8"))
C = "globals/colors?id="
T = "globals/typography?id="
MAIL = "mailto:contacto@lindsaymeneses.com?subject=Navidad%20Multiplaza%202026"

_seq = iter(range(1, 10**6))


def uid():
    return f"n{next(_seq):06x}"


def px(v, unit="px"):
    return {"unit": unit, "size": v}


def pad(t, r=None, b=None, l=None):
    r = t if r is None else r
    return {"unit": "px", "top": t, "right": r, "bottom": t if b is None else b, "left": r if l is None else l, "isLinked": False}


def container(children, settings=None, inner=True):
    s = {"content_width": "full", "flex_direction": "column", "padding": pad(0)}
    s.update(settings or {})
    return {"id": uid(), "elType": "container", "isInner": inner, "settings": s, "elements": children}


def widget(kind, settings):
    return {"id": uid(), "elType": "widget", "widgetType": kind, "isInner": False, "settings": settings, "elements": []}


def fx_widget():
    css = (HERE / "fx/fx.css").read_text()
    js = (HERE / "fx/art.js").read_text() + "\n" + (HERE / "fx/tour.js").read_text()
    html = f'<canvas class="nm-snow" aria-hidden="true"></canvas><style>{css}</style><script>{js}</script>'
    return widget("html", {"html": html, "_css_classes": "nm-fx"})


def art(kind, size="card", label=""):
    return widget("html", {"html": f'<div class="nm-art {size}" data-art="{kind}" data-label="{label}"></div>',
                           "_css_classes": "nm-art-w"})


def eyebrow(num, text, color="accent", align="left", rule=True):
    return widget("heading", {
        "title": f"{num} &nbsp;{text}" if num else text, "header_size": "p", "align": align,
        "_css_classes": ("nm-eyebrow" if rule else "nm-label") + (" nm-c" if align == "center" and rule else ""),
        "__globals__": {"title_color": C + color, "typography_typography": T + "accent"},
    })


def heading(text, size="h2", color="primary", align="left", fs=None, cls="", typo="primary"):
    s = {"title": text, "header_size": size, "align": align, "_css_classes": cls,
         "__globals__": {"title_color": C + color, "typography_typography": T + typo}}
    if fs:
        s["typography_font_size"] = px(fs)
        s["typography_font_size_tablet"] = px(round(fs * .78))
        s["typography_font_size_mobile"] = px(max(round(fs * .56), 20))
    return widget("heading", s)


def text(html, color="text", align="left", maxw=None):
    s = {"editor": html, "align": align, "__globals__": {"text_color": C + color, "typography_typography": T + "text"}}
    if maxw:
        s["_element_width"] = "initial"
        s["_element_custom_width"] = px(maxw)
        s["_element_custom_width_mobile"] = px(100, "%")
    return widget("text-editor", s)


def button(label, url, outline=False, fg="noche"):
    s = {"text": label, "link": {"url": url}, "size": "md",
         "border_radius": {"unit": "px", "top": 999, "right": 999, "bottom": 999, "left": 999, "isLinked": True},
         "text_padding": pad(17, 34), "__globals__": {"typography_typography": T + "accent"}}
    if outline:
        s.update({"background_color": "transparent", "border_border": "solid",
                  "border_width": {"unit": "px", "top": 1, "right": 1, "bottom": 1, "left": 1, "isLinked": True}})
        s["__globals__"].update({"button_text_color": C + fg, "border_color": C + "accent",
                                 "button_background_hover_color": C + "accent", "hover_color": C + "noche"})
    else:
        s["__globals__"].update({"background_color": C + "accent", "button_text_color": C + "noche",
                                 "button_background_hover_color": C + "oroclaro"})
    return widget("button", s)


def line(color="accent", width=72, center=False):
    return widget("divider", {"width": px(width), "weight": px(1), "align": "center" if center else "left",
                              "_css_classes": "nm-line" + (" nm-c" if center else ""), "__globals__": {"color": C + color}})


def row(children, gap=28, mobile="column", wrap=True, align=None):
    s = {"flex_direction": "row", "flex_wrap": "wrap" if wrap else "nowrap", "flex_direction_mobile": mobile,
         "gap": {"unit": "px", "size": gap, "column": str(gap), "row": str(gap)}}
    if align:
        s["flex_align_items"] = align
    return container(children, s)


def col(children, width, gap=22, justify="center"):
    return container(children, {"width": px(width, "%"), "width_mobile": px(100, "%"), "flex_justify_content": justify,
                                "gap": {"unit": "px", "size": gap, "column": str(gap), "row": str(gap)}})


def card(children, bg=None, basis=23, cls="nm-card", p=30, gap=14):
    s = {"width": px(basis, "%"), "width_mobile": px(100, "%"), "flex_grow": 1, "padding": pad(p, p - 4),
         "gap": {"unit": "px", "size": gap, "column": str(gap), "row": str(gap)},
         "border_radius": {"unit": "px", "top": 18, "right": 18, "bottom": 18, "left": 18, "isLinked": True},
         "css_classes": cls}
    if bg:
        s.update({"background_background": "classic", "__globals__": {"background_color": C + bg}})
    return container(children, s)


def slide(children, bg, extra=None, cls="", pad_y=110):
    s = {"content_width": "boxed", "boxed_width": px(1180), "flex_direction": "column", "flex_justify_content": "center",
         "min_height": px(100, "vh"), "padding": pad(pad_y, 48), "padding_mobile": pad(round(pad_y * .7), 20),
         "gap": {"unit": "px", "size": 26, "column": "26", "row": "26"},
         "background_background": "classic", "__globals__": {"background_color": C + bg},
         "css_classes": ("nm-slide " + cls).strip()}
    s.update(extra or {})
    return container(children, s, inner=False)


K = COPY

# 1 · Portada
p = K["portada"]
hero = slide([
    fx_widget(),
    eyebrow("", p["eyebrow"], "accent", "center"),
    heading(p["titulo_html"], "h1", "blanco", "center", fs=112),
    line("accent", 90, center=True),
    text(f"<p>{p['bajada']}</p>", "oroclaro", "center", maxw=620),
    row([button(p["cta_primario"], "#concepto"), button(p["cta_secundario"], "#calendario", outline=True, fg="blanco")],
        gap=14, mobile="row"),
], "noche", cls="nm-hero", extra={
    "flex_align_items": "center", "_element_id": "inicio",
    "background_background": "gradient", "background_color": "#0A241C", "background_color_b": "#15523F",
    "background_gradient_type": "radial", "background_gradient_position": "center center",
    "background_color_stop": px(30, "%"), "background_color_b_stop": px(130, "%"), "__globals__": {},
})

# 2 · Concepto
p = K["concepto"]
concepto = slide([
    row([
        col([eyebrow("01", p["eyebrow"], "secondary"), heading(p["titulo"], "h2", "primary", fs=58), line(),
             text(f"<p>{p['texto']}</p>", maxw=520),
             heading(p["cita"], "p", "vino", fs=26, cls="nm-quote", typo="secondary")], 46),
        col([art("arbol", "tall", "Árbol de luz dorado")], 50),
    ], gap=56, wrap=False, align="center"),
], "marfil", extra={"_element_id": "concepto"})

# 3 · Objetivos
p = K["objetivos"]
objetivos = slide([
    eyebrow("02", p["eyebrow"], "accent", "center"),
    heading(p["titulo"], "h2", "blanco", "center", fs=52),
    row([card([heading(n, "p", "accent", fs=40, typo="secondary"), heading(it["titulo"], "h3", "blanco", fs=26),
               text(f"<p>{it['texto']}</p>", "oroclaro")], basis=30, cls="nm-card nm-glass", p=38)
         for n, it in zip(("I", "II", "III"), p["items"])], gap=24),
], "primary")

# 4 · Experiencias
p = K["experiencias"]
experiencias = slide([
    eyebrow("03", p["eyebrow"], "secondary", "center"),
    heading(p["titulo_html"], "h2", "primary", "center", fs=52, cls="nm-shine"),
    row([card([art(k, "card", it["titulo"]), heading(it["titulo"], "h3", "primary", fs=24), text(f"<p>{it['texto']}</p>")],
              "blanco", basis=22, p=14, gap=12)
         for k, it in zip(("arbol", "villa", "musica", "regalo"), p["items"])], gap=20),
], "marfil")

# 5 · Decoración
p = K["decoracion"]
claves = "".join(f"<li>{c}</li>" for c in p["claves"])
decoracion = slide([
    row([
        col([eyebrow("04", p["eyebrow"], "accent"), heading(p["titulo"], "h2", "blanco", fs=52), line(),
             text(f"<p>{p['texto']}</p>", "oroclaro", maxw=460),
             text(f'<ul class="nm-keys">{claves}</ul>', "accent")], 40),
        col([row([art("esferas", "tile", "Esferas"), art("copo", "tile", "Copo de nieve")], gap=14, mobile="row", wrap=False),
             row([art("guirnalda", "tile", "Guirnalda"), art("estrella", "tile", "Estrella")], gap=14, mobile="row", wrap=False)],
            56, gap=14),
    ], gap=56, wrap=False, align="center"),
], "noche")

# 6 · Calendario
p = K["calendario"]
calendario = slide([
    eyebrow("05", p["eyebrow"], "secondary", "center"),
    heading(p["titulo"], "h2", "primary", "center", fs=52),
    row([card([eyebrow("", f["etiqueta"], "secondary", rule=False), heading(f["titulo"], "h3", "primary", fs=28),
               text(f"<p>{f['texto']}</p>")], basis=22, cls="nm-card nm-phase", p=30, gap=10)
         for f in p["fases"]], gap=28),
], "marfil", extra={"_element_id": "calendario"})

# 7 · Medición
p = K["medicion"]
medicion = slide([
    eyebrow("06", p["eyebrow"], "accent", "center"),
    heading(p["titulo"], "h2", "blanco", "center", fs=52),
    row([card([heading(f"0{i + 1}", "p", "accent", fs=34, typo="secondary"), heading(it["titulo"], "h3", "blanco", fs=24),
               text(f"<p>{it['texto']}</p>", "oroclaro")], basis=22, cls="nm-card nm-glass", p=30)
         for i, it in enumerate(p["items"])], gap=20),
], "primary")

# 8 · Cierre
p = K["cierre"]
cierre = slide([
    eyebrow("07", "Siguiente paso", "oroclaro", "center"),
    heading(p["titulo"], "h2", "blanco", "center", fs=76),
    line("oroclaro", 90, center=True),
    text(f"<p>{p['texto']}</p>", "oroclaro", "center", maxw=560),
    button(p["cta"], MAIL),
], "vino", extra={"flex_align_items": "center", "background_background": "gradient", "background_color": "#9B1530",
                  "background_color_b": "#4A0614", "background_gradient_type": "radial",
                  "background_gradient_position": "center center", "background_color_stop": px(0, "%"),
                  "background_color_b_stop": px(100, "%"), "__globals__": {}})

# Pie de página · Multiplaza · Grupo Roble
pie = container([
    row([
        col([heading("Multiplaza", "p", "blanco", fs=30), heading("Un centro de Grupo Roble", "p", "accent", typo="accent")], 32, gap=6),
        col([heading(K["pie"]["frase"], "p", "oroclaro", "center", fs=22, typo="secondary")], 32, gap=6),
        col([heading("Contacto", "p", "accent", "right", typo="accent"),
             text('<p><a href="' + MAIL + '" style="color:inherit">contacto@lindsaymeneses.com</a></p>', "oroclaro", "right")], 32, gap=6),
    ], gap=24, align="center"),
    line("accent", 100, center=False),
    text(f"<p>{K['nombre_campana']} · Propuesta creativa Navidad 2026 para Multiplaza · Grupo Roble</p>", "salvia", "center"),
], {"content_width": "boxed", "boxed_width": px(1180), "padding": pad(64, 48, 40), "padding_mobile": pad(48, 20, 90),
    "gap": {"unit": "px", "size": 28, "column": "28", "row": "28"}, "background_background": "classic",
    "__globals__": {"background_color": C + "noche"}, "css_classes": "nm-footer"}, inner=False)

CONTENT = [hero, concepto, objetivos, experiencias, decoracion, calendario, medicion, cierre, pie]
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
