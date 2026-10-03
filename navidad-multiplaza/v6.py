"""Navidad Multiplaza 2026 · v6: la presentación con widgets nativos de Elementor Pro.

Genera cinco documentos de Elementor:
  tpl-codigo.json      (162) barra del sitio, CSS, navegación por secciones y comparadores (código recortado de la v4)
  tpl-portada.json     (168) portada: widget Slides de Elementor Pro (se cambia por el slider de Slider Revolution
                             con `python3 v6.py --revslider` cuando exista el slider `navidad-multiplaza-2026`)
  page-elementor-data.json (7) secciones 01–04 y Parte I · Multiplaza Escazú (portadilla, entradas, fachadas, capítulo)
  tpl-zonas.json       (169) Parte I · zonas 07–16 (vacíos, túnel de arcos, plazas y pasillos de Escazú)
  tpl-parte2.json      (163) Parte II · Multiplaza Curridabat, cifras, cierre y pie

Todo el contenido usa widgets nativos (heading, text-editor, divider, image, video, gallery de Pro, counter,
icon-list, icon-box, image-box, button, form de Pro, slides de Pro) con animaciones de entrada y efectos de
movimiento de Elementor. Solo los comparadores antes/después siguen siendo HTML, porque Elementor no tiene ese
widget. Los textos vienen de la v5 (fuente_v5.py) y se amplían con una frase de contexto por galería.

Uso:  python3 v6.py [--revslider]
"""
import json
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent / "sitio"))
from sitio import shell_markup  # noqa: E402

C = "globals/colors?id="
T = "globals/typography?id="
UP = "https://lindsaymeneses.com/wp-content/uploads/2026/09/"
MAIL = "mailto:contacto@lindsaymeneses.com?subject=Navidad%20Multiplaza%202026"
REVSLIDER_ALIAS = "navidad-multiplaza-2026"
TPL_CODIGO, TPL_PORTADA, TPL_ZONAS, TPL_PARTE2 = 162, 168, 169, 163   # plantillas de Elementor Pro (Plantillas → Guardadas)

# ------------------------------------------------------------------ medios (ID de la biblioteca de WordPress)
MEDIA = {
    "textura-madera-oscura": 157, "textura-dorado-antiguo": 156, "textura-terciopelo-burdeos": 155,
    "textura-piedra-negra": 154, "textura-metal-brunido": 153, "textura-fibra-natural": 152,
    "fachada-esc-automercado-3.mp4": 151, "fachada-esc-automercado-3": 150, "fachada-esc-automercado-2.mp4": 149,
    "fachada-esc-automercado-2": 148, "fachada-esc-automercado-1.mp4": 147, "fachada-esc-automercado-1": 146,
    "fachada-esc-cinemark.mp4": 145, "fachada-esc-cinemark": 144, "fachada-esc-esquinera.mp4": 143,
    "fachada-esc-esquinera": 142, "fachada-esc-mccafe.mp4": 141, "fachada-esc-mccafe": 140,
    "fachada-esc-bcr.mp4": 139, "fachada-esc-bcr": 138, "fachada-esc-lateral.mp4": 137, "fachada-esc-lateral": 136,
    "fachada-esc-universal.mp4": 135, "fachada-esc-universal": 134, "fachada-esc-multiplaza.mp4": 133,
    "fachada-esc-multiplaza": 132, "fachada-esc-principal.mp4": 131, "fachada-esc-principal": 130,
    "fachada-curri-entrada.mp4": 129, "fachada-curri-entrada": 128, "fachada-curri-zara.mp4": 127,
    "fachada-curri-zara": 126, "fachada-curri-zara-esquina.mp4": 125, "fachada-curri-zara-esquina": 124,
    "fachada-curri-hm.mp4": 123, "fachada-curri-hm": 122, "fachada-curri-lateral.mp4": 121, "fachada-curri-lateral": 120,
    "fachada-curri-principal.mp4": 119, "fachada-curri-principal": 118,
    "palmeras-iluminadas": 117, "vacio-esc-cupula": 116, "vacio-esc-esferas": 115, "vacio-esc-atrio-b": 114,
    "vacio-esc-atrio-a": 113, "fachada-esc-bershka": 112, "fachada-esc-hm-smartfit": 111,
    "vacio-curri-foodcourt-b": 110, "vacio-curri-foodcourt-a": 109, "vacio-curri-pasillo-largo": 108,
    "vacio-curri-estrellas": 107, "vacio-curri-naturalizer-b": 106, "vacio-curri-naturalizer-a": 105,
    "vacio-curri-universal-b": 104, "vacio-curri-universal-a": 103, "vacio-curri-pasillo-b": 102,
    "vacio-curri-pasillo-a": 101, "vacio-curri-koaj-b": 100, "vacio-curri-koaj-a": 99,
    "plaza-cinemark-render": 98, "plaza-reebok-detalle": 97, "plaza-reebok-render": 96, "equiz-vertigo-esferas": 95,
    "equiz-vertigo-cascabeles": 94, "santo-katrin-plano-2": 93, "santo-katrin-plano-1": 92, "santo-katrin-render": 91,
    "plaza-honor-tren": 90, "plaza-honor-render": 89, "pasillo-bcr-vertigo": 88, "banca-dorada": 87,
    "renos-dorados-2": 86, "renos-dorados-1": 85, "plaza-siman-render-3": 84, "plaza-siman-render-2": 83,
    "plaza-siman-render-1": 82, "quinta-etapa-ref": 81, "quinta-etapa-diametro": 80, "quinta-etapa-ficha": 79,
    "quinta-etapa-estrella": 78, "quinta-etapa-render": 77, "brunos-inspiracion-2": 76, "brunos-inspiracion-1": 75,
    "stand-kolbi": 74, "banca-plateada": 73, "plaza-brunos-carretilla": 72, "plaza-brunos-soldados-set": 71,
    "plaza-brunos-arboles": 70, "plaza-brunos-panoramica": 69, "plaza-brunos-simulador": 68,
    "plaza-brunos-soldados": 67, "plaza-brunos-stand": 66, "plaza-brunos-render-2": 65, "plaza-brunos-render-1": 64,
    "logo-kolbi": 63, "logo-xiaomi.png": 62, "plaza-tukis-render-3": 61, "plaza-tukis-render-2": 60,
    "plaza-tukis-render-1": 59, "plaza-tukis-plano": 58, "casa-santa-interior-2": 57, "casa-santa-interior-1": 56,
    "casa-de-santa": 55, "pasillo-starbucks-tukis": 54, "plaza-starbucks-arcos-ref": 53, "plaza-starbucks-render": 52,
    "red-silk-351516": 51, "macetero-plano": 50, "tunel-ref-4": 49, "tunel-ref-3": 48, "tunel-ref-2": 47,
    "tunel-ref-1": 46, "tunel-arcos-techo": 45, "tunel-arcos-frontal": 44, "tunel-arcos-pasillo": 43,
    "tunel-arcos-filigrana": 42, "tunel-arcos-render-2": 41, "tunel-arcos-render-1": 40, "cascabeles-referencia": 39,
    "kv-where-the-magic-begins": 38,
}


def media(key):
    """{url, id} de un medio: la clave es el nombre sin «nm26-» y, salvo para mp4/png, sin extensión."""
    name = "nm26-" + key + ("" if "." in key else ".jpg")
    return {"url": UP + name, "id": MEDIA[key]}


# ------------------------------------------------------------------ utilidades de Elementor
_seq = iter(range(1, 10**6))


def uid():
    return f"w{next(_seq):06x}"


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


def anim(s, kind="fadeInUp", delay=0, duration="slow"):
    """Animación de entrada nativa de Elementor (Avanzado → Efectos de movimiento → Animación de entrada)."""
    s["_animation"] = kind
    if delay:
        s["_animation_delay"] = delay
    if duration:
        s["animation_duration"] = duration
    return s


