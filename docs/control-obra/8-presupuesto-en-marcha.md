# 8 · El presupuesto en marcha

!!! abstract "Conclusión primero"
    Esta página responde la pregunta que aparece el primer mes de obra: **el presupuesto ya está aprobado y congelado… ¿y ahora cómo lo toco?** Respuesta corta: **no lo tocás**. El árbol base no se edita más; todo cambio viaja como **línea de medición con estado** (`pendiente` o `modificado`), y el presupuesto "vivo" se **lee** en el esquema `Presupuesto por estados`, que separa lo original (`PRS CanIni`), lo aprobado (`PRS CanMod`) y lo que espera aprobación (`PRS CanPte`). Congelar la baseline **no es un botón de Presto** (no existe candado nativo): es disciplina + snapshot in-house.

!!! tip "Antes de arrancar, tené a mano el mapa"
    Vas a leer los esquemas `Presupuesto por estados` y `Certificación | FASES` del Árbol. Si te perdés con `EstadoPres`, `CanPres` o las columnas `PRS`, abrí en otra pestaña **[🗺 La pantalla de Control de obra](interfaz.md)**.

!!! info "Qué es esta página (y qué no)"
    Las páginas hermanas ya enseñan el **cómo operar**: [2 · Certificar el avance](2-certificar-avance.md) (cargar `CanCert`, cerrar saldos) y [3 · Adicionales y estados de pago](3-adicionales-y-estados-de-pago.md) (crear las líneas de medición con su estado). Esta página junta la **gestión del presupuesto una vez que arrancó la obra**: la regla que lo protege, cómo leerlo por estados, qué significa "congelado" en Presto y cómo se mide el desvío contra la versión aprobada. No repite los pasos de las otras — las referencia.

---

## La regla que gobierna todo: el presupuesto aprobado NO se edita

