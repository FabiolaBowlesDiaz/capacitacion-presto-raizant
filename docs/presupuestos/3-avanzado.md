# 3 · Presupuesto avanzado

!!! abstract "Conclusión primero"
    Acá aprendés a **sanear un presupuesto heredado** (lo más útil del día a día): detectar y corregir lo que hace que "los informes no sumen", consolidar APU, propagar precios desde un catálogo maestro, reclasificar costos por zona (Espacios) y usar expresiones. Es el módulo que te enseña a **certificar la calidad** del presupuesto antes de congelarlo.

!!! warning "Estado de esta página"
    Apunte de capacitación **CL-3 (Presupuesto Avanzado)**. ⚠️ Importante: de CL-3 **no tenemos capturas**, así que algunos nombres exactos de botones están tomados del audio y pueden variar en tu pantalla (van marcados `(?)`). El contenido y los procedimientos sí son fiables. Cada paso cita el minuto `[hh:mm]`.

---

## Primero: las 4 reglas de coherencia (la base de todo el saneamiento)

Si se violan, **Presto no avisa** pero los informes de recursos salen descuadrados:

| Regla | Qué significa |
|---|---|
| **Un capítulo/subcapítulo siempre tiene cantidad = 1** | Son títulos, no llevan cantidad. Si convertís un nodo a capítulo, su cantidad colapsa a 1. |
| **Todo recurso básico debe colgar de una PARTIDA** | Un material/MO/maquinaria nunca debe colgar directo de un subcapítulo. |
| **Un recurso con naturaleza partida NO suma como recurso** | Si un material quedó marcado como partida, descuadra los informes de recursos. |
| **Un concepto = un precio** | El mismo recurso compartido entre partidas tiene un único precio; tocarlo afecta a todas. |

!!! tip "Aprendé a leer los colores del precio (clave en este módulo)"
    **Negro** = precio base (tecleado). **Magenta** = calculado (tiene APU). **Rojo** = precio forzado a mano sobre algo que tenía APU → **bloqueado**, no recalcula. **Fondo gris** en una cantidad = cantidad **anulada** (no suma).

---

## Tarea 1 — Sanear la estructura del árbol

**Qué es:** corregir naturalezas mal asignadas en un presupuesto que recibiste (de Syneco, de un cliente, de otra obra).

**Método de revisión** `[00:00]`–`[00:20]`: en la pestaña `Árbol`, marcá sucesivamente los nodos **Capítulos / Subcapítulos / Partidas**. Al marcar **Partidas**, todos los subcapítulos deben abrirse y mostrar partidas. **Un subcapítulo que NO se abre es sospechoso** (tiene recursos básicos colgados directamente).

**Los 3 problemas típicos y su arreglo:**

1. **Un capítulo que en realidad era partida** (tiene recursos adentro): clic derecho → naturaleza `Partida`. ⚠️ Como un capítulo tenía cantidad 1, hay que **re-digitar la cantidad y unidad reales** desde un respaldo.
2. **Una partida mezclada con subcapítulos en el mismo nivel**: insertá una línea, hacela subcapítulo, y anidá la partida dentro con `Disminuir nivel`.
3. **Recursos básicos colgando de un subcapítulo**: convertí ese subcapítulo a `Partida` (una partida global con básicos es válida).

!!! tip "Truco de código para no romper la unicidad"
    Si creás un subcapítulo contenedor para una partida, dale el **mismo código + un carácter extra** (punto o guion). Presto exige códigos únicos, y el carácter extra evita el conflicto sin que se vea raro al imprimir.

---

## Tarea 2 — Corregir recursos con naturaleza partida

**Qué es:** cazar los recursos que por error tienen naturaleza partida y descuadran los informes de recursos (aparece un "ajuste de redondeo" enorme al final).

**Paso a paso** `[00:10]`–`[00:20]`:

1. Pestaña `Conceptos` → esquema **`Partidas mediciones`** (deja a la vista solo conceptos de naturaleza partida).
2. Buscá los que tengan el **precio en NEGRO** (una partida real lo tiene en magenta). Esos son sospechosos.
3. Clic derecho en el precio → **`Filtrar por color de texto`** (negro) → aísla todos.
4. A cada uno: devolvele su naturaleza correcta (material/MO/maquinaria), o armale su APU si de verdad era una subpartida.
5. **`Anular`** el filtro al terminar (no Ctrl+Z).

