"""Fuente v5 de la página Navidad Multiplaza 2026: la presentación dividida por partes.

Parte del HTML de la versión completa (respaldo/pagina7-2026-09-28-2218.html) y lo reorganiza:
  - Portada, La propuesta y el concepto (campaña, lenguaje de diseño, sistema de iluminación).
  - PARTE I · Multiplaza Escazú: portadilla → Entradas → Fachadas → Decoración interna (capítulo + zonas).
  - PARTE II · Multiplaza Curridabat: portadilla → Entradas → Fachadas → Decoración interna (capítulo + zonas).
  - En cifras, Siguiente paso y pie.
Las entradas salen de las galerías de fachadas (y las palmeras del acceso, de los vacíos). Los textos se
reescriben con un tono más actual; los datos (medidas, cantidades, materiales) se conservan tal cual.

Uso:  python3 fuente_v5.py  ->  fuente-v5.html   (luego: python3 rebuild_v4.py fuente-v5.html)
"""
import copy
import re
from pathlib import Path

from bs4 import BeautifulSoup

HERE = Path(__file__).parent
SRC = HERE / "respaldo/pagina7-2026-09-28-2218.html"
OUT = HERE / "fuente-v5.html"
U = "https://lindsaymeneses.com/wp-content/uploads/2026/09/"

soup = BeautifulSoup(SRC.read_text(encoding="utf-8"), "html.parser")
root = soup.find("div", attrs={"data-elementor-id": "7"})
S = root.find_all("div", recursive=False)          # las 25 secciones originales, en orden
assert len(S) == 25, len(S)
(HERO, PROPUESTA, CAMPANA, LENGUAJE, LUZ, FACH_ESC, FACH_CUR, VAC_ESC, VAC_CUR, TUNEL, STARBUCKS, SANTA,
 TUKIS, BRUNOS, BRUNOS2, QUINTA, SIMAN, HONOR, CURRI, KATRIN, EQUIZ, REEBOK, CIFRAS, CIERRE, PIE) = S


# ---------------------------------------------------------------- utilidades
def widgets(sec, kind=None):
    out = [w for w in sec.find_all(attrs={"data-widget_type": True})]
    return [w for w in out if kind is None or w["data-widget_type"].startswith(kind)]


def eyebrow(sec, text):
    w = next(w for w in widgets(sec, "heading") if "nm-eyebrow" in w.get("class", []))
    w.find(class_="elementor-heading-title").string = text


def title(sec, html):
    w = next(w for w in widgets(sec, "heading") if "nm-t" in w.get("class", []) and "nm-eyebrow" not in w.get("class", []))
    t = w.find(class_="elementor-heading-title")
    t.clear()
    t.append(BeautifulSoup(html, "html.parser"))


def paras(sec):
    """Párrafos normales (sin fichas, cifras ni créditos)."""
    out = []
    for w in widgets(sec, "text-editor"):
        if w.find("ul") or w.find(class_="nm-credit") or w.find(class_="nm-sub"):
            continue
        out.append(w)
    return out


def para(sec, i, html):
    w = paras(sec)[i]
    w.clear()
    w.append(BeautifulSoup(html, "html.parser"))


def set_html(widget, html):
    widget.clear()
    widget.append(BeautifulSoup(html, "html.parser"))


def stats(sec, items, i=0):
    ul = [w for w in widgets(sec, "text-editor") if w.find("ul", class_="nm-stats")][i].find("ul")
    for li in ul.find_all("li"):
        li.decompose()
    for b, t in items:
        li = soup.new_tag("li")
        bb = soup.new_tag("b")
        bb.string = b
        li.append(bb)
        li.append(t)
        ul.append(li)


def tile(sec, name):
    """Saca de la sección la figura cuyo archivo contiene `name`."""
    for f in sec.find_all("figure"):
        if name in (f.get("data-full") or "") or name in str(f.find(["img", "video"]) or ""):
            return f.extract()
    raise KeyError(name)


def new_text_widget(html, classes=""):
    w = soup.new_tag("div", attrs={"class": f"elementor-element {classes} elementor-widget elementor-widget-text-editor".replace("  ", " "),
                                   "data-element_type": "widget", "data-widget_type": "text-editor.default"})
    w.append(BeautifulSoup(html, "html.parser"))
    return w


def after(ref, widget):
    ref.insert_after(widget)
    return widget


