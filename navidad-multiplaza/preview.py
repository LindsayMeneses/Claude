"""Vista previa local de la página (imita el marcado y el CSS de Elementor para revisar el diseño).

Uso:  python3 build_template.py --page && python3 preview.py && NODE_PATH=$(npm root -g) node preview-shots.js
Escribe preview/index.html. Usa las mismas clases que Elementor (.elementor-widget, .elementor-heading-title…),
así fx/fx.css y fx/tour.js funcionan igual que en el sitio.
"""
import html
import json
import re
from pathlib import Path

HERE = Path(__file__).parent
COLORS = {"primary": "#0F3B2E", "secondary": "#B3122E", "text": "#1E2A25", "accent": "#C9A45C",
          "marfil": "#FBF6EC", "noche": "#0A241C", "vino": "#7A0C21", "oroclaro": "#EBD9AE",
          "blanco": "#FFFFFF", "salvia": "#E4ECE6"}
TYPO = {
    "primary": "font-family:'Fraunces',serif;font-weight:600;line-height:1.1;letter-spacing:-0.01em;",
    "secondary": "font-family:'Fraunces',serif;font-weight:500;font-style:italic;font-size:24px;line-height:1.25;",
    "text": "font-family:'Manrope',sans-serif;font-weight:400;font-size:17px;line-height:1.65;",
    "accent": "font-family:'Manrope',sans-serif;font-weight:600;font-size:13px;text-transform:uppercase;letter-spacing:0.2em;",
}
css = []


def g(s, key):
    ref = s.get("__globals__", {}).get(key, "") or ""
    m = re.search(r"id=(\w+)", ref)
    if not m:
        return None
    return COLORS.get(m.group(1)) if "colors" in ref else TYPO.get(m.group(1))


def box(v):
    return f"{v['top']}px {v['right']}px {v['bottom']}px {v['left']}px"


def responsive(sel, s, prop, key):
    out = []
    if key in s:
        out.append(f"{sel}{{{prop}:{s[key]['size']}{s[key]['unit']}}}")
    for dev, mq in (("tablet", 1024), ("mobile", 767)):
        if f"{key}_{dev}" in s:
            v = s[f"{key}_{dev}"]
            out.append(f"@media(max-width:{mq}px){{{sel}{{{prop}:{v['size']}{v['unit']}}}}}")
    return out


def gradient(s):
    return (f"radial-gradient(at {s.get('background_gradient_position', 'center center')}, "
            f"{s['background_color']} {s.get('background_color_stop', {'size': 0})['size']}%, "
            f"{s['background_color_b']} {s.get('background_color_b_stop', {'size': 100})['size']}%)")


