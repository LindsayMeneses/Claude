# Navidad Multiplaza 2026 — página Elementor

Sitio: lindsaymeneses.com · Elementor 4.3.2 instalado y activo.

## Sistema de diseño

**Colores globales** (Elementor → Ajustes del sitio → Colores globales)

| Nombre         | ID          | Hex       | Estado            |
|----------------|-------------|-----------|-------------------|
| Verde Pino     | `primary`   | `#0F3B2E` | ✅ aplicado        |
| Rojo Navidad   | `secondary` | `#B3122E` | ✅ aplicado        |
| Texto Carbón   | `text`      | `#1E2A25` | ✅ aplicado        |
| Dorado Champán | `accent`    | `#C9A45C` | ✅ aplicado        |
| Marfil         | `marfil`    | `#FBF6EC` | ✅ aplicado        |
| Noche Bosque   | `noche`     | `#0A241C` | ✅ aplicado        |
| Rojo Vino      | `vino`      | `#7A0C21` | ✅ aplicado        |
| Oro Claro      | `oroclaro`  | `#EBD9AE` | ✅ aplicado        |
| Blanco Nieve   | `blanco`    | `#FFFFFF` | ✅ aplicado        |
| Salvia Suave   | `salvia`    | `#E4ECE6` | ✅ aplicado        |

**Tipografía global** (✅ aplicada)

| ID          | Uso                     | Fuente                          |
|-------------|-------------------------|---------------------------------|
| `primary`   | Títulos                 | Fraunces 600, 1.1, -0.01em      |
| `secondary` | Subtítulos / tarjetas   | Fraunces 500 itálica, 24px      |
| `text`      | Párrafos                | Manrope 400, 17px, 1.65         |
| `accent`    | Etiquetas y botones     | Manrope 600, 13px, mayúsculas, 0.2em |

## Estructura v5 · la presentación por partes (02-10-2026)

Fuente: `fuente_v5.py` parte del HTML de la v4 (`respaldo/pagina7-2026-09-28-2218.html`), reescribe los textos
con un tono más actual (los datos del deck se conservan tal cual) y reorganiza las 30 secciones en partes:

| # | Sección | Fondo |
|---|---|---|
| — | Portada «Where the Magic Begins» · botones «Recorrer Escazú» y «Ir a Curridabat» | video |
| 01–04 | La propuesta (índice de las tres capas y de cada centro) · Campaña · Lenguaje de diseño · Sistema de iluminación | |
| **Parte I** | **Multiplaza Escazú** · portadilla con las tres capas | video fachada |
| 05 | Escazú · Entradas: entrada esquinera, puente BCR y palmeras del acceso | oscuro |
| 06 | Escazú · Fachadas: 9 animaciones + 2 renders | oscuro |
| **Parte I** | **Decoración interna** · capítulo (vacíos, pasillos, plazas) | render |
| 07–16 | Vacíos · Túnel de arcos · Plaza Starbucks · Pasillo y Casa de Santa · Plaza Tukis · Plaza Brunos (2) · Pasillo Quinta Etapa · Plaza Siman · Pasillo BCR – Vértigo y Plaza Honor | alternado |
| **Parte II** | **Multiplaza Curridabat** · portadilla con las tres capas | video fachada |
| 17 | Curridabat · Entradas: entrada H&M y entrada techada | oscuro |
| 18 | Curridabat · Fachadas: principal, lateral, esquina Zara y frentes Zara · Bershka · Pull&Bear · Stradivarius | oscuro |
| **Parte II** | **Decoración interna** · capítulo con las tres plazas espejo (Cinemark, Kolbi, Old Navy) | render |
| 19–22 | Vacíos y food court · Plaza Santo Katrin · Pasillo Equiz – Vértigo · Plaza Reebok | alternado |
| 23–24 | En cifras · Siguiente paso (formulario) · pie | |

Las entradas se sacaron de las galerías de fachadas (y las palmeras, de los vacíos de Escazú); los videos de
fachada y los renders son los mismos `nm26-*` de la v4. Las portadillas se clonan de la sección de Curridabat
de la v4 y los capítulos, de «En cifras».

**Publicada el 02-10-2026** (página 7 y plantilla 163 por la API REST; la plantilla 162 no cambió). Los JSON exactos
que se publicaron están en `publicar/` (`v5-pagina7.json`, `v5-tpl163.json`, `v5-tpl162.json`).

Regenerar y publicar (igual que la v4, con la fuente v5):

```
python3 fuente_v5.py                 # -> fuente-v5.html (no se sube al repo)
python3 rebuild_v4.py fuente-v5.html # -> page-elementor-data.json (7), tpl-codigo.json (162), tpl-parte2.json (163)
```

`rebuild_v4.py` reparte las 30 secciones entre la página y la plantilla «Segunda parte» buscando que pesen
parecido (~100 KB cada una). Sin argumento sigue reconstruyendo la v4 desde el respaldo.

Vista previa local sin acceso al sitio (fotos sustituidas por marcadores):
`python3 -c "import sys,json; sys.argv=['x','fuente-v5.html']; import rebuild_v4 as r; json.dump(r.build(), open('preview/all.json','w'), ensure_ascii=False)"`
→ `python3 preview.py preview/all.json index.html && NODE_PATH=$(npm root -g) node preview-shots.js`.

