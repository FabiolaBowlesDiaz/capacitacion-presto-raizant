# 0 · Fundamentos del control de obra

!!! abstract "Conclusión primero"
    Antes de tocar un botón, hay **tres ideas** que hacen que todo lo demás se entienda: (1) hay **tres "avances" distintos** que la gente mezcla todo el tiempo, y este rol maneja **dos de ellos** (no el tercero); (2) una vez **congelado el presupuesto base, no se edita más** — los cambios entran por otras puertas; y (3) toda la salud de obra sale de cruzar **tres magnitudes: PV, EV y AC**. Si entendés esto, el resto del rol es seguir pasos.

---

## Idea 1 — Los tres avances que se confunden

Esta es **la trampa conceptual más importante** del rol. El capacitador la repite: _"no quiero que se confundan… uno muchas veces piensa el avance de la obra en el sentido del avance físico… cuidado en esa parte."_ Hay **tres** cosas que se llaman "avance" y son distintas:

| Avance | Qué es | Dónde se registra | ¿Lo maneja este rol? |
|---|---|---|---|
| **Certificable** | El avance que el cliente **aprueba para pagarte** (estados de pago) | Módulo Gestión de Proyectos (`CanCert`) | ✅ Sí — Tareas 2 y 3 |
| **Físico (cantidad real ejecutada)** | Lo que **de verdad se construyó** en obra | Árbol, columna `CanReal` (rol Obra/Almacén) | ➖ Solo lo lee el EVM |
| **Costo real** | Lo que **de verdad costó** lo construido | Ventana Entregas (rol Obra/Almacén) | ➖ Solo lo lee el EVM |

> 📖 **Fuente oficial:** _Certificación y seguimiento_ (RIB), p. 3 — _"La certificación representa el importe de la obra ejecutada que debe ser abonada por el cliente."_ Es decir: **certificar = avance para cobrar**, no necesariamente lo que físicamente se hizo.

!!! danger "Por qué importa para Raizant"
    La **certificación** puede ir adelantada o atrasada respecto al **avance físico** real. Si reportás a dirección "vamos al 40%" sin aclarar si es 40% **certificado** (cobrado) o 40% **físico** (construido) o 40% en **costo**, podés dar una foto equivocada. La torre de control cruza los tres justamente para detectar cuando se despegan (ej. certificaste más de lo que construiste).

---

## Idea 2 — El presupuesto base se congela; los cambios entran por otra puerta

Una vez que el presupuesto está aprobado y arranca la obra, **se convierte en la línea base ("baseline") y no se edita más**. Esto no es un capricho: es lo que permite **medir desvíos** (si movés la base, ya no sabés contra qué comparás).

Entonces, ¿por dónde entran los cambios de la obra? Por **cuatro datos de ejecución**, que entran por dos roles distintos:

```
        PRESUPUESTO BASE (congelado)  ← no se toca más
                  │
     ┌────────────┼────────────────────────┐
     │  Entran durante la ejecución:        │
     │                                      │
  ESTE ROL (Control de obra):          ROL OBRA/ALMACÉN:
   1. Certificación (CanCert)           3. Cantidad real ejecutada (CanReal)
   2. Adicionales (líneas medición)     4. Costo real (imputación en Entregas)
```

> 📖 **Fuente oficial:** _Órdenes de cambio_ (RIB), p. 3 — _"Las nuevas unidades de obra necesarias durante la ejecución se pueden gestionar… a través de las nuevas líneas de medición."_ Un adicional **nunca** se mete editando el presupuesto base.

!!! danger "Falla silenciosa que nace de acá"
    Si metés un adicional **digitándolo directo** en el árbol (en vez de por una línea de medición), Presto **no entiende** que es un cambio de alcance: lo lee como **sobrecertificación** y lo pinta en rojo. La forma correcta está en [3 · Adicionales y estados de pago](3-adicionales-y-estados-de-pago.md). _(C08 FS-2.)_

---

## Idea 3 — Las tres magnitudes del valor ganado (PV, EV, AC)

