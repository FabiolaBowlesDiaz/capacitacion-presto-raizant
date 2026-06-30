# 2 · Imputar el consumo a la partida (`Destino`)

!!! abstract "Conclusión primero"
    Esta es **la tarea más importante de todo el rol.** Cuando un material sale de bodega hacia una partida, le ponés dos cosas: **`Destino`** (a qué partida se gastó) y **`Fecha`** (cuándo se usó). Recién con eso el costo **sube al árbol** y la obra "ve" el gasto. Si recibís material pero no lo imputás, la partida queda en **cero costo** y la obra parece más barata de lo que es. **Recibir ≠ imputar.**

!!! tip "Antes de arrancar, tené a mano el mapa"
    Si _"la columna Destino"_, _"desdoblar"_ o _"la pestaña Árbol"_ no los ubicás, abrí en otra pestaña **[🗺 La pantalla de Obra/Almacén](interfaz.md)**.

!!! warning "Requisito de licencia"
    Igual que toda la pantalla de Entregas: necesitás el módulo **Facturación y Control** en la licencia. Sin él, estos pasos no están disponibles.

!!! info "De dónde sale este contenido"
    Fuente principal: **documentación oficial de Presto (RIB)** — _Tutorial de Presto_ (p. 30, cálculo del coste a partir de suministros y destinos) y _Manual de Presto completo_ (pp. 147–152). Complemento: apunte **C07** (caso 6 y 9) + video **`FactCon_08_08_2025`** (minutos `[hh:mm]`).

---

## Antes de empezar: el prerrequisito que rompe a todos

!!! danger "Las partidas tienen que tener la propiedad `Destino` asignada — si no, no podés imputar"
    Para que una partida pueda recibir consumo, tiene que estar marcada con la propiedad **`Destino`** (= "centro de coste"). Eso se hace una sola vez al armar la obra (lo hace el rol Presupuestos/Planificación; las partidas quedan con un fondo azulado). **Si una partida no tiene esa propiedad, cuando vayas a imputar la sugerencia de `Destino` sale completamente en blanco** y no vas a poder ligar el costo. _(C07, FS-5, video `[01:40]`.)_

    👉 Si te pasa, no es error tuyo: avisá a quien armó la obra (Enrique) que esa partida no quedó marcada como `Destino`.

---

## El concepto en una frase

La columna **`Destino`** de cada suministro = **el código de la partida a la que se le carga ese gasto**. El propio Presto lo define: _"el código del destino o centro de coste al cual se va a imputar el consumo del suministro."_ Es **lo que liga el costo real a la partida**: sin `Destino` + fecha, el importe **no sube** al árbol como costo real. `[01:30]` `[02:00]`

---

## Tarea 1 — Sacar de bodega solo una parte (desdoblar)

**Qué es:** muchas veces no mandás a producción todo lo que recibiste de golpe. Recibiste 119 m³ de material y hoy salen 40 a una partida. Para eso se **desdobla** la línea: se parte en "lo que sale" y "lo que queda".

📖 **Fuente oficial:** Tutorial de Presto, p. 32 (acción `Desdoblar`).

**Dónde estás:** en la subventana **`Suministros`** (la franja de abajo), sobre la línea del material.

**Paso a paso** `[01:30]`:

1. En la columna **`Cantidad`** del material, hacé **clic derecho** → elegí **`Desdoblar`**.
2. Indicá cuánto **sale ahora** a producción (p. ej. `40`) → `Aceptar`.
3. **La señal de que salió bien:** la línea se parte en **dos**: una con `40` (lo que sale) y otra con `79` (el saldo). Las dos juntas siguen sumando los 119 originales. ✅

!!! note "El desdoblar siempre conserva el total"
    No importa cuántas veces partas una línea: las fracciones **siempre suman la cantidad original**. Es seguro hacerlo. `[01:30]`

!!! note "¿Salió todo de una? No hace falta desdoblar"
    Si todo el material recibido se va a una sola partida de una vez, te saltás este paso y vas directo a la Tarea 2 sobre la línea completa.

---

## Tarea 2 — Decir a qué partida se gastó (`Destino`)

**Qué es:** asignar la partida que recibe el gasto.

📖 **Fuente oficial:** Tutorial de Presto, p. 30 — el coste se calcula a partir de los suministros y **los destinos designados**.

**Dónde mirar:** la columna **`Destino`** de la subventana `Suministros` (hacia la derecha).

**Paso a paso** `[01:30]` `[01:40]`:

1. En la línea de lo que sale (p. ej. la de `40`), andá a la columna **`Destino`** y usá el **botón de sugerencia `…`**.
2. Presto lista **primero las partidas donde ese recurso está presupuestado** (por eso importa el prerrequisito de arriba). Elegí la partida correcta (p. ej. `rellenos`).
3. **La señal de que salió bien:** la columna `Destino` queda con el código de la partida, y al lado aparece su descripción. ✅

!!! warning "Si la sugerencia sale vacía"
    Es el síntoma del prerrequisito: esa partida **no tiene la propiedad `Destino`**. _"Es normal que aquí la sugerencia no te sugiera nada"_ cuando falta. Avisá a quien armó la obra. _(C07, FS-5, video `[01:40]`.)_

---

## Tarea 3 — Fechar la imputación (la fecha que decide el período)

**Qué es:** poner la fecha en que el material **salió a producción** — esta fecha decide en qué período cae el costo.

📖 **Fuente oficial:** Tutorial p. 30 + Manual pp. 148–151 (el coste se imputa en la fecha de utilización real / consumo).

