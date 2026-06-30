# 1 · Recibir material: la Entrega (albarán)

!!! abstract "Conclusión primero"
    Acá aprendés a **registrar que un material llegó a la obra**: creás un documento de **Entrega** (el albarán), elegís el proveedor que te lo trajo, lo fechás, y cargás abajo los materiales que recibiste con su **cantidad real** (la que llegó, no la que compraste) y su **precio real de compra**. Es el primer paso del costo real — pero todavía NO le dice a Presto a qué partida se gastó (eso es la [Tarea siguiente](2-imputar-consumo.md)).

!!! tip "Antes de arrancar, tené a mano el mapa"
    Las instrucciones usan palabras como _"la cabecera de arriba"_, _"la subventana Suministros"_, _"el botón de los tres puntos"_. Si algo no lo ubicás, abrí en otra pestaña **[🗺 La pantalla de Obra/Almacén](interfaz.md)** — es el mapa con cada zona de la ventana `Entregas`.

!!! warning "Requisito de licencia — sin esto no podés avanzar"
    La ventana `Entregas` **solo funciona si la licencia incluye el módulo de Facturación y Control**. Si tu licencia no lo tiene, el botón aparece en gris. Antes de operar este rol, **verificá que el módulo de Facturación y Control esté incluido en la licencia** (es un requisito a confirmar al contratar/renovar).

!!! info "De dónde sale este contenido"
    Fuente principal: **documentación oficial de Presto (RIB)** — _Manual de Presto completo_ (cap. Facturación / Documentos, pp. 135–139). Se complementa con el apunte interno **C07 — Facturación y Entregas** (casos 1–8) y la transcripción del video **`FactCon_08_08_2025`** (de ahí los minutos `[hh:mm]`).

---

## Antes de empezar: lo que necesitás

| Necesitás | Por qué |
|---|---|
| **El módulo Facturación y Control en la licencia** | Sin él, la ventana `Entregas` ni se abre |
| **La tabla de Proveedores cargada** (`Ver ▸ Entidades`) | Toda entrega exige un proveedor; si no está en la tabla, no lo podés elegir |
| **La divisa por defecto definida** (`Propiedades`) | Si el proveedor se creó a mano sin divisa, el documento sale "raro" — conviene fijar la divisa real (BOB) |
| **El presupuesto con sus recursos cargados** (ventana `Conceptos`) | Lo que recibís se elige de esos recursos del presupuesto |

!!! note "¿Qué es una \"Entidad\"?"
    En Presto, **Entidad = proveedor o subcontratista** (el agente que te entrega el material o ejecuta el trabajo). Se cargan en `Ver ▸ Entidades` y después las elegís en cada entrega. Pensalo como tu **agenda de proveedores**.

---

## Tarea 1 — Abrir la ventana de Entregas

**Qué es:** abrir la pantalla donde se registran las recepciones de material.

📖 **Fuente oficial:** Manual de Presto, cap. *Facturación / Documentos*, pp. 135–136 (las ventanas `Pedidos`, `Entregas` y `Facturas` comparten la misma mecánica).

**Paso a paso** `[00:30]`:

1. Andá a la **cinta de arriba** y hacé clic en la pestaña **`Ver`**.
2. En el grupo **`Documentos`**, hacé clic en el **botón `Entregas`** (queda **hundido/marcado** cuando está activo). Se abre la ventana: **cada fila de arriba es una Entrega** (un albarán).
3. Activá también el **botón `Suministros`** (mismo grupo; también queda hundido al activarlo). Aparece, **abajo**, una subventana: ahí va el **detalle de qué materiales** trae la entrega seleccionada arriba.

!!! tip "Las dos zonas de la pantalla"
    Quedate con esto: **arriba** está la _cabecera_ (un renglón por albarán: quién, cuándo, cuánto) y **abajo** está el _detalle_ (las líneas de materiales de ese albarán). Vas a saltar todo el tiempo entre esas dos zonas. La subventana de abajo muestra en su título de qué entrega ves el detalle, p. ej. `Suministros EN-001|1302|30/11/2025`.

---

## Tarea 2 — Crear el documento de entrega (la cabecera)

**Qué es:** abrir un albarán nuevo y darle su código.

