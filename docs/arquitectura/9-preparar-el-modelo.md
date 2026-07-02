# 9 · Preparar el modelo antes de exportar (avanzado)

!!! abstract "Conclusión primero"
    Las páginas 1–5 cuentan el viaje **desde el lado de Presto**. Esta lo cuenta **desde el lado del modelo**: qué tiene que dejar listo **el modelador en Revit ANTES de exportar** para que el resultado caiga ordenado y no haya que corregir a mano después. Cuatro frentes: **(1)** definir el **parámetro de agrupación** como estándar del modelo (¿código de montaje o un parámetro de ejemplar propio?) y codificar con los **códigos del presupuesto**, **(2)** dejar armada la **plantilla de códigos** (script del código) y **limpiar la configuración heredada** antes de exportar, **(3)** usar el **salto bidireccional** modelo ⇄ Presto como control de calidad del modelador, y **(4)** saber qué cambia (y qué se rompe) cuando trabajás sobre un **modelo central/federado**.

!!! tip "Antes de arrancar, tené a mano el mapa"
    Usamos la ventana de exportación de Cost-It (pestañas `Opciones`, `Categorías`, `Script del código`) y, en Revit, `Gestionar ▸ Configuración adicional ▸ Código de montaje`. Si algo no lo ubicás, abrí **[🗺 La pantalla de Arquitectura](interfaz.md)**.

!!! info "De dónde sale este contenido"
    Fuente principal: la transcripción del video **`CSE - Cost It - 23/01/2026`** (de ahí los minutos `[hh:mm]`) y la **documentación oficial de Presto (RIB)** — _Manual de Cost-it_. Complemento: apuntes internos **09** y **C01**. Esta página **complementa** (no reemplaza) a sus hermanas: donde un procedimiento ya está detallado en otra página, acá va lo esencial + el link.

---

## Por qué preparar el modelo cambia todo

El propio relator lo demuestra con dos exportaciones del **mismo modelo** `[03:40]`:

- **Sin preparar** (códigos que venían "al azar"): partidas 🔴 rojas agrupadas por tipo, códigos genéricos, verdes mezcladas → horas de corrección en Presto.
- **Modelo codificado** (cada elemento con el código de su partida del presupuesto): _"No tiene absolutamente nada que ver con el primer intento… esto ya se ve muy organizado."_ `[03:40]` El árbol sale listo para volcarse al estudio.

!!! danger "La falla silenciosa madre: exportar sin codificar"
    Si exportás un modelo sin codificación, **Cost-It no te avisa ni falla**: te genera igual un árbol — pero con partidas rojas agrupadas por tipo y códigos genéricos que **no matchean con ninguna partida del estudio**. Después, al volcar ([Página 4](4-codificar-y-volcar.md)), todo queda **gris (sin match) y fuera del presupuesto en silencio** (FS-5). La preparación del modelo no es cosmética: es la condición del puente.

!!! warning "Para codificar necesitás licencia de edición de Revit"
    El **modo visor** de Revit alcanza para **exportar**, pero **no guarda cambios**: el relator codifica tipos en la demo y al cerrar avisa _"como estoy en modo visor no voy a conservar ninguno de los cambios"_ `[03:30]`. Asignar códigos de montaje **es editar el modelo** → lo hace el modelador con licencia de Revit, no quien solo tiene el visor.

---

## Tarea 1 — Definir el parámetro de agrupación (el estándar del modelo) ⭐

**Qué es:** decidir, **antes de modelar/codificar**, qué parámetro de Revit va a agrupar los elementos en partidas — y con qué valores.

**Por qué importa:** es la decisión de gobierno de todo el flujo. En la [Página 1 (Tarea 4)](1-traspaso-inicial.md) elegís el parámetro **al momento de exportar**; acá está la mitad que le toca **al modelo**: ese parámetro tiene que **existir y estar bien cargado** en los elementos.

📖 **Fuente oficial:** Manual de Cost-it, pp. 5 y 8 (selección de códigos).

**Las dos reglas del estándar** `[00:20]`–`[00:30]`, `[03:20]`:

1. **Los valores del parámetro deben ser los códigos de las partidas del presupuesto.** _"El objetivo… es que los valores del parámetro fueran coincidentes con los distintos códigos de las partidas principales del presupuesto."_ `[03:20]` Un tipo de ventana lleva el código de la partida "Ventana PVC fijo" → al volcar, su cantidad cae exactamente ahí.
2. **Elegí bien entre parámetro de TIPO y de EJEMPLAR:**

| Opción | Qué es | Cuándo sirve | Límite |
|---|---|---|---|
| **Código de montaje** (defecto) | Parámetro **de tipo** de Revit | Cuando todos los elementos de un mismo tipo van a la **misma partida** (el caso normal) | Cambiarlo en uno lo cambia en **todos los del tipo** → no admite códigos distintos dentro del mismo tipo `[02:10]` |
| **Parámetro personalizado de ejemplar** | Un parámetro que creás vos, **individual por elemento** | Cuando elementos del **mismo tipo** deben ir a **partidas distintas** (p. ej. mismo muro en pisos que se presupuestan aparte) | El catálogo de Revit **no lo carga** (ver Tarea 2) |

!!! tip "El truco del filtro: codificá SOLO lo presupuestable"
    Práctica real de usuarios que el relator destaca `[00:30]`: crear el parámetro personalizado y cargarlo **únicamente en los elementos que interesan para el presupuesto**. Después, al exportar, se desmarca **"incluir elementos sin código"** → **solo se exporta lo codificado**. El parámetro de agrupación funciona a la vez como **filtro**: lo no presupuestable (mobiliario decorativo, vegetación…) ni siquiera viaja.

!!! note "Verificá tu decisión con el recuento ANTES de exportar"
    En `Opciones ▸ Codificación`, el botón **`elementos con código`** te dice cuántos elementos tienen valor en el parámetro elegido (en el curso: 108 de 292) y te lista los **códigos duplicados** en tipos distintos `[00:30]`. Si el número no es el que esperabas, el modelo no está listo — corregí **antes** de exportar, no después.

---

## Tarea 2 — Codificar el modelo con los códigos del presupuesto

**Qué es:** cargar en Revit el catálogo de códigos del estudio y asignar a cada tipo el código de su partida.

**Por qué importa:** es la mitad "Revit" del circuito de la [Página 4](4-codificar-y-volcar.md) — ahí está el **paso a paso completo** (Parte A). Acá, el resumen operativo para el modelador y lo que la página 4 no cubre.

📖 **Fuente oficial:** Manual de Cost-it, pp. 5–6 (catálogos).

**Resumen del circuito** `[03:20]`–`[03:30]`:

1. Presupuestos te entrega el **archivo de catálogo** (texto tabulado exportado desde el estudio con `Archivo ▸ Exportar ▸ Catálogo Revit`).
2. En Revit: **`Gestionar ▸ Configuración adicional ▸ Código de montaje ▸ Examinar`** → seleccioná el archivo → `Aceptar`. ⚠️ Guardalo en una **ubicación conocida y estable**: Revit queda **apuntando** a ese archivo `[03:20]`.
3. Por cada tipo: **editar tipo → `Código de montaje` → botón `…`** → elegí el código (ves la estructura del presupuesto agrupada por capítulos). Al ser parámetro **de tipo**, basta asignarlo a un elemento y queda en todos los de ese tipo `[03:30]`.
4. Es un **"suma y sigue"**: se repite tipo por tipo hasta cubrir todo lo presupuestable `[03:30]`. En el modelo de ejemplo del curso, además del código de montaje cargaron la **nota clave** en los materiales (es el parámetro que Presto usa para materiales).

!!! warning "Si tu estándar usa un parámetro de EJEMPLAR, el catálogo no te sirve"
    `Gestionar ▸ Configuración adicional ▸ Código de montaje` solo carga el parámetro **de tipo**. Para un parámetro de ejemplar, el relator plantea (sin ejecutarlo) exportar los códigos de las partidas a **Excel** y cargarlos con un **plugin de Revit** en el parámetro creado al efecto `[03:30]`. **Verificar el mecanismo con RIB/Revit antes de comprometerlo** — en el curso quedó como evaluación, no como procedimiento probado.

---

