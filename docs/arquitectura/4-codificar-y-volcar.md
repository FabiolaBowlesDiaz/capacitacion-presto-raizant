# 4 · Codificar el modelo y volcar al presupuesto

!!! abstract "Conclusión primero"
    Hasta acá, Cost-It **creó un presupuesto desde el modelo**. Pero lo normal en Raizant es al revés: ya existe un **estudio** (presupuesto con sus partidas, APUs y precios) y querés **llenar esas partidas con las cantidades del modelo**. Para que eso funcione, el modelo tiene que llevar **los códigos de las partidas del presupuesto**. Esta página tiene las dos mitades: **(A)** entregar al modelador el **catálogo de códigos** para que codifique el modelo en Revit, y **(B)** **volcar** las cantidades al estudio con `Mediciones temporales → Importar → Asignar por código inferior → Traspasar`.

!!! tip "Antes de arrancar, tené a mano el mapa"
    Usamos `Ver ▸ Mediciones temporales` en Presto y `Gestionar ▸ Configuración adicional ▸ Código de montaje` en Revit. Si no los ubicás, abrí **[🗺 La pantalla de Arquitectura](interfaz.md)**.

!!! info "De dónde sale este contenido"
    Fuente principal: **documentación oficial de Presto (RIB)** — _Manual de Cost-it_ (pp. 5–6 catálogos, p. 17 Mediciones temporales) y _Un ejemplo de presupuesto y certificación con Revit y Presto_. Complemento: apunte **C01** (casos 13, 14) y la transcripción del video (minutos `[hh:mm]`).

---

## Por qué este orden importa

Pensalo como dos llaves que tienen que coincidir:

```
   PRESUPUESTO (estudio)            MODELO (Revit)
   partida 05.02 "Muro H21"   ⇄    elementos con código de montaje "05.02"
                              │
                  el código es la llave que une los dos
```

Si el modelo **no** lleva los códigos de las partidas del estudio, el volcado **no encuentra dónde poner las cantidades** y todo queda sin emparejar (gris). Por eso primero se **codifica el modelo** (Parte A) y recién después se **vuelca** (Parte B).

---

# Parte A — Codificar el modelo con las partidas del presupuesto

## Tarea 1 — Exportar el catálogo de códigos desde Presto

**Qué es:** generar, desde el estudio, un archivo con los códigos de las partidas para que Revit los use.

📖 **Fuente oficial:** Manual de Cost-it, pp. 5–6 — _"Los catálogos se generan desde Presto mediante 'Archivo: Exportar: Catálogo Revit'. El campo 'Descripción de montaje' o el campo 'Nota clave'… contienen la información ampliada del formato BC3."_

**Paso a paso** `[03:20]`–`[03:30]`:

1. En Presto, con el **estudio abierto**, andá a **`Archivo ▸ Exportar ▸ Catálogo Revit`**.
2. Elegí el formato **`código de montaje`** y exportá **desde el concepto raíz** (o acotado por capítulo). Genera un **archivo de texto tabulado**.
3. Entregá ese archivo al **modelador** (arquitectura).

!!! warning "Cuidado con los niveles de subcapítulos"
    El Manual avisa: _"En algunas versiones de Revit los elementos de los subcapítulos o niveles jerárquicos inferiores al quinto se insertan directamente bajo el concepto raíz. Si esto ocurre, **desglose el cuadro de precios en varios catálogos**, con menos niveles de subcapítulos."_ 📖 _(Manual de Cost-it, p. 5.)_ Si tu presupuesto tiene muchos niveles, partilo en varios catálogos.

---

## Tarea 2 — Cargar el catálogo en Revit y codificar los tipos

**Qué es:** que el modelador asigne a cada tipo del modelo el código de su partida.

📖 **Fuente oficial:** Manual de Cost-it, p. 6 (asignación por catálogo de códigos de montaje).

**Dónde estás:** en **Revit** (lo hace el modelador).

**Paso a paso** `[03:30]`:

1. En Revit: **`Gestionar ▸ Configuración adicional ▸ Código de montaje ▸ Examinar`** → seleccioná el archivo de texto del catálogo → **`Aceptar`**.
2. Para cada **tipo**: editar tipo → parámetro **`Código de montaje`** → botón **`…`** → elegir el código de la partida correspondiente (aparece como la estructura del presupuesto, agrupada por capítulos).
3. Como el código de montaje es **de tipo**, basta asignarlo a **un** elemento del tipo y queda en todos.

!!! note "Si se agregan partidas nuevas a mitad de proyecto"
    No se puede exportar **solo** las partidas nuevas: se **re-exporta el catálogo entero** (desde la raíz o acotado por capítulo) y, al reimportarlo en Revit, **sobreescribe conservando los valores anteriores y añadiendo los nuevos**. `[04:00]`

!!! warning "Para un parámetro de EJEMPLAR, el catálogo no alcanza"
    El catálogo de Revit sirve para parámetros **de tipo** (código de montaje). Si necesitás un parámetro **de ejemplar** (código distinto por elemento del mismo tipo), hay que buscar otra vía (p. ej. exportar los códigos a Excel y un plugin que los cargue en un parámetro creado al efecto). El soporte lo plantea como evaluación, no lo ejecuta — **confirmar el mecanismo con RIB** antes de comprometerlo. `[03:30]`

---

# Parte B — Volcar las cantidades al estudio

## Tarea 3 — Exportar el modelo codificado (filtrando lo no presupuestable)

**Qué es:** sacar del modelo ya codificado un archivo de Presto solo con lo que tiene código.

**Paso a paso** `[03:30]`–`[03:40]`:

1. En Revit, `Cost-It ▸ Exportar`. En **`Opciones`**, **desmarcá "incluir elementos sin código"** → así filtrás lo no presupuestable.
2. **`Exportar`** → guardá ese archivo de Presto y **cerralo**.

