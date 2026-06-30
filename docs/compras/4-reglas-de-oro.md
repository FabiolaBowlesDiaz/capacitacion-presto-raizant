# 4 · Reglas de oro y fallas silenciosas

!!! abstract "Conclusión primero"
    Esta página es la más importante del rol. Reúne **lo que Presto NO te avisa** cuando comprás — los errores que el sistema acepta callado y que después salen caros. Leela antes de emitir tu primera orden de compra, y volvé cada vez que dudes. Cada falla viene con **cómo blindarte**.

!!! info "De dónde sale"
    Las fallas están verificadas en la **documentación oficial RIB** (lo que Presto sí controla y lo que no) y en el apunte interno C06 §4, que las registró durante la capacitación. El "blindaje" es la práctica recomendada para Raizant.

---

## Las 3 reglas de oro de las compras

!!! danger "Regla 1 — Cotizar y aprobar es disciplina del proceso, NO de Presto"
    Presto **te deja comprar directo, sin cotizar ni que nadie apruebe.** No tiene flujo de aprobación ni roles de usuario. Que una compra grande **deba** cotizarse entre varios y aprobarse antes de emitir **lo pone el proceso de Raizant**, no el sistema. 📖 _(Manual p. 126, p. 135; C06 §0.3.)_

!!! danger "Regla 2 — El precio de compra NO toca el presupuesto ni el objetivo"
    Lo que pagás de verdad vive en una cadena de precio aparte. **Nunca** vas a "arruinar" el presupuesto por registrar el precio real — al contrario, es lo que te deja medir el desvío. Registralo siempre con el precio real. 📖 _(Manual p. 138; C06 §0.4.)_

!!! danger "Regla 3 — La cadena pedido → entrega → factura no se encadena sola"
    Presto **no obliga** a que cada compra recorra el ciclo completo ni a que las cantidades coincidan (three-way match). Esa coherencia la cuida el equipo. 📖 _(Tutorial p. 29; Manual p. 139.)_

---

## Fallas silenciosas (lo que Presto rompe sin avisar)

### ⚠️ FS-1 — Te copia el proveedor de la OC anterior

Al crear la **siguiente** orden de compra, Presto **arrastra el mismo proveedor** de la fila de arriba, automáticamente. Si no mirás, le comprás al equivocado.

**Cómo te blindás:** en **cada** OC nueva, confirmá el proveedor a mano antes de cargar materiales. _(video `[00:50]`.)_

---

### ⚠️ FS-2 — La fecha "de hoy" queda mal

Presto pone la fecha del calendario de Windows por defecto. Si no la corregís, la OC queda con fecha de emisión equivocada.

**Cómo te blindás:** verificá la fecha en cada OC; que coincida con la fecha real de la compra/aprobación.

---

### ⚠️ FS-3 — Te deja pedir más de lo presupuestado (sobre-pedido)

La sugerencia de "lo que falta pedir" (objetivo − ya pedido) es **solo una sugerencia, no un tope**. Presto acepta que pidas 5.000 de algo presupuestado en 3.780, sin avisar.

**Cómo te blindás:** mirá siempre el número de "lo que falta" antes de confirmar la cantidad. A nivel proceso: una alerta in-house cuando el acumulado pedido de un material supere su objetivo.

---

### ⚠️ FS-4 — El "estado verde" parece aprobación, pero no lo es

El verde solo **protege los campos** contra edición accidental, y es **reversible** (cualquiera lo desbloquea con un clic derecho). No es la autorización del jefe.

**Cómo te blindás:** la aprobación de compras vive **fuera** de Presto (en el proceso de Raizant). No uses el verde como si fuera un permiso. _(Manual p. 136; C06 FS-6.)_

---

### ⚠️ FS-5 — Cotizar es opcional → compras a dedo

Se puede **saltar Contratos** por completo y comprar directo, sin comparar ofertas.

**Cómo te blindás:** regla de proceso — sobre cierto monto, la OC exige contrato/cotización con un mínimo de proveedores antes de emitir. _(Manual p. 126; C06 FS-4.)_

---

### ⚠️ FS-6 — Los pedidos generados se editan tras adjudicar

Después de adjudicar un contrato y pasarlo a pedido, podés **cambiarle el proveedor o la cantidad** a cualquier OC generada — y no queda rastro de que difiere de lo adjudicado.

**Cómo te blindás:** si cambiás algo post-adjudicación, documentalo aparte. A nivel proceso: alertar cuando el proveedor de una OC no coincide con el adjudicado en su contrato. _(C06 FS-9.)_

---

### ⚠️ FS-7 — Recibís de menos y Presto no te frena

Si pediste 100 y llegaron 50, Presto **no te avisa** que la OC quedó incompleta. El dato del pendiente existe en las ventanas, pero no hay alerta automática.

**Cómo te blindás:** revisá el pendiente en `Entidades → [Proveedores] Importes` o el informe de desviaciones. La alerta proactiva es tejido in-house. _(C07 FS-3.)_

---

### ⚠️ FS-8 — Sin roles ni auditoría

No hay usuarios ni permisos. El único control es **ocultar ventanas por computadora** (con una contraseña compartida), sin registro de quién hizo qué.

**Cómo te blindás:** la trazabilidad de actores (quién creó/editó/adjudicó) vive en la capa in-house. Asumir que Presto, solo, no resuelve esto. _(C06 FS-7.)_

---

### ⚠️ FS-9 — No hay importación nativa de OCs

Las órdenes de compra se **teclean a mano**; no se importan desde otro sistema sin un desarrollo a medida. Riesgo de error de digitación.

**Cómo te blindás:** doble chequeo de las OCs grandes; a futuro, conector in-house que reduzca el tecleo. _(C06 FS-3.)_

---

## Tabla resumen

| # | Falla silenciosa | Tu blindaje |
|---|---|---|
| FS-1 | Copia el proveedor anterior | Confirmá proveedor en cada OC |
| FS-2 | Fecha "de hoy" mal | Verificá la fecha siempre |
| FS-3 | Deja sobre-pedir | Mirá "lo que falta" antes de confirmar |
| FS-4 | Verde ≠ aprobación | Aprobación fuera de Presto |
| FS-5 | Cotizar es opcional | Regla de monto que obligue cotizar |
| FS-6 | OCs editables tras adjudicar | Documentá cambios post-adjudicación |
| FS-7 | No avisa recepción incompleta | Revisá el pendiente; alerta in-house |
| FS-8 | Sin roles ni auditoría | Trazabilidad en capa propia |
| FS-9 | Sin import de OCs | Doble chequeo; conector a futuro |

---

!!! tip "El hilo común de todas las fallas"
    Casi todas dicen lo mismo: **Presto registra, pero no controla.** Donde esperarías que un sistema te frene (sobre-pedido, compra sin aprobar, recepción incompleta), Presto te deja seguir. Ese control es lo que Raizant construye como "tejido propio" alrededor de Presto. Conocer estas fallas es el primer paso para no caer en ellas.

---

📖 **Fuentes oficiales (RIB):** _Manual de Presto completo_, pp. 126, 135–139. · _Tutorial de Presto_, p. 29. · Complemento: apunte C06 §4 (fallas silenciosas verificadas en capacitación).