PARALLAX = {"motion_fx_motion_fx_scrolling": "yes", "motion_fx_translateY_effect": "yes",
            "motion_fx_translateY_speed": px(1.2),
            "motion_fx_translateY_affectedRange": {"unit": "%", "size": "", "sizes": {"start": 0, "end": 100}},
            "motion_fx_devices": ["desktop", "tablet"]}
MOUSE = {"motion_fx_motion_fx_mouse": "yes", "motion_fx_mouseTrack_effect": "yes",
         "motion_fx_mouseTrack_direction": "negative", "motion_fx_mouseTrack_speed": px(0.3)}


def sizes(fs):
    return {"typography_font_size": px(fs), "typography_font_size_tablet": px(round(fs * .8)),
            "typography_font_size_mobile": px(max(round(fs * .58), 20))}


def row(cols, widths, settings=None):
    s = {"flex_direction": "row", "flex_wrap": "nowrap", "flex_direction_tablet": "column",
         "flex_direction_mobile": "column", "gap": gap(56), "flex_align_items": "center"}
    s.update(settings or {})
    out = []
    for col, w in zip(cols, widths):
        out.append(container(col, {"width": px(w, "%"), "width_tablet": px(100, "%"), "width_mobile": px(100, "%"),
                                   "flex_justify_content": "center", "gap": gap(20)}))
    return container(out, s)


def grid(items, cols, gap_px=14, settings=None):
    """Fila que envuelve: cada hijo ocupa 100/cols % (2 columnas en celular, 1 si cols == 1)."""
    s = {"flex_direction": "row", "flex_wrap": "wrap", "gap": gap(gap_px), "flex_align_items": "stretch"}
    s.update(settings or {})
    w = round((100 - (cols - 1) * 1.3) / cols, 2)
    out = []
    for it in items:
        out.append(container(it if isinstance(it, list) else [it],
                             {"width": px(w, "%"), "width_tablet": px(48.5 if cols > 1 else 100, "%"),
                              "width_mobile": px(100 if cols <= 2 else 48.5, "%"), "gap": gap(8)}))
    return container(out, s)


# ------------------------------------------------------------------ widgets
def eyebrow(text, dark, center=False, delay=0):
    return widget("heading", anim({
        "title": text, "header_size": "p", "align": "center" if center else "left",
        "_css_classes": "nm-eyebrow nm-c" if center else "nm-eyebrow",
        "__globals__": {"title_color": C + ("accent" if dark else "secondary"), "typography_typography": T + "accent"}},
        "fadeIn", delay))


def title(html, dark, center=False, size=None, tag="h2", delay=100):
    s = {"title": html, "header_size": tag, "align": "center" if center else "left",
         "_css_classes": "nm-t nm-shine" if dark else "nm-t",
         "__globals__": {"title_color": C + ("blanco" if dark else "primary"), "typography_typography": T + "primary"}}
    s.update(sizes(size or (60 if dark else 56)))
    return widget("heading", anim(s, "fadeInUp", delay))


def divider(center=False, delay=200):
    return widget("divider", anim({"width": px(90 if center else 72), "weight": px(1), "align": "center" if center else "left",
                                   "_css_classes": "nm-line nm-c" if center else "nm-line",
                                   "__globals__": {"color": C + "accent"}}, "fadeIn", delay))


def text(html, dark, center=False, narrow=True, cls="", delay=250):
    s = {"editor": html, "align": "center" if center else "left",
         "__globals__": {"text_color": C + ("oroclaro" if dark else "text"), "typography_typography": T + "text"}}
    cls = " ".join(c for c in [cls, "nm-c" if center else ""] if c)
    if cls:
        s["_css_classes"] = cls
    if narrow:
        s.update({"_element_width": "initial", "_element_custom_width": px(560), "_element_custom_width_mobile": px(100, "%")})
    return widget("text-editor", anim(s, "fadeInUp", delay))


def credit(html, dark, delay=350):
    return widget("text-editor", anim({"editor": f'<p class="nm-credit">{html}</p>', "align": "left",
                                       "__globals__": {"text_color": C + ("oroclaro" if dark else "text"),
                                                       "typography_typography": T + "text"}}, "fadeIn", delay))


def intro(eye, ttl, body, dark, center=False, size=None):
    out = [eyebrow(eye, dark, center), title(ttl, dark, center, size), divider(center)]
    if body:
        out.append(text(body, dark, center))
    return out


def caption(ttl, sub, dark):
    """Pie de foto o video: nombre en Fraunces y subtítulo en Manrope espaciada."""
    return widget("heading", {"title": f"{ttl}<small>{sub}</small>", "header_size": "p", "align": "left",
                              "_css_classes": "nm-cap",
                              "__globals__": {"title_color": C + ("blanco" if dark else "primary"),
                                              "typography_typography": T + "secondary"}})


def video(key, poster_key, label, dark, ratio="43", frame=False, delay=0):
    """Video alojado nativo: autoplay silencioso en bucle; el JS de la plantilla 162 lo pausa fuera de pantalla."""
    s = {"video_type": "hosted", "hosted_url": media(key), "poster": media(poster_key), "autoplay": "yes", "mute": "yes",
         "loop": "yes", "play_on_mobile": "yes", "controls": "", "aspect_ratio": ratio, "_css_classes": "nm-vid",
         "video_aria_label": label}
    if frame:
        s["_css_classes"] += " nm-frame-w"
        s.update(PARALLAX)
    return widget("video", anim(s, "fadeIn", delay))


def image(key, alt, dark, caption_text=None, frame=False, lightbox=True, delay=0, size="large", hover="grow"):
    s = {"image": media(key), "image_size": size, "align": "left", "_css_classes": "nm-img",
         "link_to": "file" if lightbox else "none", "open_lightbox": "yes" if lightbox else "no"}
    if caption_text:
        s.update({"caption_source": "custom", "caption": caption_text})
    if hover and not frame:
        s["hover_animation"] = hover
    if frame:
        s["_css_classes"] += " nm-frame-w"
        s.update(PARALLAX)
    return widget("image", anim(s, "fadeIn", delay))


def gallery(keys, cols, ratio="4:3", delay=200, hover="zoom-in"):
    """Galería de Elementor Pro con lightbox nativo: muestra el título del medio al pasar el cursor."""
    return widget("gallery", anim({
        "gallery_type": "single", "gallery": [media(k) for k in keys], "gallery_layout": "grid",
        "columns": cols, "columns_tablet": min(cols, 3), "columns_mobile": 2, "gap": px(12), "gap_tablet": px(10),
        "gap_mobile": px(8), "aspect_ratio": ratio, "image_size": "large", "lazyload": "yes",
        "gallery_link": "file", "open_lightbox": "yes", "overlay_background": "yes", "overlay_title": "title",
        "overlay_description": "caption", "content_hover_animation": "fade-in", "image_hover_animation": hover,
        "content_alignment": "left", "content_vertical_position": "bottom", "_css_classes": "nm-gal",
        "__globals__": {"overlay_color": "", "title_typography_typography": T + "secondary",
                        "description_typography_typography": T + "accent"},
        "overlay_color": "rgba(7,24,18,0.72)", "title_color": "#FFFFFF", "description_color": "#EBD9AE"},
        "fadeInUp", delay))


ICON = {"value": "fas fa-gem", "library": "fa-solid"}


def icon_list(items, dark, icon=None, delay=300, inline=False):
    """Lista con icono dorado. Cada elemento puede ser texto o (etiqueta, valor)."""
    out = []
    for it in items:
        t = it if isinstance(it, str) else f"<strong>{it[0]}</strong> {it[1]}"
        out.append({"_id": uid()[1:], "text": t, "selected_icon": icon or ICON, "link": {"url": ""}})
    s = {"icon_list": out, "view": "inline" if inline else "traditional", "space_between": px(10), "icon_size": px(11),
         "icon_align": "left", "_css_classes": "nm-list",
         "__globals__": {"icon_color": C + "accent", "text_color": C + ("oroclaro" if dark else "text"),
                         "icon_typography_typography": T + "text"}}
    return widget("icon-list", anim(s, "fadeInUp", delay))


