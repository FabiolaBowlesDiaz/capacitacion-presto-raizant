# 1 · Traer el modelo a Presto (traspaso inicial)

!!! abstract "Conclusión primero"
    Acá aprendés el **camino base de Cost-It**: tomar un modelo de Revit y, con un par de decisiones, generar un **presupuesto con cantidades** en Presto. El botón clave es **`Exportar`** (crea una obra de Presto **nueva**). Antes de pulsarlo elegís **qué parámetro agrupa los elementos en partidas** (la codificación) y **qué categorías** llevás. Cuando termina, en Presto aparece el árbol con sus capítulos, partidas y líneas de medición.

!!! tip "Antes de arrancar, tené a mano el mapa"
    Las instrucciones usan _"la pestaña `Cost-It` de la cinta"_, _"la ventana de exportación"_, _"el árbol de Presto"_. Si algo no lo ubicás, abrí en otra pestaña **[🗺 La pantalla de Arquitectura](interfaz.md)**.

!!! warning "Requisito de licencia — sin esto no podés avanzar"
    El menú `Cost-It` **solo aparece en Revit si el complemento está instalado y la licencia incluye el módulo Cost-It**. Si no ves la pestaña `Cost-It` en la cinta de Revit, no vas a poder exportar. **Verificá que el módulo Cost-It esté incluido en la licencia** antes de operar este rol (es un requisito a confirmar al contratar/renovar).

!!! info "De dónde sale este contenido"
    Fuente principal: **documentación oficial de Presto (RIB)** — _Manual de Cost-it_ (pp. 7–14). Se complementa con el apunte interno **C01** (casos 1–5) y la transcripción del video **`CSE - Cost It - 23/01/2026`** (de ahí los minutos `[hh:mm]`).

---

## Antes de empezar: lo que necesitás

| Necesitás | Por qué |
|---|---|
| **El módulo Cost-It activo + el complemento en Revit** | Sin el menú `Cost-It` en la cinta de Revit no hay botón `Exportar` |
| **El modelo abierto en Revit, con la vista 3D activa** | Cost-It exporta lo que está en la vista. Revit en **modo visor** (sin licencia de edición) **alcanza para exportar**, no para editar |
| **NO tener una obra de Presto abierta** | `Exportar` crea una obra **nueva**; tener otra abierta confunde el resultado |
| **NO dejar elementos seleccionados en Revit** | Si hay algo seleccionado, Cost-It **solo exporta lo seleccionado**, no el modelo entero |

!!! note "Dato oficial: qué se exporta exactamente"
    El Manual lo aclara: _"Solo se exporta la información de los elementos seleccionados. Si no hay selección se exportan **todos los elementos visibles en la vista** desde la que se exporta."_ 📖 _(Manual de Cost-it, p. 7)_. Por eso conviene **crear una vista específica** con exactamente lo que querés medir; en caso de duda, no dejes nada seleccionado.

---

## Tarea 1 — Verificar el módulo y abrir el modelo

**Qué es:** confirmar que Cost-It está activo y dejar el modelo listo.

📖 **Fuente oficial:** Manual de Cost-it, p. 1–2 (instalación y activación del complemento).

**Paso a paso** `[00:00]`:

1. **En Presto:** abrí la ventana inicial → **`Activación`** → confirmá que el **módulo "Cost-It"** figura **operativo**. Cerrá esa ventana.
2. **En Revit:** mirá la **cinta de arriba** y confirmá que está la pestaña **`Cost-It`**. Si no está, el complemento no se instaló (se instala con **Revit cerrado**, según el manual que viene con la licencia).
3. Abrí tu modelo y, en el **navegador de proyectos** (panel izquierdo de Revit), dejá activa una **vista 3D**.

!!! tip "Cómo sabés que salió bien"
    Ves la pestaña `Cost-It` en la cinta de Revit **y** el módulo aparece operativo en Presto. ✅

---

## Tarea 2 — Lanzar el traspaso (`Exportar`) y leer Estadísticas

**Qué es:** disparar la lectura del modelo y ver un primer resumen.