def divider_of(sec):
    return widgets(sec, "divider")[0]


def clone(sec, anchor=None):
    c = copy.deepcopy(sec)
    if anchor:
        c["id"] = anchor
    elif c.has_attr("id"):
        del c["id"]
    return c


def n(i):
    return f"{i:02d}"


def credit(sec, html):
    for w in widgets(sec, "text-editor"):
        p = w.find(class_="nm-credit")
        if p:
            set_html(w, f'<p class="nm-credit">{html}</p>')
            return


MECA = "Iluminación de fachadas, entradas y vacíos · <b>La Meca Concept</b>"
KARJIM = "Ambientación y decoración interior · <b>Karjim Design</b>"


# ---------------------------------------------------------------- portada
eyebrow(HERO, "Navidad 2026 · Multiplaza Escazú y Multiplaza Curridabat")
para(HERO, 0, "<p>Propuesta integral de iluminación y ambientación navideña para Multiplaza Escazú y Multiplaza "
              "Curridabat. Un recorrido en tres capas por cada centro comercial: las <strong>entradas</strong> que reciben, "
              "las <strong>fachadas</strong> que anuncian desde la calle y la <strong>decoración interna</strong> que envuelve "
              "vacíos, pasillos y plazas.</p>")
stats(HERO, [("2", "centros comerciales"), ("3", "capas: entradas, fachadas, interior"), ("17", "animaciones de luz")])
btns = HERO.find("div", class_="nm-btns")
set_html(btns, '<a class="nm-btn" href="#escazu">Recorrer Escazú</a><a class="nm-btn ghost" href="#curridabat">Ir a Curridabat</a>')

# ---------------------------------------------------------------- 01 la propuesta
eyebrow(PROPUESTA, f"{n(1)} La propuesta")
title(PROPUESTA, "Dos centros, <em>un mismo lenguaje de luz</em>")
para(PROPUESTA, 0, "<p>La Navidad 2026 de Multiplaza se vive como un recorrido. Empieza en la calle, con las entradas y las "
                   "fachadas encendidas, y continúa adentro: vacíos, pasillos y plazas se transforman zona por zona. "
                   "Escazú y Curridabat comparten el concepto y cada centro lo interpreta con sus propios espacios.</p>")
set_html(PROPUESTA.find("div", class_="nm-zcols"), (
    '<div><h3>Cómo se organiza<span>Tres capas</span></h3>'
    '<ul class="nm-zones"><li>Entradas · la bienvenida desde el acceso</li><li>Fachadas · la luz que anuncia desde la calle</li>'
    '<li>Decoración interna · vacíos, pasillos y plazas</li></ul>'
    f'<p class="nm-credit" style="margin-top:14px">{MECA}</p><p class="nm-credit" style="margin-top:8px">{KARJIM}</p></div>'
    '<div><h3>Parte I<span>Multiplaza Escazú</span></h3>'
    '<ul class="nm-zones"><li>Entradas y accesos</li><li>Fachadas</li><li>Vacíos y tragaluces</li><li>Túnel de arcos</li>'
    '<li>Plaza Starbucks</li><li>Pasillo Starbucks → Tukis y Casa de Santa</li><li>Plaza Tukis</li><li>Plaza Brunos</li>'
    '<li>Pasillo Quinta Etapa</li><li>Plaza Siman</li><li>Pasillo BCR – Vértigo</li><li>Plaza Honor</li></ul></div>'
    '<div><h3>Parte II<span>Multiplaza Curridabat</span></h3>'
    '<ul class="nm-zones"><li>Entradas y accesos</li><li>Fachadas</li><li>Vacíos y food court</li><li>Plaza Santo Katrin</li>'
    '<li>Pasillo Equiz – Vértigo</li><li>Plaza Reebok</li><li>Plaza Cinemark</li><li>Plaza Kolbi</li><li>Plaza Old Navy</li></ul>'
    '<p class="nm-note" style="margin-top:12px">Plaza Cinemark y Plaza Kolbi retoman diseños de Escazú; Plaza Old Navy repite Plaza Honor.</p></div>'))

