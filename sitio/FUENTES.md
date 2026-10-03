# Landing Lindsay Meneses — fuentes y publicación

## Datos usados (solo información pública)

| Dato | Fuente |
|---|---|
| Jefa de Mercadeo y Publicidad, Grupo Roble (Multiplaza Escazú y Curridabat), San José | [LinkedIn](https://www.linkedin.com/in/lindsay-meneses-cambronero-3b424420/), [LinkedIn (Multiplaza Escazú)](https://www.linkedin.com/in/lindsay-lindsay-meneses-9b43b077/) |
| Más de 10 años en mercadeo y publicidad | LinkedIn (resumen en buscadores) |
| Máster en Marketing, Marketing Digital y Redes Sociales, IM Digital Business School (2019–2022) | LinkedIn / RocketReach |
| Administración de Empresas, Universidad Hispanoamericana | LinkedIn / RocketReach |
| Funciones: eventos, estrategias de mercadeo y publicidad, clientes y presupuestos, tráfico del centro comercial | LinkedIn (Multiplaza Escazú) |
| 2021 «Elf Christmas», inauguración de la Navidad en vivo (20 nov 2021) | [Reglamento Multiplaza](https://www.multiplaza.com/escazu/blog/reglamento-concurso-inauguracion-de-la-navidad-multiplaza-concepto-elf-christmas) |
| 2022 «Christmas Around the World» (decoraciones del mundo, patinaje, desfiles, emprendimientos) | [Tico Urbano](https://ticourbano.com/2022/11/03/la-magia-de-la-navidad-llega-a-multiplaza-con-christmas-around-the-world/), [La Fatfluencer](https://www.lafatfluencer.com/2022/11/01/multiplaza-inaugura-temporada-navidena/) |
| 2024 Día de las Madres | [Delfino](https://delfino.cr/2024/08/multiplaza-celebra-el-dia-de-las-madres-con-una-serie-de-eventos-y-sorpresas) |
| 2024 Día de la Niñez: 7 set–6 oct, más de 8 dragones animatrónicos de más de 4 m; cita de Lindsay | [Delfino](https://delfino.cr/2024/09/dragones-y-dinosaurios-invaden-multiplaza-para-celebrar-el-dia-de-la-ninez) |
| 2024 Black Friday: horario extendido, hasta 70 % de descuento y premios | [Delfino](https://delfino.cr/2024/11/multiplaza-llega-con-horario-extendido-70-de-descuento-y-premios-increibles-este-black-friday) |
| 2024 «El Regalo de Dar» con BAC; meta de 500 regalos para Fundación Génesis | [Delfino](https://delfino.cr/2024/11/bac-impulsa-campana-el-regalo-de-dar-para-apoyar-cinco-ongs-en-esta-navidad) |
| 2026 Propuesta Navidad Multiplaza | deck interno (ver `../navidad-multiplaza/ANALISIS-PPT.md`) |

No se usaron correos ni teléfonos de directorios (ZoomInfo, RocketReach); el contacto es contacto@lindsaymeneses.com.
Falta: foto de Lindsay (LinkedIn pide inicio de sesión) — agregarla como widget Imagen en «Perfil».

## Publicación

1. Crear la página (una vez): `POST wp/v2/pages` con `title`, `slug: lindsay-meneses`, `status: publish`,
   `template: elementor_canvas`, `meta: {_elementor_edit_mode: builder, _elementor_template_type: wp-page}`.
2. `python3 build_landing.py` y enviar `landing-elementor-data.json` en `meta._elementor_data`.
3. Portada del sitio: `POST wp/v2/settings {show_on_front: page, page_on_front: <ID>}`.
4. `DELETE elementor/v1/cache`.

Cada nuevo evento: agregar una tarjeta con `proyecto(...)` y, si tiene página propia, su enlace.
