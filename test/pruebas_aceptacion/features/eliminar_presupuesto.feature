Característica: Eliminar un presupuesto
    Como administrador de la secretaría de prevención del delito
    requiero eliminar un presupuesto
    para poder dejar de darle seguimiento.

    Escenario: Datos correctos
        Dado que estoy dentro del sistema como administrador
        Y entro a la sección de Modificar Presupuesto
        Y selecciono el presupuesto "2021 2020-12-10"
        Cuando presiono el botón Eliminar del presupuesto
        Y confirmo la acción con el botón de Si, estoy seguro
        Entonces puedo ver que el presupuesto "2021 2020-12-10" ya no está en la lista de presupuestos.