# ---------------------------------------------------------------- 02–04 concepto
eyebrow(CAMPANA, f"{n(2)} Campaña")
title(CAMPANA, "Una campaña, <em>un hilo dorado</em>")
para(CAMPANA, 0, "<p>Toda la decoración nace del universo de <em>Where the Magic Begins</em>. Los key visuals de la campaña y "
                 "los cascabeles dorados se repiten de la fachada a la última plaza, para que cada visitante reconozca la "
                 "misma historia en cada rincón de los dos centros.</p>")

eyebrow(LENGUAJE, f"{n(3)} Lenguaje de diseño")
para(LENGUAJE, 0, "<p>El sistema visual de la propuesta se apoya en <strong>cinco tonos en una proporción fija</strong> y "
                  "<strong>seis materiales que se reconocen antes de tocarlos</strong>: madera oscura, dorado antiguo, "
                  "terciopelo, piedra, metal bruñido y fibra natural.</p>")
credit(LENGUAJE, KARJIM)

eyebrow(LUZ, f"{n(4)} Sistema de iluminación")
title(LUZ, "Tres capas <em>de luz cálida</em>")
after(divider_of(LUZ), new_text_widget(
    "<p>La luz se construye en tres capas que se suman sin competir: una base ambiental que apenas se percibe, acentos "
    "puntuales que revelan cada pieza y el gesto espectacular de filamentos y cortinas LED en dorado.</p>",
    "elementor-widget__width-initial"))
credit(LUZ, KARJIM)

# ================================================================ PARTE I · ESCAZÚ
# Portadilla: a partir de la de Curridabat (fondo en video, lista de tres tarjetas).
ESCAZU = clone(CURRI, "escazu")
ESCAZU.find("video")["data-src"] = U + "nm26-fachada-esc-principal.mp4"
ESCAZU.find("video")["poster"] = U + "nm26-fachada-esc-principal-1024x682.jpg"
ESCAZU.find("video")["aria-label"] = "Fachada iluminada de Multiplaza Escazú: Fachada principal"
eyebrow(ESCAZU, "Parte I · Multiplaza Escazú")
title(ESCAZU, "Escazú: <em>donde empieza la magia</em>")
para(ESCAZU, 0, "<p>El recorrido arranca en Escazú y se cuenta en tres capas: las entradas que dan la bienvenida, las fachadas "
                "que convierten el edificio en un espectáculo de luz y una decoración interior que avanza por vacíos, "
                "pasillos y plazas hasta Plaza Honor.</p>")
set_html(ESCAZU.find("ul", class_="nm-mirror"), (
    '<li><b>Entradas</b>Entrada esquinera, puente del BCR y palmeras iluminadas en el acceso.</li>'
    '<li><b>Fachadas</b>Nueve animaciones de luz sobre el edificio real y dos frentes comerciales.</li>'
    '<li><b>Decoración interna</b>Vacíos, pasillos y plazas: diez zonas, del túnel de arcos a Plaza Honor.</li>'))
ESCAZU.find("ul", class_="nm-mirror")["class"] = ["nm-mirror"]
credit(ESCAZU, f"{MECA} · {KARJIM}")

# Entradas Escazú: a partir de la sección centrada de fachadas de Curridabat.
ENT_ESC = clone(FACH_CUR)
eyebrow(ENT_ESC, f"{n(5)} Escazú · Entradas")
title(ENT_ESC, "La bienvenida <em>empieza afuera</em>")
para(ENT_ESC, 0, "<p>Antes de cruzar la puerta, la Navidad ya recibe. La entrada esquinera y el puente del BCR se animan con "
                 "luz, y las palmeras del acceso se visten de luz cálida para marcar el camino hacia el interior.</p>")
grid = ENT_ESC.find("div", class_="nm-grid")
grid.clear()
grid["class"] = ["nm-grid", "g3"]
for f in (tile(FACH_ESC, "esquinera"), tile(FACH_ESC, "fachada-esc-bcr"), tile(VAC_ESC, "palmeras")):
    f["data-lb"] = "ent-esc"
    f["style"] = "--ar:4/3"
    grid.append(f)
