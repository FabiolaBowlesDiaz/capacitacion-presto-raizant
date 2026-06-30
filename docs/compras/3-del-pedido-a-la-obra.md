# 3 · Del pedido a la obra

!!! abstract "Conclusión primero"
    La orden de compra es solo el principio. Acá ves **qué pasa después**: cuando el material **llega a obra** se registra una **entrega** (albarán), y eso hace que el **costo real suba a la partida** — incluso si todavía no llegó la factura. Entender este encadenamiento es lo que conecta "comprar" con "saber cuánto va costando la obra de verdad".

!!! info "De dónde sale este contenido"
    Fuente principal: **documentación oficial RIB** — _Tutorial de Presto_ (pp. 29–32) y _Cómo se calculan los costes reales_ (RIB). Es el material que **cierra dudas** que los apuntes internos dejaban abiertas. Complemento: apuntes C06/C07.

!!! note "Alcance de esta página"
    El detalle fino de Entregas y Facturas pertenece a otro rol (Almacén/Recepción y Administración). Acá lo vemos **desde compras**: lo justo para entender cómo tu OC se transforma en costo real. No es el manual completo de recepción.

---

## El ciclo completo: OC → Entrega → Factura

```
   PEDIDO (OC)  ──▶  ENTREGA (albarán)  ──▶  FACTURA
   "lo pedí"         "llegó a obra"          "lo pagué"
                          │
                          ▼
                  el COSTO REAL sube
                     a la partida
```

📖 **Fuente oficial:** Tutorial de Presto, p. 29 — _"Presto dispone de documentos de tipo pedido y de tipo entrega o albarán. Su utilización es opcional, y su funcionamiento es similar al documento de tipo factura."_

!!! tip "La idea más importante de toda la página"
    El **costo real** de la obra no espera a la factura. La doc oficial lo dice claro:

    > _"El cálculo del coste se realiza a partir de los suministros anotados en documentos de coste (**entregas Y/O facturas**)…"_ 📖 _(Tutorial p. 30.)_

    Ese **"y/o"** significa: **la entrega, por sí sola, ya cuenta como costo.** No hace falta la factura para que la obra "sepa" que ese material costó plata.

---

## El eslabón que une todo: la LÍNEA de suministro

No se encadenan los documentos enteros, sino **cada línea de material**. Una línea de suministro lleva, en sus columnas, **de qué pedido vino, en qué entrega llegó y en qué factura se pagó**.

📖 **Fuente oficial:** Tutorial p. 30 / Manual p. 138 — _"Una línea de suministro puede mostrar el pedido, la entrega y la factura a la que pertenece… De esta forma, desde cada suministro se comprueban directamente los demás documentos a los que pertenece."_

Por eso los **casos parciales** (llega de a poco, se factura aparte) se manejan a nivel de línea, no de documento entero.

---

## Tarea 1 — Pasar el pedido a entrega (cuando llega el material)

**Qué es:** registrar que lo que pediste **llegó a obra**, generando la entrega a partir de la OC.

📖 **Fuente oficial:** Tutorial p. 30 — `Pasar a entrega`.

**Paso a paso:**

1. En la ventana `Pedidos`, hacé **clic derecho sobre el pedido** (o sobre **un suministro suelto**, si llegó solo una parte) → **`Pasar a entrega`**.
2. Presto crea la **entrega** con los materiales y **hereda el precio** de la OC. La columna `Entrega` de cada suministro queda apuntando al documento de entrega.

!!! tip "Recomendación para Raizant"
    Hacé `Pasar a entrega` **desde la OC** (no creando la entrega a mano). Así el precio viaja automático desde el pedido, queda trazable, y el **costo real está disponible el mismo día que recibís** el material.

---

## Caso A — El material llega SIN factura: ¿de dónde sale el costo?

Esto pasa todo el tiempo: el material ya está en obra, pero la factura del proveedor llega después. ¿La obra "sabe" cuánto costó? **Sí.**

