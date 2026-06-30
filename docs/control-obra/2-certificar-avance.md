# 2 · Certificar el avance

!!! abstract "Conclusión primero"
    Acá está el **día a día** del rol: cada vez que cierra una fase (un mes), cargás cuánto avanzó cada partida para cobrarlo. Tres cosas que tenés que clavar: (1) el avance **siempre se ingresa como cantidad**, nunca como porcentaje; (2) después de cargar, hay que **marcar la fase como "certificación actual"** o Presto **no acumula nada** (es el olvido #1 de todos); y (3) los acumulados (`CanCert`, `ImpCert`) solo suman **hasta la fase actual**.

!!! tip "Antes de arrancar, tené a mano el mapa"
    Vas a trabajar en la pestaña **`Árbol`** con el esquema **`Certificación | FASES`** y en la pestaña **`Fechas`**. Si te perdés con las columnas (`N: CanCert`, `CanCertAct`, `PorCertPres`…), abrí en otra pestaña **[🗺 La pantalla de Control de obra](interfaz.md)**.

!!! warning "Requisito de licencia"
    La certificación vive en el módulo **Gestión de Proyectos**. Si tu licencia no lo incluye, el esquema `Certificación | FASES` no aparece en el desplegable. Verificá que el módulo esté incluido antes de operar.

!!! info "De dónde sale este contenido"
    Fuente principal: **documentación oficial de Presto (RIB)** — _Certificación y seguimiento_ (cap. Avance, p. 4). Se complementa con el apunte interno **C08** y la transcripción del video **`gestion_de_proyectos_09_12_2025`** (minutos `[hh:mm]` y la ruta de clic exacta). Si la doc y el video chocan, gana la doc.

---

## Antes de empezar: el avance se ingresa por cantidad

> 📖 **Fuente oficial:** _Certificación y seguimiento_ (RIB), p. 4 — _"el avance de la obra se registra introduciendo la cantidad ejecutada o certificable de cada unidad de obra."_

El capacitador lo refuerza: _"En el Presto se ingresa la certificación o el avance que se certifica, se ingresa por cantidad."_ `[00:50]`. Si el dato te llega como **porcentaje**, alguien lo convirtió desde una cantidad — pedí el dato original en cantidad. Cargar un % rompe la lógica.

---

## Tarea 1 — Preparar el esquema del Árbol para certificar

**Qué es:** dejar la pantalla del presupuesto lista para cargar avance. Se hace una vez por sesión de trabajo.

**Paso a paso** `[00:50]`:

1. Andá a la pestaña **`Árbol`** (viene en el esquema `presupuesto`).
2. Abrí el **menú de esquemas** y cambialo a **`Certificación | FASES`** (está un poco debajo de la mitad de la lista).
3. **Desplegá el árbol hasta el nivel de las partidas** (con el menú de niveles del árbol). Las partidas son donde se certifica.
4. **Inmovilizá las columnas de referencia:** clic derecho sobre la columna **`CanPres`** → **`Inmovilizar columna`**. Así `CanPres` y todo lo de su izquierda quedan fijas (como congelar paneles en Excel) mientras te desplazás por las fases.

**La señal de que salió bien:** aparecen **pares de columnas numeradas por fase** — `1: CanCert` / `1: Cert`, `2: CanCert` / `2: Cert`, … una pareja por fase, cada par con su fecha al pie (`31-Dic-25`, `30-Ene-26`…). Con 15 fases verás 15 pares. ✅

!!! note "¿Qué es cada columna del par?"
    **`N: CanCert`** es donde **vos digitás** la cantidad certificada de la fase N. **`N: Cert`** es el **importe** que Presto calcula solo (`cantidad × precio`). No toques la segunda, solo la primera.

---

## Tarea 2 — Ingresar el avance certificado de una fase

**Qué es:** cargar cuánto se certificó de una partida en un período.

**Dónde estás:** en el Árbol, esquema `Certificación | FASES`, sobre la partida que querés certificar.

**Paso a paso** `[00:50]`–`[01:00]`:

1. Ubicá la partida (ej. "excavaciones").
2. Parate en la celda **`N: CanCert`** de la fase que corresponde (ej. fase 1).
3. **Digitá la cantidad certificada** (ej. `100`).
4. **La señal de que salió bien:** la columna pareada **`N: Cert`** muestra sola el **importe** = cantidad × precio unitario (ej. `100 × 827 = 82.700`). ✅

!!! tip "El precio sale del presupuesto, no lo ponés vos"
    La columna **`Cert`** ya trae el precio unitario de certificación, que viene del presupuesto de adjudicación. Vos solo ponés la **cantidad**; el importe se calcula con ese precio. _(C08 R-1/R-2.)_

---

## Tarea 3 — Cerrar el saldo contra el presupuesto (botón de tres puntos)

**Qué es:** completar lo que falta de una partida hasta llegar a lo presupuestado, sin sacar la cuenta a mano.

**Cuándo:** cuando una partida quedó con un saldo chico por certificar y querés cerrarla.

**Ejemplo:** la partida tiene `CanPres = 119`, ya certificaste 100 → faltan 19. `[01:00]`

**Paso a paso:**

1. Parate en la celda **`N: CanCert`** de la fase donde cerrás el saldo.
2. Apretá el **botón de tres puntos `…`** que aparece en la celda. Presto **sugiere el cuadre con el presupuesto** y rellena el saldo (los 19 que faltaban).

> El capacitador: _"Solito el Presto debería hacerte el cuadre con el presupuesto… puedes cerrarlo con el botón de sugerencia si te queda algo de saldo por certificar."_ `[01:00]`

---

## Tarea 4 — Marcar la "certificación actual" (¡el paso que todos olvidan!)

**Qué es:** decirle a Presto cuál es la fase vigente. **Sin esto, los datos que cargaste NO se acumulan.**

📖 **Fuente oficial:** _Certificación y seguimiento_ (RIB), p. 9 — el ejemplo oficial aclara: _"se ha certificado hasta la fase 10, que es la fase aprobada"_ → la fase aprobada/actual es la que define hasta dónde acumula.

**Dos formas equivalentes** `[01:00]`:

- **(A) Desde Fechas:** pestaña `Fechas` → la fecha de la fase → **clic derecho** sobre `NatC` → **`Certificación actual`**.
- **(B) Desde el Árbol:** parate en cualquiera de las dos columnas de la fase (`N: CanCert` o `N: Cert`) → **clic derecho** → **`Certificación actual`**.

**La señal de que salió bien:** tras unos segundos, el par de columnas de esa fase queda **naranja**; la anterior "certificación actual" pierde el naranja. ✅

!!! danger "Falla silenciosa #1 — el olvido más caro del rol"
    Si la fase **no está** marcada como certificación actual, Presto **te deja digitar datos pero NO los acumula** en `CanCert`/`ImpCert`, **sin ningún error ni aviso**. El reporte de avance a dirección queda subvaluado en silencio. El capacitador: _"el Presto no te va a estar acumulando estos dos datos… créanme que de esto se olvida la gente."_ **Cada cierre de fase: cargá el avance Y movele la certificación actual.** _(C08 FS-1, video `[00:40]`, `[01:00]`–`[01:10]`.)_

---

## Tarea 5 — Leer los acumulados (la foto de la obra)

**Qué es:** entender qué te dicen las columnas de acumulado una vez marcada la certificación actual.

**Ejemplo:** cargaste fase 1 = 100 y fase 2 = 100, con la fase 2 como certificación actual.

| Columna | Qué muestra | En el ejemplo |
|---|---|---|
| **`CanCert`** | Cantidad certificada **acumulada** hasta la fase actual | `200` |
| **`ImpCert`** | Importe certificado **acumulado** hasta la fase actual | suma de las fases ≤ actual |
| **`CanCertAct`** | Cantidad certificada **de la fase actual** (la naranja) | `100` |
| **`ImpCertAct`** | Importe **de la fase actual** | importe de la fase 2 |
| **`PorCertPres`** | **% certificado sobre presupuesto** | ej. excavaciones 26,60% |

!!! warning "El % se calcula con IMPORTES, no con cantidades"
    `PorCertPres = ImpCert / ImpPres`. El capacitador lo aclara expreso: _"no es con la cantidad, es con los importes."_ Y ese % se proyecta hacia arriba: partida → capítulo → **concepto raíz**. El % del concepto raíz es **el número único** que se le presenta a dirección. _(C08 R-4/R-5, video `[01:10]`.)_

!!! note "Si digitás en una fase NO marcada como actual, no suma"
    Probalo: cargá 100 en una fase posterior a la actual y mirá `CanCert` — **sigue igual** (no sumó los 100). Solo acumula hasta la fase naranja. Esto es la otra cara de la Falla silenciosa #1. _(C08 caso 10, video `[01:10]`.)_

---

## 🎥 Mirá el video

| Tema | Minuto |
|---|---|
| Preparar esquema `Certificación | FASES`, inmovilizar columnas | `[00:50]` |
| Ingresar cantidad certificada por fase (`CanCert`) | `[00:50]`–`[01:00]` |
| Cerrar saldo con el botón de tres puntos | `[01:00]` |
| Marcar certificación actual (desde Fechas o Árbol) | `[01:00]` |
| Leer acumulados (`CanCert`/`ImpCert`/`PorCertPres`) | `[01:10]` |

> Video fuente: `gestion_de_proyectos_09_12_2025.mp4`. Relator de soporte de Presto. _El video es complemento: la referencia primaria es la documentación oficial citada en cada tarea._

---

## ⚠️ Lo que Presto NO te avisa (resumen)

- **Si no marcás la certificación actual**, no acumula nada — sin error. _(Tarea 4)_
- **Datos en fases posteriores a la actual** no suman. _(Tarea 5)_
- **El % es por importes**, no por cantidades — no lo leas mal. _(Tarea 5)_
- **Si el dato llega en %**, alguien lo convirtió: pedí la cantidad original. _(antes de empezar)_

👉 Todas, con cómo blindarte, en [5 · Reglas de oro y fallas silenciosas](5-reglas-de-oro.md).

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá lo aprendido"
    Sobre la obra de prueba **BLEND** _(con una licencia que tenga Gestión de Proyectos)_:

    1. Poné el Árbol en esquema `Certificación | FASES` e inmovilizá `CanPres`.
    2. Elegí una partida y certificá **100** en la fase 1 (`1: CanCert`). Verificá que `1: Cert` calcule el importe solo.
    3. **Marcá la fase 1 como certificación actual** (clic derecho → `Certificación actual`) y comprobá que `CanCert` ahora muestra `100`.
    4. Certificá otra cantidad en la **fase 2 sin marcarla** como actual → confirmá que `CanCert` **sigue en 100** (no sumó).
    5. Ahora marcá la fase 2 como actual y mirá que `CanCert` salta al acumulado.

    **Cómo sabés que salió bien:** entendés en vivo que **el acumulado solo sube cuando movés la certificación actual**.

---

📖 **Fuente oficial (RIB):** _Certificación y seguimiento_ — cap. Avance / Certificación por fases, pp. 4, 9. **Complemento interno:** apunte C08 (casos 6–10) · transcripción `gestion_de_proyectos_09_12_2025`.