**Dónde mirar:** la columna **`Fecha`** de la línea de suministro.

**Paso a paso** `[01:30]`:

1. En la línea que estás imputando, andá a la columna **`Fecha`** y escribí la fecha real de la salida (ej. `01/12/2025`).
2. **Esa fecha tiene que caer dentro de la fase de certificación actual** (el período de trabajo activo).

!!! danger "Falla silenciosa #2 — fecha fuera de fase = costo que no aparece y solo se ve gris"
    Si la fecha de imputación cae **fuera de la fase de certificación actual**, Presto **no calcula nada** por más que recalcules; el único síntoma es que la fecha se ve **gris**. _"Si las fechas de imputación quedan fuera de la fase de certificación actual, no va a haber ningún tipo de cálculo… uno va a notar fechas de imputación grises."_ Si ves gris, **moviste el costo a un período donde no cuenta**. _(C07, FS-2, video `[02:30]`.)_

---

## Tarea 4 — Verificar que el costo SUBIÓ al árbol

**Qué es:** comprobar que lo que imputaste de verdad llegó a la partida como costo real.

📖 **Fuente oficial:** Tutorial "Cómo se calculan los costes reales" (variables del árbol `ImpInput` / `ImpReal`).

**Dónde mirar:** la pestaña **`Árbol`** de la ventana de Facturación y Control.

**Paso a paso** `[02:00]`:

1. Andá a la pestaña **`Árbol`**.
2. Hacé **`Inicio ▸ Recalcular`** (o la tecla F5). _(No hace falta recalcular en cada paso; hacelo de vez en cuando, tras un lote de imputaciones.)_
3. Mirá la columna **`ImpReal`** de la partida: antes estaba en cero y ahora muestra el **costo real consolidado** de esa partida. Ejemplo del video: la partida de excavaciones muestra `585.056` = exactamente lo que se imputó ahí. ✅

!!! note "`ImpInput` vs `ImpReal` — por qué a veces difieren"
    - **`ImpInput`** = la **suma directa** de lo que imputaste (el costo real "auténtico", sin promedios).
    - **`ImpReal`** = el costo con **precio medio ponderado**, que Presto usa para las curvas de valor ganado (EVM).

    Solo difieren si **el mismo material se compró a precios distintos** en distintas entregas. Si todo se compró al mismo precio, los dos números son iguales. El costo real "se lee de Presto, no se recalcula a mano". `[02:00]`

---

## Casos especiales: mano de obra y subcontratos

La imputación funciona igual, pero el ritmo cambia:

- **Mano de obra:** no se imputa día a día, sino por **cierres** mensuales o quincenales (con el libro de asistencia consolidado). Desdoblás el total contratado por cierre y lo imputás con `Destino` + fecha de cierre. `[01:10]` `[01:40]`
- **Subcontrato:** la cantidad es el **global del contrato**; lo desdoblás por **avance** (p. ej. 0,8 y luego 0,2, alineado con la cantidad ejecutada), y cada fracción se imputa con `Destino` + fecha. `[01:20]` `[01:50]`

---

## 🎥 Mirá el video

| Tema | Minuto |
|---|---|
| Desdoblar para sacar a producción | `[01:30]` |
| Asignar `Destino` (partida) | `[01:30]`–`[01:40]` |
| Sugerencia de Destino vacía (prerrequisito) | `[01:40]` |
| Variante mano de obra (cierres) | `[01:10]`–`[01:40]` |
| Variante subcontrato (por avance) | `[01:20]`–`[01:50]` |
| Recalcular y ver `ImpReal` en el árbol | `[02:00]` |
| Fechas grises fuera de fase | `[02:30]` |

> Video fuente: `FactCon_08_08_2025.mp4`. _Complemento de la documentación oficial citada en cada tarea._

---

## ⚠️ Lo que Presto NO te avisa (resumen)

- **Si no imputás, la partida queda en cero costo** y nada te lo recuerda → la obra se ve más barata. _(toda esta página)_
- **Fecha fuera de fase = no calcula** y solo se ve gris. _(Tarea 3)_
- **Sugerencia de Destino vacía** = la partida no tiene la propiedad `Destino`. _(Tarea 2)_

👉 Todas, con cómo blindarte, en [5 · Reglas de oro y fallas silenciosas](5-reglas-de-oro.md).

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá lo aprendido"
    Partiendo de la entrega que cargaste en la [Tarea 1](1-recepcion-entrega.md), sobre **BLEND**:

    1. Tomá un material recibido con cantidad, p. ej. 100, y **desdoblalo**: sacá `30` a producción.
    2. A la línea de `30`, asignale un **`Destino`** (una partida que tenga la propiedad asignada).
    3. Ponele una **fecha** dentro del período de trabajo actual.
    4. Andá al **`Árbol`**, hacé **`Recalcular`** y buscá esa partida: su **`ImpReal`** tiene que mostrar el costo de esos 30.
    5. **Prueba de la falla silenciosa:** cambiá la fecha de imputación a un año distinto, recalculá, y mirá cómo el costo **desaparece** y la fecha queda **gris**. Después corregila.

    **Cómo sabés que salió bien:** con la fecha correcta, el `ImpReal` de la partida refleja tu imputación; con la fecha mala, se va a cero y se pone gris.

---

📖 **Fuentes oficiales (RIB):** _Tutorial de Presto_, p. 30 y 32 · _Manual de Presto completo_, pp. 147–152.
**Complementos internos:** apunte C07 — Facturación y Entregas (casos 6 y 9) · transcripción `FactCon_08_08_2025`.
