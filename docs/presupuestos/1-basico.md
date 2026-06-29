# 1 · Presupuesto básico

!!! abstract "Conclusión primero"
    En esta sección armás un presupuesto **de cero**: configurás el entorno, creás la obra, levantás la estructura de capítulos y partidas, le decís a Presto qué es cada cosa (naturalezas), definís las monedas, armás tu primer APU y sacás un informe. Es el **primer día** del curso y la base de todo lo demás.

!!! info "De dónde sale este contenido"
    Apunte de capacitación **CL-1 (Presupuesto Básico)** + **Manual de Presto completo (RIB)**. Cada paso cita el minuto `[hh:mm]` del video para que puedas ir a verlo. Lo marcado con ⚠️ `(?)` es un nombre de botón tomado del audio, pendiente de confirmar con captura.

---

## Antes de empezar: lo que necesitás

| Necesitás | Por qué |
|---|---|
| **Presto instalado** (idealmente con licencia) | La ventana de Activación muestra licencia, versión y módulos |
| **Las tres ventanas abiertas**: Árbol, Presupuesto, Conceptos | Son las tres fundamentales (menú `Ver`) |
| **El esquema de columnas en `Presupuesto`** | Si estás en otro esquema, te faltan columnas clave (le pasó a Enrique en vivo) |
| **Un borrador del itemizado** (un Excel: Código · Unidad · Descripción · Cantidad) | Si vas a copiar/pegar en vez de teclear todo |

---

## Tarea 1 — Configurar el entorno (una sola vez por computadora)

**Qué es:** dejar Presto configurado como conviene, antes de trabajar. Se hace una vez por estación.

**Por qué importa:** trabajar siempre en MAYÚSCULAS es la base de una codificación consistente entre proyectos — prerrequisito de que los filtros y las búsquedas funcionen.

**Paso a paso** `[00:00]`:

1. Menú `Archivo → Activación` _(opcional)_: muestra el número de licencia, versión y módulos contratados. Útil para pedir soporte. Cerrar con `Aceptar` (no cambia nada).
2. Menú `Archivo → Entorno de trabajo → Generales`. Dejá marcadas el **ajuste automático de ancho de columnas** y el **cálculo automático** (ambas recomendadas).
3. **Desmarcá "aceptar códigos en minúsculas"** ⚠️ `(?)`. Así Presto pasa todo código a mayúsculas. Los filtros y la búsqueda distinguen mayúsculas de minúsculas.
4. **Desmarcá "actualizar solo la ventana de tabla activa"** ⚠️ `(?)`. Así un cambio en una tabla se refleja al toque en las demás.
5. En `Márgenes`, dejá los recuadros en blanco por ahora.

---

## Tarea 2 — Crear una obra nueva (con auditoría)

**Qué es:** arrancar un presupuesto desde cero.

**Paso a paso** (`Archivo → Nuevo`) `[00:10]`–`[00:20]`:

1. En **`Camino`**: elegí la carpeta donde se guarda. El botón `Defecto` apunta al directorio de obras predeterminado.
2. **`Nombre`**: el que quieras (en el video: "presupuesto básico del 27 de noviembre").
3. **`Plantilla`**: elegí **"sin plantilla"** para partir de cero. _(Las plantillas traen capítulos predefinidos que pueden chocar con tu estructura.)_
4. **Marcá "iniciar proceso de auditoría"** _(recomendado)_: crea puntos de restauración automáticos.
5. `Aceptar`.

!!! warning "Cuidado con el archivo de auditoría"
    La auditoría crea un archivo especial **junto** al `.presto`. Si movés la obra a otra computadora, **mové también ese archivo** o perdés los puntos de restauración.

