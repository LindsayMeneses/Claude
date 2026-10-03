# Portada con Slider Revolution · guía de construcción

La portada de la v6 está hoy en la plantilla **168** con el widget *Slides* de Elementor Pro (8 diapositivas,
Ken Burns, fundido de 1,4 s). Slider Revolution 7.2.1 está instalado pero **no tiene API de escritura**: sus rutas
REST (`/wp-json/sliderrevolution/...`) solo leen, y la importación (`.zip`) se hace desde el panel. Por eso el
slider se arma una vez en el panel con esta guía; después el cambio en la página es automático.

## 1. Crear el módulo

Slider Revolution → **New Blank Module**.

| Ajuste | Valor |
|---|---|
| Title | Navidad Multiplaza 2026 |
| **Alias** | `navidad-multiplaza-2026` (exacto: es lo que usa el shortcode) |
| Layout | Full Screen · Layers Grid 1240 × 868 (desktop), 1024, 778, 480 |
| Background | #0A241C (Noche Bosque) |
| Slide duration | 7000 ms · Loop · Pause on hover · Stop on first interaction: off |
| Progress bar | Top, 2 px, color #C9A45C a 60 % |
| Navigation | Arrows *Hesperiden* color #EBD9AE · Bullets *Hermes* horizontal, 22 × 2 px, color #C9A45C |
| Parallax / 3D | Mouse parallax ON, niveles 5–10–15 (fondo, foto, textos) |
| Lazy load | Smart |

## 2. Las 8 diapositivas

Imágenes de la biblioteca de Medios (prefijo `nm26-`). Todas con **Ken Burns** (escala 100 → 112 %, 9 s, easing
Power1.easeInOut) y una **capa de sombra** (shape full-size, degradado 180° de `rgba(7,24,18,0)` 25 % a
`rgba(7,24,18,.78)`) encima del fondo. Las transiciones alternan **Fade** (1400 ms) y **Slot Zoom Fade** (1200 ms).

| # | Fondo (Medios) | Título | Texto | Botón → ancla |
|---|---|---|---|---|
| 1 | nm26-fachada-esc-principal.jpg (o el `.mp4` como video de fondo, mudo, en bucle) | Where the Magic Begins | Navidad 2026 · Multiplaza Escazú y Multiplaza Curridabat. Un recorrido en tres capas: entradas, fachadas y decoración interna. | Recorrer Escazú → `#escazu` |
| 2 | nm26-tunel-arcos-render-1.jpg | Un túnel de arcos y cascabeles | Arcos de guirnalda, moños de terciopelo y cascabeles dorados acompañan todo el pasillo de Escazú. | Ver el túnel → `#arcos` |
| 3 | nm26-plaza-starbucks-render.jpg | Un túnel de luz hacia el árbol | Plaza Starbucks: los arcos guían, por ambos lados, hasta el árbol Gift of Joy. | Ver Plaza Starbucks → `#starbucks` |
| 4 | nm26-plaza-brunos-render-1.jpg | Un árbol de 7 metros | Plaza Brunos: soldados, regalos, trineo y escaleras espejadas alrededor del árbol kölbi. | Ver Plaza Brunos → `#brunos` |
| 5 | nm26-plaza-siman-render-1.jpg | Carrusel dorado y renos | Plaza Siman: un árbol dentro de un carrusel dorado sobre base roja BAC. | Ver Plaza Siman → `#siman` |
| 6 | nm26-fachada-curri-principal.jpg (o `.mp4`) | Curridabat: la misma magia, otro escenario | Entradas, fachadas y plazas que retoman lo mejor de Escazú. | Ir a Curridabat → `#curridabat` |
| 7 | nm26-santo-katrin-render.jpg | Un área de juego de 4 × 22 m | Plaza Santo Katrin: ball pit, toboganes y casitas bajo un cielo de esferas. | Ver Santo Katrin → `#katrin` |
| 8 | nm26-plaza-reebok-render.jpg | Árboles de espejo | Plaza Reebok: reflejos que multiplican la luz de la plaza. | Ver Plaza Reebok → `#reebok` |

## 3. Capas de cada diapositiva (iguales en las 8; se copian con *Duplicate slide*)

Alineadas a la izquierda, bloque de 760 px de ancho, margen izquierdo 120 px (24 px en móvil).

| Capa | Estilo | Animación de entrada | Salida |
|---|---|---|---|
| **Antetítulo** «Navidad 2026 · Multiplaza» | Manrope 600 · 11 px · espaciado 0,3 em · mayúsculas · #C9A45C | *Fade in from left* 900 ms, inicio 300 ms, desenfoque 6 px → 0 | Fade out 500 ms |
| **Título** (texto de la tabla) | Fraunces 300 itálica · 84 px (60 tablet, 40 móvil) · interlineado 1,02 · #FFFFFF | *Split by words* (mask bottom), 1100 ms, retardo 40 ms entre palabras, inicio 600 ms, easing Power3.easeOut | Fade + 20 px abajo, 600 ms |
| **Filete** (shape 72 × 1 px, #C9A45C) | — | *Scale X* 0 → 1 desde la izquierda, 900 ms, inicio 1300 ms | Fade out |
| **Texto** | Manrope 400 · 19 px (16 móvil) · interlineado 1,65 · #EBD9AE | *Fade in from bottom* 20 px, 1000 ms, inicio 1500 ms | Fade out |
| **Botón** | Manrope 600 · 13 px · espaciado 0,2 em · mayúsculas · fondo #C9A45C · texto #0A241C · sin radio · 54 px de alto · padding 0 32 px · hover: fondo #EBD9AE | *Fade in from bottom* 14 px, 900 ms, inicio 1900 ms | Fade out |
| **Contador** «01 / 08» (esquina inferior derecha) | Fraunces 400 · 22 px · #EBD9AE | Fade in 800 ms, inicio 2200 ms | — |
| **Partículas** (add-on Particle Effects, solo diapositivas 1 y 6) | 60 partículas, color #EBD9AE, opacidad 0,35, tamaño 1–3 px, velocidad 0,6, dirección arriba | — | — |

El botón enlaza al ancla con *Scroll below slider* desactivado y *Action: Scroll to ID* (misma pestaña). Las anclas
existen en la página: `escazu`, `arcos`, `starbucks`, `brunos`, `siman`, `curridabat`, `katrin`, `reebok`.

## 4. Conectarlo a la página

1. Publicar el módulo (Save → el shortcode será `[rev_slider alias="navidad-multiplaza-2026"]`).
2. Regenerar la portada con el shortcode y publicar la plantilla 168:

```
python3 v6.py --revslider          # tpl-portada.json pasa a un widget Shortcode con el slider
```

Subir `tpl-portada.json` al meta `_elementor_data` de la plantilla **168** (igual que el resto, por la API REST)
y limpiar la caché de Elementor (`DELETE elementor/v1/cache`). La clase `nm-rev` ya tiene estilos (altura
mínima 100 svh) en la plantilla de código 162.

Si en algún momento se prefiere volver al widget Slides de Pro, basta `python3 v6.py` sin la opción y republicar 168.

## 5. Exportar como respaldo

Con el módulo listo: Slider Revolution → módulo → **Export** (incluye imágenes). Guardar el `.zip` en
`navidad-multiplaza/revslider/` (no se sube al repo por tamaño; se anota la fecha aquí).
