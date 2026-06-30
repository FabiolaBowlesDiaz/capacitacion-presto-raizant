# 2 · Contratos: cotizar y adjudicar

!!! abstract "Conclusión primero"
    Acá aprendés el camino **B** — el profesional. En vez de comprarle directo a un proveedor, armás un **lote de compra** (un "contrato"), le pedís precio a **varios proveedores**, los **comparás lado a lado**, le **adjudicás** al mejor y Presto **genera las órdenes de compra solo**. Es más pasos que el pedido manual, pero deja documentado que comparaste ofertas antes de gastar.

!!! tip "Antes de arrancar, tené a mano el mapa"
    Esta es la página con más pantallas. Si te perdés, abrí **[🗺 La pantalla de Compras](interfaz.md)** — la zona de `Contratos` y su subventana comparativa están explicadas ahí.

!!! warning "Requisito de licencia"
    Igual que todo el rol, esto **solo funciona con el módulo de Contratación** en la licencia. Además, **exportar la solicitud de precios está bloqueado en la versión demo** — verificá que tu licencia lo permita.

!!! info "De dónde sale este contenido"
    Fuente principal: **documentación oficial RIB** — _Tutorial de Presto_ (pp. 19–24, ejercicio completo de compras paso a paso) y _Manual de Presto completo_ (pp. 126–130, Contratos). Complemento: apunte C06 (casos 8–15) y transcripción del video.

---

## El flujo completo de un vistazo

```
1. Marcar qué se compra (suministros)
2. Agrupar en lotes (rellenar grupos)        ─┐
3. Calcular recursos                          ├─ preparación
4. Crear los contratos                       ─┘
5. Asociar proveedores al contrato
6. Pedirles precio (solicitud de precios)    ─┐
7. Cargar/importar los precios               ├─ cotización
8. Comparar                                  ─┘
9. ADJUDICAR al mejor                         ── decisión
10. Pasar a pedido (Presto genera las OCs)    ── compra
```

---

## Tarea 1 — Marcar qué conceptos se van a comprar

**Qué es:** decirle a Presto cuáles partidas/recursos vas a comprar o subcontratar. Solo lo marcado entra al circuito de compras.

📖 **Fuente oficial:** Tutorial de Presto, p. 20 — _"Los conceptos que se van a comprar o subcontratar directamente deben marcarse como suministros."_

**Paso a paso:**

1. En la ventana **`Presupuesto`** o **`Conceptos`**, hacé **clic derecho sobre el concepto** que vas a comprar → elegí **`Suministro`**.
2. **La señal de que salió bien:** el ícono del concepto **queda con fondo naranja** 🟧.
3. Repetí con cada material/partida que vayas a comprar.

!!! note "La marca naranja es tu lista de compras"
    A partir de acá, el naranja 🟧 te dice de un vistazo qué está en el circuito de compras y qué no. _(Tutorial p. 20.)_

---

## Tarea 2 — Agrupar los suministros en lotes ("rellenar grupos")

**Qué es:** juntar los materiales parecidos en **grupos de compra**, para cotizar cada grupo con los proveedores que correspondan (ej. todos los áridos juntos, toda la cerámica junta).

📖 **Fuente oficial:** Tutorial de Presto, p. 20 — _"Para que funcione el proceso de clasificación y búsqueda de proveedores cada suministro tiene que estar asociado a un grupo de compras."_

**Paso a paso:**

1. En la ventana **`Conceptos`**, elegí un esquema que muestre los recursos (ej. `[Naturalezas básicas]`).
2. En la **cinta de arriba**, andá al apartado de **Contratación** y elegí **`Rellenar grupos`**.
3. Presto rellena la columna **`Grupo`** de cada concepto. El criterio recomendado del video: **las primeras 3 letras del código**.
4. Si un grupo quedó mal, lo cambiás a mano: botón **sugerir** sobre el campo `Grupo` de ese concepto.

!!! tip "Preseleccioná solo los recursos"
    Antes de `Rellenar grupos`, seleccioná solo los recursos (no los capítulos ni las partidas), para que no se agrupen cosas que no son materiales. _(C06 caso 8.)_

---

## Tarea 3 — Calcular recursos y crear los contratos

**Qué es:** que Presto calcule cuánto se necesita de cada material (por fase) y arme un **contrato (lote) por grupo**.

📖 **Fuente oficial:** Tutorial de Presto, pp. 20–21 + Manual p. 127 — _"Se genera un contrato por cada grupo seleccionado."_

**Paso a paso:**

1. En la cinta, elegí **`Calcular recursos`** → botón **`Defecto`** → marcá **`Por fases, agrupadas por`** → elegí **`Conceptos.Grupo`** → `Aceptar`. _(Esto NO cambia las cantidades del presupuesto.)_
2. Elegí **`Crear contratos`**. Tenés dos opciones:
   - **Un contrato por fase** → tabla densa (un contrato por cada fase y recurso).
   - **Desmarcado** → versión **compacta** (un solo contrato por grupo, con la cantidad total). _(Recomendado para empezar.)_
