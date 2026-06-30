# 6 · Reglas de oro y fallas silenciosas

!!! abstract "Conclusión primero"
    Una **falla silenciosa** es algo que Cost-It **hace mal sin avisarte** y que rompe el presupuesto por dentro. En este rol son especialmente peligrosas porque el presupuesto es un **derivado del modelo**: un código mal puesto, un re-traspaso a ciegas o una baseline no congelada **desfasan el costo de toda la obra** sin que nadie lo note hasta tarde. Esta página junta las **3 reglas de oro** del rol + las **11 fallas silenciosas** con su blindaje.

!!! tip "Leé esto antes de tu primer traspaso de verdad"
    No son conceptos teóricos: son los errores que el equipo **va a cometer** los primeros días. La mayoría tiene la misma raíz: **Cost-It traspasa pero no gobierna** — no congela, no alerta y no sincroniza solo. La disciplina la pone el proceso de Raizant.

!!! info "De dónde sale este contenido"
    Fuente: apunte interno **C01** (§4 Fallas silenciosas y §3 Reglas de comportamiento), verificado contra la **documentación oficial RIB** (_Manual de Cost-it_) y el video `CSE - Cost It - 23/01/2026`.

---

## Las 3 reglas de oro del rol

!!! success "Regla 1 — Para re-sincronizar, siempre `Añadir` (nunca `Exportar`)"
    `Exportar` crea una obra **nueva**; `Añadir` actualiza la que **ya tenés abierta**. Re-sincronizar con `Exportar` por error deja un **archivo paralelo** y el presupuesto bueno sin actualizar. Antes de pulsar `Añadir`, confirmá que **la obra correcta está abierta**.

!!! success "Regla 2 — El presupuesto es tan bueno como la codificación del modelo"
    Cada partida nace de un **valor de parámetro** del modelo. Si el modelo no lleva los códigos de las partidas del estudio (o los lleva mal), el volcado manda la cantidad a la partida equivocada **o a ninguna**. Codificar bien el modelo (1:1 con las partidas) es la condición de que todo funcione.

!!! success "Regla 3 — Nunca aceptes un re-traspaso a ciegas"
    Cost-It no congela ni compara versiones. Antes de `Traspasar`, **revisá las inserciones verdes** y la columna `Acción` (`ninguna`/`actualizar`/`borrar`). Y antes de aceptar cambios grandes, **versioná/congelá** el estudio aprobado (tejido in-house) para poder medir el desvío.

---

## Las 11 fallas silenciosas (y cómo blindarte)

### 🔴 FS-1 — Re-sincronización no gobernada: el presupuesto se desfasa del modelo sin aviso

**Qué pasa:** Cost-It **no avisa** cuando el modelo cambia ni fuerza la re-sync. El ciclo `Añadir → re-asignar → Comprobar → Buscar líneas desaparecidas → Traspasar` es manual. Si nadie lo dispara, el presupuesto queda viejo y la torre de control mide sobre datos falsos. _(video `[03:50]`)_

**Blindaje:** designar un **responsable de re-sync** y un **procedimiento estándar disparado por cada cambio de modelo**. El tejido in-house debe **detectar cambios y agendar** la resincronización. _(Ver [Página 5](5-resincronizar.md).)_

---

### 🔴 FS-2 — Usar `Exportar` cuando se debía usar `Añadir`: obra paralela

**Qué pasa:** los dos botones están **juntos** en el mismo diálogo. `Exportar` crea un `.presto` nuevo; al re-sincronizar por error con él, el estudio bueno **queda sin actualizar** y trabajás sobre un archivo equivocado. _(video `[03:50]`)_

**Blindaje:** procedimiento escrito que fije **`Añadir`** como el único botón aprobado para re-sincronizar, con checklist de "obra correcta abierta antes de `Añadir`".

---

### 🔴 FS-3 — Cantidades negras (fuera del 2%) parecen confiables pero son la declarada

**Qué pasa:** una cantidad **⚫ negra** no es la calculada por Cost-It, es la que **declara el modelo** porque el prisma difería más del 2%. Puede esconder una geometría irregular, un hueco o un recorte mal resuelto. _(video `[01:40]`)_

**Blindaje:** **marcar/filtrar las cantidades negras** para que el presupuestador las revise antes de cerrar; decidir caso por caso si se fuerza el valor BIM exacto. _(Ver [Página 2](2-leer-y-verificar.md).)_

---

### 🔴 FS-4 — Partida verde (tipos mezclados) presupuestada con un único APU

**Qué pasa:** una partida **🟢 verde** agrupa elementos de **tipos distintos** que suelen necesitar APUs distintos; el verde es solo **advertencia**, no bloqueo. Si la presupuestás con un único precio, el costo sale mal. _(video `[01:10]`–`[01:20]`)_

**Blindaje:** paso **obligatorio** de revisión del semáforo verde; usar **discriminador** (antes de exportar) o **`Desglosar`** (en Presto). No aceptar partidas verdes sin decisión explícita. _(Ver [Página 3](3-afinar-y-desglosar.md).)_

---

### 🔴 FS-5 — El match por código depende 100% de la codificación; las grises quedan fuera en silencio

**Qué pasa:** al volcar al estudio, las líneas que no encuentran su partida quedan **grises** y **silenciosamente fuera del presupuesto**. Un código mal puesto manda la cantidad a la partida equivocada o a ninguna. _(video `[03:50]`)_

**Blindaje:** **estándar de codificación Raizant** (modelo ↔ partidas 1:1) + una validación que **liste las líneas grises** (sin match) y los conceptos del estudio que quedaron **sin cantidad** tras el traspaso. _(Ver [Página 4](4-codificar-y-volcar.md).)_

---

