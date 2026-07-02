# 1 · Armar el cronograma (el diagrama de barras)

!!! abstract "Conclusión primero"
    El cronograma en Presto se arma en la ventana **`Diagrama de barras`**, que **reutiliza el mismo árbol del presupuesto**: cada partida es una actividad, sin estructura paralela. El trabajo tiene un orden estricto: primero la **previa** (calendario laborable/festivo, certificación actual en la primera fase, ventana de visualización), después las **duraciones** (columna `DURTOT`, con sugerencia automática desde el APU), después los **enlaces de precedencia** (FC/FF/CC) y los **solapes**. Al final podés exportarlo a MS Project o XML — pero Presto queda como master, porque la exportación **pierde el calendario**.

!!! warning "Requisito de licencia"
    Todo lo de esta página vive en el módulo **Planificación**. Verificá en la **instancia de activación** de Presto que esté habilitado; si no, seguí con la versión demo. `[00:00]`

!!! info "De dónde sale este contenido"
    Fuente principal: transcripción del video **`Plan_10_12_2025`** (de ahí salen los minutos `[hh:mm]` y las rutas de clic), estructurada en los apuntes internos **06** y **C05**. No hay todavía documento oficial RIB citado para este módulo; lo que el audio no deja confirmar está marcado como *"verificar en Presto"*.

---

## El modelo mental: el Gantt ES el árbol del presupuesto

> _"El diagrama de barras simplemente te hace uso de la estructura del árbol que tienes armada… Para el Presto, por defecto, las partidas principales… son los elementos a planificar."_ `[00:30]`

- Cada fila del árbol (concepto raíz, capítulo, subcapítulo, partida) es una **actividad**. No creás tareas nuevas: programás lo que ya presupuestaste. `[01:00]`
- Por defecto, lo programable son las **partidas de primer orden** (no las subpartidas). Para programar subpartidas, la partida madre se convierte en tipo `Resumen` (ver Tarea 5). `[00:30]` `[01:00]`
- **Límite:** el diagrama de barras maneja un máximo de **10.000 actividades**, contando concepto raíz, capítulos, subcapítulos y partidas. Para presupuestos muy desglosados, planificá a nivel de partida de primer orden. `[01:00]`

**Por qué le importa a Raizant:** este es el fin del "cronograma del superintendente en Excel". El Gantt vive colgado de las mismas partidas que el presupuesto — una sola fuente de verdad temporal.

---

## BLOQUE A — La previa (antes de tocar una sola barra)

## Tarea 1 — Revisar el calendario: laborable vs festivo

**Qué es:** decirle a Presto qué días se trabaja. Los días **festivos no cuentan** al calcular duraciones — el propio Presto lo define así: _"un día que no cuenta al calcular las duraciones en el diagrama de barras"_. `[00:10]`

**Por qué va primero:** si cambiás el calendario después de armar barras, todas las duraciones recalculan. Se hace ANTES. `[00:10]`

**Dónde estás:** pestaña **`Fechas`** (menú `Ver` → interruptor `Fechas`), esquema **`Días`**.

**Paso a paso — dejar todos los sábados laborables de un saque** `[00:00]`–`[00:10]`:

1. En la pestaña `Fechas`, abrí el menú de esquemas y elegí **`Días`** → ves el calendario completo, una fila por día.
2. Mirá la columna de los **íconos del día de semana** (`NatSem`): los íconos **negros** (lun–vie) están en estatus **`laborable`**; los **rojos** (sáb/dom) están en **`festivo`**. Clic secundario sobre un ícono te muestra su estatus.
3. **No** vayas sábado por sábado (serían ~53 clics). En la columna **`Día`**, pará el cursor en una celda con la letra **`S`** (sábado) → **clic secundario** → **`Filtrar por contenido`** → la tabla muestra solo los sábados.
4. Seleccioná toda la columna `NatSem` (clic en la **cabecera**) → clic secundario sobre el ícono → cambiá el estatus de **`festivo` → `laborable`**. Listo: todos los sábados del calendario quedaron laborables.
5. **Quitá el filtro inmediatamente**: menú `Inicio` → botón **`Anular`** (o el acceso directo en la barra de título de Presto).
6. **Feriados irrenunciables** (los de Bolivia, en nuestro caso): esos se marcan **a mano**, uno a uno, ubicando la fecha en la tabla y pasándola a `festivo`. `[00:10]`–`[00:20]`