📖 **Fuente oficial:** Manual de Presto, p. 136 — _"Para crear un documento hay que introducir al menos los campos `Documento`, `Entidad` y `Fecha`."_

**Dónde estás:** en la **franja de arriba** (la cabecera de `Entregas`).

**Paso a paso** `[00:50]`:

1. En la cabecera, hacé clic en la primera celda de la columna **`Documento`** (la de más a la izquierda).
2. Escribí el **código del albarán/recepción** (el número del remito del proveedor, o uno propio). Ejemplo verificado por captura: **`EN-001`**.
3. La columna **`NatC`** (naturaleza), que está al lado, **no la toques** — se va a poner sola con el ícono del proveedor cuando lo asignes en la Tarea 4.

!!! note "Tres campos obligatorios, nada más"
    Para que la fila exista, Presto solo exige `Documento`, `Entidad` y `Fecha`. Con esos tres ya tenés el "sobre" del albarán; el detalle de materiales viene después (Tarea 5).

---

## Tarea 3 — Elegir el proveedor (Entidad)

**Qué es:** decirle a la entrega **quién** te trajo el material.

📖 **Fuente oficial:** Manual de Presto, p. 136 — _"El campo `Entidad` contiene el código del agente que emite o recibe el documento… El campo `Resumen` corresponde a esta entidad."_

**Dónde mirar:** la columna **`Entidad`** de la cabecera (a la derecha del documento).

**Paso a paso** `[00:50]`:

1. Hacé clic en la celda de la columna **`Entidad`** y usá el **botón de sugerencia `…`**. Se abre tu **tabla de proveedores**.
2. Elegí el proveedor que te entregó. Ejemplo de captura: Entidad **`1302`**, cuyo nombre (`Resumen`) es **`MEGA ARIDOS`**.
3. **La señal de que salió bien:** la columna **`Resumen`** se llena sola con el nombre del proveedor, y el **ícono de `NatC` cambia al de proveedor**. ✅ Verificá ese ícono — es la marca de que la entidad quedó bien asignada.

!!! danger "Falla silenciosa #1 — Presto copia el proveedor de la entrega anterior"
    Cuando creás la **siguiente** entrega, Presto **arrastra el mismo proveedor y la misma fecha** de la fila de arriba, solito (no usa el reloj de Windows, usa el documento previo). Si no te fijás, terminás atribuyendo el material al proveedor equivocado **sin ningún aviso**. Regla de oro: **en cada entrega nueva, confirmá el proveedor a mano**, aunque parezca que ya está puesto. _(C07, falla silenciosa FS-1, video `[01:10]`.)_

---

## Tarea 4 — Poner la fecha de recepción

**Qué es:** fechar el albarán con el día real en que llegó el material.

📖 **Fuente oficial:** Manual de Presto, p. 136 (la `Fecha` es uno de los 3 campos obligatorios del documento).

**Dónde mirar:** la columna **`Fecha`** de la cabecera.

**Paso a paso** `[00:50]`:

1. Mirá la columna **`Fecha`**: en una entrega nueva Presto pone la fecha de hoy; en las siguientes **repite la fecha de la entrega anterior**.
2. **Corregila al día real de la recepción** — el día en que de verdad llegó el camión. Hacé clic en la celda y escribí día/mes/año, o usá el botón de sugerencia.
3. Coherencia con la planificación: si el material se necesita en un período (p. ej. relleno a partir del 31/12), fechá la entrega dentro de ese período.

!!! warning "Falla silenciosa #2 — la fecha mal puesta no calcula el costo, y solo se ve gris"
    La fecha de la entrega (y sobre todo la **fecha de imputación** que ponés en la Tarea siguiente) decide en qué período entra el costo. Si queda **fuera de la fase de certificación actual**, Presto **no calcula nada** y la única señal es que la fecha se ve **gris**. **Siempre confirmá la fecha** antes de seguir. _(C07, falla silenciosa FS-2, video `[02:30]`.)_

---

## Tarea 5 — Cargar los materiales recibidos (suministros)

**Qué es:** detallar **qué** te entregó ese proveedor — los materiales, con su cantidad y precio.

