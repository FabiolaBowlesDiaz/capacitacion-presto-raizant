# 3 · Adicionales y estados de pago

!!! abstract "Conclusión primero"
    Dos cosas en una página, porque van juntas: (1) cómo entra un **adicional** (un cambio de obra: más cantidad, una partida nueva) **sin romper el presupuesto base** — siempre por una **línea de medición**, nunca digitándolo directo; y (2) cómo se emite el **estado de pago** (el documento de cobro al cliente). La regla de oro: un adicional digitado directo en el árbol, Presto lo lee como **sobrecertificación** (rojo), no como cambio de alcance.

!!! tip "Antes de arrancar, tené a mano el mapa"
    Vas a trabajar en la subventana **`Mediciones`** (abajo) y en los esquemas `Certificación | FASES` y `Presupuesto por estados` del Árbol. Si te perdés con `EstadoPres`, `FaseCert`, `Desdoblar`, abrí en otra pestaña **[🗺 La pantalla de Control de obra](interfaz.md)**.

!!! warning "Requisito de licencia"
    Los adicionales y estados de pago viven en el módulo **Gestión de Proyectos** (las órdenes de cambio requieren _"la licencia de Presto Gestión del proyecto"_, 📖 _Órdenes de cambio_, p. 4). Verificá que el módulo esté incluido antes de operar.

!!! info "De dónde sale este contenido"
    Fuente principal: **documentación oficial de Presto (RIB)** — _Certificación y seguimiento_ (Estados del presupuesto, pp. 11–13; Informes, p. 15) y _Órdenes de cambio_ (pp. 3–7). Se complementa con el apunte interno **C08** y la transcripción del video **`gestion_de_proyectos_09_12_2025`** (minutos `[hh:mm]`). Si la doc y el video chocan, gana la doc.

---

## La regla de oro: un adicional entra por una línea de medición

> 📖 **Fuente oficial:** _Certificación y seguimiento_ (RIB), p. 4 — _"Una línea del presupuesto se puede desglosar en dos o más para certificarla parcialmente; se pueden crear líneas nuevas, añadidas a las del presupuesto; se puede marcar en cada línea si pertenece o no al presupuesto original para realizar una gestión activa de los cambios."_

Y la advertencia de las órdenes de cambio: _"Las nuevas unidades de obra necesarias durante la ejecución se pueden gestionar… a través de las nuevas líneas de medición."_ 📖 _(Órdenes de cambio, p. 3.)_

!!! danger "Falla silenciosa #2 — el error que arruina el seguimiento"
    Si metés un adicional **digitándolo directo** en el árbol (en la celda `N: CanCert`, por encima de lo presupuestado), Presto **no entiende** que es un cambio de alcance: lo pinta **ROJO** = sobrecertificación. _"Presto en ningún caso sabe que son 20 metros cúbicos con respecto a una modificación… no hay forma de hacerlo enterar."_ La forma correcta es **siempre** por línea de medición con su estado. _(C08 FS-2, video `[01:10]`–`[01:20]`.)_

---

## Los tres estados de una línea de medición

Toda línea de medición tiene un **`EstadoPres`** que define cómo cuenta:

| `EstadoPres` | Color | Qué significa | ¿Suma al presupuesto vigente? | ¿Entra al estado de pago? |
|---|---|---|---|---|
| **`Inicial`** | negro | Parte del presupuesto original | ✅ Sí (a `PRS CanIni`) | ✅ Sí |
| **`Modificado`** | verde | Adicional **aprobado** | ✅ Sí (a `PRS CanMod`) | ✅ Sí |
| **`Pendiente`** | — | Adicional **en espera de aprobación** | ❌ No | ❌ No (corre como costo de Raizant) |

> 📖 **Fuente oficial:** _Certificación y seguimiento_ (RIB), p. 12 — _"Las cantidades del presupuesto inicial y de los cambios aprobados se suman para obtener el presupuesto normal o vigente y la cantidad pendiente de aprobación se suma… para obtener el presupuesto total posible."_

!!! danger "Falla silenciosa #3 — el adicional pendiente que nadie aprueba"
    Un adicional en estado **`pendiente`** NO suma al presupuesto ni al estado de pago: figura solo como **costo real**. Si nadie gestiona su aprobación, ese costo **lo absorbe Raizant** (lo construiste pero no lo cobrás). Hacé seguimiento de los pendientes hasta que se aprueben o se rechacen. _(C08 FS-10, video `[01:30]`.)_

---

## Tarea 1 — Crear la línea del presupuesto inicial (en Mediciones)

**Qué es:** registrar la cantidad presupuestada de una partida como una línea de medición, base sobre la que después certificás y agregás adicionales.

**Paso a paso** `[01:20]`:

1. Marcá la partida (ej. "relleno") y abrí la subventana **`Mediciones`** (abajo).
2. Creá la línea inicial: en **`Comentario`** escribí `rellenos`; en **`Cantidad`** poné `119`. Enter.
3. **Verificá la columna `Espacio`:** NO puede quedar en blanco. Si quedó vacía, asigná un espacio genérico.
4. Andá a la **cinta `Inicio` ▸ `Recalcular`** (al menos una vez). La cantidad aparece en `119` en **magenta** (= calculada por líneas de medición). ✅
5. Verificá que **`EstadoPres`** quedó en **`inicial`** (toda línea nace así).

!!! warning "Falla silenciosa #4 — la columna `Espacio` en blanco"
    Si `Espacio` queda vacío, la línea puede no computar bien. El capacitador insiste: _"es súper importante que aparezca información."_ Asigná siempre un espacio (genérico si no tenés uno específico). _(C08 FS-6, video `[01:20]`.)_

---

## Tarea 2 — Certificar con respaldo: el botón `Desdoblar`

**Qué es:** partir una línea de medición en dos para certificar por fases distintas, dejando el avance **respaldado** por mediciones (mejor que digitar directo).

📖 **Fuente oficial:** _Certificación y seguimiento_ (RIB), p. 10 — _"Si no se puede certificar de una vez la cantidad de una línea… Utilice el menú contextual «Desdoblar» y podrá introducir la cantidad que quiere desdoblar."_

**Paso a paso (desdoblar 119 en 100 + 19)** `[01:20]`–`[01:30]`:

1. En `Mediciones`, parate sobre la cantidad `119` → **clic derecho** → **`Desdoblar`**.
2. Indicá cuánto separar: `100` → `Aceptar`. La línea se parte en dos: `100` y `19`.
3. A la línea de `100`: en la columna **`FaseCert`**, desplegá el menú y asigná **fase 1**.
4. A la línea de `19`: en `FaseCert` asigná **fase 2**.
5. `Inicio ▸ Recalcular`. En el Árbol reaparecen los `100` (fase 1) y `19` (fase 2), ahora **respaldados por líneas de medición** (en magenta). ✅

> El capacitador: _"Eso es certificar mediante líneas de medición."_ `[01:30]`. La doc lo recomienda: así la certificación se obtiene _"de forma natural como la versión as-built del presupuesto"_ 📖 _(p. 5)_.

---

## Tarea 3 — Agregar el adicional (la cantidad extra)

**Qué es:** registrar más cantidad de la presupuestada como un cambio, sin tocar la base.

**Ejemplo:** la obra necesitó 20 m³ de relleno extra sobre los 119 iniciales. `[01:10]`

**Paso a paso** `[01:30]`:

1. En `Mediciones`, creá una línea nueva: `Comentario` = `rellenos adicional 01`; verificá `Espacio`; `Cantidad` = `20`.
2. En **`EstadoPres`** elegí uno de dos:
   - **`pendiente`** → a la espera de aprobación del cliente (no entra a estado de pago todavía).
   - **`modificado`** (queda en **verde**) → adicional **aprobado**, sí figura en estado de pago y suma para cobrar.
3. **No te olvides la `FaseCert`:** desplegá la columna `FaseCert` y asigná la fase del adicional (ej. fase 3).
4. `Inicio ▸ Recalcular`.

> El capacitador lo deja claro: _"Una modificación al presupuesto inicial tiene que ingresarse aquí abajo, como una línea de medición… por obligación."_ `[01:30]`

!!! danger "Falla silenciosa #5 — el adicional sin `FaseCert`"
    Una línea de adicional **sin `FaseCert` asignada** no se certifica en ninguna fase: queda en el aire. _"Esto también de repente se le va a la gente."_ Después de crear el adicional, confirmá que tiene su fase. _(C08 FS-7, video `[01:30]`.)_

---

## Tarea 4 — Verificar el presupuesto "vivo" (esquema `Presupuesto por estados`)

**Qué es:** confirmar que Presto guardó por separado el inicial y la modificación.

**Paso a paso** `[01:40]`:

1. En el Árbol, cambiá el esquema de `Certificación | FASES` a **`Presupuesto por estados`**.
2. Leé las columnas:

| Columna | Qué muestra | En el ejemplo |
|---|---|---|
| **`PRS CanIni`** | Cantidad del presupuesto inicial | `119` |
| **`PRS CanMod`** | Cantidad de la modificación aprobada | `20` |
| **`CanPres`** | Unificación (lo que Presto usa para desvíos) | `139` |
| **`ImpPresIni`** / **`ImpPresMod`** / **`ImpPres`** | Los mismos, en importe | `979.132` + `164.560` = `1.143.692` |

> El capacitador: _"Si bien ves ahora 139, Presto recuerda que originalmente eran 119."_ `[01:40]`

!!! note "Si el adicional quedó en `pendiente`"
    Recalculá y vas a ver que `CanPres` **sigue en 119** (el adicional NO suma al vigente); los 20 quedan en la columna de **cambios pendientes**, sin sumar al presupuesto ni al estado de pago. Es la diferencia clave entre `modificado` (suma) y `pendiente` (no suma). _(C08 caso 13, video `[01:40]`.)_

