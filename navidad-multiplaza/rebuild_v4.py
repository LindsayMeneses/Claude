"""Reconstruye la página de Navidad Multiplaza 2026 (versión completa del 28-09, 22:18) como datos de Elementor.

La versión original se sobrescribió el 29-09 y solo quedó su HTML (respaldo/pagina7-2026-09-28-2218.html).
Este script recorre ese HTML y vuelve a armar cada contenedor y widget (títulos, textos, divisores y
galerías) con los estilos globales del sitio. Además agrega:
  - la barra y el menú de lindsaymeneses.com (shell_markup de sitio/sitio.py);
  - botones nativos de Elementor en lugar de enlaces HTML;
  - el formulario de Elementor Pro en el cierre;
  - efectos de movimiento de Elementor Pro (desplazamiento vertical suave) en las fotos grandes.

Uso:  python3 rebuild_v4.py  ->  page-elementor-data.json (meta _elementor_data de la página 7)
"""
import json
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent / "sitio"))
from sitio import shell_markup  # noqa: E402

SRC = HERE / "respaldo/pagina7-2026-09-28-2218.html"
C = "globals/colors?id="
T = "globals/typography?id="
MAIL = "mailto:contacto@lindsaymeneses.com?subject=Navidad%20Multiplaza%202026"

_seq = iter(range(1, 10**6))


def uid():
    return f"v{next(_seq):06x}"


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


def sizes(fs):
    return {"typography_font_size": px(fs), "typography_font_size_tablet": px(round(fs * .8)),
            "typography_font_size_mobile": px(max(round(fs * .58), 20))}


def buttons(items, align="left"):
    """Botones nativos: mismo borde y alto en las dos variantes, para que queden alineados."""
    out = []
    for label, url, ghost in items:
        s = {"text": label, "link": {"url": url}, "size": "md", "_element_width": "auto", "_element_width_mobile": "inherit",
             "align_mobile": "justify", "_css_classes": "nm-ebtn", "border_border": "solid",
             "border_width": {"unit": "px", "top": 1, "right": 1, "bottom": 1, "left": 1, "isLinked": True},
             "border_radius": {"unit": "px", "top": 0, "right": 0, "bottom": 0, "left": 0, "isLinked": True},
             "text_padding": pad(19, 32), "__globals__": {"typography_typography": T + "accent"}}
        if ghost:
            s["background_color"] = "transparent"
            s["__globals__"].update({"button_text_color": C + "blanco", "border_color": C + "oroclaro",
                                     "button_background_hover_color": C + "accent", "hover_color": C + "noche",
                                     "button_hover_border_color": C + "accent"})
        else:
            s["__globals__"].update({"background_color": C + "accent", "button_text_color": C + "noche", "border_color": C + "accent",
                                     "button_background_hover_color": C + "oroclaro", "hover_color": C + "noche",
                                     "button_hover_border_color": C + "oroclaro"})
        out.append(widget("button", s))
    return container(out, {"flex_direction": "row", "flex_direction_mobile": "column", "flex_wrap": "wrap", "gap": gap(14),
                           "flex_align_items": "center", "flex_justify_content": "center" if align == "center" else "flex-start",
                           "flex_align_items_mobile": "stretch"})