📖 **Fuente oficial:** _Cómo se calculan los costes reales_ (RIB) + Tutorial p. 30.

- El costo sale del **precio que vive en la línea de la entrega** (heredado de la OC, o tecleado del albarán/remito si la entrega se cargó a mano).
- El costo real **sube a la partida** en cuanto el suministro tiene su **`Destino`** (la partida a la que se imputa) **+ la fecha**. Todo desde la entrega, sin factura.
- Es un costo **real pero provisional**: cuando llega la factura y hacés `Pasar a factura`, Presto **recalcula** si el precio facturado difiere del de la entrega.

!!! note "Cómo se calcula el costo real: precio medio ponderado"
    Si compraste el mismo material en varias tandas a precios distintos, Presto usa el **precio medio ponderado** (no el último, ni FIFO/LIFO): suma todos los importes y divide por la cantidad total. Es estable y mejora a medida que avanza la obra. 📖 _(Cómo se calculan los costes reales, RIB.)_

---

## Caso B — Llega en varias entregas, una sola factura

Soportado de fábrica. Ejemplo de la doc (Tutorial p. 30): de un pedido de 4 materiales, solo llega la arena → `Pasar a entrega` **sobre ese suministro** → se crea una entrega solo con arena; el resto queda pendiente para entregas futuras. Después, una sola factura puede recoger materiales de varias entregas.

📖 **Fuente oficial:** Manual p. 139 (ejemplo de pedido recibido en dos partes con `Desdoblar`).

---

## Caso C — ¿Dónde veo cuánto falta recibir?

Pediste 100, llegaron 50. Tres lugares para ver el pendiente:

| Dónde | Qué muestra |
|---|---|
| Ventana `Entidades` → esquema `[Proveedores] Importes` | pedido vs entregado vs facturado vs **pendiente**, por proveedor |
| Ventana `Insumos` → esquema de existencias | por material: en documentos vs consumido |
| Informe `07 Contratación → Desviaciones de cantidades` | reporte formal previsto/contratado/pedido |

📖 **Fuente oficial:** Tutorial pp. 28–30.

!!! danger "Falla silenciosa: Presto NO te frena si recibís de menos"
    El dato del pendiente **existe** en esas ventanas, pero Presto **no te avisa solo** cuando una OC quedó incompleta ("faltan 50 kg"). No frena nada. La **alerta proactiva** de recepción incompleta es trabajo del proceso/tejido propio de Raizant, no de Presto. _(C07 FS-3.)_

---

## Lo que Presto NO obliga (y Raizant tiene que cuidar)

📖 **Fuente oficial:** Tutorial p. 29 (uso "opcional") + Manual p. 139.

- **No obliga la cadena** OC → Entrega → Factura. Podés registrar una entrega sin pedido detrás, o un pedido que nunca se reciba. Presto no protesta.
- **No valida el "three-way match"** (que la OC, la entrega y la factura coincidan en cantidad y precio). Cerrar ese cruce es trabajo del tejido propio.

!!! warning "La regla para Raizant"
    Que cada compra recorra **pedido → entrega → factura** y que las tres coincidan **es disciplina del proceso**, no algo que Presto fuerce. El sistema da los datos; el control lo pone el equipo.

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá lo aprendido"
    _(Con licencia que tenga Contratación.)_

    1. Tomá una OC que hayas creado y hacé `Pasar a entrega` **sobre un solo material** (entrega parcial).
    2. Verificá que en ese suministro la columna `Entrega` quedó llena, pero el resto de los materiales siguen pendientes.
    3. Andá a `Entidades → [Proveedores] Importes` y mirá cómo aparece el material **pendiente** de recibir.

    **Cómo sabés que salió bien:** el material entregado muestra su documento de entrega y el costo real ya figura en su partida; el no entregado aparece como pendiente.

---

📖 **Fuentes oficiales (RIB):** _Tutorial de Presto_, pp. 29–32. · _Cómo se calculan los costes reales_. · _Manual de Presto completo_, pp. 138–139. · Complemento: apuntes C06 / C07.
