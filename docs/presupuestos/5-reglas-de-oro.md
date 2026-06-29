# 5 · Reglas de oro y fallas silenciosas

!!! danger "Por qué esta página es la más importante del manual"
    Presto **no es un ERP** y casi nunca te frena ni te avisa cuando hacés algo mal. Los errores no salen como un cartel rojo: salen como **informes que no suman**, **costos que no cuadran** o **valor ganado mentiroso** — semanas después. Esta página lista lo que rompe en silencio y cómo blindarte. **Léela antes de cerrar tu primer presupuesto.**

---

## Las 3 reglas de oro

| # | Regla | Qué pasa si la rompés |
|---|---|---|
| **1** | **Un concepto = un código único = un precio.** El código es la identidad. | Si duplicás o renombrás mal un código, se rompen informes, valor ganado y el puente contable. |
| **2** | **El presupuesto se congela al iniciar la obra (baseline) y no se vuelve a tocar.** | Es la línea base contra la que se mide el desvío. Si la editás después, perdés la referencia para medir CPI/SPI. Presto **no tiene candado** → es disciplina + snapshot in-house. |
| **3** | **Niveles homogéneos.** Los inferiores de un nodo deben ser todos del mismo tipo. | Si mezclás subcapítulos con partidas bajo el mismo padre, los informes salen mal. |

---

## Las 10 fallas silenciosas (FS) y cómo blindarte

!!! warning "FS-1 — Naturaleza mal asignada o niveles mezclados"
    **Síntoma:** un subcapítulo quedó como "partida", o un nodo mezcla subcapítulos con partidas. Presto no avisa, pero los informes salen mal. `[01:10]`
    **Blindaje:** checklist de QA de estructura — verificar que cada nodo del árbol sea homogéneo antes de congelar la baseline.

!!! warning "FS-2 — Divisa omitida o moneda de consolidación sin definir"
    **Síntoma:** los informes "no suman bien". Es **el error más reportado a soporte**. Un recurso en USD sin marcar su `Divisa` se lee como moneda local → importes mal, en silencio. `[01:20]`
    **Blindaje:** estándar obligatorio de definir divisas y moneda de consolidación al crear la obra.

!!! warning "FS-3 — Botón `Automático` desactivado"
    **Síntoma:** las columnas de totales (`CanTotPres`, `TotPres`) se ven en cero o vacías, y parece que "Presto está mal". Pasa cuando alguien lo desactiva para ganar velocidad. `[03:00]`
    **Blindaje:** "verificar `Automático` activo antes de leer totales". Relevante para Raizant por trabajar sobre OneDrive.

!!! warning "FS-4 — Esquema de columnas equivocado"
    **Síntoma:** faltan columnas clave (ej. `CanPres`) y creés que no existen. Le pasó a Enrique en vivo. `[00:50]`
    **Blindaje:** estandarizar y guardar el esquema `Presupuesto` para todo el equipo.

!!! warning "FS-5 — Paridad de divisa desactualizada"
    **Síntoma:** como Presto no se conecta a tipos de cambio, la paridad queda vieja por meses sin alerta, distorsionando los recursos importados. `[01:30]`
    **Blindaje:** rutina in-house que actualice la paridad y dispare `Recalcular`, o que alerte cuando la fecha supere N días.

!!! warning "FS-6 — Cantidades que se redondean a cero"
    **Síntoma:** un recurso con cantidad 0,0004 y solo 3 decimales se redondea a cero y desaparece del cálculo, sin error. `[01:40]`
    **Blindaje:** definir suficientes decimales en la plantilla de obra; validar recursos cuya cantidad redondeada sea 0.

!!! warning "FS-7 — La auditoría NO es congelado de baseline ni aprobación"
    **Síntoma:** se cree que la auditoría "protege" el presupuesto. Registra cambios y permite revertir, pero **no bloquea la edición** ni implementa el filtro de aprobación. Solo guarda el usuario de Windows. `[03:40]`
    **Blindaje:** workflow de aprobación + congelado formal de la baseline (snapshot bloqueado por el tejido in-house).

!!! warning "FS-8 — Copias de restauración que confunden"
    **Síntoma:** la restauración deja un `.presto` con nombre parecido al original; alguien abre por error una versión vieja. `[03:40]`
    **Blindaje:** convención de nombres/carpeta para restauraciones y limpieza periódica.

!!! warning "FS-9 — La búsqueda (Ctrl+B) 'no encuentra nada'"
    **Síntoma:** buscás un texto pero el cursor está en la columna `Código` → no encuentra. La búsqueda mira **la columna donde está el cursor**. `[02:40]`
    **Blindaje:** es educación, no bug — parate en la columna correcta antes de buscar.

!!! warning "FS-10 — La carga manual es punto de error humano"
    **Síntoma:** teclear, copiar/pegar y arrastrar siempre puede meter errores. El flujo automático Revit→Cost-It→Presto los evita. `[01:00]`
    **Blindaje:** priorizar Cost-It (mediciones automáticas) y Excel2Presto sobre el tecleo; mantener una base de precios maestra.

---

## Checklist antes de congelar la baseline

- [ ] Cada nodo del árbol es homogéneo (todos subcapítulos o todas partidas)
- [ ] Todas las divisas y la moneda de consolidación están definidas
- [ ] Ningún recurso en otra moneda quedó sin su `Divisa`
- [ ] El botón `Automático` está activo y los totales calculan
- [ ] No hay códigos duplicados
- [ ] Ninguna cantidad importante se redondeó a cero
- [ ] Se guardó el snapshot congelado de la baseline (proceso in-house)

---

📖 **Fuente:** apunte C02 (§3 Reglas de cálculo, §4 Fallas silenciosas) · Base de conocimiento Presto.