## Tarea 3 — Dejar lista la plantilla de códigos (script del código) y limpiar la configuración heredada

**Qué es:** preparar los códigos ampliados/scripts que la exportación va a usar — y asegurarte de que **no queden restos de una configuración anterior**.

**Por qué importa:** la ventana de exportación **recuerda** lo que se configuró antes (scripts, discriminadores, categorías duplicadas). Si exportás tu modelo codificado con la configuración de otro ensayo, el resultado sale filtrado o duplicado **sin ningún aviso**.

📖 **Fuente oficial:** Manual de Cost-it, pp. 18–26 (script del código). El detalle de discriminador, código ampliado y filtros JavaScript está en la [Página 3 (Tarea 4)](3-afinar-y-desglosar.md) — no lo repetimos acá.

**Lo que suma esta página:**

**3a · La plantilla de sintaxis (el `.txt` del material de apoyo)** `[02:50]`:

- Con el material del curso viene un **bloc de notas** ("duplicar categorías – sintaxis código") con la **sintaxis del código ampliado**: `código | unidad | descripción | precio` (precio **opcional**; separador barra vertical `|`).
- El relator trabaja **copiando y pegando desde ese `.txt`** y editándolo — no escribe de memoria. Hacé lo mismo: tené la plantilla de sintaxis del equipo a mano y **copiá los valores exactos desde el modelo** (un espacio o tilde de más en el valor del parámetro y el filtro no encuentra nada) `[03:00]`.
- Si tu partida va a un estudio con APUs, **no le pongas precio** en el código ampliado — el precio viene del estudio `[02:50]`.
- Antes de exportar, botón **`Evaluar todos`**: te muestra qué elementos van a entrar y con qué código; `result` en blanco = ese elemento **no se exporta** `[03:00]`.

**3b · Limpiar la configuración heredada antes de exportar el modelo codificado** `[03:40]`:

1. En `Opciones`: dejá **`código y descripción de montaje`** y **desmarcá `incluir elementos sin código`** (filtrás lo no presupuestable).
2. En `Categorías`: **borrá el contenido de `Discriminador`** si quedó de otro ensayo (el desglose ya viene resuelto por la codificación).
3. En `Script del código`: **borrá los scripts** que no apliquen a esta exportación.
4. **Eliminá las categorías duplicadas** que no necesites: clic derecho sobre la categoría duplicada → **`Eliminar`**.

!!! warning "La configuración vieja contamina en silencio"
    En el propio curso, el relator tiene que deshacer su ejemplo anterior (quitar el discriminador `tipo`, borrar dos scripts y eliminar la categoría duplicada de muros) **antes** de exportar el modelo codificado, porque si no _"me va a obstaculizar el ejemplo"_ `[03:40]`. Un script olvidado **filtra elementos que sí querías** (el `null` los excluye) y una categoría duplicada **duplica cantidades** — y la exportación termina "bien" igual. La cura de fondo es la Tarea 5: plantillas oficiales.

---

## Tarea 4 — Saltar del modelo a Presto y volver (el QA del modelador)

**Qué es:** usar la navegación bidireccional para verificar, elemento por elemento, que tu codificación manda cada cosa a la partida correcta.

**Por qué importa:** el paso a paso completo está en la [Página 2 (Tarea 2)](2-leer-y-verificar.md). Acá, el uso que le toca **al modelador**: después de exportar un modelo recién codificado, no entregues sin este chequeo.

📖 **Fuente oficial:** Manual de Cost-it, p. 28 (Localizar).

**El chequeo en dos direcciones** `[01:00]`–`[01:10]`:

- **Del modelo a Presto** _(¿a qué partida fue a parar este elemento?)_: marcá el elemento en Revit → cinta **`Cost-It` ▸ `Localizar`** → Presto salta a su partida/línea. Si cae en una partida que no es la suya, **el código de ese tipo está mal**.
- **De Presto al modelo** _(¿qué elementos tiene esta partida?)_: seleccioná la partida (o el capítulo) → clic derecho ▸ **`seleccionar en el modelo`** → en Revit, **"aislar elementos"** para verlos solos y **"editar tipo"** para confirmar el código. Un intruso a la vista = un tipo codificado con el código equivocado.

