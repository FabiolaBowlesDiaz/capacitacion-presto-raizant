# 7 · Diseñar informes (plantillas propias)

!!! abstract "Conclusión primero"
    Hasta acá aprendiste a **imprimir** los informes que Presto trae de fábrica ([Básico, Tarea 10](1-basico.md#tarea-10-sacar-un-informe)). Acá aprendés a **crearlos y personalizarlos**: Presto te autogenera una plantilla desde la pantalla que estés mirando, y con el **Diseñador** le agregás datos por coordenadas, filtros, subtotales, preguntas al usuario y totales con impuesto. Es la herramienta con la que Raizant va a armar su **set propio de informes** — diseñados una vez, usados en todas las obras.

!!! tip "¿Te perdés con los menús? Tené el mapa a mano"
    El Diseñador se abre desde la cinta de Presto (zona 9 del **[🗺 mapa de la pantalla](interfaz.md)**), pero adentro tiene **sus propios menús**: `Archivo`, `Inicio`, `Ver`, `Herramientas` y `Sección`.

!!! info "De dónde sale este contenido — y una advertencia de honestidad"
    Video **Informes avanzados** (`infos_av_03_12_2025.mp4`, 3h 25min, Presto v25) + apuntes 04 y C10. Cada paso cita el minuto `[hh:mm]` del video. ⚠️ **De este video no tenemos capturas de pantalla**: los nombres de botones y menús salen del audio de la clase. Lo dudoso está marcado como **"verificar en Presto"** — si al seguir un paso el botón se llama distinto, avisá para corregir la página.

---

## Antes de empezar: lo que necesitás

| Necesitás | Por qué |
|---|---|
| Lo del [Presupuesto básico](1-basico.md) y [avanzado](3-avanzado.md) | El curso da por sabidos el filtro por expresión, las naturalezas como números y la tabla de redondeos |
| **La ventana `Entidades` cargada** (emisor + cliente) | Viene **vacía** y nadie la llena sola; sin esto los informes formales salen sin emisor ni destinatario `[01:10]` |
| Un logo en JPG/PNG en disco | Si vas a insertar el logotipo de Raizant |
| Saber cuál es tu **impresora predeterminada de Windows** | La orientación y el tamaño de papel del informe dependen de ella `[00:20]` |

---

## Tarea 1 — Generar una plantilla autogenerada desde la vista activa

**Qué es:** cada vez que abrís el Diseñador, Presto **crea solo una plantilla** ("Informe 1") copiando **la vista que tenés en pantalla en ese momento** — con las mismas columnas visibles. Es el punto de partida de cualquier informe nuevo.

**Por qué importa:** no arrancás de una hoja en blanco. Si armás en pantalla la vista que querés como informe (columnas, esquema), Presto te hace el 80% del trabajo. De hecho, **todos los informes de APU de fábrica nacieron de esta plantilla** `[00:10]`.

**Paso a paso** `[00:00]`:

1. Posicionate en la vista que querés convertir en informe (ej. la pestaña **`Presupuesto`**, o la pestaña **`Conceptos`** con un esquema como "mano de obra presupuesto").
2. En la cinta: **`Inicio ▸ Diseñar`** → se abre la ventana de diseño con una pestaña **"Informe 1"** que replica tus columnas.
3. Para ver cómo queda: pulsá el **interruptor de Vista preliminar** — está **entre el botón Guardar y el botón Deshacer** (no vayas por el menú Archivo, este es el acceso directo). El botón **lupa** agranda la vista.
4. Para salir de la vista preliminar usá su botón **`Cerrar`** — esa ventana **no tiene la X de Windows**; `Cerrar` es la única salida `[00:00]`.

!!! tip "Ideá el informe en la pantalla, no en el Diseñador"
    Si querés un informe que muestre "la partida arriba y sus recursos abajo", ponete en la vista de concepto + inferiores y recién ahí dale `Diseñar`: la plantilla sale con ese patrón (es el origen de los informes de APU) `[00:10]`.

---

## Tarea 2 — El Diseñador: las secciones de una plantilla

**Qué es:** una plantilla no es una hoja lisa: está dividida en **franjas horizontales (secciones)**, y cada sección se imprime en un momento distinto del informe. Entender esto es entender cualquier informe de Presto.

| Sección | Cuándo se imprime |
|---|---|
| **Prólogo** | Al principio — la portada `[03:00]` |
| **Inicio** | Solo en la **primera página** `[03:00]` |
| **Cabecera** | Encabezado que se repite en cada página |
| **Separador 1** | Al abrir cada grupo (ver Tarea 5) |
| **Elemento 1** | El **cuerpo** del informe: una fila por cada concepto que pase el filtro. Puede haber varias |
| **Fin de separador 1** | Al cerrar cada grupo — acá van los **subtotales** |
| **Pie** | Pie de cada página |
| **Final** | Solo en la **última página** — el total general `[03:00]` |
| **Epílogo** | La contraportada `[03:00]` |
| **Página maestra** | Un "preimpreso" (membrete) sobre el que se imprime todo lo demás `[03:00]`–`[03:10]` |

Las secciones se agregan desde el menú **`Sección`** (un interruptor por cada una) `[03:00]`. Las secciones `Elemento` conviene **dejar que Presto las cree solo** al autogenerar la plantilla — ponerlas a mano es complicado `[03:00]`. Hay también una sección `Búsqueda` que está en desuso (el fabricante la retiraría — verificar en Presto) `[03:00]`.

**La ventana Propiedades** `[00:20]`: doble clic sobre cualquier recuadro abre una ventana lateral con sus propiedades (también con el botón **`Propiedades`**). Lo que muestre depende de dónde cliquees:

- Clic en un **recuadro** → propiedades del control (origen, formato, borde…).
- Clic en el nombre de una **sección** → propiedades de la sección (tabla, máscara, selección…).
- Clic **fuera del área de impresión** → propiedades **generales de la plantilla**: anchura (cm), **orientación** (vertical/horizontal — usá horizontal si tenés muchas columnas) y tamaño de papel (recomendado: "el definido en la impresora") `[00:20]`.

---

## Tarea 3 — Cuadros de texto: literal vs fórmula, e invocar un dato por coordenadas

**Qué es:** el contenido de un informe vive en **controles** (cuadros de texto, líneas, rectángulos, gráficos). Lo que imprime cada cuadro se define en su propiedad **`Origen`**, y ahí manda una regla de oro:

!!! danger "Las comillas mandan: con comillas = texto plano, sin comillas = fórmula"
    En `Origen`, un texto **entre comillas** (`"Listado de insumos:"`) se imprime **literal**. **Sin comillas**, Presto lo interpreta como **expresión** (fórmula que trae un dato). Por eso cambiar títulos y encabezados de cualquier informe es fácil y seguro: editás lo que está entre comillas y no tocás ninguna fórmula `[00:30]`–`[00:40]`.

**Crear un cuadro y editar su contenido** `[00:50]`, `[00:30]`–`[00:40]`:

1. **`Herramientas ▸ Cuadro de texto`** → el cursor pasa a "modo dibujo": arrastrá para dibujarlo; al soltar vuelve a modo selección.
2. Doble clic en el cuadro → Propiedades → **`Origen`** → botón **tres puntos** → se abre el **Generador de expresiones** (el mismo del filtro por expresión del curso avanzado).
3. Para ganar tiempo: **Ctrl+C / Ctrl+V** duplica cuadros ya formateados; las **flechas del teclado** los mueven fino `[00:50]`–`[01:00]`.

**Invocar un dato por coordenadas** `[01:10]`–`[01:20]` — el mecanismo central del Diseñador. Presto es, en el fondo, una base de datos: para traer una celda al informe le das **dos coordenadas**:

- **1ª coordenada = la columna** (campo interno): `Conceptos.Resumen`, `Conceptos.Pres`…
- **2ª coordenada = el identificador** del concepto, que puede ser una de dos:

| Identificador | Sintaxis | Cuándo sirve |
|---|---|---|
| **Naturaleza** (número, **sin comillas**) | `Conceptos.Resumen[NAT==110]` | Solo para conceptos **únicos** (raíz, proyectista) |
| **Código** (**entre comillas**) | `Conceptos.Resumen[Código=="O00733"]` | Para **cualquier** concepto — el código es único |

Ejemplos verificados en el video:

- `Conceptos.Resumen[NAT==0]` → el **nombre de la obra** (NAT 0 = concepto raíz; `[NAT==0].Pres` = total del presupuesto) `[01:00]`–`[01:10]`.
- `Conceptos.Resumen[NAT==110]` → el **cliente/mandante** (110 = proyectista, cargado en `Entidades`) `[01:10]`.
- `Conceptos.TOT3[Código=="O00764"]` → el importe total de un concepto puntual (el nombre interno `TOT3` sale del audio — verificar en Presto) `[01:20]`.

!!! warning "La ventana Entidades viene vacía — y nadie te avisa"
    Los datos de la **empresa constructora** (emisor) y del **proyectista** (cliente) que imprimen casi todos los informes formales viven en la ventana **`Entidades`**, que **viene vacía en toda obra nueva**: *"si tú no te metes en esta ventana, esta ventana va a permanecer vacía"* `[01:10]`. Cargala como parte del setup de cada obra: un concepto con naturaleza *empresa constructora* (Raizant) y uno con naturaleza *proyectista* (el cliente). En informes de España se usa *promotor*; para la localización Bolivia, verificar en Presto cuál aplica.

**Otras propiedades útiles del cuadro** `[00:30]`–`[00:40]`: **`Auto extensible`** (Sí = si el texto no entra, salta de línea; No = **se corta sin avisar**), **`Visible`** (hay cuadros invisibles que solo hacen cálculos internos), **`Estilo de fondo`** (el color de fondo NO se imprime hasta que lo pasás de invisible a **visible**) y **`Formato`** (en celdas numéricas, cambialo de `auto` a **`numérico`** — los decimales se atan a la tabla de redondeos de la obra `[01:40]`–`[01:50]`).

**El logo de Raizant** `[01:30]`: `Herramientas ▸ Gráfico` → dibujá el control → Propiedades → **`Archivo`** → tres puntos → elegí el JPG/PNG. Presto **incrusta una miniatura** en la plantilla: el logo viaja con ella aunque el destinatario no tenga el archivo.

---

## Tarea 4 — Filtrar y seleccionar qué se imprime

**Qué es:** decidir qué conceptos entran al informe. Se configura en las propiedades de la sección **`Elemento 1`** `[01:50]`–`[02:10]`:

| Propiedad | Qué hace |
|---|---|
| **`Tabla`** | De qué tabla interna lee (default: **`Conceptos`** — no la cambies si querés el presupuesto) |
| **`Clave`** | El identificador (default: **`Código`**; la alternativa es la naturaleza) |
| **`Máscara`** | Filtra por el **inicio del código**: `"O008*"` (entre comillas, asterisco al final, respetando mayúsculas) imprime solo los códigos que empiezan por `O008` `[02:00]` |
| **`Selección`** | Filtra por **expresión**: `Conceptos.Nat==6` imprime solo la mano de obra `[02:00]` |

Las naturalezas que usa este video (¡son números!): **6** = mano de obra, **7** = maquinaria, **8** = material, **0** = concepto raíz, **110** = proyectista `[02:00]`.

**Combinar grupos con el "o lógico" `||`** `[02:00]`–`[02:10]`:

```
Conceptos.Nat==8 || Conceptos.Nat==7 || Conceptos.Nat==6
```

imprime materiales, maquinaria y mano de obra a la vez. `||` se lee "o": entra al informe todo concepto que cumpla **cualquiera** de las condiciones.

!!! tip "Presto autogenera más expresión de la necesaria"
    Al abrir `Selección` en una plantilla autogenerada vas a ver una expresión larga. Se puede **simplificar a lo mínimo** (`Conceptos.Nat==6` basta) `[02:00]`.

---

## Tarea 5 — Separadores y subtotales

**Qué es:** partir el cuerpo del informe en **grupos** (por letra del código, por naturaleza…) y cerrar cada grupo con su **subtotal** — el patrón visual clásico de los informes de Presto. *"Los subtotales no salen mágicamente, uno los tiene que crear"* `[02:50]`.

**Paso a paso — los separadores** `[02:10]`–`[02:20]`:

1. En Propiedades de **`Elemento 1`**: **`Separador = Sí`** (aparece la sección `Separador 1` arriba) y **`Fin de separador = Sí`** (aparece `Fin de separador 1` abajo).
2. **`Ordenar por`** = `Conceptos.Código` (o naturaleza, unidad, divisa…). Es a la vez el criterio de **orden** y de **corte** de los grupos.
3. **`Carácter separador`** = `1` corta un grupo nuevo cada vez que cambia el **primer carácter** del código; `2`, cada vez que cambian los dos primeros.

**Paso a paso — el subtotal en `Fin de separador 1`** `[02:50]`:

1. Creá dos cuadros de texto: uno con texto plano `"Subtotal:"` y otro (alineado con la columna de totales) que va a mostrar el número. Opcional: una **línea** de adorno encima.
2. Al cuadro numérico: **`Formato = numérico`** (nunca `auto`).
3. Averiguá el **nombre** del cuadro que imprime los totales en `Elemento 1` (en el video era `cuadro 15` — en tu plantilla puede variar; se averigua con **Rastreo**, ver más abajo). En el **`Origen`** del cuadro nuevo escribí ese nombre, **sin comillas**: `cuadro15`.
4. Propiedad **`Cálculo`** → operación **`Suma`** (hay también media, máximo, mínimo) → **`Elemento número = 1`** (la sección donde vive el cuadro que sumás) → **`Reiniciar fin de separador = 1`** (resetea la suma al cerrar cada grupo). Lo demás, **dejalo por defecto** `[02:50]`.
5. Vista preliminar: cada grupo cierra con su subtotal. El relator lo verificó contra la suma real de la obra y coincidió `[02:50]`–`[03:00]`.

!!! tip "Rastreo: encontrar un cuadro en un informe denso"
    En **Vista preliminar** → botón **`Rastreo`** → el informe muestra el **nombre** de cada control (ej. "cuadro 15"). Después: salí de la vista preliminar, hacé **clic fuera del área de impresión** (que no quede nada seleccionado), **`Ver ▸ Lista de controles`**, escribí el nombre **sin espacios** (`cuadro15`) y doble clic: el control queda seleccionado en la plantilla `[01:40]`. Es la forma segura de editar informes de fábrica.

---

## Tarea 6 — Preguntas y respuestas (informes parametrizables)

**Qué es:** variables que el informe **pregunta al usuario al ejecutarse** ("¿qué tipo de recurso querés?", "¿qué % de IVA?"). Con ellas, **una sola plantilla** cubre varios informes — menos plantillas que mantener.

**Paso a paso — crear las variables** `[02:20]`–`[02:30]`: menú **`Ver ▸ Parámetros / Preguntas`** (verificar en Presto el nombre exacto) → una tabla con columnas Variable / Pregunta / Longitud / Mayúsculas / Respuesta:

| Tipo | Cómo se define | Ejemplo |
|---|---|---|
| **Lista** | Opciones separadas por `;`, todo entre comillas; con **`Longitud = 1`** la variable toma solo el **primer carácter** de la opción elegida | Variable `recurso`, Respuesta `"1.- Mano de obra;2.- Maquinaria;3.- Materiales;4.- Todos;"` |
| **Numérica** | Un número directo (sin comillas) → sirve para cálculos | Variable `iva`, Respuesta `20` |
| **Alfanumérica** | Texto entre comillas | Variable `comentario` |

Naming recomendado: minúsculas, sin acentos, sin espacios, guion bajo. Dentro de la tabla movete con ++tab++ — el ++enter++ **cierra la ventana** `[02:20]`.

**Paso a paso — usar la variable en `Selección` con `IIF`** `[02:30]`–`[02:40]`: `IIF` es la función condicional de Presto (Generador de expresiones → **Funciones ▸ Presto**): "si la condición es cierta, esto; si no, esto otro". Anidando una por opción:

```
IIF("recurso"==1, Conceptos.Nat==6,
  IIF("recurso"==2, Conceptos.Nat==7,
    IIF("recurso"==3, Conceptos.Nat==8,
      Conceptos.Nat==6 || Conceptos.Nat==7 || Conceptos.Nat==8)))
```

- La última opción ("Todos") sale **por descarte** — no necesita otro `IIF`.
- Cerrá con **tantos `)` como `IIF` abriste** (acá, 3) `[02:40]`.
- Al ejecutar: respuesta 1 → solo MO; 2 → maquinaria; 3 → materiales; 4 → los tres. El botón **`Volver`** de la vista preliminar te regresa al cuadro de preguntas para cambiar la respuesta sin salir `[02:40]`.

---

## Tarea 7 — Totales finales con impuestos (sección Final)

**Qué es:** el total general del informe, más el impuesto calculado y el gran total — impresos solo en la **última página**.

**Paso a paso** `[03:00]`–`[03:10]`:

1. **`Sección ▸ Final`** → aparece la sección Final.
2. Atajo del relator: **copiá los 3 controles** del `Fin de separador 1` (texto, número y línea) y **pegalos** en Final. Cambiá `"Subtotal:"` por `"TOTAL:"`.
3. En el cuadro numérico → `Cálculo`: mantené `Suma` y `Elemento número = 1`, pero **`Reiniciar fin de separador = 0`**. Con `0` la suma **no se resetea nunca** → acumula todo el informe = total general.
4. **El impuesto:** nuevo cuadro con texto plano `"Impuestos:"` + un cuadro numérico (formato `numérico`) cuyo `Origen` sea `cuadro25 * "iva" / 100` — donde `cuadro25` es el **nombre** del cuadro del total (en tu plantilla puede llamarse distinto: verificalo con Rastreo) e `"iva"` es la variable de pregunta de la Tarea 6. Para redondear a 2 decimales: `RA(cuadro25 * "iva" / 100)` (`RA` = función redondear del curso avanzado — verificar en Presto la sintaxis exacta) `[03:10]`.
5. **El gran total:** otro cuadro numérico con `Origen` = `cuadro25 + cuadro28` (suma de cuadros por nombre; `cuadro28` era el del impuesto en el video) `[03:10]`.
6. Vista preliminar: en el video, total ≈ 67 millones, IVA 20% ≈ 13 millones, gran total = la suma. Cambiando la respuesta a 10% con `Volver`, recalculó `[03:10]`.

!!! warning "El impuesto del informe NO es el impuesto del presupuesto"
    Este IVA se calcula **en la presentación**, no en el dato. Si el presupuesto no lo modela, el informe y el presupuesto pueden divergir. Para Raizant: modelá los impuestos como **[conceptos porcentaje](2-intermedio.md#tarea-2-modelar-un-concepto-porcentaje-leyes-sociales-iva)** dentro del presupuesto y que el informe solo los imprima. El video usa "IVA 20%" (Chile); las tasas bolivianas (IVA/IT) hay que definirlas con contabilidad.

---

## Tarea 8 — Guardar, compartir y versionar plantillas

**Qué es:** una plantilla es un **archivo** independiente de la obra. En el video se guarda como `Informe curso versión 25` de tipo Presto Report (extensión `.PrestoReport` — verificar en Presto) y el relator la reparte **por el chat** `[03:20]`.

**Lo que hay que saber:**

1. **Los informes de fábrica** viven en la **carpeta de instalación de Presto ▸ carpeta `Report`**, organizados por país (Chile, España, Perú, Bolivia) `[03:10]`.
2. **Antes de editar un informe de fábrica: `Guardar como` una copia.** *"Si no te quieres echar un informe… dale a guardar como, ponle otro nombre y ese edítalo"* `[03:20]`. (Si igual lo rompés, soporte te reenvía el original.)
3. En los informes de fábrica, **no toques las fórmulas**: están "archiprobadas" (sin ediciones desde 2023). Editá a lo sumo fuente, formato, decimales `[03:10]`–`[03:20]`.
4. La plantilla es **portable**: incrusta las imágenes (Tarea 3), así que viaja completa por archivo.

!!! danger "Gobernanza Raizant: las plantillas oficiales NO viven en el escritorio de nadie"
    En el video las plantillas se reparten "por chat" y quedan en el escritorio de cada uno. Ese es el camino directo a que **cada usuario imprima un informe distinto** con el mismo presupuesto. Regla para Raizant:

    - Las plantillas oficiales viven en **una única carpeta compartida y versionada del equipo** — no en perfiles locales. *(La ubicación definitiva es una decisión de gobernanza pendiente, ligada a dónde se publique este sitio — issue DRI-187.)*
    - Toda modificación se hace sobre una **copia con nombre y fecha** (`Guardar como`), nunca sobre el original de fábrica ni sobre la plantilla oficial vigente.
    - Un solo dueño del set de plantillas (rol Presupuestos) aprueba los cambios.

---

## 🎥 Mirá el video

| Tema | Minuto |
|---|---|
| Plantilla autogenerada + vista preliminar | `[00:00]`–`[00:10]` |
| Propiedades de plantilla, formato de cuadros | `[00:20]`–`[00:50]` |
| Cuadros de texto, coordenadas, Entidades, logo | `[00:50]`–`[01:30]` |
| Rastreo, formato numérico y redondeos | `[01:40]`–`[01:50]` |
| Tabla, clave, máscara y selección con `\|\|` | `[01:50]`–`[02:10]` |
| Separadores | `[02:10]`–`[02:20]` |
| Preguntas y respuestas + `IIF` | `[02:20]`–`[02:50]` |
| Subtotales | `[02:50]`–`[03:00]` |
| Sección Final, impuestos, informes de fábrica, compartir | `[03:00]`–`[03:25]` |

> Video fuente: `infos_av_03_12_2025.mp4` (3h 25min). El módulo siguiente del curso ("Gestión de proyecto": avances que se certifican para estados de pago `[03:20]`) se cubre en el rol [Control de obra](../control-obra/index.md).

---

## ⚠️ Lo que Presto NO te avisa (resumen)

- **Ventana `Entidades` vacía** → los informes formales salen sin emisor ni cliente. Cargala en el setup de cada obra.
- **Naturaleza usada como coordenada en un concepto repetido** → trae el dato equivocado o nada, sin error. Preferí código entre comillas.
- **`Auto extensible = No`** → los textos largos salen **cortados** en el papel.
- **`Reiniciar fin de separador` invertido** → "subtotales" que son totales corridos, o un total general que se resetea. Regla: `1` en Fin de separador, `0` en Final.
- **Formato `auto` en celdas numéricas** → decimales inconsistentes que no respetan la tabla de redondeos.
- **Impuesto calculado solo en el informe** → el dato del presupuesto y el papel divergen.
- **Plantillas guardadas en el perfil local de cada máquina / repartidas por chat** → cada usuario ve informes distintos del mismo presupuesto. Carpeta compartida única.
- **Editar un informe de fábrica sin `Guardar como`** → echás a perder el original.

👉 Las fallas generales del presupuesto están en [4 · Reglas de oro y fallas silenciosas](5-reglas-de-oro.md).

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá lo aprendido"
    Sobre la obra de prueba **BLEND**:

    1. Ponete en la vista Presupuesto y generá la plantilla autogenerada (`Inicio ▸ Diseñar`). Mirala en vista preliminar.
    2. Agregá un cuadro con texto plano `"Obra:"` y al lado uno con la expresión `Conceptos.Resumen[NAT==0]`.
    3. En `Elemento 1`, dejá la `Selección` en `Conceptos.Nat==8 || Conceptos.Nat==6` (materiales + mano de obra).
    4. Activá `Separador` y `Fin de separador`, ordená por `Conceptos.Código` con carácter separador `1`, y armá el subtotal (`Suma`, `Elemento número = 1`, `Reiniciar fin de separador = 1`).
    5. Creá la variable de lista `recurso` y usala en `Selección` con `IIF`. Probá las 4 respuestas con el botón `Volver`.
    6. Agregá la sección `Final` con el total general (`Reiniciar fin de separador = 0`).
    7. Guardá la plantilla con `Guardar como` en la carpeta compartida del equipo — no en tu escritorio.

    **Cómo sabés que salió bien:** el subtotal de mano de obra del informe coincide con la suma de MO que ves en la obra (el mismo chequeo que hizo el relator `[02:50]`–`[03:00]`).

---

📖 **Fuente oficial:** apuntes 04-informes-avanzados.md y C10-modulo-informes-avanzados-casos-uso.md (basados en el video; ⚠️ sin verificación por capturas todavía). Documentación RIB de informes: pendiente de identificar el PDF específico en `presto-documentacion/`.