---

## Tarea 3 — Desbloquear un precio forzado (texto rojo)

**Qué es:** cuando alguien tecleó un precio sobre un concepto que tenía APU, el número queda **rojo** y bloqueado — `Recalcular` no lo toca.

**Paso a paso** `[00:20]`–`[00:30]`:

1. Clic derecho sobre el precio rojo → opciones **`desbloquear` / `bloquear`**.
2. Elegí **`desbloquear`** → el precio vuelve a magenta y recalcula desde su APU.

> Para cazarlos en masa: esquema `Partidas mediciones` → filtrar por color de texto rojo → corregir todos.

---

## Tarea 4 — Ajustar a un precio objetivo SIN contaminar otras partidas

**Qué es:** dejar una partida en un precio exacto, prorrateando hacia adentro, sin forzar el precio a mano (que dejaría rojo).

**Paso a paso** (`Herramientas → Ajustar`) `[00:30]`:

1. Botón `…` → seleccioná la partida.
2. Fijá el precio objetivo.
3. En la sección **`Cambiar`**, elegí el eje de prorrateo:

!!! danger "La regla de negocio dura"
    - Prorratear por **`Precio`** → si los recursos se comparten con otras partidas, **las arrastra** (porque "un concepto = un precio").
    - Prorratear por **`Cantidad`** → no toca precios → **no contamina** otras partidas.
    - **Si hay recursos compartidos, ajustá SOLO por Cantidad.**

El precio resultante queda en magenta (real). Reversible con Deshacer.

---

## Tarea 5 — Reducir niveles (consolidar el APU)

**Qué es:** colapsar los subanálisis intermedios para que el informe de APU muestre los recursos básicos directamente bajo la partida.

**Paso a paso** (`Herramientas → Reducir niveles`) `[00:40]`–`[01:00]`:

1. En `Relaciones`, dejá la máscara `*` (todos los niveles).
2. Marcá qué simplificar:
    - **`Auxiliares`** (recurso básico + calculado) → **seguro**, sube sus inferiores consolidando cantidades.
    - **`Partidas`** → ⚠️ ataca **TODO** concepto partida, incluidas las principales → **puede desarmar el presupuesto entero**.

!!! danger "No marques 'Partidas' a ciegas"
    Para consolidar solo subpartidas, reservá una **letra inicial** en su código (ej. `P`) y usá la máscara `P*`. Así consolida solo esas, sin tocar las partidas principales.

!!! tip "Validación: el total casi no debe cambiar"
    Tras reducir, la variación del total debe ser marginal (centavos). Si el total "explota" en millones, hay **cantidades anuladas** escondidas (ver Tarea 6).

---

## Tarea 6 — Detectar cantidades anuladas

**Qué es:** encontrar cantidades marcadas como "anuladas" (fondo gris, no suman) antes de reducir niveles, porque la anulación **no se hereda** y al reducir vuelven a sumar, distorsionando el total.

**Paso a paso** (ventana `Relaciones`) `[01:00]`–`[01:20]`:

1. Menú `Ver` → **`Relaciones`** → esquema **`Partidas y Auxiliares con Inferiores`**.
2. Buscá una celda `CanPres` con **fondo gris** → clic derecho → **`Filtrar por color de fondo`** → aísla todas las anuladas.
3. A cada una: **`Desanular`** (si debía sumar) o **`Eliminar`** (si de verdad no va).
4. Anulá el filtro al terminar.

---

## Tarea 7 — Actualizar desde un catálogo maestro

**Qué es:** volcar precios/descripciones/APU actualizados desde un archivo de obra de referencia (un "Presto maestro" de precios) hacia tu presupuesto.

**Paso a paso** (`Herramientas → Actualizar`) `[01:20]`–`[01:40]`:

1. Campo `Desde`: botón `…` → seleccioná el archivo de referencia (no hace falta abrirlo).
2. Elegí qué actualizar: todo, o con máscara (ej. `M*` = solo materiales), o lo seleccionado.
3. `Aceptar` → actualiza los conceptos cuyo código exista en la referencia.

