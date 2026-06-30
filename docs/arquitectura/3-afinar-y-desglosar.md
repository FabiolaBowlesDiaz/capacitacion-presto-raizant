# 3 · Afinar y desglosar

!!! abstract "Conclusión primero"
    Después del traspaso, algunas partidas salen **🟢 verdes**: tienen el mismo código pero **mezclan tipos distintos** (p. ej. dos clases de pilar en una sola partida), y cada tipo suele necesitar su propio precio (APU). Acá aprendés a **separarlas** — de dos formas: **a mano en Presto** (`Desglosar`) o, mejor, **antes de exportar desde Revit** (el **discriminador** y el **script del código**). También a **devolver** un valor de Presto al modelo, y a **guardar tu configuración** como plantilla para no rehacerla cada vez.

!!! tip "Antes de arrancar, tené a mano el mapa"
    Si no ubicás `Herramientas ▸ Desglosar`, la columna `Discriminador` o la pestaña `Script del código`, abrí **[🗺 La pantalla de Arquitectura](interfaz.md)**.

!!! info "De dónde sale este contenido"
    Fuente principal: **documentación oficial de Presto (RIB)** — _Manual de Cost-it_ (pp. 18–26) y _Personalización de la exportación de Revit_. Complemento: apunte **C01** (casos 8, 10, 11, 12) y la transcripción del video (minutos `[hh:mm]`).

---

## Por qué una partida sale verde (y por qué importa)

Recordá el **semáforo del resultado** ([Página 1](1-traspaso-inicial.md)): una partida **🟢 verde** tiene código, pero agrupa **elementos de tipos distintos**. Ejemplo típico: dos tipos de pilar (uno de 30×30, otro de 40×40) cayeron en la misma partida porque comparten código de montaje. El problema: cada tipo probablemente lleva un **APU (precio) distinto**, y mezclados no se pueden presupuestar bien.

Tenés **dos momentos** para separarlos:

| Cuándo | Cómo | Página |
|---|---|---|
| **Después** de exportar, en Presto | `Herramientas ▸ Desglosar` (Tarea 1) | esta |
| **Antes** de exportar, en Revit | Discriminador o script del código (Tarea 4) | esta |

> La regla práctica: si te pasa **una vez**, desglosá en Presto; si te pasa **siempre** en ese tipo de modelo, arreglalo **antes** con el discriminador para no repetir el trabajo manual.

---

## Tarea 1 — Desglosar una partida verde (en Presto)

**Qué es:** separar una partida con tipos mezclados en varias partidas, cada una de un solo tipo.

📖 **Fuente oficial:** Manual de Cost-it, p. 25 (Desglosar) · C01 caso 8.

**Dónde estás:** en **Presto**, sobre la partida 🟢 verde del árbol.

**Paso a paso** `[01:30]`–`[01:40]`:

1. _(Recomendado)_ Antes de separar, **editá el `Resumen`** de la partida verde a un **nombre genérico** (la descripción heredada de un tipo confunde cuando se separe).
2. Seleccioná la fila de la partida → menú **`Herramientas ▸ Desglosar`**.
3. Elegí el **criterio** por el que separás: una **columna** de la subventana de mediciones (p. ej. `Familia Tipo BIM`) **o** una **variable** importada de Revit. El cuadro te muestra abajo los **valores** que va a usar para separar (p. ej. los dos tipos de pilar).
4. Mantené marcado **"mover vínculos y huecos junto a sus líneas de medición principales"** → **`Aceptar`**.
5. La partida se separa en varias, **cada una con líneas de un solo tipo**.
6. Seleccioná los `Resumen` resultantes → clic derecho → **estado negro** (fondo blanco, texto negro) para **limpiar la marca verde**, que ya no aplica.

!!! note "El código del desglose lo arma Presto (y lo podés editar)"
    El código de cada partida nueva lo compone Presto (parte del código de montaje + parte del tipo). **No es personalizable desde el desglose**, pero **lo podés editar a mano** después, sin perder el vínculo con el modelo. `[01:30]`

---

## Tarea 2 — Devolver un valor de Presto al modelo (actualizar valores)

**Qué es:** escribir de vuelta en Revit un código o valor que cambiaste en Presto, para que quede en el modelo.

