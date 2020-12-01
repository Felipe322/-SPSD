Característica: Modificar una actividad
    Como administrador de la secretaría de prevención del delito
    requiero modificar una actividad
    para poder asignarle un nuevo programa y otro actividad.

    Escenario: Datos correctos
        Dado que estoy dentro del sistema como administrador
        Y entro a la sección de Modificar Actividad
        Y selecciono la actividad "28 2 4"
        Y remplazo el Programa por "27"
        Y la actividad por "3"
        Cuando presiono el botón Guardar de la actividad
        Entonces puedo ver la actividad "27 2 3" modificada en la lista de actividades.