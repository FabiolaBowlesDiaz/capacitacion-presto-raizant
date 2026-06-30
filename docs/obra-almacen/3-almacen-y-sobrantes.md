# 3 · Material del almacén central y sobrantes

!!! abstract "Conclusión primero"
    Cuando un material **viene del almacén central** (sobró de otra obra, ya está comprado, no hay compra nueva), **no se registra como una entrega de proveedor**: se carga como **Parte de obra** imputándolo directo a la partida (`Destino` + fecha + precio). Y cuando un material **sobra y vuelve** a la bodega, se corrige con cantidad negativa. Pero lo más importante de entender: **Presto NO lleva el inventario del almacén** — eso se queda en Syneco. Presto solo registra el **costo** cuando el material **se consume** en la obra.

!!! tip "Antes de arrancar, tené a mano el mapa"
    Si _"parte de obra"_, _"Destino"_ o _"cantidad negativa"_ no te quedan claros, leé primero **[0 · Fundamentos](0-fundamentos.md)** (la parte de "gasto ≠ coste") y tené a mano **[🗺 La pantalla](interfaz.md)**.

!!! warning "Requisito de licencia"
    Igual que el resto del rol: necesitás el módulo **Facturación y Control** en la licencia.

!!! info "De dónde sale este contenido"
    Fuente: **documentación oficial de Presto (RIB)** — _Manual de Presto completo_, pp. 147–152 (gasto ≠ coste, destinos, partes de obra, existencias), p. 110 (los 3 tipos de concepto), p. 55 (obras enlazadas). Verificado contra la práctica de Raizant (migración Syneco → Presto).

---

## 1 · La idea grande: Presto registra COSTO, no INVENTARIO

Esta es la conclusión que más confusión evita, y es **oficial del Manual**:

> 📖 _"Los materiales en almacén representan un **gasto**, pero **no coste**, porque no se han utilizado."_ _(Manual, p. 148)_

Traducido a Raizant:

- El material que está en el **almacén central** ya es un **gasto** (se compró en su momento, en otra obra o como stock).
- Recién se vuelve **costo de BLEND** (o de la obra que sea) cuando **se manda a la obra y se consume** en una partida.

!!! danger "Lo que NO hace Presto (y por qué el almacén se queda en Syneco)"
    Presto **no es un sistema de gestión de almacén/stock**. No lleva:

    - ❌ Inventario multiobra (qué hay en la bodega central y cuánto).
    - ❌ Interdepósitos (mover material entre depósitos).
    - ❌ Traspasos de stock entre obras.

    Todo eso **se sigue manejando en Syneco**, como hoy. Presto-obra solo registra el **costo** del material cuando se consume. **No intentes modelar el almacén central como una "obra" de Presto** — no tiene un movimiento nativo para entregar material de una obra a otra, y solo agrega complejidad sin resolver nada.

---

## 2 · Cómo se reparte el trabajo entre los dos sistemas

| Qué cosa | Dónde se registra | Qué guarda |
|---|---|---|
| Inventario del almacén central + interdepósitos + devoluciones de stock | **Syneco** (como hoy) | El **gasto** y el movimiento físico entre depósitos |
| El **costo** del material cuando se consume en la obra | **Presto** (la obra) | El **coste**: parte de obra → partida (`Destino` + fecha + precio) |

---

## 3 · Caso A — Material del almacén llega a la obra (sin compra)

Sobró material de otra obra, está en el almacén central, y ahora se asigna a tu obra. **No hubo compra nueva**, así que no hay un proveedor que te dé un albarán. Por eso no es una entrega de proveedor común: se usa un **Parte de obra**.

📖 **Fuente oficial:** Manual de Presto, p. 150 (el Parte de obra imputa consumo sin entrega ni factura).

**Qué es un Parte de obra:** un documento que **imputa consumo directo a una partida**, sin necesidad de una orden de compra ni una factura detrás. Es el camino limpio para meter a la obra un material que ya existía.

**Qué cargás:**

| Campo | Qué poner |
|---|---|
| **`Destino`** | La **partida** de la obra donde se usa el material (debe existir y tener la propiedad Destino) |
| **`Fecha`** (FecInput) | La fecha real en que se consumió |
| **`Precio`** | El valor del material en el almacén |
| **`Cantidad`** | Lo que se consumió |

Con `Destino` + fecha + precio, el costo sube a la partida **igual que en una entrega normal** — la diferencia es que no hubo OC ni factura. El Manual lo habilita expresamente: el costo se calcula de _"entregas **y/o** facturas"_ — ese "y/o" permite registrar costo **sin compra**.

!!! note "Alternativa: entrega manual sin OC"
    También se puede cargar como una **entrega manual** (sin orden de compra detrás), poniendo el precio del material a mano. El Parte de obra es la vía más limpia porque está pensada justo para imputar consumo sin documento de compra.