📖 **Fuente oficial:** Manual de Cost-it (actualizar valores en el modelo) · C01 caso 10. _(Requiere licencia full; la demo lo bloquea.)_

**Paso a paso** `[02:10]`:

1. En Presto, **clic derecho sobre la cabecera de una columna** → **`Insertar variables`** (en **conceptos**) → elegí el parámetro de Revit (p. ej. código de montaje). Aparece como columna con los valores del modelo.
2. **Cambiá el valor** en esa columna (p. ej. a `TEST001`). ⚠️ **No es en tiempo real**: cambiar la celda **no** actualiza el modelo solo.
3. **Clic derecho sobre la celda ▸ `Actualizar valores en el modelo`** (Presto → Revit). _(La opción inversa, `Actualizar valores desde el modelo`, es Revit → Presto.)_

!!! danger "Cuidado con el parámetro de tipo"
    Si el parámetro es el **código de montaje** (de tipo), cambiar uno **cambia todos los del tipo** → conflicto si querías códigos distintos. Para eso, usá un **parámetro de ejemplar** (individual por elemento). `[02:10]`

---

## Tarea 3 — Afinar cómo se mide cada categoría

**Qué es:** decidir, por categoría, en qué unidad sale la partida (área, volumen, longitud…) y sacar **dos mediciones** del mismo grupo si hace falta.

📖 **Fuente oficial:** Manual de Cost-it, pp. 9 y 31–32 (tipo de medición, duplicar categoría).

**Dónde estás:** pestaña **`Categorías`** de la ventana de exportación (en Revit).

**Paso a paso** `[02:40]`:

1. **Tipo de medición** (columna `Medida`): por cada categoría, elegí **`área` / `volumen` / `longitud` / `número` / `caja` / `personalizado`**. Define en qué unidad sale (p. ej. muros en m² **o** en m³).
2. **Duplicar categoría** (para sacar **dos** mediciones de los mismos elementos, p. ej. área **y** volumen): clic derecho sobre la celda de la categoría → **`duplicar categoría`**.

!!! warning "Al duplicar, ponele un código a cada copia"
    El fabricante lo pide: cuando duplicás una categoría, hay que **escribir algo en el `Código`** de cada copia para distinguirlas — pero ese código **se escribe desde la pestaña `Script del código`**, no en la celda directamente (Tarea 4). Si no, las dos copias se pisan. `[02:40]`

---

## Tarea 4 — El script del código y el discriminador (separar ANTES de exportar) ⭐

**Qué es:** dos herramientas para que las partidas salgan ya separadas y bien codificadas **desde Revit**, sin desglosar a mano después.

📖 **Fuente oficial:** Manual de Cost-it, pp. 18–26 (script del código, formato BC3 ampliado, discriminador) · _Personalización de la exportación de Revit_.

**Dónde estás:** pestaña **`Script del código`** y columna **`Discriminador`** de la ventana de exportación.

### 4a · El discriminador (lo más simple)

1. En la pestaña `Categorías`, escribí en la celda **`Discriminador`** el nombre de un parámetro de Revit (p. ej. `tipo`).
2. Cost-It genera **partidas ya separadas** por ese valor — hace el desglose **antes** de exportar. En el ejemplo, los dos tipos de pilar salen **ya en dos partidas**, sin tocar Presto. `[03:00]`

### 4b · El código ampliado (poner código, unidad, descripción y precio)

En la pestaña `Script del código` podés escribir un **código ampliado** con esta sintaxis (formato del registro `~C` del BC3):

```
código | unidad | descripción | precio
```

- Separador = **barra vertical** `|`. El **precio es opcional** (en Raizant suele venir del estudio, no del modelo).
- Ejemplo oficial: `Result = "E04AB040 | kg | ACERO CORRUGADO | 2,35";`
- 📖 _(Manual de Cost-it, p. 20.)_

### 4c · Filtro JavaScript (medir solo lo que cumple un criterio)

Para acotar el universo (p. ej. medir **solo** los muros de hormigón), Cost-It admite un pequeño **script en JavaScript**:

- `$[NombreDelParámetro]$` (entre corchetes-dólar) = el parámetro a evaluar.
- `Result = "código…"` = el código ampliado que se le asigna si cumple.
- **`null`** = **no medir / no exportar** ese elemento.
- `""` (vacío) = se mide con el código de defecto de `Opciones`.

