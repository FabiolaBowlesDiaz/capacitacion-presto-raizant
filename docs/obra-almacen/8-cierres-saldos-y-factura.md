# 8 · Cierres, saldos y la factura del proveedor

!!! abstract "Conclusión primero"
    Esta página cierra el ciclo que empezaste en [1 · Recibir material](1-recepcion-entrega.md) y [4 · Del pedido a la factura](4-del-pedido-a-la-factura.md). Acá aprendés **cuatro cosas**: (1) leer los **saldos** — pedí 100, ¿cuánto recibí, cuánto consumí, cuánto queda en bodega?; (2) qué hay que revisar en la **factura del proveedor** después del `Pasar a factura` (el orden importa: **fecha → IVA → vencimiento**) y cómo se marca el **pago efectivo** (estado verde); (3) cómo se **cierra un periodo** — spoiler: Presto no tiene un botón "cerrar", el cierre es una disciplina de fechas + estados + checklist; y (4) el **three-way match** OC↔remito↔factura como checklist operativo antes de mandar a pagar.

!!! tip "Antes de arrancar, tené a mano el mapa"
    Si `BasePed`/`BaseEnt`/`BaseFac`, _"desdoblar"_ o _"la fase de certificación actual"_ no te suenan, pasá antes por **[🗺 La pantalla de Obra/Almacén](interfaz.md)** y **[0 · Fundamentos](0-fundamentos.md)**. Esta es la página más "de control" del rol: supone que ya sabés recibir e imputar.

!!! warning "Requisito de licencia"
    Necesitás el módulo **Facturación y Control**. Para ver pedidos (OC) también entra en juego **Contratación** (del rol Compras).

!!! info "De dónde sale este contenido"
    Fuente principal: apuntes **07** (Facturación y Control) y **C07** (entregas, casos 9–11) + video `FactCon_08_08_2025` (3h48m). Cada paso cita su `[hh:mm]`. Lo que las fuentes no muestran queda marcado **"verificar en Presto"** — no lo inventamos.

---

## 1 · Los saldos: pedí 100 — ¿cuánto recibí, cuánto consumí, cuánto queda?

La vida de un material tiene **cuatro números** que casi nunca coinciden, y cada uno vive en su columna:

```
PEDIDO (OC)  →  RECIBIDO (entrega)  →  CONSUMIDO (imputado)  →  BODEGA (existencia)
  BasePed          BaseEnt                BaseDest              recibido − consumido
```

