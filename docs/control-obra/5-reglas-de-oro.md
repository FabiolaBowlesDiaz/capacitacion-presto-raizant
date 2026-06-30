# 5 · Reglas de oro y fallas silenciosas

!!! abstract "Conclusión primero"
    Presto es honesto con los números que calcula, pero **no te avisa cuando el dato que entró está mal**. Casi todos los problemas del control de obra son **silenciosos**: no hay error rojo ni alerta, simplemente el número queda mal y vos lo reportás como bueno. Esta página junta **todas** las trampas del rol — las de certificación (C08) y las del EVM (C09) — con cómo blindarte de cada una. Leela antes de presentar cualquier número a dirección.

!!! tip "Cómo usar esta página"
    No hace falta memorizarla. Tenela a mano como **checklist de cierre**: antes de decir "la obra va al X%" o "el CPI está en Y", recorré las reglas que apliquen y confirmá que ningún dato está roto.

---

## Las 3 reglas de oro del rol

!!! danger "Regla de oro #1 — Marcá la certificación actual en CADA cierre"
    Presto **solo acumula** hasta la fase marcada como **certificación actual** (naranja). Si te olvidás de moverla, los datos que cargaste **no suman** y el avance reportado queda subvaluado **sin ningún aviso**. Es el olvido más frecuente y más caro. **Cada cierre de fase: cargá el avance Y movele la certificación actual.**

!!! danger "Regla de oro #2 — Los adicionales SIEMPRE por línea de medición"
    Un cambio de obra (más cantidad, partida nueva) **nunca** se digita directo en el árbol. Va por una **línea de medición** en la subventana `Mediciones`, con su `EstadoPres` (`modificado`/`pendiente`) y su `FaseCert`. Digitado directo, Presto lo lee como **sobrecertificación** (rojo), no como cambio de alcance.

!!! danger "Regla de oro #3 — Un indicador sobre datos rotos miente"
    El EVM (CPI/SPI/EAC) es matemáticamente perfecto, pero **solo vale si el dato base es confiable**. Antes de creerle a un CPI verde, verificá las 4 compuertas: baseline congelada, cantidad real cargada, consumos imputados, y certificación actual con sus fechas de imputación dentro. **Un CPI verde sobre costo incompleto es la trampa central del rol.**

---

## Fallas silenciosas de la CERTIFICACIÓN (C08)

| # | Falla silenciosa | Qué pasa | Cómo blindarte |
|---|---|---|---|
| **FS-1** | **Olvidar marcar "certificación actual"** | Presto deja digitar pero **no acumula** en `CanCert`/`ImpCert`, sin error | En cada cierre, después de cargar, clic derecho → `Certificación actual` en la fase. Verificá que `CanCert` cambió. |
| **FS-2** | **Adicional digitado directo en el árbol** | El importe se pone **rojo** = sobrecertificación; Presto no lo entiende como cambio | Meter todo adicional por línea de medición con `EstadoPres`. |
| **FS-3** | **Las fases no se mueven solas** | Presto **nunca** avanza la certificación actual según el reloj de Windows | La gestión de la fase es 100% manual; ponelo en tu rutina de cierre. |
| **FS-4** | **Fechas auto-generadas en día no laborable** | `Crear fechas de certificación` marca el "31" aunque sea sábado | Revisá el calendario y movè a mano las que caen mal (clic derecho). |
| **FS-5** | **Calendario corto** | Si la obra dura más que los meses definidos, faltan fases | Proyectá de más; la herramienta se puede re-ejecutar con más meses. |
| **FS-6** | **Columna `Espacio` en blanco** | La línea de medición puede no computar bien | Asigná siempre un espacio (genérico si no hay uno específico). |
| **FS-7** | **Adicional sin `FaseCert`** | La línea de adicional no se certifica en ninguna fase | Tras crear el adicional, confirmá que tiene su fase asignada. |
| **FS-8** | **Confundir avance certificable con físico/costo real** | Mezclar los tres avances distorsiona la lectura | Tené claro: este módulo es **certificación (cobro)**; el físico y el costo van por Obra/Almacén. |
| **FS-9** | **El dato llega en % en vez de cantidad** | Cargar un % rompe la lógica (la columna es `CanCert`, cantidad) | Pedí siempre el dato en **cantidad original**, no convertido. |
| **FS-10** | **Adicional `pendiente` que nadie aprueba** | No suma al presupuesto ni al estado de pago; corre como costo de Raizant | Hacé seguimiento de los pendientes hasta que se aprueben o rechacen. |