grid.find_all("figcaption")[0].clear()
grid.find_all("figcaption")[0].append(BeautifulSoup("<b>Entrada esquinera</b>Escazú · animación de luz", "html.parser"))
grid.find_all("figcaption")[1].clear()
grid.find_all("figcaption")[1].append(BeautifulSoup("<b>Puente BCR</b>Escazú · acceso peatonal · animación de luz", "html.parser"))
grid.find_all("figcaption")[2].clear()
grid.find_all("figcaption")[2].append(BeautifulSoup("<b>Palmeras iluminadas</b>Escazú · acceso", "html.parser"))
credit(ENT_ESC, MECA)
# la galería de un solo elemento de las palmeras queda vacía en vacíos: se elimina
for g in VAC_ESC.find_all("div", class_="nm-grid"):
    if not g.find("figure"):
        g.find_parent(attrs={"data-widget_type": True}).decompose()

# Fachadas Escazú (sin las dos entradas, que ya tienen su sección)
eyebrow(FACH_ESC, f"{n(6)} Escazú · Fachadas")
title(FACH_ESC, "El edificio <em>se vuelve luz</em>")
para(FACH_ESC, 0, "<p>El proyecto de fachadas llega a su etapa final: todas las fachadas del centro comercial ya están "
                  "resueltas. Cada vista proyecta la animación de luz propuesta sobre la fotografía real del edificio, "
                  "para ver exactamente cómo se encenderá.</p>")
stats(FACH_ESC, [("9", "animaciones de fachada"), ("2", "renders de frentes comerciales")])
credit(FACH_ESC, MECA)

# Capítulo Decoración interna Escazú: a partir de «En cifras» (fondo desenfocado, texto centrado).
INT_ESC = clone(CIFRAS)
INT_ESC.find("img")["src"] = U + "nm26-plaza-brunos-render-1-1536x835.jpg"
INT_ESC.find("img")["alt"] = "Plaza Brunos: árbol de 7 metros con soldados y trineo"
eyebrow(INT_ESC, "Parte I · Decoración interna")
title(INT_ESC, "Adentro, <em>la magia se despliega</em>")
set_html([w for w in widgets(INT_ESC, "text-editor") if w.find("ul")][0],
         "<p>Diez zonas interiores, pensadas como una secuencia: cortinas de luz sobre los vacíos, un túnel de arcos que "
         "acompaña el pasillo, plazas con árbol, ball pit y carrusel, y un cierre bajo la cúpula de Plaza Honor.</p>")
widgets(INT_ESC, "text-editor")[-1]["class"] = ["elementor-element", "elementor-widget__width-initial", "nm-c",
                                                "elementor-widget", "elementor-widget-text-editor"]
after(widgets(INT_ESC, "text-editor")[-1], BeautifulSoup(
    '<div class="elementor-element elementor-widget elementor-widget-html" data-element_type="widget" data-widget_type="html.default">'
    '<ul class="nm-mirror img">'
    f'<li><div class="nm-ph"><img alt="Cortina de luz con esferas sobre el vacío" loading="lazy" src="{U}nm26-vacio-esc-esferas.jpg" width="1131" height="1391"/></div>'
    '<div class="tx"><b>Vacíos</b>Cortinas LED, esferas y adornos colgantes sobre los tragaluces.</div></li>'
    f'<li><div class="nm-ph"><img alt="Túnel de arcos con cascabeles" loading="lazy" src="{U}nm26-tunel-arcos-render-1-1536x1346.jpg" width="1536" height="1346"/></div>'
    '<div class="tx"><b>Pasillos</b>Túnel de arcos, Quinta Etapa, BCR – Vértigo y el pasillo hacia Plaza Tukis.</div></li>'
    f'<li><div class="nm-ph"><img alt="Plaza Honor con el árbol Gift of Joy y el tren navideño" loading="lazy" src="{U}nm26-plaza-honor-render-1536x1021.jpg" width="1538" height="1022"/></div>'
    '<div class="tx"><b>Plazas</b>Starbucks, Casa de Santa, Tukis, Brunos, Siman y Honor.</div></li></ul></div>', "html.parser").div)

eyebrow(VAC_ESC, f"{n(7)} Escazú · Vacíos")
title(VAC_ESC, "Luz que cae <em>desde los tragaluces</em>")
para(VAC_ESC, 0, "<p>Cortinas LED descienden sobre tragaluces y vacíos, acompañadas de esferas y adornos colgantes que llenan la "
                 "altura del edificio. Deslice sobre la primera imagen para comparar la cortina sola con la versión con adornos.</p>")
credit(VAC_ESC, MECA)

