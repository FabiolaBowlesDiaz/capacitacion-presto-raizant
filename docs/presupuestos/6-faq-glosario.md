# 6 · Preguntas frecuentes y glosario

## Preguntas frecuentes (FAQ)

??? question "¿Por qué no me aparece la columna `CanPres` (o cualquier otra)?"
    Casi siempre porque la ventana está en **otro esquema de columnas**, no en `Presupuesto`. Cambialo en el desplegable de arriba a la derecha de la pestaña. Si ocultaste una columna por accidente, el botón `Defecto` (en `Elegir columnas visibles`) la trae de vuelta.

??? question "¿Por qué los totales me salen en cero o vacíos?"
    El botón **`Automático`** (menú `Inicio`, sección Calcular) probablemente está desactivado. Cuando está apagado, las columnas de consolidación dejan de calcular. Reactivalo o usá `Recalcular`.

??? question "¿Por qué un precio cambió si yo no lo toqué?"
    Porque en Presto **un recurso = un precio**, y ese precio se comparte en todas las partidas donde se usa. Si alguien cambió el precio del cemento, cambió en todos los APU que lo llevan. Es la "única fuente de verdad" funcionando — pero hay que tenerla presente.

??? question "¿Por qué la búsqueda (Ctrl+B) no encuentra nada?"
    Porque busca por la **columna donde está el cursor**. Si querés buscar un texto de la descripción, primero hacé clic en una celda de la columna `Resumen`; si buscás un código, parate en `Código`.

??? question "¿Qué significan los colores de los precios?"
    **Negro** = precio base (tecleado a mano). **Magenta** = precio calculado (tiene un APU debajo, o hubo conversión de moneda). **Cantidad en magenta** = respaldada por líneas de medición. Los colores son información, no adorno.

??? question "¿Puedo importar mi presupuesto desde Excel?"
    Sí. En este nivel se hace por copiar/pegar (alineando las columnas). El método más eficiente, **Excel2Presto**, se ve en [Presupuesto intermedio](2-intermedio.md). Ojo: Excel2Presto **solo lee archivos locales, no de OneDrive**.

??? question "¿Qué es el PEM y dónde lo veo?"
    Es el **Presupuesto de Ejecución Material**: el total de la obra antes de gastos generales, utilidad e IVA. En Presto es el importe del **concepto raíz** (el tope del árbol).

??? question "¿Cómo marco una partida que es un subcontrato (precio cerrado, sin APU)?"
    En Presto no hay una "naturaleza subcontrato": se marca con la propiedad **Suministro** (clic derecho sobre la partida → Suministro; el ícono se pone naranja 🟧). Se ve en [Presupuesto intermedio](2-intermedio.md).

---

## Glosario — la jerga traducida

| Término | Qué significa |
|---|---|
| **Obra / `.presto`** | Un archivo de Presto = una base de datos completa e independiente de esa obra. |
| **Concepto** | Cualquier fila del árbol: un capítulo, una partida o un recurso. Tiene un código único. |
| **Capítulo / subcapítulo** | Agrupadores de la estructura (ej. "Obra gruesa" → "Hormigones"). No se miden; suman lo que tienen adentro. |
| **Partida** | La unidad que se mide y se cobra (ej. "m³ de hormigón"). Es la hoja que se valoriza. |
| **Recurso** | Lo más básico: un material, mano de obra o maquinaria que compone una partida. |
| **APU** | Análisis de Precio Unitario: la receta de una partida (sus recursos con cantidad y precio). |
| **Naturaleza (NATSE)** | El "tipo" de un concepto: capítulo, partida, material, mano de obra, maquinaria, otros. Define cómo sale en los informes. |
| **Línea de medición** | El desglose de la cantidad de una partida en parciales (por ejes, sectores). Respalda la cantidad. |
| **Rendimiento** | La cantidad de un recurso **por una unidad** de la partida (ej. 350 kg de cemento por m³). Distinto del **metraje** (cantidad total de la partida en la obra). |
| **Metraje** | La cantidad total de una partida en toda la obra. Lo pone arquitectura (Revit); el precio lo pone presupuestos. |
| **Moneda de consolidación** | La moneda principal de la obra. Todo se consolida a ella. |
| **Paridad** | La equivalencia entre dos monedas (manual; Presto no se conecta a tipos de cambio). |
| **Concepto raíz** | El concepto del tope del árbol, que consolida el total de la obra (el PEM). |
| **PEM** | Presupuesto de Ejecución Material: el costo de la obra antes de gastos generales, utilidad e IVA. |
| **Esquema de columnas** | La vista de columnas de cada ventana. Para presupuesto, usar el esquema `Presupuesto`. |
| **Baseline / línea base** | El presupuesto congelado al iniciar la obra, contra el que se mide el desvío. |
| **BC3 / FIEBDC** | El formato estándar de intercambio de presupuestos (un archivo `.bc3`). Sirve para importar/exportar entre programas. |
| **Código2** | Un código secundario por concepto, usado como puente hacia el plan de cuentas de contabilidad (Syneco). |
| **Suministro** | La propiedad que marca una partida como subcontrato / precio cerrado (ícono naranja). |
| **Excel2Presto** | El complemento que importa un itemizado de Excel armando el árbol automáticamente. |
| **EVM / Valor ganado** | El método para medir salud de obra (CPI, SPI): compara lo planeado, lo avanzado y lo gastado. |
| **Auditoría / punto de restauración** | El historial de cambios de la obra; permite volver a un estado anterior (creando una copia). |

---

!!! tip "¿Falta una pregunta o un término?"
    Esta página crece con las dudas reales del equipo durante la adopción. Si te trabaste con algo que no está acá, avisá para agregarlo (ver [Cómo mantener este sitio](../contribuir.md)).
