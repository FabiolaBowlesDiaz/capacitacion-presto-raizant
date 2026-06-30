# 1 · Pedido manual (Orden de Compra a mano)

!!! abstract "Conclusión primero"
    Acá aprendés el **camino más directo para comprar** en Presto: crear una **Orden de Compra (OC)** tecleándola vos mismo. Elegís el proveedor, ponés la fecha, cargás los materiales que vas a pedir con su cantidad y precio, y dejás el documento "a firme". Es el camino **A** — rápido y a mano, sin pasar por una cotización entre varios proveedores _(eso es el camino B, en [Contratos: cotizar y adjudicar](2-contratos-cotizar.md))_.

!!! tip "Antes de arrancar, tené a mano el mapa"
    Las instrucciones usan palabras como _"la cinta de arriba"_, _"la franja de abajo"_, _"la subventana Suministros"_. Si algo no lo ubicás, abrí en otra pestaña **[🗺 La pantalla de Compras](interfaz.md)** — es el mapa con cada zona de las ventanas `Pedidos` y `Contratos`. Volvé a él cuando te pierdas.

!!! warning "Ojo con la licencia (estado actual de Raizant)"
    Para **operar** Compras hace falta tener activo el módulo **Contratación** en la licencia. La máquina local todavía **no lo tiene activo** (upgrade en curso). Eso significa que hoy esto se puede **estudiar y seguir paso a paso**, pero recién vas a poder **crear OCs de verdad** cuando se active el módulo. Lo avisamos para que no te frustres si un botón aparece en gris.

!!! info "De dónde sale este contenido"
    Apunte de capacitación **C06 — Contratación y Pedidos** (casos de uso 1–7) + transcripción del video **`Contratacion_30_12_2025`** + **Tutorial de Presto (RIB oficial)**. Cada paso cita el minuto `[hh:mm]` del video por si querés verlo.

---

## Antes de empezar: lo que necesitás

| Necesitás | Por qué |
|---|---|
| **El módulo Contratación activo** en la licencia | Sin él, las ventanas `Pedidos` y `Contratos` no funcionan |
| **La tabla de Proveedores cargada** (`Ver ▸ Entidades`) | Toda OC exige un proveedor; si no está en la tabla, no lo podés elegir |
| **Los datos de facturación del proveedor** (divisa, forma de pago, días, IVA) | Predeterminan los vencimientos e impuestos cuando después se facture |
| **El presupuesto con sus materiales y recursos** (ventana `Conceptos`) | Lo que pedís en la OC se elige de esos conceptos; sin ellos no hay qué pedir |

!!! note "¿Qué es una \"Entidad\"?"
    En Presto, **Entidad = proveedor o subcontratista**. Es la empresa o persona a la que le comprás. Se cargan una sola vez en `Ver ▸ Entidades` (a mano, o copiando/pegando desde un Excel) y después las elegís en cada OC. Pensalo como tu **agenda de proveedores**.

---

## Tarea 1 — Abrir la ventana de Pedidos

**Qué es:** prender la pantalla donde viven las Órdenes de Compra.

**Paso a paso** `[00:10]`:

1. Andá a la **cinta de arriba** y hacé clic en la pestaña **`Ver`**.
2. Buscá el **interruptor `Pedidos`** y hacé clic para encenderlo. Se abre la ventana: **cada fila de arriba es un Pedido (una OC)**.
3. Encendé también el **interruptor `Suministros`** (en el mismo grupo). Aparece, **abajo**, una subventana: ahí va el **detalle de qué materiales lleva** el pedido que tengas seleccionado arriba.

!!! tip "Las dos zonas de la pantalla de Pedidos"
    Quedate con esto: **arriba** está la _cabecera_ (un renglón por OC: quién, cuándo, total) y **abajo** está el _detalle_ (las líneas de materiales de la OC seleccionada). Vas a saltar todo el tiempo entre esas dos zonas. La subventana de abajo muestra en su título algo como `Suministros P00001|2202|30/12/2025` — eso confirma de qué OC estás viendo el detalle.

---

## Tarea 2 — Crear el documento de la OC (la cabecera)

**Qué es:** abrir una orden de compra nueva y darle su número.

**Dónde estás:** en la **franja de arriba** (la cabecera de `Pedidos`).

**Paso a paso** `[00:10]`:

1. En la cabecera, hacé clic en la primera celda de la columna **`Documento`** (la de más a la izquierda).
2. Apretá el **botón de los tres puntos `…`** que aparece en la celda. Presto te **sugiere el número correlativo** que sigue (ej. `P00001`). Aceptalo.
3. La columna **`NatC`** (naturaleza), que está al lado, **no la toques** — se va a poner sola con el ícono del proveedor cuando lo asignes en la Tarea 4.

!!! note "El número de OC es su identidad"
    Ese `P00001` es el identificador del documento. Dejá que Presto los numere solo (con los tres puntos) para que salgan correlativos y sin repetir.

---

## Tarea 3 — Poner la fecha de la OC

**Qué es:** fechar la orden de compra (la fecha en que la emitís).

**Dónde mirar:** la columna **`Fecha`** de la cabecera (a la derecha del proveedor).

