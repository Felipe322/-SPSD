Característica: Agregar una actividad
    Como administrador de la secretaría de prevención del delito
    requiero registrar una actividad nuevo
    para poder asignarle gastos.

    Escenario: Datos correctos
        Dado que estoy dentro del sistema como administrador
        Y entro a la sección de Agregar Actividad
        Y capturo los datos: Programa "27", Componente "2", Actividad "3", Monto "2,982.23", Descripcion "Presupuesto para Febrero", Mes "02", Partida "2111 - MATERIALES Y ÚTILES DE OFICINA", Año "2020 2020-12-13"
        Cuando presiono el botón Guardar de la actividad
        Entonces puedo ver la actividad "2000 - MATERIALES Y SUMINISTROS" agregado en la lista de actividades.