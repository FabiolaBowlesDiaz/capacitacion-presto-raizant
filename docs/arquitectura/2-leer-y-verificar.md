# 2 · Leer y verificar el resultado

!!! abstract "Conclusión primero"
    El modelo ya está en Presto, pero **no todas las cantidades nacen iguales**. Cost-It a veces **calcula** la cantidad (la pinta de **🟣 magenta**) y a veces **copia la del modelo tal cual** (la pinta de **⚫ negra**) — y eso depende de la **regla del 2%**. Una cantidad negra es una **señal de revisar**. En esta página aprendés a leer ese color, a saltar de una partida al elemento en el modelo (y vuelta) para verificar, y qué cambia cuando trabajás con un **modelo central/federado**.

!!! tip "Antes de arrancar, tené a mano el mapa"
    Usamos los esquemas de la subventana `Mediciones` (`Datos generales`, `Prest Dimensiones`, `Localización BIM`). Si no los ubicás, abrí **[🗺 La pantalla de Arquitectura](interfaz.md)**.

!!! info "De dónde sale este contenido"
    Fuente principal: **documentación oficial de Presto (RIB)** — _Manual de Cost-it_ (pp. 14–16). Complemento: apunte **C01** (casos 6, 7, 9) y la transcripción del video (minutos `[hh:mm]`).

---

## La regla del 2%, explicada de una vez

Cada elemento del modelo está rodeado por un **prisma** imaginario: una caja con sus dimensiones (`N`, `Longitud`, `Anchura`, `Altura`). Cost-It puede **calcular** la cantidad multiplicando esas dimensiones, **o** puede usar la cantidad que el modelo declara directamente. ¿Cómo decide? Con la **regla del 2%**:

!!! quote "La regla, palabra por palabra del Manual"
    _"Si el resultado de operar las dimensiones difiere en más del 2% de esta cantidad, las dimensiones se transfieren anuladas; en otro caso se toma el resultado de la operación."_ 📖 _(Manual de Cost-it, p. 15)_

En cristiano:

- Si el **prisma calculado** se parece (≤ 2% de diferencia) a la **cantidad del modelo** → Cost-It **calcula** la cantidad y la pinta **🟣 magenta**.
- Si **difiere más del 2%** (el objeto tiene geometría rara: huecos, recortes, mochetas) → Cost-It **usa la cantidad declarada del modelo** y la pinta **⚫ negra**, dejando las dimensiones "anuladas" (a título informativo).

!!! example "El ejemplo del propio Manual (muy claro)"
    Un muro de **12,00 m²**, 3,00 m de longitud:

    - Si la altura es **4,00 m** → 3,00 × 4,00 = 12,00 m². Coincide → los tres datos viajan, cantidad **🟣 magenta**.
    - Si la altura es **4,05 m** → 3,00 × 4,05 = 12,15 m². Difiere **menos** del 2% → se toma 12,15, **🟣 magenta**.
    - Si la altura es **4,50 m** → 3,00 × 4,50 = 13,50 m². Difiere **más** del 2% → se mantiene **12,00 m²** (la del modelo) y las dimensiones se anulan → cantidad **⚫ negra**.

    📖 _(Manual de Cost-it, p. 15.)_

!!! warning "La regla del 2% es FIJA del fabricante — no se configura"
    No hay una casilla para cambiar ese 2%. _"Es algo predeterminado, determinado por el fabricante del software."_ `[01:40]`. Lo que sí podés hacer es **forzar el valor BIM exacto** en un caso puntual (Tarea 3).

---

## Tarea 1 — Leer el color de la cantidad (magenta vs negra)

**Qué es:** mirar cada línea de medición y entender de dónde salió su cantidad.

📖 **Fuente oficial:** Manual de Cost-it, p. 15 (líneas de medición, dimensiones anuladas).

**Dónde estás:** subventana **`Mediciones`**, esquema **`Datos generales`** (el que muestra `Cantidad`, `N`, `Longitud`, `Anchura`, `Altura`).

**Paso a paso** `[01:40]`:

1. Seleccioná una partida en el árbol y mirá abajo sus **líneas de medición**.
2. Mirá el **color de la celda `Cantidad`**:
   - **🟣 Magenta** = la calculó Cost-It desde el prisma (las dimensiones cuadran). Confiable.
   - **⚫ Negra** = la copió del modelo tal cual (el prisma no representaba bien al objeto). **Revisala.**
3. Mirá las celdas de dimensión (`Longitud`/`Anchura`/`Altura`):
   - **Blanca** = esa dimensión **participa** del cálculo.
   - **Gris** = esa dimensión está **anulada** (declarada pero no usada). _Clic derecho sobre la celda gris te muestra el estado "anulado"._

!!! note "Por qué te importa una cantidad negra"
    Una cantidad **negra** te está diciendo: "el prisma de este objeto no coincidió con su cantidad real" → puede esconder una geometría irregular, un hueco mal definido o un recorte. **No es necesariamente un error**, pero **es un dato a auditar** antes de confiar en él para el presupuesto.

---

## Tarea 2 — Saltar de la partida al elemento en el modelo (y vuelta)

**Qué es:** verificar visualmente que una partida agrupa los elementos correctos.

📖 **Fuente oficial:** Manual de Cost-it, p. 28 (Localizar) · C01 caso 7.

**Paso a paso** `[01:00]`–`[01:10]`:

**De Presto a Revit** _(¿qué elementos tiene esta partida?)_:

1. En Presto, seleccioná una **línea de medición** (o varias con Ctrl, o el título de la partida, o el capítulo entero).
2. **Clic derecho ▸ `seleccionar en el modelo`**. Revit marca esos elementos.
3. En Revit, usá **"aislar elementos"** para verlos solos, y **"editar tipo"** para confirmar el valor del parámetro agrupador.

