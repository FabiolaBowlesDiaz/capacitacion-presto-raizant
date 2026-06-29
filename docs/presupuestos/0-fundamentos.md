# 0 · Fundamentos de Presto

!!! abstract "Conclusión primero"
    Presto es, en el fondo, **una base de datos en forma de árbol**. Todo lo que hagas —presupuesto, compras, certificación, contabilidad— cuelga de ese árbol y de una regla simple: **cada concepto tiene un código único y un solo precio**. Si entendés esto, entendés Presto. Si lo rompés, Presto **no te avisa** y los informes salen mal.

Esta página es el modelo mental. Es corta a propósito. Léela antes que nada.

---

## 1. Qué es Presto (y qué NO es)

**Qué es:** un programa para armar y controlar el **costo de una obra**. Cada obra es **un archivo `.presto`**, y ese archivo es una **base de datos completa e independiente**.

!!! quote "La analogía que lo explica todo"
    *"Cada `.presto` es como un Access independiente."* Contiene todos sus datos adentro; lo podés llevar a otra computadora y no pierde nada. **No hay un servidor central** que tenga "todas las obras": cada obra ≈ su propio archivo.

**Qué NO es:** Presto **no es un ERP**. Esto es importantísimo para Raizant:

- No tiene usuarios ni permisos por persona (registra el usuario de Windows, no quién es quién).
- No te obliga a seguir un flujo de aprobación.
- No encadena obligatoriamente requisición → orden de compra → recepción → factura.
- No trae un conector automático a la contabilidad (Syneco).

!!! note "Por qué importa para Raizant"
    Todo eso que Presto **no** hace por sí solo es exactamente lo que construimos nosotros por fuera (el "tejido conectivo": el puente a Syneco, el congelado de la baseline, la torre de control). Presto pone el **dato confiable**; nosotros ponemos el **proceso alrededor**.

---

## 2. El árbol de Conceptos (lo único que existe de verdad)

Todo en Presto es un **concepto**: una fila del árbol. Y los conceptos se anidan unos dentro de otros, como carpetas:

```
OBRA (raíz)  ← el total del presupuesto
│
├── CAPÍTULO          (ej. "Obra gruesa")
│   ├── SUBCAPÍTULO   (ej. "Hormigones")
│   │   └── PARTIDA   (ej. "Hormigón de vigas y pilares")  ← lo que se mide y se paga
│   │        ├── MATERIAL      (cemento, arena, ripio)
│   │        ├── MANO DE OBRA  (concretero)
│   │        └── MAQUINARIA    (mixer)
```

- Una **partida** es la unidad que se mide y se cobra (ej. "m³ de hormigón").
- La descomposición de una partida en sus materiales + mano de obra + maquinaria es el **APU** (Análisis de Precio Unitario).
- Los materiales, mano de obra y maquinaria son los **recursos** (lo más básico del árbol).

### Las dos reglas de cálculo del árbol

| Regla | Qué significa |
|---|---|
| **El precio del superior = la suma de los importes de sus inferiores** | El precio de una partida es la suma de su APU. El de un capítulo, la suma de sus partidas. Y así hasta la raíz. |
| **La cantidad del inferior se multiplica por la del superior** | Si una partida tiene 10 m³ y su APU lleva 350 kg de cemento por m³, Presto sabe que la obra usa 3.500 kg. |

---

## 3. "Un concepto = un código = un precio"

Esta es **la** regla de oro de la que sale todo lo demás:

!!! danger "El código es la identidad del concepto"
    - **No pueden existir dos conceptos con el mismo código.** Presto lo rechaza.
    - **Cambiar el precio de un recurso lo cambia en TODAS las partidas donde se usa.** Si subís el precio del cemento, sube en cada APU que lo lleva. Eso es lo bueno (una sola fuente de verdad) y lo peligroso (un cambio se propaga a todo).
    - Si duplicás, renombrás mal o rompés la jerarquía de códigos, se rompen los informes, el valor ganado y el puente contable — **y Presto no te avisa**.

!!! warning "Los códigos distinguen MAYÚSCULAS de minúsculas"
    `MAT001` y `mat001` son, para Presto, dos cosas distintas en filtros y búsquedas. **Recomendación: trabajar siempre en MAYÚSCULAS** (se configura una vez, ver [Presupuesto básico](1-basico.md)).

---

## 4. Cada módulo es una "ventana" del mismo dato

Presto tiene módulos (Presupuesto, Planificación, Contratación, Gestión, Facturación…). Pero **no son programas separados que se sincronizan**: son **vistas distintas del mismo árbol**.

!!! quote "El principio operativo"
    *"Se lee de Presto, no se recalcula."*

Cuando cambiás un precio en Presupuesto, el cambio ya lo ve Facturación, Gestión y los informes — **porque es el mismo registro**, no una copia. No hay que "pasar datos" de un módulo a otro.

Las tres ventanas que vas a usar todo el tiempo en presupuesto:

| Ventana | Para qué sirve |
|---|---|
| **Árbol** | Ver toda la estructura jerárquica en una sola vista, desplegable por niveles |
| **Presupuesto** | Crear la estructura y armar los APU (la ventana de trabajo habitual) |
| **Conceptos** | La base de datos plana: todos los conceptos en una lista (el catálogo) |

---

## 5. La cantidad nace en Revit (no se teclea)

En el flujo objetivo de Raizant, la **cantidad** de cada partida no se escribe a mano: **se hereda del modelo de Revit** vía Cost-It. El modelo BIM es la fuente de verdad de las cantidades; el presupuesto es un **cálculo derivado** (cantidad del modelo × precio del APU).

!!! note "Mientras tanto"
    Hasta que el modelo Revit esté completo, las cantidades se cargan a mano o por Excel (lo vemos en [Presupuesto básico](1-basico.md)). Pero el destino es: **la cantidad la pone arquitectura desde el modelo**, el presupuestador pone el **precio**.

---

## 6. Los colores son información, no adorno

!!! quote
    *"En Presto los colores te dan información importante."*

| Lo que ves | Qué significa |
|---|---|
| Precio en texto **negro** | Precio **base**: lo tecleaste a mano, no tiene descomposición |
| Precio en texto **magenta/rosado** | Precio **calculado**: tiene un APU debajo que lo respalda, o hubo conversión de moneda |
| Cantidad en **magenta** | Cantidad **respaldada por líneas de medición** (no es un número suelto) |

Aprender a leer los colores te dice de un vistazo si un precio es "a dedo" o está respaldado.

---

<div class="admonition success">
<p class="admonition-title">Ya tenés el modelo mental</p>
<p>Con esto entendido, todo lo demás son procedimientos. Seguí con <a href="../1-basico/">1 · Presupuesto básico</a>, donde armás tu primer presupuesto de cero, paso a paso.</p>
</div>

---

📖 **Fuentes de esta página:** Base de conocimiento Presto (las 10 verdades), Manual de Presto completo (RIB), Componentes de Presto, Presto: una presentación global. · Apunte de capacitación: CL-1, Presupuesto Básico.
