# La pantalla de Obra/Almacén: dónde está cada cosa

!!! abstract "Por qué esta página va primero"
    Lo que más cuesta de Presto **no es entender los conceptos — es no perderse entre tantos menús, botones y pestañas.** Esta página es tu mapa de la pantalla donde vas a trabajar todos los días: la ventana **Entregas** y su subventana **Suministros**. Volvé a ella cada vez que una instrucción te diga "andá a tal columna" y no sepas dónde está.

!!! tip "Cómo leemos las rutas de clic en todo el manual"
    En todas las tareas vas a ver rutas escritas así: **`Ver ▸ Entregas`**. Se lee de izquierda a derecha como un camino: primero la **pestaña** de la cinta de arriba (`Ver`), después el **botón** que activás (`Entregas`). Los botones de la cinta funcionan como **interruptores**: al hacerles clic quedan **hundidos/marcados** (activos) y vuelven a salir al hacer clic de nuevo.

!!! warning "Requisito de licencia — sin esto la pantalla no aparece"
    Toda esta pantalla vive en el módulo **Facturación y Control**. Si tu licencia no lo incluye, los botones `Entregas`, `Facturas` y `Suministros` no aparecen y no podés operar este rol. Antes de empezar, **verificá que el módulo de Facturación y Control esté incluido en la licencia** (es un requisito a confirmar al contratar/renovar).

---

## Cómo abrir la pantalla

1. Andá a la **cinta de arriba** y hacé clic en la pestaña **`Ver`**.
2. En el grupo **`Documentos`**, hacé clic en el **botón `Entregas`**. Se abre la ventana: **cada fila de arriba es una Entrega** (un albarán / una recepción de material).
3. Activá también el **botón `Suministros`** (mismo grupo). Aparece, **abajo**, una subventana con el **detalle de qué materiales** trae la entrega que tengas seleccionada arriba.

---

## Las 2 zonas de la pantalla (quedate con esto)

La pantalla de Entregas tiene **dos franjas horizontales**:

1. **Arriba — la cabecera (`Entregas`):** un renglón por documento de recepción. Dice **quién** te entregó (proveedor), **cuándo** (fecha) y **cuánto** (las bases/importes). Es el "sobre" del albarán.
2. **Abajo — el detalle (`Suministros`):** las líneas de materiales del albarán seleccionado arriba. Dice **qué** llegó, **cuánto**, a **qué precio** y a **qué partida** se imputa. Es el "contenido" del sobre.

Vas a saltar todo el tiempo entre esas dos zonas. La subventana de abajo muestra en su título de qué entrega estás viendo el detalle, p. ej. `Suministros EN-001|1302|30/11/2025`.

---

## La cabecera `Entregas` (franja de arriba) — columna por columna

Cada fila es **un documento de entrega**. Estas son las columnas, en el orden en que las vas a ver:

| Columna | Qué es | Ejemplo |
|---|---|---|
| **`Documento`** | El código del albarán / recepción. Lo ponés vos (o lo numera Presto). | `EN-001` |
| **`Info`** | Información descriptiva del documento. | — |
| **`NatC`** | Naturaleza. Se pone sola con el **ícono de proveedor** cuando asignás la Entidad — es tu señal de que el proveedor quedó bien puesto. | (ícono proveedor) |
| **`Entidad`** | El código del proveedor que te entregó. | `1302` |
| **`Resumen`** | El nombre del proveedor (se llena solo al elegir la Entidad). | `MEGA ARIDOS` |
| **`Fecha`** | La fecha en que recibiste el material. | `30/11/2025` |
| **`Divisa`** | La moneda del documento. | `CLP` / `BOB` |
| **`BaseEnt`** | El importe total de la **entrega**. | — |
| **`BaseDest`** | El importe ya **imputado a partidas** (consumo cargado). | — |
| **`BasePed`** | El importe del **Pedido / Orden de Compra** vinculado. El eslabón con Compras. | — |
| **`BaseFac`** | El importe ya **facturado** del documento. El eslabón con la factura. | — |
| **`Obra`** | La obra a la que pertenece el documento. | — |
| **`Nota`** | Nota libre. | — |

