# 2 · Presupuesto intermedio

!!! abstract "Conclusión primero"
    Acá pasás de "armar el presupuesto" a "armarlo bien y a escala": importás de Excel con el método pro (**Excel2Presto**), entendés a fondo las **naturalezas**, marcás los **subcontratos**, y preparás el **puente con contabilidad** (Código2).

!!! note "Estado de esta página"
    🚧 En construcción. La estructura y las fuentes ya están definidas; el contenido detallado paso a paso se completa en el issue **DRI-191**. Fuente: apunte **C03 (Presupuesto intermedio, 430 líneas)** + transcripción **CL-2** + manuales RIB.

## Temas de esta sección

- **Excel2Presto** — el método eficiente para llevar un itemizado de Excel a Presto (arma el árbol automáticamente).
    - ⚠️ Pitfall clave: **solo lee archivos locales, no de OneDrive** → copiá el Excel a disco antes de importar.
- **Naturalezas a fondo** — material, mano de obra, maquinaria, % (porcentaje), otros.
- **Subcontratos = partida + propiedad "Suministro"** — clic derecho → Suministro, el ícono se pone **naranja 🟧**. Es lo que diferencia una partida con precio cerrado (sin APU) de una con APU. _(CL-2 minuto `[01:30:00]`)_
- **Conceptos porcentaje (%)** — para modelar IVA por tipo, gastos proporcionales, etc.
- **Agentes / proveedores / entidades** — cómo se cargan los proveedores en la obra.
- **Código2** — el código secundario que sirve de puente al plan de cuentas de Syneco. ⚠️ NO es un mecanismo para recodificar; es solo para informes/contabilidad.
- **Personalización de columnas y esquemas** — guardar tu vista de trabajo.

## ⚠️ Pitfalls de esta sección

- El flag **Suministro NO viaja en un archivo BC3** → si importás/exportás, hay que volver a marcarlo en Presto.
- **Código2 no recodifica**: cambiar el Código2 no cambia la identidad del concepto (esa es el `Código`).

📖 **Fuente:** C03 — Presupuesto intermedio · CL-2 · Personalizacion-de-columnas-y-esquemas.pdf · Uso-de-colores.pdf (RIB).
