# 0 · Fundamentos de Compras

!!! abstract "Conclusión primero"
    Antes de tocar un botón, hay **tres ideas** que hacen que todo lo demás se entienda: (1) hay **dos caminos** para llegar a una orden de compra; (2) en compras conviven **tres precios distintos que NO se pisan entre sí**; y (3) Presto **no es un ERP** — registra la compra, pero no te obliga a cotizar ni a aprobar. Si entendés esto, el resto del rol es seguir pasos.

---

## Idea 1 — Los dos caminos para comprar

Presto deja llegar a una **Orden de Compra (OC)** por dos caminos, y **no te obliga** a usar ninguno en particular:

```
                    ┌─────────────────────────────┐
   Camino A  ──────▶│   PEDIDO (Orden de Compra)   │
   (directo)        └─────────────────────────────┘
                                  ▲
   Camino B                       │  "pasar a pedido"
   (cotizar) ──▶ CONTRATO ──▶ adjudicar ──┘
```

| | 🅰️ Camino A — Pedido manual | 🅱️ Camino B — Vía Contratos |
|---|---|---|
| **Qué hacés** | Tecleás la OC directo: proveedor, materiales, cantidad, precio | Armás un lote, pedís precios a varios, comparás, **adjudicás** y Presto genera las OCs |
| **Cuándo** | Ya sabés a quién comprarle | Querés comparar ofertas antes de decidir |
| **Analogía** | Comprar en la ferretería de siempre | Pedir 3 presupuestos, elegir el mejor, comprar |
| **Página** | [1 · Pedido manual](1-pedido-manual.md) | [2 · Contratos: cotizar y adjudicar](2-contratos-cotizar.md) |

!!! warning "Lo que Presto NO te obliga (importante para Raizant)"
    Podés **saltarte Contratos por completo** y comprar directo, sin cotizar ni comparar. La doc lo confirma y el video lo repite: _"nada impide ir directamente a la ventana de pedidos"_. Que en Raizant **haya que cotizar** sobre cierto monto **no lo controla Presto** — es una regla del proceso de la empresa. _(C06 §0.2; Manual p. 126: la creación de contratos es una opción, no una obligación.)_

---

## Idea 2 — Los tres precios que no se contaminan

En el mundo de las compras hay **tres precios diferentes** del mismo material, y editar uno **no toca** los otros. Esto es clave para no romper el presupuesto sin querer:

| Precio | Qué es | Quién lo pone |
|---|---|---|
| **1. Precio del presupuesto** | El de presentación (lo que se cotizó al cliente) | Presupuestos (Enrique) |
| **2. Objetivo de coste** | La línea base de cuánto _debería_ costar | Sale de la planificación |
| **3. Precio de compra** | Lo que de verdad te cobró el proveedor | Vos, en la OC |

> 📖 **Fuente oficial:** Manual de Presto p. 138 — _"El precio por defecto es el precio contratado o el de objetivo, en este orden."_ El precio que escribís en la OC vive en la línea de suministro; **no reescribe** el presupuesto ni el objetivo.

!!! tip "Por qué esto es bueno"
    Como el precio de compra **no pisa** el objetivo, podés registrar lo que realmente pagaste **para medir el desvío** (¿compraste más caro o más barato de lo planeado?) sin arruinar la línea base congelada del presupuesto. Es justo lo que Raizant necesita para controlar costos. _(C06 §0.4.)_

---

## Idea 3 — Presto NO es un ERP

El relator de la capacitación lo repite varias veces, y es la advertencia más importante del rol: **Presto registra las compras, pero no es un sistema de gestión que controle el flujo por vos.**

Qué significa, en concreto:

| Lo que un ERP haría | Lo que Presto hace |
|---|---|
| Exigir aprobación del jefe antes de comprar | ❌ No hay flujo de aprobación |
| Roles y permisos por usuario | ❌ No hay usuarios; solo se ocultan ventanas por computadora (con contraseña) |
| Obligar la cadena pedido→entrega→factura | ❌ Es opcional; podés comprar sin recibir, recibir sin pedir |
| Registrar quién hizo cada cosa (auditoría) | ❌ Solo guarda el usuario de Windows |

> 📖 **Fuente oficial:** Manual de Presto p. 135 — _"El control económico se puede realizar por completo usando sólo facturas. La introducción de pedidos y entregas es opcional."_ · Confirmado en C06 §0.3 / video `[02:10]`.

!!! danger "La consecuencia para Raizant"
    Todo lo que Presto **no** obliga — aprobar antes de comprar, no pasarse del presupuesto, encadenar la entrega y la factura — **lo tiene que poner el proceso de Raizant** (la disciplina del equipo + el "tejido propio" que se está construyendo). Presto es el **registro** de la compra, no el **guardián** del flujo. Tenelo presente en cada paso del rol.

---

## El estado "verde": proteger ≠ aprobar

Un punto que confunde a todos: Presto deja marcar un documento en **estado verde ("a firme")**, que **bloquea** la cantidad y el precio para que no se editen por error.

⚠️ Pero el verde **NO es una aprobación.** Es reversible (un clic derecho lo desbloquea) y cualquiera con acceso lo puede cambiar. No es el "OK del jefe". Si en Raizant una compra necesita autorización, eso vive **fuera** de Presto.

> 📖 **Fuente oficial:** Manual p. 136 (estados de color = provisional/definitivo/protegido) y p. 138 (_"los campos Cantidad, Factor, PorDto, Precio e IVA de los documentos con estado verde se muestran como no editables"_).

---

## En resumen

- **Dos caminos:** comprar directo (A) o cotizar y adjudicar (B). Presto no te obliga a cotizar.
- **Tres precios:** el de compra no toca el presupuesto ni el objetivo → podés medir el desvío sin romper nada.
- **Presto no es ERP:** registra, no controla. La aprobación y el "no pasarse del presupuesto" los pone Raizant.

Con esto claro, seguí con **[1 · Pedido manual](1-pedido-manual.md)** para tu primera orden de compra.

---

📖 **Fuentes oficiales (RIB):** _Manual de Presto completo_, pp. 126, 135–138. · Complemento: apunte C06 (§0) · transcripción `Contratacion_30_12_2025`.
