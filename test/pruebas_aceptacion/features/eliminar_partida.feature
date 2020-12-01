Característica: Eliminar una partida
    Como administrador de la secretaría de prevención del delito
    requiero eliminar una partida
    para poder dejar de darle seguimiento.

    Escenario: Datos correctos
        Dado que estoy dentro del sistema como administrador
        Y entro a la sección de Modificar Partida
        Y selecciono la partida "2114 - MATERIALES"
        Cuando presiono el botón Eliminar de la partida
        Y confirmo la acción con el botón de Si, estoy seguro
        Entonces puedo ver que la partida "2114 - MATERIALES" ya no está en la lista de partidas.