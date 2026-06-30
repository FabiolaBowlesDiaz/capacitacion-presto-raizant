# 1 · Armar la línea temporal (las fases de certificación)

!!! abstract "Conclusión primero"
    Antes de certificar nada, la obra necesita un **calendario de fases**: las fechas en que se va a cortar el avance para cobrar (normalmente, fin de cada mes). Un archivo de Presto **no trae línea temporal por defecto** — hay que crearla. Acá aprendés a fijar la **fecha de inicio**, **generar las fechas de certificación** de un saque, y **ajustar** las que caigan en día no laborable. Es un paso de **setup** que se hace una vez al arrancar la obra (lo suele hacer quien arma el presupuesto).

!!! tip "Antes de arrancar, tené a mano el mapa"
    Las instrucciones usan palabras como _"la pestaña `Fechas`"_, _"el esquema `Días`"_, _"la columna `NatC`"_. Si algo no lo ubicás, abrí en otra pestaña **[🗺 La pantalla de Control de obra](interfaz.md)** — es el mapa de las pestañas `Fechas` y `Árbol`. Volvé a él cuando te pierdas.

!!! warning "Requisito de licencia"
    Las fases de certificación viven en el módulo **Gestión de Proyectos**. Si tu licencia no lo incluye, la herramienta `Crear fechas de certificación` aparece inhabilitada (podés seguir el manual con la versión demo). Verificá que el módulo esté incluido antes de operar.

!!! info "De dónde sale este contenido"
    Fuente principal: **documentación oficial de Presto (RIB)** — _Certificación y seguimiento_ (cap. Fases de certificación, p. 3). Se complementa con el apunte interno **C08** y la transcripción del video **`gestion_de_proyectos_09_12_2025`** (de ahí salen los minutos `[hh:mm]` y la ruta de clic exacta). Cada tarea cita su fuente. Si la doc y el video chocan, gana la doc.

---

## ¿Qué es una "fase" y por qué importa?

> 📖 **Fuente oficial:** _Certificación y seguimiento_ (RIB), p. 3 — _"La certificación se realiza por fases o períodos financieros, que pueden ser meses o cualquier otro plazo de tiempo."_

Una **fase** es el período entre dos fechas de certificación (normalmente, un mes). Cada vez que cierra una fase, se certifica el avance de ese período para cobrarlo. Las fases son la **columna vertebral del tiempo** de la obra: sin ellas no hay certificación, no hay estados de pago y no hay curvas S.

---

## Tarea 1 — Fijar la fecha de inicio de la obra

**Qué es:** decirle a Presto cuándo arranca la obra. De esa fecha cuelga todo el calendario.

**Dónde estás:** en la ventana de **`Propiedades`** del archivo.

**Paso a paso** `[00:00]`:

1. Andá a la **cinta de arriba**, pestaña **`Ver`**, y abrí la ventana **`Propiedades`**.
2. Buscá la sección **`Tiempos`**.
3. Localizá el parámetro **`FEC Inicio Obra`** (es _"el inicio de las actividades sin precedencias y la visualización del diagrama de barras"_).
4. Fijalo en el **primer día real de la obra** (ej. `01/12/25`).
5. Hacé clic en **`Aceptar`**.

!!! note "Por qué conviene hacerlo primero"
    Esta fecha será la **propuesta por defecto** cuando crees la línea temporal en la Tarea 2. Si las dos coinciden, el calendario arranca prolijo. El capacitador insiste: _"Eso siempre hay que establecerlo, siempre hay que establecerlo."_ `[00:00]`

---

## Tarea 2 — Crear las fechas de certificación (generar las fases)

**Qué es:** generar de un saque todo el calendario de fechas de cierre de la obra.

📖 **Fuente oficial:** _Certificación y seguimiento_ (RIB), p. 3 (Fases de certificación). El cómo operativo (la herramienta y sus campos) sale del video.

**Pre-chequeo — confirmá que falta la línea temporal:**

1. Andá a la pestaña **`Ver`** → activá el **botón `Fechas`** → se abre la pestaña `Fechas`.
2. Si el archivo **no tiene** línea temporal, la pestaña aparece **vacía** y no te deja hacer clic en nada. Eso confirma que hay que crearla. `[00:10]`

**Paso a paso para crearla** `[00:10]`–`[00:20]`:

1. Andá a la **cinta de arriba**, pestaña **`Procesos`**, y hacé clic en **`Crear fechas de certificación`**.
2. Se abre un diálogo con cuatro campos. Llenálos así:

| Campo | Qué poné | Ejemplo |
|---|---|---|
| **`Día inicial`** | Ya viene con la `FEC Inicio Obra`. Dejalo. | `01/12/25` |
| **`Número de meses`** | Cuánto dura la obra (proyectá de más, mejor que falten). | `15` |
| **`Día de certificación`** | El día del mes que será fecha de corte (1–31). | `31` (= fin de mes) |
| **`Añadir todos los días del mes`** | Marcá esta casilla (viene desmarcada). | ✅ marcada |

3. Hacé clic en **`Aceptar`**. La pestaña `Fechas` **se llena con una tabla**: un calendario con el último día de cada mes marcado con el **ícono de fase** (el "€"). ✅

!!! tip "Presto ajusta solo los meses de 30 días y febrero"
    Aunque pongas `31` como día de certificación, Presto entiende que abril tiene 30 y febrero 28/29: ajusta la fecha al último día real de cada mes. No tenés que hacer nada.

