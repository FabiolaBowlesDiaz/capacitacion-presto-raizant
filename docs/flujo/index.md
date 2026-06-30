# El flujo: el dato nace una vez y viaja

!!! abstract "La idea en una frase"
    Cada persona del equipo hace su tarea en su rol. Pero el dato que cargás **no se queda en tu pantalla: viaja** a la siguiente etapa, y a la siguiente. Si nace bien, llega bien y la empresa decide con números reales. Si nace tarde, sin dueño o con precio cero, se rompe aguas abajo — **aunque vos hayas hecho perfecto lo tuyo.** Esta sección es el mapa de ese viaje.

## Por qué leer esto, además de tu rol

El manual te enseña **cómo** se hace cada tarea en tu puesto. Esta sección te enseña algo distinto y igual de importante: **cómo encaja tu trabajo en el de los demás.**

Pensalo así: podés armar un APU impecable, pero si lo cargás con el código de montaje equivocado, el de compras le comprará bien y el de contabilidad no podrá traducirlo a una cuenta. Tu tarea estuvo bien hecha *en tu pantalla* — pero el dato se rompió en el camino.

!!! quote "Lo que buscamos"
    🔴 **No queremos información maquillada: queremos la real.** Un número verde que miente es peor que un “no sé” honesto, porque sobre el número verde se toman decisiones de plata.

## El recorrido del dato en Raizant

El dato de una obra hace un viaje de punta a punta. Cada flecha es un **traspaso**: alguien entrega, alguien recibe.

```
  ARQUITECTURA        PRESUPUESTO         COMPRAS          OBRA / ALMACÉN      CONTROL DE OBRA     CONTABILIDAD
  ┌──────────┐       ┌──────────┐       ┌──────────┐      ┌──────────┐        ┌──────────┐       ┌──────────┐
  │  Revit   │  ──▶  │  Presto  │  ──▶  │  Orden   │ ──▶  │ Recepción│  ──▶   │   Mide   │  ──▶  │  Syneco  │
  │ Cost-It  │       │ APU/precios      │de compra │      │ + consumo│        │ la salud │       │ contable │
  │cantidades│       │ baseline │       │          │      │ real     │        │ CPI/SPI  │       │  EERR    │
  └──────────┘       └──────────┘       └──────────┘      └──────────┘        └──────────┘       └──────────┘
     Fernanda          Enrique          Daniel/Hubert      Obra+Almacén        Torre/Control       Carolina
```

Cada etapa **lee** lo que hizo la anterior y **no lo vuelve a teclear**. Ese es el primer principio, y el más importante.

## Los 3 principios que sostienen todo

=== "A · Un dato, un dueño, una fuente"

    Cada hecho **nace una sola vez**, en el sistema que es su dueño. Los demás lo **leen**, nunca lo vuelven a digitar ni lo recalculan por su cuenta.

    > **Ejemplo:** las cantidades del edificio nacen en el modelo de Fernanda. Si en presupuesto alguien teclea una cantidad “a mano” en vez de traerla del modelo, ya hay **dos versiones** del mismo número — y tarde o temprano una miente.

    Si ves el mismo dato en dos lados con valores distintos, **no se promedia**: se busca cuál es el dueño y se corrige en el origen.

=== "B · Segregación de funciones"

    **Ejecutar ≠ Medir/Verificar ≠ Aprobar/Pagar** nunca en la misma persona en el mismo ciclo. El que hace el trabajo no es el único que dice cuánto avanzó, y el que pide un material no es el que lo recibe.

    > **Por qué:** no es desconfianza de la persona, es diseño del sistema. Cuando una sola mano hace todo el ciclo, un error (o un desvío) **no tiene quién lo atrape**.

=== "C · Cuatro ojos (nadie juez y parte)"

    El que ejecuta **mide y propone** su número; un segundo, **independiente**, lo **verifica** contra un dato crudo. La cifra no se aprueba sola.

    > **Ejemplo:** el superintendente mide su avance de obra (lo necesita para dirigir) y levanta la certificación. Pero su número **se contrasta** con el material que realmente se consumió. Si dice 80% de avance y solo salió material para el 50%, **el dato lo marca solo** — sin señalar a nadie, simplemente no cuadra y se investiga.

## A dónde te lleva esta sección

<div class="grid cards" markdown>

-   :material-sync: **Los 2 ciclos**

    ---

    Cómo viaja el dato en el **ciclo de compras** (Pide ≠ Compra ≠ Recibe ≠ Paga) y en el **ciclo de obra** (Ejecuta ≠ Mide ≠ Aprueba).

    [:octicons-arrow-right-24: Ver](los-dos-ciclos.md)

-   :material-heart-pulse: **El ciclo de vida del dato**

    ---

    Las 5 etapas de la vida de un dato y **dónde puede pudrirse** en cada una — con su guardián.

    [:octicons-arrow-right-24: Ver](ciclo-de-vida-del-dato.md)

-   :material-medal: **Las 3 reglas de oro**

    ---

    Las tres reglas **no negociables** que mantienen el dato sano. Si una se rompe, el cierre se bloquea.

    [:octicons-arrow-right-24: Ver](reglas-de-oro.md)

</div>

!!! tip "Y en cada rol: “Tu lugar en el flujo”"
    Dentro de cada rol vas a encontrar una página **“Tu lugar en el flujo”** que aterriza todo esto a tu puesto: de quién recibís el dato, qué entregás, de qué sos dueño y qué se rompe aguas abajo si tu dato llega tarde o sucio.

---

!!! note "Estado de este contenido"
    Esta sección destila el documento interno de **gobierno de datos y roles de Raizant** a una versión friendly para todo el equipo. Algunos responsables todavía están **⚠️ por definir** (se cierran en la sesión de firmas) y quedan marcados como tales. Cuando se firmen, se actualiza acá.