!!! note "No existe la media jornada"
    Presto solo tiene dos estatus: `laborable` o `festivo`. Si un día se trabaja aunque sea 30 minutos, va como laborable. _"No hay una instancia de media jornada."_ `[00:10]`

---

## Tarea 2 — Dejar la "certificación actual" en la primera fase

**Qué es:** un cambio de estatus de una fecha, que marca desde dónde arrancan todos los cálculos de planificación.

**Por qué importa:** en Control de obra la certificación actual va avanzando con la ejecución. Pero acá **todavía no hay ejecución** — estamos en la previa — y si la certificación actual quedó en una fase intermedia (por ejemplo, del ejercicio de certificación de la clase anterior), el flujo de caja y la planificación de recursos **no arrancan desde el día 1**.

**Paso a paso** `[00:20]`:

1. En la pestaña `Fechas`, ubicá la **primera fase** del calendario (en el video, el 31-dic-25).
2. **Clic secundario** sobre ella → marcá **`Certificación actual`**.
3. Confirmalo visualmente cambiando el esquema de la pestaña `Fechas` a **`Fases planificación`**: la primera fase debe verse marcada como la actual.

!!! danger "Falla silenciosa — la certificación actual fuera de la primera fase rompe los cálculos sin error visible"
    Presto no avisa nada: simplemente _"el flujo de caja de la planificación y la planificación de los recursos no se ve como que se estuviera haciendo desde el día 1 del calendario"_. Es una consulta clásica de soporte — la gente hace todo bien y "la planificación se ve algo extraña". El capacitador insiste: _"siempre la primera fase tiene que quedar marcada con la propiedad certificación actual para efectos del módulo de planificación."_ `[00:20]` _(C05 FS-3.)_

---

## Tarea 3 — Definir la ventana de visualización (`FEC Inicio Obra` / `FEC Fin Obra`)

**Qué es:** fijar el área temporal donde se van a dibujar las barras.

**Dónde estás:** menú **`Ver` → `Propiedades`**, sección **`Tiempos`**.

**Paso a paso** `[00:20]`–`[00:30]`:

1. Revisá **`FEC Inicio Obra`** y **`FEC Fin Obra`**: juntos definen **la ventana de visualización del diagrama de barras** — _"con estos dos parámetros tú fijas la ventana de trabajo donde tú vas a armar el diagrama de barras"_.
2. **No confundas** `FEC Fin Obra` con el fin del calendario: el calendario puede extenderse mucho más allá; este parámetro solo acota hasta dónde se ve el Gantt.
3. Clic en **`Aceptar`**.

!!! tip "Si te quedás corto, ampliá sobre la marcha"
    Si armando el Gantt una barra se pasa de `FEC Fin Obra`, volvé a `Ver ▸ Propiedades` y ampliá esa fecha con el **botón de sugerencia**. Ninguna barra debe quedar fuera de la ventana. `[00:30]` `[00:50]`

---

## BLOQUE B — El diagrama de barras

## Tarea 4 — Abrir el diagrama de barras y dejar la visualización estándar

**Qué es:** configurar la ventana igual que el capacitador, porque la primera vez que la abrís es muy probable que la visualización no coincida.

**Paso a paso** `[00:30]`–`[00:50]`:

1. Menú **`Ver`** → interruptor **`Diagrama de barras`** (está al lado de `Fechas`).
2. En la barra de herramientas interna, abrí el menú **`Resúmenes`** (número de niveles/nodos abiertos) → marcá **`Planificadas`** → el árbol se despliega hasta el nivel de **partidas**.
3. En el selector de esquemas elegí **`Plan, fechas y holguras`** — el esquema estándar de trabajo, _"el que tradicionalmente se ve en otras aplicaciones distintas a Presto"_.
4. **Desmarcá** las subventanas inferiores de **mediciones**, **antecesores** y **sucesores** (los tres primeros botones del grupo de cuatro) para despejar la pantalla. Las de antecesores/sucesores las vas a reabrir en la Tarea 6.
5. **Mantené activo** el cuarto botón: el **marco del diagrama de barras** (si lo desmarcás, se cierra el área de las barras).
6. **Mantené activos** dos interruptores más: el botón **naranja `Fechas estimadas`** — es el que **dibuja las barras**; si lo apagás, desaparecen todas aunque haya duraciones — y el **visualizador de enlaces** (las flechitas). `[00:50]`
7. Ajustá la **escala temporal** con el menú de niveles **1–16**: nivel 1 = años; alrededor del 12 ya ves los días de la semana; en los más altos aparecen las **marcas rojas verticales** de los festivos. `[00:50]`–`[01:00]`

