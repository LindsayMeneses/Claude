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

## Estructura de la página (`navidad-multiplaza-elementor.json`)

1. Portada: pantalla completa, degradado noche → pino, 2 botones
2. Concepto: gran idea + key visual
3. Objetivos: 3 tarjetas con ícono
4. Experiencias: 4 tarjetas con imagen
5. Decoración: texto + mosaico de 4 imágenes
6. Calendario: 4 fases (nov → ene)
7. Cifras: contadores animados
8. Cierre: fondo vino + llamado a la acción

Plantilla "Elementor Canvas" (sin cabecera ni pie del tema), animaciones de entrada y
tamaños adaptados a tableta y celular. Los textos marcados **[PPT]** se reemplazan con
el contenido real del deck; las imágenes están vacías hasta subir las del PPT.

Regenerar: `python3 build_template.py` (JSON importable, con marcas [PPT] e imágenes vacías)
y `python3 build_template.py --page` (datos para la página publicada: sin marcas [PPT] y con
paneles decorativos degradado + ícono dorado en lugar de las imágenes que aún no existen).

## Página publicada

- https://lindsaymeneses.com/navidad-multiplaza-2026/ — página ID 7, plantilla Elementor Canvas.
- Se creó vía `wp/v2/pages` con el meta `_elementor_data` (contenido de `page-elementor-data.json`).
- No es la portada todavía.

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
