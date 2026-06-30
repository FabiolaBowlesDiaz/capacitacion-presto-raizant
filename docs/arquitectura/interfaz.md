# La pantalla de Arquitectura: dónde está cada cosa

!!! abstract "Por qué esta página va primero"
    Lo que más cuesta de Cost-It **no es entender qué hace — es que trabajás en DOS programas a la vez** y los botones están repartidos entre Revit y Presto. Esta página es tu mapa: dónde está el menú `Cost-It` en **Revit**, y dónde aparece el resultado en **Presto**. Volvé a ella cada vez que una tarea te diga "andá a tal botón".

!!! tip "Cómo leemos las rutas de clic"
    En todas las tareas vas a ver caminos escritos así: **`Cost-It ▸ Exportar`** (en Revit) o **`Ver ▸ Mediciones temporales`** (en Presto). Se lee de izquierda a derecha: primero la **pestaña/menú** de la cinta, después el **botón**. Cuando el paso es en Revit lo decimos; cuando es en Presto, también.

!!! warning "Antes que nada: ¿tu licencia tiene Cost-It?"
    El menú `Cost-It` **solo aparece en Revit si el complemento está instalado y la licencia incluye el módulo**. Cómo verificarlo está abajo, en "Cómo saber si tenés el módulo".

---

## El reparto: Revit manda las cantidades, Presto las recibe

Quedate con esta foto mental antes de cualquier botón:

```
   REVIT  (tu modelo 3D)                         PRESTO  (el presupuesto)
   ┌──────────────────────────┐                  ┌──────────────────────────┐
   │  menú Cost-It en la cinta │   ── Exportar ─► │  pestaña Árbol           │
   │  • Exportar               │   ── Añadir ───► │  + subventana Mediciones │
   │  • Añadir                 │                  │  + Mediciones temporales │
   │  • Localizar              │  ◄── Localizar ──│                          │
   └──────────────────────────┘                  └──────────────────────────┘
        (las cantidades nacen aquí)                   (se leen y afinan aquí)
```

- **Revit** es donde **nacen** las cantidades (cada muro, ventana, pilar tiene su geometría).
- **Cost-It** es el plugin que las **traspasa** a Presto y las arma como partidas.
- **Presto** es donde **leés, verificás y afinás** el presupuesto que resultó.

---

## Lado Revit — el menú `Cost-It` de la cinta

Cuando el complemento está instalado, en Revit aparece una **pestaña `Cost-It`** en la cinta de arriba. Sus tres botones principales:

| Botón | Qué hace | Cuándo lo usás |
|---|---|---|
| **`Exportar`** | El **corazón** de Cost-It. Lee el modelo y **crea una obra de Presto nueva** con las cantidades. | La **primera vez** que traés un modelo. _(Tarea 1)_ |
| **`Añadir`** | Vuelca el modelo a una **obra de Presto que ya está abierta**, sin crear una nueva. | Para **re-sincronizar** cuando el modelo cambió. _(Página 5)_ |
| **`Localizar`** | Marcás un elemento en Revit y Presto **salta a su partida**. | Para verificar a qué partida fue a parar un elemento. _(Página 2)_ |

!!! danger "La confusión #1 del rol: `Exportar` vs `Añadir`"
    Están **uno al lado del otro** y hacen cosas distintas: **`Exportar` crea una obra nueva**; **`Añadir` actualiza la que ya tenés abierta**. Usar `Exportar` cuando querías `Añadir` te deja **dos presupuestos paralelos** y el bueno sin actualizar. Regla de oro: traspaso inicial = `Exportar`; re-sincronizar = `Añadir`. _(Lo repetimos en cada página donde aplica.)_ 📖 _(Manual de Cost-it, p. 7: "Exportar crea una obra… Para insertar los resultados en una obra existente vea Añadir a un presupuesto existente".)_

### La ventana de exportación (lo que se abre al pulsar `Exportar`)

Al pulsar `Exportar` se abre una ventana con **pestañas** y, abajo, una fila de **botones**:

| Pestaña | Para qué sirve |
|---|---|
| **`Estadísticas`** | Un **gráfico** que te muestra cuántos elementos hay por categoría (cuál es la más numerosa) y el avance de la exportación. |
| **`Opciones`** | El cerebro: qué se incluye, cómo se mide cada cosa y — lo más importante — **la codificación** (qué parámetro agrupa los elementos en partidas). |
| **`Categorías`** | La lista de categorías de Revit (Muros, Puertas, Pilares…) para **marcar/desmarcar** cuáles llevar. |
| **`Script del código`** | Avanzado: escribir un código ampliado o un filtro para medir solo lo que cumpla un criterio. |

| Botón (abajo) | Qué hace |
|---|---|
| **`Defecto`** | Restaura las opciones predeterminadas. |
| **`Exportar`** | Crea la **obra nueva** en Presto. |
| **`Añadir`** | Vuelca a la **obra abierta** (re-sync). |
| **`Cancelar`** | Cierra sin traspasar. |
| **`Ayuda`** | Abre el manual oficial de Cost-It. |