def counter(number, suffix, ttl, dark, prefix=""):
    return widget("counter", {
        "starting_number": 0, "ending_number": number, "prefix": prefix, "suffix": suffix, "duration": 2200,
        "thousand_separator": "", "title": ttl, "_css_classes": "nm-counter",
        "__globals__": {"number_color": C + ("accent" if dark else "secondary"),
                        "title_color": C + ("oroclaro" if dark else "text"),
                        "title_typography_typography": T + "text", "typography_number_typography": T + "primary"}})


def counters(items, dark, cols=None, delay=300):
    """items: (número, sufijo, texto)."""
    cols = cols or len(items)
    g = grid([counter(n, suf, t, dark) for n, suf, t in items], cols, 18)
    g["settings"].update({"_css_classes": "nm-counters"})
    g["settings"] = anim(g["settings"], "fadeInUp", delay)
    return g


def icon_box(icon, ttl, body, dark, delay=0):
    return widget("icon-box", anim({
        "selected_icon": {"value": icon, "library": "fa-solid"}, "title_text": ttl, "description_text": body,
        "position": "top", "text_align": "left", "title_size": "h3", "icon_space": px(14), "icon_size": px(26),
        "view": "default", "_css_classes": "nm-box",
        "__globals__": {"primary_color": C + "accent", "title_color": C + ("blanco" if dark else "primary"),
                        "description_color": C + ("oroclaro" if dark else "text"),
                        "title_typography_typography": T + "secondary", "description_typography_typography": T + "text"}},
        "fadeInUp", delay))


def image_box(key, ttl, body, dark, delay=0):
    return widget("image-box", anim({
        "image": media(key), "image_size": "large", "title_text": ttl, "description_text": body, "position": "top",
        "text_align": "left", "title_size": "h3", "image_space": px(14), "_css_classes": "nm-ibox",
        "__globals__": {"title_color": C + ("blanco" if dark else "primary"),
                        "description_color": C + ("oroclaro" if dark else "text"),
                        "title_typography_typography": T + "secondary", "description_typography_typography": T + "text"}},
        "fadeInUp", delay))


def buttons(items, align="left", delay=400):
    out = []
    for label, url, ghost in items:
        s = {"text": label, "link": {"url": url}, "size": "md", "_element_width": "auto", "_element_width_mobile": "inherit",
             "align_mobile": "justify", "_css_classes": "nm-ebtn", "border_border": "solid",
             "border_width": {"unit": "px", "top": 1, "right": 1, "bottom": 1, "left": 1, "isLinked": True},
             "border_radius": {"unit": "px", "top": 0, "right": 0, "bottom": 0, "left": 0, "isLinked": True},
             "text_padding": pad(19, 32), "hover_animation": "grow", "__globals__": {"typography_typography": T + "accent"}}
        if ghost:
            s["background_color"] = "transparent"
            s["__globals__"].update({"button_text_color": C + "blanco", "border_color": C + "oroclaro",
                                     "button_background_hover_color": C + "accent", "hover_color": C + "noche",
                                     "button_hover_border_color": C + "accent"})
        else:
            s["__globals__"].update({"background_color": C + "accent", "button_text_color": C + "noche", "border_color": C + "accent",
                                     "button_background_hover_color": C + "oroclaro", "hover_color": C + "noche",
                                     "button_hover_border_color": C + "oroclaro"})
        out.append(widget("button", anim(s, "fadeInUp", delay)))
    return container(out, {"flex_direction": "row", "flex_direction_mobile": "column", "flex_wrap": "wrap", "gap": gap(14),
                           "flex_align_items": "center", "flex_justify_content": "center" if align == "center" else "flex-start",
                           "flex_align_items_mobile": "stretch"})


def sponsor(key, name, dark):
    return widget("image", anim({"image": media(key), "image_size": "medium", "align": "left", "caption_source": "custom",
                                 "caption": f"Patrocinador · {name}", "_css_classes": "nm-sponsor", "width": px(150),
                                 "link_to": "none"}, "fadeIn", 400))


def form():
    def f(i, kind, label, ph, req=True, w="50"):
        return {"_id": f"nm{i}", "custom_id": kind if kind in ("name", "email", "message") else f"campo{i}",
                "field_type": "textarea" if kind == "message" else ("email" if kind == "email" else "text"),
                "field_label": label, "placeholder": ph, "required": "true" if req else "", "width": w,
                "width_mobile": "100", "rows": 4}
    return widget("form", anim({
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
                        "button_hover_color": C + "noche"}}, "fadeInUp", 300))


# ------------------------------------------------------------------ comparadores (HTML de la v5)
_V5 = BeautifulSoup((HERE / "fuente-v5.html").read_text(encoding="utf-8"), "html.parser")
_CMP = {}
for _f in _V5.select("figure.nm-cmp"):
    _k = re.sub(r"-\d+x\d+(?=\.\w+$)", "", _f.find("img")["src"].split("/")[-1])
    _CMP[_k.replace("nm26-", "").replace(".jpg", "")] = re.sub(r">\s+<", "><", str(_f)).replace(
        "https://lindsaymeneses.com/wp-content/", "/wp-content/")


def compare(keys, cols, delay=250):
    html = f'<div class="nm-grid g{cols}">' + "".join(_CMP[k] for k in keys) + "</div>"
    return widget("html", anim({"html": html, "_css_classes": "nm-cmpw"}, "fadeInUp", delay))


# ------------------------------------------------------------------ secciones
_light = iter(range(10**6))


def slide(children, dark=False, anchor=None, center=False, bg_video=None, bg_image=None, overlay=None, nm_title=None,
          cls=""):
    bg = "noche" if dark else ("marfil" if next(_light) % 2 == 0 else "blanco")
    classes = " ".join(c for c in ["nm-slide", "nm-dark" if dark else "", "nm-center" if center else "", cls] if c)
    s = {"content_width": "boxed", "boxed_width": px(1200), "flex_direction": "column", "flex_justify_content": "center",
         "min_height": px(100, "vh"), "padding": pad(120, 56), "padding_tablet": pad(96, 40), "padding_mobile": pad(84, 22),
         "gap": gap(30), "background_background": "classic", "__globals__": {"background_color": C + bg},
         "css_classes": classes}
    if anchor:
        s["_element_id"] = anchor
    if nm_title:
        s["_attributes"] = f"data-nm-title|{nm_title}"
    if center:
        s["flex_align_items"] = "center"
    if bg_video:
        s.update({"background_background": "video", "background_video_link": media(bg_video)["url"],
                  "background_video_fallback": media(bg_video.replace(".mp4", "")), "background_play_on_mobile": "yes",
                  "background_video_start": 0, "background_overlay_background": "classic",
                  "background_overlay_color": overlay or "rgba(7,24,18,0.62)"})
    elif bg_image:
        s.update({"background_image": media(bg_image), "background_position": "center center", "background_size": "cover",
                  "background_attachment": "scroll", "background_overlay_background": "classic",
                  "background_overlay_color": overlay or "rgba(7,24,18,0.74)"})
        if dark:
            s["__globals__"] = {}
            s["background_color"] = "#0A241C"
    return container(children, s, inner=False)


MECA = "Iluminación de fachadas, entradas y vacíos · <b>La Meca Concept</b>"
KARJIM = "Ambientación y decoración interior · <b>Karjim Design</b>"