---

## Tarea 4 — Importar y asignar por código inferior

**Qué es:** traer las líneas de medición del modelo a la "sala de espera" del estudio y emparejarlas con las partidas.

📖 **Fuente oficial:** Manual de Cost-it, p. 17 (Mediciones temporales, Comprobar, Inserción).

**Dónde estás:** en **Presto**, con el **estudio abierto** (el presupuesto con APUs pero **sin cantidades** en las partidas principales).

**Paso a paso** `[03:40]`–`[03:50]`:

1. Menú **`Ver ▸ Mediciones temporales`** → se abre una ventana nueva, vacía.
2. Botón **`Importar`** → elegí el **archivo de Presto del modelo** (el de la Tarea 3) → la tabla se llena con **todas las líneas de medición** del modelo.
3. Seleccioná **toda la columna `Org Relación`** (clic en su cabecera) → clic derecho → **`Asignar unidad de obra ▸ por código inferior`**.
4. **Leé el resultado por color:**
   - Celdas **🟢 verdes** = encontraron **match** con una partida del árbol. ✅
   - Celdas **grises** = **sin coincidencia** (sobrantes, no presupuestables, o código mal puesto).

!!! danger "Las grises son tu alerta — no las ignores"
    Una línea **gris** es una cantidad del modelo que **no encontró su partida**. Si es un sobrante real, está bien; pero si era algo que **debía** presupuestarse, su código está mal y **quedó fuera del presupuesto en silencio** (falla silenciosa FS-5). Revisá las grises antes de traspasar.

---

## Tarea 5 — Traspasar (las cantidades pasan al árbol)

**Qué es:** mover definitivamente las cantidades emparejadas al presupuesto.

**Paso a paso** `[03:50]`:

1. _(Antes)_ Hacé **clic afuera** para no dejar nada seleccionado.
2. Botón **`Traspasar`** → la ventana de `Mediciones temporales` **se vacía** y las cantidades pasan al **árbol** y a la subventana `Mediciones`.
3. **Verificá:** el árbol ahora tiene cantidades en las partidas; el vínculo con el modelo persiste (seleccioná una partida → `seleccionar en el modelo` y se marcan los elementos).

!!! quote "La regla que lo gobierna todo"
    _"Aquí claramente fue clave el haberle pasado la codificación de las partidas en el proceso del catálogo de Revit."_ `[03:50]` — La **calidad del match depende 100% de haber codificado bien el modelo** (Parte A). Sin esa codificación, el volcado no empareja nada.

---

## El circuito completo, en una imagen

```
A. Presto: Archivo▸Exportar▸Catálogo Revit  ──►  archivo de códigos
                                                       │
B. Revit: Gestionar▸Código de montaje▸Examinar  ◄──────┘
          + asignar código a cada tipo
                                                       │
C. Revit: Cost-It▸Exportar (sin "elementos sin código")
                                                       │
D. Presto (estudio): Ver▸Mediciones temporales
          ▸ Importar ▸ Asignar por código inferior ▸ Traspasar
                                                       │
                                                       ▼
              Estudio con APUs + cantidades del modelo = presupuesto vivo
```

---

## 🎥 Mirá el video

| Tema | Minuto |
|---|---|
| Exportar catálogo de códigos desde Presto | `[03:20]`–`[03:30]` |
| Cargar catálogo y codificar tipos en Revit | `[03:30]` |
| Exportar modelo codificado (filtro sin código) | `[03:30]`–`[03:40]` |
| Mediciones temporales: Importar + Asignar por código inferior | `[03:40]`–`[03:50]` |
| Traspasar al árbol + verificar | `[03:50]` |
| Partidas nuevas a mitad de proyecto (re-exportar catálogo) | `[04:00]` |

> Video fuente: `CSE - Cost It - 23/01/2026.mp4`. _Complemento de la documentación oficial citada en cada tarea._

---

## ⚠️ Lo que Cost-It NO te avisa (resumen)

- **El match depende 100% de la codificación del modelo** → un código mal puesto manda la cantidad a la partida equivocada o a ninguna. _(Tarea 4)_
- **Las líneas grises (sin match) quedan fuera del presupuesto en silencio** → hay que revisarlas a mano. _(Tarea 4)_
- **No hay exportación selectiva de partidas nuevas** → se re-exporta el catálogo entero. _(Tarea 2)_

👉 Todas, con cómo blindarte, en [6 · Reglas de oro y fallas silenciosas](6-reglas-de-oro.md).

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá lo aprendido"
    _(Con un estudio de prueba que ya tenga partidas con APUs y un modelo codificado.)_

    1. Desde el estudio, `Archivo ▸ Exportar ▸ Catálogo Revit` desde la raíz. Abrí el archivo de texto y confirmá que están los códigos de tus partidas.
    2. Exportá el modelo codificado **sin** "elementos sin código".
    3. En el estudio: `Ver ▸ Mediciones temporales ▸ Importar` → `Asignar por código inferior`. Contá cuántas líneas salieron **🟢 verdes** (match) y cuántas **grises** (sin match).
    4. Revisá una gris: ¿es un sobrante real o un código mal puesto?
    5. `Traspasar` y comprobá que las partidas del árbol ahora tienen cantidades.

    **Cómo sabés que salió bien:** el estudio quedó con sus APUs **y** las cantidades del modelo, y podés saltar de cualquier partida al elemento en Revit.

---

📖 **Fuentes oficiales (RIB):** _Manual de Cost-it_, pp. 5–6 y 17 · _Un ejemplo de presupuesto y certificación con Revit y Presto_. · **Complementos internos:** apunte C01 (casos 13, 14) · transcripción `CSE - Cost It - 23/01/2026`.