📖 **Fuente oficial:** Manual de Presto, pp. 137–138 — _"Se pueden añadir suministros a un documento: tecleando su código… usando el botón de sugerir… copiando y pegando el concepto o arrastrándolo desde las ventanas del presupuesto y de conceptos."_

**Dónde estás:** ahora trabajás en la **subventana `Suministros`** (la franja de abajo). Asegurate de que el botón `Suministros` esté activado (naranja).

Hay **dos formas** de cargar un material. Usá la que te resulte más cómoda:

### Forma A — por sugerencia (la más rápida) `[00:50]` `[01:00]`

1. En la subventana de abajo, hacé clic en la primera celda de la columna **`Código`** y usá el **botón de sugerencia `…`**. Se abre la lista de **todos los recursos del presupuesto** (materiales, mano de obra, maquinaria, subcontratos), en orden alfabético.
2. Elegí el recurso que recibiste. Ejemplo de captura: **`MAE00017`** = `Bolón selecc c/flete 15 kms`.
3. Presto rellena solo el `Resumen`, la `Ud` (p. ej. `m3`), la `Divisa` y un `Precio` por defecto.
4. **La señal de que salió bien:** el ícono del material **se pone naranja** 🟧 (lo ves en `Conceptos`). Eso significa "este recurso ya figura en una entrega". Si no tiene el naranja, **no lo registraste todavía**. `[00:50]`

### Forma B — por arrastre (visual) `[00:50]` `[01:10]`

1. **Desacoplá** la pestaña `Entregas`: clic izquierdo sostenido sobre la pestaña, arrastrá un poco hacia abajo y soltá (queda como ventana flotante).
2. Andá a la pestaña **`Conceptos`** y seleccioná el/los recurso(s) con la **fila completa**. Podés seleccionar varios a la vez.
3. **Arrastrá** la fila (clic izquierdo sostenido) y **soltala** sobre la subventana `Suministros`.

!!! note "Limitación verificada"
    El arrastre **solo funciona desde la pestaña `Conceptos`**, no desde `Recursos`. _"Arrastrar solamente se puede hacer a través de la pestaña de conceptos."_ `[01:20]`

!!! note "¿Mano de obra o un subcontrato en vez de un material?"
    La misma Entrega sirve para registrar **mano de obra** (el documento es el cierre de la cuadrilla) o un **subcontrato** (refleja la contratación del subcontratista). El procedimiento es el mismo: elegís el recurso, ponés cantidad y precio. `[01:10]` `[01:20]`

---

## Tarea 6 — Poner la cantidad que LLEGÓ (entrega parcial)

**Qué es:** registrar cuánto material **efectivamente recibiste** (no necesariamente todo lo que se compró).

📖 **Fuente oficial:** Manual de Presto, p. 138 (la cantidad recibida puede ser una parcialidad de la compra).

**Dónde mirar:** la columna **`Cantidad`** de la subventana `Suministros`.

**Paso a paso** `[00:50]` `[01:00]`:

1. En la columna **`Cantidad`**, escribí lo que **efectivamente llegó** en este camión. El proveedor entrega por parcialidades: si compraste 119 m³ y llegaron 119, ponés 119; si llegaron 50, ponés 50.
2. La columna **`Importe`** se calcula sola = `Cantidad` × `Precio`. No la toques.

!!! warning "Falla silenciosa #3 — Presto no te dice de forma confiable cuánto falta por recibir"
    En el video, al recibir una parte de una compra mayor, la sugerencia de "cuánto falta por recibir" **falló**: _"falta seguramente alguna información… no me lo está haciendo, pero en teoría debería habérmelo hecho."_ El control de "comprado vs. recibido" **no es automático ni confiable** en esta versión. El dato existe en otras ventanas (lo ves en [Tarea 4 · del pedido a la factura](4-del-pedido-a-la-factura.md)), pero el aviso proactivo es tejido propio de Raizant. **No confíes en que Presto te frene si recibís de más o de menos.** _(C07, falla silenciosa FS-3, video `[01:20]`.)_

---

## Tarea 7 — Poner el precio real de compra

**Qué es:** registrar a qué precio te lo vendió de verdad el proveedor (el del albarán/remito).

📖 **Fuente oficial:** Manual de Presto, p. 138 — _"El precio por defecto es… el de objetivo."_ Se sobrescribe con el real.

