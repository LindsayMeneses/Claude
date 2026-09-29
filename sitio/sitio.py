"""lindsaymeneses.com — genera las páginas Elementor del sitio (inicio y hub de proyectos) con la carcasa común.

Uso:  python3 sitio.py  ->  out/inicio.json, out/proyectos.json   (meta _elementor_data de cada página)
      from sitio import shell_html                                  (lo usa la página de Navidad Multiplaza)
Estructura con contenedores y widgets nativos de Elementor (títulos, textos, botones, contadores, lista de iconos);
un widget HTML lleva la carcasa (barra + menú + motor de scroll: shell.css / shell.js) y las fotos animadas.
Datos: FUENTES.md.  IDs de páginas: IDS (se completan al crearlas en WordPress).
"""
import html as H
import json
import re
from pathlib import Path

HERE = Path(__file__).parent
C = "globals/colors?id="
T = "globals/typography?id="
UP = "https://lindsaymeneses.com/wp-content/uploads/2026/09/"
MAIL = "mailto:contacto@lindsaymeneses.com?subject=Contacto%20desde%20lindsaymeneses.com"
LINKEDIN = "https://www.linkedin.com/in/lindsay-meneses-cambronero-3b424420/"
IDS = json.loads((HERE / "ids.json").read_text()) if (HERE / "ids.json").exists() else {"inicio": 0, "proyectos": 0}

FOTOS = {
    "rojo": [(768, "nm-rojo-dorado-768x432.jpg"), (1536, "nm-rojo-dorado-1536x864.jpg"), (2048, "nm-rojo-dorado-2048x1152.jpg")],
    "cascabeles": [(768, "nm-c03-768x539.jpg"), (1536, "nm-c03-1536x1077.jpg"), (2048, "nm-c03-2048x1436.jpg")],
    "luces": [(768, "nm-c13-768x513.jpg"), (1536, "nm-c13-1536x1026.jpg"), (1920, "nm-c13.jpg")],
    "esferas": [(768, "nm-esferas-navidad-768x512.jpg"), (1536, "nm-esferas-navidad-1536x1024.jpg"), (2048, "nm-esferas-navidad-2048x1365.jpg")],
    "pino": [(768, "nm-c05-768x512.jpg"), (1536, "nm-c05-1536x1024.jpg"), (2048, "nm-c05-2048x1365.jpg")],
    "chispa": [(768, "nm-c01-768x512.jpg"), (1536, "nm-c01-1536x1024.jpg"), (2048, "nm-c01-2048x1365.jpg")],
    "estrella": [(769, "nm-estrella-769x1024.jpg"), (1153, "nm-estrella-1153x1536.jpg")],
    "copo": [(768, "nm-c06-768x509.jpg"), (1536, "nm-c06-1536x1017.jpg"), (2048, "nm-c06-2048x1356.jpg")],
}

# Proyectos (cada evento). «url» = tiene landing propia (página hija de «Proyectos»).
PROYECTOS = [
    {"titulo": "Navidad Multiplaza <em>2026</em>", "meta": "2026 · Propuesta · Escazú y Curridabat", "foto": "rojo",
     "texto": "Decoración navideña zona por zona: túnel de luz, árbol de 7 metros, ball pit de 158 m² y un cielo de cables de luz.",
     "url": "/proyectos/navidad-multiplaza-2026/"},
    {"titulo": "El Regalo de <em>Dar</em>", "meta": "2024 · Alianza con BAC", "foto": "cascabeles",
     "texto": "Campaña con BAC a beneficio de Fundación Génesis, con la meta de reunir 500 regalos para niños."},
    {"titulo": "Dragones y <em>dinosaurios</em>", "meta": "2024 · Día de la Niñez", "foto": None,
     "texto": "Del 7 de setiembre al 6 de octubre: más de ocho dragones animatrónicos de más de 4 metros."},
    {"titulo": "Christmas Around <em>the World</em>", "meta": "2022 · Navidad", "foto": "esferas",
     "texto": "Decoraciones inspiradas en el mundo, pista de patinaje, desfiles, arte y emprendimientos."},
    {"titulo": "Elf <em>Christmas</em>", "meta": "2021 · Navidad en vivo", "foto": "estrella",
     "texto": "Inauguración de la Navidad transmitida en vivo en las redes de Multiplaza."},
]

