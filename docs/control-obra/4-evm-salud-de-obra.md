# 4 · El EVM: leer la salud de la obra (valor ganado)

!!! abstract "Conclusión primero"
    Esta es la **pantalla más importante del control de obra**: en una sola tabla, Presto te dice si la obra va **sobrecostada o con ahorro** (índice **CPI**), si va **atrasada o adelantada** (índice **SPI**), **en cuánto va a terminar costando** (estimación **EAC**) y **qué % de obra llevás ganado** (% **Avance**). Lo mejor: Presto **ya calcula todo esto solo** — vos no hacés cuentas, solo aprendés a **abrir el esquema correcto y leerlo**. Vive en la pestaña **`Fechas`**, esquema **`[Fases] EVM Valor ganado`**.

!!! tip "Antes de arrancar, tené a mano el mapa"
    Las instrucciones usan palabras como _"la pestaña de arriba"_, _"el menú de esquemas"_, _"la última fila"_. Si algo no lo ubicás, abrí en otra pestaña **[🗺 La pantalla de Control de obra](interfaz.md)** — es el mapa de las pestañas `Fechas` y `Árbol` con cada columna explicada. Volvé a él cuando te pierdas.

!!! warning "Requisito de licencia — sin esto no hay números"
    El EVM se alimenta del **costo real** y de la **certificación**, que viven en los módulos **Facturación y Control** y **Gestión de Proyectos**. Si la licencia no los incluye, el esquema `[Fases] EVM Valor ganado` aparece **vacío o en gris**. Antes de operar este rol, **verificá que ambos módulos estén incluidos en la licencia** (es un requisito a confirmar al contratar/renovar).

!!! info "De dónde sale este contenido"
    Fuente principal: **documentación oficial de Presto (RIB)** — _El valor ganado explicado en 4 páginas_, _Valor ganado: el proyecto A-12_ y _Cómo se calculan los costes reales_ (las tres definen las fórmulas y los nombres de variable que vas a ver en pantalla). Se complementa con el apunte interno **C09 — EVM / Valor ganado** y la transcripción del video **`FactCon_08_08_2025`** (de ahí salen los minutos `[hh:mm]` y los nombres exactos de columna verificados sobre capturas con sus tooltips). Cada tarea cita su **documento oficial y página**. Si el documento oficial y el video chocan, **gana el documento oficial**.

---

## Antes de empezar: las 3 magnitudes que se cruzan

Todo el EVM nace de cruzar **tres números** a una misma fecha de corte. Si entendés estos tres, el resto es leer:

| Sigla | Nombre | Qué es, en criollo | Columna en Presto |
|---|---|---|---|
| **PV** | Valor planificado | Cuánto **habías planeado** haber producido a la fecha (la línea base) | `OrPlan` |
| **EV** | Valor ganado | Cuánto **vale lo que realmente hiciste**, medido al precio del plan | `OrRealObj` |
| **AC** | Costo real | Cuánto te **costó de verdad** lo que hiciste | `OrReal` |

> 📖 **Fuente oficial:** _El valor ganado explicado en 4 páginas_ (RIB), p. 2 — _"El valor ganado es el «Earned Value» (EV)… En Presto se llama «RealObj»… El coste real… lo llamamos «Actual Cost» (AC)… En Presto es «Real»."_ El presupuesto total (la referencia que no cambia) es el **BAC**, en Presto **`Obj`**.

!!! note "La idea clave del valor ganado, con un ejemplo"
    Tenés una zanja de 1.000 m y un tubo de 1.000 m. Excavaste 500 m de zanja (50%) e instalaste 400 m de tubo (40%). **No podés sumar 500 + 400** y decir "voy por 900 de 2.000". Lo que se hace es **multiplicar cada cantidad por su costo** para poder sumar peras con manzanas: así obtenés un **% de avance global real** (en el ejemplo oficial, 43,3%). Ese "importe realizado" es el **valor ganado**. _(📖 mismo documento, p. 1.)_

---

## Tarea 1 — Antes de mirar el EVM, confirmá que el dato esté completo

**Qué es:** una verificación rápida de que Presto tiene con qué calcular. **Un EVM verde sobre datos incompletos miente** — esta es la regla de oro del rol.

