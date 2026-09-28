"""Landing profesional de Lindsay Meneses (lindsaymeneses.com), hecha con widgets nativos de Elementor.

Uso:  python3 build_landing.py  ->  landing-elementor-data.json (meta _elementor_data de la página)
Datos: ver FUENTES.md (solo información pública verificada). Cada proyecto es un evento/campaña; los
proyectos con página propia (p. ej. Navidad Multiplaza 2026) enlazan a ella.
Animaciones nativas de Elementor: presentación de fondo con Ken Burns, entradas (fadeInUp) y contadores.
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
C = "globals/colors?id="
T = "globals/typography?id="
UP = "https://lindsaymeneses.com/wp-content/uploads/2026/09/"
MAIL = "mailto:contacto@lindsaymeneses.com?subject=Contacto%20desde%20lindsaymeneses.com"
LINKEDIN = "https://www.linkedin.com/in/lindsay-meneses-cambronero-3b424420/"

# Medios ya subidos (ID, archivo)
IMG = {
    "rojo": (14, "nm-rojo-dorado-scaled.jpg"), "luces": (27, "nm-c13.jpg"), "pino": (23, "nm-c05-scaled.jpg"),
    "esferas": (9, "nm-esferas-navidad-scaled.jpg"), "cascabeles": (21, "nm-c03-scaled.jpg"),
    "chispa": (19, "nm-c01-scaled.jpg"), "estrella": (17, "nm-estrella-scaled.jpg"), "copo": (24, "nm-c06-scaled.jpg"),
}

_seq = iter(range(1, 10**6))


def uid():
    return f"l{next(_seq):06x}"


def px(v, unit="px"):
    return {"unit": unit, "size": v}


def pad(t, r=None, b=None, l=None):
    r = t if r is None else r
    return {"unit": "px", "top": t, "right": r, "bottom": t if b is None else b, "left": r if l is None else l, "isLinked": False}


def gap(n):
    return {"unit": "px", "size": n, "column": str(n), "row": str(n)}


def anim(s, delay=0, kind="fadeInUp"):
    s.update({"_animation": kind, "animation_duration": "slow", "_animation_delay": delay})
    return s


def container(children, settings=None, inner=True):
    s = {"content_width": "full", "flex_direction": "column", "padding": pad(0)}
    s.update(settings or {})
    return {"id": uid(), "elType": "container", "isInner": inner, "settings": s, "elements": children}


def widget(kind, settings):
    return {"id": uid(), "elType": "widget", "widgetType": kind, "isInner": False, "settings": settings, "elements": []}


def eyebrow(text, color="accent", align="left", d=0):
    return widget("heading", anim({"title": text, "header_size": "p", "align": align,
                                   "_css_classes": "lm-eyebrow" + (" lm-c" if align == "center" else ""),
                                   "__globals__": {"title_color": C + color, "typography_typography": T + "accent"}}, d))


def heading(text, size="h2", color="primary", align="left", fs=None, typo="primary", d=100, cls="lm-t"):
    s = {"title": text, "header_size": size, "align": align, "_css_classes": cls,
         "__globals__": {"title_color": C + color, "typography_typography": T + typo}}
    if fs:
        s.update({"typography_font_size": px(fs), "typography_font_size_tablet": px(round(fs * .8)),
                  "typography_font_size_mobile": px(max(round(fs * .6), 20))})
    return widget("heading", anim(s, d))


def text(markup, color="text", align="left", maxw=None, d=200):
    s = {"editor": markup, "align": align, "__globals__": {"text_color": C + color, "typography_typography": T + "text"}}
    if maxw:
        s.update({"_element_width": "initial", "_element_custom_width": px(maxw), "_element_custom_width_mobile": px(100, "%")})
    return widget("text-editor", anim(s, d))


def button(label, url, ghost=False, dark=True, align="left", d=300):
    """Botón nativo: mismo borde, alto y tipografía en ambas variantes, así quedan alineados."""
    fg = "blanco" if dark else "primary"
    s = {"text": label, "link": {"url": url, "is_external": url.startswith("http"), "nofollow": False},
         "align": align, "align_mobile": "justify", "size": "md", "_element_width": "auto", "_element_width_mobile": "inherit",
         "border_border": "solid", "border_width": {"unit": "px", "top": 1, "right": 1, "bottom": 1, "left": 1, "isLinked": True},
         "border_radius": {"unit": "px", "top": 0, "right": 0, "bottom": 0, "left": 0, "isLinked": True},
         "text_padding": pad(19, 34), "_css_classes": "lm-btn",
         "__globals__": {"typography_typography": T + "accent"}}
    if ghost:
        s["background_color"] = "transparent"
        s["__globals__"].update({"button_text_color": C + fg, "border_color": C + ("oroclaro" if dark else "primary"),
                                 "button_background_hover_color": C + "accent", "hover_color": C + "noche",
                                 "button_hover_border_color": C + "accent"})
    else:
        s["__globals__"].update({"background_color": C + "accent", "button_text_color": C + "noche", "border_color": C + "accent",
                                 "button_background_hover_color": C + "oroclaro", "hover_color": C + "noche",
                                 "button_hover_border_color": C + "oroclaro"})
    return widget("button", anim(s, d))


def image(key, alt, cls="lm-img", size="large", d=0):
    i, f = IMG[key]
    return widget("image", anim({"image": {"url": UP + f, "id": i, "alt": alt, "source": "library"}, "image_size": size,
                                 "_css_classes": cls}, d, "fadeIn"))


def counter(n, title, prefix="", suffix="", d=0):
    return widget("counter", anim({"starting_number": 0, "ending_number": n, "prefix": prefix, "suffix": suffix,
                                   "duration": 2200, "thousand_separator": "", "title": title, "_css_classes": "lm-counter",
                                   "__globals__": {"number_color": C + "accent", "title_color": C + "oroclaro",
                                                   "typography_title_typography": T + "text"}}, d))


def icon_list(items, color="text", d=200):
    return widget("icon-list", anim({"icon_list": [{"_id": uid(), "text": t, "selected_icon": {"value": "fas fa-minus", "library": "fa-solid"}}
                                                   for t in items],
                                     "_css_classes": "lm-list", "__globals__": {"icon_color": C + "accent", "text_color": C + color,
                                                                               "icon_typography_typography": T + "text"}}, d))


def line(color="accent", width=72, center=False, d=150):
    return widget("divider", anim({"width": px(width), "weight": px(1), "align": "center" if center else "left",
                                   "__globals__": {"color": C + color}}, d, "fadeIn"))


def row(children, g=40, align="stretch", wrap=True, mobile="column", tablet=None):
    s = {"flex_direction": "row", "flex_wrap": "wrap" if wrap else "nowrap", "flex_direction_mobile": mobile,
         "gap": gap(g), "flex_align_items": align}
    if tablet:
        s["flex_direction_tablet"] = tablet
    return container(children, s)


def col(children, w, g=20, tablet=None, justify="center", extra=None):
    s = {"width": px(w, "%"), "width_mobile": px(100, "%"), "gap": gap(g), "flex_justify_content": justify}
    if tablet:
        s["width_tablet"] = px(tablet, "%")
    s.update(extra or {})
    return container(children, s)


def section(children, bg, eid=None, extra=None, cls=""):
    s = {"content_width": "boxed", "boxed_width": px(1200), "flex_direction": "column", "gap": gap(28),
         "padding": pad(130, 56), "padding_tablet": pad(100, 40), "padding_mobile": pad(84, 22),
         "background_background": "classic", "__globals__": {"background_color": C + bg}, "css_classes": ("lm-sec " + cls).strip()}
    if eid:
        s["_element_id"] = eid
    s.update(extra or {})
    return container(children, s, inner=False)


CSS = """<style>
.lm-t .elementor-heading-title{font-weight:400!important;letter-spacing:-.02em!important;line-height:1.06!important}
.lm-t em{font-style:italic;font-weight:300;color:#C9A45C}
.lm-eyebrow .elementor-heading-title{letter-spacing:.28em!important}
.lm-eyebrow .elementor-heading-title::before{content:"";display:inline-block;width:36px;height:1px;background:currentColor;vertical-align:middle;margin:0 14px 3px 0;opacity:.7}
.lm-eyebrow.lm-c .elementor-heading-title::after{content:"";display:inline-block;width:36px;height:1px;background:currentColor;vertical-align:middle;margin:0 0 3px 14px;opacity:.7}
.lm-btn .elementor-button{min-height:56px;display:inline-flex;align-items:center;justify-content:center;transition:all .4s ease}
.lm-img img{width:100%!important;height:var(--h,300px)!important;object-fit:cover;display:block;border-radius:0!important}
.lm-img.tall{--h:620px}.lm-img.feat{--h:520px}.lm-img.card{--h:260px}
.lm-card{transition:transform .6s cubic-bezier(.2,.7,.2,1)}.lm-card:hover{transform:translateY(-6px)}
.lm-card .lm-img{overflow:hidden}.lm-card .lm-img img{transition:transform 1.4s cubic-bezier(.2,.7,.2,1)}.lm-card:hover .lm-img img{transform:scale(1.05)}
.lm-frame{position:relative;isolation:isolate}
.lm-frame::after{content:"";position:absolute;inset:0;transform:translate(18px,18px);border:1px solid rgba(201,164,92,.65);z-index:-1;pointer-events:none}
.lm-counter .elementor-counter-number-wrapper{font-family:'Fraunces',serif;font-weight:300;font-size:clamp(48px,5vw,76px);line-height:1}
.lm-counter .elementor-counter-title{font-size:14px;line-height:1.4;margin-top:8px;text-align:left}
.lm-counter .elementor-counter-number-wrapper{justify-content:flex-start}
.lm-list .elementor-icon-list-item{padding:6px 0!important}
.lm-time .elementor-icon-list-text{font-size:16px}
@media(max-width:1024px){.lm-img.tall{--h:520px}.lm-img.feat{--h:420px}}
@media(max-width:767px){.lm-img.tall{--h:380px}.lm-img.feat{--h:300px}.lm-img.card{--h:220px}.lm-frame::after{transform:translate(10px,10px)}}
@media (prefers-reduced-motion:reduce){.elementor-invisible{visibility:visible!important}.lm-card,.lm-card .lm-img img{transition:none}}
</style>"""

hero = container([
    widget("html", {"html": CSS}),
    col([
        eyebrow("Mercadeo · Publicidad · Experiencias de marca", "accent"),
        heading("Lindsay <em>Meneses</em>", "h1", "blanco", fs=104),
        line("accent", 90),
        text("<p>Creo experiencias de marca que se viven en persona: campañas, eventos y temporadas que llenan de gente "
             "los centros comerciales. Jefa de Mercadeo y Publicidad en Grupo Roble · Multiplaza Costa Rica.</p>",
             "oroclaro", maxw=560),
        row([button("Ver proyectos", "#proyectos"), button("Conversemos", MAIL, ghost=True, d=400)], g=14, align="center",
            mobile="column"),
    ], 64, g=26, tablet=90),
], {"content_width": "boxed", "boxed_width": px(1200), "min_height": px(100, "vh"), "flex_justify_content": "center",
    "padding": pad(140, 56), "padding_mobile": pad(110, 22, 90), "gap": gap(20), "_element_id": "inicio",
    "background_background": "slideshow", "background_slideshow_gallery": [{"id": IMG[k][0], "url": UP + IMG[k][1]} for k in ("luces", "rojo", "pino")],
    "background_slideshow_loop": "yes", "background_slideshow_slide_duration": 6000, "background_slideshow_slide_transition": "fade",
    "background_slideshow_transition_duration": 1500, "background_slideshow_ken_burns": "yes",
    "background_slideshow_ken_burns_zoom_direction": "in", "background_overlay_background": "gradient",
    "background_overlay_color": "#071812", "background_overlay_color_b": "#0A241C", "background_overlay_gradient_angle": {"unit": "deg", "size": 90},
    "background_overlay_color_stop": px(35, "%"), "background_overlay_color_b_stop": px(100, "%"),
    "background_overlay_opacity": {"unit": "px", "size": .82}, "css_classes": "lm-sec lm-hero"}, inner=False)

sobre = section([
    row([
        col([image("estrella", "Estrella dorada", "lm-img tall lm-frame", "large")], 42, tablet=100),
        col([
            eyebrow("01 · Perfil", "secondary"),
            heading("Más de diez años convirtiendo visitas en <em>momentos</em>", "h2", "primary", fs=52),
            line(),
            text("<p>Profesional en mercadeo y publicidad con más de 10 años de experiencia. Lidera la estrategia de mercadeo, "
                 "los eventos y las campañas de Multiplaza Escazú y Multiplaza Curridabat, en Grupo Roble.</p>"
                 "<p>Su trabajo une estrategia y producción: coordinación de eventos, campañas de temporada, alianzas con marcas, "
                 "manejo de clientes y presupuestos, y seguimiento del tráfico de los centros comerciales.</p>", maxw=520),
            icon_list(["Máster en Marketing, Marketing Digital y Redes Sociales · IM Digital Business School",
                       "Administración de Empresas · Universidad Hispanoamericana",
                       "San José, Costa Rica"], "text"),
        ], 50, g=22, tablet=100),
    ], g=80, align="center", wrap=False, tablet="column"),
], "marfil", "perfil")

cifras = section([
    row([
        col([counter(10, "años en mercadeo y publicidad", "+")], 30, tablet=30),
        col([counter(2, "centros comerciales Multiplaza en Costa Rica", d=150)], 30, tablet=30),
        col([counter(15, "zonas en la propuesta Navidad 2026", d=300)], 30, tablet=30),
    ], g=40, wrap=False),
], "noche", extra={"padding": pad(90, 56), "padding_mobile": pad(70, 22)})

areas = section([
    eyebrow("02 · Qué hace", "secondary", "center"),
    heading("Estrategia que se ve, se toca y se <em>recuerda</em>", "h2", "primary", "center", fs=50),
    row([col([heading(t, "h3", "primary", fs=26, d=100 + i * 80), line(width=40, d=150 + i * 80), text(f"<p>{d}</p>", d=200 + i * 80)],
             23, g=14, tablet=46, justify="flex-start")
         for i, (t, d) in enumerate([
             ("Eventos y temporadas", "Navidad, Día de la Niñez, Día de las Madres: conceptos, montaje y activaciones que atraen a toda la familia."),
             ("Campañas y publicidad", "Estrategia, mensajes y medios para campañas comerciales como Black Friday y aperturas de marcas."),
             ("Alianzas y causas", "Campañas con marcas y fundaciones, como «El Regalo de Dar» con BAC y Fundación Génesis."),
             ("Gestión y resultados", "Manejo de clientes y presupuestos, y seguimiento del tráfico de los centros comerciales."),
         ])], g=32),
], "blanco", "areas")

def proyecto(img_key, alt, anio, titulo, desc, url=None, d=0, basis=31):
    kids = [image(img_key, alt, "lm-img card", "medium_large", d), eyebrow(anio, "secondary", d=d + 80),
            heading(titulo, "h3", "primary", fs=28, d=d + 120), text(f"<p>{desc}</p>", d=d + 160)]
    if url:
        kids.append(button("Ver proyecto", url, ghost=True, dark=False, d=d + 200))
    return container(kids, {"width": px(basis, "%"), "width_tablet": px(46, "%"), "width_mobile": px(100, "%"), "flex_grow": 1,
                            "gap": gap(14), "css_classes": "lm-card"})


proyectos = section([
    eyebrow("03 · Proyectos", "accent", "center"),
    heading("Cada evento, un <em>proyecto</em>", "h2", "blanco", "center", fs=56),
    line("accent", 90, center=True),
    row([
        col([image("rojo", "Esferas rojas y doradas en un pino", "lm-img feat lm-frame", "large")], 56, tablet=100),
        col([eyebrow("2026 · Propuesta · Escazú y Curridabat", "accent"),
             heading("Navidad <em>Multiplaza</em> 2026", "h3", "blanco", fs=48),
             text("<p>Propuesta de decoración navideña zona por zona: fachadas, un túnel de luz en Plaza Starbucks, "
                  "un árbol de 7 metros en Plaza Brunos, ball pit de 158 m² en Plaza Tukis y un cielo de cables de luz "
                  "en Plaza Santo Katrin.</p>", "oroclaro", maxw=460),
             button("Ver el proyecto", "/navidad-multiplaza-2026/")], 38, g=20, tablet=100),
    ], g=64, align="center", wrap=False, tablet="column"),
    row([
        proyecto("esferas", "Esferas navideñas pintadas a mano", "2022 · Navidad", "Christmas Around the World",
                 "Temporada navideña con decoraciones inspiradas en distintas partes del mundo, pista de patinaje, "
                 "desfiles, arte y emprendimientos.", d=0),
        proyecto("cascabeles", "Cascabeles rojos y blancos", "2024 · Alianza", "El Regalo de Dar",
                 "Campaña con BAC a beneficio de fundaciones, con la meta de reunir 500 regalos para niños de "
                 "Fundación Génesis y activaciones en los centros comerciales.", d=120),
        proyecto("copo", "Copo de nieve decorativo", "2024 · Día de la Niñez", "Dragones y dinosaurios",
                 "Del 7 de setiembre al 6 de octubre: más de ocho dragones animatrónicos de más de 4 metros "
                 "y espacios interactivos para las familias.", d=240),
    ], g=32),
], "noche", "proyectos", extra={"padding_mobile": pad(84, 22)})

trayectoria = section([
    row([
        col([eyebrow("04 · Trayectoria", "secondary"), heading("Temporadas que marcaron el <em>calendario</em>", "h2", "primary", fs=46),
             line()], 38, tablet=100, justify="flex-start"),
        col([widget("icon-list", anim({"icon_list": [{"_id": uid(), "text": t, "selected_icon": {"value": "fas fa-circle", "library": "fa-solid"}}
                                                     for t in [
                                                         "2021 · «Elf Christmas»: inauguración de la Navidad transmitida en vivo en redes",
                                                         "2022 · «Christmas Around the World» en Multiplaza",
                                                         "2024 · Día de las Madres: eventos y sorpresas",
                                                         "2024 · Día de la Niñez con dragones y dinosaurios animatrónicos",
                                                         "2024 · Black Friday: horario extendido, descuentos y premios",
                                                         "2024 · «El Regalo de Dar» con BAC y Fundación Génesis",
                                                         "2026 · Propuesta Navidad Multiplaza (Escazú y Curridabat)"]],
                                       "space_between": px(18), "icon_size": px(8), "_css_classes": "lm-list lm-time",
                                       "__globals__": {"icon_color": C + "accent", "text_color": C + "text",
                                                       "icon_typography_typography": T + "text"}}, 200))], 56, tablet=100),
    ], g=64, wrap=False, tablet="column"),
], "marfil", "trayectoria")

contacto = section([
    eyebrow("05 · Contacto", "oroclaro", "center"),
    heading("¿Creamos la próxima <em>temporada</em>?", "h2", "blanco", "center", fs=64),
    line("oroclaro", 90, center=True),
    text("<p>Eventos, campañas y experiencias de marca para centros comerciales y marcas que quieren que la gente llegue, "
         "se quede y vuelva.</p>", "oroclaro", "center", maxw=560),
    row([button("Escríbeme", MAIL, align="center"), button("LinkedIn", LINKEDIN, ghost=True, align="center", d=400)],
        g=14, align="center", mobile="column"),
], "noche", "contacto", extra={"flex_align_items": "center", "background_background": "classic",
                               "background_image": {"url": UP + IMG["chispa"][1], "id": IMG["chispa"][0], "source": "library"},
                               "background_position": "center center", "background_size": "cover",
                               "background_overlay_background": "classic", "background_overlay_color": "#071812",
                               "background_overlay_opacity": {"unit": "px", "size": .78}})

pie = container([
    heading("Lindsay Meneses", "p", "blanco", "center", fs=24, typo="secondary", d=0),
    text("<p>Mercadeo y publicidad · San José, Costa Rica · <a href=\"" + MAIL + "\" style=\"color:inherit\">contacto@lindsaymeneses.com</a></p>",
         "salvia", "center", d=0),
], {"content_width": "boxed", "boxed_width": px(1200), "padding": pad(48, 56), "padding_mobile": pad(40, 22), "gap": gap(10),
    "background_background": "classic", "__globals__": {"background_color": C + "noche"}}, inner=False)

CONTENT = [hero, sobre, cifras, areas, proyectos, trayectoria, contacto, pie]

if __name__ == "__main__":
    data = json.dumps(CONTENT, ensure_ascii=False, separators=(",", ":"))
    (HERE / "landing-elementor-data.json").write_text(data, encoding="utf-8")
    print("ok landing-elementor-data.json", len(data), "bytes")