_seq = iter(range(1, 10**6))


def uid():
    return f"s{next(_seq):06x}"


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
    return widget("html", {"html": markup, **({"_css_classes": cls} if cls else {})})


def compact_css(path):
    css = re.sub(r"/\*.*?\*/", "", path.read_text(), flags=re.S)
    return re.sub(r"\s*\n\s*", "", css)


def compact_js(path):
    return "\n".join(l.strip() for l in path.read_text().splitlines() if l.strip() and not l.strip().startswith(("//", "/*")))


def shell_markup():
    """Carcasa: estilos + motor + configuración del menú (hub y proyectos de respaldo)."""
    fb = [{"title": re.sub("<.*?>", "", p["titulo"]), "link": p["url"], "meta": p["meta"]} for p in PROYECTOS if p.get("url")]
    cfg = H.escape(json.dumps(fb, ensure_ascii=False), quote=True)
    return (f'<div class="lx-shell" data-home="/" data-hub="{IDS["proyectos"]}" data-hub-url="/proyectos/" data-projects="{cfg}"></div>'
            f'<style>{compact_css(HERE / "shell.css")}</style><script>{compact_js(HERE / "shell.js")}</script>')


def shell_html():
    return html(shell_markup(), "lx-shell-w")


def img(key, alt, sizes="100vw", eager=False):
    f = FOTOS[key]
    srcset = ", ".join(f"{UP}{n} {w}w" for w, n in f)
    return (f'<img src="{UP}{f[min(1, len(f) - 1)][1]}" srcset="{srcset}" sizes="{sizes}" alt="{H.escape(alt)}" '
            + ('fetchpriority="high">' if eager else 'loading="lazy" decoding="async">'))


def k(text, color="accent", align="left"):
    return widget("heading", {"title": text, "header_size": "p", "align": align, "_css_classes": "lx-k",
                              "__globals__": {"title_color": C + color, "typography_typography": T + "accent"}})


def h(text, size="h2", color="blanco", align="left", fs=None, cls="lx-t", typo="primary"):
    s = {"title": text, "header_size": size, "align": align, "_css_classes": cls,
         "__globals__": {"title_color": C + color, "typography_typography": T + typo}}
    if fs:
        s.update({"typography_font_size": px(fs), "typography_font_size_tablet": px(round(fs * .78)),
                  "typography_font_size_mobile": px(max(round(fs * .52), 22))})
    return widget("heading", s)


def t(markup, color="oroclaro", align="left", maxw=None, cls=""):
    s = {"editor": markup, "align": align, "__globals__": {"text_color": C + color, "typography_typography": T + "text"}}
    if cls:
        s["_css_classes"] = cls
    if maxw:
        s.update({"_element_width": "initial", "_element_custom_width": px(maxw), "_element_custom_width_mobile": px(100, "%")})
    return widget("text-editor", s)


def btn(label, url, ghost=False, on_dark=True, align="left"):
    s = {"text": label, "link": {"url": url, "is_external": url.startswith("http"), "nofollow": False}, "align": align,
         "size": "md", "_element_width": "auto", "_element_width_mobile": "inherit", "align_mobile": "justify", "_css_classes": "lx-btn",
         "border_border": "solid", "border_width": {"unit": "px", "top": 1, "right": 1, "bottom": 1, "left": 1, "isLinked": True},
         "border_radius": {"unit": "px", "top": 0, "right": 0, "bottom": 0, "left": 0, "isLinked": True},
         "text_padding": pad(20, 34), "__globals__": {"typography_typography": T + "accent"}}
    if ghost:
        s["background_color"] = "transparent"
        s["__globals__"].update({"button_text_color": C + ("blanco" if on_dark else "primary"),
                                 "border_color": C + ("oroclaro" if on_dark else "primary"),
                                 "button_background_hover_color": C + "accent", "hover_color": C + "noche",
                                 "button_hover_border_color": C + "accent"})
    else:
        s["__globals__"].update({"background_color": C + "accent", "button_text_color": C + "noche", "border_color": C + "accent",
                                 "button_background_hover_color": C + "oroclaro", "hover_color": C + "noche",
                                 "button_hover_border_color": C + "oroclaro"})
    return widget("button", s)