**Por qué importa (clave para Raizant):** el EVM es matemáticamente perfecto, pero solo vale si el dato base es confiable. Antes de creerle al CPI, revisá estos cuatro puntos:

| Revisá que… | Dónde | Si falta… |
|---|---|---|
| La **baseline (objetivo de coste) esté congelada** | módulo Planificación | el PV "flota" y el SPI/Avance mienten |
| La **cantidad real ejecutada** esté cargada | Árbol, columna `CanReal` | no hay valor ganado (EV = 0) |
| Los **consumos estén imputados** con su precio real | ventana `Entregas` | el costo real (AC) queda incompleto |
| La **fase de certificación actual** esté marcada e incluya las fechas de imputación | pestaña `Fechas` | los montos **no suman** y no hay cálculo |

!!! danger "Falla silenciosa #1 — las fechas de imputación grises"
    Si una fecha de imputación de un consumo queda **fuera** de la fase de certificación actual, ese monto **no entra al cálculo** y el EVM se ve "sano" justamente porque le falta costo. Presto te avisa de una sola forma: **pinta esa fecha de imputación en gris**. Antes de afirmar "la obra va bien", asegurate de que **no haya fechas grises**. _(C09 §0.6, video `[02:30]`.)_

---

## Tarea 2 — Abrir el esquema EVM

**Qué es:** llegar a la tabla donde Presto consolida toda la salud de obra.

📖 **Fuente oficial:** _Valor ganado: el proyecto A-12_ (RIB), p. 7 — _"Los valores… se pueden ver en la ventana de fechas, mediante las variables de la tabla «Agenda» acumuladas a origen."_

**Paso a paso** `[02:20]`:

1. Andá a la **cinta de arriba**, pestaña **`Ver`**, y activá el **botón `Fechas`** (queda hundido). O hacé clic directo en la **pestaña `Fechas`** de arriba si ya la tenés abierta.
2. Buscá el **menú desplegable de esquemas** (arriba, sobre la tabla — es el selector que dice qué "vista" de columnas estás viendo).
3. Desplegalo y elegí **`[Fases] EVM Valor ganado`**.
4. **La señal de que salió bien:** la tabla cambia y aparece una **fila por cada fase** (período), con columnas de nombres raros como `OrPlanPres`, `OrCert`, `EvmCpi`, `EvmSpi`, `Avance`. ✅

!!! note "¿Por qué una fila por fase?"
    Cada fila es un **período de la obra** (normalmente un mes). Leídas **hacia abajo**, las columnas van **acumulando** mes a mes — y así forman las **curvas** (las famosas "curvas S") de lo planificado, lo ganado y lo gastado. La **última fila con datos** es siempre tu **corte vigente**: la foto de hoy.

!!! tip "Existen DOS esquemas EVM — elegí según quién mira"
    - **`[Fases] EVM Valor ganado`** → la mirada del **constructor** (la que usás vos en Raizant). Acá el costo real (AC) es lo que de verdad gastaste.
    - **`[Fases] EVM Valor ganado DO`** → la mirada de la **Dirección de Obra / mandante**. Acá el "costo real" es la **certificación** (lo que se le abona al contratista). _(C09 §0.5.)_

    Para controlar **tu** obra, usá el primero. El segundo sirve cuando querés ver la obra con los ojos del cliente.

---

## Tarea 3 — Recalcular (el paso que todos olvidan)

**Qué es:** forzar a Presto a actualizar los números.

📖 **Fuente oficial:** el módulo no refresca en tiempo real; hay que recalcular tras cargar datos (C09, prerrequisito P-6; video `[02:00]`).

**Paso a paso:**

1. Andá a la **cinta de arriba**, pestaña **`Inicio`**, y hacé clic en **`Recalcular`** (también está el atajo en la barra de título).
2. Esperá unos segundos: los números de la tabla `Fechas` se ponen al día.

!!! warning "Si no recalculás, ves números viejos"
    Cargaste un consumo nuevo o moviste la certificación actual y **el EVM no cambió**. No es un error: Presto **no recalcula solo**. Acordate de apretar `Recalcular` cada vez que tocaste algo. _(C09 R-5.)_

---

