# 0 · Fundamentos: entrega, costo real y bodega

!!! abstract "Conclusión primero"
    Antes de tocar un botón, entendé tres cosas y nunca te vas a perder: **(1)** una **Entrega** es el documento que registra que un material **llegó de verdad** a la obra; **(2)** ese material recién se vuelve **costo de una partida** cuando lo **imputás** con `Destino` + fecha (no cuando llega, sino cuando se usa); y **(3)** Presto registra **costo de obra, no inventario de almacén** — eso último se queda en Syneco.

!!! tip "Antes de arrancar, tené a mano el mapa"
    Si una palabra como _"la cabecera"_, _"la subventana Suministros"_ o _"la columna Destino"_ no la ubicás, abrí en otra pestaña **[🗺 La pantalla de Obra/Almacén](interfaz.md)**.

!!! info "De dónde sale este contenido"
    Fuente principal: **documentación oficial de Presto (RIB)** — _Manual de Presto completo_ (cap. Análisis de gastos y costes, pp. 147–152; Documentos, pp. 135–139) y _Tutorial de Presto_ (pp. 24–32). Se complementa con el apunte interno **C07 — Facturación y Entregas** y la transcripción del video **`FactCon_08_08_2025`** (de ahí salen los minutos `[hh:mm]`).

---

## 1 · ¿Qué es una Entrega? (= albarán = recepción)

Una **Entrega** es el documento que registra que un proveedor **te entregó material en la obra**. Es el equivalente Presto del **remito** o **nota de recepción de almacén** que firmás cuando llega el camión.

El propio Presto lo describe así en pantalla: _"documentos que acompañan a los suministros cuando se reciben en obra. Se considera que un suministro ha sido comprado si figura en algún documento de entrega o en una factura."_ `[00:30]`

El capacitador la llama **el corazón del módulo**: es la ventana que mete el **costo real auténtico** a la obra. Sin entregas cargadas, lo que de verdad se gastó es **cero** para Presto. `[00:30]` `[02:00]`

!!! note "Una entrega puede ser parcial"
    El proveedor no siempre te entrega todo de una vez. Si compraste 100 sacos y te llegaron 50, registrás una entrega de 50; los otros 50 los registrás en otra entrega cuando lleguen. **Cargás lo que efectivamente llega**, no lo que se compró. `[00:50]`

!!! note "No es solo para materiales"
    La misma Entrega sirve para registrar **mano de obra** (el documento es el cierre de la cuadrilla) y **subcontratos** (el documento refleja el avance del subcontratista). Cualquier cosa que se "reciba" y tenga un costo, entra por acá. `[00:30]` `[01:10]`

---

## 2 · Los 3 datos que TODOS confunden (leelo dos veces)

Esta es la confusión más común del rol. Hay **tres datos distintos** que la gente mezcla, y cada uno se carga en **otra pantalla**. Tu rol (Obra/Almacén) maneja principalmente el **#3**.

| # | El dato | Qué es en palabras simples | Dónde se carga | Lo cubre |
|---|---|---|---|---|
| 1 | **Certificación** (`CanCert`) | Lo que se le **cobra al cliente/mandante** (estados de pago). NO es lo que se hizo, es lo que se factura hacia afuera. | Módulo **Gestión de Proyectos** | Rol Control de obra |
| 2 | **Avance físico real** (`CanReal`) | Lo que **realmente se ejecutó** en obra (en cantidad). NO es plata, es cuánto se hizo. | Módulo **Facturación y Control**, pestaña `Árbol` | Rol Control de obra |
| 3 | **Costo real** (`ImpInput` / `ImpReal`) | El **dinero que de verdad se gastó** (precio real × cantidad consumida). | **Tu pantalla**: `Ver → Entregas` + `Suministros`, imputado con `Destino` + fecha | **Este rol** |