!!! quote "Ejemplo oficial (de una línea)"
    ```
    $[Tipo]$ == "Partición interior" ? "E07P010" : ""
    ```
    Mide los de tipo "Partición interior" con el código `E07P010`, y el resto con el de defecto. 📖 _(Manual de Cost-it, p. 20.)_

!!! tip "Ayudas mientras escribís el script"
    El editor colorea para detectar errores: **verde** = comentario, **azul** = funciones del lenguaje, **magenta** = parámetros de Revit. 📖 _(Manual de Cost-it, p. 20.)_ El botón **`Evaluar todos`** valida el script antes de exportar; **`Sin colores`** acelera la escritura desactivando el coloreado. _El soporte de Presto **no enseña** JavaScript en sí — para casos complejos, apoyate en RIB o en el manual (botón `Ayuda`)._ `[02:50]`–`[03:00]`

---

## Tarea 5 — Guardar tu configuración como plantilla (`.CostItLayout`)

**Qué es:** conservar toda la configuración (categorías, medidas, scripts, discriminadores) para reutilizarla en el próximo proyecto.

📖 **Fuente oficial:** Manual de Cost-it, p. 10 y 16 (guardar/recuperar configuraciones).

**Paso a paso** `[03:10]`:

1. En la barra de la pestaña `Categorías`, pulsá el botón **disquet** (guardar) → poné un nombre → genera un archivo **`.CostItLayout`**.
2. Para reusarlo en otro modelo: botón **recuperar configuración** → elegí el `.CostItLayout`.

!!! note "Por qué esto vale oro para Raizant"
    Las plantillas `.CostItLayout` **versionadas como estándar** son lo que da **resultados reproducibles** entre proyectos y entre personas. Sin plantilla, cada quien rehace la configuración a mano cada vez (y con criterios distintos) → es la falla silenciosa FS-10. Definir las plantillas oficiales del equipo es parte del estándar BIM de Raizant.

---

## 🎥 Mirá el video

| Tema | Minuto |
|---|---|
| Desglosar partida verde + limpiar estado | `[01:30]`–`[01:40]` |
| Devolver valores de Presto a Revit | `[02:10]` |
| Tipo de medición + duplicar categoría | `[02:40]` |
| Script del código (ampliado + JavaScript) | `[02:50]`–`[03:00]` |
| Discriminador (separar antes de exportar) | `[03:00]`–`[03:10]` |
| Guardar `.CostItLayout` | `[03:10]` |

> Video fuente: `CSE - Cost It - 23/01/2026.mp4`. _Complemento de la documentación oficial citada en cada tarea._

---

## ⚠️ Lo que Cost-It NO te avisa (resumen)

- **Una partida verde se puede presupuestar con un solo APU** aunque mezcle tipos → el verde es advertencia, no freno. _(Tarea 1)_
- **Devolver un código de montaje cambia todos los del tipo** → conflicto silencioso. _(Tarea 2)_
- **Si no guardás el `.CostItLayout`, perdés la configuración** entre sesiones. _(Tarea 5)_

👉 Todas, con cómo blindarte, en [6 · Reglas de oro y fallas silenciosas](6-reglas-de-oro.md).

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá lo aprendido"
    1. Identificá una partida **🟢 verde** en el árbol. Antes de tocarla, renombrá su `Resumen` a algo genérico.
    2. `Herramientas ▸ Desglosar` por `Familia Tipo BIM`. Comprobá que se separó en varias partidas de un solo tipo y limpiá el estado a negro.
    3. Volvé a Revit y, en la pestaña `Categorías`, escribí un **discriminador** (`tipo`) en una categoría. Re-exportá y comprobá que ahora sale **ya separada**, sin desglosar a mano.
    4. Guardá la configuración como un `.CostItLayout` con un nombre claro (ej. `Raizant-base.CostItLayout`).

    **Cómo sabés que salió bien:** lograste el **mismo desglose** de dos maneras (a mano en Presto y automático con el discriminador) y tenés tu plantilla guardada.

---

📖 **Fuentes oficiales (RIB):** _Manual de Cost-it_, pp. 9–10, 16, 18–26, 31–32 · _Personalización de la exportación de Revit_. · **Complementos internos:** apunte C01 (casos 8, 10, 11, 12) · transcripción `CSE - Cost It - 23/01/2026`.
