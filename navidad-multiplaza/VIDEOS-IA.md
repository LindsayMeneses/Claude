# Clips de 6 s con IA · Navidad Multiplaza 2026

La página ya está lista para reproducirlos: cada clip entra en fundido sobre la foto de su sección, en
silencio y en bucle; se carga solo al acercarse y se pausa fuera de pantalla. Con «reducir movimiento»
activado se sigue viendo la foto.

## Especificación común

- 6 s · 16:9 · 1080p · 24 fps · **sin audio** · sin texto, logos ni personas reconocibles.
- Movimiento lento y continuo (se reproduce en bucle): sin cortes ni cambios de plano.
- Estilo único para todas: lujo sobrio, luz cálida, poca profundidad de campo, bokeh suave.
- Modo recomendado: **imagen a video**, usando como referencia la foto que ya está en la página;
  así el clip coincide con la foto sobre la que aparece.
- Modelo sugerido: Seedance 2.0 (fal.ai) o Veo 3.1 (Gemini API / HeyGen).

Sufijo de estilo para añadir a cada prompt:

> Luxury holiday campaign, cinematic, warm champagne-gold light, shallow depth of field, soft bokeh,
> slow smooth camera motion, seamless loop, no text, no logos, no people, 16:9, 6 seconds.

## Los 6 clips

| # | Sección (clave) | Foto de referencia | Prompt |
|---|---|---|---|
| 1 | Portada (`portada`) | `nm-rojo-dorado-2048x1152.jpg` | Extreme close-up of glossy red and gold Christmas baubles hanging on a fresh pine branch; the camera drifts slowly to the right while the ornaments sway almost imperceptibly and warm light glints across their surface; out-of-focus golden lights pulse gently in the background. |
| 2 | Plaza Starbucks (`luces`) | `nm-c13.jpg` | Slow forward dolly through an elegant tunnel of arches wrapped in thousands of warm-white micro LED lights, leading toward a tall illuminated Christmas tree at the end; lights twinkle softly, evening in an upscale open-air shopping plaza. |
| 3 | Plaza Brunos (`arbol`) | `nm-c12.jpg` | Low-angle slow crane up a monumental 7-metre Christmas tree decorated in white and red, standing among tropical palm trees at dusk; a white-and-silver sleigh and giant gift boxes at its base; the tree lights fade on gradually. |
| 4 | Curridabat (`pino`) | `nm-c05-2048x1365.jpg` | Looking up at a canopy of warm light strings stretched across an elegant plaza between building facades, forming a soft grid; the strands sway very gently and the bulbs twinkle against a deep blue evening sky. |
| 5 | Plaza Reebok (`copo`) | `nm-c06-2048x1356.jpg` | Mirrored Christmas trees on a square base filled with silver spheres; the camera orbits slowly and reflections of warm lights slide across the mirrored surfaces; dark, refined background. |
| 6 | Cierre (`chispa`) | `nm-c01-2048x1365.jpg` | A single sparkler ignites and burns in slow motion in the foreground, golden sparks drifting into a dark warm bokeh background; calm and celebratory. |

Opcional: el fondo de «En cifras» reutiliza el clip 2 con desenfoque; no hace falta otro.

## Cómo se integran

1. Generar cada clip y subirlo a Medios (`web_upload_media` desde la URL del resultado); nombre
   `nm-vid-<clave>.mp4`, idealmente de menos de 4 MB (H.264, 1080p o 1280 px de ancho).
2. Añadir la URL en `VIDEOS` dentro de `build_template.py`, por ejemplo
   `VIDEOS = {"portada": "https://lindsaymeneses.com/wp-content/uploads/2026/09/nm-vid-portada.mp4"}`.
3. `python3 build_template.py --page`, publicar el meta `_elementor_data` y limpiar la caché de Elementor.

## Requisitos para generarlos desde esta sesión

- Una clave de API en el entorno: `FAL_KEY` (fal.ai, Seedance/Kling/Veo), `HEYGEN_API_KEY` (HeyGen) o
  `GEMINI_API_KEY` (Veo en la Gemini API).
- Para fal.ai o HeyGen, además, permitir en la red del entorno `queue.fal.run` / `fal.media` o
  `api.heygen.com` / `resource.heygen.ai`. La Gemini API (`generativelanguage.googleapis.com`) ya
  responde desde aquí.