!!! note "Las 4 \"bases\" son tu tablero de control del albarán"
    Fijate en `BasePed`, `BaseEnt`, `BaseDest` y `BaseFac`: te dicen de un vistazo en qué etapa está cada recepción. **`BasePed`** = lo que se pidió, **`BaseEnt`** = lo que llegó, **`BaseDest`** = lo que ya se imputó a una partida, **`BaseFac`** = lo que ya se facturó. Cuando las cuatro coinciden, el ciclo de ese material cerró completo.

---

## La subventana `Suministros` (franja de abajo) — columna por columna

Cada fila es **una línea de material** del albarán seleccionado arriba:

| Columna | Qué es | Ejemplo |
|---|---|---|
| **`Código`** | El código del recurso recibido (material, mano de obra, maquinaria, subcontrato). | `MAE00017` |
| **`NatC`** | La naturaleza del recurso (material / mano de obra / etc.). | — |
| **`Resumen`** | La descripción del recurso. | `Bolón selecc c/flete 15 kms` |
| **`Cantidad`** | Cuánto recibiste en esta entrega (puede ser parcial). | — |
| **`Factor`** | Factor de conversión que se aplica a la cantidad. | — |
| **`CanNeta`** | La cantidad neta después del factor. | — |
| **`Ud`** | La unidad de medida. | `m3` |
| **`Divisa`** | La moneda de la línea. | `CLP` |
| **`PorDto`** | El porcentaje de descuento de la línea, si hay. | — |
| **`Precio`** | El precio unitario. Por defecto trae el del objetivo de coste; lo **sobrescribís con el precio real de compra**. | `6.908` |
| **`PrNeto`** | El precio neto después del descuento. | — |
| **`Importe`** | `Cantidad` × `Precio`. Se calcula solo. | `6.908,00` |
| **`Destino`** | La **partida / centro de coste** a la que se imputa el consumo. **Esta columna es la que liga el costo real a la partida.** | — |
| **`Fecha`** | La fecha de imputación del consumo (decide en qué período entra el costo real). | — |
| **`Nota`** | Nota libre de la línea. | — |

!!! danger "La columna `Destino` es la más importante de toda la pantalla"
    Sin `Destino` + fecha, un material que recibiste **no cuenta como costo de ninguna partida**. Puede estar cargado en la entrega, con su precio y todo, pero si no le decís a qué partida pertenece, la obra no lo "ve" como gasto. Acordate de esto: **recibir ≠ imputar.** Lo aprendés a fondo en [2 · Imputar el consumo](2-imputar-consumo.md).

---

## El interruptor naranja 🟧 — tu semáforo de "ya recepcionado"

Cuando cargás un material en una entrega, su **ícono se pone naranja** 🟧 (lo ves en la columna `Info` de la ventana `Conceptos`). Esto significa: **"este recurso ya figura en un documento de entrega"**. Si un recurso **no** tiene la marca naranja, todavía **no lo recepcionaste**. Es la forma más rápida de saber, de un vistazo, qué llegó y qué no.

---

## Capturas de esta pantalla

!!! info "Capturas reales en camino"
    Ya tenemos **2 capturas reales** de la ventana Entregas + Suministros de una obra de prueba. Las que faltan (un suministro desdoblado con `Destino` + fecha imputados, el `ImpReal` subiendo al árbol, y la tabla consolidada `Ver → Suministros` filtrada "sin factura") se agregarán cuando esté disponible la licencia con el módulo de Facturación y Control. Mientras tanto, el texto de cada tarea te orienta paso a paso sin necesidad de la imagen.

---

📖 **Fuente oficial (RIB):** _Manual de Presto completo_ — cap. Facturación / Documentos, pp. 135–139. **Complemento interno:** apunte C07 — Facturación y Entregas (glosario de columnas verificado por captura) · transcripción `FactCon_08_08_2025`.
