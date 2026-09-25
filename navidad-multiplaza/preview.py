"""Vista previa local de la página (aproximación fiel del render de Elementor).

Uso:  python3 build_template.py --page && python3 preview.py [iconos.html]
      -> escribe preview/index.html; capturas con `node preview-shots.js`.
Sirve para revisar diseño sin acceso al sitio. Los iconos SVG se toman del HTML que
devuelve WordPress (content.rendered), si se pasa como argumento.
"""
import html
import json
import re
import sys
from pathlib import Path

COLORS = {"primary": "#0F3B2E", "secondary": "#B3122E", "text": "#1E2A25", "accent": "#C9A45C",
          "marfil": "#FBF6EC", "noche": "#0A241C", "vino": "#7A0C21", "oroclaro": "#EBD9AE",
          "blanco": "#FFFFFF", "salvia": "#E4ECE6"}
TYPO = {
    "primary": "font-family:'Fraunces',serif;font-weight:600;line-height:1.1;letter-spacing:-0.01em;",
    "secondary": "font-family:'Fraunces',serif;font-weight:500;font-style:italic;font-size:24px;line-height:1.25;",
    "text": "font-family:'Manrope',sans-serif;font-weight:400;font-size:17px;line-height:1.65;",
    "accent": "font-family:'Manrope',sans-serif;font-weight:600;font-size:13px;text-transform:uppercase;letter-spacing:0.2em;",
}
ICONS = {}
css = []


def g(settings, key):
    ref = settings.get("__globals__", {}).get(key, "")
    m = re.search(r"id=(\w+)", ref or "")
    if not m:
        return None
    return COLORS.get(m.group(1)) if "colors" in ref else TYPO.get(m.group(1))


def box(v):
    return f"{v['top']}px {v['right']}px {v['bottom']}px {v['left']}px"


def size_rules(sel, s, prop, key):
    out = []
    if key in s:
        out.append(f"{sel}{{{prop}:{s[key]['size']}{s[key]['unit']}}}")
    for dev, mq in (("tablet", 1024), ("mobile", 767)):
        k = f"{key}_{dev}"
        if k in s:
            out.append(f"@media(max-width:{mq}px){{{sel}{{{prop}:{s[k]['size']}{s[k]['unit']}}}}}")
    return out


