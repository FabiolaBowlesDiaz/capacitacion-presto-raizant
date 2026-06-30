# 1 · Pedido manual (Orden de Compra a mano)

!!! abstract "Conclusión primero"
    Acá aprendés el **camino más directo para comprar** en Presto: crear una **Orden de Compra (OC)** tecleándola vos mismo. Elegís el proveedor, ponés la fecha, cargás los materiales que vas a pedir con su cantidad y precio, y dejás el documento "a firme". Es el camino **A** — rápido y a mano, sin pasar por una cotización entre varios proveedores _(eso es el camino B, en [Contratos: cotizar y adjudicar](2-contratos-cotizar.md))_.

!!! tip "Antes de arrancar, tené a mano el mapa"
    Las instrucciones usan palabras como _"la cinta de arriba"_, _"la franja de abajo"_, _"la subventana Suministros"_. Si algo no lo ubicás, abrí en otra pestaña **[🗺 La pantalla de Compras](interfaz.md)** — es el mapa con cada zona de las ventanas `Pedidos` y `Contratos`. Volvé a él cuando te pierdas.

!!! warning "Requisito de licencia — sin esto no podés avanzar"
    Las ventanas `Pedidos` y `Contratos` **solo funcionan si la licencia incluye el módulo de Contratación**. Si tu licencia no lo tiene, estos botones aparecen en gris y no vas a poder crear ninguna OC. Antes de operar este rol, **verificá que el módulo de Contratación esté incluido en la licencia** (es un requisito a confirmar al contratar/renovar).

!!! info "De dónde sale este contenido"
    Fuente principal: **documentación oficial de Presto (RIB)** — _Manual de Presto completo_ (cap. Contratación y compras, Facturación) y _Tutorial de Presto_. Se complementa con el apunte interno **C06 — Contratación y Pedidos** y la transcripción del video **`Contratacion_30_12_2025`** (de ahí salen los minutos `[hh:mm]`, para los puntos que el video muestra y la doc no detalla). Cada tarea cita su **página oficial** y, cuando aplica, el minuto del video.

---

## Antes de empezar: lo que necesitás

| Necesitás | Por qué |
|---|---|
| **El módulo Contratación en la licencia** | Sin él, las ventanas `Pedidos` y `Contratos` ni se abren |
| **La tabla de Proveedores cargada** (`Ver ▸ Entidades`) | Toda OC exige un proveedor; si no está en la tabla, no lo podés elegir _(igual se pueden crear "sobre la marcha", ver Tarea 4)_ |
| **Los datos de facturación del proveedor** (divisa, forma de pago, días, IVA) | Predeterminan los vencimientos e impuestos cuando después se facture _(Manual, esquema "Datos de facturación")_ |
| **El presupuesto con sus materiales y recursos** (ventana `Conceptos`) | Lo que pedís en la OC se elige de esos conceptos |

!!! note "Dato oficial: el pedido es OPCIONAL"
    El Manual lo dice expresamente: _"El control económico se puede realizar por completo usando sólo facturas. La introducción de pedidos y entregas es **opcional**."_ 📖 _(Manual, p. 135)_. Es decir: el pedido **no es obligatorio** para Presto. Lo usamos igual porque deja registro de la compra y se encadena después con la entrega y la factura — pero entendé que es una **decisión de proceso de Raizant**, no algo que Presto te fuerce.

!!! note "¿Qué es una \"Entidad\"?"
    En Presto, **Entidad = proveedor o subcontratista** (el agente que emite o recibe el documento). Se cargan en `Ver ▸ Entidades` (a mano o pegando desde Excel) y después las elegís en cada OC. Pensalo como tu **agenda de proveedores**.

---

## Tarea 1 — Abrir la ventana de Pedidos

**Qué es:** abrir la ventana donde están las Órdenes de Compra.

📖 **Fuente oficial:** Manual de Presto, cap. *Facturación / Documentos*, p. 135–136 (las ventanas `Pedidos`, `Entregas` y `Facturas` comparten la misma mecánica).

**Paso a paso** `[00:10]`:

1. Andá a la **cinta de arriba** y hacé clic en la pestaña **`Ver`**.
2. En el grupo **`Documentos`**, hacé clic en el **botón `Pedidos`** (queda **hundido/marcado** cuando está activo). Se abre la ventana: **cada fila de arriba es un Pedido (una OC)**.
3. Activá también el **botón `Suministros`** (mismo grupo; también queda hundido al activarlo). Aparece, **abajo**, una subventana: ahí va el **detalle de qué materiales lleva** el pedido que tengas seleccionado arriba.

!!! warning "¿No ves el botón `Pedidos` en el grupo `Documentos`?"
    Si en tu pestaña `Ver`, grupo `Documentos`, solo aparecen **`Insumos`** y **`Vencimientos`** (y NO `Pedidos`/`Contratos`/`Entregas`/`Facturas`), es porque **tu licencia todavía no incluye el módulo de Contratación**. Sin ese módulo no podés operar este rol — podés estudiar el manual, pero los botones recién aparecen cuando la licencia tenga Contratación activo.

!!! tip "Las dos zonas de la pantalla de Pedidos"
    Quedate con esto: **arriba** está la _cabecera_ (un renglón por OC: quién, cuándo, total) y **abajo** está el _detalle_ (las líneas de materiales de la OC seleccionada). Vas a saltar todo el tiempo entre esas dos zonas. La subventana de abajo muestra en su título algo como `Suministros P00001|2202|30/12/2025` — eso confirma de qué OC estás viendo el detalle.

---

## Tarea 2 — Crear el documento de la OC (la cabecera)

**Qué es:** abrir una orden de compra nueva y darle su número.

📖 **Fuente oficial:** Manual de Presto, p. 136 — _"Para crear un documento hay que introducir al menos los campos `Documento`, `Entidad` y `Fecha`."_

**Dónde estás:** en la **franja de arriba** (la cabecera de `Pedidos`).

**Paso a paso** `[00:10]`:

1. En la cabecera, hacé clic en la primera celda de la columna **`Documento`** (la de más a la izquierda).
2. Apretá el **botón de los tres puntos `…`** que aparece en la celda. Presto te **sugiere el número correlativo** que sigue (ej. `P00001`). Aceptalo.
3. La columna **`NatC`** (naturaleza), que está al lado, **no la toques** — se va a poner sola con el ícono del proveedor cuando lo asignes en la Tarea 4.

!!! warning "Regla oficial: documento + proveedor no se pueden repetir"
    El Manual avisa: _"La combinación de código de documento y entidad debe ser **única para cada anualidad**."_ 📖 _(Manual, p. 136)_. O sea: no puede haber dos OCs con el mismo número **y** el mismo proveedor en el mismo año. Por eso conviene dejar que Presto numere solo (con los tres puntos): los saca correlativos y sin chocar.

---

## Tarea 3 — Poner la fecha de la OC

**Qué es:** fechar la orden de compra (la fecha en que la emitís).

📖 **Fuente oficial:** Manual de Presto, p. 136 (la `Fecha` es uno de los 3 campos obligatorios del documento; además, _"el estado… se ve en el campo Fecha"_).

**Dónde mirar:** la columna **`Fecha`** de la cabecera (a la derecha del proveedor).

**Paso a paso** `[00:10]`:

1. Mirá la columna **`Fecha`**: Presto ya puso **la fecha de hoy** (la del calendario de Windows).
2. **Verificala y corregila** si no es la fecha real del documento: hacé clic en la celda y escribí día/mes/año, o usá el botón de sugerencia.

!!! warning "Falla silenciosa: la fecha de hoy queda mal y nadie te avisa"
    Como Presto pone "hoy" por defecto, es muy fácil dejar una OC con fecha equivocada sin darte cuenta. **Siempre confirmá la fecha** antes de seguir — tiene que coincidir con la fecha real en que aprobaste/emitiste la compra. _(Confirmado en C06, falla silenciosa FS-2.)_

---

## Tarea 4 — Elegir el proveedor

**Qué es:** decirle a la OC a quién le comprás.

📖 **Fuente oficial:** Manual de Presto, p. 136 — _"El campo `Entidad` contiene el código del agente que emite o recibe el documento… Se pueden crear entidades sobre la marcha. El campo `Resumen` corresponde a esta entidad."_

