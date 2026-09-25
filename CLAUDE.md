# CLAUDE.md

Repositorio de trabajo de Lindsay Meneses. Se enfoca en **mercadeo, publicidad, copywriting, branding, diseño** y **desarrollo web** (WordPress, PHP, SQL, CSS, HTML y JS).

## Idioma
- Responde en **español**, salvo que se pida otro idioma.
- Escribe los textos de marketing en el idioma y para el mercado del cliente. No traduzcas de forma literal.

## Herramientas instaladas
- Hay 619 skills en `.claude/skills/` y 48 agentes en `.claude/agents/`. El índice por categoría está en `CATALOGO.md`.
- Si varias skills se solapan (por ejemplo `copywriting`, `market-copy` y `ad-creative`), usa la más específica para la tarea. Si no está claro cuál, empieza por la de `coreyhaines31/marketingskills`.
- Para tareas grandes, como auditorías, campañas completas o rediseños, reparte el trabajo entre los agentes especializados en paralelo.
- Los conectores MCP disponibles son `Servidor` (WHM/cPanel), `web` (WordPress) y `github`. Antes de hacer cambios en producción (DNS, email, bases de datos, SSL, publicar posts), confirma con el usuario.

## Cómo trabajar (basado en las pautas de Andrej Karpathy)
1. **Piensa antes de actuar.** Di qué estás suponiendo. Si hay dudas o varias interpretaciones, pregunta.
2. **Simplicidad primero.** Haz lo mínimo que resuelve el pedido, sin funciones ni abstracciones de más.
3. **Cambios quirúrgicos.** Toca solo lo necesario y respeta el estilo del código existente.
4. **Ejecuta guiado por objetivos.** Define cómo se verifica el éxito y comprueba el resultado antes de darlo por terminado.

## Conectores MCP del proyecto (`.mcp.json`)
Claude Code pide aprobación la primera vez que abres el proyecto. Las claves se leen de variables de entorno. Nunca las escribas en el repo ni en el chat.
| Conector | Para qué | Variables |
|---|---|---|
| `imagenes` | Generar y editar imágenes con GPT Image de OpenAI (por defecto) o con Gemini/Nano Banana | `OPENAI_API_KEY`, `GEMINI_API_KEY`, opcional `IMAGE_PROVIDER` (`openai`/`gemini`) |
| `chatgpt-gemini` | Consultar a modelos de ChatGPT y Gemini para segundas opiniones, lluvia de ideas o revisión | `OPENAI_API_KEY`, `GEMINI_API_KEY`, opcional `OPENROUTER_API_KEY` |
| `meigen` | Generación de imágenes con biblioteca de prompts (Midjourney, GPT Image, Seedance) | `MEIGEN_API_TOKEN` (las búsquedas públicas funcionan sin clave) |
| `blender` | Controlar Blender para modelado 3D. Solo funciona en una computadora con Blender y su add-on | ninguna |

Las imágenes generadas se guardan en `imagenes/`, que no se sube al repo.
