Característica: Agregar un capítulo
    Como administrador de la secretaría de prevención del delito
    requiero registrar un capítulo nuevo
    para poder asignarle partidas.

    Escenario: Datos correctos
        Dado que estoy dentro del sistema como administrador
        Y entro a la sección de Agregar Capítulo
        Y capturo los datos: Clave "2000", Nombre "MATERIALES Y SUMINISTROS"
        Cuando presiono el botón Guardar
        Entonces puedo ver el capítulo "2000 - MATERIALES Y SUMINISTROS" agregado en la lista de capítulos.

