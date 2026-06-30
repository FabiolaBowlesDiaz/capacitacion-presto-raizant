# 5 · Reglas de oro y fallas silenciosas

!!! abstract "Conclusión primero"
    Una **falla silenciosa** es un error que Presto **acepta sin avisarte** y que rompe la salud de la obra por dentro. En este rol son especialmente peligrosas porque tu trabajo alimenta el costo real, y un dato mal cargado **infla o desinfla la rentabilidad** sin que nadie lo note hasta tarde. Esta página junta las 8 trampas del rol Obra/Almacén con la regla concreta para blindarte de cada una.

!!! tip "Leé esto antes de cargar tu primera entrega de verdad"
    No son conceptos teóricos: son los errores que el equipo **va a cometer** en sus primeros días. Tenerlos presentes te ahorra rehacer trabajo y, sobre todo, evita que la dirección tome decisiones con números falsos.

!!! info "De dónde sale este contenido"
    Fuente: apunte interno **C07 — Facturación y Entregas** (§4 Fallas silenciosas) verificado contra la documentación oficial RIB y el video `FactCon_08_08_2025`.

---

## Las 3 reglas de oro del rol

!!! success "Regla 1 — Todo lo que se consume se imputa, y con su precio"
    El costo real **solo existe** cuando imputás el consumo a la partida (`Destino` + fecha + precio). Un albarán cargado pero **sin imputar** deja el costo incompleto → el CPI se infla → **la obra se ve sana sin estarlo**. **Recibir no es imputar.**

!!! success "Regla 2 — La fecha de imputación tiene que caer en el período actual"
    La fecha del consumo decide en qué período entra el costo. Si cae **fuera de la fase de certificación actual**, Presto **no calcula** y solo lo "avisa" pintando la fecha de **gris**. Avance y costo del **mismo período**.

!!! success "Regla 3 — El precio real vive en el documento, no pisa el presupuesto"
    El precio real de compra que cargás en la entrega **no modifica** el presupuesto ni el objetivo de coste. Por eso podés (y debés) registrar lo que de verdad costó, para medir el desvío, sin miedo a arruinar la línea base.

---

## Las 8 fallas silenciosas (y cómo blindarte)

### 🔴 FS-1 — Presto copia el proveedor y la fecha de la entrega anterior

**Qué pasa:** al crear una entrega nueva, Presto **hereda la Entidad y la Fecha** del documento anterior (no usa el reloj de Windows). Si no corregís, la entrega queda con el **proveedor equivocado** o la **fecha equivocada**, sin aviso. _(video `[01:10]`)_

**Blindaje:** en **cada** entrega nueva, **confirmá a mano el proveedor y la fecha**, aunque ya aparezcan llenos. Sospechá de cualquier fila con fecha idéntica a la de arriba.

---

### 🔴 FS-2 — Fecha de imputación fuera de fase: no calcula y solo se ve gris

**Qué pasa:** si la fecha de imputación cae fuera de la fase de certificación actual, el costo real **no suma** por más que recalcules. El único síntoma es la **fecha en gris**. _(video `[02:30]`)_

**Blindaje:** después de imputar, **mirá que ninguna fecha quede gris**. Si la ves gris, o corregís la fecha o se mueve la fase actual. No cierres el período con fechas grises pendientes.

---

### 🔴 FS-3 — Presto no te dice de forma confiable cuánto falta por recibir

**Qué pasa:** al recibir una parcialidad de una compra mayor, la sugerencia de saldo pendiente **falló** en el video. El control "comprado vs. recibido" **no es automático**. _(video `[01:20]`)_

**Blindaje:** mirá el saldo en las ventanas que sí lo tienen (`Entidades → [Proveedores] Importes`, `Insumos → Existencias`, informe de desviaciones — ver [Tarea 4](4-del-pedido-a-la-factura.md)). **No confíes** en que Presto te frene si recibís de más o de menos.

---

### 🔴 FS-4 — El enlace OC ↔ Entrega ↔ Factura no es obligatorio: entregas huérfanas