def btns(items, align="flex-start"):
    return container(items, {"flex_direction": "row", "flex_direction_mobile": "column", "flex_wrap": "wrap", "gap": gap(14),
                             "flex_align_items": "center", "flex_align_items_mobile": "stretch", "flex_justify_content": align})


def row(children, g=48, align="flex-start", wrap=False, tablet="column", cls=""):
    s = {"flex_direction": "row", "flex_wrap": "wrap" if wrap else "nowrap", "flex_direction_mobile": "column",
         "flex_direction_tablet": tablet, "gap": gap(g), "flex_align_items": align}
    if cls:
        s["css_classes"] = cls
    return container(children, s)


def col(children, w, g=20, tablet=100, cls="", justify="flex-start"):
    s = {"width": px(w, "%"), "width_tablet": px(tablet, "%"), "width_mobile": px(100, "%"), "gap": gap(g), "flex_justify_content": justify}
    if cls:
        s["css_classes"] = cls
    return container(children, s)


def section(children, bg, eid=None, extra=None, cls=""):
    s = {"content_width": "boxed", "boxed_width": px(1240), "flex_direction": "column", "gap": gap(28),
         "padding": pad(150, 56), "padding_tablet": pad(110, 40), "padding_mobile": pad(90, 22),
         "background_background": "classic", "__globals__": {"background_color": C + bg}, "css_classes": ("lx-sec " + cls).strip()}
    if eid:
        s["_element_id"] = eid
    s.update(extra or {})
    return container(children, s, inner=False)


def pin(children, cls, height_vh, eid=None, sticky_extra=None):
    """Sección fijada: contenedor alto (height_vh) con un hijo pegajoso de una pantalla."""
    st = {"flex_justify_content": "center", "flex_align_items": "center", "css_classes": "lx-stick", "padding": pad(0, 56),
          "padding_mobile": pad(0, 22)}
    st.update(sticky_extra or {})
    s = {"css_classes": f"lx-pin {cls}", "min_height": px(height_vh, "vh"), "min_height_mobile": px(max(height_vh - 60, 100), "vh"),
         "background_background": "classic", "__globals__": {"background_color": C + "noche"}}
    if eid:
        s["_element_id"] = eid
    return container([container(children, st)], s, inner=False)


def card(p, w="36vw"):
    foto = (f'<div class="lx-ph">{img(p["foto"], re.sub("<.*?>", "", p["titulo"]), "(max-width:767px) 84vw, 36vw")}</div>'
            if p.get("foto") else f'<div class="lx-ph lx-num"><span>{p["meta"][:4]}</span></div>')
    kids = [html(foto), container([k(p["meta"]), h(p["titulo"], "h3", "blanco", fs=34), t(f"<p>{p['texto']}</p>")]
                                  + ([btns([btn("Ver proyecto", p["url"])])] if p.get("url") else
                                     [k("Caso en preparación", "salvia")]),
                                  {"gap": gap(12), "padding": pad(28, 30, 32)})]
    return container(kids, {"width": {"unit": "vw", "size": 36}, "width_tablet": {"unit": "vw", "size": 60}, "width_mobile": {"unit": "vw", "size": 84},
                            "gap": gap(0), "css_classes": "lx-card" + ("" if p.get("url") else " lx-soon")})


