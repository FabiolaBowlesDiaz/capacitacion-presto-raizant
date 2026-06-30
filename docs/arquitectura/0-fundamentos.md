# 0 · Fundamentos de Cost-It

!!! abstract "Conclusión primero"
    Cost-It traduce tu **modelo de Revit** en un **presupuesto de Presto**. La regla de oro que cambia todo: con Cost-It, **el presupuesto deja de tener cantidades tecleadas a mano — pasa a ser un cálculo derivado del modelo.** Cada muro, cada ventana, cada pilar que dibujás aporta su cantidad. Entender **cómo se traduce** Revit a Presto, y qué **no** hace Cost-It por vos, es lo que evita que el presupuesto salga mal sin que nadie lo note.

!!! tip "Antes de arrancar, tené a mano el mapa"
    Esta página usa palabras como _"capítulo"_, _"línea de medición"_, _"el árbol de Presto"_. Si algo no lo ubicás, abrí en otra pestaña **[🗺 La pantalla de Arquitectura](interfaz.md)**.

!!! info "De dónde sale este contenido"
    Fuente principal: **documentación oficial de Presto (RIB)** — _Manual de Cost-it_ y _Cost-it (BIM 5D con Presto)_. Se complementa con el apunte interno **C01** y la transcripción del video **`CSE - Cost It - 23/01/2026`** (de ahí salen los minutos `[hh:mm]`, para lo que el video muestra y la doc no detalla).

---

## 1. Qué es Cost-It y dónde encaja

Cost-It es el **módulo puente Revit → Presto** — lo que en la industria se llama **5D BIM** (las tres dimensiones del modelo + tiempo + **costo**). Toma las cantidades de todos los elementos de un modelo 3D y las lleva a Presto, **estructuradas como partidas de un presupuesto**.

> _"El módulo que se encarga de traspasar la información de las cantidades de todos los elementos que están en un modelo 3D hacia el Presto… hacia las partidas principales del presupuesto."_ `[00:00]`

Dos hechos básicos que conviene fijar:

1. **Cost-It corre DENTRO de Revit** (es un complemento/plugin de Revit), aunque genere un archivo de Presto.
2. **Se trabaja con Revit y Presto abiertos a la vez**, lado a lado.

!!! note "Dónde está Cost-It en la cadena de Raizant"
    Cost-It es el **nacimiento de la cadena de costo**. Reemplaza el modelado manual de cantidades que se hacía en Syneco. Aguas abajo, esas partidas con cantidades alimentan a Compras (Contratos/Pedidos), a Obra/Almacén (Entregas/costo real) y a Control de obra (certificación y valor ganado). **Cost-It llega solo hasta "presupuesto con cantidades del modelo"** — no compra, no recibe, no certifica.

---

## 2. Cómo se traduce Revit a Presto (la tabla clave)

Esto es el corazón del rol. Cost-It convierte la estructura de Revit en estructura de Presto así:

| En Revit… | …se convierte en Presto en |
|---|---|
| **Categoría** (Muros, Puertas, Ventanas, Pilares…) | **Capítulo** (el contenedor organizativo) |
| **Familia** _(opcional)_ | **Subcapítulo** (solo si marcás "subcapítulos de familias") |
| **Valor del parámetro agrupador** (por defecto, el "código de montaje") | **Partida / unidad de obra** → _cada valor distinto = una partida_ |
| **Cada elemento** (un muro concreto, una ventana concreta) | **Línea de medición** dentro de la partida |
| **La cantidad del elemento** (su área / volumen / longitud / número) | **Cantidad** de esa línea; la partida **suma** sus líneas |
| **Un hueco** (un vano, una ventana en un muro) | **Línea de medición con cantidad negativa** (resta) |

!!! example "Un ejemplo para aterrizarlo"
    Imaginá que en Revit tenés 40 muros, todos con el mismo "código de montaje" `MUR-01`. Cost-It crea **una partida** `MUR-01` en Presto, con **40 líneas de medición** (una por muro), y la partida muestra la **suma** de las superficies de los 40. Si esos muros tienen ventanas, cada ventana entra como una **línea negativa** que resta su superficie. Así, sin teclear una sola cantidad, tenés la partida medida.

---

## 3. La pieza que vos gobernás: la codificación

De toda la tabla de arriba, hay **una decisión que es tuya** y que define si el puente funciona: **qué parámetro de Revit agrupa los elementos en partidas.**

> _"Yo le tengo que decir: creame una partida en base a un cierto parámetro… y que se agrupen los elementos que estén con ese mismo valor de parámetro."_ `[00:20]`

- Por defecto, Cost-It usa el parámetro **"código de montaje"** (en inglés, _Assembly Code_) — un campo estándar de Revit.
- El objetivo final es que **cada partida del modelo coincida con una partida del presupuesto** que armó el departamento de estudio. Si el modelo lleva los códigos de las partidas del presupuesto, el match es automático (lo vemos en la [Página 4](4-codificar-y-volcar.md)).