## Tarea 4 — Leer la salud de la obra de un vistazo (la última fila)

**Qué es:** mirar las **cuatro columnas de índices** en la **última fila con datos** y saber, en 10 segundos, cómo va la obra.

**Dónde mirar:** la **última fila** que tenga números (la fase de certificación actual). Recorré estas cuatro columnas:

| Columna | Qué responde | Verde (sano) | Amarillo | Rojo (alerta) |
|---|---|---|---|---|
| **`EvmCpi`** (CPI) | ¿Gasto bien? | ≥ 0,95 | 0,85 – 0,95 | < 0,85 |
| **`EvmSpi`** (SPI) | ¿Voy a tiempo? | ≥ 0,95 | 0,85 – 0,95 | < 0,85 |
| **`EvmEacCpi`** (EAC) | ¿En cuánto termina? | ≤ BAC | — | > BAC × 1,10 |
| **`Avance`** | ¿Cuánto llevo ganado? | (es un %) | — | — |

!!! tip "Presto ya te pinta los índices"
    En la propia tabla, Presto colorea el `EvmCpi` y el `EvmSpi`: **verde** cuando van ≥ 1 (bien) y **rojo** cuando van < 1 (mal). Un golpe de vista a los colores ya te dice mucho antes de leer el número. _(C09 §4.1; en las capturas, `1,3434` sale verde y `0,8700` sale rojo.)_

### Los 4 índices, uno por uno

**CPI — ¿gasto eficiente?** (columna `EvmCpi`)
> Tooltip de Presto: _"Índice de desempeño del coste CPI, valor ganado (OrRealObj) dividido por coste real (OrReal)."_ → **CPI = EV / AC**.
> Por cada peso que gastaste, cuánto valor de obra ganaste. **CPI > 1 = ahorro** (lo hecho costó menos de lo esperado); **CPI < 1 = sobrecosto.** 📖 _(El valor ganado en 4 páginas, p. 2: "Si CPI es mayor que 1, hay ahorro.")_

**SPI — ¿voy a tiempo?** (columna `EvmSpi`)
> Tooltip: _"Índice de desempeño del cronograma SPI, valor ganado (RealObj) dividido por coste estimado a la fecha (Plan)."_ → **SPI = EV / PV**.
> Cuánto del trabajo que **planeaste** para hoy realmente ganaste. **SPI < 1 = atraso.** 📖 _(El valor ganado en 4 páginas, p. 3.)_

**EAC — ¿en cuánto va a terminar?** (columnas `EvmEac` y `EvmEacCpi`)
> Tooltips: `EvmEac` = _"Estimación a la conclusión"_; `EvmEacCpi` = _"…ajustada con CPI"_.
> La proyección de cuánto va a costar la obra **completa** si sigue el ritmo actual. La variante más usada es **EAC ajustado = BAC / CPI**: si venís con CPI < 1, te proyecta un costo final **mayor** que el presupuesto. Comparalo contra el BAC (tu objetivo de coste total). 📖 _(El valor ganado en 4 páginas, p. 3; A-12, p. 6.)_

**% Avance — ¿cuánto llevo ganado?** (columna `Avance`)
> Tooltip: _"Valor ganado (OrRealObj) dividido por objetivo (Obj)."_ → **Avance = EV / BAC**.
> El % de obra (en valor) efectivamente ganado a la fecha. **Compáralo con el % físico** (lo certificado): si hay una brecha grande (>10%), puede haber mala imputación o adicionales sin registrar.

!!! example "Leé el caso real del proyecto A-12 (lo trae la doc oficial)"
    Un proyecto militar real terminó con `CPI = 0,76` y `SPI = 0,72` — la obra costaba más y avanzaba más lento de lo planeado **desde casi el primer mes**. La estimación final (EAC) trepó de 3.981 a más de 5.200 M$. Nadie reaccionó a tiempo y el contrato se rescindió. La moraleja oficial: el EVM **avisa temprano**, pero alguien tiene que **leerlo y decidir**. 📖 _(Valor ganado: el proyecto A-12, pp. 6–9.)_

---

## Tarea 5 — Leer las curvas (las columnas hacia abajo)