def portada(revslider=False):
    """Plantilla 168. Con --revslider usa el slider de Slider Revolution (shortcode); si no, el widget Slides de Pro."""
    if revslider:
        hero = widget("shortcode", {"shortcode": f'[rev_slider alias="{REVSLIDER_ALIAS}"]', "_css_classes": "nm-rev"})
    else:
        def sl(i, key, head, desc, btn, url, pos="left", zoom="in"):
            return {"_id": f"nmsl{i}", "heading": head, "description": desc, "button_text": btn, "link": {"url": url},
                    "background_color": "#0A241C", "background_image": media(key), "background_size": "cover",
                    "background_ken_burns": "yes", "zoom_direction": zoom, "background_overlay": "yes",
                    "background_overlay_color": "rgba(7,24,18,0.52)", "background_overlay_blend_mode": "normal",
                    "horizontal_position": pos, "vertical_position": "middle", "text_align": pos,
                    "custom_style": "yes", "content_color": "#FBF6EC"}
        hero = widget("slides", {
            "slides": [
                sl(1, "fachada-esc-principal", "Where the Magic Begins",
                   "Navidad 2026 · Multiplaza Escazú y Multiplaza Curridabat. Un recorrido en tres capas: entradas, fachadas y decoración interna.",
                   "Recorrer Escazú", "#escazu"),
                sl(2, "tunel-arcos-render-1", "Un túnel de arcos y cascabeles",
                   "Arcos de guirnalda, moños de terciopelo y cascabeles dorados acompañan todo el pasillo de Escazú.",
                   "Ver el túnel", "#arcos", zoom="out"),
                sl(3, "plaza-starbucks-render", "Un túnel de luz hacia el árbol",
                   "Plaza Starbucks: los arcos guían, por ambos lados, hasta el árbol Gift of Joy.", "Ver Plaza Starbucks", "#starbucks"),
                sl(4, "plaza-brunos-render-1", "Un árbol de 7 metros",
                   "Plaza Brunos: soldados, regalos, trineo y escaleras espejadas alrededor del árbol kölbi.",
                   "Ver Plaza Brunos", "#brunos", zoom="out"),
                sl(5, "plaza-siman-render-1", "Carrusel dorado y renos",
                   "Plaza Siman: un árbol dentro de un carrusel dorado sobre base roja BAC.", "Ver Plaza Siman", "#siman"),
                sl(6, "fachada-curri-principal", "Curridabat: la misma magia, otro escenario",
                   "Entradas, fachadas y plazas que retoman lo mejor de Escazú.", "Ir a Curridabat", "#curridabat", zoom="out"),
                sl(7, "santo-katrin-render", "Un área de juego de 4 × 22 m",
                   "Plaza Santo Katrin: ball pit, toboganes y casitas bajo un cielo de esferas.", "Ver Santo Katrin", "#katrin"),
                sl(8, "plaza-reebok-render", "Árboles de espejo",
                   "Plaza Reebok: reflejos que multiplican la luz de la plaza.", "Ver Plaza Reebok", "#reebok", zoom="out"),
            ],
            "slides_height": px(100, "vh"), "slides_height_mobile": px(88, "vh"), "content_max_width": px(760, "px"),
            "slide_padding": pad(80, 120), "slide_padding_mobile": pad(48, 24),
            "navigation": "both", "pause_on_hover": "yes", "pause_on_interaction": "yes", "autoplay": "yes",
            "autoplay_speed": 7000, "infinite": "yes", "transition": "fade", "transition_speed": 1400,
            "content_animation": "fadeInUp", "arrows_position": "inside", "arrows_size": px(44), "dots_size": px(8),
            "heading_spacing": px(18), "description_spacing": px(26),
            "_css_classes": "nm-slides",
            "__globals__": {"heading_typography_typography": T + "primary", "description_typography_typography": T + "text",
                            "button_typography_typography": T + "accent", "arrows_color": C + "oroclaro", "dots_color": C + "accent",
                            "heading_color": C + "blanco", "description_color": C + "oroclaro",
                            "button_color": C + "noche", "button_background_color": C + "accent",
                            "button_border_color": C + "accent"},
            "heading_typography_font_size": px(84), "heading_typography_font_size_tablet": px(60),
            "heading_typography_font_size_mobile": px(40), "heading_typography_font_weight": "300",
            "heading_typography_line_height": px(1.02, "em"), "heading_typography_letter_spacing": px(-1.5),
            "description_typography_font_size": px(19), "description_typography_font_size_mobile": px(16),
            "button_border_width": px(1), "button_border_radius": px(0), "button_size": "md",
        })
    return [container([hero], {"content_width": "full", "padding": pad(0), "css_classes": "nm-slide nm-hero",
                               "_element_id": "inicio", "_attributes": "data-nm-title|Portada",
                               "background_background": "classic", "background_color": "#0A241C"}, inner=False)]


def comun():
    """Secciones 01–04: propuesta, campaña, lenguaje de diseño y sistema de iluminación."""
    out = []
    # 01 La propuesta: índice con listas nativas
    def zone_list(ttl, sub, items, dark=False):
        return [widget("heading", anim({"title": f"{ttl}<span>{sub}</span>", "header_size": "h3", "align": "left",
                                        "_css_classes": "nm-h3",
                                        "__globals__": {"title_color": C + "primary", "typography_typography": T + "accent"}},
                                       "fadeIn", 200)),
                icon_list(items, dark, delay=300)]
    out.append(slide([
        row([intro("01 La propuesta", "Dos centros, <em>un mismo lenguaje de luz</em>",
                   "<p>La Navidad 2026 de Multiplaza se vive como un recorrido. Empieza en la calle, con las entradas y las "
                   "fachadas encendidas, y continúa adentro: vacíos, pasillos y plazas se transforman zona por zona. "
                   "Escazú y Curridabat comparten el concepto y cada centro lo interpreta con sus propios espacios.</p>", False)
             + [credit(MECA + "<br>" + KARJIM, False)],
             zone_list("Cómo se organiza", "Tres capas",
                       [("Entradas", "la bienvenida desde el acceso"), ("Fachadas", "la luz que anuncia desde la calle"),
                        ("Decoración interna", "vacíos, pasillos y plazas")])],
            [52, 44]),
        row([zone_list("Parte I", "Multiplaza Escazú",
                       ["Entradas y accesos", "Fachadas", "Vacíos y tragaluces", "Túnel de arcos", "Plaza Starbucks",
                        "Pasillo Starbucks → Tukis y Casa de Santa", "Plaza Tukis", "Plaza Brunos", "Pasillo Quinta Etapa",
                        "Plaza Siman", "Pasillo BCR – Vértigo", "Plaza Honor"]),
             zone_list("Parte II", "Multiplaza Curridabat",
                       ["Entradas y accesos", "Fachadas", "Vacíos y food court", "Plaza Santo Katrin", "Pasillo Equiz – Vértigo",
                        "Plaza Reebok", "Plaza Cinemark", "Plaza Kolbi", "Plaza Old Navy"])
             + [text("<p class=\"nm-note\">Plaza Cinemark y Plaza Kolbi retoman diseños de Escazú; Plaza Old Navy repite Plaza Honor.</p>",
                     False, narrow=False, delay=350)]],
            [48, 48], {"flex_align_items": "flex-start"}),
    ], anchor="propuesta"))

    # 02 Campaña
    out.append(slide([row([
        intro("02 Campaña", "Una campaña, <em>un hilo dorado</em>",
              "<p>Toda la decoración nace del universo de <em>Where the Magic Begins</em>. Los key visuals de la campaña y "
              "los cascabeles dorados se repiten de la fachada a la última plaza, para que cada visitante reconozca la "
              "misma historia en cada rincón de los dos centros.</p>", True)
        + [icon_list(["Key visual de campaña", "Cascabeles dorados", "Moños de terciopelo rojo", "Rojo y dorado"], True, inline=True)],
        [image("kv-where-the-magic-begins", "Key visual Where the Magic Begins", True, frame=True),
         gallery(["cascabeles-referencia", "tunel-arcos-render-1"], 2, "3:4", 300)]],
        [44, 52])], dark=True))

    # 03 Lenguaje de diseño (paleta y materiales siguen en HTML: son fichas de diseño sin equivalente nativo)
    pal = _V5.find("div", class_="nm-bar5")
    pal_html = re.sub(r">\s+<", "><", str(pal) + str(pal.find_next_sibling("ul")) + str(pal.find_next_sibling("div", class_="nm-rule")))
    mats = re.sub(r">\s+<", "><", str(_V5.find("ul", class_="nm-mats"))).replace("https://lindsaymeneses.com/wp-content/", "/wp-content/")
    out.append(slide([
        row([intro("03 Lenguaje de diseño", "The Origin Workshop · <em>Before the Light</em>",
                   "<p>El sistema visual de la propuesta se apoya en <strong>cinco tonos en una proporción fija</strong> y "
                   "<strong>seis materiales que se reconocen antes de tocarlos</strong>: madera oscura, dorado antiguo, "
                   "terciopelo, piedra, metal bruñido y fibra natural.</p>", False) + [credit(KARJIM, False)],
             [widget("html", anim({"html": pal_html}, "fadeInUp", 200))]], [48, 48]),
        widget("html", anim({"html": mats}, "fadeInUp", 300)),
    ]))

    # 04 Sistema de iluminación: tres cajas de icono nativas
    layers = [("fas fa-moon", "Capa 01 · Ambiental",
               "Crea la oscuridad controlada del espacio. No se ve: se siente. 2700 K máximo, intensidad muy baja y continua, nunca la fuente a la vista."),
              ("fas fa-lightbulb", "Capa 02 · Puntual",
               "Dirige la mirada hacia el elemento protagonista. Spots de precisión, halo de corte limpio: solo el objeto existe."),
              ("fas fa-star", "Capa 03 · Espectacular",
               "Filamentos y cortinas LED en dorado, el gesto cinematográfico. Cálido, nunca multicolor; muy lento o estático, nunca intermitente.")]
    out.append(slide(
        intro("04 Sistema de iluminación", "Tres capas <em>de luz cálida</em>",
              "<p>La luz se construye en tres capas que se suman sin competir: una base ambiental que apenas se percibe, acentos "
              "puntuales que revelan cada pieza y el gesto espectacular de filamentos y cortinas LED en dorado.</p>", True)
        + [grid([icon_box(i, t, b, True, 150 + k * 120) for k, (i, t, b) in enumerate(layers)], 3, 24),
           text("<p class=\"nm-rule\"><b>Regla de oro</b><span>Si desde fuera del espacio no se ve la luz sino solo el efecto, el diseño está bien ejecutado.</span></p>",
                True, narrow=False, delay=450),
           credit(KARJIM, True)],
        dark=True, bg_image="vacio-curri-foodcourt-b"))
    return out


