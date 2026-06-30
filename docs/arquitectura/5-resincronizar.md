# 5 · Re-sincronizar cuando el modelo cambia

!!! abstract "Conclusión primero"
    El diseño **siempre** cambia: arquitectura saca dos ventanas, ensancha un muro, agrega un ambiente. Cuando eso pasa, el presupuesto **no se actualiza solo** — hay que re-sincronizar a mano. La regla de oro: usás el botón **`Añadir`** (que vuelca al estudio **abierto**), **nunca `Exportar`** (que crearía una obra paralela). Y antes de aceptar, **revisás qué cambió** con `Comprobar` y `Buscar líneas desaparecidas`. Esta página es el **corazón del gobierno del dato** del rol: si nadie hace esto bien, modelo y presupuesto se desfasan sin que nadie lo note.

!!! tip "Antes de arrancar, tené a mano el mapa"
    Usamos el botón `Añadir` (en la ventana de exportación de Revit) y la ventana `Mediciones temporales` de Presto. Si no los ubicás, abrí **[🗺 La pantalla de Arquitectura](interfaz.md)**.

!!! info "De dónde sale este contenido"
    Fuente principal: **documentación oficial de Presto (RIB)** — _Manual de Cost-it_ (p. 7 Añadir, p. 17 gestión de versiones del modelo). Complemento: apunte **C01** (casos 15, 16, verificados con capturas reales del curso) y la transcripción del video (minutos `[hh:mm]`).

---

## La regla de oro de toda esta página: `Añadir`, no `Exportar`

!!! danger "Para re-sincronizar SIEMPRE se usa `Añadir`"
    - **`Exportar`** crea una obra de Presto **NUEVA** (es para el traspaso inicial).
    - **`Añadir`** vuelca el modelo a la obra de Presto que **ya tenés abierta**, sin duplicarla.

    Si re-sincronizás con `Exportar` por error, te quedás con **un archivo paralelo** y el presupuesto bueno **sin actualizar** — y nadie te avisa. Los dos botones están **uno al lado del otro** en el mismo diálogo. 📖 _(Manual de Cost-it, p. 7: "Para insertar los resultados en una obra existente vea el apartado 'Añadir a un presupuesto existente'.")_

---

## El ciclo de re-sincronización (de un vistazo)

```
1. Cambia el modelo en Revit
        │
2. Estudio ABIERTO en Presto  +  Cost-It▸Exportar… pero pulsás AÑADIR
        │  (vuelve a llenar Mediciones temporales)
3. Asignar por código inferior   ← OBLIGATORIO, primero
        │
4. Comprobar          → acción: ninguna / actualizar
5. Buscar líneas      → acción: borrar (lo que se eliminó del modelo)
   desaparecidas
        │
6. Revisás las inserciones VERDES y la columna Acción
        │
7. Traspasar  → el presupuesto queda al día
```

---

## Tarea 1 — Volcar el modelo cambiado con `Añadir`

**Qué es:** traer las novedades del modelo a la "sala de espera" del estudio, sin crear obra nueva.

📖 **Fuente oficial:** Manual de Cost-it, p. 7 (Añadir a un presupuesto existente).

**Paso a paso** `[03:50]`:

1. Hacé el cambio en Revit (en el ejemplo del curso: **suprimir 2 de las 15 ventanas**).
2. **Abrí el estudio en Presto** (el presupuesto que querés actualizar) y, en Revit, no dejes nada seleccionado.
3. En Revit, `Cost-It ▸ Exportar` para abrir el diálogo — **pero pulsá `Añadir`** (NO `Exportar`).
4. `Añadir` vuelve a llenar la ventana **`Mediciones temporales`** de Presto con las líneas del modelo.

!!! note "Lo que vas a ver en el diálogo"
    El diálogo de `Añadir` muestra una **vista previa en gráfico de torta** por naturaleza/categoría (p. ej. "Script del código Áreas / Materiales") y los botones `Defecto · Exportar · Añadir · Cancelar · Ayuda`. _(Verificado por captura del curso.)_

---

## Tarea 2 — Re-asignar el match (obligatorio antes de comprobar)

**Qué es:** volver a emparejar las líneas del modelo con las partidas del estudio.

**Paso a paso** `[03:50]`:

1. En `Mediciones temporales`, seleccioná **toda la columna `Org Relación`** (clic en su cabecera).
2. Clic derecho → **`Asignar unidad de obra ▸ por código inferior`**.

!!! warning "Este paso NO es opcional"
    _"Es obligatorio este primer paso."_ `[03:50]`. Sin re-asignar el match, `Comprobar` no sabe contra qué partidas comparar y el resultado no sirve.

---

## Tarea 3 — `Comprobar`: ver qué cambió

**Qué es:** detectar qué líneas se modificaron respecto al presupuesto actual.

📖 **Fuente oficial:** Manual de Cost-it, p. 17 — _"Para seleccionar las mediciones de los elementos del modelo que no han sido medidos previamente pulse 'Comprobar'… y quedarán identificadas como 'Inserción'."_

**Paso a paso** `[04:00]`:

1. Pulsá el botón **`Comprobar`**.
2. Mirá la columna **`Acción`**:
   - **`ninguna`** = esa línea no cambió → no se traspasa nada.
   - **`actualizar`** = esa línea cambió → se va a actualizar.
3. Las líneas **nuevas** quedan marcadas como **"Inserción"** (en **🟢 verde**, ver Tarea 5).

---

## Tarea 4 — `Buscar líneas desaparecidas`: lo que se borró del modelo

**Qué es:** detectar los elementos que **se eliminaron** del modelo, para borrar su cantidad del presupuesto.

**Paso a paso** `[04:00]`:

1. Pulsá el botón **`Buscar líneas desaparecidas`**.
2. Marca con acción **`borrar`** las líneas de elementos eliminados del modelo. En el ejemplo del curso, marca **exactamente las 2 ventanas** que se quitaron.

!!! note "Por qué es un paso aparte"
    `Comprobar` ve lo que **cambió o se agregó**, pero no lo que **desapareció** (un elemento borrado ya no está en el modelo para comparar). Por eso hay un botón específico que sale a buscar las líneas huérfanas. Si te lo saltás, el presupuesto sigue contando cantidades de elementos que ya no existen.

---

## Tarea 5 — Revisar las inserciones verdes ANTES de traspasar ⭐

**Qué es:** confirmar que los cambios son **exactamente** los que esperás, antes de aceptarlos.

📖 **Fuente oficial:** Manual de Cost-it, p. 17 (gestión de versiones del modelo) · C01 caso 16 (verificado por captura).

**Paso a paso** `[04:00]`:

1. En `Mediciones temporales`, las filas etiquetadas **"Inserción… OBSERVACIONES"** aparecen resaltadas en **🟢 verde** = lo que **entró/cambió** en este re-traspaso. _(Este es el **tercer semáforo**, distinto del verde de "match por código inferior" y del verde de "tipos mezclados".)_
2. Recorré la columna **`Acción`** (`ninguna` / `actualizar` / `borrar`) y revisá las filas verdes: ¿los cambios son **exactamente** los esperados? (en el ejemplo, 2 líneas `borrar` = las 2 ventanas).
3. **Solo cuando confirmaste**, hacé **clic afuera** (no dejes nada seleccionado) → botón **`Traspasar`**.
4. **Resultado:** las ventanas pasan de 15 a 13; los muros ganan superficie al taparse los huecos. El presupuesto quedó al día.

!!! danger "No aceptes cambios a ciegas"
    Cost-It **no congela ni alerta**. Si pulsás `Traspasar` sin revisar las inserciones verdes y la columna `Acción`, podés aceptar un cambio que no querías (o no notar uno que faltaba). **Revisar antes de aceptar es un requisito del proceso de Raizant**, no un lujo. _(Fallas silenciosas FS-1 y FS-6.)_

---

## Por qué este rol necesita un responsable designado

!!! warning "La re-sincronización NO se deja a criterio individual"
    Como Cost-It no avisa cuándo hay que re-sincronizar ni fuerza el ciclo, Raizant designa un **responsable de re-sync** con un **procedimiento estándar disparado por cada cambio de modelo**. El tejido in-house debe **detectar cambios de modelo y recordar/agendar** la resincronización — porque Cost-It no lo hace solo. Sin esto, modelo y presupuesto se separan callados y la "torre de control" mide sobre datos viejos.

**El procedimiento mínimo de Raizant (propuesto):**

1. Arquitectura avisa "cambié el modelo" (o el tejido in-house lo detecta).
2. El responsable de re-sync corre el ciclo `Añadir → re-asignar → Comprobar → Buscar líneas desaparecidas`.
3. Revisa inserciones verdes y acciones **antes** de `Traspasar`.
4. _(Antes de aceptar cambios grandes)_ se **versiona/congela** el estudio aprobado, para poder medir el desvío (esto es tejido in-house, Cost-It no lo hace).

---

## 🎥 Mirá el video

| Tema | Minuto |
|---|---|
| Cambiar el modelo + `Añadir` (no `Exportar`) | `[03:50]` |
| Re-asignar por código inferior (obligatorio) | `[03:50]` |
| `Comprobar` → acción ninguna/actualizar | `[04:00]` |
| `Buscar líneas desaparecidas` → acción borrar | `[04:00]` |
| Revisar inserciones verdes + `Traspasar` | `[04:00]` |

> Video fuente: `CSE - Cost It - 23/01/2026.mp4`. _Complemento de la documentación oficial citada en cada tarea._

---

## ⚠️ Lo que Cost-It NO te avisa (resumen)

- **No te avisa cuándo hay que re-sincronizar** → el presupuesto se desfasa del modelo en silencio. _(Por qué hay responsable)_
- **`Exportar` en vez de `Añadir` crea una obra paralela** y deja el bueno sin actualizar. _(Regla de oro)_
- **No congela baseline**: cada re-traspaso sobreescribe sin guardar el "antes". _(Tarea 5)_

👉 Todas, con cómo blindarte, en [6 · Reglas de oro y fallas silenciosas](6-reglas-de-oro.md).

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá lo aprendido"
    _(Con el estudio ya volcado de la [Página 4](4-codificar-y-volcar.md).)_

    1. En Revit, **borrá un par de elementos** (p. ej. 2 ventanas) y, si podés, **ensanchá un muro**.
    2. Con el estudio **abierto** en Presto, `Cost-It ▸ Exportar…` → pulsá **`Añadir`** (¡no `Exportar`!).
    3. `Asignar por código inferior` → `Comprobar` → `Buscar líneas desaparecidas`.
    4. Antes de traspasar, **identificá las filas verdes (Inserción)** y las que dicen `borrar`. Confirmá que coinciden con tu cambio (2 ventanas `borrar`).
    5. `Traspasar` y verificá que el conteo de ventanas bajó y que el muro ensanchado cambió de cantidad.

    **Cómo sabés que salió bien:** el presupuesto refleja **exactamente** tu cambio de modelo, sin obras paralelas y sin cantidades fantasma de lo que borraste.

---

📖 **Fuentes oficiales (RIB):** _Manual de Cost-it_, pp. 7 y 17. · **Complementos internos:** apunte C01 (casos 15, 16, verificados con capturas) · transcripción `CSE - Cost It - 23/01/2026`.
