# 4 · Del pedido a la factura

!!! abstract "Conclusión primero"
    El material que pediste (Orden de Compra del rol Compras) **se encadena solo** con tu entrega y, después, con la factura — sin teclear todo de nuevo. Con **`Pasar a entrega`** convertís un pedido en una recepción (heredando el precio de la OC), y con **`Pasar a factura`** convertís la entrega en una factura cuando llega la del proveedor. Y para saber **cuánto material falta por recibir**, hay tres lugares donde mirarlo. **Ojo:** Presto **no te obliga** a encadenar ni te frena si recibís de más — esa disciplina la pone el proceso de Raizant.

!!! tip "Antes de arrancar, tené a mano el mapa"
    Si _"la cabecera"_, _"el menú de clic derecho"_ o las columnas `BasePed`/`BaseEnt`/`BaseFac` no las ubicás, abrí en otra pestaña **[🗺 La pantalla de Obra/Almacén](interfaz.md)**.

!!! warning "Requisito de licencia"
    Necesitás el módulo **Facturación y Control** (y, para los pedidos/OC, el módulo **Contratación** — eso es del rol Compras). Sin ellos estos botones aparecen en gris.

!!! info "De dónde sale este contenido"
    Fuente principal: **documentación oficial de Presto (RIB)** — _Tutorial de Presto_, pp. 24–32 (ciclo OC → entrega → factura) y _Manual de Presto completo_. Complemento: apuntes **C06** (compras) y **C07** (entregas, casos 10–11) + videos `Contratacion_30_12_2025` y `FactCon_08_08_2025`.

---

## 1 · El ciclo completo y dónde estás vos

```
Pedido (OC)  →  Entrega (recepción)  →  Factura
   Compras         VOS (almacén)          Administración
```

Cada material es un **suministro** (una línea) que arrastra en sus columnas de qué **Pedido** vino, en qué **Entrega** llegó y en qué **Factura** se pagó. Por eso el ciclo se encadena a nivel de **línea**, no de documento entero — y por eso se pueden manejar entregas y facturas parciales sin enredarse. _(Tutorial, p. 29.)_

---

## 2 · `Pasar a entrega` — convertir un pedido en una recepción

**Qué es:** en vez de teclear la entrega desde cero, partís del pedido (OC) que ya hizo Compras y lo convertís en entrega. El precio y los materiales se **heredan de la OC**.

📖 **Fuente oficial:** Tutorial de Presto, p. 30.

**Dos formas, según cuánto llegó:**

| Situación | Qué hacés | Resultado |
|---|---|---|
| **Llegó TODO el pedido** | Clic derecho sobre el **pedido entero** → `Pasar a entrega` | Crea la entrega con todos sus materiales y el precio de la OC |
| **Llegó SOLO una parte** | Clic derecho sobre **UN suministro suelto** del pedido → `Pasar a entrega` | Crea una entrega parcial, solo con ese material; el resto queda pendiente |

!!! note "Por qué conviene `Pasar a entrega` desde la OC (recomendación Raizant)"
    Si hacés la entrega **desde el pedido** (en vez de a mano), el **precio viene automático de la OC** — es más rápido, más trazable, y el costo real queda disponible el mismo día de la recepción sin tener que buscar el precio. La entrega manual (tecleando todo) queda para cuando no hubo OC detrás (ej. material de almacén, ver [Tarea 3](3-almacen-y-sobrantes.md)).

!!! note "La entrega ya es costo, sin esperar la factura"
    Recordá lo de [Fundamentos](0-fundamentos.md): apenas la entrega tiene `Destino` + fecha, **el costo real ya subió a la partida** con el precio del albarán. La factura solo lo confirma o corrige después. No esperes la factura para tener el costo real.

---

## 3 · `Pasar a factura` — cuando llega la factura del proveedor

**Qué es:** convertir la entrega en una factura de proveedor cuando llega la factura real. Lo hace normalmente **Administración / cuentas por pagar**, pero conviene que lo conozcas porque nace de tu entrega.

📖 **Fuente oficial:** Manual de Presto, pp. 135–139 + C07 caso 10.

**Paso a paso** `[02:40]`:

1. En la cabecera `Entregas`, clic derecho sobre la celda **`Documento`** de la entrega → **`Pasar a factura`**.
2. Presto pide el **folio/código de la factura** del proveedor → tecladlo → `Aceptar`.
3. **Resultado:** se crea el documento en `Ver → Facturas`; en cada línea de `Suministros` la columna `factura` muestra el folio; la base `BaseFac` se llena sola.
4. **Corregir el IVA** (Presto pone IVA de España por defecto): seleccionar la columna IVA → clic derecho → `Sugerir` → el IVA local (para Bolivia, parametrizar el IVA boliviano vigente).
5. **Corregir la fecha de la factura**: la `Fecha` de la factura es un campo **distinto** del de la entrega — Presto pone hoy; poné la del folio real.
6. **Asignar el vencimiento**: clic derecho sobre el documento → elegir plazo (contado, 30/45/60 días, etc.). La subventana `Vencimientos` calcula el importe y la fecha de pago.

!!! warning "Falla silenciosa — proveedor creado a mano genera un vencimiento \"contado\" fantasma"
    Si el proveedor se creó a mano sin sus datos de pago, al pasar a factura Presto añade un vencimiento "contado" por defecto que hay que **borrar y recrear** con el plazo real. Lo prolijo es cargar los proveedores antes con su divisa y condición de pago. _(C07, FS-6, video `[02:50]`.)_