def render(el):
    s, eid = el["settings"], el["id"]
    sel = f".elementor-element-{eid}"
    if el["elType"] == "container":
        r = ["display:flex", f"flex-direction:{s.get('flex_direction', 'column')}", f"padding:{box(s['padding']) if 'padding' in s else '10px'}",
             f"gap:{s['gap']['size']}px" if "gap" in s else "gap:20px", "box-sizing:border-box", "position:relative"]
        for k, prop in (("flex_wrap", "flex-wrap"), ("flex_justify_content", "justify-content"), ("flex_align_items", "align-items")):
            if s.get(k):
                r.append(f"{prop}:{s[k]}")
        if "width" in s:
            r.append(f"width:{s['width']['size']}%;flex-shrink:1;min-width:0")
        if s.get("flex_grow"):
            r.append(f"flex-grow:{s['flex_grow']}")
        if "min_height" in s:
            r.append(f"min-height:{s['min_height']['size']}{s['min_height']['unit']}")
        if "border_radius" in s:
            r.append(f"border-radius:{s['border_radius']['top']}px")
        if s.get("background_background") == "gradient":
            r.append(f"background:{gradient(s)}")
        elif g(s, "background_color"):
            r.append(f"background:{g(s, 'background_color')}")
        css.append(f"{sel}{{{';'.join(r)}}}")
        mob = []
        if s.get("flex_direction_mobile"):
            mob.append(f"flex-direction:{s['flex_direction_mobile']}")
        if "width_mobile" in s:
            mob.append(f"width:{s['width_mobile']['size']}%")
        if "padding_mobile" in s:
            mob.append(f"padding:{box(s['padding_mobile'])}")
        if mob:
            css.append(f"@media(max-width:767px){{{sel}{{{';'.join(mob)}}}}}")
        inner = "".join(render(c) for c in el["elements"])
        if s.get("content_width") == "boxed":
            css.append(f"{sel}>.e-con-inner{{width:100%;max-width:{s['boxed_width']['size']}px;margin:0 auto;display:flex;flex-direction:inherit;"
                       f"flex-wrap:inherit;gap:inherit;justify-content:inherit;align-items:inherit}}")
            inner = f'<div class="e-con-inner">{inner}</div>'
        idattr = f' id="{s["_element_id"]}"' if s.get("_element_id") else ""
        return f'<div class="elementor-element elementor-element-{eid} e-con {s.get("css_classes", "")}"{idattr}>{inner}</div>'

    w = el["widgetType"]
    cls = f'elementor-element elementor-element-{eid} elementor-widget elementor-widget-{w} {s.get("_css_classes", "")}'
    align = s.get("align", "left")
    if s.get("_element_width") == "initial":
        css.append(f"{sel}{{width:{s['_element_custom_width']['size']}px;max-width:100%}}")
        if align == "center":
            css.append(f"{sel}{{align-self:center}}")
    if w == "heading":
        css.append(f"{sel} .elementor-heading-title{{{g(s, 'typography_typography')};color:{g(s, 'title_color')};text-align:{align};margin:0}}")
        css.extend(responsive(f"{sel} .elementor-heading-title", s, "font-size", "typography_font_size"))
        t = s["header_size"]
        return f'<div class="{cls}"><{t} class="elementor-heading-title">{s["title"]}</{t}></div>'
    if w == "text-editor":
        css.append(f"{sel}{{{g(s, 'typography_typography')};color:{g(s, 'text_color')};text-align:{align}}}{sel} p{{margin:0}}")
        return f'<div class="{cls}">{s["editor"]}</div>'
    if w == "button":
        outline = s.get("border_border") == "solid"
        bg = "transparent" if outline else g(s, "background_color")
        border = f"border:1px solid {g(s, 'border_color')}" if outline else "border:0"
        css.append(f"{sel} .elementor-button{{{g(s, 'typography_typography')};display:inline-block;background:{bg};color:{g(s, 'button_text_color')};"
                   f"{border};border-radius:999px;padding:{box(s['text_padding'])};text-decoration:none;transition:all .3s}}"
                   f"{sel} .elementor-button:hover{{background:{g(s, 'button_background_hover_color')};color:{g(s, 'hover_color') or g(s, 'button_text_color')}}}")
        return f'<div class="{cls}"><a class="elementor-button" href="{html.escape(s["link"]["url"])}">{s["text"]}</a></div>'
    if w == "divider":
        m = "0 auto" if s.get("align") == "center" else "0"
        css.append(f"{sel} .elementor-divider-separator{{display:block;width:{s['width']['size']}px;border-top:{s['weight']['size']}px solid {g(s, 'color')};margin:{m}}}")
        return f'<div class="{cls}"><div class="elementor-divider"><span class="elementor-divider-separator"></span></div></div>'
    if w == "html":
        return f'<div class="{cls}">{s["html"]}</div>'
    return f"<!-- {w} -->"


if __name__ == "__main__":
    data = json.loads((HERE / "page-elementor-data.json").read_text())
    body = "".join(render(el) for el in data)
    page = f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Vista previa · Navidad Multiplaza 2026</title>
<link href="fonts/fonts.css" rel="stylesheet">
<style>body{{margin:0}}*{{box-sizing:border-box}}em{{font-style:italic}}{''.join(css)}</style></head>
<body><div class="elementor">{body}</div></body></html>"""
    (HERE / "preview").mkdir(exist_ok=True)
    (HERE / "preview/index.html").write_text(page)
    print("ok preview/index.html", len(page), "bytes")