> 📖 **Fuente oficial:** Manual de Cost-it, p. 5 — _"Se recomienda introducir el código de la unidad de obra en el campo 'Código de montaje' del tipo… En el caso de los materiales debe figurar en el campo 'Nota clave'."_

!!! danger "Regla load-bearing: el código de montaje es un parámetro DE TIPO"
    Esto es sutil y te va a morder si no lo sabés: el "código de montaje" es un parámetro **del tipo**, no de cada elemento individual. **Si lo cambiás en un muro, lo cambiás en TODOS los muros de ese mismo tipo.** ¿Cuándo es un problema? Cuando dos elementos del mismo tipo tienen que ir a **partidas distintas**. En ese caso hay que usar un **parámetro de ejemplar** (individual por elemento). _(Lo retomamos en las [Páginas 3](3-afinar-y-desglosar.md) y [4](4-codificar-y-volcar.md).)_ `[02:10]`

---

## 4. El presupuesto pasa a ser un derivado del modelo

Esta es la idea que cambia la mentalidad del equipo. El entregable final **no es "el presupuesto"** suelto: es **el APU del estudio × la cantidad del modelo BIM**.

> _"El objetivo es que las cantidades provengan… del modelo."_ `[03:30]`

**Consecuencia directa para Raizant:** la calidad del presupuesto depende de la **calidad y la codificación del modelo**. Un modelo bien hecho y bien codificado da un presupuesto confiable casi solo; un modelo mal codificado no tiene puente. Por eso el trabajo de arquitectura **es** trabajo de presupuesto: lo que dibujás y cómo lo codificás es la base de toda la torre de control.

```
   Modelo Revit          Cost-It          Presupuesto Presto
   (cantidades)     ──►   (puente)   ──►   cantidad × APU = costo
        ▲                                          │
        └──────  fuente de verdad de  ─────────────┘
                 las CANTIDADES
```

---

## 5. Los tres semáforos de color (resumen)

Cost-It pinta de colores como información, no como adorno. Hay **tres semáforos**, cada uno en su pantalla. Acá va el resumen; el detalle está en sus páginas:

| Semáforo | Dónde | Qué te dice |
|---|---|---|
| **Resultado** (🔴/⬜/🟢) | sobre el `Resumen` de la partida | si los elementos tienen código y si mezclan tipos → [Página 1](1-traspaso-inicial.md) |
| **Cantidad / regla 2%** (🟣/⚫) | sobre la `Cantidad` de la línea | si la cantidad la **calculó** Cost-It o la copió del modelo → [Página 2](2-leer-y-verificar.md) |
| **Re-sincronización** (🟢 "Inserción") | en `Mediciones temporales` | qué cambió en el último re-traspaso → [Página 5](5-resincronizar.md) |

---

## 6. Lo que Cost-It NO hace (y por eso hay tejido in-house)

Tan importante como lo que hace es lo que **no** hace. Cost-It **traspasa**, pero:

!!! warning "Cost-It NO congela el presupuesto (baseline)"
    Cada vez que re-traspasás, Cost-It **sobreescribe** las cantidades. No guarda una versión "antes/después", no te avisa de desfases. Congelar el presupuesto aprobado (la línea base contra la que se mide el avance) es **disciplina de proceso + herramienta in-house**, no algo que Cost-It haga.

!!! warning "Cost-It NO sincroniza solo cuando el modelo cambia"
    Si arquitectura modifica el diseño, el presupuesto **no se actualiza solo**. Hay que correr a mano el ciclo de re-sincronización (`Añadir` → comprobar → traspasar, [Página 5](5-resincronizar.md)). Nadie te avisa que hay que hacerlo. Por eso Raizant designa un **responsable de re-sync**.

!!! warning "Cost-It NO valida la codificación por vos"
    Si un elemento tiene el código mal puesto, su cantidad va a la **partida equivocada** — o a **ninguna**, y queda fuera del presupuesto en silencio. La validación de "modelo ↔ partidas 1:1" es tejido in-house.

Estas tres cosas son exactamente las **fallas silenciosas** del rol. Las tenés todas, con su blindaje, en [6 · Reglas de oro y fallas silenciosas](6-reglas-de-oro.md).

---

## En una imagen, el flujo completo del rol

```
1. Modelás en Revit  ──►  2. Codificás (código de montaje = partida)
                                        │
                                        ▼
3. Cost-It ▸ Exportar  ──►  4. Presto arma el árbol con cantidades
                                        │
                                        ▼
5. Verificás (magenta/negra, verde)  ──►  6. Volcás al estudio (APU × cantidad)
                                        │
                                        ▼
              7. El modelo cambia  ──►  8. Re-sync con Añadir
```

---

📖 **Fuentes oficiales (RIB):** _Manual de Cost-it_, pp. 5–9 (codificación, traducción Revit→Presto, opciones) · _Cost-it (BIM 5D con Presto)_. · **Complemento interno:** apunte C01 §0 · transcripción `CSE - Cost It - 23/01/2026`.
