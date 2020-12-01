Característica: Modificar un capítulo
    Como administrador de la secretaría de prevención del delito
    requiero modificar un capítulo
    para poder asignarle un nuevo nombre.

    Escenario: Datos correctos
        Dado que estoy dentro del sistema como administrador
        Y entro a la sección de Capítulos
        Y selecciono el capítulo "2000 - MATERIALES Y SUMINISTROS"
        Y remplazo el Nombre por "MATERIALES Y SUMINISTROS 2"
        Cuando presiono el botón Guardar
        Entonces puedo ver el capítulo "2000 - MATERIALES Y SUMINISTROS 2" modificado en la lista de capítulos.