Característica: Agregar una actividad
    Como administrador de la secretaría de prevención del delito
    requiero registrar una actividad nuevo
    para poder asignarle gastos.

    Escenario: Datos correctos
        Dado que estoy dentro del sistema como administrador
        Y entro a la sección de Agregar Actividad
        Y capturo los datos: Programa "20", Componente "5", Actividad "3", Monto "2,982.23", Descripcion "Presupuesto para Febrero", Mes "02", Partida "2110 - MATERIALES, ÚTILES Y EQUIPOS MENORES DE OFICINA", Año "2020"
        Cuando presiono el botón Agregar de la actividad
        Entonces puedo ver la actividad agregada, con la descripción "Presupuesto para Febrero".