Es la [regla de oro #3 del flujo](../flujo/reglas-de-oro.md): la baseline es la **vara contra la que se mide el desvío**; si la movés, ya no sabés contra qué comparás. Y en este rol tiene una forma muy concreta:

- **No se digita** un cambio directo en el árbol: si metés cantidad extra en `N: CanCert`, Presto lo pinta **rojo** = sobrecertificación, no cambio de alcance. _"Presto en ningún caso sabe que son 20 metros cúbicos con respecto a una modificación… no hay forma de hacerlo enterar."_ `[01:10]`–`[01:20]`
- **No se re-edita** la cantidad ni el precio de la partida en la ventana Presupuesto "para que cuadre".
- **Todo cambio entra por una línea de medición** en la subventana `Mediciones`, con su `EstadoPres` y su `FaseCert`. _"Una modificación al presupuesto inicial tiene que ingresarse aquí abajo, como una línea de medición… por obligación."_ `[01:30]`

👉 El paso a paso de crear esas líneas (inicial, desdoblar, adicional `pendiente`/`modificado`) está completo en **[3 · Adicionales y estados de pago](3-adicionales-y-estados-de-pago.md)** — no lo repetimos acá.

!!! danger "Por qué es tan estricto"
    Presto guarda la baseline como **líneas de medición en estado `Inicial`** — pero **nada impide** que alguien las modifique después: no hay candado, no hay roles de usuario, no hay flujo de aprobación nativo. _(Base de conocimiento, hallazgos #2 y #6.)_ La única protección real es que **todo el equipo respete esta regla** + el snapshot in-house (más abajo).

---

## Leer el presupuesto "vivo": el esquema `Presupuesto por estados`

Cuando la obra lleva meses y se acumularon adicionales, la pregunta de dirección es: **¿cuánto del presupuesto es original, cuánto es cambio aprobado y cuánto está en el aire?** Ese desglose Presto lo mantiene solo — si los cambios entraron bien — y se lee en un solo lugar:

**Dónde:** pestaña `Árbol` → desplegar el menú de esquemas → **`Presupuesto por estados`** `[01:40]`.

| Columna | Qué muestra | De dónde sale |
|---|---|---|
| **`PRS CanIni`** / **`ImpPresIni`** | Cantidad / importe del **presupuesto original** (la baseline) | Líneas de medición en estado `Inicial` |
| **`PRS CanMod`** / **`ImpPresMod`** | Cantidad / importe de los **cambios aprobados** | Líneas en estado `Modificado` (verde) |
| **`CanPres`** / **`ImpPres`** | El **presupuesto vigente** = inicial + modificado. Es el valor que Presto usa para desviaciones y análisis de costo | Suma de los dos anteriores |
| **`PRS CanPte`** / **`ImpPresPte`** | Cantidad / importe de los cambios **pendientes de aprobación** — NO suman al vigente | Líneas en estado `Pendiente` |
| **`ImpPresPosible`** | El presupuesto **total posible** si se aprobara todo lo pendiente | Vigente + pendientes |

> 📖 **Fuente oficial:** _Certificación y seguimiento_ (RIB), p. 12 — _"Las cantidades del presupuesto inicial y de los cambios aprobados se suman para obtener el presupuesto normal o vigente y la cantidad pendiente de aprobación se suma… para obtener el presupuesto total posible."_

Cómo se lee en la práctica (el ejemplo del video, rellenos): `PRS CanIni = 119`, `PRS CanMod = 20`, `CanPres = 139`. _"Si bien ves ahora 139, Presto recuerda que originalmente eran 119."_ `[01:40]`

!!! tip "Este esquema es tu informe de gestión de cambios"
    Recorrelo a nivel de **capítulos** (los importes se proyectan hacia arriba hasta el concepto raíz): en una pasada ves qué capítulos acumulan más adicionales y **cuánta plata está en `Pte`** esperando una firma. Cada boliviano en `ImpPresPte` es obra que quizás ya se está ejecutando **sin derecho a cobro todavía** (ver Fallas silenciosas, abajo).

---

## El cuadre de presupuesto al certificar (botón de tres puntos)

Al certificar el remanente de una partida, no calculés el saldo a mano: parate en la celda `N: CanCert` de la fase y apretá el **botón de tres puntos `…`** → Presto sugiere el **cuadre con el presupuesto** y rellena lo que falta por certificar. _"Solito el Presto debería hacerte el cuadre con el presupuesto."_ `[01:00]` El paso a paso completo está en [2 · Certificar el avance, Tarea 3](2-certificar-avance.md).

!!! note "El cuadre cierra contra el presupuesto VIGENTE"
    El cuadre compara contra la cantidad presupuestada — y tras un adicional **aprobado**, esa cantidad es `CanPres` unificado (139, no 119) `[01:40]`. Consecuencia práctica: si el adicional quedó en `pendiente`, el cuadre te va a cerrar contra el original; lo pendiente **no** entra al saldo certificable.

---

## Congelar la baseline: qué significa (y qué no) en Presto

**Congelar = declarar que el presupuesto aprobado es la versión de referencia y que no se edita más.** Tres cosas que hay que tener claras:

1. **En Presto no hay candado nativo.** El estado `Inicial` de las líneas de medición marca qué es baseline, pero cualquiera con el archivo abierto puede editarla. La auditoría de Presto registra el **usuario de Windows** (no hay usuarios internos), y el único control de acceso (`Entorno → Restricciones`) es por computadora, no por usuario, y no es auditable. _(Base de conocimiento, §4.1 y §4.8.)_
2. **En Raizant la protección es el snapshot.** Al congelar, se guarda una **copia versionada del archivo aprobado** (proceso in-house, fuera de Presto). Esa copia es la vara: si alguien toca la base por error, hay contra qué comparar y restaurar. _(Base de conocimiento, §5: "Snapshot + versionado de baseline".)_
3. **Antes de congelar se valida.** Presto **no avisa** de inconsistencias que rompen informes (códigos duplicados, jerarquía rota, redondeos a cero) — la validación es previa al freeze. El checklist completo vive en [Presupuestos · Reglas de oro → "Checklist antes de congelar la baseline"](../presupuestos/5-reglas-de-oro.md).

Después del freeze, los **4 datos de ejecución** son las únicas puertas de entrada: certificación y adicionales por este rol ([página 2](2-certificar-avance.md) y [página 3](3-adicionales-y-estados-de-pago.md)); cantidad real y costo real por [Obra/Almacén](../obra-almacen/index.md). El mapa conceptual está en [0 · Fundamentos, Idea 2](0-fundamentos.md).

---

## Comparar versiones y medir la desviación

¿Qué te da Presto nativo para comparar "lo aprobado" contra "lo que va pasando"?

| Comparación | Dónde se ve | Estado |
|---|---|---|
| Presupuesto original vs. adicionales (aprobados y pendientes) | Esquema `Presupuesto por estados` (esta página) | ✅ Nativo, si los cambios entraron por mediciones `[01:40]` |
| Presupuestado vs. certificado (% de avance de cobro) | Columna `PorCertPres` del esquema `Certificación \| FASES` | ✅ Nativo — ver [página 2](2-certificar-avance.md) `[01:10]` |
| Certificado acumulado en el tiempo (curva S) | Pestaña `Fechas`, esquema `Planificación y certificación` (`Cert` / `OrCert`), export a Excel | ✅ Nativo + Excel `[01:40]`–`[01:50]` |
| Desviación de costo y plazo (CPI / SPI / EAC) | Esquema EVM — contra la baseline como vara | ✅ Nativo — ver [4 · El EVM](4-evm-salud-de-obra.md) |
| Versión congelada vs. archivo actual (¿alguien tocó la base?) | — | ⚠️ **No nativo**: se hace comparando contra el **snapshot** in-house |
| Informe impreso de "desviación del presupuesto" dedicado | — | ⚠️ **Verificar en Presto** — el video no lo muestra; los informes vistos son de certificación y estado de pago `[01:50]` |

!!! warning "La desviación solo vale si la vara no se movió"
    Presto calcula las desviaciones **contra `CanPres`** `[01:40]`. Si alguien editó líneas `Inicial` después del freeze, el desvío se mide contra un número movido y **ningún informe te lo va a avisar**. Por eso el snapshot: es lo único que permite auditar que la baseline sigue siendo la aprobada.

---

## ⚠️ Fallas silenciosas del presupuesto en marcha

- **Olvidar marcar la `Certificación actual`** — el paso que **todos** olvidan. Presto deja digitar avance en cualquier fase, pero **solo acumula hasta la fase marcada como actual**, sin error ni aviso: el avance reportado queda subvaluado en silencio. _"Créanme que de esto se olvida la gente."_ `[00:40]`, `[01:00]` — cómo marcarla, en [página 2](2-certificar-avance.md).
- **El adicional `pendiente` suma al costo real pero NO al cobro.** Lo construís, te cuesta plata, y mientras nadie gestione su aprobación no entra al estado de pago: **lo absorbe Raizant**. Revisá `ImpPresPte` en cada cierre y perseguí cada pendiente hasta que se apruebe o rechace. `[01:30]`–`[01:40]` _(C08 FS-10.)_
- **El cambio digitado directo en el árbol** = sobrecertificación roja, no adicional: se pierde la trazabilidad original/modificado y el esquema por estados deja de contar la historia real. `[01:10]`–`[01:20]` _(C08 FS-2.)_
- **La baseline que muta sin snapshot** — Presto no tiene candado ni te avisa; el EVM sigue calculando, pero contra una vara movida. _(Base de conocimiento, R5.)_

👉 Todas las fallas del rol, con su blindaje, en [5 · Reglas de oro y fallas silenciosas](5-reglas-de-oro.md).

---

## 🎥 Mirá el video

| Tema | Minuto |
|---|---|
| Cuadre de presupuesto con el botón de tres puntos | `[01:00]` |
| Por qué el cambio digitado directo sale rojo (sobrecertificación) | `[01:10]`–`[01:20]` |
| El adicional entra por línea de medición, "por obligación" | `[01:30]` |
| Esquema `Presupuesto por estados` (inicial / modificado / `CanPres`) | `[01:40]` |
| Informes de certificación y estado de pago | `[01:50]`–`[02:00]` |

> Video fuente: `gestion_de_proyectos_09_12_2025.mp4`. _El video es complemento: la referencia primaria es la documentación oficial citada en cada sección._

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá lo aprendido"
    Sobre la obra de prueba **BLEND** _(con una licencia que tenga Gestión de Proyectos, y con las líneas de medición del [ejercicio de la página 3](3-adicionales-y-estados-de-pago.md) ya creadas)_:

    1. Abrí el esquema **`Presupuesto por estados`** y, para una partida con adicional, anotá los cinco números: `PRS CanIni`, `PRS CanMod`, `CanPres`, `PRS CanPte`, `ImpPresPosible`.
    2. Cambiá un adicional de `modificado` a `pendiente`, recalculá, y verificá cómo se mueve la plata de `ImpPresMod` a `ImpPresPte` (y que `ImpPres` baja).
    3. En `Certificación | FASES`, usá el **botón de tres puntos** para cuadrar el saldo de esa partida y fijate contra qué cantidad cerró (¿el original o el vigente?).
    4. Simulá el control de baseline: exportá o copiá el archivo como "snapshot", editá una cantidad `Inicial` a propósito, y comprobá que **ningún aviso de Presto** te lo señala — solo la comparación contra el snapshot lo detecta.

    **Cómo sabés que salió bien:** podés responder de memoria "¿cuánto de este presupuesto es original, cuánto es cambio aprobado y cuánto está pendiente?", y explicar por qué el congelado depende del proceso y no de Presto.

---

📖 **Fuentes oficiales (RIB):** _Certificación y seguimiento_ — Estados del presupuesto (pp. 11–13). **Complemento interno:** apunte C08 (casos 8, 13; reglas R-6/R-7; FS-1, FS-2, FS-10) · extracto `05-gestion-de-proyectos.md` · Base de conocimiento Presto (`00-base-conocimiento-presto.md`, hallazgo #6, §5, R5) · transcripción `gestion_de_proyectos_09_12_2025`.
