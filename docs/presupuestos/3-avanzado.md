# 3 · Presupuesto avanzado

!!! abstract "Conclusión primero"
    Acá aprendés a **sanear un presupuesto heredado** (lo más útil del día a día): detectar y corregir lo que hace que "los informes no sumen", consolidar recetas, traer precios desde un catálogo maestro, clasificar costos por zona (Espacios) y usar fórmulas. Es el módulo que te enseña a **revisar la calidad** del presupuesto antes de congelarlo.

!!! tip "¿Te perdés con los menús? Tené el mapa a mano"
    Cuando una instrucción diga "la cinta de arriba" o "la pestaña Conceptos", mirá el **[🗺 mapa de la pantalla](interfaz.md)**.

!!! warning "Una aclaración sobre esta página"
    Sale del apunte **CL-3 (Presupuesto Avanzado)**. De esa clase **no tenemos capturas**, así que algún nombre exacto de botón puede verse un poco distinto en tu pantalla. El paso a paso sí es confiable. Cada paso cita el minuto `[hh:mm]`.

---

## Primero: las 4 reglas que tenés que cuidar

Si se rompen, **Presto no te avisa** pero los informes salen descuadrados. Tenelas presentes:

| Regla | Qué significa |
|---|---|
| **Un capítulo siempre tiene cantidad = 1** | Son títulos, no llevan cantidad. Si convertís algo a capítulo, su cantidad se vuelve 1. |
| **Todo material/MO/maquinaria debe colgar de una PARTIDA** | Nunca debe colgar directo de un capítulo. |
| **Un recurso marcado como "partida" NO suma como recurso** | Si un material quedó como partida por error, descuadra los informes. |
| **Un concepto = un precio** | El mismo material compartido entre partidas tiene un solo precio; si lo tocás, cambia en todas. |

!!! tip "Aprendé a leer los colores del precio (es clave acá)"
    **Negro** = precio tecleado a mano. **Magenta** = calculado (tiene receta). **Rojo** = un precio que alguien forzó a mano encima de una receta → quedó **bloqueado** y ya no recalcula. **Cantidad con fondo gris** = cantidad **anulada** (no suma).

---

## Tarea 1 — Revisar y enderezar la estructura

**Qué es:** corregir las naturalezas mal puestas en un presupuesto que te llegó de afuera (de Syneco, de un cliente, de otra obra).

**Dónde:** la pestaña de ventana **`Árbol`** (en la fila Obras · Presupuesto · **Árbol** · Conceptos). El Árbol te muestra toda la jerarquía de una.

**Cómo encontrar los problemas** `[00:00]`–`[00:20]`: en el Árbol hay un menú para abrir niveles de golpe. Mandá a abrir hasta el nivel **Partidas**: todos los subcapítulos deberían abrirse y mostrar partidas adentro. **Si un subcapítulo NO se abre, es sospechoso** — seguro tiene materiales colgando directo (mal).

**Los 3 problemas típicos y cómo arreglarlos:**

1. **Un "capítulo" que en realidad era una partida** (tiene materiales adentro): clic derecho en su ícono de naturaleza → cambialo a **`Partida`**. ⚠️ Como antes era capítulo (cantidad 1), ahora tenés que **escribir la cantidad y unidad reales** mirando un respaldo.
2. **Una partida mezclada con subcapítulos en el mismo nivel:** insertá una fila nueva, hacela subcapítulo, y meté la partida adentro con **`Disminuir nivel`**.
3. **Materiales colgando directo de un subcapítulo:** convertí ese subcapítulo en **`Partida`** (una partida con materiales adentro es válida).

!!! tip "Truco para no chocar con códigos repetidos"
    Si creás un subcapítulo para contener una partida, dale el **mismo código + un puntito o guion** al final. Presto no permite dos códigos iguales, y ese carácter extra evita el choque sin que se vea raro al imprimir.

---

## Tarea 2 — Cazar recursos con naturaleza partida (mal puesta)

**Qué es:** encontrar los materiales que quedaron marcados como "partida" por error, que descuadran los informes (aparece un "ajuste" gigante al final).

**Dónde:** la pestaña **`Conceptos`** (la lista plana de todo). Arriba a la izquierda de la tabla hay un **desplegable de esquema** — cambialo a **`Partidas mediciones`**, que deja a la vista solo las cosas marcadas como partida.

**Paso a paso** `[00:10]`–`[00:20]`:

1. En `Conceptos`, poné el esquema **`Partidas mediciones`**.
2. Recorré la lista buscando los que tengan el **precio en NEGRO** — una partida de verdad lo tiene en **magenta**, así que un negro acá es sospechoso.
3. Para juntarlos todos: clic derecho sobre un precio negro → **`Filtrar por color de texto`** (negro). Quedan a la vista solo los sospechosos.
4. A cada uno, en su columna de naturaleza, devolvele lo que era (material / mano de obra / maquinaria). O, si de verdad debía ser una subpartida, armale su receta.
5. Para sacar el filtro al final: botón **`Anular`** (cinta ▸ Inicio ▸ grupo Filtrar). ⚠️ **No** se saca con Ctrl+Z.

