"""Genera la plantilla Elementor (JSON importable) de la página Navidad Multiplaza 2026.

Uso:  python3 build_template.py         ->  escribe navidad-multiplaza-elementor.json
      python3 build_template.py --page  ->  escribe page-elementor-data.json (meta _elementor_data)
Los textos marcados con «[PPT]» se reemplazan con el contenido real del deck.
"""
import json
import secrets
import sys

# --page: datos para una página WordPress; sin imágenes del PPT, cada imagen vacía se
# sustituye por un panel decorativo para que no queden huecos.
PAGE = "--page" in sys.argv

C = "globals/colors?id="
T = "globals/typography?id="


_seq = iter(range(1, 10**6))


def uid():
    # En modo página, IDs cortos y deterministas para un JSON estable.
    return f"n{next(_seq):06x}" if PAGE else secrets.token_hex(4)[:7]


def container(children, settings=None, inner=False):
    s = {"content_width": "boxed", "flex_direction": "column", "boxed_width": {"unit": "px", "size": 1200}}
    s.update(settings or {})
    return {"id": uid(), "elType": "container", "isInner": inner, "settings": s, "elements": children}


def widget(kind, settings):
    return {"id": uid(), "elType": "widget", "widgetType": kind, "isInner": False, "settings": settings, "elements": []}


FX = """<canvas class="nm-snow" aria-hidden="true"></canvas>
<style>
.nm-hero{position:relative;overflow:hidden}
.nm-hero>*>*:not(.nm-fx){position:relative;z-index:1}
.nm-fx{position:absolute!important;inset:0;margin:0!important;pointer-events:none;z-index:0;width:100%!important}
.nm-fx .elementor-widget-container{height:100%}
.nm-snow{width:100%;height:100%;display:block}
.nm-hero h1 em{background:linear-gradient(100deg,#C9A45C 20%,#FFF3D1 40%,#EBD9AE 50%,#C9A45C 70%);
  background-size:220% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;
  animation:nm-shine 5s ease-in-out infinite}
@keyframes nm-shine{0%,100%{background-position:100% 0}50%{background-position:0 0}}
.nm-card{transition:transform .45s cubic-bezier(.2,.7,.2,1),box-shadow .45s}
.nm-card:hover{transform:translateY(-8px);box-shadow:0 30px 60px -24px rgba(10,36,28,.45)!important}
.nm-panel svg{animation:nm-twinkle 3.2s ease-in-out infinite;transform-origin:center}
.nm-panel:nth-child(2n) svg{animation-delay:1.1s}
@keyframes nm-twinkle{0%,100%{transform:scale(1);opacity:.85}50%{transform:scale(1.12);opacity:1;
  filter:drop-shadow(0 0 10px rgba(235,217,174,.6))}}
.nm-line .elementor-divider-separator,.nm-line{transform-origin:left}
.nm-line.nm-in{animation:nm-grow 1s cubic-bezier(.2,.7,.2,1) both}
@keyframes nm-grow{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@media (prefers-reduced-motion:reduce){.nm-hero h1 em,.nm-panel svg,.nm-line.nm-in{animation:none}
  .nm-card,.nm-card:hover{transition:none;transform:none}.nm-snow{display:none}}
</style>
<script>
(function(){
  var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('.nm-line').forEach(function(el){
    if(!('IntersectionObserver' in window)){el.classList.add('nm-in');return;}
    new IntersectionObserver(function(es,o){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('nm-in');o.unobserve(e.target);}});},{threshold:.6}).observe(el);
  });
  if(reduce)return;
  var c=document.querySelector('.nm-snow');if(!c)return;
  var x=c.getContext('2d'),w,h,d=Math.min(window.devicePixelRatio||1,2),f=[];
  function size(){w=c.clientWidth;h=c.clientHeight;c.width=w*d;c.height=h*d;x.setTransform(d,0,0,d,0,0);}
  size();addEventListener('resize',size);
  var n=Math.round(Math.min(110,w/12));
  for(var i=0;i<n;i++)f.push({x:Math.random()*w,y:Math.random()*h,r:Math.random()*2.2+.6,
    s:Math.random()*.5+.25,o:Math.random()*Math.PI*2,g:Math.random()<.22});
  function tick(t){
    x.clearRect(0,0,w,h);
    for(var i=0;i<f.length;i++){var p=f[i];
      p.y+=p.s;p.x+=Math.sin(t/1800+p.o)*.35;if(p.y>h+5){p.y=-5;p.x=Math.random()*w;}
      var a=p.g?.55+.45*Math.sin(t/400+p.o):.75;
      x.beginPath();x.arc(p.x,p.y,p.g?p.r*.9:p.r,0,6.283);
      x.fillStyle=p.g?'rgba(235,217,174,'+a+')':'rgba(255,255,255,'+a*.8+')';
      if(p.g){x.shadowBlur=8;x.shadowColor='rgba(235,217,174,.9)';}else x.shadowBlur=0;
      x.fill();}
    if(!document.hidden)requestAnimationFrame(tick);
  }
  document.addEventListener('visibilitychange',function(){if(!document.hidden)requestAnimationFrame(tick);});
  requestAnimationFrame(tick);
})();
</script>"""


def eyebrow(text, color="accent", align="left"):
    return widget("heading", {
        "title": text, "header_size": "p", "align": align,
        "typography_text_transform": "uppercase",
        "typography_letter_spacing": {"unit": "em", "size": 0.25},
        "__globals__": {"title_color": C + color, "typography_typography": T + "accent"},
    })