📖 **Fuente oficial:** Manual de Cost-it, p. 7 (Exportar) y p. 8 (Estadísticas).

**Dónde estás:** en **Revit**, en la pestaña `Cost-It` de la cinta.

**Paso a paso** `[00:10]`:

1. **Hacé clic en una zona vacía** del modelo para **no dejar nada seleccionado** (si no, solo exporta lo marcado).
2. En la cinta, **pestaña `Cost-It` ▸ botón `Exportar`**. _("El corazón de Cost-It; todos los otros botones son complementarios.")_ Aparece una **barra de avance** y después la **ventana de exportación**.
3. Mirá la pestaña **`Estadísticas`**: es un **gráfico circular** que te dice **qué categoría tiene más elementos** (en el modelo de ejemplo, lo más numeroso son los **muros**).

!!! note "Tené paciencia con modelos grandes"
    La lectura **tarda en proporción al tamaño del modelo y al hardware** (la ventana corre sobre el motor de Revit). Un modelo grande no exporta tan rápido como uno de ejemplo. `[00:10]`

---

## Tarea 3 — Configurar `Opciones` (qué incluir y cómo medir)

**Qué es:** decidir qué información se trae y en qué unidad sale cada cosa.

📖 **Fuente oficial:** Manual de Cost-it, pp. 8–9 (Opciones, Tipo de medición, Líneas de medición, huecos, subcapítulos).

**Dónde estás:** pestaña **`Opciones`** de la ventana de exportación.

**Paso a paso** `[00:20]`:

1. Pulsá el botón **`Defecto`** (abajo) para partir de las opciones predeterminadas.
2. En la **sección `Incluir`**, lo **mínimo obligatorio** es **`líneas de medición`** — sin esto **no hay cantidades**. Conviene sumar también **`parámetros de tipos`** y **`parámetros de elementos`** (después sirven para desglosar y para devolver valores).
3. Lo demás (referencias espaciales, miniaturas, familias, vistas, IFC…) es **opcional**: solo agrega datos para consultar. **Ojo: cuantas más cosas marques, más tarda la exportación.**
4. **Tipo de medición** (cómo se referencian los elementos): elegí entre **`tipos`** / **`materiales`** / **`ambos`**. Para empezar, dejá **`tipos`**.
5. _(Opcional)_ **"Descontar huecos mayores de…"**: con el umbral en **`0`**, cualquier hueco definido entra como **línea de medición negativa** (resta del muro).
6. _(Opcional)_ **"Subcapítulos de familias"**: agrega un nivel intermedio de subcapítulos. Por defecto la estructura es solo **capítulos y partidas**.

!!! note "Dato oficial tranquilizador"
    Lo que marques en `Incluir` **no cambia las cantidades**, solo agrega columnas consultables: _"Las opciones… no producen resultados diferentes, solo limitan la información que se exporta para acelerar el proceso."_ 📖 _(Manual de Cost-it, p. 8)_. Es decir: si dudás, podés probar con un modelo chico y después ajustar.

---

## Tarea 4 — Elegir el parámetro agrupador (la codificación) ⭐

**Qué es:** la decisión más importante — **qué parámetro de Revit convierte a los elementos en partidas**.

📖 **Fuente oficial:** Manual de Cost-it, pp. 5 y 8 (Selección de códigos; código de montaje vs nota clave; lista de elementos y duplicados).

**Dónde estás:** sección **`Codificación`** (o **`Selección de códigos`**) dentro de `Opciones`.

**Concepto:** **cada valor distinto** del parámetro que elijas genera **una partida** que agrupa los elementos con ese mismo valor. _"Código de montaje B01, eso es una partida. Código de montaje B02, otra partida."_ `[00:20]`

**Paso a paso** `[00:20]`–`[00:30]`:

1. Elegí de dónde sale el código de cada partida. Tres opciones:
   - **`Código y descripción de montaje`** _(el de defecto)_: usa el parámetro **"código de montaje"** de Revit (es **de tipo**). Para **materiales**, Presto usa siempre el parámetro **"Nota clave"**.
   - **`Parámetro elegido por el usuario`**: escribís el nombre de **cualquier** parámetro del modelo (incluso uno personalizado que creaste para agrupar). Cost-It te autocompleta.
   - **`Código Revit`** _(última opción)_: agrupa por el **identificador interno** de cada tipo → trae todo agrupado por tipo y **inhabilita** las otras opciones.
2. **Casilla "Incluir elementos sin código de unidad de obra asignado"**:
   - **Desmarcada** → los elementos **sin** valor en el parámetro **no se exportan** (filtro útil para llevar solo lo presupuestable).
   - **Marcada** → se exportan, agrupados **por tipo**, con el `Resumen` en **🔴 rojo**.
3. Pulsá el botón **`elementos con código`** (o "Actualiza el número de elementos con código"): hace un **recuento** y te avisa cosas. Ejemplo del curso: 108 de 292 elementos con código de montaje; 104 materiales (12 con nota clave); y el aviso **"códigos de montaje duplicados: 4"**.
4. Hacé clic en el enlace de **duplicados** para ver qué códigos se repiten en **elementos de distinto tipo** (p. ej. `B10`, `C1010`). Esto te **anticipa** qué partidas saldrán **🟢 verdes** en el resultado (tipos mezclados, [Página 3](3-afinar-y-desglosar.md)).

!!! danger "Recordá: el código de montaje es un parámetro DE TIPO"
    Cambiarlo en un elemento lo cambia en **todos los del mismo tipo**. **No sirve** cuando elementos del mismo tipo deben ir a partidas distintas → ahí usás un **parámetro de ejemplar** personalizado. _"Tiene que ser otro que sea individual para cada elemento."_ `[02:10]`

!!! note "Dato oficial sobre los elementos sin código"
    _"En los elementos sin código de unidad de obra asociado se usa el código interno de Revit al exportar y **aparecen en el presupuesto en estado rojo**."_ 📖 _(Manual de Cost-it, p. 5)_. El rojo es tu señal de "esto no tiene código, revisalo".

---

## Tarea 5 — Filtrar `Categorías` y ejecutar la exportación

**Qué es:** elegir qué grupos de elementos llevás y disparar el traspaso final.

📖 **Fuente oficial:** Manual de Cost-it, pp. 9–14 (Categorías y opciones de exportación).

**Dónde estás:** pestaña **`Categorías`** de la ventana de exportación.

**Paso a paso** `[00:40]`–`[00:50]`:

1. Verificá que los **checkmarks de arriba** (`model`, `analytical`, `annotation`, `internal`, `anidadas`, `extra`, `sin elementos`) estén **todos marcados**. ⚠️ Si los desmarcás, la lista de categorías puede salir **vacía**.
2. **Marcá/desmarcá** categorías (columna `exportar`) para filtrar qué grupos van a Presto. Usá el botón **`vista preliminar`** para ver los elementos de una categoría antes de decidir.
3. Pulsá el botón **`Exportar`** (abajo) → se abre el cuadro de **guardado del archivo de Presto** (el nombre propuesto es modelo + fecha/hora). Elegí carpeta y **`Guardar`**.
4. Arranca la exportación (barra de avance abajo). **Señal de fin: cuando la ventana de Cost-It se cierra sola, terminó.** ✅

!!! danger "No confundas `Exportar` con `Añadir`"
    En esta primera vez usás **`Exportar`** (crea la obra nueva). El botón **`Añadir`**, que está al lado, es para **re-sincronizar** sobre una obra ya abierta — lo vas a usar más adelante ([Página 5](5-resincronizar.md)), no ahora. 📖 _(Manual de Cost-it, p. 7.)_

---

## Tarea 6 — Leer el resultado en Presto

**Qué es:** abrir el presupuesto que se generó y entender el semáforo de colores.

📖 **Fuente oficial:** Manual de Cost-it, pp. 14–15 (resultado en Presto, líneas de medición).

**Dónde estás:** ahora en **Presto**.

**Paso a paso** `[00:50]`–`[01:20]`:

1. En Presto, andá a la pestaña **`Árbol`** → menú de **nodos** → mostrá **`Partidas`**. Aparece la estructura: **capítulos** (= las categorías de Revit) con **partidas** anidadas.
2. Abrí la subventana **`Mediciones`** (la franja de abajo): ahí ves las **líneas de medición** de la partida seleccionada (una por elemento del modelo).
3. **Leé el semáforo del resultado** (el color sobre el `Resumen` de cada partida):

| Color | Significa | Qué hacer |
|---|---|---|
| 🔴 **Rojo** | Elementos **sin código** (Presto los agrupó por tipo) | Faltó codificar → revisar en el modelo |
| ⬜ **Blanco** (texto negro) | Con código y de **un solo tipo** | OK, no hay nada que hacer |
| 🟢 **Verde** | Con código pero de **tipos distintos** | Revisar si conviene **desglosar** ([Página 3](3-afinar-y-desglosar.md)) |

!!! tip "Cómo sabés que el traspaso salió bien"
    Tenés un árbol con capítulos = tus categorías de Revit, cada partida con sus líneas de medición y una cantidad sumada. Las partidas **blancas** están listas; las **rojas** y **verdes** te están pidiendo una revisión (próximas páginas).

---

## 🎥 Mirá el video

| Tema | Minuto |
|---|---|
| Verificar licencia/plugin, abrir el modelo | `[00:00]` |
| Lanzar `Exportar`, leer Estadísticas | `[00:10]` |
| Opciones: Incluir, tipo de medición, huecos | `[00:20]` |
| Codificación: parámetro agrupador + duplicados | `[00:20]`–`[00:30]` |
| Categorías + ejecutar la exportación | `[00:40]`–`[00:50]` |
| Leer el árbol y el semáforo en Presto | `[00:50]`–`[01:20]` |

> Video fuente: `CSE - Cost It - 23/01/2026.mp4` (4h 11min). Relator de soporte de Presto/RIB. _El video es complemento: la referencia primaria es la documentación oficial citada en cada tarea. (El audio transcribe "Cost-It" como "COSID/COSIT" — es error de voz.)_

---

## ⚠️ Lo que Cost-It NO te avisa (resumen)

- **Si dejás algo seleccionado en Revit, solo exporta eso** → podés traer medio modelo sin darte cuenta. _(Antes de empezar)_
- **Los elementos sin código se cuelan en rojo o quedan fuera** según una casilla fácil de pasar por alto. _(Tarea 4)_
- **Códigos duplicados en tipos distintos → partidas verdes** que quizá necesitan APUs distintos. _(Tarea 4 y 6)_
- **El código de montaje es de tipo** → no sirve para códigos distintos en elementos del mismo tipo. _(Tarea 4)_

👉 Todas, con cómo blindarte, en [6 · Reglas de oro y fallas silenciosas](6-reglas-de-oro.md).

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá lo aprendido"
    Sobre un modelo de prueba _(con una licencia que tenga el módulo Cost-It)_:

    1. Abrí el modelo en Revit con una **vista 3D** activa y hacé clic afuera para no dejar nada seleccionado.
    2. `Cost-It ▸ Exportar` → en `Estadísticas`, identificá **cuál es la categoría más numerosa**.
    3. En `Opciones`, dejá **`líneas de medición`** marcado, tipo de medición en **`tipos`**, y elegí **`código de montaje`** como codificación.
    4. Pulsá **`elementos con código`** y anotá **cuántos elementos tienen código** y **cuántos duplicados** hay.
    5. En `Categorías`, dejá solo **Muros** y **`Exportar`**. En Presto, abrí el `Árbol` y contá cuántas partidas salieron **🔴 rojas**, **⬜ blancas** y **🟢 verdes**.

    **Cómo sabés que salió bien:** en Presto aparece un capítulo "Muros" con sus partidas y, abajo, las líneas de medición con sus cantidades.

---

📖 **Fuentes oficiales (RIB):** _Manual de Cost-it_, pp. 5–15. · **Complementos internos:** apunte C01 (casos 1–5) · transcripción `CSE - Cost It - 23/01/2026`.
