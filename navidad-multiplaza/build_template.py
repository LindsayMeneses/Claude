"""Genera la plantilla Elementor (JSON importable) de la página Navidad Multiplaza 2026.

Uso:  python3 build_template.py  ->  escribe navidad-multiplaza-elementor.json
Los textos marcados con «[PPT]» se reemplazan con el contenido real del deck.
"""
import json
import secrets

C = "globals/colors?id="
T = "globals/typography?id="


def uid():
    return secrets.token_hex(4)[:7]


def container(children, settings=None, inner=False):
    s = {"content_width": "boxed", "flex_direction": "column", "boxed_width": {"unit": "px", "size": 1200}}
    s.update(settings or {})
    return {"id": uid(), "elType": "container", "isInner": inner, "settings": s, "elements": children}


def widget(kind, settings):
    return {"id": uid(), "elType": "widget", "widgetType": kind, "isInner": False, "settings": settings, "elements": []}


def eyebrow(text, color="accent", align="left"):
    return widget("heading", {
        "title": text, "header_size": "p", "align": align,
        "typography_text_transform": "uppercase",
        "typography_letter_spacing": {"unit": "em", "size": 0.25},
        "__globals__": {"title_color": C + color, "typography_typography": T + "accent"},
    })


def heading(text, size="h2", color="primary", align="left", px=None):
    s = {"title": text, "header_size": size, "align": align,
         "__globals__": {"title_color": C + color, "typography_typography": T + "primary"}}
    if px:
        s["typography_font_size"] = {"unit": "px", "size": px}
        s["typography_font_size_tablet"] = {"unit": "px", "size": round(px * 0.75)}
        s["typography_font_size_mobile"] = {"unit": "px", "size": round(px * 0.55)}
    return widget("heading", s)


def text(html, color="text", align="left"):
    return widget("text-editor", {"editor": html, "align": align,
                                  "__globals__": {"text_color": C + color, "typography_typography": T + "text"}})


def button(label, url, bg="accent", fg="noche", outline=False):
    s = {"text": label, "link": {"url": url}, "size": "md",
         "border_radius": {"unit": "px", "top": 999, "right": 999, "bottom": 999, "left": 999, "isLinked": True},
         "text_padding": {"unit": "px", "top": 16, "right": 34, "bottom": 16, "left": 34, "isLinked": False},
         "hover_animation": "grow",
         "__globals__": {"typography_typography": T + "accent"}}
    if outline:
        s.update({"background_color": "transparent", "border_border": "solid",
                  "border_width": {"unit": "px", "top": 1, "right": 1, "bottom": 1, "left": 1, "isLinked": True}})
        s["__globals__"].update({"button_text_color": C + fg, "border_color": C + fg,
                                 "button_background_hover_color": C + fg, "hover_color": C + "noche"})
    else:
        s["__globals__"].update({"background_color": C + bg, "button_text_color": C + fg,
                                 "button_background_hover_color": C + "oroclaro"})
    return widget("button", s)


def divider(color="accent", width=64):
    return widget("divider", {"width": {"unit": "px", "size": width}, "weight": {"unit": "px", "size": 2},
                              "__globals__": {"color": C + color}})


def image(label):
    # Imagen provisional hasta subir las del PPT a la biblioteca de medios.
    return widget("image", {"image": {"url": "", "id": ""}, "image_size": "large",
                            "_title": label,
                            "image_border_radius": {"unit": "px", "top": 18, "right": 18, "bottom": 18, "left": 18, "isLinked": True}})


def section(children, bg, pad=120, extra=None):
    s = {"padding": {"unit": "px", "top": pad, "right": 24, "bottom": pad, "left": 24, "isLinked": False},
         "padding_mobile": {"unit": "px", "top": round(pad * 0.6), "right": 16, "bottom": round(pad * 0.6), "left": 16, "isLinked": False},
         "gap": {"unit": "px", "size": 24, "column": "24", "row": "24"},
         "background_background": "classic",
         "__globals__": {"background_color": C + bg}}
    s.update(extra or {})
    return container(children, s)


