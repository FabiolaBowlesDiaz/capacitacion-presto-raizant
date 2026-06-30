# 5 · Preguntas frecuentes y glosario

## Preguntas frecuentes (FAQ)

??? question "No veo los botones `Pedidos` ni `Contratos` en el menú `Ver`. ¿Por qué?"
    Porque tu licencia **no tiene el módulo de Contratación**. En `Ver ▸ grupo Documentos`, sin ese módulo solo aparecen `Insumos` y `Vencimientos`. Cuando la licencia lo incluya, aparecen también `Pedidos`, `Contratos`, `Entregas` y `Facturas`.

??? question "¿Tengo que usar Contratos, o puedo comprar directo?"
    Podés comprar directo (camino A, [Pedido manual](1-pedido-manual.md)) sin pasar por Contratos. Presto **no te obliga** a cotizar. Usás Contratos (camino B) cuando querés comparar ofertas entre varios proveedores antes de decidir. Que se cotice sobre cierto monto es una regla del proceso de Raizant, no de Presto.

??? question "Si registro el precio real de compra, ¿se me cambia el presupuesto?"
    No. El precio de compra vive en una cadena aparte; **no toca** ni el precio del presupuesto ni el objetivo de coste. Por eso registrás siempre el precio real sin miedo — es lo que después te deja medir el desvío. _(Manual p. 138.)_

??? question "¿Qué significa que un material esté en naranja 🟧?"
    Que **ya figura en algún Pedido, Contrato, Entrega o Factura**. Sin naranja = todavía no lo pediste. Es tu semáforo rápido para ver qué falta comprar. _(Manual; C06 §6.)_

??? question "Marqué \"estado verde\" en una OC. ¿Eso es la aprobación de la compra?"
    No. El verde solo **protege los campos** (bloquea cantidad y precio para que no se editen por error) y es reversible. **No es una autorización.** Presto no tiene flujo de aprobación; eso vive en el proceso de Raizant. _(Manual p. 136.)_

??? question "Pedí 100, llegaron 50. ¿Presto me avisa que falta?"
    No te avisa solo. El dato del pendiente está en `Entidades ▸ [Proveedores] Importes` y en el informe de desviaciones, pero **no hay alerta automática**. Tenés que revisarlo. _(Tutorial p. 28–30.)_

??? question "El material llegó pero la factura todavía no. ¿La obra sabe cuánto costó?"
    Sí. Con la **entrega** (albarán) ya alcanza: el costo real sube a la partida con el precio de la entrega, sin esperar la factura. Cuando llegue la factura, Presto recalcula si el precio cambió. _(Tutorial p. 30; ver [Del pedido a la obra](3-del-pedido-a-la-obra.md).)_

??? question "¿Cómo cotizo un subcontrato (no un material)?"
    Igual que un material, pero el concepto debe estar marcado como **partida + suministro** (no hay "naturaleza subcontrato"). Lo asociás a una entidad subcontratista y podés licitar entre varios desde la ventana `Contratos`. _(Manual; C06 §0 / caso variante.)_

??? question "Adjudiqué un contrato pero `Pasar a pedido` está en gris. ¿Por qué?"
    `Pasar a pedido` se habilita **solo después de adjudicar** (cuando el campo `Proveedor` del contrato está lleno). Si está gris, todavía no adjudicaste. Es la única validación de secuencia fuerte del módulo. _(C06 R-5.)_

---

## Glosario — la jerga traducida

| Término | Qué significa |
|---|---|
| **Pedido / Orden de Compra (OC)** | El documento con el que le pedís materiales a un proveedor. Cabecera (documento + proveedor + fecha) + líneas de suministro. |
| **Contrato** | Un **lote de compra**: agrupa materiales parecidos para cotizar entre varios proveedores, comparar y adjudicar. No es un material; es un paquete. |
| **Suministro** | Cada **línea de detalle** de un documento (un material con su cantidad y precio). También es la **propiedad** que marca un concepto como "se compra" (ícono naranja). |
| **Entidad** | Un **proveedor o subcontratista**. Tu agenda de a quién le comprás. Vive en `Ver ▸ Entidades`. |
| **Adjudicar** | Elegir el proveedor ganador de un contrato. Llena el campo `Proveedor` y habilita generar las OCs. |
| **Pasar a pedido** | Convertir un contrato adjudicado en órdenes de compra reales, automáticamente (una por fase). |
| **Pasar a entrega** | Registrar que el material de una OC llegó a obra, generando el albarán/entrega. |
| **Objetivo de coste** | La línea base de cuánto debería costar un material (sale de la planificación). Contra esto se mide el desvío. |
| **Precio de compra** | Lo que de verdad te cobra el proveedor. No toca el presupuesto ni el objetivo. |
| **Solicitud de precios** | El archivo (Excel) que se le manda al proveedor para que complete sus precios, y se reimporta para comparar. |
| **Marca naranja 🟧** | Señal de que un concepto ya está pedido/contratado/entregado/facturado. |
| **Estado verde ("a firme")** | Protección de campos (bloquea cantidad/precio). **No es aprobación.** |
| **Three-way match** | El cruce OC ↔ Entrega ↔ Factura (que coincidan cantidad y precio). Presto lo modela pero **no lo obliga**; lo controla el proceso. |
| **`BasePed`** | La columna que muestra el **total** de un pedido. |
| **`OrgContrato`** | En una OC generada desde un contrato, indica de qué contrato salió (trazabilidad). |
| **Precio medio ponderado** | Cómo Presto calcula el costo real cuando comprás en varias tandas: suma importes ÷ cantidad total. |

---

!!! tip "¿Falta una pregunta o un término?"
    Esta página crece con las dudas reales del equipo durante la adopción. Si te trabaste con algo que no está acá, avisá para agregarlo (ver [Cómo mantener este sitio](../contribuir.md)).
