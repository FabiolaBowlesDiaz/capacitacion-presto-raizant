# 2 · Objetivo de coste y curva S (planificación económica)

!!! abstract "Conclusión primero"
    Con el Gantt armado, tres procesos convierten el plan en **números por fase**: (1) **`Procesos ▸ Generar`** crea el **objetivo de coste** aplicando un **coeficiente de paso** sobre el presupuesto de adjudicación — esa es tu **línea base de coste**, el PV contra el que después el EVM mide la realidad; (2) **`Procesos ▸ Rellenar la planificación económica`** reparte cantidades y montos en las fases **según las barras del Gantt**; (3) **`Procesos ▸ Calcular recursos`** deriva el **calendario de necesidad de recursos** para Compras. El resultado son tres columnas acumuladas por fase (plan de coste, plan de venta, certificado) — la materia prima de la **curva S**. Ojo: **nada de esto se recalcula solo** si el Gantt cambia.

!!! warning "Prerrequisitos de esta página"
    1. El **diagrama de barras armado** — la planificación económica se reparte según las barras ([página anterior](1-armar-el-cronograma.md)).
    2. La **certificación actual en la primera fase** — si no, el flujo no arranca del día 1 (Tarea 2 de la [página anterior](1-armar-el-cronograma.md)).
    3. El **presupuesto de adjudicación con valores** (columnas de cantidad, precio e importe presupuestado llenas en el `Árbol`).

!!! info "De dónde sale este contenido"
    Fuente principal: transcripción del video **`Plan_10_12_2025`**, bloques `[02:30]`–`[03:30]`, estructurada en el apunte interno **C05** (casos 14–21). Los nombres de columna (`CanObj`, `Obj`, `ImpObj`, `CanPlan`, `Plan`, `PlanPrece`) se infieren del audio y los apuntes — **verificar los rótulos exactos en Presto** cuando haya licencia disponible.

---

## Las DOS estructuras de precio (no las confundas nunca)

Antes de tocar nada, el concepto que sostiene toda la página. En Presto coexisten **dos juegos de columnas de dinero** que se planifican en paralelo `[02:30]`–`[02:50]`:

| | **Presupuesto de adjudicación** | **Objetivo de coste** |
|---|---|---|
| Qué es | Lo que se **presenta al cliente** para adjudicar la obra: el precio de **venta** | Tu estimación de **coste propio** (con el margen ya descontado), contra la que se controla el costo real |
| Columnas en el `Árbol` | `CanPres` / `Pres` / `ImpPres` | `CanObj` / `Obj` / `ImpObj` |
| Periodificado como | `PlanPrece` (proyección de **estados de pago**) | `Plan` (línea base de coste = **PV** del EVM) |

> _"El objetivo de coste en el fondo representa eso, es tu línea base de la ejecución de la obra, pero ya después con el otro módulo [Facturación y control] irás viendo cómo te van saliendo los costos reales."_ `[02:40]`

!!! warning "Falla silenciosa — leer la curva equivocada"
    Tomar los montos de venta (`PlanPrece`) como si fueran la línea base de coste (`Plan`), o al revés, **falsea el margen y el EVM**. En todo reporte, rotulá explícitamente cada serie: objetivo de coste (PV) / venta (adjudicación) / certificado. _(C05 FS-8.)_

---

## Tarea 1 — Revisar el esquema `Objetivo de coste` (todo en cero, y está bien)

**Qué es:** conocer las columnas que vas a llenar, antes de llenarlas.

**Dónde estás:** pestaña **`Árbol`**.

**Paso a paso** `[02:30]`:

1. Abrí el menú de esquemas y elegí **`Objetivo de coste`**.
2. Vas a ver las columnas del presupuesto de adjudicación (`CanPres`, `Pres`, `ImpPres`) y, al lado, las del objetivo **en cero**: `CanObj` (cantidad objetivo — debería terminar igualita a `CanPres`), `Obj` (precio unitario objetivo) e `ImpObj` (importe objetivo = `CanObj × Obj`).
3. **No las llenes a mano.** Hay una herramienta que lo hace de un saque (Tarea 2): _"hay una herramienta que te permite aplicar un coeficiente de paso sobre los precios que ya existen en el presupuesto de adjudicación."_ `[02:30]`

---

## Tarea 2 — Generar el objetivo de coste (el coeficiente de paso)

**Qué es:** crear la línea base de coste aplicando un porcentaje sobre los precios de adjudicación. **La decisión del coeficiente es de quien controla el margen** (jefe de presupuestos / control de obra), no de quien dibuja barras.