---

## Tarea 5 — Emitir el estado de pago (el documento de cobro)

**Qué es:** generar el informe que se le presenta al cliente para cobrar la fase.

📖 **Fuente oficial:** _Certificación y seguimiento_ (RIB), p. 15 — los informes están en el grupo **"05 Gestión del proyecto"**: _"Cantidades e importes de una certificación"_ y _"Certificación actual y a origen"_.

**Informe básico (España)** `[01:50]`:

1. Andá a los **Informes de España** → grupo **Gestión de proyectos** → **`Certificación anterior, actual y acumulado al origen por capítulo y partidas`** (el primero de la lista).
2. Dejá todo por defecto → **`Vista preliminar`**. Acumula **hasta la fase de certificación actual**. Muestra: cantidad presupuestada, certificación anterior, certificación actual y acumulado al origen.

**Informe más completo (Chile) — `Estado de pago con porcentaje de devolución de anticipo`** `[01:50]`–`[02:00]`:

1. Informes de Chile → `Estados de pago` → ese informe.
2. **`Número de estado de pago`** = el número de la fase de certificación actual (ej. `3`).
3. Respondé las preguntas extra (las que el informe España no tiene):
   - **`% de reajuste`** → ajuste por inflación/índice (debe estar pactado en contrato).
   - **`% de retención`** → lo que se retiene del total.
   - **`% de devolución de anticipo`** → descuenta el anticipo pactado (ej. 10%).
4. `Vista preliminar`: muestra todo el desglose y, al final, descuenta el % de devolución de anticipo → el número final a cobrar.

> El importe del mes se calcula así: 📖 _"El importe de la certificación del mes se obtiene por diferencia entre la certificación total y el importe de la fase anterior."_ _(Certificación y seguimiento, p. 6.)_

!!! tip "Los informes se exportan a Excel y se pueden personalizar"
    La doc lo aclara: _"Una plantilla de Excel genera una hoja resumen de la certificación que se puede modificar y personalizar."_ 📖 _(p. 7.)_ Si Raizant necesita un formato propio de estado de pago, se parte de esa plantilla.

---

## 🎥 Mirá el video

| Tema | Minuto |
|---|---|
| Por qué el adicional no se digita directo (sobrecertificación roja) | `[01:10]`–`[01:20]` |
| Crear la línea inicial en Mediciones (`Espacio`, recalcular) | `[01:20]` |
| Desdoblar + asignar `FaseCert` | `[01:20]`–`[01:30]` |
| Agregar el adicional (`modificado`/`pendiente`, `FaseCert`) | `[01:30]` |
| `Presupuesto por estados` (inicial vs modificado) | `[01:40]` |
| Informe de estado de pago (España / Chile) | `[01:50]`–`[02:00]` |

> Video fuente: `gestion_de_proyectos_09_12_2025.mp4`. Relator de soporte de Presto. _El video es complemento: la referencia primaria es la documentación oficial citada en cada tarea._

---

## ⚠️ Lo que Presto NO te avisa (resumen)

- **Adicional digitado directo** = sobrecertificación roja, no cambio de alcance. _(regla de oro)_
- **Adicional `pendiente`** que nadie aprueba → lo paga Raizant. _(estados)_
- **`Espacio` en blanco** → la línea puede no computar. _(Tarea 1)_
- **Adicional sin `FaseCert`** → no se certifica en ninguna fase. _(Tarea 3)_

👉 Todas, con cómo blindarte, en [5 · Reglas de oro y fallas silenciosas](5-reglas-de-oro.md).

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá lo aprendido"
    Sobre la obra de prueba **BLEND** _(con una licencia que tenga Gestión de Proyectos)_:

    1. En una partida, creá la línea inicial en `Mediciones` (cantidad presupuestada, con `Espacio` asignado). Recalculá y verificá que aparece en magenta.
    2. **Desdoblá** esa línea en dos y asigná cada parte a una fase distinta (`FaseCert` 1 y 2).
    3. Agregá una línea de **adicional** con `EstadoPres = pendiente` y mirá en `Presupuesto por estados` que `CanPres` **no cambia**.
    4. Cambiá ese adicional a `modificado` (verde), recalculá, y comprobá que ahora **sí** suma a `CanPres`.
    5. Generá el informe `Certificación actual y a origen` y revisá el desglose.

    **Cómo sabés que salió bien:** entendés que `pendiente` no suma y `modificado` sí, y que el adicional vive en una línea de medición, no en el árbol.

---

📖 **Fuentes oficiales (RIB):** _Certificación y seguimiento_ — Avance (p. 4), Certificación por líneas de medición (pp. 5, 10–11), Estados del presupuesto (pp. 12–13), Informes (pp. 6–7, 15) · _Órdenes de cambio_ (pp. 3–7). **Complemento interno:** apunte C08 (casos 11–15) · transcripción `gestion_de_proyectos_09_12_2025`.