**Paso a paso** `[00:10]`:

1. Mirá la columna **`Fecha`**: Presto ya puso **la fecha de hoy** (la del calendario de Windows).
2. **Verificala y corregila** si no es la fecha real del documento: hacé clic en la celda y escribí día/mes/año, o usá el botón de sugerencia.

!!! warning "Falla silenciosa: la fecha de hoy queda mal y nadie te avisa"
    Como Presto pone "hoy" por defecto, es muy fácil dejar una OC con fecha equivocada sin darte cuenta. **Siempre confirmá la fecha** antes de seguir — tiene que coincidir con la fecha real en que aprobaste/emitiste la compra.

---

## Tarea 4 — Elegir el proveedor

**Qué es:** decirle a la OC a quién le comprás.

**Dónde mirar:** la columna **`Entidad`** de la cabecera (a la derecha de la fecha del documento).

**Paso a paso** `[00:20]`:

1. Hacé clic en la celda de la columna **`Entidad`** y apretá el **botón de los tres puntos `…`**. Se abre tu **tabla de proveedores**.
2. Buscá el proveedor. Si la lista es larga, **clic derecho sobre el título de una columna ▸ Ordenar** para ordenarla por nombre o código y ubicarlo más rápido.
3. Hacé doble clic sobre el proveedor (o seleccionalo y `Aceptar`).
4. **La señal de que salió bien:** en la columna `Entidad` aparece su **código** (ej. `2202`), la columna **`Resumen`** de al lado se llena sola con su **nombre** (ej. `BIO BIO`), y el **ícono de `NatC` cambia al de proveedor**. ✅

!!! danger "Falla silenciosa #1 — Presto copia el proveedor de la OC anterior"
    Cuando creás la **siguiente** OC, Presto **arrastra el mismo proveedor** de la fila de arriba, solito. Si no te fijás, terminás comprándole al proveedor equivocado **sin ningún aviso**. Regla de oro: **en cada OC nueva, confirmá el proveedor a mano**, aunque parezca que ya está puesto. `[00:50]`

---

## Tarea 5 — Cargar los materiales (suministros)

**Qué es:** detallar QUÉ le comprás a ese proveedor — los materiales, mano de obra o subcontratos, con su cantidad y precio.

**Dónde estás:** ahora trabajás en la **subventana `Suministros`** (la franja de abajo). Antes de empezar, asegurate de que **el único interruptor prendido abajo sea `Suministros`** (que no haya otra subventana abierta encima).

**Paso a paso** `[00:20]`–`[00:40]`:

1. En la subventana de abajo, hacé clic en la primera celda de la columna **`Código`** y apretá el **botón de los tres puntos `…`**. Se abre la lista de **todos los conceptos del presupuesto** (materiales, mano de obra, subcontratos).
2. **Filtrá para encontrar lo que buscás:** escribí las primeras letras en el **encabezado de la columna** (filtra por código y por descripción). Ejemplo: tecleá `MA` y quedan solo los materiales con código `MA…`. Elegí el que quieras (ej. cemento).
3. Apretá **Enter**: se crea una fila nueva, lista para el siguiente material. Repetí el filtro/elección para cada uno.
4. **La señal de que salió bien:** el ícono del material **se pone naranja** 🟧. Eso significa "este concepto ya figura en un pedido". Si no tiene el naranja, **no lo pediste todavía**. `[00:30]`

!!! tip "Las 4 formas de agregar un material (elegí la que te sirva)"
    Además de teclear el código (lo de arriba), podés: **(b)** usar el botón **`Sugerir`** (te muestra los materiales del mismo proveedor); **(c)** **copiar/pegar o arrastrar** el concepto desde las ventanas `Presupuesto` o `Conceptos`; **(d)** teclear directamente un código nuevo. Para empezar, quedate con teclear el código + filtrar — es la más simple.

!!! note "¿Mano de obra o un subcontrato en vez de un material?"
    El mismo Pedido sirve para contratar **mano de obra** (filtrá con `O` al buscar el recurso) o un **subcontrato** (filtrá con `S`; suelen ir con cantidad = 1, porque es un precio cerrado). La OC simplemente **une un proveedor con lo que le pedís**, sea material, gente o un subcontrato.

---

## Tarea 6 — Poner la cantidad

**Qué es:** decir cuánto pedís de cada material.

**Dónde mirar:** la columna **`Cantidad`** de la subventana `Suministros`.

**Paso a paso** `[00:30]`–`[00:50]`:

1. En la columna **`Cantidad`**, apretá el **botón de sugerencia `…`**. Presto te **sugiere la cantidad presupuestada** de ese material (la que sale del presupuesto). Ejemplo del video: 3.780 sacos de cemento.
2. **No estás obligado a pedir todo de una.** Escribí la fracción que vas a comprarle a este proveedor (ej. 1.000 de los 3.780). El resto lo podés pedir después, a otro proveedor.
3. Cuando hagas un **segundo pedido** del mismo material, la ventana de sugerencia te muestra tres números: lo presupuestado, **lo que ya pediste**, y **lo que falta** (presupuestado − pedido). Ejemplo: si ya pediste 1.000, te dice que faltan 2.780. 🎯