**Dónde mirar:** la columna **`Precio`** de la subventana `Suministros`.

**Paso a paso** `[01:00]`:

1. En la columna **`Precio`**, Presto ya puso un número: es el **precio del objetivo de coste** (el estimado del presupuesto). Ejemplo de captura: `6.908`.
2. **Sobrescribilo** con el **precio real** que figura en el documento del proveedor. Hacé clic en la celda y escribí el precio real de compra.
3. _(Opcional)_ Si hubo **descuento**, cargalo en la columna **`PorDto`** (% de descuento). Presto calcula solo el precio neto (`PrNeto`).
4. **La columna `Importe` se recalcula sola** = cantidad × precio. ✅

!!! note "Tranquilo: este precio NO te pisa el presupuesto"
    El precio que ponés acá vive **solo en la línea de la entrega** — _"no sobrescriben a los valores que se hayan armado a nivel del presupuesto."_ _(video `[01:10]`)_. Por eso podés registrar lo que de verdad costó (para medir el desvío) sin arruinar el presupuesto original. Son cadenas de precio independientes.

---

## ✅ Hasta acá: el material está "recibido", pero todavía no es costo de ninguna partida

Importante: con las Tareas 1 a 7 registraste **que el material llegó** y **cuánto costó**. Pero Presto **todavía no sabe a qué partida se gastó**. Ese material está "en la bodega" del documento.

👉 Para que se vuelva **costo real de una partida**, falta imputarlo con `Destino` + fecha. Eso es el **corazón del rol** y lo aprendés en la página siguiente: **[2 · Imputar el consumo a la partida](2-imputar-consumo.md)**.

---

## 🎥 Mirá el video

| Tema | Minuto |
|---|---|
| Abrir Entregas, marco general | `[00:30]` |
| Crear el documento + proveedor + fecha | `[00:50]` |
| Cargar suministros (sugerencia / arrastre) | `[00:50]`–`[01:10]` |
| Cantidad recibida (parcial) | `[00:50]`–`[01:00]` |
| Precio real de compra | `[01:00]`–`[01:10]` |
| Variante mano de obra / subcontratos | `[01:10]`–`[01:20]` |

> Video fuente: `FactCon_08_08_2025.mp4` (3h 48min). Relator de soporte de Presto. _El video es complemento: la referencia primaria es la documentación oficial citada en cada tarea._

---

## ⚠️ Lo que Presto NO te avisa (resumen)

- **Te copia el proveedor y la fecha de la entrega anterior** → podés atribuir el material al equivocado, en silencio. _(Tarea 3 y 4)_
- **La fecha fuera de fase no calcula el costo** → solo se ve gris. _(Tarea 4)_
- **No te dice de forma confiable cuánto falta por recibir** → podés recibir de más sin freno. _(Tarea 6)_
- **El precio real no pisa el presupuesto** → registrás lo real sin miedo. _(Tarea 7)_

👉 Todas, con cómo blindarte, en [5 · Reglas de oro y fallas silenciosas](5-reglas-de-oro.md).

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá lo aprendido"
    Sobre la obra de prueba **BLEND** _(con una licencia que tenga el módulo de Facturación y Control)_:

    1. Creá una entrega nueva (`Documento` = `EN-PRUEBA-01`) y ponele un proveedor de la tabla de Entidades.
    2. Corregí la fecha al día de hoy bien.
    3. Cargale **2 materiales** por el método de sugerencia; a uno ponele una **cantidad parcial** (la mitad de lo presupuestado).
    4. Sobrescribí el `Precio` de uno con un precio "real" inventado y verificá que el `Importe` se calcule solo.
    5. Andá a `Conceptos` y comprobá que esos 2 materiales aparecen con **ícono naranja** 🟧.

    **Cómo sabés que salió bien:** el proveedor aparece con su ícono en `NatC`, los materiales tienen el naranja 🟧, y el `Importe` de cada línea refleja tu cantidad × precio.

---

📖 **Fuentes oficiales (RIB):** _Manual de Presto completo_ — cap. Facturación / Documentos, pp. 135–139.
**Complementos internos:** apunte C07 — Facturación y Entregas (casos 1–8) · transcripción `FactCon_08_08_2025`.
