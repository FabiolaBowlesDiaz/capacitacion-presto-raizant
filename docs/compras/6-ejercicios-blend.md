# 6 · Ejercicios en BLEND

!!! abstract "Para qué sirven"
    Practicá el rol completo sobre la obra de prueba **BLEND**, en un entorno seguro donde no rompés nada real. Hacelos en orden: cada uno se apoya en el anterior.

!!! warning "Requisito"
    Estos ejercicios necesitan una licencia con el **módulo de Contratación** activo (los botones `Pedidos` y `Contratos` tienen que aparecer en `Ver ▸ Documentos`). Si todavía no lo tenés, leé las páginas igual — cuando se active, volvés acá a practicar.

---

## Ejercicio 1 — Tu primera Orden de Compra (camino A)

!!! example "Pedido manual"
    1. Abrí `Ver ▸ Documentos ▸ Pedidos` y creá una OC nueva (columna `Documento`, botón `…`).
    2. Ponele la fecha de hoy **bien verificada**.
    3. Asignale un proveedor de la tabla de Entidades.
    4. Cargale **2 materiales**; a uno ponele una **fracción** de la cantidad presupuestada.
    5. Sobrescribí el `Precio` de uno con un precio "real" inventado.
    6. Dejá la OC en **estado verde**.

    **✅ Salió bien si:** los materiales quedaron naranja 🟧, el total `BasePed` refleja tus cantidades y precios, y con el verde no podés editar la cantidad.

    👉 Repasá en [1 · Pedido manual](1-pedido-manual.md).

---

## Ejercicio 2 — Detectá el proveedor heredado (falla silenciosa)

!!! example "La trampa de FS-1"
    1. Creá una **segunda** OC justo después de la primera.
    2. **Antes de tocar nada**, mirá la columna `Entidad`: ¿qué proveedor tiene puesto?

    **✅ Salió bien si:** notaste que Presto **copió el proveedor de la OC anterior** solo. Cambialo a mano. Ahora ya sabés por qué hay que confirmar el proveedor en cada OC.

    👉 Repasá en [4 · Reglas de oro](4-reglas-de-oro.md) (FS-1).

---

## Ejercicio 3 — Cotizá y adjudicá (camino B)

!!! example "Contratos"
    1. Marcá **3 materiales** como suministro (naranja 🟧).
    2. `Rellenar grupos` → `Calcular recursos` → `Crear contratos`.
    3. Abrí `Contratos` y confirmá que aparece tu lote.
    4. Asociá **2 proveedores** y cargales precios distintos a mano.
    5. Compará `1: Importe` vs `2: Importe` y **adjudicá** al más barato.
    6. `Pasar a pedido`.

    **✅ Salió bien si:** tras adjudicar se llenaron `Proveedor` y `Cont`, `Pasar a pedido` dejó de estar gris, y en `Pedidos` aparecieron las OCs del proveedor ganador.

    👉 Repasá en [2 · Contratos: cotizar y adjudicar](2-contratos-cotizar.md).

---

## Ejercicio 4 — Del pedido a la obra (entrega parcial)

!!! example "Costo real sin factura"
    1. Tomá una OC y hacé `Pasar a entrega` **sobre un solo material** (entrega parcial).
    2. Verificá que ese suministro tiene la columna `Entrega` llena.
    3. Andá a `Entidades ▸ [Proveedores] Importes` y mirá el material **pendiente** de recibir.

    **✅ Salió bien si:** el material entregado ya muestra costo real en su partida (sin factura), y el no entregado aparece como pendiente.

    👉 Repasá en [3 · Del pedido a la obra](3-del-pedido-a-la-obra.md).

---

## Ejercicio 5 — Encontrá lo que Presto no te avisa

!!! example "Caza de fallas silenciosas"
    Probá a propósito:

    1. **Sobre-pedir:** en una OC, pedí más cantidad de la presupuestada de un material. ¿Te frenó Presto? _(No.)_
    2. **Estado verde:** ¿el verde te pidió alguna contraseña o aprobación de otra persona? _(No — solo bloqueó campos.)_

    **✅ Salió bien si:** comprobaste en vivo que Presto **acepta callado** ambas cosas. Eso es exactamente por qué el proceso de Raizant tiene que poner esos controles.

    👉 Repasá en [4 · Reglas de oro y fallas silenciosas](4-reglas-de-oro.md).

---

!!! tip "Cuando termines"
    Si pudiste hacer los 5 sin trabarte, ya manejás el rol Compras de punta a punta: comprar directo, cotizar y adjudicar, encadenar a la obra, y reconocer las trampas. Lo que sigue en el día a día es hacerlo sobre obras reales, con la disciplina de proceso que Presto no fuerza por vos.
