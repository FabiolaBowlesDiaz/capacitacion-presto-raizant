# 8 · Ejercicios en BLEND

!!! abstract "Para qué es esta página"
    Un recorrido práctico de punta a punta para **fijar el rol** sobre un modelo de prueba. Hacelos en orden: cada uno usa lo del anterior. Al final vas a haber recorrido el ciclo completo — del modelo al presupuesto y de vuelta cuando el diseño cambia.

!!! warning "Requisito de licencia"
    Estos ejercicios **necesitan una licencia con el módulo Cost-It** y el complemento instalado en Revit. Si tu Revit no muestra la pestaña `Cost-It`, el módulo no está activo — podés estudiar el manual, pero recién operás cuando la licencia lo incluya (Cloud). _(Ver [La pantalla de Arquitectura](interfaz.md).)_

!!! tip "Cómo aprovecharlos"
    Para cada ejercicio anotá **qué esperabas** y **qué salió**. Cuando no coincidan, volvé a la página indicada — ahí está el porqué. La idea no es "que salga", sino **entender por qué salió así**.

---

## Ejercicio 1 — Tu primer traspaso

📄 _Repasa: [1 · Traer el modelo a Presto](1-traspaso-inicial.md)_

1. Abrí el modelo en Revit con una **vista 3D** activa y hacé clic afuera para no dejar nada seleccionado.
2. `Cost-It ▸ Exportar` → en `Estadísticas`, anotá **cuál es la categoría más numerosa**.
3. En `Opciones`: `líneas de medición` marcado, tipo de medición en `tipos`, codificación = `código de montaje`.
4. Pulsá `elementos con código` y anotá: **¿cuántos elementos tienen código? ¿cuántos duplicados hay?**
5. En `Categorías`, dejá solo **Muros** y `Exportar`.

!!! success "Lo lograste si…"
    En Presto aparece un capítulo "Muros" con sus partidas, y abajo las líneas de medición con sus cantidades. Sabés cuántas partidas salieron 🔴 / ⬜ / 🟢.

---

## Ejercicio 2 — Leer las cantidades

📄 _Repasa: [2 · Leer y verificar](2-leer-y-verificar.md)_

1. Entrá a una partida de muros y contá cuántas cantidades están **🟣 magenta** y cuántas **⚫ negras**.
2. Elegí una **magenta**: clic derecho ▸ `seleccionar en el modelo` y confirmá que se marcó el muro correcto en Revit.
3. Elegí una **negra** (si hay): hacé visible `BIM Sup` y compará la cantidad declarada con el valor BIM exacto. ¿Por qué difería más del 2%?

!!! success "Lo lograste si…"
    Podés explicar, partida por partida, **por qué** cada cantidad es magenta o negra, y saltar al modelo a verificar cualquiera.

---

## Ejercicio 3 — Separar una partida verde

📄 _Repasa: [3 · Afinar y desglosar](3-afinar-y-desglosar.md)_

1. Identificá una partida **🟢 verde**. Renombrá su `Resumen` a algo genérico.
2. `Herramientas ▸ Desglosar` por `Familia Tipo BIM`. Comprobá que se separó en partidas de un solo tipo y limpiá el estado a negro.
3. Volvé a Revit, escribí un **discriminador** (`tipo`) en una categoría, re-exportá y comprobá que ahora sale **ya separada**.
4. Guardá la configuración como `Raizant-base.CostItLayout`.

!!! success "Lo lograste si…"
    Conseguiste el mismo desglose de **dos maneras** (a mano en Presto y automático con el discriminador) y tenés tu plantilla guardada.

---

## Ejercicio 4 — Codificar y volcar al estudio

📄 _Repasa: [4 · Codificar el modelo y volcar](4-codificar-y-volcar.md)_

_(Con un estudio de prueba que ya tenga partidas con APUs.)_

1. Desde el estudio: `Archivo ▸ Exportar ▸ Catálogo Revit` desde la raíz. Abrí el archivo y confirmá que están los códigos de tus partidas.
2. _(Si podés)_ cargá el catálogo en Revit y asigná el código de montaje a un par de tipos.
3. Exportá el modelo codificado **sin** "elementos sin código".
4. En el estudio: `Ver ▸ Mediciones temporales ▸ Importar` → `Asignar por código inferior`. Contá **🟢 verdes** (match) y **grises** (sin match).
5. Revisá una gris: ¿sobrante real o código mal puesto? Después `Traspasar`.

!!! success "Lo lograste si…"
    El estudio quedó con sus APUs **y** las cantidades del modelo, y podés saltar de cualquier partida al elemento en Revit.

---

## Ejercicio 5 — Re-sincronizar un cambio de diseño

📄 _Repasa: [5 · Re-sincronizar](5-resincronizar.md)_

1. En Revit, **borrá 2 ventanas** y, si podés, **ensanchá un muro**.
2. Con el estudio **abierto** en Presto, `Cost-It ▸ Exportar…` → pulsá **`Añadir`** (¡no `Exportar`!).
3. `Asignar por código inferior` → `Comprobar` → `Buscar líneas desaparecidas`.
4. Antes de traspasar, identificá las filas **verdes (Inserción)** y las de acción `borrar`. ¿Coinciden con tu cambio (2 ventanas `borrar`)?
5. `Traspasar` y verificá que el conteo de ventanas bajó y que el muro cambió de cantidad.

!!! success "Lo lograste si…"
    El presupuesto refleja **exactamente** tu cambio de modelo, sin obras paralelas y sin cantidades fantasma de lo que borraste.

---

## Desafío integrador — "del plano al presupuesto vivo"

!!! example "Si querés ponerte a prueba de verdad"
    Hacé el ciclo completo **sin mirar las páginas**:

    1. Codificá un modelo chico con los códigos de un estudio.
    2. Volcá las cantidades al estudio (match por código inferior).
    3. Cambiá el modelo (agregá y borrá elementos).
    4. Re-sincronizá con `Añadir`, revisá los cambios y traspasá.
    5. Listá: ¿quedó alguna línea gris (sin match)? ¿alguna partida verde sin desglosar? ¿alguna cantidad negra sin revisar?

    **El objetivo:** que al terminar puedas decir, con confianza, "este presupuesto refleja el modelo de hoy, y sé exactamente qué quedó pendiente de revisar". Eso es ser el **primer eslabón de confianza** de la torre de control.

---

## Para seguir

- ¿Dudas sueltas? → [7 · Preguntas frecuentes y glosario](7-faq-glosario.md)
- ¿Querés blindarte de los errores típicos? → [6 · Reglas de oro y fallas silenciosas](6-reglas-de-oro.md)
- ¿Te perdiste con algún botón? → [🗺 La pantalla de Arquitectura](interfaz.md)

---

📖 **Fuentes:** _Manual de Cost-it_ (RIB) · apunte interno C01 · transcripción `CSE - Cost It - 23/01/2026`.
