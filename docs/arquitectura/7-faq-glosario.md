# 7 · Preguntas frecuentes y glosario

!!! abstract "Para qué es esta página"
    Las dudas que aparecen siempre en este rol, respondidas corto, y el **diccionario** de la jerga de Cost-It. Si una palabra de otra página no te cierra, buscala acá.

---

## Preguntas frecuentes

??? question "¿Cost-It es parte de Presto o de Revit?"
    De los dos, en cierto modo. Es un **módulo de Presto/RIB** que se instala como **complemento (plugin) dentro de Revit**. Genera un archivo de Presto, pero el botón `Exportar` lo apretás en la cinta de Revit. Por eso se trabaja con **Revit y Presto abiertos a la vez**.

??? question "¿Necesito licencia de Revit para usar Cost-It?"
    Para **exportar**, no: Cost-It funciona con **Revit en modo visor** (sin licencia de edición). Lo que no podés en modo visor es **editar** el modelo. Para **devolver valores al modelo** (Presto → Revit) sí hace falta la licencia full (la demo de Presto lo bloquea).

??? question "¿Cuál es la diferencia entre `Exportar` y `Añadir`?"
    **`Exportar`** crea una obra de Presto **nueva** (traspaso inicial). **`Añadir`** vuelca el modelo a la obra que **ya tenés abierta**, sin duplicarla (re-sincronización). Es la confusión #1 del rol: para actualizar un presupuesto existente, **siempre `Añadir`**.

??? question "¿Por qué una cantidad sale magenta y otra negra?"
    Por la **regla del 2%**. Si la cantidad calculada desde el prisma del objeto se parece (≤2%) a la que declara el modelo → Cost-It la **calcula** y la pinta **🟣 magenta**. Si difiere más del 2% (geometría irregular) → usa la **declarada** del modelo y la pinta **⚫ negra**. La negra conviene revisarla. _(Ver [Página 2](2-leer-y-verificar.md).)_

??? question "Una partida salió verde. ¿Está mal?"
    No necesariamente: **🟢 verde** significa que la partida tiene código pero agrupa **tipos distintos**. Es una **advertencia** de que quizá cada tipo necesita su propio precio (APU). Decidí si la **desglosás** (en Presto) o la **discriminás** (antes de exportar). _(Ver [Página 3](3-afinar-y-desglosar.md).)_

??? question "¿Por qué hay tres verdes distintos?"
    Porque Cost-It usa el color en tres pantallas diferentes: (1) verde del **resultado** = tipos mezclados en una partida; (2) verde del **match por código inferior** = la línea encontró su partida al volcar; (3) verde de **Inserción** = lo que entró/cambió en una re-sincronización. Mirá **en qué pantalla estás** para saber cuál es.

??? question "Cambié el modelo. ¿El presupuesto se actualiza solo?"
    **No.** Cost-It no sincroniza solo ni te avisa. Tenés que correr el ciclo de re-sincronización a mano (`Añadir → re-asignar → Comprobar → Buscar líneas desaparecidas → Traspasar`). Por eso Raizant designa un **responsable de re-sync**. _(Ver [Página 5](5-resincronizar.md).)_

??? question "¿Cómo verifico que una partida agrupa los elementos correctos?"
    De Presto a Revit: clic derecho sobre la línea ▸ **`seleccionar en el modelo`**. De Revit a Presto: marcá el elemento y `Cost-It ▸ Localizar`. ⚠️ En un **modelo central/federado** esto no funciona (límite de la API): hay que abrir el archivo individual que indica la columna `Archivo`.

??? question "¿Dónde pongo los códigos de mis partidas para que el modelo los lleve?"
    En Revit, en el parámetro **"Código de montaje"** del tipo (para materiales, en **"Nota clave"**). El catálogo de códigos lo generás desde Presto (`Archivo ▸ Exportar ▸ Catálogo Revit`) y se carga en Revit con `Gestionar ▸ Configuración adicional ▸ Código de montaje`. _(Ver [Página 4](4-codificar-y-volcar.md).)_

??? question "¿El precio del material sale del modelo?"
    No necesariamente. En Raizant el **precio (APU) viene del estudio/presupuesto**, no del modelo. Cost-It trae las **cantidades**; el precio se lo pone la partida del presupuesto. El presupuesto final es **cantidad del modelo × APU del estudio**.

??? question "¿Cost-It congela el presupuesto aprobado?"
    **No.** Cada re-traspaso **sobreescribe** las cantidades sin guardar una versión previa. Congelar la baseline (para medir desvío después) es **trabajo in-house**, no de Cost-It.

??? question "Trabajamos con Revit 2027. ¿Cost-It anda?"
    Pendiente de confirmar. El curso usa Cost-It **25.05.00** con Revit 25/26. Hay que **verificar con RIB** la versión de Cost-It compatible con Revit 2027 antes de comprometer el flujo. Sin compatibilidad, el puente no opera (falla silenciosa FS-11).