## Estructura de la página (v3 · línea editorial con fotografía)

Contenido real del deck (ver `ANALISIS-PPT.md`); textos en `copy.json`, estilos y recorrido en `fx/`.

1. Portada: foto a sangre, titular «La Navidad se enciende plaza a plaza», 3 datos, 2 botones alineados
2. El recorrido: índice de las 15 zonas (10 en Escazú, 5 en Curridabat)
3. Fachadas e identidad: foto enmarcada (cascabeles) + paleta del deck (Red Silk 351516)
4. Plaza Starbucks: túnel de luz hacia el árbol (foto a sangre)
5. Zona familiar: Casa de Santa y Plaza Tukis (ball pit 158 m², guirnalda, esferas 7 cm)
6. Plaza Brunos: árbol de 7 m, trineo, soldados, regalos (ficha completa de piezas)
7. Pasillos y plazas de Escazú: Quinta Etapa, Siman, BCR – Vértigo, Honor
8. Curridabat: plazas espejo y cielo de cables de Santo Katrin (4 × 22 m, 19 cables)
9. Plaza Reebok: árboles de espejo
10. En cifras: 6 datos del deck sobre luces desenfocadas
11. Cierre: «Encendamos juntos la Navidad 2026» + botón Conversemos (mailto)

**Línea gráfica:** Fraunces en peso ligero con cursiva dorada, etiquetas Manrope espaciadas con filete,
alternancia marfil / blanco / noche, fotos con filete dorado desplazado, botones rectos de igual altura.

**Animaciones (sutiles):** cada elemento aparece con fundido y un leve desenfoque que se aclara; las fotos
entran desenfocadas y enfocan, luego derivan muy despacio (Ken Burns); bokeh cálido flotante y nieve suave
en la portada; sin «clic en cualquier parte». Respeta «reducir movimiento».

**Fotos:** CC0 (Unsplash vía Wikimedia Commons) subidas a Medios (`nm-*.jpg`, IDs 9, 10, 14–17, 19, 21,
23, 24, 26, 27). Son de referencia: se pueden cambiar por renders del PPT exportados como imagen editando
`FOTOS` en `build_template.py`.

Regenerar: `python3 build_template.py --page` → publicar `page-elementor-data.json` en el meta
`_elementor_data` de la página 7 y limpiar caché (`DELETE elementor/v1/cache`).
Vista previa local: `python3 preview.py && NODE_PATH=$(npm root -g) node preview-shots.js`.

## Página publicada (v4, reconstruida)

- https://lindsaymeneses.com/proyectos/navidad-multiplaza-2026/ — página ID 7, hija de «Proyectos» (158), Canvas.
- **v4 (29-09-2026):** reconstrucción de la versión completa del 28-09 (22:18), que se había sobrescrito.
  Se armó desde `respaldo/pagina7-2026-09-28-2218.html` con `rebuild_v4.py`: los mismos textos, renders
  `nm26-*`, 17 videos de fachadas, lightbox y comparadores. Mejoras con Elementor Pro: formulario de
  contacto, efecto de movimiento en las fotos grandes, botones nativos y el menú del sitio.
- Está repartida en tres documentos de Elementor (cada uno se publica y verifica por separado):
  | Documento | ID | Contenido |
  |---|---|---|
  | Página «Navidad Multiplaza 2026» | 7 | Portada y secciones 01–11; incluye las dos plantillas |
  | Plantilla «Código (CSS, JS y menú)» | 162 | Estilos, recorrido, lightbox, videos y menú del sitio |
  | Plantilla «Segunda parte» | 163 | Secciones 12–23, cierre con formulario y pie |
  Las plantillas se editan en Elementor → Plantillas → Plantillas guardadas.
- La página tiene CSS personalizado (Ajustes de página → CSS personalizado) para el título de portada.
- Publicar: `python3 rebuild_v4.py` → subir `tpl-codigo.json` (162), `tpl-parte2.json` (163) y
  `page-elementor-data.json` (7) → verificar cada uno → `DELETE elementor/v1/cache` (si no, WordPress
  sigue mostrando la versión anterior).
- **Antes de publicar, comprobar la fecha de modificación de la página 7:** si cambió desde la última
  publicación propia, otra sesión trabajó en ella y hay que revisar antes de sobrescribir.
- `build_template.py` genera la v3 (fotos de referencia); ya no es la versión publicada.

## Pendiente

- [x] Colores globales (10) y tipografías globales (Fraunces + Manrope)
- [x] Crear la página con textos provisionales
- [ ] Subir el PPT a cPanel y extraerlo en `public_html/deck-navidad/` (al 2026-09-25 no existía
      ni `deck-navidad/` ni `deck-navidad.zip`)
- [ ] Leer textos y tema del PPT, reemplazar los [PPT] (texto provisional en la fuente),
      subir las imágenes a Medios y cambiar los paneles decorativos por widgets de imagen
- [x] Botón «Conversemos» abre un correo a contacto@lindsaymeneses.com
- [ ] Ponerla como portada (opcional, confirmar con la usuaria)
- [ ] Limpieza cuando ya se haya usado el PPT: borrar `deck-navidad.zip`, `deck-navidad/`,
      `cw-runner-7f3k9q.php`, `fase1-instalar-y-extraer.php`