**Dónde mirar:** la columna **`Entidad`** de la cabecera (a la derecha de la fecha del documento).

**Paso a paso** `[00:20]`:

1. Hacé clic en la celda de la columna **`Entidad`** y apretá el **botón de los tres puntos `…`**. Se abre tu **tabla de proveedores**.
2. Buscá el proveedor. Si la lista es larga, **clic derecho sobre el título de una columna ▸ Ordenar** para ordenarla por nombre o código y ubicarlo más rápido.
3. Hacé doble clic sobre el proveedor (o seleccionalo y `Aceptar`).
4. **La señal de que salió bien:** en la columna `Entidad` aparece su **código** (ej. `2202`), la columna **`Resumen`** de al lado se llena sola con su **nombre** (ej. `BIO BIO`), y el **ícono de `NatC` cambia al de proveedor**. ✅

!!! note "¿No está el proveedor en la lista? Lo creás al vuelo"
    La doc oficial permite **crear la entidad sobre la marcha** sin salir del documento. Igual, lo prolijo para Raizant es cargar los proveedores antes en `Ver ▸ Entidades` con sus datos de facturación completos, así los vencimientos e IVA salen bien después.

!!! danger "Falla silenciosa #1 — Presto copia el proveedor de la OC anterior"
    Cuando creás la **siguiente** OC, Presto **arrastra el mismo proveedor** de la fila de arriba, solito. Si no te fijás, terminás comprándole al proveedor equivocado **sin ningún aviso**. Regla de oro: **en cada OC nueva, confirmá el proveedor a mano**, aunque parezca que ya está puesto. _(C06, falla silenciosa FS-1, video `[00:50]`.)_

---

## Tarea 5 — Cargar los materiales (suministros)

**Qué es:** detallar QUÉ le comprás a ese proveedor — los materiales, mano de obra o subcontratos, con su cantidad y precio.

📖 **Fuente oficial:** Manual de Presto, p. 137–138 — _"Se pueden añadir suministros a un documento: tecleando su código… usando el botón de sugerir… copiando y pegando el concepto o arrastrándolo desde las ventanas del presupuesto y de conceptos."_

**Dónde estás:** ahora trabajás en la **subventana `Suministros`** (la franja de abajo). Antes de empezar, asegurate de que **el único interruptor prendido abajo sea `Suministros`**.

**Paso a paso** `[00:20]`–`[00:40]`:

1. En la subventana de abajo, hacé clic en la primera celda de la columna **`Código`** y apretá el **botón de los tres puntos `…`**. Se abre la lista de **todos los conceptos del presupuesto** (materiales, mano de obra, subcontratos).
2. **Filtrá para encontrar lo que buscás:** escribí las primeras letras en el **encabezado de la columna** (filtra por código y por descripción). Ejemplo: tecleá `MA` y quedan solo los materiales con código `MA…`. Elegí el que quieras (ej. cemento).
3. Apretá **Enter**: se crea una fila nueva, lista para el siguiente material. Repetí el filtro/elección para cada uno.
4. **La señal de que salió bien:** el ícono del material **se pone naranja** 🟧. Eso significa "este concepto ya figura en un pedido". Si no tiene el naranja, **no lo pediste todavía**. _(video `[00:30]`)_

!!! tip "Las 4 formas oficiales de agregar un material (elegí la que te sirva)"
    El Manual (p. 137–138) lista cuatro: **(a)** teclear su código —que puede incluso no existir aún en el presupuesto—; **(b)** el botón **`Sugerir`** (muestra los suministros del mismo proveedor y misma naturaleza); **(c)** **copiar/pegar o arrastrar** el concepto desde `Presupuesto` o `Conceptos`; **(d)** teclear un código nuevo. Para empezar, quedate con la (a): teclear el código + filtrar.

!!! note "Dato oficial útil: cargar un costo sin sumar cantidad"
    _"Si la cantidad es nula, el precio unitario se toma como importe; esto permite introducir costes que no impliquen un aumento de la cantidad del suministro."_ 📖 _(Manual, p. 138)_. Sirve, por ejemplo, para cargar un flete o un cargo fijo en la misma OC sin que altere la cantidad del material.