!!! warning "Falla silenciosa — el calendario corto"
    Si la obra **dura más** que el `Número de meses` que pusiste, te van a **faltar fases** para certificar al final. No es grave: **la herramienta se puede volver a correr** con más meses (no es de un solo uso). El capacitador lo aclara: _"¿esta herramienta se aplica una vez y después no? No."_ Por las dudas, proyectá de más. _(C08 FS-5, video `[00:10]`–`[00:20]`.)_

---

## Tarea 3 — Inspeccionar el calendario (esquema `Días`)

**Qué es:** mirar el calendario día por día para entender qué generó Presto.

**Paso a paso** `[00:20]`:

1. En la pestaña `Fechas`, abrí el **menú de esquemas** y elegí **`Días`** (está más abajo en la lista).
2. La vista cambia a **una fila por día**.

**Cómo leer las columnas:**

- **`NatC`** (naturaleza): los íconos numéricos **1 a 7 = días de la semana** (lunes a domingo, que se repiten).
- **`Dia`**: el mismo día de la semana en letra (L/M/X/J/V/S/D).
- El **ícono "€"** sobre `NatC` = **fecha de certificación** (fin de fase). **No es la moneda euro.**
- Las fechas de certificación se ven **en color**: la **certificación actual es naranja**, las demás grises.

---

## Tarea 4 — Mover una fecha que cayó en día no laborable

**Qué es:** correr una fecha de certificación cuando cae sábado, domingo o feriado.

**Por qué:** la herramienta marca mecánicamente (ej. todos los "31") sin saber si es día hábil. Vos hacés el ajuste fino.

**Concepto — los tres estados de una fecha** (clic derecho sobre su celda `NatC`):

- **`No certificación`** — fecha común, sin ícono.
- **`Certificación`** — fecha de cierre de fase (con ícono "€").
- **`Certificación actual`** — la fase vigente (naranja). _(Esta la usás en la Tarea siguiente.)_

**Ejemplo del video — el 31-ene cae sábado, pasarlo al 30-ene** `[00:30]`–`[00:40]`:

1. Parate en el **30-ene** (que está en `No certificación`) → **clic derecho** sobre su celda `NatC` → elegí **`Certificación`**. Aparece el ícono "€".
2. Parate en el **31-ene** (que está en `Certificación`) → **clic derecho** → elegí **`No certificación`**. Desaparece el ícono.

> El capacitador lo resume: _"Es solo un cambio de estatus con este clic secundario."_ `[00:40]`

!!! tip "Crear una fase intermedia extra"
    ¿Necesitás un corte adicional fuera del calendario mensual? Parate en **cualquier** fecha → clic derecho → `Certificación`. Se crea una fase nueva entre las existentes. `[00:40]`

!!! danger "Falla silenciosa — las fechas NO se mueven solas con el calendario de Windows"
    Marcar fechas y, sobre todo, mover la "certificación actual" es **100% manual**. Presto **nunca** avanza la fase solo según la fecha del sistema. _"En ningún caso se va a ir moviendo solo según el calendario de Windows."_ Acordate de gestionarlo vos cada cierre. _(C08 FS-3 / FS-4, video `[00:40]`.)_

---

## 🎥 Mirá el video

| Tema | Minuto |
|---|---|
| Fijar `FEC Inicio Obra` en Propiedades | `[00:00]` |
| Pestaña Fechas vacía + crear fechas de certificación | `[00:10]` |
| Campos del diálogo (meses, día de certificación) | `[00:10]`–`[00:20]` |
| Esquema `Días`, leer NatC / ícono € / colores | `[00:20]`–`[00:30]` |
| Mover una fecha (clic derecho, 3 estados) | `[00:30]`–`[00:40]` |

> Video fuente: `gestion_de_proyectos_09_12_2025.mp4` (2h 03min). Relator de soporte de Presto. _El video es complemento: la referencia primaria es la documentación oficial citada en cada tarea._

---

## ⚠️ Lo que Presto NO te avisa (resumen)

- **El calendario corto** te deja sin fases al final → proyectá de más; la herramienta se puede re-ejecutar. _(Tarea 2)_
- **Las fechas auto-generadas caen en días no laborables** → ajustalas a mano. _(Tarea 4)_
- **Las fases no se mueven solas** con el reloj de Windows → la gestión es manual. _(Tarea 4)_

👉 Todas, con cómo blindarte, en [5 · Reglas de oro y fallas silenciosas](5-reglas-de-oro.md).

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá lo aprendido"
    Sobre la obra de prueba **BLEND** _(con una licencia que tenga Gestión de Proyectos)_:

    1. En `Ver ▸ Propiedades ▸ Tiempos`, fijá `FEC Inicio Obra` en el primer día de la obra.
    2. Con `Procesos ▸ Crear fechas de certificación`, generá **12 meses** con día de certificación **30**.
    3. Pasate al esquema `Días` y encontrá la primera fecha de certificación (la naranja).
    4. Tomá una fecha que caiga en fin de semana y **movela** al viernes anterior (clic derecho → `Certificación` en el viernes; `No certificación` en el sábado).

    **Cómo sabés que salió bien:** la pestaña `Fechas` muestra una fila por día, con el ícono "€" en los fines de mes, y la fecha que moviste cambió de lugar.

---

📖 **Fuente oficial (RIB):** _Certificación y seguimiento_ — cap. Certificación / Fases de certificación, p. 3. **Complemento interno:** apunte C08 (casos 1–5) · transcripción `gestion_de_proyectos_09_12_2025`.
