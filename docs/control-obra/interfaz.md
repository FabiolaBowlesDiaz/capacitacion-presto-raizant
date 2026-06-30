# La pantalla de Control de obra: dónde está cada cosa

!!! abstract "Por qué esta página va primero"
    Lo que más cuesta de Presto **no es entender los conceptos — es no perderse entre tantos menús, esquemas y columnas.** Este rol vive sobre todo en **dos pantallas** que vas a usar todos los días: la pestaña **`Fechas`** (la línea del tiempo, donde están las fases y las curvas) y la pestaña **`Árbol`** (el presupuesto, donde se digita el avance y se lee el costo real). Volvé a esta página cada vez que una instrucción te diga "andá a tal esquema" y no sepas dónde está.

!!! tip "Cómo leemos las rutas en todo el manual"
    Vas a ver dos tipos de instrucción:

    - **Ruta de cinta:** `Ver ▸ Fechas` se lee de izquierda a derecha: primero la **pestaña** de la cinta de arriba (`Ver`), después el **botón** que activás (`Fechas`).
    - **Cambio de esquema:** _"poné el esquema `Certificación | FASES`"_ significa abrir el **menú desplegable de esquemas** (el selector arriba de la tabla) y elegir esa vista. El **esquema** es la "vista" de columnas: la misma tabla cambia de columnas según el esquema que elijas. **Este es el concepto más importante de la pantalla.**

!!! warning "Requisito de licencia — sin esto las pantallas no aparecen"
    Las fases y la certificación viven en el módulo **Gestión de Proyectos**; el costo real y el EVM, en **Facturación y Control**. Si tu licencia no los incluye, los esquemas de certificación/EVM no aparecen en el desplegable. Antes de empezar, **verificá que ambos módulos estén incluidos** (es un requisito a confirmar al contratar/renovar).

---

## El concepto que ordena todo: la pestaña y el esquema

Presto no tiene una pantalla por tarea. Tiene **pocas pestañas** y, dentro de cada una, **muchos esquemas** (vistas). Para este rol, esto es lo que tenés que tener clarísimo:

```
Pestaña ÁRBOL  (el presupuesto, una fila por capítulo/partida)
   ├── esquema "Certificación | FASES"      → certificar avance (Tarea 2)
   ├── esquema "Presupuesto por estados"     → ver inicial vs modificado (Tarea 3)
   └── esquema "Control de costes | FASES"   → ver el costo real ImpInput/ImpReal (Tarea 4)

Pestaña FECHAS  (la línea del tiempo, una fila por fase/período)
   ├── esquema "Días" / "fases planificación" → mover y marcar fases (Tarea 1)
   ├── esquema "[Fases] EVM Valor ganado"      → leer CPI/SPI/EAC (Tarea 4)
   └── esquema "Meses facturación"             → cobros, pagos, flujo de caja
```

> 📖 **Fuente oficial:** _Certificación y seguimiento_ (RIB), p. 9 — el ejemplo oficial empieza diciendo _"Acceda a la ventana «Ver: Fechas», esquema «[Fases] Resumen»… En la ventana de árbol, esquema «Certificación», puede ver los campos…"_. Toda la operación es **elegir la pestaña + el esquema correcto**.

---

## La pestaña `Fechas` — la línea del tiempo de la obra

Andá a la **cinta de arriba**, pestaña **`Ver`**, y activá el **botón `Fechas`** (queda hundido). Se abre una tabla donde **cada fila es una fase** (un período, normalmente un mes).

### Para qué la usás

| Cuándo | Qué esquema poné | Qué hacés ahí |
|---|---|---|
| Al armar la obra | `Días` o `fases planificación` | Crear y ajustar las fechas de certificación (las fases) |
| Cada cierre de mes | `fases planificación` | Marcar la **certificación actual** (la fase naranja) |
| Para ver la salud | `[Fases] EVM Valor ganado` | Leer CPI / SPI / EAC / % Avance |
| Para ver la caja | `Meses facturación` | Cobros, pagos y flujo de caja |

### El "ícono €" y los colores de las fechas

- El **ícono con forma de "€"** sobre la columna `NatC` **NO tiene nada que ver con euros**: es el **ícono de fase / certificación**. Marca que esa fecha es una fecha de cierre de fase.
- Las fechas de certificación se ven **destacadas en color**: la **certificación actual es naranja** (la más oscura), las demás quedan grises. La naranja es **el corte vigente** de la obra.

!!! danger "La fase naranja («certificación actual») es la más importante de esta pantalla"
    Presto **solo acumula** los datos hasta la fase marcada como **certificación actual**. Si te olvidás de moverla cada mes, los números se quedan congelados en el mes anterior **sin ningún aviso**. Lo aprendés a fondo en [2 · Certificar el avance](2-certificar-avance.md).

---

## La pestaña `Árbol` — el presupuesto, fila por fila

Es la misma tabla del presupuesto que usa el rol de Presupuestos, pero acá la mirás con **otros esquemas**. Cada fila es un capítulo o una partida; entrás (doble clic) para desplegar.

### Esquema `Certificación | FASES` — donde se digita el avance

