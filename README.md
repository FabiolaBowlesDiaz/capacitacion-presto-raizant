# Capacitación Presto · Raizant

Web de capacitación de **Presto** por rol, para bajar la curva de aprendizaje en la migración Syneco → Presto.

Sitio estático generado con [MkDocs Material](https://squidfunk.github.io/mkdocs-material/). Buscable, por rol y por tarea.

## 🌐 Sitio publicado

**https://fabiolabowlesdiaz.github.io/capacitacion-presto-raizant/**

Cada push a `main` publica automáticamente (GitHub Actions → GitHub Pages, tarda ~2 min). No hace falta buildear ni subir nada a mano.

## Editar contenido

Dos caminos:

1. **Desde el navegador** (cambios chicos): botón ✏️ "editar esta página" en cualquier página del sitio → edita el `.md` en GitHub → commit → se publica solo.
2. **En local** (cambios grandes, con preview en vivo):

```powershell
# Levantar el preview (desde esta carpeta)
python -m mkdocs serve
```

Abrí **http://127.0.0.1:8000**. Mientras editás un `.md`, la página se actualiza sola.

## Estructura

```
capacitacion-web/
├── mkdocs.yml            ← configuración (tema, navegación, buscador)
├── docs/                 ← todo el contenido (markdown)
│   ├── index.md          ← portada
│   ├── flujo/            ← gobierno de datos (los 2 ciclos, reglas de oro)
│   ├── presupuestos/     ← rol Presupuestos
│   ├── compras/          ← rol Compras
│   ├── obra-almacen/     ← rol Obra / Almacén
│   ├── control-obra/     ← rol Control de obra
│   ├── planificacion/    ← cronograma y objetivo de coste
│   ├── arquitectura/     ← rol Arquitectura (Cost-It)
│   └── contribuir.md     ← cómo mantener el sitio
├── overrides/            ← ajustes del tema (noindex)
├── .github/workflows/    ← deploy automático a GitHub Pages
└── site/                 ← web generada (NO se versiona, se regenera)
```

## Cómo agregar contenido

Ver `docs/contribuir.md` — tiene la plantilla de página, la guía de estilo y las convenciones.

## Setup inicial (solo la primera vez en una máquina nueva)

```powershell
pip install mkdocs-material mkdocs-glightbox
```

> ⚠️ El repo es público: no cargar montos reales de presupuestos, datos de proveedores ni credenciales en las páginas. Los ejercicios usan la obra BLEND como contexto pero con cantidades didácticas.

---

_Tracking del proyecto en Linear: **Raizant - Capacitación Presto**._
