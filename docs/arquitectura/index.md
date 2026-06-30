# Rol Arquitectura (Cost-It · Revit → Presto)

!!! info "¿Este rol es para vos?"
    Sos **arquitectura / modelado BIM** si tu trabajo es **dibujar el proyecto en Revit**. Acá aprendés cómo ese modelo 3D se convierte, casi solo, en el **presupuesto con cantidades** de Presto. Es el rol que está en el **nacimiento de toda la cadena de costo**: si el modelo está bien hecho y bien codificado, el presupuesto se llena solo; si no, no hay puente. También es para **presupuestos (Enrique)**, porque del lado de Presto hay que revisar y afinar lo que llega del modelo.

!!! abstract "La idea en una frase"
    **Cost-It** es el puente que lleva las cantidades del modelo de **Revit** a las partidas de **Presto** (lo que se llama **5D BIM**). El presupuesto deja de tecletearse a mano: pasa a ser un **cálculo derivado del modelo** → _cantidad del modelo × precio (APU) del estudio_. La **fuente de verdad de las cantidades es el modelo Revit**, no Presto.

!!! warning "Requisito de licencia — leelo antes de arrancar"
    Este rol **solo se puede operar si la licencia incluye el módulo Cost-It** (el que habilita Revit → Presto) **y** el **complemento de Cost-It instalado en Revit** en una versión compatible. Si en Revit no aparece el menú `Cost-It` en la cinta, el módulo no está. Es un **requisito a confirmar al contratar/renovar** la licencia. _(Detalle en [La pantalla de Arquitectura](interfaz.md).)_

---

## Este rol vive en DOS programas (no en uno)

A diferencia de los otros roles, acá trabajás con **Revit y Presto abiertos a la vez**, lado a lado:

| Dónde | Qué hacés ahí |
|---|---|
| **En Revit** _(el menú `Cost-It`)_ | Lanzás el traspaso (`Exportar`), elegís cómo se agrupan los elementos en partidas, y re-sincronizás cuando el modelo cambia (`Añadir`). |
| **En Presto** _(pestaña `Árbol` + subventana `Mediciones`)_ | Leés el resultado, revisás las cantidades, desglosás partidas y volcás las cantidades al presupuesto del estudio. |

!!! tip "¿Te perdés entre tantos menús y botones? Empezá por acá"
    Antes que nada, mirá **[🗺 La pantalla de Arquitectura: dónde está cada cosa](interfaz.md)**. Es el mapa del menú `Cost-It` en la cinta de Revit y de la zona de Presto donde aparece el resultado — para que cuando una tarea diga "andá a tal botón", sepas dónde está.

---

## Tu recorrido de aprendizaje

Está ordenado de lo más simple (traer el modelo por primera vez) a lo más completo (mantenerlo sincronizado cuando el diseño cambia).

<div class="grid cards" markdown>

-   **0 · Fundamentos de Cost-It**

    ---

    El modelo mental: cómo Revit se traduce a Presto (categoría → capítulo, elemento → línea de medición), por qué el presupuesto es **un derivado del modelo**, los **tres semáforos de color** y lo que Cost-It **no** hace por vos.

    [:octicons-arrow-right-24: Empezar aquí](0-fundamentos.md)

-   **1 · Traer el modelo a Presto (traspaso inicial)**

    ---

    El camino base: lanzar `Exportar`, elegir el **parámetro que agrupa los elementos en partidas** (la codificación), filtrar categorías y leer el árbol que aparece en Presto.

    [:octicons-arrow-right-24: Ver](1-traspaso-inicial.md)

-   **2 · Leer y verificar el resultado**

    ---

    Las cantidades **magenta vs negra** (la regla del 2%), cómo saltar de una partida al elemento en el modelo y vuelta, y qué cambia con un modelo central/federado.

    [:octicons-arrow-right-24: Ver](2-leer-y-verificar.md)

-   **3 · Afinar y desglosar**

    ---

    Separar partidas con **tipos mezclados** (semáforo verde), el **discriminador** y el **script del código** para que salga bien desde el modelo, y guardar tu configuración como plantilla.

    [:octicons-arrow-right-24: Ver](3-afinar-y-desglosar.md)

-   **4 · Codificar el modelo y volcar al presupuesto**

    ---

    Cómo entregar al modelador el **catálogo de códigos** de las partidas, y cómo **volcar las cantidades del modelo a un estudio ya armado** (con sus APUs y precios).

    [:octicons-arrow-right-24: Ver](4-codificar-y-volcar.md)

-   **5 · Re-sincronizar cuando el modelo cambia**

    ---

    El corazón del rol: cuando el diseño cambia, actualizar el presupuesto con **`Añadir` (nunca `Exportar`)**, `Comprobar`, `Buscar líneas desaparecidas` y revisar los cambios antes de aceptarlos.

    [:octicons-arrow-right-24: Ver](5-resincronizar.md)

-   **6 · Reglas de oro y fallas silenciosas**

    ---

    Lo que Cost-It **no** te avisa: el presupuesto se desfasa del modelo sin aviso, partidas verdes presupuestadas mal, códigos que mandan la cantidad a la nada. Las 11 trampas con su blindaje.

    [:octicons-arrow-right-24: Ver](6-reglas-de-oro.md)

-   **7 · Preguntas frecuentes y glosario**

    ---

    Las dudas que aparecen siempre + el diccionario de la jerga (Cost-It, código de montaje, regla del 2%, discriminador, `.CostItLayout`…).

    [:octicons-arrow-right-24: Ver](7-faq-glosario.md)

-   **8 · Ejercicios en BLEND**

    ---

    Practicá cada paso sobre un modelo de prueba, en un entorno seguro _(cuando la licencia tenga el módulo Cost-It)_.

    [:octicons-arrow-right-24: Ver](8-ejercicios-blend.md)

</div>

## En una frase, qué vas a aprender

A convertir un **modelo de Revit** en un **presupuesto con cantidades** dentro de Presto: a elegir cómo se agrupan los elementos en partidas, a verificar que las cantidades sean confiables, a encadenarlas con el presupuesto del estudio, y a mantener todo sincronizado cuando el diseño cambia — entendiendo qué hace Cost-It solo y qué tiene que controlar el proceso de Raizant (porque Cost-It **traspasa**, pero **no congela, no alerta y no sincroniza solo**).

---

!!! note "Fuente de este rol"
    Construido sobre la **documentación oficial de Presto (RIB)** — _Manual de Cost-it_, _Cost-it (BIM 5D con Presto)_ y _Personalización de la exportación de Revit_ — complementada con el apunte interno **C01** y la **traducción/transcripción del video de Cost-It** (`CSE - Cost It - 23/01/2026`), que cubre situaciones que la documentación oficial no detalla. Cada página cita su fuente oficial por página y, cuando aplica, el minuto del video.