def form():
    """Formulario de Elementor Pro: envía a contacto@ y guarda cada envío en Elementor → Envíos."""
    def f(i, kind, label, ph, req=True, w="50"):
        return {"_id": f"nm{i}", "custom_id": kind if kind in ("name", "email", "message") else f"campo{i}",
                "field_type": "textarea" if kind == "message" else ("email" if kind == "email" else "text"),
                "field_label": label, "placeholder": ph, "required": "true" if req else "", "width": w,
                "width_mobile": "100", "rows": 4}
    return widget("form", {
        "form_name": "Navidad Multiplaza 2026 · Conversemos",
        "form_fields": [f(1, "name", "Nombre", "Tu nombre"), f(2, "email", "Correo", "tu@empresa.com"),
                        f(3, "empresa", "Empresa o área", "Opcional", req=False, w="100"),
                        f(4, "message", "Mensaje", "¿Qué te gustaría conversar sobre la propuesta?", w="100")],
        "show_labels": "yes", "input_size": "md", "button_size": "md", "button_width": "100",
        "button_text": "Enviar mensaje", "submit_actions": ["email", "collect_submissions"],
        "email_to": "contacto@lindsaymeneses.com", "email_subject": "Navidad Multiplaza 2026 · Nuevo mensaje",
        "email_content": "[all-fields]", "email_from_name": "Navidad Multiplaza 2026", "email_reply_to": "email",
        "success_message": "¡Gracias! Recibimos tu mensaje y te responderemos pronto.",
        "error_message": "No se pudo enviar. Escríbenos a contacto@lindsaymeneses.com.",
        "required_field_message": "Este campo es obligatorio.", "invalid_message": "Revisa este dato.",
        "_css_classes": "nm-form", "_element_width": "initial", "_element_custom_width": px(640),
        "_element_custom_width_mobile": px(100, "%"),
        "__globals__": {"label_typography_typography": T + "accent", "field_typography_typography": T + "text",
                        "button_typography_typography": T + "accent", "label_color": C + "oroclaro",
                        "field_text_color": C + "blanco", "button_background_color": C + "accent",
                        "button_text_color": C + "noche", "button_background_hover_color": C + "oroclaro",
                        "button_hover_color": C + "noche"},
    })


# Efecto de movimiento de Elementor Pro: la foto se desplaza un poco más lento que la página.
PARALLAX = {"motion_fx_motion_fx_scrolling": "yes", "motion_fx_translateY_effect": "yes",
            "motion_fx_translateY_speed": px(1.2), "motion_fx_translateY_affectedRange": {"unit": "%", "size": "", "sizes": {"start": 0, "end": 100}},
            "motion_fx_devices": ["desktop", "tablet"]}

# Ajustes al CSS original: la barra del sitio reemplaza la marca del recorrido y el formulario toma la paleta.
CSS_EXTRA = (".nm-brand{display:none!important}.nm-tour .nm-bar{top:0}"
             ".nm-form .elementor-field-group .elementor-field{background:rgba(7,24,18,.55)!important;border:1px solid rgba(201,164,92,.45)!important;border-radius:0!important;color:#fff!important}"
             ".nm-form .elementor-field::placeholder{color:rgba(235,217,174,.55)}"
             ".nm-form .elementor-field-label{letter-spacing:.2em;text-transform:uppercase;font-size:11px}"
             ".nm-form .elementor-button{border-radius:0!important;min-height:54px;letter-spacing:.22em;text-transform:uppercase}"
             ".nm-ebtn .elementor-button{min-height:54px;display:inline-flex;align-items:center;justify-content:center}"
             ".nm-dark .nm-note a,.nm-footer a{color:#EBD9AE}")


def inner_html(el):
    return "".join(str(c) for c in el.contents).strip()


def slim(markup):
    """Aligera el HTML de las galerías sin cambiar lo que se ve: rutas relativas, miniaturas sin srcset
    (se muestran a menos de 400 px, basta la versión de 1024) y sin espacios entre etiquetas."""
    markup = markup.replace("https://lindsaymeneses.com/wp-content/", "/wp-content/")
    markup = re.sub(r'(<figure class="nm-tile[^>]*>.*?</figure>)',
                    lambda m: re.sub(r' srcset="[^"]*"| sizes="[^"]*"', "", m.group(1)), markup, flags=re.S)
    return re.sub(r">\s+<", "><", markup)


def classes(el):
    return [c for c in el.get("class", []) if c.startswith("nm-")]