| Pregunta | Dónde mirarlo |
|---|---|
| Pedí 100, ¿cuánto **recibí**? | En la cabecera `Entregas`: comparar **`BasePed`** (base del pedido) vs **`BaseEnt`** (base de la entrega). Para la vista consolidada por proveedor o por material, usá los **tres lugares** de la [página 4, sección 4](4-del-pedido-a-la-factura.md#4-cuanto-material-falta-por-recibir-tres-lugares-para-verlo) — no los repetimos acá. |
| Recibí 100, ¿cuánto **se consumió**? | En la cabecera `Entregas`: **`BaseDest`** = lo ya imputado a partidas (con `Destino` + fecha). En la línea de suministro, lo desdoblado **con** `Destino` es consumo; lo desdoblado **sin** `Destino` es saldo. |
| ¿Cuánto **queda en bodega** de la obra? | **`existencias = lo comprado − lo imputado`** — Presto lo calcula solo _(Manual, pp. 149/151, ver [página 3](3-almacen-y-sobrantes.md))_. Vista por material: ventana **`Insumos`** → esquema **`[Suministros] Existencias y consumos`**. |
| ¿Y el detalle línea por línea? | Menú **`Ver → Suministros`**, esquema **`*`**: relaciona cada suministro con su entrega, su factura, cantidades, `CanNeta`, precios reales e importes. Exportable a Excel `[03:40]`. |

!!! note "Presto sí sabe el \"total de compras\", pero no te hace la resta"
    Al recibir por segunda vez el mismo material, la sugerencia de cantidad muestra el **total ya comprado** (ej. "hay 100 comprados"), pero en el video **la resta automática del saldo pendiente falló** — el capacitador mismo dijo _"no me lo está haciendo, pero en teoría debería"_ `[01:20]`. La cuenta "cuánto falta" la hacés vos (o el tejido in-house de Raizant). Ya lo viste como Falla silenciosa #3 en la [página 4](4-del-pedido-a-la-factura.md).

!!! warning "Bodega de la obra ≠ almacén central"
    La existencia que calcula Presto es **de tu obra** (lo que recibiste y aún no imputaste). El inventario del **almacén central** sigue viviendo en Syneco — ver [3 · Almacén y sobrantes](3-almacen-y-sobrantes.md).

---

## 2 · La factura del proveedor: lo que viene DESPUÉS de `Pasar a factura`

El mecanismo básico de `Pasar a factura` (clic derecho sobre el `Documento` de la entrega → folio → aceptar) ya lo viste en la [página 4, sección 3](4-del-pedido-a-la-factura.md#3-pasar-a-factura-cuando-llega-la-factura-del-proveedor). Acá va **lo que esa página no cubre**: el orden correcto de revisión, la variante por línea, y el IVA local.

### 2.1 El orden importa: fecha → IVA → vencimiento

📖 **Fuente:** apunte 07 §3.E + video `[02:40]`–`[02:50]`.

1. **Fecha de la factura primero.** Presto pone la fecha de hoy; corregila a la del folio real. Recordá: `facturas.fecha` ≠ `entregas.fecha` — _"no son el mismo campo por si acaso"_ `[02:40]`.
2. **Después el IVA.** Seleccionar **todas** las celdas de la columna `IVA` → clic derecho → **`Sugerir`** → elegir el IVA local. En el video: _"siempre primer paso, revisen el IVA... porque después el tema del vencimiento va a agarrar el IVA que aparece acá"_ `[02:40]`.
3. **Recién ahí el vencimiento.** Clic derecho sobre el código del documento → elegir plazo (contado, mes actual, 14/30/45/60 días, dos vencimientos). La subventana `Vencimientos` calcula importe, fecha de pago e IVA `[02:50]`.

!!! danger "Si el vencimiento se calculó con el IVA equivocado o la fecha equivocada: borrá y rehacé"
    El propio capacitador se equivocó de fecha en el video y lo mostró: **borrá las líneas de la subventana `Vencimientos`** (marcar fila → suprimir), **corregí** la fecha o el IVA, y **volvé a elegir** el vencimiento con clic derecho. _"No es algo que en el Presto no se pueda revertir."_ `[03:00]`

!!! note "IVA de Bolivia — parametrizar una vez, verificar en Presto"
    Presto trae el IVA de **España** por defecto y el curso usa 19% (Chile) `[02:40]`. Para Raizant hay que **parametrizar el IVA boliviano** — IVA **13%** (y evaluar cómo tratar el **IT 3%**, que no es un IVA) — ⚠️ **verificar en Presto** cómo se da de alta un tipo de IVA local en la lista de `Sugerir` y **confirmar las tasas vigentes con contabilidad** antes de facturar en serio. _(Apunte 07 §10.5.)_

### 2.2 Variante: pasar a factura UNA LÍNEA (el caso subcontratos)

No siempre facturás el documento entero. Al **subcontratista se le paga por avance**: si en el periodo hizo el 20% del global, la factura es solo por esa fracción.

**Paso a paso** `[03:00]`:

1. En la subventana `Suministros`, seleccioná la **línea desdoblada** del avance (ej. el 20% del global — ver [página 2](2-imputar-consumo.md) para desdoblar).
2. Clic derecho **sobre esa línea** (cualquier celda) → **`Pasar a factura`** → folio (ej. `FC-N-S-001-01` si es el primer pago de varios).
3. La factura nace **solo con esa línea**: la otra fracción queda sin facturar, esperando el siguiente avance. El monto base = solo el importe de esa línea.

> _"Se puede hacer al detalle... quizás no es muy recurrente a nivel de recursos, pero sí para el tema de los subcontratos se hace muchas veces de esa forma."_ `[03:00]`

### 2.3 Dar de alta el pago: los estados (negro → verde)

Registrar la factura **no** le dice a Presto que se pagó. _"El Presto todavía no sabe que esto tiene que tomarse como egresos... está como a la espera."_ `[03:00]` Son **dos pasos**, normalmente de Administración, pero tenés que conocerlos porque cierran el ciclo que vos abriste:

| Paso | Dónde | Qué significa |
|---|---|---|
| 1. Documento **negro → verde** | Clic derecho sobre el código del documento de factura → estado | Negro = "en firme" (recepcionada, en el sistema). **Verde = revisada/aprobada** (pasó el chequeo de compras/contable) `[03:00]` |
| 2. Vencimiento **rojo → verde** | En la subventana `Vencimientos`, pararse en la nota (texto rojo) → clic derecho → estado verde | Rojo = pago **pendiente**. Verde = **se pagó efectivamente**. _"Eso recién en Presto va a decir: aquí efectivamente hay un egreso"_ `[03:00]` |

- La columna **`Banco`** registra la entidad bancaria del pago (no sugiere nada; se digita) `[03:00]`.
- El color en `Vencimientos` no es error: **rojo = pago** (egreso al proveedor), **negro = cobro** (ej. devolución de IVA) `[02:50]`.
- Hasta que el vencimiento no está verde, ese importe figura como **"pago pendiente"** en el flujo de caja — es dato de proyección, no de gasto ejecutado `[03:30]`.

---

## 3 · "Cerrar" una entrega o un periodo: qué es de verdad

Acá va una verdad incómoda: **Presto no tiene un botón "cerrar entrega" ni "cerrar mes"**. En las fuentes no aparece ningún candado nativo que congele un documento o un periodo. Lo que existe es una **combinación de tres mecanismos** que, usados con disciplina, equivalen a un cierre:

| Mecanismo | Qué "cierra" | Dónde vive |
|---|---|---|
| **La fase de certificación actual** | El periodo: toda fecha de imputación **fuera** de la fase actual queda **gris y no suma** `[02:30]` | Módulo Gestión de Proyectos (rol [Control de obra](../control-obra/index.md)); cuando Control de obra avanza la fase, tu periodo quedó de facto cerrado |
| **Los estados** (negro → verde) | El documento: verde = revisado/aprobado; ya no debería tocarse | Facturas y vencimientos (sección 2.3) |
| **El checklist de cierre** (abajo) | La calidad del dato antes de soltar el periodo | Proceso Raizant, no Presto |

!!! warning "Lo que el \"cierre\" bloquea — y lo que NO"
    Cerrar el periodo (avanzar la fase) **no borra ni congela** tus entregas: solo hace que las imputaciones con fecha vieja **dejen de calcular** si caen fuera de la fase actual — el único síntoma es la **fecha gris** `[02:30]`. Presto tampoco impide que alguien edite un documento "cerrado" en verde. El candado duro (snapshot, permisos) es **tejido in-house de Raizant**, no Presto. ⚠️ Si en tu versión aparece alguna opción de bloqueo de documentos, **verificar en Presto** — las fuentes no la muestran.

**Tu checklist ANTES de que Control de obra avance la fase** (esto es lo que sí depende de vos):

1. ☐ Todas las entregas del periodo están **registradas y fechadas** con su fecha real (no la heredada del documento anterior — [FS-1](5-reglas-de-oro.md)).
2. ☐ Todo lo que salió de bodega está **imputado** (`Destino` + fecha **dentro de la fase actual**). Buscá fechas **grises** en `Suministros`: gris = no está sumando `[02:30]`.
3. ☐ **Mano de obra**: el cierre mensual/quincenal (libro de asistencia consolidado) está desdoblado e imputado `[01:10]`, `[01:40]`.
4. ☐ **Subcontratos**: el avance del periodo está desdoblado, imputado y (si corresponde pago) pasado a factura por línea (sección 2.2).
5. ☐ `Inicio → Recalcular` y verificar que el **`ImpReal`** de tus partidas refleja el periodo ([página 2](2-imputar-consumo.md)).
6. ☐ Correr el filtro de **entregas sin factura** (sección 4) y avisar a Administración de las huérfanas.

**Consecuencia de cerrar mal:** si te quedó una imputación sin hacer y la fase ya avanzó, al cargarla después con la fecha real vieja **no va a sumar nada** (fecha gris) — y si le ponés una fecha nueva para que sume, el costo cae **en el mes equivocado**. Las dos opciones son malas: por eso el checklist va **antes** del cierre.

---

## 4 · El three-way match OC↔remito↔factura: checklist antes de mandar a pagar

El concepto ya lo viste en [El flujo → Los dos ciclos](../flujo/los-dos-ciclos.md): ninguna factura se paga si no coincide con **lo que se pidió** (OC) y **lo que llegó** (remito = entrega). Acá está como **procedimiento operativo**.

**Dónde se hace:** menú **`Ver → Suministros`** → esquema **`Entrega facturas compras en firme`** (o `*`) — la tabla que relaciona cada suministro con su entrega y su factura `[03:40]`. Es exportable a Excel para el cruce formal.

**El checklist (por factura, antes de aprobar el pago):**

| # | Chequeo | Cómo | Si no cuadra |
|---|---|---|---|
| 1 | **¿La factura nace de una entrega?** | La factura debe haberse creado con `Pasar a factura` (la columna `factura` de los suministros tiene el folio). Una factura digitada a mano _"pierde la conexión o pierde el seguimiento"_ `[02:40]` | Rechazar el atajo: pedí que se rehaga desde la entrega |
| 2 | **¿La entrega tiene OC detrás?** | Cabecera `Entregas`: **`BasePed`** con valor. | ⚠️ Presto **no obliga** este enlace ([página 4, sección 6](4-del-pedido-a-la-factura.md)); una entrega sin OC necesita justificación (¿material de almacén? → va por [Parte de obra](3-almacen-y-sobrantes.md), no por entrega) |
| 3 | **¿Cantidad facturada = cantidad recibida?** | En `Ver → Suministros`: comparar `Cantidad`/`CanNeta` de la línea contra el folio físico del proveedor | Diferencia = factura por material que no llegó (o llegó de más sin OC): frenar |
| 4 | **¿Precio factura = precio OC/entrega?** | `Precio`/`PrNeto` de la línea (heredado de la OC si encadenaste bien — [página 4](4-del-pedido-a-la-factura.md)) vs precio del folio | Diferencia de precio = renegociación no registrada o error del proveedor: aclarar antes de pagar |
| 5 | **¿Fecha e IVA correctos?** | `facturas.fecha` = fecha del folio; IVA local, no el de España (sección 2.1) | Corregir ANTES del vencimiento (el vencimiento arrastra el IVA) `[02:40]` |
| 6 | **¿Vencimiento real?** | Subventana `Vencimientos`: plazo pactado con el proveedor, no el "contado" fantasma de entidades creadas a mano ([FS-6, página 4](4-del-pedido-a-la-factura.md)) | Borrar el vencimiento y recrear con el plazo real |

!!! danger "Presto te da la tabla, no el control"
    La tabla `Ver → Suministros` **cruza** entrega↔factura y el modelo tiene `BasePed` para la OC — pero **nada en Presto frena** una factura sin entrega, una entrega sin OC, o un precio distinto. El match **obligatorio** es proceso de Raizant: este checklist es la versión manual mientras el tejido in-house no lo automatice. _(Apunte 07 §6 y C07 FS-4.)_

---

## 5 · Registrar el avance físico real (`CanReal`) — y en qué se diferencia de certificar

Cerraste el periodo con los **costos** (secciones 1–3); falta el otro dato de ejecución: **cuánto se ejecutó físicamente**. Es un número distinto de todo lo anterior:

| Dato | Qué es | Dónde se registra |
|---|---|---|
| **`CanCert`** (certificado) | Avance **aprobado para cobro** al cliente. No es avance físico | Rol [Control de obra](../control-obra/2-certificar-avance.md) (Gestión de Proyectos) |
| **`CanReal`** (ejecutado) | Lo **realmente ejecutado** en obra, en cantidad. No es dinero | Pestaña **`Árbol`** → esquema **`Control de costes | FASES`** → columna `CanReal` (módulo Facturación y Control) |
| **Consumo imputado** | El **dinero** del costo real | `Ver → Entregas` ([página 2](2-imputar-consumo.md)) |

**Paso a paso** `[00:00]`, `[00:10]`:

1. Pestaña **`Árbol`** → menú **Esquemas** → **`Control de costes | FASES`**.
2. En las columnas pareadas por fase, cambiar el modo de la primera columna a **`CanReal`** (menú desplegable de visualización; la lista es alfabética).
3. Digitar la **cantidad ejecutada** por fase. Apoyo: abrir la subventana **`Fases`** con esquema **`Planificación y certificación`** para ver al lado lo planificado y lo certificado; el botón de tres puntos sugiere esos valores `[00:10]`.
4. Podés ejecutar **más de lo que te certifican** (ej. ejecutaste 110, te certificaron 100): son campos distintos y el orden natural es **primero ejecución, después certificación** `[00:10]`, `[00:20]`.

!!! note "Para qué sirve si no mueve dinero"
    `CanReal` alimenta la columna `RealObj` (cantidad real × precio objetivo = costo estimado) y las curvas de desviación EVM `[00:20]`. Y es **requisito** del costo real: _"sin esta información de cantidad ejecutada el Presto igual no te va a calcular costo real"_ `[00:30]`. Quién lo digita en Raizant (¿jefe de obra? ¿almacén?) es una definición del [flujo](../flujo/los-dos-ciclos.md) — ⚠️ pendiente de la sesión de firmas.

---

## ⚠️ Fallas silenciosas de esta página

!!! warning "Falla silenciosa — la entrega sin factura es invisible hasta que alguien filtra"
    Presto **nunca avisa** que una entrega quedó sin su factura: la huérfana solo aparece si alguien corre el filtro de `Ver → Suministros` → columna `factura` → filtrar por vacío ([página 4, sección 5](4-del-pedido-a-la-factura.md)). **No es teoría:** al mapear el proceso anterior se encontraron **cientos de miles de dólares en órdenes de pago sin factura asociada** — meses de compromisos que ningún sistema mostraba. El blindaje: correr el filtro en **cada cierre** (checklist, sección 3) y alertar entregas sin factura de más de N días.

!!! warning "Falla silenciosa — la fecha de imputación fuera de fase no suma y solo lo \"dice\" en gris"
    Si imputás con fecha fuera de la fase de certificación actual, **no hay error, no hay aviso**: el importe simplemente no calcula y la fecha se ve gris `[02:30]`. En un cierre apurado, eso es costo real que desaparece del mes. Revisión de fechas grises = paso 2 del checklist de cierre.

!!! warning "Falla silenciosa — vencimiento calculado antes de corregir IVA o fecha"
    El vencimiento **arrastra** el IVA y la fecha que encuentre al momento de crearse `[02:40]`, `[03:00]`. Si después corregís el IVA, el vencimiento viejo queda mal calculado y nadie protesta. Orden siempre: fecha → IVA → vencimiento; si te equivocaste, borrar el vencimiento y rehacer.

👉 El resto de las fallas del ciclo (entidad/fecha heredadas, saldo no confiable, vencimiento "contado" fantasma) están en [5 · Reglas de oro y fallas silenciosas](5-reglas-de-oro.md).

---

## 🎥 Mirá el video

| Tema | Minuto | Video |
|---|---|---|
| `CanReal`: esquema, columnas pareadas, sugerencia | `[00:00]`–`[00:20]` | `FactCon_08_08_2025` |
| Saldo pendiente / total de compras (y la resta que falló) | `[01:20]` | `FactCon_08_08_2025` |
| Fecha de factura ≠ fecha de entrega; IVA con `Sugerir` | `[02:40]` | `FactCon_08_08_2025` |
| Vencimientos: plazos, rojo=pago/negro=cobro, borrar y rehacer | `[02:50]`–`[03:00]` | `FactCon_08_08_2025` |
| Pasar a factura una línea (subcontrato por avance) | `[03:00]` | `FactCon_08_08_2025` |
| Estados negro→verde; vencimiento rojo→verde = egreso efectivo | `[03:00]` | `FactCon_08_08_2025` |
| Tabla `Ver → Suministros` y filtro "sin factura" | `[03:40]` | `FactCon_08_08_2025` |

> _El video es complemento: cada afirmación de esta página cita su timestamp; lo no visto en fuentes quedó marcado "verificar en Presto"._

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá un cierre completo"
    Sobre **BLEND** _(con licencia de Facturación y Control)_, simulá el cierre de un periodo:

    1. **Saldos:** elegí un material con entrega registrada y contestá las tres preguntas: ¿cuánto se pidió (`BasePed`), cuánto llegó (`BaseEnt`), cuánto se consumió (`BaseDest`)? Verificá la existencia en `Insumos → [Suministros] Existencias y consumos`.
    2. **Factura por línea:** tomá una entrega de subcontrato (o simulá una), desdoblá un avance parcial y hacé `Pasar a factura` **sobre esa línea**. Comprobá que la factura nace solo con ese importe.
    3. **Orden fecha → IVA → vencimiento:** en esa factura, corregí primero la fecha, después el IVA (clic derecho → `Sugerir`), y recién ahí asigná vencimiento a 30 días. Después equivocate a propósito: borrá el vencimiento, cambiá la fecha y rehacelo.
    4. **Pago efectivo:** pasá el documento a estado verde y el vencimiento de rojo a verde. Andá a `Fechas → Meses facturación` y mirá cómo el importe se movió de "pago pendiente" a "pago".
    5. **Cierre:** corré el checklist de la sección 3: buscá fechas grises en `Suministros`, recalculá, y filtrá `Ver → Suministros` por columna `factura` vacía.

    **Cómo sabés que salió bien:** podés contestar las 3 preguntas de saldo sin dudar, la factura parcial tiene solo el importe de la línea, el vencimiento quedó con IVA y fecha correctos, el pago verde aparece como egreso, y sabés exactamente qué entregas quedaron huérfanas.

---

📖 **Fuentes internas:** apuntes `07-facturacion-y-control.md` (§3.E–G, §8, §10) y `C07-modulo-facturacion-entregas-casos-uso.md` (casos 9–11, FS-2/FS-4) · transcripción `FactCon_08_08_2025` (timestamps citados).
**Complementa a:** [4 · Del pedido a la factura](4-del-pedido-a-la-factura.md) (el encadenado OC→entrega→factura) y [Los dos ciclos](../flujo/los-dos-ciclos.md) (el three-way match como concepto).