---

## Tarea 3 — Desbloquear un precio forzado (el que está en rojo)

**Qué es:** cuando alguien escribió un precio a mano encima de una partida que tenía receta, el número quedó **rojo** y **bloqueado** — ya no recalcula.

**Paso a paso** `[00:20]`–`[00:30]`:

1. Hacé **clic derecho sobre el precio rojo** → en el menú aparecen las opciones **`desbloquear` / `bloquear`**.
2. Elegí **`desbloquear`** → el precio vuelve a **magenta** y se recalcula solo desde su receta.

!!! tip "Para cazarlos todos de una"
    En `Conceptos` con esquema `Partidas mediciones`, clic derecho en un precio rojo → `Filtrar por color de texto` (rojo) → corregís todos juntos.

---

## Tarea 4 — Llevar una partida a un precio exacto SIN arruinar otras

**Qué es:** dejar una partida en un precio redondo, ajustando los recursos de adentro, pero **sin forzar el precio a mano** (que la dejaría roja y bloqueada).

**Dónde:** cinta de arriba ▸ pestaña **`Herramientas`** ▸ **`Ajustar`**.

**Paso a paso** `[00:30]`:

1. En el campo de concepto, hacé clic en el botón **`…`** y seleccioná la partida.
2. Escribí el **precio objetivo** al que la querés llevar.
3. En la sección **`Cambiar`**, elegí cómo se reparte el ajuste:

!!! danger "La regla que te salva de un desastre"
    - Si ajustás por **`Precio`** y esos materiales se usan también en **otras partidas**, les cambia el precio **a todas** (porque "un concepto = un precio").
    - Si ajustás por **`Cantidad`**, solo cambia las cantidades de esta partida → **no toca a las demás**.
    - **Regla: si los materiales se comparten, ajustá SOLO por Cantidad.**

El precio final queda en magenta (calculado, real). Si te arrepentís, Deshacer (Ctrl+Z).

---

## Tarea 5 — Reducir niveles (simplificar la receta para el informe)

**Qué es:** aplastar las sub-recetas intermedias para que el informe de la receta muestre los materiales directamente bajo la partida, sin pasos intermedios.

**Dónde:** cinta de arriba ▸ pestaña **`Herramientas`** ▸ **`Reducir niveles`**.

**Paso a paso** `[00:40]`–`[01:00]`:

1. En la opción `Relaciones`, dejá la máscara **`*`** (significa "todos los niveles").
2. Tildá qué querés simplificar:
    - **`Auxiliares`** (las sub-recetas) → **es seguro**: las aplasta subiendo sus materiales un nivel.
    - **`Partidas`** → ⚠️ esto toca **TODAS** las partidas, incluso las principales → **puede desarmarte el presupuesto entero**.

!!! danger "No tildes 'Partidas' a lo loco"
    Si solo querés aplastar ciertas subpartidas, ponéles a todas un código que empiece con una **letra reservada** (ej. `P`) y usá la máscara **`P*`**. Así toca solo esas, sin desarmar las partidas reales.

!!! tip "Cómo saber que salió bien"
    Después de reducir, el **total casi no debe cambiar** (unos centavos). Si el total se dispara en millones, es que había **cantidades anuladas** escondidas → andá a la Tarea 6.

---

## Tarea 6 — Encontrar cantidades anuladas

**Qué es:** las cantidades que alguien "anuló" (fondo gris, no suman) se vuelven peligrosas al reducir niveles, porque la anulación se pierde y vuelven a sumar, inflando el total.

**Dónde:** cinta de arriba ▸ pestaña **`Ver`** ▸ botón **`Relaciones`** (abre una ventana nueva). En su desplegable de esquema, elegí **`Partidas y Auxiliares con Inferiores`**.

**Paso a paso** `[01:00]`–`[01:20]`:

1. Buscá una celda de cantidad con **fondo gris** (esa es una anulada).
2. Clic derecho sobre ella → **`Filtrar por color de fondo`** → quedan a la vista todas las anuladas.
3. A cada una: **`Desanular`** (si en realidad debía sumar) o **`Eliminar`** (si de verdad no va).
4. Sacá el filtro con **`Anular`** al terminar.

---

## Tarea 7 — Traer precios desde un catálogo maestro

**Qué es:** volcar precios, descripciones y recetas actualizadas desde otra obra de referencia (un "Presto maestro" de precios) hacia tu presupuesto.