---

## Fallas silenciosas del EVM / valor ganado (C09)

| # | Falla silenciosa | Qué pasa | Cómo blindarte |
|---|---|---|---|
| **FS-1** | **Fechas de imputación grises** | Si la fecha de un consumo cae fuera de la fase actual, el monto **no suma** y el EVM se ve "sano" porque le falta costo | Antes de leer el EVM, revisá que **no haya fechas de imputación grises**; la fase actual debe incluir todas las imputaciones del período. |
| **FS-2** | **Confundir `OrReal` (ponderado) con `ImpInput` (auténtico)** | Conciliar caja contra el ponderado da descuadres inexplicables | Para conciliación financiera usá **`ImpInput`** (suma directa); para curvas EVM, `OrReal`. Rotulá siempre cuál mostrás. |
| **FS-3** | **EVM verde sobre costo real incompleto** | Consumos sin imputar, lag de carga, precio en 0 → un CPI verde que miente | La capa de confiabilidad de la torre degrada a "dato no confiable" cualquier índice cuya base no pase las compuertas de calidad. |
| **FS-4** | **Sin baseline congelada** | Si el objetivo de coste cambió o nunca se congeló, el PV "flota" y SPI/Avance pierden sentido | Congelá/versioná el objetivo de coste aprobado **antes** de la ejecución. |
| **FS-5** | **El SPI tiende a 1 al final aunque haya atraso** | Limitación conocida del SPI clásico (al final, EV→BAC y PV→BAC) | No te quedes solo con el SPI: cruzalo con el **avance físico vs cronograma** (Gantt) y los hitos en riesgo. |
| **FS-6** | **Brecha físico vs económico no visible en una columna** | El esquema da `Avance` (económico) pero el % físico vive en certificación | La torre calcula `%físico − %económico` y alerta si la brecha supera el 10% (posible mala imputación o adicionales). |

---

## El principio que une todo

> **Un indicador EVM sobre datos rotos miente.** El motor de Presto es correcto; su validez depende **enteramente** de que el dato base (costo real imputado a tiempo, baseline congelada, certificación marcada) sea confiable.

Por eso, en el nuevo enfoque de Raizant:

- **Presto calcula** los indicadores (CPI, SPI, EAC, % Avance) — no hay que programar el motor.
- **La torre de control pone la capa de confiabilidad**: detecta el dato roto (fechas grises, consumos sin imputar, baseline sin congelar) y **degrada a gris** el indicador que no es de fiar, en vez de mostrarlo verde.
- **La alarma temprana es lo nuestro**: avisar cuando un número se sale de rumbo, antes de que el desvío sea irreversible — como en el caso A-12, donde el EVM avisó desde el mes 2 pero nadie reaccionó.

---

## Checklist de cierre de fase (para imprimir)

Antes de reportar el avance del mes, confirmá:

- [ ] Cargué el avance de todas las partidas de la fase (por cantidad, no %).
- [ ] **Marqué la fase como certificación actual** y `CanCert` se actualizó.
- [ ] Los adicionales del mes entraron por línea de medición, con `EstadoPres` y `FaseCert`.
- [ ] Revisé que no haya adicionales `pendiente` olvidados.
- [ ] En el EVM, **no hay fechas de imputación grises**.
- [ ] La baseline (objetivo de coste) sigue congelada.
- [ ] Recalculé (`Inicio ▸ Recalcular`) antes de leer cualquier número.
- [ ] Si concilio con caja, uso `ImpInput`, no `OrReal`.

---

📖 **Fuentes oficiales (RIB):** _Certificación y seguimiento_ · _Órdenes de cambio_ · _El valor ganado explicado en 4 páginas_ · _Cómo se calculan los costes reales_. **Complementos internos:** apuntes C08 (§3 fallas silenciosas) y C09 (§7 fallas silenciosas) · transcripciones de los videos de capacitación.
