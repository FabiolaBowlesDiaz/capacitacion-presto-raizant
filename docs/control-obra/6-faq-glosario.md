# 6 · Preguntas frecuentes y glosario

!!! abstract "Conclusión primero"
    Las dudas que aparecen siempre en este rol, respondidas corto, y el **diccionario de columnas** — porque el control de obra es el rol con más columnas de nombre raro (`CanCert`, `ImpCert`, `EvmCpi`, `OrReal`, `FaseCert`…). Tené esta página a mano mientras te acostumbrás.

---

## Preguntas frecuentes

### ¿Cuál es la diferencia entre certificar y el avance físico?
**Certificar** = registrar el avance que el cliente **aprueba para pagarte** (para emitir estados de pago). El **avance físico** = lo que de verdad se construyó. Pueden no coincidir: podés tener certificado el 40% pero físicamente ejecutado el 35% (o al revés). Este rol maneja la **certificación**; el avance físico (cantidad real) lo carga el rol Obra/Almacén y el EVM lo cruza. _(Ver [0 · Fundamentos](0-fundamentos.md).)_

### Cargué el avance pero los acumulados no cambian. ¿Por qué?
Casi seguro **no marcaste la fase como "certificación actual"**. Presto solo acumula hasta la fase naranja. Clic derecho sobre la fase → `Certificación actual`, y `CanCert` se actualiza. Es la falla silenciosa #1 del rol.

### ¿El avance se ingresa como cantidad o como porcentaje?
**Siempre como cantidad** (la columna es `CanCert`). Si te lo pasan en %, alguien lo convirtió desde una cantidad — pedí el dato original. Cargar un % rompe la lógica.

### Metí un adicional y se puso rojo. ¿Está mal?
Sí: el rojo es **sobrecertificación**. Lo digitaste directo en el árbol y Presto no entiende que es un cambio de alcance. El adicional va por una **línea de medición** en `Mediciones`, con su `EstadoPres` y `FaseCert`. _(Ver [3 · Adicionales](3-adicionales-y-estados-de-pago.md).)_

### ¿Qué diferencia hay entre un adicional `modificado` y uno `pendiente`?
**`modificado`** (verde) = aprobado: suma al presupuesto vigente y entra al estado de pago (lo cobrás). **`pendiente`** = en espera de aprobación: NO suma, corre solo como costo. Si un adicional `pendiente` nunca se aprueba, ese costo lo absorbe Raizant.

### El CPI me da verde pero siento que la obra va mal. ¿Le creo?
Antes de creerle, verificá que el dato base esté completo: ¿hay **fechas de imputación grises**? ¿está la **baseline congelada**? ¿se imputaron **todos los consumos**? Un CPI verde sobre costo real incompleto miente — es la trampa central del EVM. _(Ver [5 · Reglas de oro](5-reglas-de-oro.md).)_

### ¿Por qué el costo real del EVM no coincide con la suma de mis facturas?
Porque hay **dos** costos reales: `ImpInput` (suma aritmética directa = auténtico, para conciliar con caja) e `ImpReal`/`OrReal` (precio medio ponderado, para las curvas del EVM). Si compraste el mismo material a precios distintos, difieren. No es un error. _(Ver [4 · EVM](4-evm-salud-de-obra.md), Tarea 6.)_

### ¿Qué significan CPI y SPI en una frase?
**CPI = ¿gasto bien?** (mayor a 1 = ahorro, menor = sobrecosto). **SPI = ¿voy a tiempo?** (mayor a 1 = adelantado, menor = atrasado).

### El SPI me da casi 1 pero sé que vamos atrasados. ¿Por qué?
Es una limitación conocida: el SPI **tiende a 1 al final** de la obra aunque haya atraso real (porque EV y PV convergen al total). No te quedes solo con el SPI: cruzalo con el avance físico vs el cronograma del Gantt.

### ¿Tengo que recalcular siempre?
Sí. Presto **no refresca en tiempo real**. Después de cargar avance, mover la certificación actual, o tocar mediciones, andá a `Inicio ▸ Recalcular` antes de leer cualquier número.

### ¿Dónde saco las curvas S para el tablero?
En la pestaña `Fechas`, esquema `[Fases] EVM Valor ganado`, botón `Exportar a Excel`. De ahí salen las tres curvas PV/EV/AC. Ese export es el que alimenta el dashboard de la torre de control. _(Ver [4 · EVM](4-evm-salud-de-obra.md), Tarea 7.)_

---

## Glosario de columnas y términos

### Certificación (pestaña Árbol, esquema `Certificación | FASES`)

| Término | Significado |
|---|---|
| **`CanPres`** | Cantidad presupuestada (tu referencia / el máximo "normal"). |
| **`Cert`** | Precio unitario de certificación (viene del presupuesto de adjudicación). |
| **`N: CanCert`** | Donde **digitás** la cantidad certificada de la fase N (1:, 2:, 3:…). |
| **`N: Cert`** | Importe de esa fase = `N: CanCert` × precio. Se calcula solo. |
| **`CanCert`** | Cantidad certificada **acumulada** hasta la fase actual. Magenta=de mediciones, negro=digitado, rojo (en ImpCert)=sobrecertificación. |
| **`ImpCert`** | Importe certificado **acumulado** hasta la fase actual. |
| **`CanCertAct`** / **`ImpCertAct`** | Cantidad / importe **de la fase actual** (la naranja). |
| **`PorCertPres`** | % certificado sobre presupuesto = `ImpCert / ImpPres` (con importes, no cantidades). |