---

## 4 · Caso B — Material que sobra y vuelve al almacén

Compraste/recibiste de más y el sobrante vuelve a la bodega. Hay **dos situaciones**:

### B.1 — El material nunca se llegó a usar (solo estaba en stock de la obra)

- **No lo imputás** y listo: queda como existencia, no como costo. La existencia se calcula sola: `existencias = lo comprado − lo imputado`. _(Manual, pp. 149/151)_
- El material físico que vuelve al almacén central **se registra como inventario en Syneco** (no en Presto).

### B.2 — El material YA se había imputado a una partida (y ahora vuelve)

- Hay que **restar el costo** que se cargó de más. Se hace con una imputación de **cantidad negativa** (parte de obra o entrega) sobre la **misma partida**.
- Eso descuenta el costo que había subido al árbol, dejando la partida con el costo real correcto.

!!! warning "Por qué importa hacer bien la devolución"
    Si imputaste material que después volvió a bodega y **no corregís**, esa partida queda con **costo inflado** — parece que gastó más de lo que de verdad usó. Y como Presto no te avisa, el error queda silencioso hasta que alguien cruza los números. La cantidad negativa es la forma de "deshacer" el costo de un sobrante ya imputado.

---

## 5 · Los 3 tipos de concepto (para entender el modelo)

Presto clasifica cada concepto por su **tipo de coste** (Manual p. 110). Te ayuda a ubicar dónde encaja el material de almacén:

| Tipo | Qué es | Ejemplo |
|---|---|---|
| **Suministro** | Lo que se **compra o subcontrata** (aporta costo por documentos de compra). | El material que comprás a un proveedor |
| **Destino** (centro de coste) | Donde se **ejecuta/consume** (la partida). Aporta costo por facturas y **partes de obra**. | La partida "rellenos" |
| **Indefinido** (por defecto) | Pasa a Suministro automáticamente si aparece en un documento de compra. | Un recurso recién creado |

El material del almacén = un **suministro** que imputás a un **destino** (la partida) vía parte de obra.

!!! warning "No crees un Destino \"ALMACÉN\" intermedio dentro de la obra"
    Tentación común: hacer una partida-destino llamada "ALMACÉN" para que el material "entre ahí" y después "salga". **No lo hagas** salvo necesidad real. El Manual avisa (p. 147): _"la dificultad de imputar costes correctamente aumenta geométricamente con el número de destinos."_ Lo limpio es imputar **directo a la partida** donde se consume.

---

## 6 · Resumen para logística

```
ALMACÉN CENTRAL (vive en Syneco)
   │  el material ya es GASTO (se compró antes)
   ▼
Se manda a la obra y se consume
   │  Parte de obra: Destino (partida) + Fecha + Precio
   ▼
PRESTO registra el COSTE en la partida
   │
   ├─ Si sobra y nunca se usó  → no se imputa (vuelve a Syneco como stock)
   └─ Si sobra y ya se imputó  → cantidad negativa para restar el costo
```

---

## ⚠️ Pendiente honesto (no afirmar como cerrado)

!!! note "Dos consultas técnicas de RIB que faltan revisar"
    El Manual menciona dos documentos técnicos de RIB que **no están en nuestro repositorio**: _"Facturación centralizada"_ y _"SIE (Sistema de Información Económica)"_. Podrían describir un patrón "obra-almacén" más elaborado. Para una certeza del 100% antes de descartar definitivamente el modelado del almacén en Presto, conviene pedirlos a RIB / Aminfo. **Lo verificado hoy alcanza para operar**: el almacén se queda en Syneco, Presto registra el costo al consumir.

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá lo aprendido"
    Sobre **BLEND** _(con licencia de Facturación y Control)_:

    1. Simulá que llega material del almacén central: cargá un **Parte de obra** con un material, imputándolo directo a una partida (`Destino` + fecha + precio), **sin** orden de compra.
    2. Recalculá y verificá que el **`ImpReal`** de esa partida subió.
    3. Simulá una devolución: hacé una imputación de **cantidad negativa** del mismo material sobre la misma partida.
    4. Recalculá y comprobá que el costo de la partida **bajó** en consecuencia.

    **Cómo sabés que salió bien:** el costo de la partida sube con el parte de obra y baja con la cantidad negativa, sin tocar ninguna orden de compra.

---

📖 **Fuente oficial (RIB):** _Manual de Presto completo_ — pp. 55 (obras enlazadas), 110 (tipos de coste), 135–136 (documentos), 147–152 (gasto ≠ coste, destinos, partes de obra, existencias).
**Verificado contra:** la práctica de migración Syneco → Presto de Raizant.