**Qué es:** entender las columnas de **importes acumulados**, que leídas hacia abajo dibujan las curvas S.

**Dónde mirar:** las columnas de la izquierda y centro de la tabla. Estas son las que importan:

| Columna | Qué acumula | En el EVM es… |
|---|---|---|
| **`OrPlan`** | El importe **planificado** (objetivo periodificado) | **PV** (valor planificado) |
| **`OrRealObj`** | Cantidad real × precio del plan | **EV** (valor ganado) |
| **`OrReal`** | El costo real acumulado | **AC** (costo real) |
| **`OrCert`** | La certificación acumulada | producción cobrada |
| **`OrPlanPres`** | La producción planificada a precio de venta | curva de venta planificada |
| **`OrRealPres`** | La producción real a precio de venta | curva de venta real |

> 📖 **Fuente oficial:** los tooltips de cada columna empiezan con `Agenda.<nombre>` y declaran la fórmula. Ej.: `Agenda.OrRealObj` = _"Valor ganado, cantidad realmente ejecutada a coste estimado."_ El prefijo **`Or`** significa "acumulado por fase (a origen)". _(C09 §2.2, verificado sobre capturas con tooltip.)_

!!! note "El esquema NO inventa datos — todo viene del Árbol"
    El relator del video es tajante: _"Todos estos números vienen del árbol. No hay ningún otro origen desconocido."_ La pestaña `Fechas` solo **agrupa por fase** lo que ya vive en el Árbol y se consolida en el concepto raíz. Por eso, si un número del EVM te sorprende, podés **bajar al Árbol** y rastrear de qué partida sale. _(C09 §0.3, video `[02:20]`.)_

---

## Tarea 6 — Distinguir el costo real "auténtico" del "ponderado"

**Qué es:** entender por qué a veces el costo real del EVM **no coincide** con la suma de tus facturas — y cuál usar para conciliar con caja.

**Por qué importa:** hay **dos** costos reales en Presto y editar uno no toca el otro. Confundirlos genera descuadres "inexplicables" al conciliar.

| | Costo real **auténtico** | Costo real del **EVM (ponderado)** |
|---|---|---|
| Columna (en el Árbol) | **`ImpInput`** | `ImpReal` → en `Fechas` es **`OrReal`** |
| Qué es | **Suma aritmética directa** de todo lo imputado | **Precio medio ponderado** cuando un recurso se compró a precios distintos |
| Para qué sirve | **Conciliar con caja / contabilidad** | Las **curvas de desviación del EVM** |

> 📖 **Fuente oficial:** _Cómo se calculan los costes reales_ (RIB), p. 3, tabla de variables:
> - **`Real`** = _"Coste real basado en consumos reales y promedios"_ (ponderado).
> - **`ImpInput`** = _"Coste basado en suma directa de imputaciones"_.
>
> Y la regla del mismo documento: _"Los costes reales deben calcularse con el precio medio de las compras… El coste medio ponderado es robusto… estable."_

**Paso a paso para compararlos:**

1. Andá a la pestaña **`Árbol`**, menú de esquemas → **`Control de costes | FASES`**.
2. Ubicá las columnas **`ImpInput`** (auténtico) e **`ImpReal`** (ponderado), una al lado de la otra.
3. Si **difieren**, es porque compraste el **mismo material a precios distintos** y Presto promedió para el EVM. **No es un error.** _(C09 §0.4, video `[02:10]`.)_

!!! danger "Falla silenciosa #2 — conciliar caja contra el número equivocado"
    Si querés cuadrar el costo real contra las facturas pagadas, usá **`ImpInput`** (la suma directa), **no** `OrReal` (el ponderado). Quien concilia caja contra el ponderado ve descuadres que no entiende. Para las **curvas del EVM**, en cambio, Presto usa `OrReal` a propósito (es más estable). Cada uno tiene su uso — lo importante es **saber cuál estás mirando**. _(C09 FS-2.)_

---

## Tarea 7 — Exportar las curvas a Excel / Power BI

**Qué es:** sacar la tabla del EVM a Excel para graficar las curvas S y armar el tablero de la torre de control.

📖 **Fuente oficial:** _Valor ganado: el proyecto A-12_ (RIB), p. 8 — _"También se puede generar una gráfica… exportando directamente la tabla de fechas a Excel."_