> 📖 **Fuente oficial:** Manual de Cost-it, pp. 7–10 (Exportar, Estadísticas, Opciones, Categorías). · Botones verificados por captura del curso (Cost-It `25.05.00`).

---

## Lado Presto — dónde aparece el resultado

Una vez exportado, en **Presto** mirás el presupuesto que se armó:

- **Pestaña `Árbol`** (cinta de Presto → menú de nodos → mostrar **`Partidas`**): la estructura que llegó del modelo — **capítulos** (= las categorías de Revit) con sus **partidas** anidadas.
- **Subventana `Mediciones`** (la franja de abajo): el **detalle de líneas de medición** de la partida seleccionada. Cada elemento del modelo es una línea. Esta subventana tiene su **propio menú de esquemas**, que cambia qué columnas ves:

| Esquema de `Mediciones` | Qué columnas muestra |
|---|---|
| **`Datos generales`** | `Cantidad`, `N`, `Longitud`, `Anchura`, `Altura` — las dimensiones del prisma del objeto. _(El color de `Cantidad` sigue la regla del 2%, ver [Página 2](2-leer-y-verificar.md).)_ |
| **`Prest Dimensiones`** | `BIM Long`, `BIM Sup`, `BIM Volumen`, `BIM Peso` — el valor BIM exacto del modelo. |
| **`Localización BIM`** | `X`/`Y`/`Z`, `Planta`, ejes, habitación y — clave en modelos centrales — la columna **`Archivo`** (de qué Revit vino el elemento). |
| **`Identificación BIM`** | `Familia Tipo BIM` (familia : tipo) — útil para desglosar. |

- **Ventana `Mediciones temporales`** (`Ver ▸ Mediciones temporales`): la **sala de espera** por donde pasan las cantidades cuando las volcás a un estudio ya armado, o cuando re-sincronizás. _(Páginas 4 y 5.)_

> 📖 **Fuente oficial:** Manual de Cost-it, pp. 15–17 (líneas de medición, regla del 2%, Mediciones temporales). · Glosario de columnas verificado en C01 §5.

---

## Los tres semáforos de color (no confundirlos)

Cost-It usa colores como **metadato**, y hay **tres semáforos distintos** en tres lugares distintos. Es el error de lectura #1:

| # | Dónde aparece | Qué significan los colores |
|---|---|---|
| **1 · Resultado** | Sobre el `Resumen` de cada **partida** en el árbol | 🔴 **rojo** = elementos **sin código** (Presto los agrupa por tipo) · ⬜ **blanco** = con código y un solo tipo (OK) · 🟢 **verde** = con código pero **tipos mezclados** (revisar si desglosar) |
| **2 · Cantidad (regla 2%)** | Sobre la celda `Cantidad` de cada **línea** | 🟣 **magenta** = cantidad **calculada** por Cost-It · ⚫ **negra** = cantidad **declarada** del modelo _(ver [Página 2](2-leer-y-verificar.md))_ |
| **3 · Re-sincronización** | Filas **"Inserción"** en `Mediciones temporales` | 🟢 **verde** = lo que **entró/cambió** en el último re-traspaso _(ver [Página 5](5-resincronizar.md))_ |

!!! warning "Son tres verdes diferentes"
    El verde del semáforo 1 (tipos mezclados) **no es** el mismo que el verde del semáforo 3 (inserción en re-sync). Cada uno vive en otra ventana y significa otra cosa. Cuando una tarea hable de "verde", fijate **en cuál de las tres pantallas estás**.

---

## Cómo saber si tenés el módulo

1. **En Revit:** abrí la cinta de arriba y buscá la pestaña **`Cost-It`**. Si no está, el **complemento no está instalado** (se instala con Revit cerrado, según el manual que viene con la licencia).
2. **En Presto:** ventana inicial → **`Activación`** → confirmá que el **módulo "Cost-It"** figure **operativo**. Con una licencia **demo** no aparece "Activación" y se limitan funciones (no guarda, bloquea "actualizar valores en el modelo").

!!! note "Las capturas de estas pantallas"
    Ya existen **capturas reales del curso de Cost-It** (versión `25.05.00`) que ilustran el diálogo de exportación, el semáforo del resultado y la re-sincronización. Se integran a estas páginas como en los demás roles; las pantallas que falten se completan cuando el módulo esté activo en la licencia (Cloud).

---

<div class="admonition success">
<p class="admonition-title">Ya tenés el mapa</p>
<p>Con esto, cuando una tarea diga "en Revit, <code>Cost-It ▸ Exportar</code>" o "en Presto, mirá la columna <code>Cantidad</code> de <code>Mediciones</code>", sabés exactamente dónde mirar. Seguí con <a href="../0-fundamentos/">0 · Fundamentos de Cost-It</a>.</p>
</div>

---

📖 **Fuentes oficiales (RIB):** _Manual de Cost-it_, pp. 5–17 · _Cost-it (BIM 5D con Presto)_ · _Personalización de la exportación de Revit_. · Complemento: apunte interno C01 §0 y §5 (glosario de columnas y semáforos verificados por captura).