Cuando ponés este esquema, aparecen **pares de columnas numeradas por fase**:

| Columna | Qué es |
|---|---|
| **`CanPres`** | La cantidad presupuestada (tu referencia / el máximo "normal"). |
| **`Cert`** | El precio unitario de certificación (viene del presupuesto de adjudicación). |
| **`N: CanCert`** | **Acá digitás** la cantidad certificada de la fase N (1:, 2:, 3:…). |
| **`N: Cert`** | El importe de esa fase = `N: CanCert` × precio. Se calcula solo. |
| **`CanCert`** (sin número) | La cantidad certificada **acumulada** hasta la fase actual. |
| **`ImpCert`** | El importe certificado **acumulado** hasta la fase actual. |
| **`CanCertAct`** / **`ImpCertAct`** | Cantidad / importe **de la fase actual** (la naranja). |
| **`PorCertPres`** | El % certificado sobre presupuesto (calculado con importes, no cantidades). |

!!! note "Los colores de `CanCert` te dicen de dónde salió el dato"
    **Magenta** = viene de líneas de medición · **Negro** = lo digitaste a mano · **Rojo** (en `ImpCert`) = **sobrecertificación** (certificaste más de lo presupuestado) · **Fondo gris** = anulado, no cuenta. El rojo es una alarma: lo ves en la [Tarea de adicionales](3-adicionales-y-estados-de-pago.md).

### Esquema `Presupuesto por estados` — el presupuesto "vivo"

Muestra cómo el presupuesto se mueve con los cambios aprobados:

| Columna | Qué es |
|---|---|
| **`PRS CanIni`** | Cantidad del presupuesto **inicial** (líneas en estado `inicial`). |
| **`PRS CanMod`** | Cantidad de los **cambios aprobados** (líneas en estado `modificado`, verde). |
| **`CanPres`** | La suma de ambos = el presupuesto **vigente**. |
| **`PRS CanPte`** | Cantidad **pendiente de aprobación** (no suma al vigente). |
| **`ImpPresIni`** / **`ImpPresMod`** / **`ImpPres`** | Los mismos tres, pero en importe. |

### Esquema `Control de costes | FASES` — el costo real

Acá vive el costo real que alimenta el EVM:

| Columna | Qué es |
|---|---|
| **`ImpInput`** | Costo real **auténtico** = suma directa de lo imputado en Entregas. _Para conciliar con caja._ |
| **`ImpReal`** | Costo real **ponderado** (precio medio si hubo compras a precios distintos). _Para el EVM._ |
| **`ImpRealObj`** | Cantidad real × precio del objetivo = el valor ganado a nivel de concepto. |
| **`N: CanReal`** | La **cantidad ejecutada real** de la fase N (la digita el control de obra). |
| **`N: Input`** | El consumo imputado a la partida en la fase N (de las Entregas). |

> 📖 **Fuente oficial:** _Cómo se calculan los costes reales_ (RIB), p. 3 — tabla de variables: `Real` = _"coste real basado en consumos reales y promedios"_; `ImpInput` = _"coste basado en suma directa de imputaciones"_; `RealObj` = _"coste basado en las cantidades reales, a precio estimado"_.

---

## La subventana `Mediciones` (abajo) — el detalle de cada partida

Cuando marcás una partida y abrís la subventana `Mediciones`, ves las **líneas de medición** que la componen. Acá se certifica con respaldo y se meten los adicionales:

| Columna / botón | Qué es |
|---|---|
| **`Comentario`** | Texto descriptivo de la línea (ej. "rellenos", "rellenos adicional 01"). |
| **`Cantidad`** | La cantidad de la línea. |
| **`Espacio`** | A qué espacio se asigna. **No puede quedar en blanco.** |
| **`EstadoPres`** | El estado de la línea: `Inicial` / `Modificado` (verde, aprobado) / `Pendiente`. |
| **`FasePlan`** / **`FaseReal`** / **`FaseCert`** | A qué fase se asigna (planificada / ejecución / certificación). |
| Botón **`Desdoblar`** (clic derecho sobre la cantidad) | Parte una línea en dos (ej. 119 → 100 + 19) para certificar por fases distintas. |

---

## Capturas de estas pantallas

!!! info "Capturas en camino"
    Las capturas críticas (la pestaña `Fechas` con la certificación actual naranja, el Árbol en esquema `Certificación | FASES` con los pares `N: CanCert`, el esquema EVM con CPI/SPI coloreados, y `Presupuesto por estados`) se agregarán cuando esté disponible la licencia con los módulos Gestión de Proyectos + Facturación y Control. Mientras tanto, el texto de cada tarea te orienta paso a paso sin necesidad de la imagen.

---

📖 **Fuente oficial (RIB):** _Certificación y seguimiento_ (pp. 3–16) · _Cómo se calculan los costes reales_ (p. 3) · _Valor ganado: el proyecto A-12_ (pp. 6–8). **Complemento interno:** apuntes C08 (certificación) y C09 (EVM), glosario de columnas verificado por captura · transcripciones `gestion_de_proyectos_09_12_2025` y `FactCon_08_08_2025`.