eyebrow(TUNEL, f"{n(8)} Escazú · Túnel de arcos")
title(TUNEL, "Túnel de arcos <em>y cascabeles</em>")
para(TUNEL, 0, "<p>Arcos de guirnalda con moños de terciopelo rojo y cascabeles dorados, sobre maceteros en Red Silk, forman un "
               "túnel que acompaña todo el pasillo. Una variante suma paneles de filigrana dorada iluminada para un efecto "
               "más envolvente.</p>")
credit(TUNEL, KARJIM)

eyebrow(STARBUCKS, f"{n(9)} Escazú · Plaza Starbucks")
title(STARBUCKS, "Un túnel de luz <em>hacia el árbol</em>")
para(STARBUCKS, 0, "<p>Los arcos de la plaza se convierten en un túnel de luz que guía, por ambos lados, hacia el túnel del "
                   "árbol Gift of Joy: un camino que invita a entrar y a quedarse.</p>")
credit(STARBUCKS, KARJIM)

eyebrow(SANTA, f"{n(10)} Escazú · Pasillo y Casa de Santa")
title(SANTA, "De Plaza Starbucks <em>a Plaza Tukis</em>")
para(SANTA, 0, "<p>Adornos colgantes rojos y dorados flotan entre cortinas de luz sobre el vacío del pasillo que une Plaza "
               "Starbucks con Plaza Tukis.</p>")
para(SANTA, 1, "<p><strong>Casa de Santa.</strong> Una cabaña de madera con guirnaldas, pensada como taller: madera, relojes, "
               "chimenea y detalles dorados que invitan a asomarse.</p>")
credit(SANTA, KARJIM)

eyebrow(TUKIS, f"{n(11)} Escazú · Plaza Tukis")
title(TUKIS, "Un ball pit <em>de 158 m²</em>")
para(TUKIS, 0, "<p>El corazón familiar del recorrido: un ball pit semicircular de 158 m² y una guirnalda que recorre todo el "
               "perímetro de la plaza, con luz blanco cálido y esferas plateadas y rojas de 7 cm.</p>")
credit(TUKIS, KARJIM)

eyebrow(BRUNOS, f"{n(12)} Escazú · Plaza Brunos")
title(BRUNOS, "Un árbol <em>de 7 metros</em>")
para(BRUNOS, 0, "<p>La pieza central de Escazú: un árbol de 7 metros en blanco y rojo sobre una tarima verde oscuro con el logo "
                "de kölbi, rodeado de soldados, regalos, escaleras espejadas, árboles de ambientación, un trineo y bancas "
                "modernas.</p>")
credit(BRUNOS, KARJIM)

eyebrow(BRUNOS2, f"{n(13)} Escazú · Plaza Brunos, en detalle")
title(BRUNOS2, "Soldados, trineo <em>y stand kölbi</em>")
after(divider_of(BRUNOS2), new_text_widget(
    "<p>Cada pieza del montaje vista de cerca: el trineo plateado, el stand, los soldados con regalos y las bancas de fibra "
    "de vidrio, junto a las referencias que inspiran la escena.</p>", "elementor-widget__width-initial nm-c"))
credit(BRUNOS2, KARJIM)

eyebrow(QUINTA, f"{n(14)} Escazú · Pasillo Quinta Etapa")
title(QUINTA, "Copos de papel <em>sobre el pasillo</em>")
para(QUINTA, 0, "<p>Guirnaldas de copos de papel blanco con bordes dorado champán, suspendidas entre cortinas de luz a lo largo "
                "del pasillo. Es la opción 1; la alternativa queda abierta para definirla juntos.</p>")
credit(QUINTA, KARJIM)

eyebrow(SIMAN, f"{n(15)} Escazú · Plaza Siman")
title(SIMAN, "Carrusel dorado <em>y renos</em>")
para(SIMAN, 0, "<p>Un árbol dentro de un carrusel dorado sobre base roja BAC, rodeado de árboles iluminados, renos dorados "
               "facetados y una banca dorada: una escena hecha para fotografiarse.</p>")
credit(SIMAN, KARJIM)

eyebrow(HONOR, f"{n(16)} Escazú · Pasillo BCR – Vértigo y Plaza Honor")
title(HONOR, "Adornos suspendidos <em>y un tren navideño</em>")
para(HONOR, 0, "<p><strong>Plaza Honor.</strong> El árbol Gift of Joy, en rojo y dorado bajo la cúpula, cierra el recorrido de "
               "Escazú rodeado por un tren navideño. El mismo diseño se repite en Plaza Old Navy de Curridabat.</p>")