def kids(el):
    base = el.find("div", class_="e-con-inner", recursive=False) or el
    return [c for c in base.find_all("div", recursive=False) if c.get("data-element_type")]


def has_media(el):
    s = str(el)
    return any(k in s for k in ('class="nm-frame', 'class="nm-grid', 'class="nm-cmp', 'nm-mirror'))


class Ctx:
    def __init__(self, dark):
        self.dark = dark


def conv_widget(el, ctx):
    kind = el["data-widget_type"].split(".")[0]
    cls = classes(el)
    center = "nm-c" in cls or (kind == "heading" and "nm-t" in cls and getattr(ctx, "center", False))
    right = "nm-r" in cls
    align = "center" if center else ("right" if right else "left")
    css = " ".join(cls)

    if kind == "heading":
        t = el.find(class_="elementor-heading-title")
        tag = t.name
        title = inner_html(t)
        if "nm-eyebrow" in cls:
            return widget("heading", {"title": title, "header_size": "p", "align": align, "_css_classes": css,
                                      "__globals__": {"title_color": C + ("accent" if ctx.dark else "secondary"),
                                                      "typography_typography": T + "accent"}})
        s = {"title": title, "header_size": tag, "align": align, "_css_classes": css,
             "__globals__": {"title_color": C + ("blanco" if ctx.dark else "primary"), "typography_typography": T + "primary"}}
        if "nm-hero-t" in cls:
            s.update(sizes(104))
        elif tag == "h1":
            s.update(sizes(88))
        elif tag == "h2":
            s.update(sizes(60 if ctx.dark else 56))
        elif tag == "h3":
            s.update(sizes(24))
        return widget("heading", s)

    if kind == "text-editor":
        s = {"editor": inner_html(el), "align": align,
             "__globals__": {"text_color": C + ("oroclaro" if ctx.dark else "text"), "typography_typography": T + "text"}}
        if css:
            s["_css_classes"] = css
        if "elementor-widget__width-initial" in el.get("class", []):
            s.update({"_element_width": "initial", "_element_custom_width": px(560),
                      "_element_custom_width_mobile": px(100, "%")})
        return widget("text-editor", s)

    if kind == "divider":
        return widget("divider", {"width": px(90 if center else 72), "weight": px(1), "align": align, "_css_classes": css or "nm-line",
                                  "__globals__": {"color": C + "accent"}})

    if kind == "html":
        markup = inner_html(el)
        if markup.startswith('<div class="nm-btns'):          # enlaces HTML -> botones nativos
            soup = BeautifulSoup(markup, "html.parser")
            items = [(a.get_text(strip=True), a["href"], "ghost" in a.get("class", [])) for a in soup.find_all("a")]
            if any(i[1].startswith("mailto:") for i in items):   # cierre: formulario Pro
                return "CIERRE", items
            return buttons(items, "center" if "center" in markup[:80] else "left")
        s = {"html": markup if "nm-fx" in cls else slim(markup)}
        if css:
            s["_css_classes"] = css
        if "nm-frame-w" in cls:
            s.update(PARALLAX)
        return widget("html", s)

    raise ValueError(kind)


def conv_children(el, ctx):
    # si el antetítulo del grupo va centrado, el título grande también
    ctx.center = any("nm-eyebrow" in c.get("class", []) and "nm-c" in c.get("class", []) for c in kids(el))
    out = []
    for c in kids(el):
        if c["data-element_type"] == "container":
            out.append(conv_container(c, ctx))
            continue
        w = conv_widget(c, ctx)
        if isinstance(w, tuple):   # botones del cierre
            back = [i for i in w[1] if not i[1].startswith("mailto:")]
            out.append(form())
            out.append(widget("text-editor", {
                "editor": '<p>¿Prefieres el correo? <a href="' + MAIL + '">contacto@lindsaymeneses.com</a></p>',
                "align": "center", "_css_classes": "nm-note",
                "__globals__": {"text_color": C + "oroclaro", "typography_typography": T + "text"}}))
            if back:
                out.append(buttons(back, "center"))
        else:
            out.append(w)
    return out