!!! note "¿Mano de obra o un subcontrato en vez de un material?"
    El mismo Pedido sirve para contratar **mano de obra** (filtrá con `O` al buscar el recurso) o un **subcontrato** (filtrá con `S`; suelen ir con cantidad = 1, porque es un precio cerrado). La OC simplemente **une un proveedor con lo que le pedís**, sea material, gente o un subcontrato. _(video `[01:00]`)_

---

## Tarea 6 — Poner la cantidad

**Qué es:** decir cuánto pedís de cada material.

📖 **Fuente oficial:** Manual de Presto, p. 138 — _"El botón de sugerir muestra valores útiles para rellenar los campos `Cantidad` y `Precio`."_

**Dónde mirar:** la columna **`Cantidad`** de la subventana `Suministros`.

**Paso a paso** `[00:30]`–`[00:50]`:

1. En la columna **`Cantidad`**, apretá el **botón de sugerencia `…`**. Presto te **sugiere la cantidad presupuestada** de ese material. Ejemplo del video: 3.780 sacos de cemento.
2. **No estás obligado a pedir todo de una.** Escribí la fracción que vas a comprarle a este proveedor (ej. 1.000 de los 3.780). El resto lo podés pedir después, a otro proveedor.
3. Cuando hagas un **segundo pedido** del mismo material, la ventana de sugerencia te muestra tres números: lo presupuestado, **lo que ya pediste**, y **lo que falta** (presupuestado − pedido). Ejemplo: si ya pediste 1.000, te dice que faltan 2.780. 🎯

!!! danger "Falla silenciosa #2 — Presto te deja pedir de más sin frenarte"
    Ese "lo que falta" es solo una **sugerencia, no un tope**. Presto **te deja pedir más de lo presupuestado** sin avisar nada. Si por error pedís 5.000 de un material que presupuestaste en 3.780, Presto lo acepta callado. Regla: **mirá siempre el número de "lo que falta"** antes de confirmar la cantidad. _(C06, falla silenciosa FS-5, video `[00:50]`.)_

---

## Tarea 7 — Poner el precio real de compra

**Qué es:** registrar a qué precio te lo vende el proveedor.

📖 **Fuente oficial:** Manual de Presto, p. 138 — _"El precio por defecto es el precio contratado o el de objetivo, en este orden."_

**Dónde mirar:** la columna **`Precio`** de la subventana `Suministros`.

**Paso a paso** `[00:40]`:

1. En la columna **`Precio`**, Presto ya puso un número: es el **precio contratado o el objetivo de coste** (el precio estimado), según cuál exista.
2. **Sobrescribilo** con el **precio real** que te pasó el proveedor (ej. 3.500 el saco). Hacé clic en la celda y escribilo.
3. _(Opcional)_ Si el proveedor te dio un **descuento**, cargalo en la columna **`PorDto`** (% de descuento). Presto calcula solo el precio neto.
4. **La columna `Importe` se calcula sola** = cantidad × precio neto. No la toques.

!!! note "Tranquilo: este precio NO te pisa el presupuesto"
    El precio que ponés acá vive en la línea de suministro del documento — **no modifica** el precio del presupuesto ni el objetivo de coste. Por eso podés registrar lo que de verdad te costó (para medir el desvío) sin arruinar tu presupuesto original. Son cadenas de precio independientes. _(C06 §0.4; video `[00:40]`.)_

---

## Tarea 8 — Ver el total y dejar la OC "a firme"

**Qué es:** revisar el total del pedido y **protegerlo** para que no se edite por error.

📖 **Fuente oficial:** Manual de Presto, p. 136 y 138 — _"El estado se elige modificando el color con el menú contextual… Los documentos en estado gris y rojo se consideran provisionales o pendientes de aprobación"_ y _"Los campos `Cantidad`, `Factor`, `PorDto`, `Precio` e `IVA` de los documentos con estado verde se muestran como no editables."_

**Paso a paso** `[00:40]`–`[01:10]`:

1. Hacé **clic afuera** de la subventana `Suministros` (en cualquier fila de la cabecera de arriba). La columna **`BasePed`** de la cabecera te muestra ahora el **total del pedido** (la suma de todos sus materiales). ✅
2. Cuando ya revisaste todo y la OC está lista para mandar al proveedor, **marcala "a firme"**: hacé **clic derecho sobre la celda `Documento`** de esa OC → elegí **`Estado verde`**.
3. **La señal de que salió bien:** las celdas `Documento` y `Nota` quedan con **fondo verde**. A partir de ahí, las columnas `Cantidad`, `Precio`, `Factor`, `PorDto` e `IVA` quedan **bloqueadas** (no se pueden editar por accidente).

!!! note "Los colores de estado, según la doc oficial"
    Presto usa el **color del documento** (sobre el campo `Fecha`) para indicar su estado: **rojo y gris = provisional / pendiente** (no se tiene en cuenta para el coste, solo para el saldo y flujo de caja); **negro = definitivo**; **verde = "a firme"** (protege los campos). 📖 _(Manual, p. 136.)_

!!! warning "Importante: el \"estado verde\" NO es una aprobación"
    El verde solo **protege los campos** contra ediciones accidentales — **es reversible** (clic derecho → otro estado y se desbloquea). **No es** un permiso ni una aprobación de tu jefe. Presto **no tiene** flujo de aprobaciones ni roles de usuario _(no es un ERP)_. Si en Raizant la compra necesita que alguien la apruebe antes, eso se controla **por fuera de Presto** (en el proceso de la empresa), no con este botón. _(C06, falla silenciosa FS-6.)_

---

## 🎥 Mirá el video

| Tema | Minuto |
|---|---|
| Abrir Pedidos, marco general | `[00:10]` |
| Crear el documento + fecha | `[00:10]` |
| Asignar el proveedor (Entidad) | `[00:20]` |
| Cargar suministros (materiales) | `[00:20]`–`[00:30]` |
| Cantidad + resta "lo que falta" | `[00:30]`–`[00:50]` |
| Precio real de compra + descuento | `[00:40]` |
| Total (BasePed) + estado verde "a firme" | `[00:40]`–`[01:10]` |
| Variante mano de obra / subcontratos | `[01:00]` |

> Video fuente: `Contratacion_30_12_2025.mp4` (2h 18min). Relator de soporte de Presto Chile. _El video es complemento: la referencia primaria es la documentación oficial citada en cada tarea._

---

## ⚠️ Lo que Presto NO te avisa (resumen)

- **Te copia el proveedor de la OC anterior** → podés comprarle al equivocado, en silencio. _(Tarea 4)_
- **Te deja pedir más de lo presupuestado** → sobre-pedido sin freno. _(Tarea 6)_
- **La fecha "de hoy" queda mal** si no la corregís. _(Tarea 3)_
- **El estado verde no es aprobación** → no confundir proteger con autorizar. _(Tarea 8)_
- **El pedido no es obligatorio ni encadena solo** con la entrega/factura → esa disciplina la pone el proceso de Raizant, no Presto. _(Manual p. 135)_

👉 Todas, con cómo blindarte, en [4 · Reglas de oro y fallas silenciosas](4-reglas-de-oro.md).

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá lo aprendido"
    Sobre la obra de prueba **BLEND** _(con una licencia que tenga el módulo Contratación)_:

    1. Creá una OC nueva (`Documento` con los tres puntos) y ponele la fecha de hoy bien.
    2. Asignale un proveedor de la tabla de Entidades.
    3. Cargale **2 materiales**: a uno ponele una **fracción** de la cantidad presupuestada (ej. la mitad) y mirá que el `Importe` se calcule solo.
    4. Sobrescribí el `Precio` de uno con un precio "real" inventado y verificá que **el total `BasePed`** de arriba cambie.
    5. Dejá la OC en **estado verde** y comprobá que ya no te deja editar la cantidad.

    **Cómo sabés que salió bien:** los materiales aparecen con ícono **naranja** 🟧, el total `BasePed` refleja tus cantidades y precios, y con el estado verde las columnas `Cantidad`/`Precio` quedan bloqueadas.

---

📖 **Fuentes oficiales (RIB):** _Manual de Presto completo_ — cap. Facturación / Documentos, pp. 135–139, y cap. Contratación y compras. · _Tutorial de Presto_, pp. 19–24.
**Complementos internos:** apunte C06 — Contratación y Pedidos (casos 1–7) · transcripción `Contratacion_30_12_2025`.