---

## 4 · ¿Cuánto material falta por recibir? Tres lugares para verlo

Esta es la pregunta de oro de logística: "pedí 100, llegaron 50, ¿cuánto falta?". Presto lo muestra en **tres lugares**, cada uno con un ángulo distinto:

| Dónde | Qué te muestra |
|---|---|
| Ventana **`Entidades`** → esquema `[Proveedores] Importes` | Por proveedor: lo pedido vs entregado vs facturado vs **pendiente** |
| Ventana **`Insumos`** → esquema `[Suministros] Existencias y consumos` | Por material: cuánto está en documentos vs cuánto se consumió (el stock) |
| Informe **`07 Contratación → Desviaciones de cantidades`** | El reporte formal: previsto vs contratado vs pedido |

Además, cuando hacés un **segundo pedido** del mismo material, la ventana de sugerencia te muestra "lo presupuestado − lo que ya pediste" = lo que falta por pedir.

!!! danger "Falla silenciosa #3 — el aviso de \"OC incompleta\" NO es automático"
    Mientras digitás una entrega, la sugerencia automática del **saldo pendiente de recepción NO fue confiable** en el video. El dato **existe** en las tres ventanas de arriba, pero **el aviso proactivo** ("OC incompleta, faltan 50 kg") **es tejido propio de Raizant** — Presto **no frena ni avisa solo** cuando recibís de menos o de más. Tenés que mirarlo vos en esas ventanas. _(C07, FS-3, video `[01:20]`.)_

---

## 5 · Detectar entregas sin factura (control periódico)

**Qué es:** revisar qué entregas siguen **sin su factura** (huérfanas), para que Administración las persiga.

📖 **Fuente oficial:** C07 caso 11, video `[03:40]`.

**Paso a paso:**

1. Menú **`Ver → Suministros`** → esquema **`Entrega facturas compras en firme`** (oculta las partidas certificadas y deja solo entregas ↔ facturas).
2. La tabla relaciona cada suministro con su **entrega** y su **factura**, con cantidades, precios e importes.
3. Para encontrar las **sin factura**: pararse en la columna `factura`, **filtrar por vacío** → quedan a la vista solo los suministros **sin factura**. Es exportable a Excel.

---

## 6 · Lo que Presto NO obliga (importante para el rediseño de Raizant)

!!! warning "Presto no es un ERP: no fuerza la cadena OC ↔ Entrega ↔ Factura"
    El **modelo de datos existe** (las columnas `BasePed`, `BaseEnt`, `BaseFac` están ahí y se cruzan). Pero Presto **no obliga** a usarlo: podés registrar una entrega **sin OC** detrás, y podés no pasarla **nunca** a factura, sin que nada proteste. El **three-way match obligatorio** (que toda entrega tenga su OC y su factura) es **tejido in-house de Raizant**, no algo que Presto imponga solo. Por eso el proceso de la empresa tiene que poner las reglas: obligar el enlace, alertar entregas sin factura después de N días, y definir quién puede cerrar una entrega sin OC.

---

## 🎥 Mirá el video

| Tema | Minuto | Video |
|---|---|---|
| Pasar pedido a entrega (total y parcial) | `[~30:00]` | `Contratacion_30_12_2025` / Tutorial p.30 |
| Pasar entrega a factura + IVA + fecha | `[02:40]` | `FactCon_08_08_2025` |
| Asignar vencimiento | `[02:50]` | `FactCon_08_08_2025` |
| Tabla consolidada suministro↔entrega↔factura | `[03:40]` | `FactCon_08_08_2025` |
| Saldo pendiente no confiable | `[01:20]` | `FactCon_08_08_2025` |

> _El video es complemento: la referencia primaria es la documentación oficial citada en cada sección._

---

## ⚠️ Lo que Presto NO te avisa (resumen)

- **No te obliga a encadenar OC ↔ Entrega ↔ Factura** → entregas huérfanas si nadie controla. _(sección 6)_
- **El saldo "cuánto falta" no es un aviso automático** → mirálo vos en las ventanas. _(sección 4)_
- **Proveedor a mano genera vencimiento "contado" fantasma** → corregilo. _(sección 3)_

👉 Todas, con cómo blindarte, en [5 · Reglas de oro y fallas silenciosas](5-reglas-de-oro.md).

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá lo aprendido"
    Sobre **BLEND** _(con licencia de Contratación + Facturación y Control)_:

    1. Tomá un pedido (OC) existente y, sobre **un suministro suelto**, hacé `Pasar a entrega` → comprobá que se creó una entrega parcial con el precio heredado de la OC.
    2. Sobre esa entrega, hacé `Pasar a factura`, poné un folio inventado, corregí el IVA y la fecha.
    3. Andá a `Ver → Suministros`, filtrá la columna `factura` por vacío y mirá qué entregas quedaron sin factura.
    4. En `Entidades → [Proveedores] Importes`, buscá un proveedor y mirá su "pendiente".

    **Cómo sabés que salió bien:** la entrega parcial hereda el precio de la OC, la factura aparece con su folio en cada línea, y el filtro de "sin factura" te muestra las huérfanas.

---

📖 **Fuentes oficiales (RIB):** _Tutorial de Presto_, pp. 24–32 · _Manual de Presto completo_, pp. 135–139.
**Complementos internos:** apuntes C06 y C07 · transcripciones `Contratacion_30_12_2025` y `FactCon_08_08_2025`.
