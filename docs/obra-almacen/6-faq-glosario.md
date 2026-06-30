# 6 · Preguntas frecuentes y glosario

!!! abstract "Conclusión primero"
    Las dudas que aparecen siempre en este rol, respondidas corto, y el diccionario de la jerga (albarán, destino, imputación, parte de obra, las bases…). Si una palabra del manual no la entendés, está acá.

---

## Preguntas frecuentes

??? question "Recibí el material pero la partida sigue mostrando costo cero. ¿Por qué?"
    Porque **recibir no es imputar**. Cargar la entrega registra que el material llegó, pero el costo solo sube a la partida cuando lo **imputás** con `Destino` + fecha. Andá a la línea del suministro, ponele el `Destino` (la partida) y la fecha, recalculá, y el costo aparece. Ver [2 · Imputar el consumo](2-imputar-consumo.md).

??? question "Puse la fecha de imputación pero el costo no aparece y la fecha está gris. ¿Qué hago?"
    La fecha quedó **fuera de la fase de certificación actual**. Presto no calcula nada cuando eso pasa, y solo lo avisa con el color gris. Corregí la fecha a una que caiga dentro del período actual, o pedí que se mueva la fase. Ver [Regla de oro 2](5-reglas-de-oro.md).

??? question "¿Tengo que esperar la factura para que la obra tenga el costo real?"
    No. **La entrega ya es documento de costo.** Apenas la entrega tiene `Destino` + fecha, el costo real sube a la partida con el precio del albarán. La factura solo lo confirma o lo corrige después. Es el "y/o" del Tutorial: el costo se calcula de _"entregas **y/o** facturas"_.

??? question "Llegó material del almacén central, sin compra ni proveedor. ¿Cómo lo cargo?"
    Como **Parte de obra**, imputándolo directo a la partida (`Destino` + fecha + precio), sin orden de compra. Ese material ya era gasto (se compró antes); recién se vuelve costo de tu obra al consumirse. Ver [3 · Material del almacén central](3-almacen-y-sobrantes.md).

??? question "Sobró material y volvió a la bodega. ¿Cómo lo descuento?"
    Si **nunca se imputó**, no hacés nada: queda como existencia (y el movimiento físico va a Syneco). Si **ya se había imputado**, hacés una imputación de **cantidad negativa** sobre la misma partida para restar el costo. Ver [3 · Material del almacén central](3-almacen-y-sobrantes.md).

??? question "¿Presto me dice cuánto falta por recibir de una compra?"
    El dato **existe** en tres lugares (`Entidades → [Proveedores] Importes`, `Insumos → Existencias`, informe de desviaciones), pero el **aviso automático no es confiable** mientras digitás. Tenés que mirarlo vos en esas ventanas. Presto no te frena si recibís de más. Ver [4 · Del pedido a la factura](4-del-pedido-a-la-factura.md).

??? question "El precio que cargo en la entrega, ¿me cambia el presupuesto?"
    No. El precio real de compra vive **solo en la línea de la entrega** — no toca el presupuesto ni el objetivo de coste. Por eso podés registrar lo que de verdad costó (para medir el desvío) sin arruinar la línea base.

??? question "Al imputar, la sugerencia de Destino sale vacía. ¿Hice algo mal?"
    No es tu error: esa **partida no tiene la propiedad `Destino`** asignada (se hace al armar la obra). Avisá a quien la armó (Enrique) para que la marque. Sin esa propiedad, ninguna partida puede recibir consumo.

??? question "¿Por qué `ImpInput` e `ImpReal` muestran números distintos?"
    `ImpInput` es la **suma directa** de tus imputaciones (el costo "auténtico"). `ImpReal` usa **precio medio ponderado** para las curvas de valor ganado. Solo difieren si el mismo material se compró a **precios distintos** en distintas entregas. Si todo fue al mismo precio, son iguales.

??? question "¿Puedo registrar mano de obra y subcontratos por acá, o solo materiales?"
    Los tres. La Entrega sirve para materiales, **mano de obra** (cierres por quincena/mes) y **subcontratos** (por avance). El procedimiento es el mismo: elegís el recurso, ponés cantidad y precio, e imputás con `Destino` + fecha.

??? question "¿Qué pasa si no tengo el módulo de Facturación y Control en la licencia?"
    No podés operar este rol: la ventana `Entregas` ni se abre (los botones salen en gris). Podés estudiar el manual, pero para cargar entregas de verdad la licencia tiene que incluir el módulo de **Facturación y Control**. Es un requisito a confirmar al contratar/renovar.

---

## Glosario de la jerga

| Término | Qué significa en palabras simples |
|---|---|
| **Entrega / albarán** | El documento que registra que un material **llegó a la obra**. El "remito" de Presto. Puede ser parcial. |
| **Suministro** | Una **línea** de material dentro de una entrega. Se desdobla para fraccionar salidas y se imputa con `Destino` + fecha. |
| **Destino** | La **partida / centro de coste** a la que se le carga el gasto de un material. La columna que liga el costo a la partida. |
| **Imputación** | La acción de poner `Destino` + fecha a un material para que su costo **suba a la partida**. El corazón del rol. |
| **Parte de obra** | Documento que imputa consumo a una partida **sin** orden de compra ni factura. Se usa para material del almacén central. |
| **Desdoblar** | Partir una línea de material en dos (ej. 119 → 40 + 79) para registrar salidas parciales. Las dos siempre suman el total. |
| **Pedido (Orden de Compra)** | La compra, aguas arriba de la entrega. La hace el rol Compras. Presto la liga con `BasePed`. |
| **Factura (de proveedor)** | El documento de pago al proveedor. Nace de la entrega con `Pasar a factura`. La maneja Administración. |
| **Entidad** | Un **proveedor o subcontratista**. Tu agenda de quién te entrega material. |
| **Gasto** | La plata que salió al **comprar** el material (aunque esté sin usar en bodega). |
| **Coste** | La plata que de verdad le pesa a una **partida**, cuando el material se **consume**. |
| **`ImpInput`** | El costo real **auténtico**: suma directa de lo imputado, sin promedios. |
| **`ImpReal`** | El costo real con **precio medio ponderado**, que Presto usa para el valor ganado (EVM). |
| **`BasePed` / `BaseEnt` / `BaseDest` / `BaseFac`** | Las cuatro "bases" de la cabecera: lo **pedido** / **entregado** / **imputado a destino** / **facturado**. Tu tablero del albarán. |
| **Fase de certificación actual** | El período de trabajo activo. Las fechas de imputación tienen que caer adentro o el costo no calcula. |
| **Three-way match** | El cruce OC ↔ Entrega ↔ Factura. Presto tiene el modelo, pero no lo obliga: es disciplina del proceso. |
| **Ícono naranja 🟧** | Marca que un recurso **ya figura en una entrega**. Si no lo tiene, todavía no se recepcionó. |

---

## Para profundizar

- El concepto de gasto ≠ coste, en [0 · Fundamentos](0-fundamentos.md).
- El paso a paso de recibir, en [1 · Recibir material](1-recepcion-entrega.md).
- El paso a paso de imputar, en [2 · Imputar el consumo](2-imputar-consumo.md).
- Las trampas, en [5 · Reglas de oro y fallas silenciosas](5-reglas-de-oro.md).

---

📖 **Fuente:** _Manual de Presto completo_ y _Tutorial de Presto_ (RIB) · apuntes internos C06/C07 · transcripciones `FactCon_08_08_2025` y `Contratacion_30_12_2025`.