**Paso a paso** `[02:20]`:

1. Con el esquema `[Fases] EVM Valor ganado` abierto, andá a la pestaña **`Inicio`** de la cinta y hacé clic en **`Exportar a Excel`**.
2. En Excel (o Power BI), graficá **por fase**: las tres curvas del EVM = **PV (`OrPlan`)**, **EV (`OrRealObj`)** y **AC (`OrReal`)**. Si querés, sumá `OrPlanPres` (venta planificada) y `OrCert` (certificación).
3. Esa misma exportación es la que alimenta el **dashboard de la torre de control** de Raizant: el tablero **lee** los CPI/SPI/EAC de Presto, **no los recalcula**.

!!! note "La pestaña `Fechas` tiene más esquemas hermanos"
    Además del EVM, el mismo desplegable trae **`Meses facturación`** (cobros, pagos y flujo de caja) y **`Fases planificación y certificación`** (curvas de venta y certificación). Salud de obra y caja conviven en la misma pestaña, en esquemas distintos. _(C09 caso 3.)_

---

## 🎥 Mirá el video

| Tema | Minuto |
|---|---|
| El Árbol consolida el costo real (`Input` / `ImpReal`) | `[02:00]` |
| Costo real ponderado vs auténtico; cantidades objetivo/real | `[02:10]` |
| La pestaña `Fechas` consolida el EVM (columna por columna) | `[02:20]` |
| Marca de certificación actual y fechas de imputación grises | `[02:30]` |
| Esquema `Meses facturación` (cobros/pagos/flujo de caja) | `[03:30]` |

> Video fuente: `FactCon_08_08_2025.mp4` (módulo Facturación y control). Relator de soporte de Presto. _El video es complemento: la referencia primaria es la documentación oficial citada en cada tarea._

---

## ⚠️ Lo que Presto NO te avisa (resumen)

- **Fechas de imputación grises** → costo que no suma y un EVM falsamente verde. _(Tarea 1)_
- **Si no recalculás**, ves números viejos sin error alguno. _(Tarea 3)_
- **El SPI tiende a 1 al final** aunque haya atraso real → no te quedes solo con el SPI, cruzalo con el avance físico del cronograma. _(C09 FS-5.)_
- **`OrReal` (ponderado) ≠ `ImpInput` (auténtico)** → no concilies caja contra el número equivocado. _(Tarea 6)_
- **Sin baseline congelada**, el PV flota y el SPI/Avance pierden sentido. _(Tarea 1)_

👉 Todas, con cómo blindarte, en [5 · Reglas de oro y fallas silenciosas](5-reglas-de-oro.md).

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá lo aprendido"
    Sobre la obra de prueba **BLEND** _(con una licencia que tenga Facturación y Control + Gestión de Proyectos)_:

    1. Abrí la pestaña `Fechas` y poné el esquema **`[Fases] EVM Valor ganado`**. Apretá **`Recalcular`**.
    2. En la **última fila con datos**, anotá los valores de **`EvmCpi`**, **`EvmSpi`** y **`Avance`**. ¿La obra va con ahorro o con sobrecosto? ¿Adelantada o atrasada?
    3. Mirá los **colores**: ¿el CPI/SPI están en verde o en rojo?
    4. Pasate a la pestaña `Árbol`, esquema `Control de costes | FASES`, y compará **`ImpInput`** con **`ImpReal`**. ¿Son iguales o difieren? Si difieren, ¿qué te dice eso?
    5. Exportá la tabla del EVM a Excel y graficá las tres curvas **PV / EV / AC**.

    **Cómo sabés que salió bien:** entendés, mirando la última fila, si la obra va sana; y sabés explicar la diferencia entre `ImpInput` y `OrReal`.

---

📖 **Fuentes oficiales (RIB):** _El valor ganado explicado en 4 páginas_ (pp. 1–4) · _Valor ganado: el proyecto A-12_ (pp. 6–9) · _Cómo se calculan los costes reales_ (p. 3). **Complementos internos:** apunte C09 — EVM / Valor ganado (glosario de columnas verificado por captura) · transcripción `FactCon_08_08_2025`.