3. Abrí la ventana **`Contratos`** (cinta `Ver ▸ Documentos ▸ Contratos`). Vas a ver tus lotes (ej. `MAE` = áridos).

!!! note "Los contratos nacen 'provisionales' (rojo)"
    La doc avisa: _"Los contratos aparecen en estado rojo, indicando que son provisionales… Cambie el estado de los contratos a definitivos eligiendo `Estado negro`."_ 📖 _(Tutorial p. 21.)_ Mientras están en rojo, algunos cálculos e informes no salen.

---

## Tarea 4 — Asociar los proveedores que van a cotizar

**Qué es:** decirle a cada contrato a qué proveedores les vas a pedir precio.

📖 **Fuente oficial:** Manual p. 128 + Tutorial p. 21 — opción **`Buscar y asociar proveedores`**.

**Paso a paso:**

1. En la ventana `Contratos`, hacé **clic derecho sobre la fila del contrato** (ej. `E07`) → **`Buscar y asociar proveedores`**.
2. Marcá los proveedores que van a cotizar y `Aceptar`.
3. **La señal de que salió bien:** en la subventana **`Suministros`** del contrato aparecen **columnas nuevas por cada proveedor** (`1: Precio`, `2: Precio`…). La cabecera de cada columna muestra el código del proveedor.

!!! tip "Otra forma de asociar"
    También podés **arrastrar** un proveedor desde la ventana `Entidades` hasta el contrato. _(Manual p. 128.)_

---

## Tarea 5 — Pedirles el precio (solicitud de precios)

**Qué es:** mandarle a cada proveedor un archivo para que complete sus precios, y después cargarlo de vuelta.

📖 **Fuente oficial:** Manual pp. 128–129 + Tutorial pp. 22–23.

**Paso a paso:**

1. Con el contrato seleccionado: **cinta `Archivo ▸ Exportar ▸ Solicitud de precios`** → formato **Excel** (o "Obra de Presto") → elegí la carpeta destino.
2. Presto genera **un archivo por proveedor**, con **todo bloqueado salvo la columna `Precio`** (el proveedor solo puede escribir precios). Si el proveedor tiene email cargado, Presto puede generar el correo solo.
3. El proveedor completa sus precios y te devuelve el archivo.
4. Para cargarlo: **cinta `Archivo ▸ Importar ▸ Solicitud de precios`** → elegí el archivo. Presto rellena la columna de ese proveedor.

!!! warning "Dos límites a tener en cuenta"
    - Se importa **un archivo a la vez** (no podés cargar dos Excel juntos). _(Manual p. 129.)_
    - Si son pocos proveedores, podés **saltarte el Excel** y teclear los precios directo en las columnas `1: Precio` / `2: Precio`. _(C06 caso 10.)_

---

## Tarea 6 — Comparar las ofertas

**Qué es:** mirar lado a lado lo que cotizó cada proveedor y ver cuál conviene.

📖 **Fuente oficial:** Manual p. 129 — _"La comparación de contratos se puede realizar directamente en la ventana de contratos, donde se pueden comparar los totales entre sí y con el importe objetivo de cada contrato."_

**Paso a paso:**

1. En la subventana `Suministros` del contrato, mirá las columnas **`1: Importe`** vs **`2: Importe`** (y las que haya). Cada una es el total de un proveedor.
2. Compará también contra el **`ImpObj`** (importe objetivo): te dice si la mejor oferta está por encima o por debajo de lo que esperabas pagar.
3. _(Opcional)_ Usá el informe **`Contratos comparativo`** para verlo formal.

---

## Tarea 7 — Adjudicar al proveedor elegido

**Qué es:** decidir el ganador. Es el paso clave — sin adjudicar, no podés generar las órdenes de compra.

📖 **Fuente oficial:** Manual p. 130 + Tutorial p. 24 — _"El contrato se adjudica rellenando el campo `Proveedor`. Puede realizarse con el botón de sugerir o con la opción `Adjudicar` sobre la cabecera del proveedor."_

**Paso a paso:**

1. Hacé **clic derecho sobre la columna del proveedor elegido** (ej. sobre `2: Precio`) → **`Adjudicar`**.
   _(O bien: en la columna `Proveedor` de la cabecera, botón sugerir → elegí el proveedor.)_
2. **La señal de que salió bien:** se llenan las columnas **`Proveedor`** (su código) y **`DOC Proveedor del contrato`** (su nombre), y el total contratado aparece en **`Cont`**.