def portadilla(anchor, eye, ttl, body, cards, bg_video):
    return slide(intro(eye, ttl, body, True)
                 + [grid([icon_box(i, t, b, True, 200 + k * 120) for k, (i, t, b) in enumerate(cards)], 3, 20),
                    credit(MECA + " · " + KARJIM, True)],
                 dark=True, anchor=anchor, bg_video=bg_video, nm_title=eye)


def capitulo(eye, ttl, body, boxes, bg_image):
    return slide(intro(eye, ttl, body, True, center=True)
                 + [grid([image_box(k, t, b, True, 200 + i * 120) for i, (k, t, b) in enumerate(boxes)], 3, 20)],
                 dark=True, bg_image=bg_image, center=True, nm_title=eye)


def vcard(key, label, dark, ratio="43"):
    return [video(key, key.replace(".mp4", ""), label, dark, ratio), caption(*label.split(" · ", 1), dark) if " · " in label else caption(label, "Animación de luz", dark)]


def icard(key, ttl, sub, dark):
    return [image(key, ttl, dark, delay=100), caption(ttl, sub, dark)]


def parte1():
    out = []
    out.append(portadilla("escazu", "Parte I · Multiplaza Escazú", "Escazú: <em>donde empieza la magia</em>",
                          "<p>El recorrido arranca en Escazú y se cuenta en tres capas: las entradas que dan la bienvenida, las fachadas "
                          "que convierten el edificio en un espectáculo de luz y una decoración interior que avanza por vacíos, "
                          "pasillos y plazas hasta Plaza Honor.</p>",
                          [("fas fa-door-open", "Entradas", "Entrada esquinera, puente del BCR y palmeras iluminadas en el acceso."),
                           ("fas fa-building", "Fachadas", "Nueve animaciones de luz sobre el edificio real y dos frentes comerciales."),
                           ("fas fa-tree", "Decoración interna", "Vacíos, pasillos y plazas: diez zonas, del túnel de arcos a Plaza Honor.")],
                          "fachada-esc-principal.mp4"))

    # 05 Entradas
    out.append(slide(intro("05 Escazú · Entradas", "La bienvenida <em>empieza afuera</em>",
                           "<p>Antes de cruzar la puerta, la Navidad ya recibe. La entrada esquinera y el puente del BCR se animan con "
                           "luz, y las palmeras del acceso se visten de luz cálida para marcar el camino hacia el interior.</p>", True, center=True)
                     + [grid([vcard("fachada-esc-esquinera.mp4", "Entrada esquinera · Escazú · animación de luz", True),
                              vcard("fachada-esc-bcr.mp4", "Puente BCR · Escazú · acceso peatonal · animación de luz", True),
                              icard("palmeras-iluminadas", "Palmeras iluminadas", "Escazú · acceso", True)], 3),
                        credit(MECA, True)], dark=True, center=True, anchor="entradas-escazu"))

    # 06 Fachadas
    fach = [("fachada-esc-multiplaza.mp4", "Fachada Multiplaza"), ("fachada-esc-universal.mp4", "Fachada Universal"),
            ("fachada-esc-lateral.mp4", "Fachada lateral"), ("fachada-esc-mccafe.mp4", "Muro McCafé"),
            ("fachada-esc-cinemark.mp4", "Fachada Cinemark"), ("fachada-esc-automercado-1.mp4", "Auto Mercado"),
            ("fachada-esc-automercado-2.mp4", "Auto Mercado · acceso"), ("fachada-esc-automercado-3.mp4", "Auto Mercado · vista general")]
    out.append(slide([
        row([intro("06 Escazú · Fachadas", "El edificio <em>se vuelve luz</em>",
                   "<p>El proyecto de fachadas llega a su etapa final: todas las fachadas del centro comercial ya están "
                   "resueltas. Cada vista proyecta la animación de luz propuesta sobre la fotografía real del edificio, "
                   "para ver exactamente cómo se encenderá.</p>", True)
             + [counters([(9, "", "animaciones de fachada"), (2, "", "renders de frentes comerciales")], True), credit(MECA, True)],
             [video("fachada-esc-principal.mp4", "fachada-esc-principal", "Fachada principal de Multiplaza Escazú, animación de luz", True, "32", frame=True),
              caption("Fachada principal", "Escazú · animación de luz", True)]], [44, 52]),
        text("<p>Cada frente del edificio, de la fachada Multiplaza a las tres vistas de Auto Mercado, con su animación en bucle. "
             "Los dos renders muestran los frentes comerciales de H&amp;M, Smart Fit, Zara, Bershka y Hooligans con cortinas de luz.</p>",
             True, narrow=False, delay=200),
        grid([vcard(k, t + " · Animación de luz", True) for k, t in fach]
             + [icard("fachada-esc-hm-smartfit", "H&amp;M · Smart Fit · Zara", "Render", True),
                icard("fachada-esc-bershka", "Bershka · Hooligans", "Render", True)], 4, 12),
    ], dark=True, anchor="fachadas"))

    # Capítulo decoración interna
    out.append(capitulo("Parte I · Decoración interna", "Adentro, <em>la magia se despliega</em>",
                        "<p>Diez zonas interiores, pensadas como una secuencia: cortinas de luz sobre los vacíos, un túnel de arcos que "
                        "acompaña el pasillo, plazas con árbol, ball pit y carrusel, y un cierre bajo la cúpula de Plaza Honor.</p>",
                        [("vacio-esc-esferas", "Vacíos", "Cortinas LED, esferas y adornos colgantes sobre los tragaluces."),
                         ("tunel-arcos-render-1", "Pasillos", "Túnel de arcos, Quinta Etapa, BCR – Vértigo y el pasillo hacia Plaza Tukis."),
                         ("plaza-honor-render", "Plazas", "Starbucks, Casa de Santa, Tukis, Brunos, Siman y Honor.")],
                        "plaza-brunos-render-1"))

    # 07 Vacíos
    out.append(slide([row([
        intro("07 Escazú · Vacíos", "Luz que cae <em>desde los tragaluces</em>",
              "<p>Cortinas LED descienden sobre tragaluces y vacíos, acompañadas de esferas y adornos colgantes que llenan la "
              "altura del edificio. Deslice sobre la primera imagen para comparar la cortina sola con la versión con adornos.</p>", False)
        + [credit(MECA, False)],
        [compare(["vacio-esc-atrio-a"], 1), gallery(["vacio-esc-esferas", "vacio-esc-cupula"], 2, "3:4", 300)]], [40, 56])],
        anchor="vacios-escazu"))

    # 08 Túnel de arcos
    out.append(slide([
        row([intro("08 Escazú · Túnel de arcos", "Túnel de arcos <em>y cascabeles</em>",
                   "<p>Arcos de guirnalda con moños de terciopelo rojo y cascabeles dorados, sobre maceteros en Red Silk, forman un "
                   "túnel que acompaña todo el pasillo. Una variante suma paneles de filigrana dorada iluminada para un efecto "
                   "más envolvente.</p>", True)
             + [icon_list([("Macetero", "65 × 65 × 60 cm"), ("Tapa", "extraíble, con orificio de 15 cm"), ("Color", "Red Silk 351516"),
                           ("Adorno", "moño de terciopelo rojo y cascabeles dorados")], True), credit(KARJIM, True)],
             [image("tunel-arcos-render-1", "Túnel de arcos", True, frame=True)]], [44, 52]),
        text("<p>La serie completa: renders del túnel desde el pasillo, el frente y el techo, el plano del macetero, la muestra de color y las referencias que inspiran la pieza.</p>", True, narrow=False, delay=200),
        gallery(["tunel-arcos-render-2", "tunel-arcos-filigrana", "tunel-arcos-pasillo", "tunel-arcos-frontal", "tunel-arcos-techo",
                 "macetero-plano", "red-silk-351516", "tunel-ref-1", "tunel-ref-2", "tunel-ref-4"], 5),
    ], dark=True, anchor="arcos"))

    # 09 Plaza Starbucks
    out.append(slide([row([
        intro("09 Escazú · Plaza Starbucks", "Un túnel de luz <em>hacia el árbol</em>",
              "<p>Los arcos de la plaza se convierten en un túnel de luz que guía, por ambos lados, hacia el túnel del "
              "árbol Gift of Joy: un camino que invita a entrar y a quedarse.</p>", True)
        + [icon_list(["Túnel de luz en los arcos", "Túnel del árbol", "Acceso por ambos lados", "Árbol Gift of Joy"], True, inline=True),
           credit(KARJIM, True)],
        [gallery(["plaza-starbucks-render", "plaza-starbucks-arcos-ref"], 2, "3:4", 200)]], [46, 50])],
        dark=True, anchor="starbucks", bg_image="plaza-starbucks-render", overlay="rgba(7,24,18,0.78)"))

    # 10 Pasillo y Casa de Santa
    out.append(slide(intro("10 Escazú · Pasillo y Casa de Santa", "De Plaza Starbucks <em>a Plaza Tukis</em>", "", False) + [row([
        [image("pasillo-starbucks-tukis", "Pasillo Plaza Starbucks → Tukis", False, frame=True),
         text("<p>Adornos colgantes rojos y dorados flotan entre cortinas de luz sobre el vacío del pasillo que une Plaza "
              "Starbucks con Plaza Tukis.</p>", False, narrow=False)],
        [gallery(["casa-de-santa", "casa-santa-interior-1", "casa-santa-interior-2"], 3, "3:4", 200),
         text("<p><strong>Casa de Santa.</strong> Una cabaña de madera con guirnaldas, pensada como taller: madera, relojes, "
              "chimenea y detalles dorados que invitan a asomarse.</p>", False, narrow=False, cls="nm-prose"),
         credit(KARJIM, False)]], [48, 48])], anchor="santa"))

    # 11 Plaza Tukis
    out.append(slide([row([
        intro("11 Escazú · Plaza Tukis", "Un ball pit <em>de 158 m²</em>",
              "<p>El corazón familiar del recorrido: un ball pit semicircular de 158 m² y una guirnalda que recorre todo el "
              "perímetro de la plaza, con luz blanco cálido y esferas plateadas y rojas de 7 cm.</p>", False)
        + [counters([(158, " m²", "de ball pit semicircular"), (7, " cm", "esferas plateadas y rojas")], False),
           icon_list([("Guirnalda", "en todo el perímetro de la plaza"), ("Iluminación", "blanco cálido")], False),
           sponsor("logo-xiaomi.png", "Xiaomi", False), credit(KARJIM, False)],
        [image("plaza-tukis-render-3", "Plaza Tukis, render en la plaza", False, frame=True),
         gallery(["plaza-tukis-plano", "plaza-tukis-render-1", "plaza-tukis-render-2"], 3, "4:3", 300)]], [44, 52])],
        anchor="tukis"))

    # 12 Plaza Brunos
    out.append(slide([row([
        intro("12 Escazú · Plaza Brunos", "Un árbol <em>de 7 metros</em>",
              "<p>La pieza central de Escazú: un árbol de 7 metros en blanco y rojo sobre una tarima verde oscuro con el logo "
              "de kölbi, rodeado de soldados, regalos, escaleras espejadas, árboles de ambientación, un trineo y bancas "
              "modernas.</p>", True)
        + [counters([(7, " m", "árbol en blanco y rojo"), (30, "", "regalos de 40, 50 y 60 cm"), (16, "", "árboles de 2 a 3 m"), (80, "", "extensiones de micro luces LED")], True, 2),
           sponsor("logo-kolbi", "kölbi", True), credit(KARJIM, True)],
        [image("plaza-brunos-render-1", "Plaza Brunos", True, frame=True),
         icon_list([("Tarima", "estructura de 3,5 m de diámetro, verde oscuro con logo kölbi"),
                    ("Trineo", "2,90 × 1,55 × 1,35 m, blanco con plateado, con logo kölbi"),
                    ("Regalos", "10 de 60 × 60 cm · 10 de 50 × 50 cm · 10 de 40 × 40 cm"),
                    ("Soldados de 1,70 m", "6 de pie y 1 con carretilla de regalos"),
                    ("Soldados de 1,30 m", "4 con regalo en la mano"),
                    ("Pareja de soldados", "con esfera en el brazo, uno sobre los hombros del otro"),
                    ("Escalera espejada", "5 m, con 2 soldados de 1,30 m"), ("Escaleras", "2 de 2 m, cada una con un soldado de 1,30 m"),
                    ("Árboles", "16 de 2 m, 2,50 m y 3 m para ambientación"), ("Luces", "80 extensiones de micro luces LED especiales"),
                    ("Stand", "4,50 × 4,00 m"), ("Bancas", "8 modernas de fibra de vidrio plateadas")], True, delay=350)]], [44, 52])],
        dark=True, anchor="brunos"))

    # 13 Plaza Brunos, en detalle
    out.append(slide(intro("13 Escazú · Plaza Brunos, en detalle", "Soldados, trineo <em>y stand kölbi</em>",
                           "<p>Cada pieza del montaje vista de cerca: el trineo plateado, el stand, los soldados con regalos y las bancas de fibra "
                           "de vidrio, junto a las referencias que inspiran la escena.</p>", False, center=True)
                     + [gallery(["plaza-brunos-render-2", "plaza-brunos-panoramica", "plaza-brunos-stand", "plaza-brunos-soldados",
                                 "plaza-brunos-simulador", "plaza-brunos-arboles", "plaza-brunos-soldados-set", "plaza-brunos-carretilla",
                                 "banca-plateada", "stand-kolbi", "brunos-inspiracion-1", "brunos-inspiracion-2"], 4),
                        credit(KARJIM, False)], center=True, anchor="brunos-detalle"))

    # 14 Quinta Etapa
    out.append(slide([row([
        intro("14 Escazú · Pasillo Quinta Etapa", "Copos de papel <em>sobre el pasillo</em>",
              "<p>Guirnaldas de copos de papel blanco con bordes dorado champán, suspendidas entre cortinas de luz a lo largo "
              "del pasillo. Es la opción 1; la alternativa queda abierta para definirla juntos.</p>", False)
        + [icon_list([("Guirnalda", "5,00 m de largo total"), ("Copos", "80 cm y 50 cm de diámetro, alternados"),
                      ("Unión", "cable de acero de 50 cm entre copos"), ("Acabado", "blanco con bordes dorado champán"),
                      ("Montaje", "gancho y aro metálico, uso interior")], False), credit(KARJIM, False)],
        [image("quinta-etapa-render", "Pasillo Quinta Etapa, render de la opción 1", False, frame=True),
         gallery(["quinta-etapa-estrella", "quinta-etapa-diametro", "quinta-etapa-ficha", "quinta-etapa-ref"], 4, "1:1", 300)]], [44, 52])],
        anchor="quinta"))

    # 15 Plaza Siman
    out.append(slide([row([
        intro("15 Escazú · Plaza Siman", "Carrusel dorado <em>y renos</em>",
              "<p>Un árbol dentro de un carrusel dorado sobre base roja BAC, rodeado de árboles iluminados, renos dorados "
              "facetados y una banca dorada: una escena hecha para fotografiarse.</p>", True)
        + [icon_list(["Carrusel dorado", "Base roja BAC", "Renos dorados facetados", "Árboles iluminados", "Banca moderna dorada"], True, inline=True),
           credit(KARJIM, True)],
        [image("plaza-siman-render-1", "Plaza Siman", True, frame=True)]], [44, 52]),
        gallery(["plaza-siman-render-2", "plaza-siman-render-3", "renos-dorados-1", "renos-dorados-2", "banca-dorada"], 5)],
        dark=True, anchor="siman"))

    # 16 BCR – Vértigo y Plaza Honor
    out.append(slide(intro("16 Escazú · Pasillo BCR – Vértigo y Plaza Honor", "Adornos suspendidos <em>y un tren navideño</em>", "", False) + [row([
        [image("pasillo-bcr-vertigo", "Pasillo BCR – Vértigo", False, frame=True),
         counters([(18, "", "adornos blanco con dorado"), (18, "", "esferas plateadas y doradas")], False)],
        [image("plaza-honor-render", "Plaza Honor", False, frame=True),
         text("<p><strong>Plaza Honor.</strong> El árbol Gift of Joy, en rojo y dorado bajo la cúpula, cierra el recorrido de "
              "Escazú rodeado por un tren navideño. El mismo diseño se repite en Plaza Old Navy de Curridabat.</p>", False, narrow=False, cls="nm-prose"),
         grid([icard("plaza-honor-tren", "Tren navideño", "Pieza", False)], 2),
         credit(KARJIM, False)]], [48, 48])], anchor="honor"))
    return out


