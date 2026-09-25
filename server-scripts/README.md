# Presentaciones web con Elementor — plan de trabajo

Sitio: **lindsaymeneses.com** (WordPress limpio, tema Twenty Twenty-Five).
Objetivo: cada presentación (empezando por **Navidad Multiplaza 2026**)
tendrá su propia página, construida con **Elementor**.

## Importante: reparto de tareas

La capa de seguridad de la plataforma **no permite** que el asistente
ejecute código PHP en el servidor ni cree archivos ejecutables (es el
patrón de los ataques web). Por eso:

- **Tú** haces 2 acciones de UI (instalar Elementor y extraer el material).
- **Claude** hace todo el diseño: paleta, tipografía, copywriting mejorado,
  maquetación, y entrega una **plantilla Elementor importable (JSON)** —
  que son *datos*, no código, así que es seguro.

## Paso 1 (tú) — Instalar Elementor
WordPress → Escritorio → **Plugins → Añadir nuevo** → busca *Elementor* →
**Instalar** → **Activar**. (2 minutos, sin código.)

## Paso 2 (tú) — Dejar el material accesible
En cPanel → **Administrador de archivos**:
1. Entra a `Archivos de proyectos` y **copia** `100 Navidad Multiplaza 2026 VF .pptx`
   a `public_html/`.
2. Renombra la copia a `deck-navidad.zip`.
3. Selecciónala → **Extract / Extraer** → dentro de `public_html/deck-navidad/`.

Esto deja disponibles:
- Textos de cada diapositiva → `public_html/deck-navidad/ppt/slides/*.xml`
- Imágenes → URLs públicas tipo
  `https://lindsaymeneses.com/deck-navidad/ppt/media/imageN.jpg`
- Colores/tipografía del tema → `ppt/theme/theme1.xml`

## Paso 3 (Claude)
Con eso, Claude lee los textos y colores reales, referencia las imágenes,
mejora el copy en tono de la **campaña de Navidad de Multiplaza**, y crea
la plantilla de la página lista para importar en Elementor.

---
*Nota:* si prefieres, en vez del Paso 2 puedes pegarme los textos y subir
las imágenes a la Biblioteca de medios; también funciona.