**Paso a paso** `[02:30]`–`[02:40]`:

1. Quedate en la pestaña **`Árbol`**, esquema **`Objetivo de coste`**.
2. Andá al menú **`Procesos` → `Generar`**. Ojo con buscarlo en el lugar equivocado — el relator lo aclara: _"no está en el menú de herramientas, está en el menú procesos."_
3. En el diálogo, **arriba marcá `Generar objetivo`** — aparece también `Generar presupuesto`; **esa no**.
4. Verificá que esté **apuntando al concepto raíz**.
5. En el campo **"porcentaje a aplicar sobre los precios"**, ingresá el **coeficiente de paso por naturaleza**: mano de obra, maquinaria, materiales, naturaleza "otros" y partidas a precio alzado. En el video usa **`90`** en todas.
6. Hay un **recuadro que debe quedar DESMARCADO** — _"hay un recuadro que no se marca, no lo marquen, tiene que quedar desmarcado"_. El audio no dice cuál es su rótulo: **verificar en Presto** qué opción es antes de operar en serio.
7. Clic en **`Aceptar`** → las columnas objetivo se llenan solas: `CanObj = CanPres`, `Obj = Pres × coeficiente/100`, `ImpObj = CanObj × Obj`.

**Cómo leer el coeficiente:** `90` = objetivo de coste **10% menor** que la adjudicación (_"voy a generar un objetivo de coste 10% menor al presupuesto de adjudicación"_) · `100` = sin margen · cuanto más bajo, más margen estimado. `[02:30]`