!!! warning "Qué es y qué NO es Actualizar"
    - **Solo toca** conceptos cuyo código exista en la referencia (los demás no se tocan).
    - Si la referencia trae un APU distinto para el mismo código, **reemplaza el APU completo**.
    - **No es en tiempo real** — hay que re-ejecutarla cada vez.
    - **NO es un comparador ni un congelado de baseline**: sobrescribe sin guardar la versión previa (salvo Deshacer). El congelado de baseline es tejido in-house.

---

## Tarea 8 — Espacios: costos por zona o fase

**Qué es:** una clasificación paralela de los costos por zona/sector/fase (ejes, losas, plantas), **sin alterar** la estructura del presupuesto.

**Cómo funciona** `[01:40]`–`[02:20]`: la **única vinculación** presupuesto↔espacios es la columna **`Espacio` de las líneas de medición**. Creás espacios (`SPC0010`, `SPC0020`…), les ponés nombre (Ejes, Losas), y asignás cada línea de medición a su espacio. Después Presto calcula el monto y los recursos por espacio.

!!! note "Conexión con Revit"
    El dato `Espacio` se puede poblar automáticamente desde Revit (vía Cost-It), mapeado al parámetro de niveles del modelo. Límite: 10.000 espacios.

---

## Tarea 9 — Expresiones (columnas de usuario y filtros)

**Qué es:** crear columnas calculadas propias y filtros con fórmulas de Presto.

> Para las expresiones, cada naturaleza se referencia por **número**: Otros=9, Material=8, Maquinaria=7, Mano de obra=6, Partida=5, Capítulo=4. `[02:50]`

Se usa en `Inicio → Insertar columna de usuario` y `Inicio → Filtro por expresión`. _(El detalle de la sintaxis de expresiones se amplía con las capturas pendientes.)_

---

## 🎥 Mirá el video

| Tema | Minuto |
|---|---|
| Saneamiento de estructura | `[00:00]`–`[00:20]` |
| Recursos con naturaleza partida / precios rojos | `[00:20]`–`[00:40]` |
| Reducir niveles + cantidades anuladas | `[00:40]`–`[01:20]` |
| Actualizar desde maestro | `[01:20]`–`[01:40]` |
| Espacios | `[01:40]`–`[02:20]` |
| Expresiones | `[02:20]`–`[03:00]` |

> Video fuente: `CL-3 - Ppto Avanzado - Lunes 01_12_2025.mp4` (3h 03min).

---

## ⚠️ Lo que Presto NO te avisa (resumen)

- **Recurso con naturaleza partida** → no suma como recurso, descuadra informes en silencio.
- **Precio forzado a mano (rojo)** → queda bloqueado, no recalcula.
- **Cantidades anuladas** → al reducir niveles, vuelven a sumar y el total "explota".
- **Reducir niveles marcando 'Partidas'** → puede desarmar el presupuesto entero.
- **Ajustar por precio con recursos compartidos** → contamina otras partidas.
- **Actualizar no es baseline** → sobrescribe sin guardar la versión previa.

👉 Todas en [5 · Reglas de oro y fallas silenciosas](5-reglas-de-oro.md).

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá lo aprendido"
    Sobre la obra de prueba **BLEND**:

    1. En la pestaña Árbol, recorré Capítulos/Subcapítulos/Partidas y encontrá algún subcapítulo que no se abra (recursos colgados directo).
    2. En `Conceptos → Partidas mediciones`, filtrá por color de texto negro y revisá si hay recursos con naturaleza partida mal puesta.
    3. Probá `Ajustar` una partida a un precio objetivo **por Cantidad** y verificá que el precio quede en magenta.

    **Cómo sabés que salió bien:** ningún informe de recursos muestra un "ajuste de redondeo" enorme al final.

---

📖 **Fuente oficial:** Expresiones-campos-de-usuario-funciones-y-filtros.pdf · Uso-de-las-variables-personalizadas.pdf · Coste-de-objetos-y-coste-de-procesos.pdf · Calculo-de-precios-por-produccion.pdf (RIB). · Apunte: C04 — Presupuesto avanzado (casos de uso 1–9, basado en audio).