!!! danger "La trampa: certificación NO es lo mismo que costo real"
    - **Certificación** = lo que **entra** (lo que te paga el cliente).
    - **Costo real** = lo que **sale** (lo que gastás en material, gente, subcontratos).

    Son dos mundos distintos, en módulos distintos. Vos cargás el costo real. Si los confundís, la rentabilidad de la obra sale completamente mal.

---

## 3 · La regla de oro de las fechas (esto rompe a todo el mundo)

El costo real solo "entra" en el período correcto si la **fecha de imputación** del material cae **dentro de la fase de certificación actual**. Si la fecha queda afuera, Presto **no calcula nada** y la única señal que te da es que **la fecha se ve gris**. `[02:30]`

> **Regla de oro:** la fecha en que imputás el consumo tiene que estar alineada con el período de trabajo actual. Es el control crítico que ata costo real → período → flujo de caja. Si ves fechas grises, algo quedó fuera de fase.

Lo trabajás en detalle en [2 · Imputar el consumo](2-imputar-consumo.md) y en [5 · Reglas de oro](5-reglas-de-oro.md).

---

## 4 · Gasto ≠ Coste: por qué Presto NO es un sistema de almacén

Esta distinción es **oficial del Manual** y resuelve la duda más grande de logística:

> 📖 _"Los materiales en almacén representan un **gasto**, pero **no coste**, porque no se han utilizado. El gasto se imputa en la fecha del documento en que se adquiere el suministro… el coste en la fecha de utilización real o consumo."_ _(Manual, p. 148)_

En palabras simples:

- **Gasto** = la plata que salió cuando **compraste** el material (aunque todavía esté en la bodega sin usar).
- **Coste** = la plata que de verdad le pesa a **una partida**, y eso ocurre recién cuando el material **se consume** en la obra.

!!! warning "Conclusión clave para Raizant: el almacén se queda en Syneco"
    **Presto modela el COSTO de la obra, no el INVENTARIO del almacén.** No lleva stock multiobra, ni interdepósitos, ni traspasos entre obras. Todo eso (el almacén central, mover material entre obras, las devoluciones de stock) **se sigue manejando en Syneco**. Presto solo registra el **costo** cuando el material **se consume** en una partida de la obra. Lo ves en detalle en [3 · Material del almacén central y sobrantes](3-almacen-y-sobrantes.md).

---

## 5 · El ciclo completo, en un vistazo

Así encadena el material desde que se pide hasta que es costo real:

```
Pedido (OC)  →  Entrega (llega a obra)  →  Imputación (Destino + fecha)  →  Factura
   ↑ Compras      ↑ VOS (almacén)            ↑ VOS — el costo real           ↑ Administración
                                              sube a la partida
```

- **Pedido / OC:** lo hace el rol Compras (lo que se va a comprar).
- **Entrega:** vos registrás que el material **llegó**. → [Tarea 1](1-recepcion-entrega.md)
- **Imputación:** vos decís a **qué partida** se gastó y **cuándo**. Acá nace el costo real. → [Tarea 2](2-imputar-consumo.md)
- **Factura:** Administración la registra cuando llega la factura del proveedor. → [Tarea 4](4-del-pedido-a-la-factura.md)

!!! note "Lo importante: la entrega ya es documento de costo, sin esperar la factura"
    El Tutorial oficial lo dice claro: el costo se calcula _"a partir de los suministros anotados en documentos de coste (**entregas Y/O facturas**)"_ _(Tutorial, p. 30)_. Ese **"y/o"** significa que **la entrega por sí sola ya mete el costo real** — si el material llegó pero la factura todavía no, el costo de la obra **ya está cargado** con el precio del albarán. La factura solo lo confirma o corrige después.

---

## En una frase

Tu trabajo registra **que el material llegó** (Entrega) y **a qué partida se gastó** (Destino + fecha). Eso —y solo eso— hace que la obra tenga un **costo real de verdad**, no uno presupuestado. Sin tu carga, la torre de control vuela a ciegas.
