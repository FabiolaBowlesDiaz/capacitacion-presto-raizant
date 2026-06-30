# La pantalla de Compras: dónde está cada cosa

!!! abstract "Por qué esta página va primero"
    Igual que en presupuesto, lo que más cuesta de Compras **no es entender qué es una orden de compra — es no perderse entre menús y botones.** Esta página es tu mapa de las **dos ventanas** del módulo (`Pedidos` y `Contratos`) y su subventana compartida (`Suministros`). Volvé a ella cada vez que una tarea te diga "andá a tal botón".

!!! tip "Cómo leemos las rutas de clic"
    En todas las tareas vas a ver caminos escritos así: **`Ver ▸ grupo Documentos ▸ Pedidos`**. Se lee de izquierda a derecha: primero la **pestaña** de la cinta (`Ver`), después el **grupo** dentro de esa pestaña (`Documentos`), y por último el **botón** (`Pedidos`).

!!! warning "Antes que nada: ¿tu licencia tiene Compras?"
    Las ventanas de este rol **solo aparecen si la licencia incluye el módulo de Contratación**. Cómo verificarlo está abajo, en "Cómo saber si tenés el módulo".

---

## Las dos ventanas del módulo Compras

Todo el rol vive en **dos ventanas**, más una subventana que comparten:

| Ventana | Qué es | Cada fila es… |
|---|---|---|
| **`Pedidos`** | Las **Órdenes de Compra** (lo que le pedís a un proveedor) | Una OC |
| **`Contratos`** | Los **lotes de cotización** (comparar precios y adjudicar) | Un lote/grupo de compra |
| **`Suministros`** _(subventana)_ | El **detalle** del documento seleccionado arriba | Una línea: un material con su cantidad y precio |

> 📖 **Fuente oficial:** Manual de Presto, cap. *Contratación y compras* (p. 126) y *Facturación / Documentos* (p. 135–136).

---

## Cómo se abren (botones del grupo `Documentos`)

Las ventanas se prenden desde la **cinta de arriba ▸ pestaña `Ver` ▸ grupo `Documentos`**. Son **botones tipo interruptor**: al hacer clic quedan **hundidos/marcados** mientras la ventana está abierta (igual que `Árbol`, `Presupuesto` o `Conceptos`).

!!! info "Qué botones deberías ver en el grupo `Documentos`"
    Con el **módulo de Contratación activo**, el grupo `Documentos` muestra: **`Insumos`**, **`Vencimientos`**, **`Pedidos`**, **`Contratos`**, **`Entregas`** y **`Facturas`**.

    ⚠️ Si **solo ves `Insumos` y `Vencimientos`** (sin `Pedidos`/`Contratos`/`Entregas`/`Facturas`), tu licencia **todavía no tiene el módulo de Contratación**. Podés estudiar el manual, pero no operar.

---

## La zona de Pedidos (camino A — comprar directo)

Cuando abrís `Pedidos`, la pantalla se parte en **dos franjas**:

- **Arriba — la cabecera:** un renglón por OC. Las columnas clave:

| Columna | Qué es |
|---|---|
| **`Documento`** | El número de la OC (ej. `P00001`) |
| **`Entidad`** | El **proveedor** (su código) |
| **`Resumen`** | El **nombre** del proveedor (se llena solo) |
| **`Fecha`** | Fecha de emisión _(y muestra el color de estado)_ |
| **`BasePed`** | El **total** del pedido |

- **Abajo — la subventana `Suministros`:** el detalle de la OC seleccionada. Las columnas clave:

| Columna | Qué es |
|---|---|
| **`Código`** | El material/recurso que pedís |
| **`Cantidad`** | Cuánto pedís |
| **`Precio`** | Precio real de compra |
| **`PorDto`** | % de descuento (opcional) |
| **`Importe`** | Se calcula solo (cantidad × precio neto) |

> 📖 Glosario de columnas verificado: Manual p. 137–138 + apunte C06 §6.

---

## La zona de Contratos (camino B — cotizar y adjudicar)

Cuando abrís `Contratos`, también hay cabecera (un renglón por lote) y la subventana `Suministros`, **pero acá la subventana es la tabla comparativa de precios**:

| Columna | Qué es |
|---|---|
| **`Código`** _(cabecera)_ | El lote/grupo de compra (ej. `MAE` = áridos) |
| **`Proveedor`** | El proveedor **adjudicado** (se llena al adjudicar) |
| **`NumPro`** | Cuántos proveedores estás comparando |
| **`1: Precio` / `2: Precio`** | El precio que cotizó cada proveedor _(la cabecera de la columna muestra su código)_ |
| **`1: Importe` / `2: Importe`** | El total de cada proveedor (precio × cantidad) — **acá comparás** |

> 📖 **Fuente oficial:** Manual de Presto, p. 126–130 (Contratos, asociar proveedores, adjudicar).

---

## La marca naranja 🟧 — tu semáforo de "ya pedido"

Un dato que vas a usar todo el tiempo: en la ventana `Conceptos`, cuando un material **ya figura en algún Pedido, Contrato, Entrega o Factura**, su ícono **se pone naranja** 🟧. Sin naranja = todavía no lo pediste. Es la forma rápida de ver, de un vistazo, qué falta comprar.

> 📖 **Fuente oficial:** Manual de Presto (la propiedad Suministro y su marca) · confirmado en C06 §6 / video `[00:30]`.

---

<div class="admonition success">
<p class="admonition-title">Ya tenés el mapa</p>
<p>Con esto, cuando una tarea diga "andá a <code>Ver ▸ Documentos ▸ Pedidos</code>" o "mirá la columna <code>BasePed</code>", sabés exactamente dónde mirar. Seguí con <a href="../0-fundamentos/">0 · Fundamentos de Compras</a>, o saltá directo a <a href="../1-pedido-manual/">1 · Pedido manual</a>.</p>
</div>

!!! note "Las capturas de estas pantallas llegan con el Cloud"
    Como el módulo de Contratación todavía no está activo en la licencia actual, las **capturas reales** de `Pedidos` y `Contratos` se agregan cuando se active (mismo método que usamos en el rol Presupuestos). Por ahora, el texto espacial te orienta igual.

---

📖 **Fuentes oficiales (RIB):** _Manual de Presto completo_, cap. Contratación y compras (pp. 126–130) y Facturación / Documentos (pp. 135–138). · Complemento: apunte C06 §6 (glosario de columnas).