### Presupuesto por estados (pestaña Árbol)

| Término | Significado |
|---|---|
| **`PRS CanIni`** | Cantidad del presupuesto inicial (líneas en estado `inicial`). |
| **`PRS CanMod`** | Cantidad de cambios aprobados (líneas `modificado`, verde). |
| **`CanPres`** | Unificación = inicial + modificado aprobado. El valor que Presto usa para desvíos. |
| **`PRS CanPte`** | Cantidad pendiente de aprobación (no suma al vigente). |
| **`ImpPresIni` / `ImpPresMod` / `ImpPres`** | Los mismos, en importe. |

### Mediciones (subventana)

| Término | Significado |
|---|---|
| **`Comentario`** | Texto descriptivo de la línea. |
| **`Espacio`** | A qué espacio se asigna. **No puede quedar en blanco.** |
| **`EstadoPres`** | Estado de la línea: `Inicial` / `Modificado` (verde, aprobado) / `Pendiente`. |
| **`FasePlan` / `FaseReal` / `FaseCert`** | Fase de planificación / ejecución / certificación a la que se asigna. |
| Botón **`Desdoblar`** | Parte una línea en dos (clic derecho sobre la cantidad). |

### EVM / valor ganado (pestaña Fechas, esquema `[Fases] EVM Valor ganado`)

| Término | Significado | En el EVM |
|---|---|---|
| **`OrPlan`** | Importe planificado acumulado (objetivo periodificado) | **PV** |
| **`OrRealObj`** | Cantidad real × precio del objetivo | **EV** (valor ganado) |
| **`OrReal`** | Costo real acumulado (ponderado) | **AC** |
| **`OrCert`** | Certificación acumulada | producción cobrada |
| **`OrPlanPres` / `OrRealPres`** | Producción planificada / real a precio de venta | curvas de venta |
| **`EvmCpi`** | Índice de desempeño del coste = EV / AC | **CPI** |
| **`EvmSpi`** | Índice de desempeño del cronograma = EV / PV | **SPI** |
| **`EvmEac` / `EvmEacCpi`** | Estimación a la conclusión / ajustada por CPI | **EAC** |
| **`Avance`** | Valor ganado / objetivo = EV / BAC | **% avance económico** |

### Costo real (pestaña Árbol, esquema `Control de costes | FASES`)

| Término | Significado |
|---|---|
| **`ImpInput`** | Costo real **auténtico** = suma directa de imputaciones. _Para conciliar con caja._ |
| **`ImpReal`** | Costo real **ponderado** (precio medio si hubo compras a precios distintos). _Para el EVM._ |
| **`ImpRealObj`** | Cantidad real × precio del objetivo (el valor ganado a nivel de concepto). |
| **`N: CanReal`** | Cantidad ejecutada real de la fase N (la carga Obra/Almacén). |
| **`N: Input`** | Consumo imputado a la partida en la fase N. |

### Siglas del valor ganado

| Sigla | Inglés | En criollo | Presto |
|---|---|---|---|
| **PV** | Planned Value | Lo que planeaste producir a la fecha | `OrPlan` |
| **EV** | Earned Value | Lo que vale lo que hiciste (a precio plan) | `OrRealObj` |
| **AC** | Actual Cost | Lo que te costó | `OrReal` / `ImpInput` |
| **BAC** | Budget At Completion | El presupuesto total (no cambia) | `Obj` |
| **CPI** | Cost Performance Index | ¿Gasto bien? (EV/AC) | `EvmCpi` |
| **SPI** | Schedule Performance Index | ¿Voy a tiempo? (EV/PV) | `EvmSpi` |
| **EAC** | Estimate At Completion | ¿En cuánto termina? | `EvmEac(Cpi)` |

### Otros términos

| Término | Significado |
|---|---|
| **Fase** | Período entre dos fechas de certificación (normalmente un mes). |
| **Certificación actual** | La fase vigente (naranja). Presto solo acumula hasta ella. |
| **Estado de pago** | Documento de cobro al cliente, derivado de la certificación acumulada. |
| **Sobrecertificación** | Certificar más de lo presupuestado sin registrarlo como cambio → importe en rojo. |
| **Curva S** | Gráfica dinero vs. tiempo (acumulado). Se exporta a Excel desde `Fechas`. |
| **Baseline** | El objetivo de coste congelado, contra el que se miden los desvíos. |

---

📖 **Fuentes oficiales (RIB):** _Certificación y seguimiento_ · _El valor ganado explicado en 4 páginas_ · _Cómo se calculan los costes reales_ · _Órdenes de cambio_. **Complementos internos:** apuntes C08 (§5 glosario) y C09 (§2 glosario) · transcripciones de los videos de capacitación.