def row(children, gap=32, wrap=True):
    return container(children, {"flex_direction": "row", "flex_wrap": "wrap" if wrap else "nowrap",
                                "flex_direction_mobile": "column",
                                "gap": {"unit": "px", "size": gap, "column": str(gap), "row": str(gap)},
                                "content_width": "full", "padding": {"unit": "px", "top": 0, "right": 0, "bottom": 0, "left": 0, "isLinked": True}},
                     inner=True)


def card(children, bg="blanco", basis=30, anim="fadeInUp", delay=0):
    return container(children, {
        "content_width": "full", "width": {"unit": "%", "size": basis}, "width_mobile": {"unit": "%", "size": 100},
        "flex_grow": 1,
        "padding": {"unit": "px", "top": 36, "right": 32, "bottom": 36, "left": 32, "isLinked": False},
        "border_radius": {"unit": "px", "top": 20, "right": 20, "bottom": 20, "left": 20, "isLinked": True},
        "background_background": "classic", "__globals__": {"background_color": C + bg},
        "box_shadow_box_shadow_type": "yes",
        "box_shadow_box_shadow": {"horizontal": 0, "vertical": 18, "blur": 40, "spread": -18, "color": "rgba(10,36,28,0.25)"},
        "_animation": anim, "animation_delay": delay,
    }, inner=True)


# 1 · Portada
hero = section([
    eyebrow("Multiplaza · Navidad 2026", "accent", "center"),
    heading("La Navidad que <em>se vive</em> en Multiplaza", "h1", "blanco", "center", px=84),
    text("<p>[PPT] Una temporada diseñada para reunir, sorprender y emocionar: experiencias, "
         "decoración y momentos que convierten cada visita en un recuerdo.</p>", "oroclaro", "center"),
    row([button("Ver la propuesta", "#concepto"), button("Calendario", "#calendario", fg="blanco", outline=True)], gap=16),
], "noche", pad=180, extra={
    "min_height": {"unit": "vh", "size": 100}, "flex_justify_content": "center", "flex_align_items": "center",
    "background_background": "gradient", "background_color": "#0A241C", "background_color_b": "#0F3B2E",
    "background_gradient_type": "radial", "background_gradient_position": "top center",
    "background_color_stop": {"unit": "%", "size": 10}, "background_color_b_stop": {"unit": "%", "size": 95},
    "__globals__": {},
})

# 2 · Concepto
concepto = section([
    row([
        container([
            eyebrow("El concepto", "secondary"),
            heading("[PPT] Nombre de la campaña", "h2", "primary", px=56),
            divider(),
            text("<p>[PPT] La gran idea en dos o tres frases: qué sentimos, qué vivimos y por qué "
                 "Multiplaza es el lugar donde la Navidad sucede.</p>"),
        ], {"content_width": "full", "width": {"unit": "%", "size": 50}, "width_mobile": {"unit": "%", "size": 100},
            "flex_justify_content": "center", "_animation": "fadeInLeft"}, inner=True),
        container([image("Key visual de la campaña")],
                  {"content_width": "full", "width": {"unit": "%", "size": 46}, "width_mobile": {"unit": "%", "size": 100},
                   "_animation": "fadeInRight"}, inner=True),
    ], gap=48, wrap=False),
], "marfil", extra={"_element_id": "concepto"})

# 3 · Objetivos
objetivos = section([
    eyebrow("Objetivos", "secondary", "center"),
    heading("Lo que vamos a lograr", "h2", "primary", "center", px=48),
    row([
        card([widget("icon-box", {"selected_icon": {"value": icon, "library": "fa-solid"}, "title_text": t,
                                  "description_text": d, "position": "top", "title_size": "h3",
                                  "__globals__": {"primary_color": C + "secondary", "title_color": C + "primary",
                                                  "description_color": C + "text",
                                                  "title_typography_typography": T + "secondary",
                                                  "description_typography_typography": T + "text"}})],
             delay=i * 150)
        for i, (icon, t, d) in enumerate([
            ("fas fa-users", "Afluencia", "[PPT] Atraer más visitas durante noviembre y diciembre."),
            ("fas fa-shopping-bag", "Ventas", "[PPT] Impulsar el ticket promedio de los locatarios."),
            ("fas fa-heart", "Emoción", "[PPT] Crear momentos memorables que se compartan."),
        ])
    ]),
], "blanco")