!!! danger "Regla dura: sin adjudicar no hay pedido"
    `Pasar a pedido` queda **deshabilitado (gris)** hasta que el contrato tenga proveedor adjudicado. Es la **única validación de secuencia fuerte** del módulo. _(C06 R-5 / video `[01:50]`.)_

!!! note "El precio adjudicado se congela en el contrato"
    Dato oficial útil: _"el precio se guarda con el contrato al adjudicarlo y el precio de oferta puede variar posteriormente sin afectar al precio del contrato."_ 📖 _(Manual p. 127.)_ O sea: una vez adjudicado, aunque el proveedor cambie su oferta, tu contrato mantiene el precio con el que ganó.

---

## Tarea 8 — Pasar a pedido (Presto genera las OCs)

**Qué es:** convertir el contrato adjudicado en órdenes de compra reales, automáticamente.

📖 **Fuente oficial:** Tutorial p. 24 — _"Elija `Pasar a pedido` sobre el contrato… Se crean los pedidos… para su proveedor, con los suministros al precio ofertado. Se genera un pedido para cada fase en la que son necesarios los suministros."_

**Paso a paso:**

1. **Clic derecho sobre la fila del contrato adjudicado** → **`Pasar a pedido`**.
2. Presto genera **un lote de pedidos** (uno por cada fase en que se necesita el material), todos apuntando al proveedor adjudicado. Cada pedido lleva en `OrgContrato` el contrato del que salió (trazabilidad).
3. Las **cantidades** salen de la planificación y las **fechas** de cada fase. Abrí `Pedidos` para verlos; podés borrar los que todavía no vayas a emitir.

!!! danger "Falla silenciosa: los pedidos generados siguen siendo editables"
    Aunque adjudicaste a un proveedor, después podés **cambiarle el proveedor o la cantidad** a cualquier OC generada — y Presto no deja rastro de que difiere de lo adjudicado. Regla: si cambiás algo post-adjudicación, documentalo por fuera. _(C06 FS-9 / video `[01:50]`.)_

---

## Tarea 9 — Dejar el contrato "a firme" y sacar el informe

**Qué es:** proteger el contrato y emitir el documento formal de adjudicación.

📖 **Fuente oficial:** Tutorial p. 24 (informes de Contratación) + C06 caso 14.

**Paso a paso:**

1. **Clic derecho sobre la fila del contrato** → **`Estado verde`** ("a firme"). Protege los campos y **habilita el informe formal**.
2. Sacá el informe desde **`Informes ▸ 07 Contratación`**. Disponibles (Tutorial p. 24):
   - _"Compara los lotes ofertados por distintos proveedores"_ (la comparativa).
   - _"Contratos con las características principales de la oferta adjudicada"_.
   - _"Desviaciones de cantidades, previsto, contratado y pedido"_.
   - _"Pedidos en firme a proveedores"_.

!!! warning "Recordá: verde protege, no aprueba"
    El estado verde **no es la autorización de tu jefe** — solo bloquea los campos. La aprobación de la compra vive en el proceso de Raizant, no en este botón. _(Ver [Fundamentos](0-fundamentos.md).)_

---

## ⚠️ Lo que Presto NO te avisa (resumen)

- **Cotizar es opcional** → se puede comprar directo sin pasar por acá. Que se cotice lo pone el proceso. _(Fundamentos)_
- **Los pedidos generados se pueden editar** tras adjudicar → lo comprado puede diferir de lo adjudicado, sin rastro. _(Tarea 8)_
- **El export de solicitud de precios** está bloqueado en demo y el email depende de Outlook. _(Tarea 5)_
- **El informe de contrato a Word** fue retirado en algunas versiones → verificá cuáles trae tu licencia.

👉 Todas, con cómo blindarte, en [4 · Reglas de oro y fallas silenciosas](4-reglas-de-oro.md).

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá lo aprendido"
    Sobre la obra **BLEND** _(con licencia que tenga Contratación)_:

    1. Marcá 3 materiales como **suministro** (que queden naranja 🟧).
    2. `Rellenar grupos` y `Crear contratos` → revisá que aparezca tu lote en la ventana `Contratos`.
    3. Asociá **2 proveedores** y cargales precios distintos a mano (sin Excel).
    4. Compará `1: Importe` vs `2: Importe` y **adjudicá** al más barato.
    5. `Pasar a pedido` y verificá en `Pedidos` que se generaron las OCs con el proveedor ganador.

    **Cómo sabés que salió bien:** tras adjudicar, las columnas `Proveedor` y `Cont` se llenan; y `Pasar a pedido` deja de estar gris y genera las OCs.

---

📖 **Fuentes oficiales (RIB):** _Tutorial de Presto_, pp. 19–24 (ejercicio de compras). · _Manual de Presto completo_, pp. 126–130 (Contratos, asociar proveedores, adjudicar). · Complemento: apunte C06 (casos 8–15) · transcripción `Contratacion_30_12_2025`.
