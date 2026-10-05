# lindsaymeneses.com — sitio de Lindsay Meneses

Portada con el perfil profesional de Lindsay y un menú hamburguesa donde cada proyecto es su propia
landing. Todo se construye con Elementor (contenedores y widgets nativos + un widget HTML con el
CSS/JS compartido). Las animaciones están inspiradas en las páginas de producto de Apple y ASUS:
secciones fijadas que avanzan con el scroll, texto que se ilumina palabra por palabra, carrusel
horizontal, línea de tiempo que se dibuja y entradas suaves con desenfoque. Todo respeta
`prefers-reduced-motion`.

| Página | ID | URL |
|---|---|---|
| Inicio (portada) | 159 | https://lindsaymeneses.com/ |
| Proyectos | 158 | https://lindsaymeneses.com/proyectos/ |
| Navidad Multiplaza 2026 | 7 | https://lindsaymeneses.com/proyectos/navidad-multiplaza-2026/ |

Las tres usan la plantilla **Elementor Canvas**. La portada se fija en Ajustes → Lectura
(`show_on_front=page`, `page_on_front=159`).

## Archivos

- `sitio.py` genera `out/inicio.json` y `out/proyectos.json` (datos de Elementor). Exporta
  `shell_markup()`, que también usa `navidad-multiplaza/build_template.py`.
- `shell.css` / `shell.js`: barra, menú, motor de scroll (`.lx-pin`, `.lx-words`, `.lx-hpin`,
  `.lx-tl`) y entradas (`.lx-rv`). Se incrustan comprimidos en el primer widget HTML de cada página.
- `ids.json`: IDs de las páginas en WordPress.
- `FUENTES.md`: de dónde sale cada dato público de Lindsay.

## Publicar

1. `python3 sitio.py` (y `python3 ../navidad-multiplaza/build_template.py --page` si cambió el menú).
2. Enviar cada JSON como meta `_elementor_data` con `POST wp/v2/pages/<ID>`.
3. Comprobar que el meta devuelto es idéntico al archivo local.
4. `DELETE elementor/v1/cache`. Responde con texto plano; eso es normal.

## Agregar un proyecto nuevo

1. Crear la landing en Elementor como **página hija de «Proyectos» (158)**, con plantilla Canvas.
   El menú la muestra sola, porque lee `/wp-json/wp/v2/pages?parent=158` (se ordena por «Orden»).
2. Incluir `shell_markup()` en su primer widget HTML para que tenga la barra y el menú.
3. En `PROYECTOS` de `sitio.py`, poner su `url` para que la tarjeta muestre «Ver proyecto», y
   volver a publicar Inicio y Proyectos.

## Pendiente

- [ ] Foto profesional de Lindsay para el perfil.
- [ ] Confirmar la participación de Lindsay en Elf Christmas 2021 y Christmas Around the World 2022.
- [ ] Landings de El Regalo de Dar, Dragones y dinosaurios, Christmas Around the World y Elf
      Christmas (hoy aparecen como «Caso en preparación»).
- [ ] Videos de 6 s con IA: requieren claves de API (ver `navidad-multiplaza/VIDEOS-IA.md`).
