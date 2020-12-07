Característica: Modificar un gasto
    Como administrador de la secretaría de prevención del delito
    requiero modificar un gasto
    para poder asignarle un nuevo precio unitario y otro cantidad.

    Escenario: Datos correctos
        Dado que estoy dentro del sistema como administrador
        Y entro a la sección de Modificar Gasto
        Y selecciono el gasto "6"
        Y remplazo el Precio Unitario por "2.50"
        Y la cantidad por "500"
        Cuando presiono el botón Guardar del gasto
        Entonces puedo ver el gasto "1250" modificada en la lista de gastos.