def render(el, parent_row=False):
    s, eid = el["settings"], el["id"]
    sel = f".el-{eid}"
    if el["elType"] == "container":
        rules = ["display:flex", f"flex-direction:{s.get('flex_direction', 'column')}",
                 f"padding:{box(s['padding']) if 'padding' in s else '10px'}",
                 f"gap:{s['gap']['size']}px" if "gap" in s else "gap:20px"]
        if s.get("flex_wrap"):
            rules.append(f"flex-wrap:{s['flex_wrap']}")
        if s.get("flex_justify_content"):
            rules.append(f"justify-content:{s['flex_justify_content']}")
        if s.get("flex_align_items"):
            rules.append(f"align-items:{s['flex_align_items']}")
        if "width" in s:
            rules.append(f"width:{s['width']['size']}%")
            rules.append("flex-shrink:1")
        if s.get("flex_grow"):
            rules.append(f"flex-grow:{s['flex_grow']}")
        if "min_height" in s:
            rules.append(f"min-height:{s['min_height']['size']}{s['min_height']['unit']}")
        if "border_radius" in s:
            rules.append(f"border-radius:{s['border_radius']['top']}px;overflow:hidden")
        if s.get("box_shadow_box_shadow_type") == "yes":
            b = s["box_shadow_box_shadow"]
            rules.append(f"box-shadow:{b['horizontal']}px {b['vertical']}px {b['blur']}px {b['spread']}px {b['color']}")
        if s.get("background_background") == "gradient":
            rules.append(f"background:radial-gradient(at {s.get('background_gradient_position', 'center center')}, "
                         f"{s['background_color']} {s.get('background_color_stop', {'size': 0})['size']}%, "
                         f"{s['background_color_b']} {s.get('background_color_b_stop', {'size': 100})['size']}%)")
        elif g(s, "background_color"):
            rules.append(f"background:{g(s, 'background_color')}")
        rules.append("box-sizing:border-box")
        css.append(f"{sel}{{{';'.join(rules)}}}")
        mob = []
        if s.get("flex_direction_mobile"):
            mob.append(f"flex-direction:{s['flex_direction_mobile']}")
        if "width_mobile" in s:
            mob.append(f"width:{s['width_mobile']['size']}%")
        if "padding_mobile" in s:
            mob.append(f"padding:{box(s['padding_mobile'])}")
        if "min_height_mobile" in s:
            mob.append(f"min-height:{s['min_height_mobile']['size']}px")
        if mob:
            css.append(f"@media(max-width:767px){{{sel}{{{';'.join(mob)}}}}}")
        inner = "".join(render(c) for c in el["elements"])
        if s.get("content_width") == "boxed":
            css.append(f"{sel}>.inner{{width:100%;max-width:{s['boxed_width']['size']}px;margin:0 auto;display:flex;"
                       f"flex-direction:inherit;flex-wrap:inherit;gap:inherit;justify-content:inherit;align-items:inherit}}")
            inner = f'<div class="inner">{inner}</div>'
        idattr = f' id="{s["_element_id"]}"' if s.get("_element_id") else ""
        return f'<div class="el-{eid}"{idattr}>{inner}</div>'

    w = el["widgetType"]
    align = s.get("align", "left")
    if w == "heading":
        rules = [g(s, "typography_typography") or "", f"color:{g(s, 'title_color')}", f"text-align:{align}", "margin:0"]
        if s.get("typography_text_transform"):
            rules.append(f"letter-spacing:{s['typography_letter_spacing']['size']}em")
        css.append(f"{sel}{{{';'.join(rules)}}}")
        css.extend(size_rules(sel, s, "font-size", "typography_font_size"))
        tag = s["header_size"]
        return f'<{tag} class="el-{eid}">{s["title"]}</{tag}>'
    if w == "text-editor":
        css.append(f"{sel}{{{g(s, 'typography_typography')};color:{g(s, 'text_color')};text-align:{align}}}"
                   f"{sel} p{{margin:0}}")
        return f'<div class="el-{eid}">{s["editor"]}</div>'
    if w == "button":
        outline = s.get("border_border") == "solid"
        bg = "transparent" if outline else g(s, "background_color")
        fg = g(s, "button_text_color")
        p = s["text_padding"]
        border = f"border:1px solid {g(s, 'border_color')}" if outline else "border:0"
        css.append(f"{sel}{{{g(s, 'typography_typography')};display:inline-block;background:{bg};color:{fg};{border};"
                   f"border-radius:999px;padding:{box(p)};text-decoration:none;transition:transform .3s}}"
                   f"{sel}:hover{{transform:scale(1.1)}}")
        return f'<div><a class="el-{eid}" href="{html.escape(s["link"]["url"])}">{s["text"]}</a></div>'
    if w == "divider":
        css.append(f"{sel}{{width:{s['width']['size']}px;border-top:{s['weight']['size']}px solid {g(s, 'color')};margin:6px 0}}")
        return f'<div class="el-{eid}"></div>'
    if w == "icon":
        name = s["selected_icon"]["value"].split("fa-", 1)[1]
        css.append(f"{sel} svg{{width:{s['size']['size']}px;height:{s['size']['size']}px;fill:{g(s, 'primary_color')}}}")
        return f'<div class="el-{eid}">{ICONS.get(name, "★")}</div>'
    if w == "icon-box":
        name = s["selected_icon"]["value"].split("fa-", 1)[1]
        css.append(f"{sel} svg{{width:50px;height:50px;fill:{g(s, 'primary_color')}}}"
                   f"{sel} h3{{{g(s, 'title_typography_typography')};color:{g(s, 'title_color')};margin:16px 0 8px}}"
                   f"{sel} p{{{g(s, 'description_typography_typography')};color:{g(s, 'description_color')};margin:0}}")
        return (f'<div class="el-{eid}">{ICONS.get(name, "")}<h3>{s["title_text"]}</h3>'
                f'<p>{s["description_text"]}</p></div>')
    if w == "counter":
        css.append(f"{sel}{{text-align:center}}{sel} .num{{{g(s, 'typography_number_typography')};font-size:69px;"
                   f"color:{g(s, 'number_color')}}}{sel} .t{{{g(s, 'typography_title_typography')};"
                   f"color:{g(s, 'title_color')};margin-top:8px}}")
        return (f'<div class="el-{eid}"><div class="num">{s["ending_number"]}{s.get("suffix", "")}</div>'
                f'<div class="t">{s["title"]}</div></div>')
    if w == "image":
        url = s["image"]["url"]
        css.append(f"{sel} img{{width:100%;display:block;border-radius:{s['image_border_radius']['top']}px}}")
        return f'<div class="el-{eid}"><img src="{url}" alt=""></div>'
    return f"<!-- {w} -->"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        src = Path(sys.argv[1]).read_text()
        for m in re.finditer(r'<svg[^>]*class="e-font-icon-svg e-fas-([\w-]+)".*?</svg>', src, re.S):
            ICONS.setdefault(m.group(1), m.group(0))
    data = json.loads(Path("page-elementor-data.json").read_text())
    body = "".join(render(el) for el in data)
    page = f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Vista previa · Navidad Multiplaza 2026</title>
<link href="fonts/fonts.css" rel="stylesheet">
<style>body{{margin:0}}em{{font-style:italic}}{''.join(css)}</style></head><body>{body}</body></html>"""
    Path("preview").mkdir(exist_ok=True)
    Path("preview/index.html").write_text(page)
    print("ok preview/index.html", len(page), "bytes;", len(ICONS), "iconos")