**Qué pasa:** Presto **no obliga** a que una entrega tenga su OC detrás ni a pasarla a factura. Podés dejar entregas **huérfanas** (sin pedido o sin factura) y quedan mudas; detectarlas exige filtrar a mano. _(video `[03:40]`, `[02:40]`)_

**Blindaje:** control periódico de entregas sin factura (`Ver → Suministros`, filtrar `factura` vacío). El proceso de Raizant debe **obligar** el enlace y **alertar** las huérfanas — es tejido in-house, no algo que Presto haga solo.

---

### 🔴 FS-5 — Sugerencia de `Destino` vacía si la partida no tiene la propiedad

**Qué pasa:** si la partida no quedó marcada con la propiedad `Destino` (paso del armado de la obra), al imputar la sugerencia sale **en blanco** y no podés ligar el costo. _(video `[01:40]`)_

**Blindaje:** si la sugerencia de `Destino` sale vacía, **no es tu error** → avisá a quien armó la obra (Enrique) que esa partida necesita la propiedad `Destino`. Checklist de setup de obra antes de habilitar las entregas.

---

### 🟠 FS-6 — Proveedor creado a mano genera un vencimiento "contado" fantasma

**Qué pasa:** al pasar a factura un proveedor creado a mano sin sus datos de pago, Presto añade un vencimiento "contado" por defecto que hay que **borrar y recrear** con el plazo real. _(video `[02:50]`)_

**Blindaje:** cargá los proveedores **antes**, con su divisa y condición de pago completas (plantilla estándar de alta de proveedor). No los crees al vuelo sin parámetros.

---

### 🟠 FS-7 — Divisa en blanco en proveedores creados a mano

**Qué pasa:** un proveedor creado a mano **sin divisa** hace que el documento de entrega salga sin moneda; hereda la general pero el cálculo se ve raro. _(video `[01:30]`)_

**Blindaje:** forzar la **divisa** (BOB para Raizant) al dar de alta cualquier entidad.

---

### 🟠 FS-8 — Cantidad cargada "a ojo" sin cruzar con la necesidad real

**Qué pasa:** el digitador puede teclear una cantidad cualquiera y Presto la acepta. El dato correcto (cuánto necesita cada partida por período) vive en la pestaña `Recursos`, pero hay que consultarlo a mano. _(video `[01:00]`)_

**Blindaje:** cruzá la cantidad recibida con lo presupuestado/pedido antes de confirmar. El tejido in-house puede precargar la cantidad esperada desde la OC y resaltar desvíos.

---

## Tabla resumen para tener a mano

| # | La trampa | El blindaje en una frase |
|---|---|---|
| FS-1 | Copia proveedor/fecha del anterior | Confirmá proveedor y fecha en cada entrega |
| FS-2 | Fecha fuera de fase = no calcula (gris) | No dejes fechas grises sin resolver |
| FS-3 | No avisa cuánto falta por recibir | Mirá el saldo en `Entidades`/`Insumos`/informe |
| FS-4 | No obliga OC↔Entrega↔Factura | Control periódico de huérfanas |
| FS-5 | Sugerencia de Destino vacía | Avisá: falta la propiedad Destino en la partida |
| FS-6 | Vencimiento "contado" fantasma | Cargá proveedores con datos de pago antes |
| FS-7 | Divisa en blanco | Forzá la divisa (BOB) al alta |
| FS-8 | Cantidad a ojo | Cruzá con lo presupuestado/pedido |

---

## La idea de fondo

!!! note "Por qué tu rol es donde más importa la disciplina"
    Casi todas estas fallas tienen algo en común: Presto **te deja hacer la cosa mal** y no te frena. Eso es porque **Presto no es un ERP** — no tiene roles, ni aprobaciones, ni te obliga a encadenar documentos. La salud de la obra en tiempo real depende de que el dato entre **bien y a tiempo**. Por eso tu trabajo, hecho con disciplina, vale tanto: sos el primer eslabón de confianza de toda la torre de control.

---

📖 **Fuente:** apunte interno C07 — Facturación y Entregas (§4) · verificado contra _Manual de Presto completo_ y el video `FactCon_08_08_2025`.