!!! tip "Podés reordenar Presto sin miedo"
    El vínculo partida ⇄ elemento **nunca se pierde**, aunque en Presto se renombre, recodifique o mueva la partida `[01:10]`. Lo que sí lo limita es el modelo central — ver Tarea 6.

---

## Tarea 5 — Guardar la configuración como plantilla reutilizable (`.CostItLayout`)

**Qué es:** conservar toda la configuración de exportación (categorías marcadas, medidas, discriminadores, scripts, duplicados) en un archivo que se recupera con un clic.

**Por qué importa:** el cómo está en la [Página 3 (Tarea 5)](3-afinar-y-desglosar.md); acá, el **para qué a nivel de equipo**. La pregunta la hizo un alumno del curso: _"¿esta configuración queda guardada o va a haber que hacerla cada exportación?"_ — y la respuesta del relator es la clave `[03:10]`:

> _"Uno puede generar una plantilla con las configuraciones, porque siempre vamos a soler trabajar más o menos en los mismos tipos de modelos Revit y siempre hacer las mismas funciones."_ `[03:10]`

**Paso a paso** `[03:10]`:

1. Con la configuración lista, en la barra de la pestaña `Categorías`: botón **disquet** (guardar) → nombrala → genera el archivo **`.CostItLayout`**.
2. En la próxima exportación (mismo tipo de modelo): botón **recuperar configuración** → elegí el `.CostItLayout` → toda la configuración vuelve.

!!! danger "Regla Raizant: la plantilla oficial es LA configuración, no una sugerencia"
    Una plantilla `.CostItLayout` **por tipo de modelo** (versionada, con nombre claro, p. ej. `Raizant-vivienda-v1.CostItLayout`) resuelve de raíz dos fallas silenciosas: la configuración perdida entre sesiones (FS-10) y la configuración heredada que contamina (Tarea 3b). El flujo correcto es **cargar plantilla → exportar**, nunca "configurar de memoria". Crear y custodiar esas plantillas es parte del estándar BIM del equipo.

---

## Tarea 6 — Modelo central/federado: qué cambia en Cost-It

**Qué es:** saber cómo se comporta Cost-It cuando el modelo abierto **reúne varios Revit vinculados** (lo normal en proyectos ejecutivos, con un modelo por disciplina).

**Por qué importa:** los hechos base están en la [Página 2 (Tarea 4)](2-leer-y-verificar.md). Acá, la vista completa para decidir el flujo de trabajo del equipo.

!!! note "«Federado» y «central»: el curso los usa como sinónimos"
    El relator habla de _"modelos centrales o modelos federados, como le quieran llamar"_ `[02:00]` — en el curso son **la misma situación**: un Revit con elementos que provienen de otros archivos Revit vinculados. La distinción fina entre "modelo central" (worksharing de Revit) y "modelo federado" (vinculación de disciplinas) **no está desarrollada en las fuentes** → si Raizant va a trabajar con worksharing, **verificar el comportamiento exacto en Presto/Revit con RIB**.

**Qué SÍ funciona y qué NO** `[01:50]`–`[02:00]`:

| Función | ¿Sobre el central/federado? | Detalle |
|---|---|---|
| **`Exportar` / `Añadir`** | ✅ Funciona | Trae todos los elementos, también los vinculados |
| **Saber de qué archivo vino cada línea** | ✅ Funciona | Esquema `Localización BIM` → columna **`Archivo`** (p. ej. "esto viene del Revit 243") |
| **`seleccionar en el modelo`** | ❌ NO funciona | No marca nada, **sin mensaje de error** |
| **`Localizar`** | ❌ NO funciona | Ídem |

**El workaround oficial** `[02:00]`: abrí el **archivo Revit individual** que indica la columna `Archivo`, dejalo como **ventana activa**, y ahí sí `seleccionar en el modelo` / `Localizar` marcan el elemento — pero en el archivo de origen, no en el central.

!!! warning "Por qué no lo arreglan: es la API de Revit, no Presto"
    _"La respuesta clásica de la gente de Revit Spain es porque la API de Revit no lo permite… es una limitante de la API de Revit que eso no se pueda hacer con el central."_ `[02:00]` No esperes que una versión nueva de Cost-It lo resuelva: el límite está aguas arriba.

