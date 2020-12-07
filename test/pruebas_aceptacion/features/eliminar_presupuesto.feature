Característica: Eliminar un presupuesto
    Como administrador de la secretaría de prevención del delito
    requiero eliminar un presupuesto
    para poder dejar de darle seguimiento.

    Escenario: Datos correctos
        Dado que estoy dentro del sistema como administrador
        Y entro a la sección de Modificar Presupuesto
        Cuando presiono el botón Eliminar del presupuesto "2020"
        Entonces puedo ver que el presupuesto "2020" ya no está en la lista de presupuestos.