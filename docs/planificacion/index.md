# Planificación (cronograma)

!!! info "¿Esta sección es para vos?"
    Sos de **planificación** si tu trabajo es **decir cuándo se hace cada cosa y cuánto va a costar hacerla en cada mes**: armar el cronograma de la obra (el Gantt), estimar duraciones, encadenar actividades, fijar la línea base de coste y proyectar el flujo de dinero y de recursos en el tiempo. Todo esto pasa **antes** de que la obra arranque — sos quien dibuja el plan contra el que después se mide la realidad.

!!! abstract "Conclusión primero"
    En Presto, **el cronograma no es un Excel aparte: es una vista más del mismo presupuesto**. El diagrama de barras usa la misma estructura del árbol — cada partida es una actividad — así que no hay doble captura ni "versión del superintendente" desconectada. Y de ese mismo Gantt salen, con procesos automáticos, el **objetivo de coste** (la línea base contra la que se mide el costo real), el **flujo planificado por fases** (la curva S) y el **calendario de recursos** que alimenta a Compras. Esa es exactamente la brecha que Raizant arrastra hoy: cronograma fuera de sistema, sin vínculo a partidas, y proyección de caja en un Excel desconectado.

!!! warning "Requisito de licencia"
    La planificación vive en el módulo **Planificación** de Presto (licencia propia). Podés verificar que esté habilitado en la **instancia de activación** de Presto, que lista los módulos disponibles. Si tu licencia no lo incluye, el propio capacitador sugiere seguir el curso con la **versión demo**. `[00:00]`

!!! danger "Prerrequisito duro: la línea temporal ya tiene que existir"
    Antes de planificar, el archivo necesita las **fases de certificación** creadas en la pestaña `Fechas` (el proceso `Crear fechas de certificación`). Si eso no está, no hay nada que planificar. Se arma una sola vez — el paso a paso está en **[Control de obra › 1 · Armar la línea temporal](../control-obra/1-linea-temporal.md)**. **No** vuelvas a correr ese proceso si la línea temporal ya existe. `[00:00]`

## Tu recorrido de aprendizaje

Son dos páginas, en el orden en que se trabaja de verdad: primero el **tiempo** (el Gantt), después el **dinero** (la planificación económica). El orden no es opcional — la planificación económica se rellena *desde* el diagrama de barras, así que sin Gantt no hay números.

<div class="grid cards" markdown>

-   **1 · Armar el cronograma (el diagrama de barras)**

    ---

    La planificación temporal: revisar el **calendario** laborable/festivo, dejar la **certificación actual en la primera fase** (el detallito que rompe todo si se olvida), configurar la ventana del Gantt, ingresar **duraciones**, crear **enlaces de precedencia**, solapar actividades, limpiar de cero y **exportar** a MS Project.

    [:octicons-arrow-right-24: Ver](1-armar-el-cronograma.md)

-   **2 · Objetivo de coste y curva S (planificación económica)**

    ---

    La planificación económica: generar el **objetivo de coste** con el coeficiente de paso (tu línea base), **periodificar** cantidades y montos por fase desde el Gantt, calcular los **recursos por fase** para Compras, y leer las **curvas** que después alimentan el EVM.

    [:octicons-arrow-right-24: Ver](2-objetivo-de-coste-y-curva-s.md)

</div>

## Quién usa esto en Raizant

El video de capacitación es genérico (no asigna roles de empresa), así que este reparto es una **propuesta** a ajustar:

| Rol | Qué hace en Planificación |
|---|---|
| **Planificador de obra / superintendente** | Revisa el calendario, arma el diagrama de barras (duraciones, enlaces, solapes), rellena la planificación económica y calcula recursos. |
| **Jefe de presupuestos / control de obra** | Define el **coeficiente de paso** y genera el **objetivo de coste** — es una decisión de margen, no de quien dibuja barras. |
| **Compras / contratación** | Consume el **calendario de recursos por fase** (exportado a Excel) para anticipar arriendos, compras y subcontratos. |
| **Torre de control** | Toma las tres curvas (objetivo de coste, venta, certificación) para el tablero de salud de obra. |

## En una frase, qué vas a aprender

A pasar de **un presupuesto aprobado** a **un plan completo de la obra**: el cronograma colgado de las mismas partidas del presupuesto (sin Excel paralelo), la línea base de coste contra la que se medirá todo, y el calendario de plata y recursos mes a mes — y, sobre todo, a saber que **Presto genera todo esto pero no lo vigila**: no congela la línea base, no recalcula solo cuando cambiás el Gantt, y no exporta el calendario con fidelidad. Esas tres vigilancias las ponemos nosotros.

---

!!! note "Fuente de esta sección"
    Construida sobre la transcripción del video de capacitación **`Plan_10_12_2025`** (3h 32min, relator de soporte de Presto) y los apuntes internos **06 — Planificación** y **C05 — Módulo Planificación (casos de uso)**. A diferencia de otras secciones, acá **todavía no hay documento oficial RIB citado página por página**: los pasos salen del video, y los detalles que el audio no deja confirmar están marcados como *"verificar en Presto"*. Cada tarea cita su minuto `[hh:mm]`.