# ---------------------------------------------------------------- Inicio
def inicio():
    hero = pin([
        shell_html(),
        html(f'{img("luces", "Árbol envuelto en luces cálidas", eager=True)}', "lx-bg"),
        container([
            k("Mercadeo · Publicidad · Experiencias de marca", "oroclaro", "center"),
            h("Lindsay <em>Meneses</em>", "h1", "blanco", "center", fs=150),
        ], {"gap": gap(22), "css_classes": "lx-name", "flex_align_items": "center"}),
        h("Diez años creando temporadas que la gente <em>recuerda</em>.", "h2", "blanco", "center", fs=64, cls="lx-t lx-after"),
        h("Desliza", "p", "oroclaro", "center", cls="lx-k lx-hint", typo="accent"),
    ], "lx-hero", 260, eid="inicio")

    perfil = section([
        k("Perfil", "accent"),
        h("Jefa de Mercadeo y Publicidad en Grupo Roble. Más de diez años llevando la estrategia a la vida real: "
          "eventos, temporadas y campañas para Multiplaza Escazú y Multiplaza Curridabat.", "p", "blanco", fs=54,
          cls="lx-t lx-words"),
    ], "noche", "perfil", extra={"padding": pad(170, 56, 150)})

    datos = [("Rol actual", "Jefa de Mercadeo y Publicidad", "Grupo Roble · Multiplaza Escazú y Multiplaza Curridabat."),
             ("Formación", "Máster en Marketing, Marketing Digital y Redes Sociales",
              "IM Digital Business School. Administración de Empresas en la Universidad Hispanoamericana."),
             ("Especialidades", "Eventos, campañas y alianzas",
              "Temporadas y activaciones, campañas comerciales, alianzas con marcas y causas, clientes, presupuestos y tráfico."),
             ("Base", "San José, Costa Rica", "Proyectos para centros comerciales y marcas en la región.")]
    formacion = section([
        row([
            col([k("Trayectoria profesional", "secondary"), h("Estrategia que se <em>vive</em> en persona", "h2", "primary", fs=58)],
                38, cls="lx-sticky"),
            col([container([k(a, "secondary"), h(b, "h3", "primary", fs=30), t(f"<p>{c}</p>", "text", maxw=560)],
                           {"gap": gap(10), "css_classes": "lx-fact"}) for a, b, c in datos], 56, g=44),
        ], g=80),
    ], "marfil", extra={"padding": pad(150, 56)})

    def cnt(n, title, prefix=""):
        return widget("counter", {"starting_number": 0, "ending_number": n, "prefix": prefix, "duration": 2400,
                                  "thousand_separator": "", "title": title, "_css_classes": "lx-counter",
                                  "__globals__": {"number_color": C + "accent", "title_color": C + "oroclaro",
                                                  "typography_title_typography": T + "text"}})
    cifras = section([row([col([cnt(10, "años en mercadeo y publicidad", "+")], 31, tablet=31),
                           col([cnt(2, "centros comerciales Multiplaza en Costa Rica")], 31, tablet=31),
                           col([cnt(5, "temporadas y campañas destacadas")], 31, tablet=31)], g=40, tablet="row")],
                     "noche", extra={"padding": pad(110, 56), "padding_mobile": pad(80, 22)})

    proyectos = pin([
        container([k("Proyectos", "accent"), h("Cada evento, <em>una historia</em>.", "h2", "blanco", fs=72)],
                  {"gap": gap(16), "padding": pad(0, 0, 36, 0)}),
        container([card(p) for p in PROYECTOS],
                  {"flex_direction": "row", "flex_wrap": "nowrap", "gap": gap(28), "css_classes": "lx-track",
                   "flex_align_items": "stretch"}),
    ], "lx-hpin", 100, eid="proyectos", sticky_extra={"flex_align_items": "flex-start", "flex_justify_content": "center", "padding": pad(90, 0, 30, 56),
                                                       "padding_mobile": pad(90, 0, 60, 22)})

    tray = section([
        row([
            col([k("Trayectoria", "secondary"), h("Temporadas que marcaron el <em>calendario</em>", "h2", "primary", fs=52)], 38,
                cls="lx-sticky"),
            col([widget("icon-list", {"icon_list": [{"_id": uid(), "text": x, "selected_icon": {"value": "fas fa-circle", "library": "fa-solid"}}
                                                    for x in ["2021 · «Elf Christmas»: inauguración de la Navidad en vivo",
                                                              "2022 · «Christmas Around the World»",
                                                              "2024 · Día de las Madres",
                                                              "2024 · Día de la Niñez con dragones y dinosaurios",
                                                              "2024 · Black Friday: horario extendido, descuentos y premios",
                                                              "2024 · «El Regalo de Dar» con BAC y Fundación Génesis",
                                                              "2026 · Propuesta Navidad Multiplaza"]],
                                      "icon_size": px(7), "_css_classes": "lx-tl",
                                      "__globals__": {"icon_color": C + "accent", "text_color": C + "text",
                                                      "icon_typography_typography": T + "text"}})], 56),
        ], g=80),
    ], "marfil", "trayectoria")

    contacto = section([
        k("Contacto", "oroclaro", "center"),
        h("Conversemos.", "h2", "blanco", "center", fs=120),
        t("<p>Eventos, campañas y experiencias de marca para que la gente llegue, se quede y vuelva.</p>", "oroclaro", "center", maxw=520),
        btns([btn("Escríbeme", MAIL), btn("LinkedIn", LINKEDIN, ghost=True)], "center"),
    ], "noche", "contacto", extra={
        "flex_align_items": "center", "min_height": px(100, "vh"), "flex_justify_content": "center",
        "background_image": {"url": UP + "nm-c01-scaled.jpg", "id": 19, "source": "library"}, "background_position": "center center",
        "background_size": "cover", "background_overlay_background": "classic", "background_overlay_color": "#071812",
        "background_overlay_opacity": {"unit": "px", "size": .8}})
    return [hero, perfil, formacion, cifras, proyectos, tray, contacto, pie()]


