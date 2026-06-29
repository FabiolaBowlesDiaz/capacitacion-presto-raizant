# Capacitación Presto · Raizant

Web de capacitación de **Presto** por rol, para bajar la curva de aprendizaje en la migración Syneco → Presto.

Sitio estático generado con [MkDocs Material](https://squidfunk.github.io/mkdocs-material/). Buscable, por rol y por tarea.

## Ver el sitio en local

```bash
# 1. Activar el entorno (una vez por terminal)
source ~/presto-web-venv/Scripts/activate

# 2. Levantar el preview (desde esta carpeta)
mkdocs serve
```

Abrí **http://127.0.0.1:8000**. Mientras editás un `.md`, la página se actualiza sola.

## Generar el HTML para compartir (sin servidor)

```bash
mkdocs build
```

Genera la carpeta `site/` con la web completa. Se puede copiar a una carpeta compartida de OneDrive y abrir `site/index.html` en cualquier navegador.

## Estructura

```
capacitacion-web/
├── mkdocs.yml          ← configuración (tema, navegación, buscador)
├── docs/               ← todo el contenido (markdown)
│   ├── index.md        ← portada
│   ├── presupuestos/   ← rol Presupuestos (piloto)
│   └── contribuir.md   ← cómo mantener el sitio
└── site/               ← web generada (NO se versiona, se regenera)
```

## Cómo agregar contenido

Ver `docs/contribuir.md` — tiene la plantilla de página, la guía de estilo y las convenciones.

## Setup inicial (solo la primera vez en una máquina nueva)

```bash
uv venv ~/presto-web-venv --python 3.11
source ~/presto-web-venv/Scripts/activate
uv pip install mkdocs-material mkdocs-glightbox
```

---

_Tracking del proyecto en Linear: **Raizant - Capacitación Presto**._
