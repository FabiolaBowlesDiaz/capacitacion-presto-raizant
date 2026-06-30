# Los 2 ciclos: cómo viaja el dato

!!! abstract "La idea en una frase"
    Casi todo lo que pasa en una obra es uno de **dos viajes**: el de **comprar un material** y el de **avanzar la obra**. En cada uno, el dato pasa de mano en mano — y en cada mano hay una regla de oro: **el que hace una cosa no hace la siguiente.** Así ningún paso queda sin un segundo par de ojos.

## Ciclo 1 · Compras — Pide ≠ Compra ≠ Recibe ≠ Paga

La obra necesita un material. Desde que se pide hasta que se paga, el dato pasa por **cuatro manos distintas**. Ninguna persona hace dos eslabones seguidos del control.

```
  OBRA              COMPRAS            PRESUPUESTO        COMPRAS           ALMACÉN            CONTABILIDAD
 ┌──────┐          ┌──────┐          ┌────────┐         ┌──────┐         ┌────────┐         ┌──────┐
 │1.Pide│   ──▶    │2.Coti│   ──▶    │3. GATE │  ──▶    │4.Emite  ──▶    │5.Recibe│   ──▶   │6.Regis│
 │ requi│          │ za 3 │         │ aprueba │        │  la OC │        │+ remito│         │ factura│
 │sición│          │ prov.│         │ (sí/no) │        │        │        │7.Salida│         │8. Paga │
 └──────┘          └──────┘          └────────┘         └──────┘         │a partida        └──────┘
  Andrés/          Daniel/           Enrique            Daniel/          └────────┘         Carolina
  jefas de obra    Hubert                               Hubert           Almacenero
```

| Paso | Quién | Qué hace | Por qué importa el traspaso |
|---|---|---|---|
| 1. Requisición | Obra | Pide el material, deja **número y registro** | Sin requisición la compra “nace por WhatsApp”, sin historia |
| 2. Cotización | Compras | Pide precio a **3 proveedores** | Presto no obliga a cotizar — lo cuida el proceso |
| 3. **Gate** | Presupuesto | Aprueba (o no) la compra | Sin este filtro, compras avanza sin respaldo |
| 4. Orden de compra | Compras | Emite la OC al adjudicado | El dato de la OC alimenta a recepción y a contabilidad |
| 5. Recepción | Almacén | Recibe y registra el **remito** | Quien compra **no** recibe → así nadie se aprueba su propia compra |
| 6-7. Salida a obra | Almacén | Asigna el material a su **partida** | Acá nace el **costo real** de la obra |
| 8. Pago | Contabilidad | Paga **solo** contra factura válida | Quien pide/recibe no paga |

!!! info "El three-way match (la triple coincidencia)"
    El control central de este ciclo es que **tres papeles coincidan**: la **orden de compra** (lo que pedí), el **remito** (lo que recibí) y la **factura** (lo que me cobran). Si los tres cuadran, se paga. Si no cuadran, salta la alarma — porque ahí es donde se cuela un cobro de más o un material que nunca llegó.

## Ciclo 2 · Obra — Ejecuta ≠ Mide ≠ Aprueba

La obra avanza. ¿Cuánto avanzó de verdad? Ese número mueve plata (certificaciones, pagos), así que **no lo decide una sola persona.**

```
  OBRA                    CONTROL DE OBRA       TORRE DE DATOS           PRESUPUESTO
 ┌──────────┐            ┌──────────┐          ┌──────────────┐         ┌──────────┐
 │1. Ejecuta│    ──▶     │3. Verifica  ──▶     │4. Contrasta  │  ──▶    │6. Demuestra
 │ y mide su│            │  en campo│          │  avance vs   │         │  que cumple
 │  avance  │            │          │          │  material vs │         │  su número
 │2. Levanta│            │          │          │  cronograma  │         │          │
 │  certif. │            │          │          │5. ¿Cuadra?   │         │          │
 └──────────┘            └──────────┘          └──────────────┘         └──────────┘
   Andrés                Control (⚠️ a definir)  Torre/Stephany          Enrique
                                                                          │
                                          si NO cuadra ──▶  🔔 ALERTA: se investiga, NO se ajusta
```

| Paso | Quién | Qué hace |
|---|---|---|
| 1-2. Ejecuta, mide y levanta | Superintendente | Está en obra, sabe cuánto avanzó: **mide y propone** la certificación |
| 3. Verifica en campo | Control de obra **(⚠️ a definir)** | Un independiente confirma el avance físico |
| 4-5. Contrasta con el dato | Torre de datos | Cruza el avance contra el **material consumido** y el cronograma |
| 6. Demuestra cumplimiento | Presupuesto | Muestra su cumplimiento **contra** el número, no lo aprueba solo |

!!! warning "La clave anti juez-y-parte"
    El superintendente **sí mide** — es quien está en obra y sabe. Lo que es independiente es la **verificación**: su cifra **no se aprueba sola**, se contrasta contra el material que realmente salió. Si levanta 80% de avance pero solo salió material para el 50%, **el dato lo marca solo**. No es desconfianza: es el principio de los cuatro ojos. Cuando algo no cuadra, **se investiga — no se ajusta el número para que cierre.**

---

!!! note "Responsables por definir"
    El rol de **Control de obra independiente** y **quién aprueba la certificación por encima de presupuesto** están **⚠️ por definir** en la sesión de firmas. El mínimo que ya funciona: la obra levanta y la **Torre de datos valida** con el cruce. El ideal: además, Control de obra verifica en campo.
