Característica: Eliminar un gasto
    Como administrador de la secretaría de prevención del delito
    requiero eliminar un gasto
    para poder dejar de darle seguimiento.

    Escenario: Datos correctos
        Dado que estoy dentro del sistema como administrador
        Y entro a la sección de Modificar Gasto
        Y selecciono el gasto "Se compraron muchos lapízes 750.0"
        Cuando presiono el botón Eliminar del gasto
        Y confirmo la acción con el botón de Si, estoy seguro
        Entonces puedo ver que el gasto "Se compraron muchos lapízes 750.0" ya no está en la lista de gastos.