def parte2():
    out = []
    out.append(portadilla("curridabat", "Parte II · Multiplaza Curridabat", "Curridabat: <em>la misma magia, otro escenario</em>",
                          "<p>Curridabat sigue el mismo recorrido en tres capas y retoma lo mejor de Escazú: Plaza Cinemark y Plaza Kolbi "
                          "repiten sus diseños y Plaza Old Navy espeja Plaza Honor. A ellas se suman Plaza Santo Katrin, el Pasillo "
                          "Equiz – Vértigo y Plaza Reebok.</p>",
                          [("fas fa-door-open", "Entradas", "La entrada de H&amp;M y la entrada techada, animadas con luz."),
                           ("fas fa-building", "Fachadas", "Cuatro animaciones: fachada principal, lateral y los frentes de Zara, Bershka, Pull&amp;Bear y Stradivarius."),
                           ("fas fa-tree", "Decoración interna", "Vacíos y food court, Santo Katrin, Equiz – Vértigo, Reebok y las tres plazas espejo.")],
                          "fachada-curri-principal.mp4"))

    out.append(slide(intro("17 Curridabat · Entradas", "Las entradas <em>reciben con luz</em>",
                           "<p>La entrada de H&amp;M y la entrada techada se animan con la misma luz de las fachadas, para que la Navidad "
                           "reciba al visitante desde el primer paso.</p>", True, center=True)
                     + [grid([vcard("fachada-curri-hm.mp4", "Entrada H&amp;M · Curridabat · animación de luz", True, "169"),
                              vcard("fachada-curri-entrada.mp4", "Entrada techada · Curridabat · animación de luz", True, "169")], 2, 16),
                        credit(MECA, True)], dark=True, center=True, anchor="entradas-curridabat"))

    out.append(slide(intro("18 Curridabat · Fachadas", "La misma luz, <em>en Curridabat</em>",
                           "<p>La estrategia de luz cruza la ciudad: la fachada principal, la lateral y los frentes de Zara, Bershka, "
                           "Pull&amp;Bear y Stradivarius se encienden con animaciones sobre la fotografía real del edificio.</p>", True, center=True)
                     + [grid([vcard("fachada-curri-principal.mp4", "Fachada principal · Curridabat · animación de luz", True, "169"),
                              vcard("fachada-curri-lateral.mp4", "Fachada lateral · Curridabat · animación de luz", True, "169"),
                              vcard("fachada-curri-zara-esquina.mp4", "Esquina Zara · Curridabat · animación de luz", True, "169"),
                              vcard("fachada-curri-zara.mp4", "Zara · Bershka · Pull&amp;Bear · Stradivarius · Curridabat · animación de luz", True, "169")], 2, 16),
                        credit(MECA, True)], dark=True, center=True, anchor="fachadas-curridabat"))

    out.append(capitulo("Parte II · Decoración interna", "Adentro, <em>Curridabat refleja Escazú</em>",
                        "<p>Siete zonas interiores: cortinas de luz en vacíos, pasillos y food court, un área de juego de 4 × 22 m, un cielo "
                        "de cables de luz, árboles de espejo y tres plazas que retoman los diseños de Escazú.</p>",
                        [("plaza-cinemark-render", "Plaza Cinemark", "Retoma Plaza Siman: árbol con carrusel BAC, renos dorados y banca dorada."),
                         ("plaza-brunos-arboles", "Plaza Kolbi", "Retoma el montaje de Escazú con árboles de base espejada y logo kölbi."),
                         ("plaza-honor-render", "Plaza Old Navy", "Repite Plaza Honor: árbol Gift of Joy bajo la cúpula y tren navideño.")],
                        "santo-katrin-render"))

    out.append(slide(intro("19 Curridabat · Vacíos", "Luz sobre pasillos <em>y food court</em>",
                           "<p>Cortinas de luz en tragaluces, pasillos y food court, en dos versiones: cortina sola o con esferas "
                           "colgantes. Deslice sobre cada imagen para compararlas.</p>", False, center=True)
                     + [compare(["vacio-curri-koaj-a", "vacio-curri-foodcourt-a"], 2),
                        compare(["vacio-curri-pasillo-a", "vacio-curri-universal-a", "vacio-curri-naturalizer-a"], 3, 300),
                        gallery(["vacio-curri-estrellas", "vacio-curri-pasillo-largo"], 2, "3:2", 350),
                        credit(MECA, False)], center=True, anchor="vacios-curridabat"))

    out.append(slide([row([
        intro("20 Curridabat · Plaza Santo Katrin", "Área de juego <em>de 4 × 22 m</em>",
              "<p>Un área de juego lineal de 4 × 22 m con ball pit, toboganes y casitas en rojo y blanco, bajo un cielo de "
              "esferas rojas y plateadas.</p>", False)
        + [counters([(4, " m", "de ancho"), (22, " m", "de largo")], False), credit(KARJIM, False)],
        [image("santo-katrin-render", "Plaza Santo Katrin", False, frame=True),
         gallery(["santo-katrin-plano-1", "santo-katrin-plano-2"], 2, "16:9", 300)]], [44, 52])], anchor="katrin"))

    out.append(slide([row([
        intro("21 Curridabat · Pasillo Equiz – Vértigo", "Un cielo <em>de cables de luz</em>",
              "<p>Diecinueve cables de luz cruzan el pasillo de lado a lado, con dos opciones de adorno colgante: cascabeles "
              "dorados o esferas rojas y blancas. Deslice sobre la imagen para comparar.</p>", True)
        + [counters([(19, "", "cables de lado a lado"), (1, "", "cable central de tres fachadas")], True),
           icon_list([("Cuadrícula", "de cables frente a Koaj")], True), credit(KARJIM, True)],
        [compare(["equiz-vertigo-cascabeles"], 1)]], [44, 52])], dark=True, anchor="equiz"))

    out.append(slide([row([
        [image("plaza-reebok-render", "Plaza Reebok", False, frame=True)],
        intro("22 Curridabat · Plaza Reebok", "Árboles <em>de espejo</em>",
              "<p>Árboles de espejo sobre una estructura de borde cuadrado, con la base rellena de esferas de 20 cm y bancas "
              "modernas: reflejos que multiplican la luz de la plaza.</p>", False)
        + [icon_list(["Árboles de espejo", "Estructura de borde cuadrado", "4 bancas modernas", "Esferas de 20 cm en la base"], False, inline=True),
           grid([icard("plaza-reebok-detalle", "Árboles facetados", "Detalle", False)], 2),
           text("<p class=\"nm-note\">El montaje requiere montacargas.</p>", False, narrow=False, delay=350), credit(KARJIM, False)]], [52, 44])],
        anchor="reebok"))

    out.append(slide(intro("23 En cifras", "La propuesta, <em>en números</em>", "", True, center=True)
                     + [counters([(158, " m²", "de ball pit en Plaza Tukis"), (7, " m", "de altura del árbol de Plaza Brunos"),
                                  (80, "", "extensiones de micro luces LED"), (30, "", "regalos de 40 a 60 cm"),
                                  (19, "", "cables de luz en el Pasillo Equiz – Vértigo"), (17, "", "animaciones de luz en fachadas y entradas")],
                                 True, 3)],
                     dark=True, center=True, bg_image="plaza-honor-render", anchor="cifras"))

    out.append(slide(intro("24 Siguiente paso", "This Christmas every moment <em>can be magical</em>",
                           "<p>Quedan por definir las opciones de cada zona: cortina sola o con esferas en los vacíos, cascabeles o esferas "
                           "en el Pasillo Equiz – Vértigo y la alternativa de copos del Pasillo Quinta Etapa. Conversemos los "
                           "siguientes pasos para encender la Navidad 2026.</p>", True, center=True)
                     + [form(),
                        widget("text-editor", {"editor": '<p>¿Prefieres el correo? <a href="' + MAIL + '">contacto@lindsaymeneses.com</a></p>',
                                               "align": "center", "_css_classes": "nm-note",
                                               "__globals__": {"text_color": C + "oroclaro", "typography_typography": T + "text"}}),
                        buttons([("Volver al inicio", "#inicio", True)], "center")],
                     dark=True, center=True, bg_image="kv-where-the-magic-begins", overlay="rgba(7,24,18,0.7)", anchor="contacto"))

    # pie
    def h(t, al, typo, color, fs=None):
        s = {"title": t, "header_size": "p", "align": al, "_css_classes": "nm-t" + (" nm-r" if al == "right" else ""),
             "__globals__": {"title_color": C + color, "typography_typography": T + typo}}
        if fs:
            s.update(sizes(fs))
        return widget("heading", s)
    cols = [[h("Multiplaza", "left", "primary", "blanco", 30), h("Grupo Roble", "left", "accent", "accent")],
            [h("Navidad 2026 · Escazú y Curridabat", "center", "secondary", "oroclaro", 20)],
            [h("Contacto", "right", "accent", "accent"),
             widget("text-editor", {"editor": '<p><a href="' + MAIL + '" style="color:inherit">contacto@lindsaymeneses.com</a></p>',
                                    "align": "right", "_css_classes": "nm-r",
                                    "__globals__": {"text_color": C + "oroclaro", "typography_typography": T + "text"}})]]
    foot = container([
        container([container(c, {"width": px(32, "%"), "width_mobile": px(100, "%"), "flex_justify_content": "center", "gap": gap(6)}) for c in cols],
                  {"flex_direction": "row", "flex_wrap": "wrap", "flex_direction_mobile": "column", "gap": gap(24), "flex_align_items": "center"}),
        widget("divider", {"width": px(72), "weight": px(1), "align": "left", "_css_classes": "nm-line", "__globals__": {"color": C + "accent"}}),
        widget("text-editor", {"editor": '<p class="nm-note">Iluminación de fachadas, entradas y vacíos: La Meca Concept · Ambientación y decoración interior: Karjim Design · Renders y fotografías de los proveedores · Multiplaza · Grupo Roble · Navidad 2026.</p>',
                               "align": "center", "_css_classes": "nm-note", "__globals__": {"text_color": C + "salvia", "typography_typography": T + "text"}}),
        widget("text-editor", {"editor": '<p><a href="/proyectos/">← Lindsay Meneses · Proyectos</a></p>', "align": "center", "_css_classes": "nm-note",
                               "__globals__": {"text_color": C + "oroclaro", "typography_typography": T + "text"}}),
    ], {"content_width": "boxed", "boxed_width": px(1200), "flex_direction": "column", "padding": pad(64, 56, 40, 56),
        "padding_mobile": pad(48, 22, 110, 22), "gap": gap(28), "background_background": "classic",
        "__globals__": {"background_color": C + "noche"}, "css_classes": "nm-footer"}, inner=False)
    out.append(foot)
    return out


