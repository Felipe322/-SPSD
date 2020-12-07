Característica: Modificar un presupuesto
    Como administrador de la secretaría de prevención del delito
    requiero modificar un presupuesto
    para poder asignarle un nuevo día.

    Escenario: Datos correctos
        Dado que estoy dentro del sistema como administrador
        Y entro a la sección de Modificar Presupuesto
        Y selecciono el presupuesto "2020"
        Y remplazo la fecha por "13/12/2020"
        Cuando presiono el botón Guardar del presupuesto
        Entonces puedo ver el presupuesto con la fecha "13 de Diciembre de 2020" modificada en la lista de presupuestos.