!!! danger "La consecuencia para el flujo Raizant"
    Si el equipo trabaja con modelos por disciplina, el **QA bidireccional de la Tarea 4 no funciona sobre el central** — y falla **en silencio** (FS-8). El procedimiento del equipo debe fijar: **(1)** conservar siempre visible la columna `Archivo`, y **(2)** que la verificación visual se haga **abriendo el archivo individual de origen**. Cómo interactúa esto con la re-sincronización (`Añadir` sobre una obra generada desde el central) no se demuestra en las fuentes → **verificar en Presto/Revit** antes de fijar el procedimiento.

---

## 🎥 Mirá el video

| Tema | Minuto |
|---|---|
| Parámetro de agrupación: tipo vs personalizado, filtro "sin código" | `[00:20]`–`[00:30]` |
| Salto bidireccional (Localizar / seleccionar en el modelo) | `[01:00]`–`[01:10]` |
| Modelo central/federado: columna `Archivo`, límite de la API | `[01:50]`–`[02:00]` |
| Conflicto del código de montaje (parámetro de tipo) | `[02:10]` |
| El `.txt` de sintaxis del código ampliado | `[02:50]`–`[03:00]` |
| Guardar/recuperar `.CostItLayout` (pregunta de alumno) | `[03:10]` |
| Codificar el modelo: catálogo + valores = códigos del presupuesto | `[03:20]`–`[03:30]` |
| Limpiar configuración heredada + exportar el modelo codificado | `[03:40]` |

> Video fuente: `CSE - Cost It - 23/01/2026.mp4` (4h 11min). _Complemento de la documentación oficial citada en cada tarea._

---

## ⚠️ Lo que Cost-It NO te avisa (resumen)

- **Exportar sin codificar "funciona"** — pero todo cae en partidas rojas/genéricas que después no matchean con el estudio. _(Arriba de todo)_
- **El modo visor no guarda la codificación** que asignes — codificar exige licencia de edición de Revit. _(Antes de empezar)_
- **La configuración heredada (scripts, discriminadores, duplicados) contamina la siguiente exportación** sin aviso. _(Tarea 3)_
- **En modelo central, `seleccionar`/`Localizar` no marcan nada** y no hay error — el QA visual falla en silencio. _(Tarea 6)_

👉 Todas, con cómo blindarte, en [6 · Reglas de oro y fallas silenciosas](6-reglas-de-oro.md).

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá lo aprendido"
    _(Con un modelo de prueba y el estudio de BLEND a mano.)_

    1. **Definí el estándar:** listá 3 tipos del modelo y decidí, para cada uno, si el código de montaje (de tipo) alcanza o si necesitarías un parámetro de ejemplar (¿hay elementos del mismo tipo que van a partidas distintas?).
    2. **Codificá 3 tipos** con el catálogo del estudio (`Gestionar ▸ Configuración adicional ▸ Código de montaje`) usando los códigos reales de las partidas de BLEND.
    3. En la ventana de exportación, pulsá **`elementos con código`** y verificá que el recuento coincida con lo que codificaste. Desmarcá "incluir elementos sin código" y exportá.
    4. **QA bidireccional:** en Presto, `seleccionar en el modelo` sobre una partida (¿están solo los elementos correctos?) y, en Revit, `Localizar` sobre un elemento (¿cae en su partida?).
    5. **Guardá la configuración** como `Raizant-prueba-v1.CostItLayout`, cerrá todo, volvé a abrir y **recuperala**: la configuración tiene que volver intacta.

    **Cómo sabés que salió bien:** el árbol sale sin partidas 🔴 rojas, cada elemento salta a su partida correcta en ambas direcciones, y tenés una plantilla que reproduce la exportación sin configurar nada de memoria.

---

📖 **Fuentes oficiales (RIB):** _Manual de Cost-it_, pp. 5–8, 18–26 y 28. · **Complementos internos:** apuntes 09 y C01 (casos 4, 7, 9, 11–13) · transcripción `CSE - Cost It - 23/01/2026`.
