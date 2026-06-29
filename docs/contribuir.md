# Cómo usar y mantener este sitio

Esta página es para quien **edita o mantiene** el manual (no para el lector final).

## Qué es esto técnicamente

Un sitio **MkDocs Material**: páginas escritas en Markdown que se convierten en una web estática, buscable, sin necesidad de servidor. El contenido vive en el repo del proyecto:

```
rediseno-proceso/capacitacion-web/
├── mkdocs.yml          ← configuración (tema, navegación, buscador)
├── docs/               ← todo el contenido (markdown)
│   ├── index.md        ← portada
│   ├── presupuestos/   ← el rol Presupuestos (piloto)
│   └── ...
└── site/               ← la web generada (NO se edita a mano)
```

## Ver el sitio en tu computadora (preview en vivo)

```bash
# 1. Activar el entorno (una vez por terminal)
source ~/presto-web-venv/Scripts/activate

# 2. Ir a la carpeta del sitio
cd "rediseno-proceso/capacitacion-web"

# 3. Levantar el servidor de preview
mkdocs serve
```

Abrí **http://127.0.0.1:8000** en el navegador. Mientras editás un `.md`, la página se actualiza sola.

## Editar o agregar una página

1. Editá el `.md` correspondiente en `docs/` (o creá uno nuevo).
2. Si es una página nueva, agregala al menú en `mkdocs.yml` (sección `nav`).
3. Guardá y mirá el cambio en el preview.

## La plantilla de cada página de tarea

Para mantener consistencia, cada página de tarea sigue estas 7 secciones:

```markdown
## Tarea N — [nombre]

**Qué es:** una frase.
**Por qué importa:** aterrizado a Raizant.
**Paso a paso** `[minuto del video]`:
1. ...

!!! warning "Cuidado"
    La falla silenciosa relacionada.

🎥 Mirá el video — [tema, minuto]
📖 Fuente oficial — [PDF, página]
✏️ Ejercicio en BLEND
```

## Reglas de estilo (de soul.md)

- **Conclusión primero**, detalle después.
- Distinguir ✅ **verificado** de ⚠️ **pendiente** — nunca mezclar.
- **Nunca inventar cifras ni datos.** Si no se tiene la fuente, se marca como pendiente.
- Traducir la jerga la primera vez que aparece.
- Tono de maestro paciente; ejemplos de BLEND/Botanic.

## Las cajas (admonitions) disponibles

| Sintaxis | Para qué |
|---|---|
| `!!! note` | Una nota / aclaración |
| `!!! tip` | Un truco útil |
| `!!! warning` | Una falla silenciosa / cuidado |
| `!!! danger` | Una regla de oro crítica |
| `!!! abstract` | La conclusión primero |
| `!!! example` | Un ejercicio |
| `??? question` | Una pregunta plegable (FAQ) |

## Publicar el sitio (pendiente de decidir)

Opciones, de la más simple a la más completa:

1. **Carpeta compartida** — `mkdocs build` genera `site/`; se copia a una carpeta de OneDrive compartida y se abre `index.html`. Simple, sin servidor.
2. **GitHub Pages interno** — versionado y con URL. Requiere repo.
3. **Servidor interno** — si se quiere control de acceso.

> La decisión de dónde publicar es del equipo (issue **DRI-187**). Afecta cómo accede cada persona.

---

## Las fuentes del contenido

| Fuente | Ubicación |
|---|---|
| Apuntes de capacitación (companions) | `rediseno-proceso/conocimiento-presto/C0X-*.md` |
| Resúmenes de cada video | `rediseno-proceso/conocimiento-presto/0X-*.md` |
| Transcripciones con timestamp | `presto-videos-capacitacion/transcripcion videos/*.md` |
| Documentación oficial RIB (PDFs) | `presto-videos-capacitacion/presto-documentacion/` |
| Capturas de pantalla | `rediseno-proceso/capturas-presto/` |