!!! danger "Falla silenciosa #2 — Presto te deja pedir de más sin frenarte"
    Ese "lo que falta" es solo una **sugerencia, no un tope**. Presto **te deja pedir más de lo presupuestado** sin avisar nada. Si por error pedís 5.000 de un material que presupuestaste en 3.780, Presto lo acepta callado. Regla: **mirá siempre el número de "lo que falta"** antes de confirmar la cantidad. `[00:50]`

---

## Tarea 7 — Poner el precio real de compra

**Qué es:** registrar a qué precio te lo vende el proveedor.

**Dónde mirar:** la columna **`Precio`** de la subventana `Suministros`.

**Paso a paso** `[00:40]`:

1. En la columna **`Precio`**, Presto ya puso un número: es el **objetivo de coste** (el precio estimado del presupuesto).
2. **Sobrescribilo** con el **precio real** que te pasó el proveedor (ej. 3.500 el saco). Hacé clic en la celda y escribilo.
3. _(Opcional)_ Si el proveedor te dio un **descuento**, cargalo en la columna **`PorDto`** (% de descuento). Presto calcula solo el precio neto.
4. **La columna `Importe` se calcula sola** = cantidad × precio neto. No la toques.

!!! note "Tranquilo: este precio NO te pisa el presupuesto"
    El precio que ponés acá vive en una **tabla aparte, interna de compras**. **No modifica** ni el precio del presupuesto ni el objetivo de coste. Por eso podés registrar lo que de verdad te costó (para medir el desvío) sin arruinar tu presupuesto original. Son tres precios independientes que no se contaminan. `[00:40]`

---

## Tarea 8 — Ver el total y dejar la OC "a firme"

**Qué es:** revisar el total del pedido y **protegerlo** para que no se edite por error.

**Paso a paso** `[00:40]`–`[01:10]`:

1. Hacé **clic afuera** de la subventana `Suministros` (en cualquier fila de la cabecera de arriba). La columna **`BasePed`** de la cabecera te muestra ahora el **total del pedido** (la suma de todos sus materiales). ✅
2. Cuando ya revisaste todo y la OC está lista para mandar al proveedor, **marcala "a firme"**: hacé **clic derecho sobre la celda `Documento`** de esa OC → elegí **`Estado verde`**.
3. **La señal de que salió bien:** las celdas `Documento` y `Nota` quedan con **fondo verde**. A partir de ahí, las columnas `Cantidad` y `Precio` quedan **bloqueadas** (no se pueden editar por accidente). `[01:10]`

!!! warning "Importante: el \"estado verde\" NO es una aprobación"
    El verde solo **protege los campos** contra ediciones accidentales — **es reversible** (clic derecho → `Estado negro` y se desbloquea). **No es** un permiso ni una aprobación de tu jefe. Presto **no tiene** flujo de aprobaciones ni roles de usuario _(no es un ERP)_. Si en Raizant la compra necesita que alguien la apruebe antes, eso se controla **por fuera de Presto** (en el proceso de la empresa), no con este botón. `[01:10]`

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

> Video fuente: `Contratacion_30_12_2025.mp4` (2h 18min). Relator de soporte de Presto Chile.

---

## ⚠️ Lo que Presto NO te avisa (resumen)

- **Te copia el proveedor de la OC anterior** → podés comprarle al equivocado, en silencio. _(Tarea 4)_
- **Te deja pedir más de lo presupuestado** → sobre-pedido sin freno. _(Tarea 6)_
- **La fecha "de hoy" queda mal** si no la corregís. _(Tarea 3)_
- **El estado verde no es aprobación** → no confundir proteger con autorizar. _(Tarea 8)_
- **No hay import nativo de OCs** desde otro sistema → todo se teclea a mano (riesgo de error de digitación).

👉 Todas, con cómo blindarte, en [4 · Reglas de oro y fallas silenciosas](4-reglas-de-oro.md).

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá lo aprendido"
    Sobre la obra de prueba **BLEND** _(cuando el módulo Contratación esté activo)_:

    1. Creá una OC nueva (`Documento` con los tres puntos) y ponele la fecha de hoy bien.
    2. Asignale un proveedor de la tabla de Entidades.
    3. Cargale **2 materiales**: a uno ponele una **fracción** de la cantidad presupuestada (ej. la mitad) y mirá que el `Importe` se calcule solo.
    4. Sobrescribí el `Precio` de uno con un precio "real" inventado y verificá que **el total `BasePed`** de arriba cambie.
    5. Dejá la OC en **estado verde** y comprobá que ya no te deja editar la cantidad.

    **Cómo sabés que salió bien:** los materiales aparecen con ícono **naranja** 🟧, el total `BasePed` refleja tus cantidades y precios, y con el estado verde las columnas `Cantidad`/`Precio` quedan bloqueadas.

---

📖 **Fuente oficial:** Tutorial-de-Presto.pdf (RIB) · Apunte: C06 — Contratación y Pedidos (casos de uso 1–7) · Transcripción `Contratacion_30_12_2025`.