### 🔴 FS-6 — Cost-It no congela baseline: los re-traspasos sobreescriben sin dejar versión previa

**Qué pasa:** no hay forma nativa de comparar "antes vs después" de un re-traspaso más allá de mirar las inserciones verdes en el momento. Una vez que traspasás, la versión anterior se perdió. _(video `[03:50]`–`[04:00]`)_

**Blindaje:** **versionar/congelar el estudio aprobado** (snapshot por el tejido in-house) antes de aceptar cambios del modelo, para poder medir el desvío. Definir el punto exacto del ciclo donde se congela.

---

### 🟠 FS-7 — Código de montaje (parámetro de tipo) no permite códigos distintos para elementos del mismo tipo

**Qué pasa:** el "código de montaje" es **de tipo** → cambiarlo en un elemento **cambia todos los del tipo**. Si dos elementos del mismo tipo deben ir a partidas distintas, no se puede con este parámetro, y al devolver a Revit entra en conflicto. _(video `[02:10]`)_

**Blindaje:** estándar que use un **parámetro de ejemplar personalizado** como agrupador cuando se necesiten códigos por elemento. Documentar cuándo aplica cada uno.

---

### 🟠 FS-8 — `seleccionar`/`localizar` rotos en modelo central: la verificación visual falla sin error claro

**Qué pasa:** sobre un modelo central/federado, `seleccionar en el modelo` y `Localizar` **no marcan nada** (límite de la API de Revit) y no dan un error claro. Parece que no funciona. _(video `[02:00]`)_

**Blindaje:** documentar que en modelo central la verificación exige **abrir el archivo individual** que indica la columna **`Archivo`** (esquema `Localización BIM`). Conservar siempre ese esquema. _(Ver [Página 2](2-leer-y-verificar.md).)_

---

### 🟠 FS-9 — Elementos sin código se cuelan al presupuesto (o quedan fuera) según una casilla fácil de pasar por alto

**Qué pasa:** la casilla **"Incluir elementos sin código"** decide todo: **marcada** trae genéricos en **🔴 rojo**; **desmarcada** los **excluye en silencio**. Es fácil no darse cuenta de en qué estado quedó. _(video `[00:30]`)_

**Blindaje:** fijar el valor de esa casilla **por tipo de exportación** en la plantilla `.CostItLayout`, y revisar el recuento de "elementos con código" (botón de la [Página 1](1-traspaso-inicial.md), Tarea 4) antes de exportar.

---

### 🟠 FS-10 — Configuración de exportación perdida entre sesiones si no se guarda el `.CostItLayout`

**Qué pasa:** categorías, scripts y discriminadores **se rehacen a mano** cada vez si no los guardaste. Distintas personas configuran distinto → resultados que no se pueden comparar. _(video `[03:10]`)_

**Blindaje:** **plantillas `.CostItLayout` oficiales versionadas** como parte del estándar BIM de Raizant. _(Ver [Página 3](3-afinar-y-desglosar.md).)_

---

### 🟡 FS-11 — Dependencia de versión Cost-It ↔ Revit no verificada para Revit 2027

**Qué pasa:** el curso usa **Cost-It 25.05.00** con Revit 25/26 ("no versiones anteriores"). El enfoque to-be de Raizant apunta a **Revit 2027** → si no hay una versión de Cost-It compatible, **el puente no opera**. _(video `[00:00]`, captura)_

**Blindaje:** **confirmar con RIB** la versión de Cost-It compatible con Revit 2027 **antes** de comprometer el flujo. Sin compatibilidad, no hay Revit → Presto.

---

## Tabla resumen para tener a mano

| # | La trampa | El blindaje en una frase |
|---|---|---|
| FS-1 | Re-sync no gobernada → desfase silencioso | Responsable de re-sync + disparo por cada cambio |
| FS-2 | `Exportar` en vez de `Añadir` → obra paralela | `Añadir` es el único botón aprobado para re-sync |
| FS-3 | Cantidad negra parece confiable | Marcá y revisá las negras antes de cerrar |
| FS-4 | Partida verde con un solo APU | Desglosá o discriminá toda partida verde |
| FS-5 | Líneas grises fuera del presupuesto | Validá grises + conceptos sin cantidad |
| FS-6 | No congela baseline | Versioná el estudio antes de aceptar cambios |
| FS-7 | Código de montaje cambia todo el tipo | Parámetro de ejemplar para códigos por elemento |
| FS-8 | `seleccionar`/`localizar` rotos en central | Abrí el archivo de la columna `Archivo` |
| FS-9 | Casilla "incluir sin código" | Fijala en el `.CostItLayout` + revisá el recuento |
| FS-10 | Config perdida entre sesiones | Plantillas `.CostItLayout` versionadas |
| FS-11 | Versión Cost-It ↔ Revit 2027 | Confirmar compatibilidad con RIB antes de migrar |

---

## La idea de fondo

!!! note "Por qué tu rol es el cimiento de toda la torre de control"
    Casi todas estas fallas tienen la misma raíz: **Cost-It traspasa, pero no gobierna.** No congela, no alerta, no sincroniza solo, no valida la codificación. Eso no es un defecto — es la frontera entre lo que compra Raizant (el commodity: Cost-It) y lo que construye in-house (el tejido conectivo: gobierno de re-sync, congelado de baseline, validación de codificación). Tu trabajo, hecho con disciplina, es **la primera fuente de verdad de toda la cadena de costo**: si el modelo está bien y se sincroniza con gobierno, todo lo que viene aguas abajo (compras, costo real, valor ganado) descansa sobre datos confiables.

---

📖 **Fuente:** apunte interno C01 (§3 reglas, §4 fallas silenciosas) · verificado contra _Manual de Cost-it_ (RIB) y el video `CSE - Cost It - 23/01/2026`.