**Dónde:** cinta de arriba ▸ pestaña **`Herramientas`** ▸ **`Actualizar`**.

**Paso a paso** `[01:20]`–`[01:40]`:

1. En el campo **`Desde`**, hacé clic en **`…`** y elegí el archivo de referencia (no hace falta ni abrirlo).
2. Elegí qué actualizar: todo, o con máscara (ej. `M*` = solo materiales), o solo lo que tengas seleccionado.
3. **`Aceptar`** → actualiza los conceptos cuyo código exista también en la referencia.

!!! warning "Qué hace y qué NO hace Actualizar"
    - **Solo toca** los conceptos cuyo código exista en la referencia (los demás no se tocan).
    - Si la referencia trae una receta distinta para el mismo código, **reemplaza la receta entera**.
    - **No es automático/en vivo** — hay que volver a ejecutarla cada vez.
    - **NO es un "congelar versión" ni un comparador**: pisa lo que tenías sin guardar copia (salvo Deshacer). El congelado de la baseline lo armamos por fuera.

---

## Tarea 8 — Espacios: ver el costo por zona o fase

**Qué es:** una forma paralela de mirar los costos, agrupados por zona/sector/fase (ejes, losas, plantas), **sin tocar** la estructura del presupuesto.

**Cómo funciona** `[01:40]`–`[02:20]`: lo único que conecta el presupuesto con los espacios es la columna **`Espacio`** dentro de las líneas de medición. Creás los espacios (`SPC0010`, `SPC0020`…), les ponés nombre (Ejes, Losas), y a cada línea de medición le asignás su espacio. Después Presto te calcula cuánto cuesta y qué recursos lleva cada zona.

!!! note "Conexión con Revit"
    El dato de Espacio se puede llenar **automáticamente desde Revit** (vía Cost-It), tomándolo de los niveles del modelo. Tope: 10.000 espacios.

---

## Tarea 9 — Fórmulas (columnas calculadas y filtros)

**Qué es:** crear tus propias columnas con cálculos, y filtros con fórmulas.

**Dónde:** cinta de arriba ▸ pestaña **`Inicio`** → **`Insertar columna de usuario`** y, en el grupo Filtrar, **`Por expresión`**.

!!! note "Dato para las fórmulas"
    En las fórmulas, cada naturaleza se nombra con un número: Otros=9, Material=8, Maquinaria=7, Mano de obra=6, Partida=5, Capítulo=4. `[02:50]` _(El detalle fino de la sintaxis lo ampliamos más adelante con capturas.)_

---

## 🎥 Mirá el video

| Tema | Minuto |
|---|---|
| Sanear la estructura | `[00:00]`–`[00:20]` |
| Recursos mal puestos / precios rojos | `[00:20]`–`[00:40]` |
| Reducir niveles + cantidades anuladas | `[00:40]`–`[01:20]` |
| Actualizar desde maestro | `[01:20]`–`[01:40]` |
| Espacios | `[01:40]`–`[02:20]` |
| Fórmulas | `[02:20]`–`[03:00]` |

> Video fuente: `CL-3 - Ppto Avanzado - Lunes 01_12_2025.mp4` (3h 03min).

---

## ⚠️ Lo que Presto NO te avisa (resumen)

- **Recurso con naturaleza partida** → no suma como recurso, descuadra informes en silencio.
- **Precio forzado a mano (rojo)** → queda bloqueado, no recalcula.
- **Cantidades anuladas** → al reducir niveles vuelven a sumar y el total "explota".
- **Reducir niveles tildando 'Partidas'** → puede desarmar el presupuesto entero.
- **Ajustar por precio con materiales compartidos** → cambia el precio en otras partidas.
- **Actualizar no es un congelado** → pisa lo anterior sin guardar copia.

👉 Todas en [4 · Reglas de oro y fallas silenciosas](5-reglas-de-oro.md).

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá lo aprendido"
    Sobre la obra de prueba **BLEND**:

    1. En la pestaña Árbol, abrí hasta el nivel Partidas y buscá algún subcapítulo que no se abra (tiene materiales colgando directo).
    2. En `Conceptos → Partidas mediciones`, filtrá por color de texto negro y fijate si hay recursos con naturaleza partida mal puesta.
    3. Probá `Ajustar` una partida a un precio objetivo **por Cantidad** y verificá que el precio quede en magenta.

    **Cómo sabés que salió bien:** ningún informe de recursos muestra un "ajuste" enorme al final.

---

📖 **Fuente oficial:** Expresiones-campos-de-usuario-funciones-y-filtros.pdf · Uso-de-las-variables-personalizadas.pdf · Coste-de-objetos-y-coste-de-procesos.pdf · Calculo-de-precios-por-produccion.pdf (RIB). · Apunte: C04 — Presupuesto avanzado.
