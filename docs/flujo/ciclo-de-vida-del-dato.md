# El ciclo de vida del dato (dónde puede pudrirse)

!!! abstract "La idea en una frase"
    Un dato tiene **vida**: nace, entra al sistema, se valida, se usa y se audita. En **cada una de esas 5 etapas** hay un punto donde puede pudrirse — y para cada punto hay un **guardián** que lo cuida. Conocer dónde se pudre es la mitad de evitarlo.

## Las 5 etapas de la vida de un dato

```
   1. NACE          2. ENTRA          3. SE VALIDA       4. SE USA          5. SE AUDITA
  ┌────────┐       ┌────────┐        ┌────────┐         ┌────────┐         ┌────────┐
  │en su   │  ──▶  │a Presto│  ──▶   │calidad │   ──▶   │EVM,    │   ──▶   │diff de │
  │sistema │       │captura │        │mínima +│         │puente, │         │deriva +│
  │dueño   │       │en origen        │reglas  │         │torre lo│         │concilia│
  │una vez │       │        │        │de oro  │         │ leen   │         │ -ción  │
  └────────┘       └────────┘        └────────┘         └────────┘         └────────┘
       │                │                 │                  │                  │
   ⚠️ nace en       ⚠️ entra tarde    ⚠️ Presto no       ⚠️ editan la       🔔 alarma:
      2 lados          o precio 0        avisa              baseline           corregir en 24h
                                                                                  │
                                                                                  └──▶ vuelve al origen
```

Fijate que la auditoría (etapa 5) **no castiga**: cuando algo no cuadra, manda a **corregir en el origen** (etapa 1). El objetivo es arreglar el sistema, no a la persona.

## Qué hace sano a un dato, y quién lo cuida

Un dato sano tiene **cuatro propiedades**. Para cada una hay un enemigo concreto (lo que pasa hoy) y un guardián (lo que lo evita):

| Propiedad del dato sano | Enemigo (lo que pasa hoy) | Guardián |
|---|---|---|
| **Adecuado** — bien formado, sin duplicados | Códigos duplicados, naturalezas mezcladas, cuenta contable vacía | Dueño del dato + validación antes de congelar |
| **Confiable** — refleja la realidad | Precio cero, certificar lo no ejecutado, factura sin respaldo | Reglas de oro + triple coincidencia + verificación independiente |
| **Al día** — fresco, no de hace semanas | Comprobantes que entran 7 días tarde; estados de resultado con un mes de atraso | Plazo máximo de frescura + captura en el momento |
| **Sin retrasos** — entra cuando pasa | Todo cargado en lote al cierre → el cierre tarda semanas | Cadencia obligatoria + bloqueo de cierre si falta |

## La idea de fondo: captura en origen

La forma más fácil de que un dato sea confiable y esté al día es **capturarlo en el momento y lugar donde sucede**, no acumularlo para cargarlo después.

!!! example "El consumo de material"
    Si el material que se usó hoy en obra se **carga hoy, con su precio**, el costo real de la obra está siempre actualizado. Si se acumulan los comprobantes para cargarlos “a fin de mes”, durante todo el mes el sistema muestra una obra **más barata de lo que es** — y se toman decisiones sobre un número que miente. Por eso la primera regla de oro existe.

!!! tip "El color es una herramienta, no un adorno"
    Cuando la confiabilidad de un dato está en rojo, sus indicadores se degradan a **gris** — un “no sé” honesto. Es preferible un gris honesto que un verde que miente, porque sobre el verde alguien decide plata.

---

!!! note "De dónde sale esto"
    Esta página destila el **ciclo de vida del dato** del documento interno de gobierno de Raizant. Las alarmas concretas de cada etapa (y de quién es cada guardián) se aterrizan a cada puesto en la página **“Tu lugar en el flujo”** de cada rol.
