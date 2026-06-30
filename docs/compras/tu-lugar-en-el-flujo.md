# Tu lugar en el flujo

!!! abstract "Para qué es esta página"
    Las demás páginas de Compras te enseñan **cómo** comprar en Presto. Esta te enseña **dónde encajás vos en el viaje del dato**: de quién recibís, qué entregás, de qué sos dueño y — lo más importante — **qué se rompe aguas abajo si tu dato sale tarde o sucio.** Es corta y vale la pena tenerla clara antes de emitir tu primera orden de compra.

!!! tip "Primero el panorama"
    Si todavía no leíste **[El flujo: el dato nace una vez y viaja](../flujo/index.md)**, empezá por ahí. Esta página es el aterrizaje de ese panorama a tu puesto.

## Dónde estás en el ciclo de compras

Compras es el **segundo y cuarto eslabón** del ciclo. No empezás vos (empieza la obra con la requisición) y no terminás vos (termina contabilidad con el pago). Estás en el medio, y eso te da una responsabilidad clave: **lo que vos cargás alimenta a todos los que vienen después.**

```
   OBRA          ►  VOS (COMPRAS)  ►  PRESUPUESTO  ►  VOS (COMPRAS)  ►  ALMACÉN     ►  CONTABILIDAD
   1. Pide          2. Cotiza          3. Gate         4. Emite OC       5. Recibe       6-8. Factura
   requisición      3 proveedores      aprueba         al adjudicado     + remito        y paga
                    ▲                                   ▲
                    └─── recibís de obra                └─── tu OC viaja a almacén Y a contabilidad
```

| | |
|---|---|
| **De quién recibís** | De **obra**: la requisición (qué se necesita y cuánto) |
| **Qué hacés** | Cotizás a 3 proveedores, y una vez aprobado el gate, **emitís la orden de compra** al adjudicado |
| **A quién se lo entregás** | A **almacén** (que recibe contra tu OC) y a **contabilidad** (que paga contra tu OC) |
| **Quién te controla** | El **gate de presupuesto** aprueba antes de la OC; el **almacén** recibe (vos no recibís lo que comprás) |

!!! warning "La regla que te toca: quien compra ≠ quien recibe"
    Vos **no recibís** el material que comprás. Lo recibe el almacén, independiente de vos. No es desconfianza: es lo que hace posible la **triple coincidencia** (orden ↔ remito ↔ factura). Si el que compra también recibe, nadie atrapa una entrega incompleta o un cobro de más.

## De qué datos sos dueño

Como compras, **sos el dueño** de estos datos. “Dueño” significa que nacen bien **porque vos los cargás bien** — nadie aguas abajo los puede arreglar:

| Dato | Qué es | Si lo cargás mal, aguas abajo… |
|---|---|---|
| **La orden de compra** | Lo que se pidió, a quién y a qué precio | Si editás el proveedor sin dejar rastro, la entrega y la factura no casan con la OC |
| **El ID único del proveedor** | El identificador del proveedor en el sistema | Si el mismo proveedor queda con **dos IDs distintos**, el puente a contabilidad (Syneco) **no lo reconoce** y la factura queda huérfana — invisible |
| **La factura del proveedor** (la registrás) | El documento que después concilia contabilidad | Si queda sin enganchar a una entrega, es una factura **huérfana**: nadie sabe a qué compra corresponde |

!!! danger "El caso que más se repite: el proveedor con dos identidades"
    Es el error silencioso más común de compras. Cargás “Ferretería López” hoy y “FERRETERIA LOPEZ SRL” la semana que viene como si fueran dos. Para vos son obvios el mismo; **para el sistema son dos proveedores distintos**. Cuando contabilidad intenta conciliar, el puente no casa y aparece un descuadre que cuesta horas rastrear. **Un proveedor, un ID, siempre.**

## El control que está en tus manos

| Control | Qué asegura | Cómo sabés que falla |
|---|---|---|
| **La compra nace de una requisición** | Que no se compre “por las dudas” sin pedido de obra | Hay una OC sin requisición que la respalde |
| **La OC tiene cotización + aprobación** | Que se compró al mejor precio y con visto bueno | Hay una OC que se emitió sin pasar por el gate |
| **El proveedor de la OC es el adjudicado** | Que no se cambió el proveedor después de comparar | El proveedor de la OC ≠ el que ganó la cotización |

!!! note "Presto no te obliga — el proceso sí"
    Recordá lo que aprendiste en los Fundamentos: **Presto registra la compra, pero no obliga** a cotizar ni a aprobar. No te va a frenar si emitís una OC sin gate. Por eso estos controles los cuida **el proceso de Raizant**, no el software. Sos vos quien cierra esa puerta.

## Tu aporte a las reglas de oro

De las [3 reglas de oro](../flujo/reglas-de-oro.md), la que más te toca es indirecta pero real: **una OC con el proveedor y el precio correctos** es lo que permite que, cuando el material llegue y se consuma, su **costo real** suba bien a la partida (Regla #1). Si tu OC tiene el precio mal, el costo real de la obra nace torcido desde el origen.

---

!!! info "¿Querés el detalle operativo?"
    Esta página es el **mapa**. El **cómo-hacer** clic por clic está en las demás páginas del rol: [Pedido manual](1-pedido-manual.md), [Contratos: cotizar y adjudicar](2-contratos-cotizar.md) y [Del pedido a la obra](3-del-pedido-a-la-obra.md).

!!! note "Responsables por definir"
    Algunos roles que se cruzan con el tuyo (como quién aprueba compras por encima de cierto monto, o el suplente del gate cuando no está disponible) están **⚠️ por definir** en la sesión de firmas. Esta página se actualiza cuando se cierren.