!!! danger "Falla silenciosa — Presto NO congela la línea base"
    `Procesos ▸ Generar` **sobrescribe** el objetivo de coste cada vez que se corre, sin guardar la versión anterior ni avisar. Si alguien lo re-ejecuta con otro coeficiente a mitad de obra, tu línea base cambió y el EVM queda midiendo contra otra cosa. El **congelado de la baseline es nuestro** (regla de oro #3 del flujo): una vez aprobado el objetivo, se toma snapshot fuera de Presto y no se vuelve a generar. _(C05 FS-1.)_

---

## Tarea 3 — Rellenar la planificación económica (periodificar desde el Gantt)

**Qué es:** repartir las cantidades y los montos de cada partida entre las fases, **según cómo quedaron las barras** del diagrama.

**Paso a paso** `[02:40]`–`[02:50]`:

1. En la pestaña **`Árbol`**, cambiá al esquema **`Planificación fases`**: aparecen **columnas pareadas por cada fase** — `CanPlan` (cantidad planificada) y `Plan` (monto, calculado a precio del objetivo de coste).
2. Menú **`Procesos` → `Rellenar la planificación económica`**.
3. El diálogo ofrece **tres métodos**; dejá marcado el **primero (el predeterminado)**: **`Aplicando los datos del diagrama de barras`** — es el que usa el fabricante en la gran mayoría de los casos. Los otros dos no se muestran en el video: **verificar en Presto** cuáles son y cuándo aplican.
4. Clic en **`Aceptar`** → Presto **distribuye** cantidades y montos por fase: si una barra abarca varias fases, reparte proporcional. Si no ves el cambio, dale a `Recalcular`.
5. **Chequeo de sanidad:** la **suma horizontal** de `CanPlan` de cada partida sigue dando la cantidad presupuestada — con este método no se descuadra nunca.

**Ver también la proyección de venta:** el esquema tiene **dos menús arriba** que conmutan qué muestran las columnas de dinero. Desplegá el segundo (está en orden alfabético) y elegí **`plan prece`** → ahora las columnas muestran los montos a **precio de presupuesto de presentación** = tu **proyección de estados de pago** por fase. Si las columnas quedan desajustadas, botón **`Ajustar anchura`**. `[02:50]`

!!! warning "Falla silenciosa — el reparto manual descuadra"
    También se puede digitar `CanPlan` **a mano**, celda por celda (hay gente que lo hace desde una planilla externa). El riesgo: Presto va **recalculando la cantidad objetivo** con lo que escribís, y si la suma horizontal no vuelve a dar la cantidad presupuestada (los `752` del ejemplo del video), el plan queda descuadrado sin aviso. Preferí SIEMPRE la vía automática desde el Gantt. `[02:40]` _(C05 FS-7.)_

---

## Tarea 4 — Leer la curva S (plazo vs avance planificado)

**Qué es:** la vista consolidada por fase de las tres series de dinero — de acá sale la clásica curva S de la obra.

**Dónde estás:** pestaña **`Fechas`**.

**Paso a paso** `[03:00]`:

1. En la pestaña `Fechas`, elegí el esquema **`Fases planificación y certificación`**.
2. Leé las tres columnas consolidadas, que se **acumulan fase a fase** (_"acumulándose por fases, así que esto va incremental"_ — 6,6M → 33,9M → 36M…):

| Columna | Qué acumula | Para qué sirve |
|---|---|---|
| **`Plan`** | Montos del **objetivo de coste** por fase | La **línea base de coste (PV)**: cuánto deberías llevar gastado a cada fecha |
| **`PlanPrece`** | Montos del **presupuesto de presentación** por fase | La **proyección de estados de pago**: cuánto deberías llevar cobrado |
| **`Cert`** | Lo **certificado** real (viene de Control de obra) | El avance real para cobrar, contra las dos anteriores |

3. Para graficar: botón **`Exportar a Excel`** → _"por lo general… la llevan a Power BI"_ y ahí se dibujan las curvas. `[03:00]`

!!! note "Presto no la llama 'curva S'"
    El video **no usa el término "curva S"** ni dibuja el gráfico dentro de Presto: genera las tres series acumuladas y las exporta (el gráfico se hace afuera, típicamente Power BI). El monto acumulado en el tiempo tiene la clásica forma de S — arranca lento, acelera al medio, frena al final — y de ahí el nombre con que lo vas a escuchar en obra.

**Cómo alimenta esto al EVM:** la columna `Plan` acumulada es el **PV (valor planificado)** — la primera de las tres magnitudes del valor ganado. Cuando la obra arranque, Control de obra le cruza el **EV** (lo realmente producido a precio de plan) y el **AC** (el costo real), y de ahí salen CPI y SPI. Ese cruce no se hace en este módulo: se lee en **[Control de obra › 4 · El EVM: leer la salud de la obra](../control-obra/4-evm-salud-de-obra.md)**.

---

## Tarea 5 — Calcular los recursos por fase (el insumo de Compras)

**Qué es:** derivar de la planificación el **calendario de necesidad de recursos**: cuánta mano de obra, maquinaria y material se necesita en cada fase — para anticipar arriendos, compras y subcontratos.

**Paso a paso** `[03:00]`–`[03:10]`:

1. Pasate a la pestaña **`Conceptos`** → menú de esquemas → elegí **`Naturalezas básicas recursos`** (ojo: hay uno que dice `Naturalezas básicas` a secas — es el otro, el que termina en **recursos**).
2. En el menú de visualización de columnas múltiples, marcá **`CanPlan`** → aparece la zona de columnas pareadas por fase, **en gris/vacía**. Es normal: `Recalcular` **no** la llena.
3. Menú **`Procesos` → `Calcular recursos`** → en la ventana, clic en el botón **`Defecto`** (marca todas las opciones por defecto, lo recomendado) → **`Aceptar`**. Qué marca exactamente ese botón no se detalla en el audio: **verificar en Presto**.
4. Resultado: cada recurso muestra su **cantidad planificada distribuida por fase**. En archivos grandes el cálculo (y el export) puede tomar **varios minutos** — paciencia.
5. **`Exportar a Excel`** → esa tabla es la que se le entrega a Compras/Contratación: _"esto ya va a permitir el tema de la anticipación de la adquisición de los recursos… el arrendar la maquinaria, el comprar los materiales o hacer la contratación debida de la mano de obra."_ `[03:10]`

!!! danger "Falla silenciosa — nada de esto se actualiza solo cuando cambia el Gantt"
    _"Si el diagrama de barras por algún motivo cualquiera se modifica, los números calculados en el árbol no se actualizan en tiempo real."_ Y los recursos tampoco. La cadena es: **Gantt cambió → re-ejecutar `Rellenar la planificación económica` → re-ejecutar `Calcular recursos`**. `Recalcular` NO alcanza. Si te salteás un paso, el árbol, las curvas y el Excel de Compras quedan **obsoletos sin ningún aviso**. `[03:00]`–`[03:10]` _(C05 FS-2.)_

---

## Tarea 6 — Sacar los informes (Gantt en PDF, flujo planificado, histograma de recursos)

**Qué es:** las salidas imprimibles del módulo.

**Paso a paso** `[03:10]`–`[03:30]`:

1. **El Gantt en PDF:** (opcional) dejá activo el menú que muestra **`CanPlan`** sobre las barras, y la **escala temporal** como quieras que salga impresa — *lo que se ve es lo que se imprime*. Después: menú **`Informes`** → informes de **España** → grupo **`Planificación temporal`** → **`Diagrama de barras`** → botón **`Exportar`** (no `Imprimir`) → formato **PDF** → en `Tamaño del papel` elegí **`Todo el documento`** → ruta de salida → `Aceptar`. `[03:10]`–`[03:20]`
2. **Flujo planificado numérico:** `Informes` → España → grupo **`3 Planificación económica`** → p. ej. *cantidad o importe por meses de capítulos y partidas* ("un informe del flujo de caja desde el punto de vista del árbol"). Al preguntar qué imprimir, elegí **`Planificación`** (lo único con datos antes de la ejecución) y cantidades o importes. `[03:20]`
3. **Histograma de recursos:** `Informes` → **Chile** → planificación económica → **`Análisis de recursos por fases`** (cantidades o importes) → elegí el tipo de recurso (p. ej. mano de obra) → `Aceptar` → genera **salida a Excel** con una pestaña de gráfica (histograma por fase) y otra de datos. `[03:20]`–`[03:30]`

---

## 🎥 Mirá el video

| Tema | Minuto |
|---|---|
| Esquema `Objetivo de coste`, columnas en cero, las dos estructuras de precio | `[02:30]` |
| `Procesos ▸ Generar` + coeficiente de paso 90 + recuadro desmarcado | `[02:30]`–`[02:40]` |
| Esquema `Planificación fases`, `CanPlan`/`Plan`, reparto manual y su riesgo | `[02:40]` |
| `Rellenar la planificación económica` (desde el Gantt) + `plan prece` | `[02:50]` |
| Curvas acumuladas en `Fechas` + exportar a Excel/Power BI + advertencia de no-actualización | `[03:00]` |
| `Calcular recursos` (botón `Defecto`) + Excel para Compras | `[03:00]`–`[03:10]` |
| Informes: Gantt a PDF, planificación económica, histograma de recursos | `[03:10]`–`[03:30]` |

> Video fuente: `Plan_10_12_2025.mp4` (3h 32min). Relator de soporte de Presto.

---

## ⚠️ Lo que Presto NO te avisa (resumen)

- **`Generar` sobrescribe el objetivo de coste** sin versión anterior: la línea base se congela fuera de Presto, y no se vuelve a generar. _(Tarea 2)_
- **El reparto manual de `CanPlan` descuadra** la cantidad presupuestada sin aviso: usá la vía automática desde el Gantt. _(Tarea 3)_
- **`Plan` ≠ `PlanPrece`**: una es coste (PV), la otra es venta (estados de pago). Rotulá siempre. _(Tareas 3–4)_
- **Si el Gantt cambia, nada se recalcula solo**: re-ejecutar `Rellenar la planificación económica` + `Calcular recursos`, siempre, en ese orden. _(Tarea 5)_

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá lo aprendido"
    Sobre la obra de prueba **BLEND**, con el Gantt de la página anterior ya armado:

    1. En `Árbol ▸ Objetivo de coste`, corré **`Procesos ▸ Generar`** con `Generar objetivo` marcado y coeficiente **90** en todas las naturalezas. Verificá que `CanObj` quedó igual a la cantidad presupuestada.
    2. Corré **`Procesos ▸ Rellenar la planificación económica`** con el método del diagrama de barras. En `Planificación fases`, conmutá el segundo menú a **`plan prece`** y comparalo con `Plan`.
    3. En `Fechas ▸ Fases planificación y certificación`, verificá que las columnas acumulan **incrementalmente** y exportá a Excel.
    4. En `Conceptos ▸ Naturalezas básicas recursos`, marcá `CanPlan` y corré **`Procesos ▸ Calcular recursos`** con `Defecto`.
    5. Ahora **cambiá una duración** en el Gantt y volvé al árbol: comprobá con tus propios ojos que **nada se actualizó** — y re-ejecutá los dos procesos.

    **Cómo sabés que salió bien:** `ImpObj` del concepto raíz ≈ 90% del importe presupuestado, la suma horizontal de `CanPlan` de cualquier partida da su cantidad presupuestada, y después del paso 5 los números cambiaron recién al re-ejecutar los procesos.

---

📖 **Fuentes:** transcripción `Plan_10_12_2025` (bloques `[02:30]`–`[03:30]`) · apuntes internos `06-planificacion.md` y `C05-modulo-planificacion-casos-uso.md` (casos 14–21). **Pendientes de verificar en Presto:** rótulo del recuadro desmarcado del diálogo `Generar`, los otros dos métodos de `Rellenar la planificación económica`, qué marca el botón `Defecto` de `Calcular recursos`, y los nombres exactos en pantalla de las columnas `CanObj`/`Obj`/`ImpObj` y `Plan`/`PlanPrece`.
