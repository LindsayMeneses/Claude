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
| Rojo Vino      | `vino`      | `#7A0C21` | ⚠️ sin confirmar   |
| Oro Claro      | `oroclaro`  | `#EBD9AE` | ⚠️ sin confirmar   |
| Blanco Nieve   | `blanco`    | `#FFFFFF` | ⏳ pendiente       |
| Salvia Suave   | `salvia`    | `#E4ECE6` | ⏳ pendiente       |

**Tipografía global** (⏳ pendiente — sigue en Roboto)

| ID          | Uso                     | Fuente                          |
|-------------|-------------------------|---------------------------------|
| `primary`   | Títulos                 | Fraunces 600                    |
| `secondary` | Subtítulos / tarjetas   | Fraunces 500 itálica            |
| `text`      | Párrafos                | Manrope 400, 17px, 1.65         |
| `accent`    | Etiquetas y botones     | Manrope 600, mayúsculas, 0.2em  |

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

Regenerar: `python3 build_template.py`

## Pendiente

- [ ] Reconectar el conector `web` (se cayó la sesión MCP) → terminar los colores y las tipografías
- [ ] Extraer el PPT en cPanel → `public_html/deck-navidad/`
- [ ] Leer textos y tema del PPT, reemplazar los [PPT], subir las imágenes a Medios
- [ ] Crear la página con la plantilla (API `elementor/v1/template-library/templates` o
      importando el JSON en Elementor → Plantillas → Importar)
- [ ] Ponerla como portada (opcional)
- [ ] Limpieza: borrar `deck-navidad.zip`, `deck-navidad/`, `cw-runner-7f3k9q.php`,
      `fase1-instalar-y-extraer.php`