def pie():
    return container([
        row([h("Lindsay <em>Meneses</em>", "p", "blanco", fs=26, cls="lx-t"),
             t('<p>Mercadeo y publicidad · San José, Costa Rica · <a href="' + MAIL + '" style="color:inherit">contacto@lindsaymeneses.com</a></p>',
               "salvia")], g=24, align="center"),
    ], {"content_width": "boxed", "boxed_width": px(1240), "padding": pad(44, 56), "padding_mobile": pad(40, 22),
        "background_background": "classic", "__globals__": {"background_color": C + "noche"}, "css_classes": "lx-foot"}, inner=False)


# ---------------------------------------------------------------- Hub de proyectos
def hub():
    hero = pin([
        shell_html(),
        html(f'{img("estrella", "Estrella dorada", eager=True)}', "lx-bg"),
        container([k("Proyectos", "oroclaro", "center"), h("Cada evento, <em>una historia</em>.", "h1", "blanco", "center", fs=120)],
                  {"gap": gap(22), "css_classes": "lx-name", "flex_align_items": "center"}),
        h("Temporadas, campañas y experiencias de marca para Multiplaza Costa Rica.", "h2", "blanco", "center", fs=46,
          cls="lx-t lx-after"),
        h("Desliza", "p", "oroclaro", "center", cls="lx-k lx-hint", typo="accent"),
    ], "lx-hero", 220)
    filas = []
    for i, p in enumerate(PROYECTOS):
        foto = (html(f'<div class="lx-ph" style="--h:64vh">{img(p["foto"], re.sub("<.*?>", "", p["titulo"]), "(max-width:767px) 100vw, 55vw")}</div>')
                if p.get("foto") else html(f'<div class="lx-ph lx-num" style="--h:64vh"><span>{p["meta"][:4]}</span></div>'))
        texto = [k(p["meta"], "accent"), h(p["titulo"], "h2", "blanco", fs=60), t(f"<p>{p['texto']}</p>", maxw=440)]
        texto.append(btns([btn("Ver proyecto", p["url"])]) if p.get("url") else k("Caso en preparación", "salvia"))
        fc, tc = col([container([foto], {"css_classes": "lx-card"})], 56), col(texto, 38, g=18, justify="center")
        filas.append(row([fc, tc] if i % 2 == 0 else [tc, fc], g=72, align="center"))
    lista = section(filas, "noche", extra={"gap": gap(140), "padding": pad(140, 56)})
    return [hero, lista, pie()]


if __name__ == "__main__":
    out = HERE / "out"
    out.mkdir(exist_ok=True)
    for name, fn in (("inicio", inicio), ("proyectos", hub)):
        data = json.dumps(fn(), ensure_ascii=False, separators=(",", ":"))
        (out / f"{name}.json").write_text(data, encoding="utf-8")
        print("ok", name, len(data), "bytes")