**De Revit a Presto** _(¿a qué partida fue este elemento?)_:

1. En Revit, **marcá un elemento**.
2. Pasá a la cinta **`Cost-It` ▸ botón `Localizar`**.
3. Presto **salta** a la partida/línea de ese elemento.

!!! tip "Dato tranquilizador: el vínculo nunca se rompe"
    Aunque después renombres, recodifiques, muevas o reestructures la partida en Presto, **el vínculo con el modelo no se pierde**. _"Por mucho que reestructures lo que es el Presto… la interacción esta no se pierde."_ `[01:10]`. Podés ordenar tu presupuesto con total libertad sin miedo a perder la trazabilidad con Revit.

---

## Tarea 3 — _(Opcional)_ Forzar el valor BIM exacto en una cantidad negra

**Qué es:** reemplazar una cantidad negra (declarada) por el valor BIM exacto del modelo, cuando lo preferís.

📖 **Fuente oficial:** Manual de Cost-it, p. 16 (medición de usuario / cantidad calculada vs declarada).

**Dónde estás:** el valor BIM exacto viaja siempre a Presto en el esquema **`Prest Dimensiones`** (columnas `BIM Long`, `BIM Sup`, `BIM Volumen`, `BIM Peso`).

**Paso a paso** `[01:50]`:

1. En la subventana `Mediciones`, hacé visible la columna del valor exacto que querés (p. ej. `BIM Sup`) usando **`Elegir columnas visibles`**.
2. **Copiá** (++ctrl+c++) el valor de `BIM Sup` y **pegalo** (++ctrl+v++) sobre la celda `Cantidad` de esa línea.
3. La cantidad **deja de estar magenta**: Presto entiende que anulás las dimensiones del prisma y usás el valor pegado.
4. Si te arrepentís, **Deshacer** (++ctrl+z++) lo revierte.

!!! note "Cuándo hacer esto"
    Solo cuando el presupuestador decide que para esa partida el **valor BIM exacto** es mejor que la cantidad declarada. No es un paso de rutina — es una corrección puntual, caso por caso.

---

## Tarea 4 — Trabajar con un modelo central/federado (la columna `Archivo`)

**Qué es:** entender qué cambia cuando el modelo abierto reúne varios Revit vinculados (lo normal en proyectos ejecutivos, con un modelo por disciplina).

📖 **Fuente oficial:** Manual de Cost-it (modelos vinculados) · C01 caso 9.

**Hechos clave** `[01:50]`–`[02:00]`:

1. **La exportación SÍ funciona** sobre un modelo central: trae todos los elementos con sus categorías.
2. Presto **registra de qué archivo vino cada línea**: esquema **`Localización BIM`** → columna **`Archivo`** (además de coordenadas X/Y/Z, planta, ejes, habitación).
3. **PERO**: por un límite de la API de Revit, **`seleccionar en el modelo` y `Localizar` NO funcionan** sobre el central. _"Es una limitante de la API de Revit que eso no se pueda hacer con el central."_ `[02:00]`

!!! warning "Cómo verificar en un modelo central"
    Si necesitás ver visualmente un elemento de un modelo central, **abrí el archivo Revit individual** que indica la columna **`Archivo`** y verificalo ahí. Conservá siempre el esquema `Localización BIM` para no perder ese rastro. Sin esto, la verificación visual "falla" sin error claro (es la falla silenciosa FS-8).

---

## 🎥 Mirá el video

| Tema | Minuto |
|---|---|
| Seleccionar partida ↔ modelo (bidireccional) | `[01:00]`–`[01:10]` |
| Cantidades magenta vs negra (regla 2%) | `[01:40]` |
| Forzar el valor BIM exacto (copiar/pegar `BIM Sup`) | `[01:50]` |
| Modelo central, columna `Archivo`, límite de la API | `[01:50]`–`[02:00]` |

> Video fuente: `CSE - Cost It - 23/01/2026.mp4`. _Complemento de la documentación oficial citada en cada tarea._

---

## ⚠️ Lo que Cost-It NO te avisa (resumen)

- **Una cantidad negra parece confiable pero es la declarada, no la calculada** → puede esconder geometría irregular. _(Tarea 1)_
- **En modelo central, `seleccionar`/`Localizar` no marcan nada** y no hay error claro → hay que abrir el archivo individual. _(Tarea 4)_

👉 Todas, con cómo blindarte, en [6 · Reglas de oro y fallas silenciosas](6-reglas-de-oro.md).

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá lo aprendido"
    Sobre el árbol que generaste en la [Página 1](1-traspaso-inicial.md):

    1. Entrá a una partida de muros y mirá sus líneas de medición: contá cuántas cantidades están **🟣 magenta** y cuántas **⚫ negras**.
    2. Elegí una línea **magenta**: clic derecho ▸ `seleccionar en el modelo` y confirmá en Revit que se marcó el muro correcto.
    3. Elegí una línea **negra** (si hay): hacé visible `BIM Sup` y compará la cantidad declarada con el valor BIM exacto.
    4. _(Opcional)_ Forzá el valor BIM exacto en esa línea negra y comprobá que deja de estar magenta; después **Deshacé**.

    **Cómo sabés que salió bien:** entendés, partida por partida, **por qué** cada cantidad es magenta o negra, y podés saltar al modelo a verificar cualquiera.

---

📖 **Fuentes oficiales (RIB):** _Manual de Cost-it_, pp. 14–16 y 28. · **Complementos internos:** apunte C01 (casos 6, 7, 9) · transcripción `CSE - Cost It - 23/01/2026`.