---

## Tarea 5 — Ingresar duraciones (`DURTOT`) — a mano o con la sugerencia del APU

**Qué es:** darle días a cada actividad. Es la columna que hace aparecer las barras.

**Paso a paso — a mano** `[00:30]`–`[00:40]`:

1. Columna **`DURTOT`** (su nombre real: relación DURTOT) = _"la duración estimada de la actividad en días"_. Parate en la celda de una partida (ej. excavaciones), digitá los días (ej. `15`) → ++enter++ → aparece la barra.
2. `DURTOT` **solo cuenta días laborables**: si entre el inicio y el fin caen festivos, no suman. Por eso la Tarea 1 va primero.
3. Columna **`FEC-I-PLAN`**: la fecha de inicio más temprana (ASAP). Se edita con el **botón de tres puntos** de la celda.
4. Columna **`FEC-F-PLAN`**: la fecha de fin más temprana. **Solo lectura** (fondo amarillo) = inicio + duración − festivos.
5. Las columnas **`FEC-IU-TOTAL`** / **`FEC-FU-TOTAL`** (fechas más tardías, ALAP) y las tres **holguras** (total, interna, libre) también son de solo lectura: las calcula Presto según la malla de enlaces. Se dejan calcular solas. `[00:40]`

**Paso a paso — con la sugerencia automática** `[02:00]`–`[02:10]`:

1. **Individual:** en la celda `DURTOT`, botón de **tres puntos** → Presto propone una duración.
2. **Masiva:** clic secundario en una celda `DURTOT` → comando **`Sugerir`** → llena las duraciones de todas las partidas que cumplen las condiciones. Si no sale a la primera, borrá y reintentá (_"si no te sale a la primera, borra y vuelve a intentar el sugerir"_).
3. **De dónde sale el número:** la partida debe tener en su **APU mano de obra** (o, en su defecto, **maquinaria**) con **unidad de tiempo hora o día**. Cálculo: rendimiento × cantidad de la partida ÷ horas por día. Ejemplo del video: `0,778 HH × 752 m³ ÷ 8 = ~73 días`.
4. El divisor `8` es el **factor hora→día** en `Ver ▸ Propiedades ▸ Tiempos` (default 8 h/día). Cambiarlo afecta la sugerencia pero **NO los importes del presupuesto**. `[02:00]`

!!! warning "Falla silenciosa — la sugerencia puede faltar o exagerar"
    Si la partida no tiene mano de obra/maquinaria en unidad de tiempo, **no hay sugerencia** y alguien puede teclear cualquier cosa sin base. Y cuando la hay, es solo un punto de partida: el propio relator baja una sugerencia de 73 días a un valor razonable de obra. _"Realmente si tú quieres colocar 100 días, te va a aceptar la duración."_ Revisá cada duración con criterio de obra. `[02:00]`–`[02:10]` _(C05 FS-6.)_

!!! note "Los tipos de actividad (clic secundario sobre la descripción)"
    - **`Resumen`** — engloba a sus hijas; su duración y fechas se calculan desde abajo y se ven en **magenta** (no se digitan). Capítulos y subcapítulos lo son por defecto.
    - **`Calculada`** — actividad con duración propia (las partidas, por defecto).
    - **`Hamaca`** — toma fecha y duración de su concepto superior; requiere **`Recalcular`**.
    - **`No planificada`** — saca el elemento del Gantt **sin borrarlo del árbol**. Es fácil marcarla por accidente y no notar que una partida desapareció del cronograma. Para revertir: pestaña `Árbol` → clic secundario → `Calculada`. `[01:00]`–`[01:20]`

---

## Tarea 6 — Crear los enlaces de precedencia (FC / FF / CC)

**Qué es:** encadenar actividades. En Presto, **"precedencia" = enlace**. `[01:30]`

**Paso a paso — enlace gráfico (barras cercanas)** `[01:00]`–`[01:10]`:

1. Acercá el cursor a la **porción final** de la barra antecesora hasta que tome forma de **cruz**.
2. **Clic izquierdo y arrastrá** hasta la **porción inicial** de la barra sucesora → soltá. Igual que en Project o Primavera.

**Paso a paso — enlace por comando (barras lejanas)** `[02:10]`:

1. En la **zona del árbol** (no sobre las barras), clic secundario sobre la descripción de la actividad → **`Crear precedencias`**.
2. En el diálogo, elegí **antecesor** o **sucesor** (botón de tres puntos) → seleccioná el otro elemento → `Aceptar`. **Solo enlaza de a uno** — no admite varios de golpe.

**Cambiar el tipo de enlace** `[01:10]`–`[01:20]`:

1. Reactivá las subventanas **`Antecesores`** / **`Sucesores`** (interruptores inferiores). Al marcar una actividad muestran el enlace con su código (ej. antecesor `A11`, superior `A1`).
2. En la columna **`Tipo`**, desplegá el menú: **`fin-comienzo`** (FC, el default), **`fin-fin`** (FF), **`comienzo-comienzo`** (CC) o **`doble`**.

**Borrar un enlace** `[01:50]`: clic sobre el enlace en el Gantt (queda punteado) → ++supr++ ; o en la subventana `Antecesores`/`Sucesores`, seleccionar la fila del enlace → ++supr++.

---

## Tarea 7 — Solapar actividades (sin romper el enlace)

**Qué es:** hacer que dos actividades enlazadas corran en paralelo unos días.

**Lo que NO se hace:** arrastrar la barra enlazada. Eso genera un **enlace negro** (inválido) y una **fecha en rojo** (bloqueada) — y Presto **no muestra ningún mensaje de error**. `[01:30]`

**Paso a paso — lo correcto** `[01:30]`–`[01:40]`:

1. Marcá la actividad **sucesora** → subventana **`Antecesores`** → ubicá la fila del enlace.
2. Si el enlace es de tipo **comienzo** (FC o CC): en la columna **`Solape`**, ingresá los días (ej. `-5` para adelantar la sucesora 5 días) → ++enter++. Las fechas siguen **flotantes**, nada se pone rojo.
3. Si el enlace es de tipo **fin** (FF): la columna `Solape` queda gris; usá la columna **`Solape tras`**.
4. Después de solapar, dale a **`Recalcular`** (menú `Inicio` o el acceso en la barra de título) para refrescar. `[01:20]` `[01:40]`

!!! warning "Falla silenciosa — arrastrar una barra enlazada rompe el cronograma sin aviso"
    El enlace queda **negro** (quebrado) y la fecha **roja** (bloqueada/inamovible), y no salta ningún error. Antes de dar por bueno un cronograma, barré el Gantt buscando **enlaces negros**. Para liberar una fecha roja: clic secundario sobre la celda → **`Fecha desbloqueada`**. `[01:30]` _(C05 FS-4.)_

!!! tip "Los colores del Gantt son metadato, no adorno"
    **Barra naranja** = partida (actividad calculada) · **barra verde/triangular** = resumen · **texto magenta** = valor calculado desde los hijos · **fecha roja** = bloqueada · **enlace negro** = inválido · **barras y enlaces rojos** = **ruta crítica** (¡no es error! son las actividades encadenadas a la que va en la delantera del cronograma) · **franjas rojas verticales** = festivos. `[00:50]`–`[01:50]`

---

## Tarea 8 — Limpiar el diagrama de barras de cero

**Qué es:** borrar todo (enlaces, duraciones, fechas bloqueadas) para rehacer el Gantt.

**Paso a paso** `[01:50]`:

1. **Borrar todos los enlaces:** menú **`Ver` → `Precedencias`** → se abre la tabla de todos los enlaces (antecesor, sucesor, tipo, solape). Clic en el **vértice fila/columna** (selecciona todo) → ++supr++. La tabla queda vacía.
2. **Borrar todas las duraciones:** en el diagrama de barras, seleccioná la columna **`DURTOT`** completa → ++supr++.
3. **Desbloquear las fechas rojas:** sobre una celda roja de `FEC-I-PLAN`, clic secundario → **`Fecha desbloqueada`**.

!!! tip "La tabla Precedencias también sirve para documentar"
    Antes de borrar (o en cualquier momento), la ventana `Precedencias` se puede **exportar a Excel** — la relación completa de enlaces del cronograma en una tabla. `[01:50]`

---

## Tarea 9 — Exportar el cronograma a MS Project o XML

**Qué es:** llevar el Gantt fuera de Presto, para reportar o para quien trabaje en Project/Primavera.

**Paso a paso** `[02:20]`:

1. Menú **`Archivo` → `Exportar`**. Dos opciones:

| Opción | Requiere | Qué lleva |
|---|---|---|
| **`Microsoft Project`** (binario) | Project **instalado** (si no, da error) | Tareas (resumen y calculadas), duraciones, fechas de comienzo/fin y la **hoja de recursos** |
| **`XML`** (Project / Primavera) | Nada instalado | Genera un `.xml` importable después |

!!! danger "Falla silenciosa — la exportación pierde el calendario"
    _"Los sábados y los domingos en esta exportación hacia Project siguen saliendo como feriados"_ — aunque en Presto los hayas dejado laborables. Quien planifique sobre ese export tendrá **duraciones erróneas** sin saberlo. Hay que entrar a las propiedades del calendario **en Project** y reconfigurar los sábados a mano. Regla de la casa: **Presto es el master del cronograma; Project/Primavera son solo salida de lectura.** `[02:20]`–`[02:30]` _(C05 FS-5.)_

---

## 🎥 Mirá el video

| Tema | Minuto |
|---|---|
| Módulo Planificación: qué hace, instancia de activación | `[00:00]` |
| Calendario: festivo/laborable, filtrar sábados, feriados a mano | `[00:00]`–`[00:20]` |
| Certificación actual en la primera fase | `[00:20]` |
| `FEC Inicio/Fin Obra` = ventana del Gantt | `[00:20]`–`[00:30]` |
| Configurar el diagrama de barras (Resúmenes, esquema, interruptores, escala) | `[00:30]`–`[01:00]` |
| `DURTOT`, `FEC-I-PLAN`, fechas ALAP y holguras | `[00:30]`–`[00:50]` |
| Tipos de actividad (resumen/calculada/hamaca/no planificada) | `[01:00]`–`[01:20]` |
| Enlaces: crear, tipos FC/FF/CC/doble, subventanas | `[01:00]`–`[01:20]` |
| Fechas bloqueadas, solapes, ruta crítica | `[01:30]`–`[01:50]` |
| Limpiar de cero (Precedencias) + sugerencia de duración | `[01:50]`–`[02:10]` |
| Armado libre + `Crear precedencias` + exportar a Project/XML | `[02:10]`–`[02:30]` |

> Video fuente: `Plan_10_12_2025.mp4` (3h 32min). Relator de soporte de Presto.

---

## ⚠️ Lo que Presto NO te avisa (resumen)

- **La certificación actual fuera de la primera fase** hace que el flujo de caja y los recursos no arranquen del día 1 — sin error visible. _(Tarea 2)_
- **Arrastrar una barra enlazada** deja un enlace negro inválido y una fecha bloqueada, sin mensaje. Solapá siempre por la columna `Solape`/`Solape tras`. _(Tarea 7)_
- **`No planificada` marcada por accidente** saca la partida del Gantt sin borrarla del árbol — y nadie lo nota. _(Tarea 5)_
- **La sugerencia de duración** falta o exagera según el APU; es un punto de partida, no una verdad. _(Tarea 5)_
- **La exportación a Project pierde el calendario** — los sábados laborables vuelven a ser feriados. _(Tarea 9)_

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá lo aprendido"
    Sobre la obra de prueba **BLEND** _(con una licencia que incluya el módulo Planificación, o la demo)_:

    1. En `Fechas ▸ Días`, dejá **todos los sábados laborables** usando `Filtrar por contenido` (¡y anulá el filtro!). Marcá a mano un feriado boliviano como `festivo`.
    2. Dejá la **primera fase** como `Certificación actual`.
    3. Abrí el `Diagrama de barras`, poné `Resúmenes ▸ Planificadas` y el esquema `Plan, fechas y holguras`.
    4. Corré el **`Sugerir`** masivo sobre `DURTOT` y revisá qué partidas quedaron sin sugerencia (¿su APU tiene mano de obra en horas?).
    5. Encadená 3 actividades con enlaces FC y **solapá** la última 5 días con `Solape = -5`.
    6. Exportá a **XML** y anotá qué le tendrías que corregir al calendario en destino.

    **Cómo sabés que salió bien:** las barras se dibujan de corrido incluyendo sábados, no hay **ningún enlace negro** ni fecha roja que no hayas puesto a propósito, y la ruta crítica se ve en rojo.

---

📖 **Fuentes:** transcripción `Plan_10_12_2025` · apuntes internos `06-planificacion.md` y `C05-modulo-planificacion-casos-uso.md` (casos 1–13).
