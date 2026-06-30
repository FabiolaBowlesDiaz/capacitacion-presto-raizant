# 7 · Ejercicios en BLEND

!!! abstract "Conclusión primero"
    Practicá el rol completo de punta a punta sobre la obra de prueba **BLEND**, en un entorno seguro. Los ejercicios van en el mismo orden que las tareas: armar el calendario → certificar → meter un adicional → leer la salud. Cada uno te dice **cómo saber que salió bien**.

!!! warning "Requisito de licencia"
    Estos ejercicios necesitan una licencia con los módulos **Gestión de Proyectos** y **Facturación y Control**. Si tu Presto no los tiene, podés leerlos para entender el flujo, pero los botones aparecerán en gris. _(Ver [La pantalla de Control de obra](interfaz.md).)_

!!! tip "Hacelos en orden y sin apuro"
    El control de obra encadena pasos: si te saltás "marcar la certificación actual", el resto no acumula. Seguí la secuencia y verificá cada señal de éxito antes de pasar al siguiente.

---

## Ejercicio 1 — Armar la línea temporal

**Objetivo:** crear el calendario de fases de la obra.

1. En `Ver ▸ Propiedades ▸ Tiempos`, fijá **`FEC Inicio Obra`** en el primer día de la obra.
2. Con `Procesos ▸ Crear fechas de certificación`, generá **12 meses**, día de certificación **30**, con la casilla `Añadir todos los días del mes` marcada.
3. Pasate al esquema **`Días`** y encontrá la primera fecha de certificación (la naranja).
4. Tomá una fecha que caiga en fin de semana y **movela** al viernes anterior (clic derecho → `Certificación` en el viernes; `No certificación` en el sábado).

✅ **Salió bien si:** la pestaña `Fechas` muestra el ícono "€" en los fines de mes y la fecha que moviste cambió de lugar.

---

## Ejercicio 2 — Certificar el avance de una partida

**Objetivo:** cargar avance y entender la "certificación actual".

1. Poné el Árbol en esquema **`Certificación | FASES`** e inmovilizá la columna `CanPres`.
2. Elegí una partida y certificá **100** en `1: CanCert` (fase 1). Verificá que `1: Cert` calcula el importe solo.
3. **Marcá la fase 1 como certificación actual** (clic derecho → `Certificación actual`). Comprobá que `CanCert` ahora muestra `100`.
4. Certificá una cantidad en la **fase 2 sin marcarla** como actual → confirmá que `CanCert` **sigue en 100** (no sumó).
5. Marcá la fase 2 como actual y mirá que `CanCert` salta al acumulado.

✅ **Salió bien si:** entendés en vivo que **el acumulado solo sube cuando movés la certificación actual**.

---

## Ejercicio 3 — Cerrar un saldo

**Objetivo:** usar el cuadre automático contra el presupuesto.

1. Elegí una partida con `CanPres` mayor a lo que ya certificaste (ej. presupuesto 119, certificado 100).
2. Parate en la celda `N: CanCert` de la fase donde cerrás → apretá el **botón de tres puntos `…`**.
3. Aceptá la sugerencia de cuadre.

✅ **Salió bien si:** Presto rellenó el saldo que faltaba (los 19) sin que sacaras la cuenta.

---

## Ejercicio 4 — Meter un adicional bien (y verlo en el presupuesto vivo)

**Objetivo:** registrar un cambio de obra sin romper la base.

1. En una partida, abrí `Mediciones` y creá la línea inicial (cantidad presupuestada, con `Espacio` asignado). Recalculá y verificá que aparece en **magenta**.
2. **Desdoblá** esa línea en dos y asigná cada parte a una fase distinta (`FaseCert` 1 y 2).
3. Agregá una línea de **adicional** con `EstadoPres = pendiente`. En `Presupuesto por estados`, mirá que `CanPres` **no cambia**.
4. Cambiá ese adicional a **`modificado`** (verde), recalculá, y comprobá que ahora **sí** suma a `CanPres`.

✅ **Salió bien si:** entendés que `pendiente` no suma y `modificado` sí, y que el adicional vive en una línea de medición, no en el árbol.

!!! danger "Probá el error a propósito (para reconocerlo)"
    Digitá 20 unidades extra **directo** en `N: CanCert` sobre una partida ya completa. Mirá cómo el importe se pone **rojo** (sobrecertificación). Después borralo y hacelo bien por línea de medición. Así reconocés el rojo cuando lo veas en una obra real.

---

## Ejercicio 5 — Emitir un estado de pago

**Objetivo:** generar el documento de cobro.

1. Con la certificación cargada y la fase actual marcada, andá a los Informes → grupo **Gestión de proyectos**.
2. Generá **`Certificación actual y a origen`** (o `Certificación anterior, actual y acumulado al origen`).
3. Revisá el desglose: presupuestado, certificación anterior, certificación actual, acumulado al origen.

✅ **Salió bien si:** el informe muestra el avance acumulado hasta tu fase actual, partida por partida.

---

## Ejercicio 6 — Leer la salud de obra (EVM)

**Objetivo:** interpretar los índices de un vistazo.

1. Abrí la pestaña `Fechas`, esquema **`[Fases] EVM Valor ganado`**. Apretá **`Recalcular`**.
2. En la **última fila con datos**, anotá **`EvmCpi`**, **`EvmSpi`** y **`Avance`**. ¿La obra va con ahorro o sobrecosto? ¿Adelantada o atrasada?
3. Mirá los **colores**: ¿el CPI/SPI están en verde o en rojo?
4. Pasate al Árbol, esquema `Control de costes | FASES`, y compará **`ImpInput`** con **`ImpReal`**. ¿Son iguales o difieren? ¿Qué te dice eso?
5. Exportá la tabla del EVM a Excel y graficá las tres curvas **PV / EV / AC**.

✅ **Salió bien si:** sabés leer en la última fila si la obra va sana, y podés explicar la diferencia entre `ImpInput` y `OrReal`.

---

## Ejercicio integrador — un cierre de mes completo

**Objetivo:** simular el cierre real de una fase de punta a punta. Recorré el [checklist de cierre](5-reglas-de-oro.md#checklist-de-cierre-de-fase-para-imprimir):

1. Cargá el avance de 3 partidas (por cantidad).
2. Marcá la fase como certificación actual y verificá que `CanCert` se actualizó.
3. Meté un adicional por línea de medición, con su `EstadoPres` y `FaseCert`.
4. Recalculá. Confirmá que no hay fechas de imputación grises en el EVM.
5. Leé el CPI/SPI de la última fila y generá el estado de pago.

✅ **Salió bien si:** completaste el ciclo sin que ningún acumulado quede "congelado" por un paso olvidado.

---

📖 **Fuentes oficiales (RIB):** _Certificación y seguimiento_ · _Órdenes de cambio_ · _El valor ganado explicado en 4 páginas_ · _Cómo se calculan los costes reales_. **Complementos internos:** apuntes C08 y C09 · transcripciones de los videos de capacitación.