def conv_container(el, ctx):
    ch = kids(el)
    sub = [c for c in ch if c["data-element_type"] == "container"]
    if len(sub) >= 2 and len(sub) == len(ch):          # fila de columnas
        kinds = ["m" if has_media(c) and not c.find(attrs={"data-widget_type": "heading.default"}) else "t" for c in sub]
        if len(sub) == 2 and kinds.count("m") == 1:
            widths = [52 if k == "m" else 44 for k in kinds]
        else:
            widths = [round(96 / len(sub))] * len(sub)
        cols = []
        for c, w in zip(sub, widths):
            cc = conv_children(c, ctx)
            cols.append(container(cc, {"width": px(w, "%"), "width_tablet": px(100, "%"), "width_mobile": px(100, "%"),
                                       "flex_justify_content": "center", "gap": gap(22)}))
        return container(cols, {"flex_direction": "row", "flex_wrap": "nowrap", "flex_direction_tablet": "column",
                                "flex_direction_mobile": "column", "gap": gap(64), "flex_align_items": "center"})
    return container(conv_children(el, ctx), {"gap": gap(22), "flex_justify_content": "center"})


def conv_slide(el, light_i):
    cls = classes(el)
    dark = "nm-dark" in cls or "nm-footer" in cls
    ctx = Ctx(dark)
    if "nm-footer" in cls:
        s = {"content_width": "boxed", "boxed_width": px(1200), "flex_direction": "column", "padding": pad(64, 56, 40, 56),
             "padding_mobile": pad(48, 22, 110, 22), "gap": gap(28), "background_background": "classic",
             "__globals__": {"background_color": C + "noche"}, "css_classes": "nm-footer"}
        return container(footer(el), s, inner=False)
    bg = "noche" if dark else ("marfil" if light_i % 2 == 0 else "blanco")
    s = {"content_width": "boxed", "boxed_width": px(1200), "flex_direction": "column", "flex_justify_content": "center",
         "min_height": px(100, "vh"), "padding": pad(120, 56), "padding_tablet": pad(96, 40), "padding_mobile": pad(84, 22),
         "gap": gap(30), "background_background": "classic", "__globals__": {"background_color": C + bg},
         "css_classes": " ".join(cls)}
    if el.get("id"):
        s["_element_id"] = el["id"]
    if "nm-center" in cls:
        s["flex_align_items"] = "center"
    children = conv_children(el, ctx)
    if "nm-hero" in cls:   # el primer widget (nm-fx) lleva el CSS/JS: se le suma la barra del sitio
        fx = children[0]
        fx["settings"]["html"] = shell_markup() + fx["settings"]["html"].replace("</style>", CSS_EXTRA + "</style>", 1)
    return container(children, s, inner=False)