credit(HONOR, KARJIM)

# ================================================================ PARTE II · CURRIDABAT
eyebrow(CURRI, "Parte II · Multiplaza Curridabat")
title(CURRI, "Curridabat: <em>la misma magia, otro escenario</em>")
para(CURRI, 0, "<p>Curridabat sigue el mismo recorrido en tres capas y retoma lo mejor de Escazú: Plaza Cinemark y Plaza Kolbi "
               "repiten sus diseños y Plaza Old Navy espeja Plaza Honor. A ellas se suman Plaza Santo Katrin, el Pasillo "
               "Equiz – Vértigo y Plaza Reebok.</p>")
mirror_img = CURRI.find("ul", class_="nm-mirror").extract()      # las plazas espejo pasan al capítulo interior
set_html(CURRI.find_all(attrs={"data-widget_type": "html.default"})[-1], (
    '<ul class="nm-mirror">'
    '<li><b>Entradas</b>La entrada de H&amp;M y la entrada techada, animadas con luz.</li>'
    '<li><b>Fachadas</b>Cuatro animaciones: fachada principal, lateral y los frentes de Zara, Bershka, Pull&amp;Bear y Stradivarius.</li>'
    '<li><b>Decoración interna</b>Vacíos y food court, Santo Katrin, Equiz – Vértigo, Reebok y las tres plazas espejo.</li></ul>'))
credit(CURRI, f"{MECA} · {KARJIM}")

ENT_CUR = clone(FACH_CUR)
eyebrow(ENT_CUR, f"{n(17)} Curridabat · Entradas")
title(ENT_CUR, "Las entradas <em>reciben con luz</em>")
para(ENT_CUR, 0, "<p>La entrada de H&amp;M y la entrada techada se animan con la misma luz de las fachadas, para que la Navidad "
                 "reciba al visitante desde el primer paso.</p>")
grid = ENT_CUR.find("div", class_="nm-grid")
grid.clear()
grid["class"] = ["nm-grid", "g2"]
for f in (tile(FACH_CUR, "fachada-curri-hm"), tile(FACH_CUR, "fachada-curri-entrada")):
    f["data-lb"] = "ent-curri"
    grid.append(f)
credit(ENT_CUR, MECA)

eyebrow(FACH_CUR, f"{n(18)} Curridabat · Fachadas")
title(FACH_CUR, "La misma luz, <em>en Curridabat</em>")
para(FACH_CUR, 0, "<p>La estrategia de luz cruza la ciudad: la fachada principal, la lateral y los frentes de Zara, Bershka, "
                  "Pull&amp;Bear y Stradivarius se encienden con animaciones sobre la fotografía real del edificio.</p>")
FACH_CUR.find("div", class_="nm-grid")["class"] = ["nm-grid", "g4"]
credit(FACH_CUR, MECA)

INT_CUR = clone(CIFRAS)
INT_CUR.find("img")["src"] = U + "nm26-santo-katrin-render.jpg"
INT_CUR.find("img")["alt"] = "Plaza Santo Katrin: área de juego con esferas colgantes"
eyebrow(INT_CUR, "Parte II · Decoración interna")
title(INT_CUR, "Adentro, <em>Curridabat refleja Escazú</em>")
set_html([w for w in widgets(INT_CUR, "text-editor") if w.find("ul")][0],
         "<p>Siete zonas interiores: cortinas de luz en vacíos, pasillos y food court, un área de juego de 4 × 22 m, un cielo "
         "de cables de luz, árboles de espejo y tres plazas que retoman los diseños de Escazú.</p>")
widgets(INT_CUR, "text-editor")[-1]["class"] = ["elementor-element", "elementor-widget__width-initial", "nm-c",
                                                "elementor-widget", "elementor-widget-text-editor"]
mirror_w = BeautifulSoup('<div class="elementor-element elementor-widget elementor-widget-html" data-element_type="widget" '
                         'data-widget_type="html.default"></div>', "html.parser").div