!!! tip "Gotcha de Raizant: nunca crees la obra dentro de OneDrive"
    Trabajá la obra en una **carpeta local** (ej. `C:\Presto\Obras\`). Varias funciones de Presto (Excel2Presto, importar) **solo leen archivos locales, no de OneDrive**. Ya sincronizás la copia final aparte.

---

## Tarea 3 — Armar la estructura: capítulos, subcapítulos y partidas

**Qué es:** levantar el esqueleto del presupuesto (la EDT).

**Cómo piensa Presto:** la ventana `Presupuesto` trabaja **por niveles**. Cada concepto es "como una carpeta" en la que entrás con doble clic.

**Paso a paso** (ventana `Presupuesto`) `[00:40]`:

1. En la columna **`Código`** escribí el identificador; ++tab++ te lleva a **`Resumen`** (el texto, máx. ~128 caracteres); ++enter++ crea la fila siguiente.
2. Creá **primero todos los del mismo nivel** (los capítulos A, B, C…); todavía no bajés de nivel.
3. **Entrar a un concepto**: doble clic en cualquier celda de su fila. **Subir un nivel**: doble clic en cualquier **cabecera de columna**.
4. **Anidar filas bajo un superior**: seleccionalas por el número de fila y pulsá **`Disminuir nivel`**. Quedan dentro del concepto de arriba. Existen también `Aumentar nivel` y `Deshacer`.

---

## Tarea 4 — Copiar y pegar el borrador desde Excel

**Qué es:** traer un itemizado que ya tenés en Excel, sin teclearlo.

!!! note "Método simple vs. método pro"
    Acá usamos copiar/pegar simple. El método automatizado (**Excel2Presto**) se enseña en [Presupuesto intermedio](2-intermedio.md) — es más eficiente, pero conviene entender este primero.

**Paso a paso** `[00:50]`–`[01:00]`:

1. Mirá el orden de columnas de tu Excel (ej.: Código · Unidad · Descripción · Cantidad).
2. En Presto: clic derecho en cualquier cabecera → **`Elegir columnas visibles`**.
3. Con `Subir`/`Bajar`, ordená las columnas de Presto para que **coincidan con el Excel**: `Código` · `Ud` · `Resumen` · `CanPres`.
4. `Aceptar`. Copiá en Excel (++ctrl+c++) y en Presto **menú `Inicio → Pegar`** (++ctrl+v++).
5. Anidá los subcapítulos/partidas con `Disminuir nivel`.
6. Restaurá el orden original de columnas con **`Inicio → Restaurar esquema`**.

!!! warning "Si no aparece la columna `CanPres`"
    Casi siempre es porque la ventana está en **otro esquema** (no `Presupuesto`). Cambialo en el desplegable de arriba a la derecha. _(Esto le pasó a Enrique en vivo.)_

---

## Tarea 5 — Decirle a Presto qué es cada cosa (naturalezas / NATSE)

**Qué es:** marcar si cada concepto es un capítulo, una partida, un material, mano de obra, etc.

**Paso a paso** `[01:10]`:

1. La columna **`NATSE`** muestra un ícono por concepto. Los de nivel raíz salen como **capítulo**; los pegados salen como **partida** (ícono rojo).
2. Para cambiar: clic derecho sobre el ícono → elegí la naturaleza (capítulo/subcapítulo, partida, material, mano de obra, maquinaria, otros). Podés seleccionar toda la columna y cambiar en bloque.
3. **Subcapítulos**: cambialos de "partida" a naturaleza **capítulo**.

!!! danger "Regla de oro: niveles homogéneos"
    Todos los inferiores de un mismo nodo deben ser **del mismo tipo** (todos subcapítulos, o todos partidas). Si mezclás, **Presto no avisa pero rompe los informes**. Ver [Reglas de oro](5-reglas-de-oro.md).

!!! tip "Truco: naturaleza automática por la inicial del código"
    En `Propiedades → Varios` podés predefinir letras (ej. `M`=material, `O`=mano de obra, `E`=maquinaria). Después, cualquier código que empiece con esa letra recibe la naturaleza solo. `[01:30]`

---

## Tarea 6 — Definir las monedas (¡antes de poner precios!)

**Qué es:** configurar con qué monedas trabajás y cuál es la principal.

**Por qué importa tanto:** el relator le dedica ~20 minutos. Si se omite, **los informes no suman bien**. Es el error más reportado a soporte.

**Paso a paso** (`Ver → Propiedades`) `[01:20]`–`[01:30]`:

1. **`Datos`**: poné el `Resumen` (nombre de la obra, sale en los informes) y la dirección.
2. **`Divisas`**: creá la tabla de monedas (máx. **6**). Por moneda: código ISO, sigla (máx. 3 letras), **paridad** y fecha. Elegí una de referencia (= valor 1) y poné las demás por regla de 3.
3. Volvé a **`Datos → variable Divisa`** y fijá la **moneda de consolidación** (la moneda principal de la obra, ej. BOB).

!!! warning "Presto NO se conecta a tipos de cambio"
    La paridad es **manual**: la cargás a mano y le das `Recalcular`. Si queda vieja, nadie te avisa. _(Candidato a automatizar in-house.)_

!!! tip "Cómo dejar el presupuesto 'flotante' en cualquier moneda"
    Dejá la `Divisa` **en blanco** en los capítulos/subcapítulos/partidas (el esqueleto) y poné la divisa **solo en los recursos** que están en otra moneda. Así, cambiando la moneda de consolidación, Presto reproyecta TODO sin tocar lo que tecleaste.

---

## Tarea 7 — Armar tu primer APU (a mano)

**Qué es:** descomponer una partida en sus materiales, mano de obra y maquinaria, con cantidades y precios.

**Paso a paso** `[01:40]`–`[02:00]`:

1. En `Presupuesto`, entrá (doble clic) a la partida (ej. _Hormigón de vigas y pilares_).
2. Escribí los recursos: `Código` + `Resumen`. Si configuraste la naturaleza automática, Presto pinta material/MO/maquinaria solo.
3. Llená:
    - **`CanPres`** = cantidad por unidad de partida (Presto la multiplica por la cantidad de la partida).
    - **`Ud`** = unidad.
    - **`Pres`** = precio unitario.
4. **`ImpPres` = `CanPres` × `Pres`** se calcula solo. El precio de la partida = suma de los importes de su APU, y aparece en **magenta** porque es calculado.

---

## Tarea 8 — Reusar APU de otra obra (arrastre desde una "base")

**Qué es:** traer partidas/APU ya armados de otra obra de referencia, sin teclearlos.

**Paso a paso** `[02:20]`–`[02:50]`:

1. `Archivo → Abrir` la obra base **marcando "abrir como solo lectura"** (para no pisarla por accidente).
2. Dejá las dos ventanas de Presto visibles, ambas en la pestaña `Presupuesto`.
3. En la base, seleccioná lo que querés (por el vértice = todo, o por número de fila con ++ctrl++ para selección discontinua).
4. **Arrastrá** (clic izquierdo sostenido) de la base a tu obra. Podés arrastrar solo recursos o partidas completas.

!!! note "Por qué importa para Raizant"
    Mantener una **base de precios maestra** (APU y precios validados) de la que arrastrar es la semilla práctica de la "única fuente de verdad" de costos. El primer presupuesto se vuelve la base de los siguientes.

---

## Tarea 9 — Mediciones: respaldar la cantidad de una partida

**Qué es:** desglosar la cantidad de una partida en parciales (por ejes, losas, sectores).

**Paso a paso** `[03:20]`:

1. Marcá la partida; abrí la subventana **`Mediciones`**.
2. En `Comentario`, describí cada parcial ("excavación ejes", "excavación losas"); ++enter++ crea la línea.
3. En `Cantidad`, escribí los parciales (ej. 100 + 200 + 452 = 752).
4. `Recalcular` → la cantidad de la partida aparece arriba en **magenta** = respaldada por mediciones.

---

## Tarea 10 — Sacar un informe

**Qué es:** generar el entregable (presupuesto, APU, listado de recursos) para imprimir o presentar.

**Paso a paso** `[03:20]`–`[03:30]`:

1. Menú `Informes` → elegí un informe. Hay grupos por país: **14 = Bolivia** (ej. `Presupuesto por ítem`).
2. Respondé la ventana de preguntas del informe (hay botón `Defecto`).
3. **`Vista preliminar`** (se cierra con la tecla ++s++, no tiene "X"), **`Imprimir`** o **`Exportar`**.

!!! note "Los parámetros del informe"
    El `% beneficio`, `% gastos generales`, `IVA` y la fecha (`FEC presupuesto`) se aplican **a nivel de informe** (en `Propiedades → Cálculo`), no en el árbol.

---

## Tarea 11 — Auditoría y puntos de restauración

**Qué es:** ver el historial de cambios o volver a un estado anterior (si creaste la obra con auditoría).

**Paso a paso** `[03:40]`:

1. Menú `Inicio → Auditoría`: lista los puntos de restauración (lo más reciente arriba) con fecha, hora, usuario de Windows y total del presupuesto.
2. Para restaurar: marcá la fila → `Restaurar`. **No pisa tu archivo**: crea una **copia** con la fecha en el nombre.

!!! warning "Limpiá las copias de restauración"
    Presto no borra esas copias. Si no la vas a usar, **borrala a mano** para no confundirte y abrir una versión vieja por error.

---

## 🎥 Mirá el video

| Tema | Minuto |
|---|---|
| Interfaz, licencia, entorno | `[00:00]` |
| Crear / abrir obra | `[00:10]`–`[00:20]` |
| Armar la estructura | `[00:30]`–`[01:10]` |
| Copiar/pegar de Excel | `[00:40]`–`[01:00]` |
| Naturalezas | `[01:10]` |
| Propiedades (divisas, redondeos) | `[01:20]`–`[01:40]` |
| APU a mano + Divisa | `[01:40]`–`[02:10]` |
| Arrastre desde base | `[02:20]`–`[02:50]` |
| Mediciones, informes | `[03:20]`–`[03:30]` |
| Auditoría | `[03:40]` |

> Video fuente: `CL-1 - Ppto Básico - Jueves 27_11_2025.mp4` (3h 47min). Relator de soporte de Presto Chile.

---

## ⚠️ Lo que Presto NO te avisa (resumen)

- **Naturaleza mal puesta o niveles mezclados** → informes rotos, en silencio.
- **Te olvidaste la divisa de un recurso** → importes inflados/desinflados, en silencio.
- **Botón `Automático` desactivado** → las columnas de totales se ven en cero (parece que "Presto está mal").
- **Estás en otro esquema de columnas** → te faltan columnas y creés que no existen.

👉 Todas, con su blindaje, en [5 · Reglas de oro y fallas silenciosas](5-reglas-de-oro.md).

---

## ✏️ Ejercicio en BLEND

!!! example "Practicá lo aprendido"
    Sobre la obra de prueba **BLEND**:

    1. Creá un capítulo nuevo "99 · PRUEBA [tu nombre]" con 2 partidas.
    2. Armá el APU de una de ellas con al menos 1 material + 1 mano de obra.
    3. Agregá una línea de medición a la otra partida y verificá que la cantidad quede en **magenta**.
    4. Sacá el informe `Presupuesto por ítem` (grupo Bolivia) y revisá que tu capítulo aparezca.

    **Cómo sabés que salió bien:** el precio de tu partida con APU aparece en magenta, y la cantidad con medición también. Si algo sale en negro donde esperabas magenta, revisá la descomposición.

---

📖 **Fuente oficial:** Presto-Presupuestos.pdf · Manual-de-Presto-completo.pdf (RIB). · Apunte: C02 — Presupuesto básico (casos de uso 1–19).