def footer(el):
    """Pie: tres columnas (marca · temporada · contacto), divisor y créditos."""
    out = []
    for c in kids(el):
        if c["data-element_type"] == "container":
            cols = []
            for col in kids(c):
                ws = []
                for w in kids(col):
                    t = w.find(class_="elementor-heading-title")
                    wc = classes(w)
                    al = "right" if "nm-r" in wc else ("center" if len(cols) == 1 else "left")
                    if t is not None:
                        txt = inner_html(t)
                        typo, color, fs = ("primary", "blanco", 30) if txt == "Multiplaza" else \
                            ("secondary", "oroclaro", 20) if len(cols) == 1 else ("accent", "accent", None)
                        s = {"title": txt, "header_size": "p", "align": al, "_css_classes": " ".join(wc),
                             "__globals__": {"title_color": C + color, "typography_typography": T + typo}}
                        if fs:
                            s.update(sizes(fs))
                        ws.append(widget("heading", s))
                    else:
                        ws.append(widget("text-editor", {"editor": inner_html(w), "align": al, "_css_classes": " ".join(wc),
                                                         "__globals__": {"text_color": C + "oroclaro", "typography_typography": T + "text"}}))
                cols.append(container(ws, {"width": px(32, "%"), "width_mobile": px(100, "%"), "flex_justify_content": "center",
                                           "gap": gap(6)}))
            out.append(container(cols, {"flex_direction": "row", "flex_wrap": "wrap", "flex_direction_mobile": "column",
                                        "gap": gap(24), "flex_align_items": "center"}))
        else:
            ctx = Ctx(True)
            w = conv_widget(c, ctx)
            if w["widgetType"] == "text-editor":
                w["settings"]["align"] = "center"
                w["settings"]["__globals__"]["text_color"] = C + "salvia"
            out.append(w)
    out.append(widget("text-editor", {"editor": '<p><a href="/proyectos/">← Lindsay Meneses · Proyectos</a></p>', "align": "center",
                                      "_css_classes": "nm-note", "__globals__": {"text_color": C + "oroclaro", "typography_typography": T + "text"}}))
    return out


def build():
    soup = BeautifulSoup(SRC.read_text(encoding="utf-8"), "html.parser")
    root = soup.find("div", attrs={"data-elementor-id": "7"})
    content, light_i = [], 0
    for el in root.find_all("div", recursive=False):
        content.append(conv_slide(el, light_i))
        if "nm-dark" not in el.get("class", []) and "nm-footer" not in el.get("class", []):
            light_i += 1
    return content


# CSS personalizado de la página 7 (Elementor Pro → Ajustes de página → CSS personalizado).
# Se guarda en _elementor_page_settings.custom_css: título de portada en cursiva, como el original.
PAGE_CSS = (".nm-hero-t .elementor-heading-title{font-style:italic!important;font-weight:600!important;"
            "letter-spacing:-.02em!important;line-height:1!important}\n.nm-hero-t .elementor-heading-title em{font-weight:300!important}")

TPL_CODIGO, TPL_PARTE2, CORTE = 162, 163, 12   # plantillas de Elementor Pro (Plantillas → Guardadas)


def template_widget(tid):
    return widget("template", {"template_id": str(tid)})


def split(content):
    """Reparte el contenido en tres documentos de Elementor, cada uno de un tamaño que se publica sin riesgo:
    la plantilla con el código (CSS, JS y menú), la página con las secciones 1–12 y la plantilla con las 13–25."""
    fx = content[0]["elements"][0]["settings"]
    code = "".join(re.findall(r"<style>.*?</style>|<script>.*?</script>", fx["html"], re.S))
    shell = re.match(r'<div class="lx-shell"[^>]*></div>', fx["html"]).group(0)
    fx["html"] = re.sub(r"<style>.*?</style>|<script>.*?</script>", "", fx["html"], flags=re.S).replace(shell, "")
    codigo = [container([widget("html", {"html": shell + code, "_css_classes": "lx-shell-w"})],
                        {"css_classes": "lx-shell-w"}, inner=False)]
    wrap = {"css_classes": "lx-shell-w"}
    pagina = ([container([template_widget(TPL_CODIGO)], wrap, inner=False)] + content[:CORTE]
              + [container([template_widget(TPL_PARTE2)], {"gap": gap(0)}, inner=False)])
    return pagina, codigo, content[CORTE:]


if __name__ == "__main__":
    for name, doc in zip(("page-elementor-data.json", "tpl-codigo.json", "tpl-parte2.json"), split(build())):
        # espacios normales en vez de no separables: se publican por transcripción y así no se pierden
        data = json.dumps(doc, ensure_ascii=False, separators=(",", ":")).replace("\u00a0", " ")
        (HERE / name).write_text(data, encoding="utf-8")
        print("ok", name, len(data), "bytes; escapado", len(json.dumps(data, ensure_ascii=False)))