Toda la "salud de obra" del EVM sale de cruzar **tres números** a una misma fecha de corte. Son la base de la [Tarea 4](4-evm-salud-de-obra.md), pero conviene entenderlos desde ya:

| Sigla | Nombre | En criollo | En Presto |
|---|---|---|---|
| **PV** | Valor planificado | Cuánto **planeaste** producir a la fecha | `OrPlan` |
| **EV** | Valor ganado | Cuánto **vale lo que hiciste**, a precio de plan | `OrRealObj` |
| **AC** | Costo real | Cuánto te **costó** lo que hiciste | `OrReal` |

> 📖 **Fuente oficial:** _El valor ganado explicado en 4 páginas_ (RIB), p. 2 — _"El valor ganado es el «Earned Value» (EV)… En Presto se llama «RealObj»… El coste real… lo llamamos «Actual Cost» (AC)… En Presto es «Real»."_ El presupuesto total (la referencia que no cambia) es el **BAC**, en Presto **`Obj`**.

!!! note "La idea del valor ganado, con un ejemplo (de la doc oficial)"
    Tenés una zanja de 1.000 m y un tubo de 1.000 m. Excavaste 500 m (50%) e instalaste 400 m de tubo (40%). **No podés sumar 500 + 400** y decir "voy por 900 de 2.000" — son cosas distintas. Lo que se hace es **multiplicar cada cantidad por su costo** para poder sumarlas: así obtenés el **% de avance global real** (en el ejemplo oficial, 43,3%). Ese "importe realizado" es el **valor ganado**. _(📖 mismo documento, p. 1.)_

De cruzar estos tres salen los **cuatro índices** que vas a leer:

- **CPI = EV / AC** → ¿gasto bien? (mayor a 1 = ahorro)
- **SPI = EV / PV** → ¿voy a tiempo? (menor a 1 = atraso)
- **EAC = BAC / CPI** → ¿en cuánto va a terminar la obra?
- **% Avance = EV / BAC** → ¿cuánto llevo ganado?

---

## Idea 4 — Un indicador sobre datos rotos miente

La advertencia que recorre todo el rol: **el EVM de Presto es matemáticamente perfecto, pero solo vale si el dato base es confiable.** Un CPI verde calculado sobre un costo real incompleto te dice "todo bien" cuando en realidad falta cargar gastos.

Las cuatro condiciones para que los números no mientan:

1. La **baseline (objetivo de coste) congelada** — si flota, el PV miente.
2. La **cantidad real ejecutada** cargada — si falta, no hay valor ganado.
3. Los **consumos imputados** con su precio — si faltan, el costo real está incompleto.
4. La **certificación actual** marcada e incluyendo las fechas de imputación — si no, los montos no suman.

!!! tip "Esto es justo lo que aporta Raizant"
    Presto **calcula** los indicadores; la torre de control de Raizant pone la **capa de confiabilidad** (detectar el dato roto y avisar) y la **alarma temprana**. El motor de EVM **no hay que programarlo** — viene nativo. Lo nuestro es que el dato que entra sea de fiar.

---

## En resumen

- **Tres avances distintos:** certificable (cobro), físico (construido), costo real. Este rol maneja la certificación; el físico y el costo solo los lee del EVM.
- **El presupuesto base se congela:** los cambios entran por líneas de medición (adicionales) y por los datos de ejecución, nunca editando la base.
- **Tres magnitudes:** PV (lo planeado), EV (lo ganado), AC (lo gastado). De ahí salen CPI, SPI, EAC y % Avance.
- **El dato manda:** un indicador verde sobre datos incompletos miente — por eso la confiabilidad es lo primero.

Con esto claro, seguí con **[1 · Armar la línea temporal](1-linea-temporal.md)** para preparar la obra.

---

📖 **Fuentes oficiales (RIB):** _Certificación y seguimiento_ (p. 3) · _Órdenes de cambio_ (p. 3) · _El valor ganado explicado en 4 páginas_ (pp. 1–2). **Complementos internos:** apuntes C08 (§0) y C09 (§0) · transcripciones de los videos de capacitación.
