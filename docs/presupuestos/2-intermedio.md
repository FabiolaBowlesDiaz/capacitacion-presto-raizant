# 2 · Presupuesto intermedio

!!! abstract "Conclusión primero"
    Acá pasás de "armar el presupuesto" a "armarlo bien y a escala". Aprendés a importar de Excel con el método pro (**Excel2Presto**), a modelar **conceptos porcentaje** (leyes sociales, IVA) y **subcontratos**, a usar las columnas potentes del APU (`Código2`, `Factor`, `Nota`), a ajustar precios masivamente y a **exportar** — incluido el camino correcto para llevar el código contable a Excel.

!!! info "De dónde sale este contenido"
    Apunte de capacitación **CL-2 (Presupuesto Intermedio)** + **capturas reales de pantalla** (que confirman los nombres internos de las columnas) + manuales RIB. Asume que ya hiciste el [Presupuesto básico](1-basico.md). Cada paso cita el minuto `[hh:mm]` del video.

---

## Antes de empezar: lo que necesitás

| Necesitás | Por qué |
|---|---|
| Saber lo del [Presupuesto básico](1-basico.md) | CL-2 da por sabido todo lo de CL-1 |
| **Excel instalado** + el complemento **Excel2Presto** | Para importar el itemizado (Tarea 1) |
| **El Excel a importar en disco LOCAL, no en OneDrive** | Con archivo en la nube, Excel2Presto **falla garantizado** |
| Una tabla de Excel limpia (una sola fila de cabecera) | Una fila de datos perdida muy abajo cuelga el análisis |

---

## Tarea 1 — Importar un itemizado con Excel2Presto

**Qué es:** el método eficiente para llevar un presupuesto de Excel a Presto. A diferencia del copiar/pegar simple, **analiza las columnas, deduce qué es cada una y arma el árbol** (capítulos → partidas) solo.

**Paso a paso** `[00:00]`–`[01:00]`:

1. **Instalar el complemento** (una vez): cerrá Excel → ejecutá el `setup` en `C:\Archivos de programa\Presto <versión>\Excel2Presto\` → reabrí Excel; aparece un menú **"Excel2Presto"**. Si no aparece: Opciones de Excel → Complementos → habilitalo a mano.
2. **Copiá el Excel a una carpeta local** (no OneDrive).
3. En el menú Excel2Presto → **`Analizar`** (dejá las opciones por defecto). El panel muestra cada columna con su asignación deducida (A→`Código`, C→`Resumen`, D→`Cantidad`…).
4. **Corregí una asignación errada**: clic derecho en la cabecera de la columna → elegí la columna de Presto correcta.
5. **Marcá las filas de capítulo**: clic derecho en el número de fila → `Tipo de línea capítulo`. Presto **re-analiza y aplica la marca a todas las filas semejantes** de un saque.
6. **Separá códigos por nivel** (panel derecho) para que las partidas se aniden bajo sus subcapítulos.
7. **`Exportar`** → genera una obra `.presto`. _(La ventana no se cierra sola; cerrala a mano y abrí el resultado en Presto.)_
8. En Presto, lo que no quedó anidado se completa con `Disminuir nivel`.

!!! warning "Los dos errores que cuelgan Excel2Presto"
    - **Archivo en OneDrive/nube** → error garantizado, no carga nada. Copialo a disco local primero.
    - **Una fila de datos perdida muy abajo** (ej. fila 25.000) → el análisis entra en bucle infinito sin avisar. Limpiá la tabla antes.

!!! danger "Cuidado: las marcas se propagan a TODO lo semejante"
    `Tipo de línea anulada` y `Celda excluida` se aplican a **todas** las filas/celdas con contenido parecido. Si excluís un "m3", se excluyen **todos** los "m3" de la columna. Revisá visualmente (las celdas grises = no se exportan) antes de exportar.

---

## Tarea 2 — Modelar un concepto PORCENTAJE (leyes sociales, IVA)

**Qué es:** una línea especial del APU que calcula un porcentaje sobre otros recursos (cargas sociales sobre la mano de obra, IVA por categoría, etc.).

**Paso a paso** `[01:00]`–`[01:30]`:

1. Creá el recurso con el símbolo **`%` en el código**. Presto lo reconoce y le da un color de código distinto (anaranjado).
2. **Lo que va a la IZQUIERDA del `%` es la máscara de búsqueda.** Ej.: `O0%` busca los conceptos cuyo código empieza con `O0` y calcula sobre ellos.
3. En la columna **`Pres`** escribí el **factor** (ej. `29` = 29%), **no un precio**.
4. **Unidad** = `%`. **Naturaleza** = una básica (ej. mano de obra, para que las leyes sociales se agrupen con la MO en el informe).

!!! danger "Regla de oro del concepto porcentaje"
    La búsqueda es **solo en el mismo nivel y solo hacia ARRIBA** (las filas de encima). Por eso el porcentaje va siempre en la **última fila** del APU. Si agregás una mano de obra **debajo** del porcentaje, **no la captura** — hay que reposicionar con `Subir`/`Bajar`.

---

## Tarea 3 — Marcar un SUBCONTRATO (partida + suministro)

**Qué es:** una partida que ejecuta un subcontratista con un precio cerrado, sin APU desglosado (muebles de cocina, instalaciones, etc.).

!!! note "No existe una naturaleza 'subcontrato'"
    Un subcontrato = **naturaleza Partida + propiedad Suministro**. Es una combinación, no un tipo propio.

**Paso a paso** `[01:30]`:

1. Dentro de la partida correspondiente, creá el concepto con **naturaleza `Partida`**.
2. Clic derecho → activá la propiedad **`Suministro`**. El ícono se pone **naranja 🟧**.
3. Cargalo: **cantidad `1`**, **unidad `global`**, **precio cerrado** del subcontratista, **sin descomposición**.

!!! warning "No confundas con el ícono 'Subcontratista'"
    Hay un ícono "Subcontratista" en otros menús que pertenece a la ventana de Entidades — **ese no sirve** para esto. Es la propiedad **Suministro** sobre la partida.

!!! tip "Por qué importa marcarlo bien"
    Un subcontrato bien marcado es **prerrequisito** para encadenarlo después a Contratos → Pedidos → Entregas → Facturas. Si está mal marcado, no fluye aguas abajo. Estandarizá internamente cómo se marca.

---

## Tarea 4 — Las columnas potentes: Código2, Factor, Nota

**Qué es:** columnas ocultas por defecto que dan mucho poder al APU.

**Paso a paso para mostrarlas** `[01:40]`:

1. Clic derecho en cualquier cabecera → **`Elegir columnas visibles`**.
2. En el filtro (⚠️ **sensible a tildes y mayúsculas**), buscá y trasladá: `Código2`, `Factor`, `FactorExp`, `Nota`.
3. `Aceptar`.

### Código2 — el puente con contabilidad

!!! abstract "Lo importante de Código2"
    Es un **código secundario** por concepto. A diferencia del `Código` (único e irrepetible), el **`Código2` se puede repetir** — por eso varios conceptos pueden colgar de la **misma cuenta contable / centro de costo** de Syneco. Es el mecanismo nativo para mapear el presupuesto al plan de cuentas.

### Factor / FactorExp — mermas, viajes, rendimientos

- La columna **`Factor` es de solo lectura** (fondo amarillo). El valor se ingresa en **`FactorExp`** como una expresión.
- Ejemplos: desperdicio 5% → `FactorExp` = `1,05`. Pérdida × viajes → `1,05*2`. Inverso de rendimiento → `1/1,0526`.
- El factor **multiplica la cantidad sin modificarla** (la cantidad base queda intacta).
- **`Nota`**: texto para documentar qué significa cada factor.

---

## Tarea 5 — Ajustar precios masivamente (Operar y Ajustar)

**Qué es:** dos palancas para reproyectar precios de forma controlada y reversible.

**Operar** (`Herramientas → Operar`) `[02:10]`:

- Subís/bajás precios por tipo de recurso con un coeficiente. **`100` = sin cambio**; `101,5` = +1,5%; `98` = −2%.
- Toca **solo precios** (no cantidades) y se aplica a **todo el árbol**. Reversible con Deshacer.

**Ajustar** (`Herramientas → Ajustar`) `[02:20]`–`[02:30]`:

- Lleva un concepto con APU a un **precio objetivo**, prorrateando sus inferiores.
- Solo funciona con conceptos que tienen descomposición. Los conceptos porcentaje quedan fuera.

---

## Tarea 6 — Guardar tu vista de columnas (esquemas)

**Qué es:** que las columnas que configuraste no se pierdan.

**Paso a paso** `[02:10]`: clic derecho en cualquier cabecera →

- **`Guardar esquema de defecto`** → guarda la vista en tu estación de trabajo.
- **`Guardar esquema en la obra`** → embebe la vista en el archivo; cualquiera que abra esa obra ve las mismas columnas (ideal para estandarizar al equipo).

---

## Tarea 7 — Exportar a Excel (¡hay DOS caminos distintos!)

!!! danger "El error que confunde a todos"
    Hay **dos botones que dicen 'Exportar a Excel'** y hacen cosas diferentes. Elegir el equivocado para el puente contable **pierde el Código2 en silencio**.

| | `Archivo → Exportar → Excel` | `Inicio → Exportar a Excel` |
|---|---|---|
| Qué saca | La estructura de precios (formato fijo) | La **vista que tenés en pantalla**, con las columnas visibles |
| ¿Lleva `Código2`? | **❌ NO** (no es configurable) | **✅ SÍ**, si la columna está visible |
| Resultado | Tabla con fórmulas | Tabla de valores (apta para Power BI) |

!!! tip "Para el puente con Syneco"
    Usá **`Inicio → Exportar a Excel`** con la columna `Código2` **visible** en pantalla. Es el único camino que lleva el código contable. El otro lo descarta.

**Otros formatos** (`Archivo → Exportar`): también existe **BC3** (formato estándar de intercambio de presupuestos), SQL Server, Catálogo Revit, MS Project.

---

## 🎥 Mirá el video

| Tema | Minuto |
|---|---|
| Excel2Presto (importar) | `[00:00]`–`[01:00]` |
| Conceptos porcentaje | `[01:00]`–`[01:30]` |
| Subcontratos | `[01:30]` |
| Columnas Código2 / Factor / Nota | `[01:40]`–`[02:10]` |
| Operar / Ajustar | `[02:10]`–`[02:30]` |
| Filtros y estados | `[02:40]`–`[03:10]` |
| Exportaciones | `[03:10]`–`[03:40]` |

> Video fuente: `CL-2 - Ppto Intermedio - Viernes 28_11_2025.mp4` (3h 48min).

---

## ⚠️ Lo que Presto NO te avisa (resumen)

- **Excel2Presto con archivo en OneDrive** → falla; copialo local.
- **Código2 vacío** → el puente contable no existe, y nadie te avisa. Cargalo siempre.
- **Código2 mal tipeado** → como se puede repetir, cruza dos cuentas sin error (a diferencia del Código).
- **Usar `Archivo → Exportar → Excel` para el puente contable** → pierde el Código2 en silencio.
- **Concepto porcentaje mal posicionado** → barre solo hacia arriba; no captura lo que esperás.

👉 Todas en [5 · Reglas de oro y fallas silenciosas](5-reglas-de-oro.md).

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá lo aprendido"
    Sobre la obra de prueba **BLEND**:

    1. Tomá una lista de materiales en Excel, copiala a una carpeta local e importala con Excel2Presto.
    2. En una partida, agregá un concepto porcentaje de leyes sociales sobre la mano de obra (código con `%`, factor en `Pres`, última fila).
    3. Marcá una partida como subcontrato (Suministro, ícono naranja).
    4. Mostrá la columna `Código2`, ponele un valor a un par de conceptos, y exportá con `Inicio → Exportar a Excel` verificando que el Código2 viaje.

    **Cómo sabés que salió bien:** el Excel exportado tiene la columna Código2 con los valores que pusiste.

---

📖 **Fuente oficial:** Presto-Presupuestos.pdf · Personalizacion-de-columnas-y-esquemas.pdf · Uso-de-colores.pdf (RIB). · Apunte: C03 — Presupuesto intermedio (casos de uso 1–18, verificado con capturas).
