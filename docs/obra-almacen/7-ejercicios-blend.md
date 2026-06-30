# 7 · Ejercicios en BLEND

!!! abstract "Conclusión primero"
    Acá practicás todo el rol de punta a punta sobre la obra de prueba **BLEND**, en un entorno seguro donde no rompés nada real. Cada ejercicio corresponde a una tarea del manual. Hacelos en orden: cada uno se apoya en el anterior.

!!! warning "Requisito de licencia"
    Estos ejercicios necesitan una licencia con el módulo **Facturación y Control** activo (y, para el ejercicio del pedido a la factura, también **Contratación**). Si tu licencia todavía no los tiene, leé igual los pasos para tener el modelo mental — cuando tengas la licencia Cloud, los hacés.

!!! tip "Cómo se valida cada ejercicio"
    Cada uno termina con un **"Cómo sabés que salió bien"**: una señal concreta en pantalla. Si no la ves, algo quedó a medias — revisá los pasos antes de seguir.

---

## Ejercicio 1 — Recibir material (la entrega básica)

**Practica:** [1 · Recibir material](1-recepcion-entrega.md)

1. Abrí la ventana `Ver → Entregas` + activá `Suministros`.
2. Creá una entrega nueva: `Documento` = `EN-PRUEBA-01`.
3. Asignale un **proveedor** de la tabla de Entidades y verificá que aparezca su ícono en `NatC`.
4. Corregí la **fecha** al día de hoy.
5. Cargá **2 materiales** por sugerencia; a uno ponele una **cantidad parcial** (la mitad de lo presupuestado).
6. Sobrescribí el `Precio` de uno con un precio "real" inventado.

!!! success "Cómo sabés que salió bien"
    El proveedor tiene su ícono en `NatC`, los 2 materiales aparecen con **ícono naranja 🟧** en `Conceptos`, y el `Importe` de cada línea = cantidad × precio.

---

## Ejercicio 2 — Imputar el consumo a una partida

**Practica:** [2 · Imputar el consumo](2-imputar-consumo.md)

1. Tomá uno de los materiales del Ejercicio 1 (con cantidad, ej. 100).
2. **Desdoblalo**: clic derecho sobre `Cantidad` → `Desdoblar` → sacá `30`.
3. A la línea de `30`, asignale un **`Destino`** (una partida que tenga la propiedad asignada).
4. Ponele una **fecha** dentro del período de trabajo actual.
5. Andá al **`Árbol`** → `Inicio ▸ Recalcular` → buscá esa partida.

!!! success "Cómo sabés que salió bien"
    El `ImpReal` de la partida muestra el costo de esos 30. Las dos líneas del desdoblar (30 y 70) suman los 100 originales.

---

## Ejercicio 3 — La falla silenciosa de la fecha gris

**Practica:** [5 · Reglas de oro, FS-2](5-reglas-de-oro.md)

1. Sobre la imputación del Ejercicio 2, cambiá la **fecha** a un año distinto (fuera del período actual).
2. Recalculá y observá la partida.
3. Corregí la fecha de vuelta al período actual y recalculá otra vez.

!!! success "Cómo sabés que salió bien"
    Con la fecha mala, el costo de la partida **desaparece** y la fecha se ve **gris**. Con la fecha corregida, el costo **vuelve a aparecer**. Ahora entendés por qué nunca hay que dejar fechas grises.

---

## Ejercicio 4 — Material del almacén central (parte de obra)

**Practica:** [3 · Material del almacén central](3-almacen-y-sobrantes.md)

1. Simulá que llega material del almacén central: cargá un **Parte de obra** con un material, imputándolo **directo** a una partida (`Destino` + fecha + precio), **sin** orden de compra.
2. Recalculá y verificá el costo.
3. Simulá una **devolución**: hacé una imputación de **cantidad negativa** del mismo material sobre la misma partida.
4. Recalculá de nuevo.

!!! success "Cómo sabés que salió bien"
    El costo de la partida **sube** con el parte de obra y **baja** con la cantidad negativa — todo sin tocar ninguna orden de compra.

---

## Ejercicio 5 — Del pedido a la factura

**Practica:** [4 · Del pedido a la factura](4-del-pedido-a-la-factura.md)

1. Tomá un pedido (OC) existente en BLEND. Sobre **un suministro suelto**, hacé `Pasar a entrega`.
2. Verificá que la entrega parcial heredó el **precio de la OC**.
3. Sobre esa entrega, hacé `Pasar a factura`, poné un folio inventado, corregí el IVA y la fecha.
4. Andá a `Ver → Suministros`, filtrá la columna `factura` por **vacío**.
5. En `Entidades → [Proveedores] Importes`, mirá el "pendiente" de un proveedor.

!!! success "Cómo sabés que salió bien"
    La entrega parcial muestra el precio de la OC, la factura aparece con su folio en cada línea, y el filtro de "sin factura" te muestra las entregas huérfanas.

---

## Ejercicio integrador — un material de punta a punta

!!! example "El ciclo completo en un solo recorrido"
    Hacé que **un material** recorra todo el ciclo y mirá las cuatro "bases" en cada paso:

    1. (Compras) Tené un pedido con ese material → mirá `BasePed` en la cabecera.
    2. `Pasar a entrega` → mirá que aparece `BaseEnt`.
    3. Imputá el consumo a una partida (`Destino` + fecha) → mirá `BaseDest` y el `ImpReal` en el árbol.
    4. `Pasar a factura` → mirá `BaseFac`.

    **Cómo sabés que salió bien:** las cuatro bases (`BasePed`, `BaseEnt`, `BaseDest`, `BaseFac`) terminan coincidiendo → el ciclo de ese material cerró completo, y su costo real está en la partida correcta.

---

## Después de practicar

Cuando hayas hecho todos los ejercicios, tenés el rol completo:

- Sabés **recibir** material (entrega) y cargar cantidad y precio reales.
- Sabés **imputar** el consumo a la partida — el corazón del costo real.
- Sabés manejar el **material del almacén** y las **devoluciones**.
- Sabés **encadenar** OC → entrega → factura y leer cuánto falta.
- Conocés las **8 fallas silenciosas** y cómo blindarte.

!!! note "Lo que sigue"
    Cuando esté la licencia Cloud con el módulo activo, vamos a sumar las **capturas reales** de cada pantalla (suministro desdoblado con Destino, el `ImpReal` en el árbol, la tabla de entregas sin factura) para que reconozcas exactamente tu pantalla. Mientras tanto, este recorrido te deja listo para operar.

---

📖 **Fuentes:** _Manual de Presto completo_ y _Tutorial de Presto_ (RIB) · apuntes internos C06/C07 · transcripciones `FactCon_08_08_2025` y `Contratacion_30_12_2025`.
