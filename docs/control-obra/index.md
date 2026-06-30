# Rol Control de obra

!!! info "¿Este rol es para vos?"
    Sos **control de obra** si tu trabajo es **medir cómo va la obra y avisar a tiempo**: registrar el avance que se le certifica al cliente (para cobrar), seguir si la obra va sobrecostada o atrasada, gestionar los adicionales, y emitir los estados de pago. Sos la **torre de control**: el que mira los números en tiempo real y enciende la alarma antes de que un desvío se vuelva un problema.

!!! warning "Requisito de licencia"
    Este rol usa **dos módulos** de Presto: **Gestión de Proyectos** (certificación, fases, estados de pago) y **Facturación y Control** (costo real y EVM / valor ganado). Si en la pestaña `Ver` no aparecen las ventanas `Fechas` y los esquemas de certificación/EVM, la licencia todavía no los trae. Confirmá que ambos módulos estén incluidos antes de arrancar. _(Detalle en [La pantalla de Control de obra](interfaz.md).)_

## Tu recorrido de aprendizaje

Está ordenado de armar el calendario de la obra hasta leer su salud completa. Hay **dos cosas distintas** que este rol mide y conviene no confundirlas nunca: la **certificación** (avance para cobrar) y el **EVM** (salud real de costo y plazo).

!!! tip "¿Te perdés entre tantos menús y botones? Empezá por acá"
    Antes que nada, mirá **[🗺 La pantalla de Control de obra: dónde está cada cosa](interfaz.md)**. Es el mapa de las pestañas `Fechas` y `Árbol` con cada esquema y columna explicada — para que cuando una tarea diga "andá a tal esquema", sepas dónde está.

<div class="grid cards" markdown>

-   **0 · Fundamentos del control de obra**

    ---

    El modelo mental: los **tres avances que se confunden** (certificable ≠ físico ≠ costo real), qué entra por este rol y qué no, y las tres magnitudes del valor ganado (**PV / EV / AC**).

    [:octicons-arrow-right-24: Empezar aquí](0-fundamentos.md)

-   **1 · Armar la línea temporal**

    ---

    El primer paso de toda obra: fijar la fecha de inicio y **crear las fechas de certificación** (las fases). Sin esto, no se puede certificar nada.

    [:octicons-arrow-right-24: Ver](1-linea-temporal.md)

-   **2 · Certificar el avance**

    ---

    El día a día: ingresar la cantidad certificada por fase, **marcar la certificación actual** (lo que todos olvidan), cerrar saldos y leer los acumulados.

    [:octicons-arrow-right-24: Ver](2-certificar-avance.md)

-   **3 · Adicionales y estados de pago**

    ---

    Cómo entra un cambio de obra **sin romper el presupuesto base** (por líneas de medición), la diferencia entre aprobado y pendiente, y cómo emitir el documento de cobro.

    [:octicons-arrow-right-24: Ver](3-adicionales-y-estados-de-pago.md)

-   **4 · El EVM: leer la salud de la obra**

    ---

    El corazón del rol: leer **CPI** (¿gasto bien?), **SPI** (¿voy a tiempo?), **EAC** (¿en cuánto termina?) y **% Avance** en una sola pantalla. Presto los calcula solo.

    [:octicons-arrow-right-24: Ver](4-evm-salud-de-obra.md)

-   **5 · Reglas de oro y fallas silenciosas**

    ---

    Lo que Presto **no** te avisa: olvidar marcar la certificación actual, meter un adicional mal, fechas grises, un EVM verde sobre datos rotos. Léelo antes de reportar a dirección.

    [:octicons-arrow-right-24: Ver](5-reglas-de-oro.md)

-   **6 · Preguntas frecuentes y glosario**

    ---

    Las dudas que aparecen siempre + el diccionario de columnas (CanCert, ImpCert, EvmCpi, OrReal, FaseCert…).

    [:octicons-arrow-right-24: Ver](6-faq-glosario.md)

-   **7 · Ejercicios en BLEND**

    ---

    Practicá cada paso sobre la obra de prueba, en un entorno seguro _(cuando la licencia tenga los módulos)_.

    [:octicons-arrow-right-24: Ver](7-ejercicios-blend.md)

</div>

## En una frase, qué vas a aprender

A pasar de **una obra en marcha** a un **tablero de salud confiable**: a certificar el avance para cobrar, a registrar los cambios sin romper el presupuesto, y a leer en tiempo real si la obra va bien o mal — y, sobre todo, a saber **cuándo un número miente** porque el dato base está incompleto. Porque la torre de control de Raizant **lee** los indicadores que Presto calcula; lo que ponemos nosotros es la **confiabilidad** del dato y la **alarma temprana**.

---

!!! note "Fuente de este rol"
    Construido sobre la **documentación oficial de Presto (RIB)** — _Certificación y seguimiento_, _Órdenes de cambio_, _El valor ganado explicado en 4 páginas_, _Valor ganado: el proyecto A-12_, _Cómo se calculan los costes reales_ y el _Manual de Presto completo_ — complementada con los apuntes internos C08 (certificación) y C09 (EVM) y las transcripciones de los videos de capacitación. Cada página cita su fuente oficial.