# ------------------------------------------------------------------ plantilla de código (162)
def codigo():
    """Barra del sitio + CSS + JS recortados de la v4 (fx/v6-codigo.css y fx/v6-codigo.js) en un widget HTML."""
    css = (HERE / "fx/v6-codigo.css").read_text(encoding="utf-8")
    js = (HERE / "fx/v6-codigo.js").read_text(encoding="utf-8")
    html = shell_markup() + "<style>" + css + "</style><script>" + js + "</script>"
    return [container([widget("html", {"html": html, "_css_classes": "lx-shell-w"})], {"css_classes": "lx-shell-w"}, inner=False)]


def template_widget(tid):
    return widget("template", {"template_id": str(tid)})


def build(revslider=False):
    """La Parte I se reparte: portadilla, entradas, fachadas y capítulo en la página; las zonas 07–16 en la plantilla 169."""
    p1 = parte1()
    corte = next(i for i, c in enumerate(p1) if c["settings"].get("_element_id") == "vacios-escazu")
    tpl = lambda tid: container([template_widget(tid)], {"gap": gap(0)}, inner=False)
    pagina = ([container([template_widget(TPL_CODIGO)], {"css_classes": "lx-shell-w"}, inner=False), tpl(TPL_PORTADA)]
              + comun() + p1[:corte] + [tpl(TPL_ZONAS), tpl(TPL_PARTE2)])
    return {"page-elementor-data.json": pagina, "tpl-codigo.json": codigo(), "tpl-portada.json": portada(revslider),
            "tpl-zonas.json": p1[corte:], "tpl-parte2.json": parte2()}


if __name__ == "__main__":
    docs = build("--revslider" in sys.argv)
    for name, doc in docs.items():
        data = json.dumps(doc, ensure_ascii=False, separators=(",", ":")).replace(" ", " ")
        (HERE / name).write_text(data, encoding="utf-8")
        print("ok", name, len(data), "bytes; escapado", len(json.dumps(data, ensure_ascii=False)))