# 4 · Experiencias
experiencias = section([
    eyebrow("Experiencias", "accent", "center"),
    heading("Momentos que <em>brillan</em>", "h2", "blanco", "center", px=48),
    row([
        card([image(t), heading(t, "h3", "primary", px=26), text(f"<p>{d}</p>")], "marfil", basis=22, delay=i * 120)
        for i, (t, d) in enumerate([
            ("Encendido del árbol", "[PPT] El evento de apertura de la temporada."),
            ("Villa navideña", "[PPT] Un recorrido inmersivo para toda la familia."),
            ("Show y música", "[PPT] Coros, conciertos y personajes."),
            ("Santa en Multiplaza", "[PPT] Fotos, cartas y sorpresas."),
        ])
    ], gap=24),
], "primary")

# 5 · Decoración / mood
decoracion = section([
    row([
        container([
            eyebrow("Decoración", "secondary"),
            heading("[PPT] Un universo visual", "h2", "primary", px=48),
            divider("secondary"),
            text("<p>[PPT] Paleta, materiales, iluminación y piezas protagonistas de la ambientación.</p>"),
        ], {"content_width": "full", "width": {"unit": "%", "size": 38}, "width_mobile": {"unit": "%", "size": 100},
            "flex_justify_content": "center"}, inner=True),
        container([row([image("Mood 1"), image("Mood 2")], gap=16), row([image("Mood 3"), image("Mood 4")], gap=16)],
                  {"content_width": "full", "width": {"unit": "%", "size": 58}, "width_mobile": {"unit": "%", "size": 100},
                   "gap": {"unit": "px", "size": 16, "column": "16", "row": "16"}, "_animation": "zoomIn"}, inner=True),
    ], gap=48, wrap=False),
], "salvia")

# 6 · Calendario
fases = [("Nov", "Lanzamiento", "[PPT] Encendido y apertura de la temporada."),
         ("Dic · 1ª quincena", "Temporada alta", "[PPT] Activaciones y shows de fin de semana."),
         ("Dic · 2ª quincena", "Cierre mágico", "[PPT] Nochebuena y último impulso de compras."),
         ("Ene", "Balance", "[PPT] Resultados y aprendizajes.")]
calendario = section([
    eyebrow("Calendario", "secondary", "center"),
    heading("La temporada, paso a paso", "h2", "primary", "center", px=48),
    row([card([eyebrow(f, "secondary"), heading(t, "h3", "primary", px=26), text(f"<p>{d}</p>")],
              "marfil", basis=22, delay=i * 120) for i, (f, t, d) in enumerate(fases)], gap=24),
], "blanco", extra={"_element_id": "calendario"})

# 7 · Cifras
cifras = section([
    row([
        container([widget("counter", {"starting_number": 0, "ending_number": n, "suffix": suf, "title": t,
                                      "__globals__": {"number_color": C + "accent", "title_color": C + "oroclaro",
                                                      "typography_number_typography": T + "primary",
                                                      "typography_title_typography": T + "accent"}})],
                  {"content_width": "full", "width": {"unit": "%", "size": 22}, "width_mobile": {"unit": "%", "size": 100}},
                  inner=True)
        for n, suf, t in [(45, "", "[PPT] Días de temporada"), (30, "+", "[PPT] Activaciones"),
                          (1, "M+", "[PPT] Visitas esperadas"), (100, "%", "Magia navideña")]
    ], gap=24),
], "noche", pad=90)

# 8 · Cierre
cierre = section([
    heading("Hagamos brillar esta Navidad", "h2", "blanco", "center", px=64),
    text("<p>[PPT] Frase de cierre de la propuesta y siguiente paso.</p>", "oroclaro", "center"),
    button("Conversemos", "#contacto"),
], "vino", pad=140, extra={"flex_align_items": "center"})

template = {
    "version": "0.4",
    "title": "Navidad Multiplaza 2026",
    "type": "page",
    "page_settings": {"hide_title": "yes", "template": "elementor_canvas"},
    "content": [hero, concepto, objetivos, experiencias, decoracion, calendario, cifras, cierre],
}

if __name__ == "__main__":
    with open("navidad-multiplaza-elementor.json", "w", encoding="utf-8") as f:
        json.dump(template, f, ensure_ascii=False, indent=1)
    print("ok", len(template["content"]), "secciones")
