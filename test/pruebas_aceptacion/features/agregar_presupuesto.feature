Característica: Agregar un presupuesto
    Como administrador de la secretaría de prevención del delito
    requiero registrar un presupuesto nuevo
    para poder asignarle actividades.

    Escenario: Datos correctos
        Dado que estoy dentro del sistema como administrador
        Y entro a la sección de Agregar Presupuesto
        Y capturo los datos: Año "2020", Fecha "12/12/2020"
        Cuando presiono el botón Guardar del presupuesto
        Entonces puedo ver el presupuesto "2020 2020-12-12" agregado en la lista de presupuestos.