def heading(text, size="h2", color="primary", align="left", px=None):
    s = {"title": text, "header_size": size, "align": align, "_animation": "fadeInUp",
         "__globals__": {"title_color": C + color, "typography_typography": T + "primary"}}
    if px:
        s["typography_font_size"] = {"unit": "px", "size": px}
        s["typography_font_size_tablet"] = {"unit": "px", "size": round(px * 0.75)}
        s["typography_font_size_mobile"] = {"unit": "px", "size": max(round(px * 0.55), 20)}
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
                              "_css_classes": "nm-line",
                              "__globals__": {"color": C + color}})


PANEL_ICONS = {"Key visual de la campaña": "fas fa-star", "Encendido del árbol": "fas fa-tree",
               "Villa navideña": "fas fa-home", "Show y música": "fas fa-music",
               "Santa en Multiplaza": "fas fa-gift", "Mood 1": "fas fa-snowflake", "Mood 2": "fas fa-star",
               "Mood 3": "fas fa-gifts", "Mood 4": "fas fa-candy-cane"}


def panel(label):
    # Panel decorativo en lugar de una imagen que aún no existe.
    tall = label.startswith("Key")
    return container([widget("icon", {"selected_icon": {"value": PANEL_ICONS.get(label, "fas fa-star"), "library": "fa-solid"},
                                       "size": {"unit": "px", "size": 72 if tall else 40},
                                       "__globals__": {"primary_color": C + "accent"}})], {
        "content_width": "full", "flex_justify_content": "center", "flex_align_items": "center", "flex_grow": 1,
        "min_height": {"unit": "px", "size": 420 if tall else 170},
        "min_height_mobile": {"unit": "px", "size": 260 if tall else 120},
        "border_radius": {"unit": "px", "top": 18, "right": 18, "bottom": 18, "left": 18, "isLinked": True},
        "background_background": "gradient", "background_color": "#0A241C", "background_color_b": "#0F3B2E",
        "background_gradient_type": "radial", "background_gradient_position": "center center",
        "_title": label, "css_classes": "nm-panel",
    }, inner=True)


def image(label):
    if PAGE:
        return panel(label)
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


def row(children, gap=32, wrap=True, mobile_row=False):
    return container(children, {"flex_direction": "row", "flex_wrap": "wrap" if wrap else "nowrap",
                                "flex_direction_mobile": "row" if mobile_row else "column",
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
        "_animation": anim, "animation_delay": delay, "css_classes": "nm-card",
    }, inner=True)


# 1 · Portada
hero = section([
    widget("html", {"html": FX, "_css_classes": "nm-fx"}),
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
    "__globals__": {}, "css_classes": "nm-hero",
})

# 2 · Concepto
concepto = section([
    row([
        container([
            eyebrow("El concepto", "secondary"),
            heading("[PPT] Destellos de Navidad", "h2", "primary", px=56),
            divider(),
            text("<p>[PPT] La Navidad no se compra: se vive. Este año, Multiplaza se transforma en un "
                 "bosque encendido de luz y oro, donde cada pasillo guarda una sorpresa y cada visita "
                 "se convierte en tradición familiar.</p>"),
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
            heading("[PPT] Un bosque de luz y oro", "h2", "primary", px=48),
            divider("secondary"),
            text("<p>[PPT] Verdes profundos, dorados champán y destellos rojo vino. Materiales nobles, "
                 "miles de luces cálidas y piezas monumentales que invitan a detenerse, mirar hacia "
                 "arriba y tomar la foto de la temporada.</p>"),
        ], {"content_width": "full", "width": {"unit": "%", "size": 38}, "width_mobile": {"unit": "%", "size": 100},
            "flex_justify_content": "center"}, inner=True),
        container([row([image("Mood 1"), image("Mood 2")], gap=16, mobile_row=True),
                   row([image("Mood 3"), image("Mood 4")], gap=16, mobile_row=True)],
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
    text("<p>[PPT] Una temporada para volver, compartir y recordar. Encendamos juntos la Navidad "
         "más luminosa de Multiplaza.</p>", "oroclaro", "center"),
    button("Conversemos", "mailto:contacto@lindsaymeneses.com?subject=Navidad%20Multiplaza%202026"),
], "vino", pad=140, extra={"flex_align_items": "center"})

template = {
    "version": "0.4",
    "title": "Navidad Multiplaza 2026",
    "type": "page",
    "page_settings": {"hide_title": "yes", "template": "elementor_canvas"},
    "content": [hero, concepto, objetivos, experiencias, decoracion, calendario, cifras, cierre],
}

if __name__ == "__main__":
    if PAGE:
        # Datos para una página WordPress (meta _elementor_data), sin las marcas [PPT].
        def slim(el):
            # Quita claves redundantes para reducir el tamaño del meta.
            if not el["isInner"]:
                del el["isInner"]
            if el["elType"] == "container" and el["settings"].get("content_width") == "full":
                el["settings"].pop("boxed_width", None)
            for child in el["elements"]:
                slim(child)
        for el in template["content"]:
            slim(el)
        data = json.dumps(template["content"], ensure_ascii=False, separators=(",", ":")).replace("[PPT] ", "")
        with open("page-elementor-data.json", "w", encoding="utf-8") as f:
            f.write(data)
        print("ok page-elementor-data.json", len(data), "bytes")
    else:
        with open("navidad-multiplaza-elementor.json", "w", encoding="utf-8") as f:
            json.dump(template, f, ensure_ascii=False, indent=1)
        print("ok", len(template["content"]), "secciones")