---

## Glosario

| Término | Qué significa |
|---|---|
| **Cost-It** | El módulo de Presto/RIB que corre como plugin de Revit y traspasa las cantidades del modelo 3D a partidas de un presupuesto de Presto (5D BIM). _(El audio del video lo transcribe como "COSID/COSIT" — es error de voz.)_ |
| **5D BIM** | El modelo 3D + tiempo (4D) + **costo** (5D). Cost-It es la pieza que le agrega el costo al modelo. |
| **`Exportar`** | Botón de Cost-It que **crea una obra de Presto nueva** con las cantidades del modelo (traspaso inicial). |
| **`Añadir`** | Botón de Cost-It que **vuelca el modelo a la obra de Presto abierta**, sin duplicarla (re-sincronización). |
| **`Localizar`** | Botón de Cost-It que, desde un elemento marcado en Revit, **salta a su partida** en Presto. |
| **Parámetro agrupador / codificación** | El parámetro de Revit (código de montaje, parámetro de usuario o código Revit) cuyo **valor define qué elementos se agrupan en cada partida**. |
| **Código de montaje** _(Assembly Code)_ | El parámetro de Revit usado **por defecto** como agrupador. Es **de tipo**: cambiarlo en un elemento lo cambia en todos los del mismo tipo. |
| **Nota clave** _(Keynote)_ | El parámetro de Revit del que Cost-It toma el código para los **materiales** (en vez del código de montaje). |
| **Partida / unidad de obra** | Cada agrupación de elementos con el mismo valor de parámetro. Es la unidad que se presupuesta (lleva su APU). |
| **Línea de medición** | Cada elemento del modelo dentro de una partida; aporta su cantidad parcial. La partida **suma** sus líneas. |
| **Prisma envolvente** | La caja imaginaria (`N`/`Longitud`/`Anchura`/`Altura`) que rodea a un objeto; base del cálculo de la cantidad magenta. |
| **Regla del 2%** | Cost-It calcula la cantidad desde el prisma (🟣 magenta) solo si difiere ≤2% de la declarada en el modelo; si no, usa la declarada (⚫ negra). **Fija del fabricante.** |
| **Semáforo del resultado** | El color sobre el `Resumen` de la partida: 🔴 sin código (por tipo) · ⬜ con código, un solo tipo · 🟢 con código, tipos mezclados. |
| **Discriminador** | Columna de `Categorías` que **separa una categoría en varias partidas** según el valor de un parámetro, **antes** de exportar (evita desglosar después en Presto). |
| **Script del código** | Pestaña de la ventana de exportación donde se escribe el **código ampliado** (`código \| unidad \| descripción \| precio`) o un **filtro JavaScript** para medir solo lo que cumple un criterio. |
| **Código ampliado (BC3 `~C`)** | Forma de escribir un código con su unidad, descripción y precio en una sola línea, con `\|` como separador. |
| **`.CostItLayout`** | Archivo de configuración de exportación (categorías, medidas, scripts, discriminadores) reutilizable como **plantilla**. |
| **Catálogo de código de montaje** | Archivo de texto tabulado que Presto exporta (`Archivo ▸ Exportar ▸ Catálogo Revit`) y Revit importa para **codificar el modelo** con las partidas del presupuesto. |
| **Mediciones temporales** | Ventana de Presto (`Ver ▸ Mediciones temporales`) donde se **importan, asignan y traspasan** las líneas del modelo al estudio, y donde se verifican los cambios en la re-sync. |
| **Asignar por código inferior** | La acción que empareja las líneas del modelo con las partidas del estudio **por código** (🟢 verde = match, gris = sin coincidencia). |
| **`Comprobar` / `Buscar líneas desaparecidas`** | Botones de verificación de la re-sync: dan acción `ninguna`/`actualizar` y `borrar`, respectivamente. |
| **Inserción** | Las filas verdes en `Mediciones temporales` que muestran lo que **entró/cambió** en un re-traspaso. |
| **Modelo central / federado** | Modelo de Revit cuyos elementos vienen de varios Revit vinculados (uno por disciplina). Se puede exportar, pero `seleccionar`/`localizar` no funcionan sobre él. |
| **Baseline** | El presupuesto aprobado que se **congela** como línea base para medir el avance. Cost-It **no** la congela: es tejido in-house. |
| **APU** | Análisis de Precio Unitario: la "receta" de precio de una partida. En Raizant lo aporta el estudio, no el modelo. |

---

📖 **Fuentes:** _Manual de Cost-it_ (RIB) · apunte interno C01 (§5 glosario de columnas, §7 glosario de términos) · transcripción `CSE - Cost It - 23/01/2026`.
