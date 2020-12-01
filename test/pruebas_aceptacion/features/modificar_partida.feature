Característica: Modificar una partida
    Como administrador de la secretaría de prevención del delito
    requiero modificar una partida
    para poder asignarle un nuevo nombre.

    Escenario: Datos correctos
        Dado que estoy dentro del sistema como administrador
        Y entro a la sección de Modificar Partida
        Y selecciono la partida "2110 - MATERIALES, ÚTILES Y EQUIPOS DE OFICINA"
        Y remplazo el Nombre por "MATERIALES, ÚTILES Y EQUIPOS MENORES DE OFICINA"
        Cuando presiono el botón Guardar de la partida
        Entonces puedo ver la partida "2110 - MATERIALES, ÚTILES Y EQUIPOS MENORES DE OFICINA" modificada en la lista de partidas.