mirror_w.append(mirror_img)
after(widgets(INT_CUR, "text-editor")[-1], mirror_w)
tx = mirror_img.find_all("div", class_="tx")
set_html(tx[0], "<b>Plaza Cinemark</b>Retoma Plaza Siman: árbol con carrusel BAC, renos dorados y banca dorada.")
set_html(tx[1], "<b>Plaza Kolbi</b>Retoma el montaje de Escazú con árboles de base espejada y logo kölbi.")
set_html(tx[2], "<b>Plaza Old Navy</b>Repite Plaza Honor: árbol Gift of Joy bajo la cúpula y tren navideño.")

eyebrow(VAC_CUR, f"{n(19)} Curridabat · Vacíos")
title(VAC_CUR, "Luz sobre pasillos <em>y food court</em>")
para(VAC_CUR, 0, "<p>Cortinas de luz en tragaluces, pasillos y food court, en dos versiones: cortina sola o con esferas "
                 "colgantes. Deslice sobre cada imagen para compararlas.</p>")
credit(VAC_CUR, MECA)

eyebrow(KATRIN, f"{n(20)} Curridabat · Plaza Santo Katrin")
title(KATRIN, "Área de juego <em>de 4 × 22 m</em>")
para(KATRIN, 0, "<p>Un área de juego lineal de 4 × 22 m con ball pit, toboganes y casitas en rojo y blanco, bajo un cielo de "
                "esferas rojas y plateadas.</p>")
credit(KATRIN, KARJIM)

eyebrow(EQUIZ, f"{n(21)} Curridabat · Pasillo Equiz – Vértigo")
title(EQUIZ, "Un cielo <em>de cables de luz</em>")
para(EQUIZ, 0, "<p>Diecinueve cables de luz cruzan el pasillo de lado a lado, con dos opciones de adorno colgante: cascabeles "
               "dorados o esferas rojas y blancas. Deslice sobre la imagen para comparar.</p>")
credit(EQUIZ, KARJIM)

eyebrow(REEBOK, f"{n(22)} Curridabat · Plaza Reebok")
title(REEBOK, "Árboles <em>de espejo</em>")
para(REEBOK, 0, "<p>Árboles de espejo sobre una estructura de borde cuadrado, con la base rellena de esferas de 20 cm y bancas "
                "modernas: reflejos que multiplican la luz de la plaza.</p>")
credit(REEBOK, KARJIM)

# ---------------------------------------------------------------- cierre
eyebrow(CIFRAS, f"{n(23)} En cifras")
stats(CIFRAS, [("158 m²", "de ball pit en Plaza Tukis"), ("7 m", "de altura del árbol de Plaza Brunos"),
               ("80", "extensiones de micro luces LED"), ("30", "regalos de 40 a 60 cm"),
               ("19", "cables de luz en el Pasillo Equiz – Vértigo"), ("17", "animaciones de luz en fachadas y entradas")])

eyebrow(CIERRE, f"{n(24)} Siguiente paso")
para(CIERRE, 0, "<p>Quedan por definir las opciones de cada zona: cortina sola o con esferas en los vacíos, cascabeles o esferas "
                "en el Pasillo Equiz – Vértigo y la alternativa de copos del Pasillo Quinta Etapa. Conversemos los "
                "siguientes pasos para encender la Navidad 2026.</p>")

for w in widgets(PIE, "text-editor"):
    if "nm-note" in w.get("class", []):
        set_html(w, '<p class="nm-note">Iluminación de fachadas, entradas y vacíos: La Meca Concept · Ambientación y decoración '
                    'interior: Karjim Design · Renders y fotografías de los proveedores · Multiplaza · Grupo Roble · Navidad 2026.</p>')

# ---------------------------------------------------------------- orden final
ORDER = [HERO, PROPUESTA, CAMPANA, LENGUAJE, LUZ,
         ESCAZU, ENT_ESC, FACH_ESC, INT_ESC, VAC_ESC, TUNEL, STARBUCKS, SANTA, TUKIS, BRUNOS, BRUNOS2, QUINTA, SIMAN, HONOR,
         CURRI, ENT_CUR, FACH_CUR, INT_CUR, VAC_CUR, KATRIN, EQUIZ, REEBOK,
         CIFRAS, CIERRE, PIE]
for sec in S:
    sec.extract()
for sec in ORDER:
    root.append(sec)

# Fondos claros alternados (marfil / blanco) los asigna rebuild_v4 por orden; nada que hacer aquí.
OUT.write_text(str(soup), encoding="utf-8")
print("ok", OUT.name, len(ORDER), "secciones")
