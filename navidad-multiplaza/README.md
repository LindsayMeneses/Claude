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

## Página publicada

- https://lindsaymeneses.com/navidad-multiplaza-2026/ — página ID 7, plantilla Elementor Canvas.
- Se creó vía `wp/v2/pages` con el meta `_elementor_data` (contenido de `page-elementor-data.json`).
- 2026-09-25: publicada la **v3** (fotografía, contenido del deck, animaciones sutiles); antes, la v2 (recorrido guiado). Verificado: el meta devuelto por la API es
  idéntico a `page-elementor-data.json`, se limpió el caché de Elementor y el HTML renderizado
  contiene «Luces de», `nm-slide` y el `mailto:` de contacto.
- No es la portada todavía.
- Análisis del PPT y cambios sugeridos: `ANALISIS-PPT.md`.

## Pendiente

- [x] Colores globales (10) y tipografías globales (Fraunces + Manrope)
- [x] Crear la página con textos provisionales
- [ ] Subir el PPT a cPanel y extraerlo en `public_html/deck-navidad/` (al 2026-09-25 no existía
      ni `deck-navidad/` ni `deck-navidad.zip`)
- [ ] Leer textos y tema del PPT, reemplazar los [PPT] (texto provisional en la fuente),
      subir las imágenes a Medios y cambiar los paneles decorativos por widgets de imagen
- [ ] Botón «Conversemos» apunta a `#contacto`, que aún no existe (agregar sección o enlace)
- [ ] Ponerla como portada (opcional, confirmar con la usuaria)
- [ ] Limpieza cuando ya se haya usado el PPT: borrar `deck-navidad.zip`, `deck-navidad/`,
      `cw-runner-7f3k9q.php`, `fase1-instalar-y-extraer.php`
