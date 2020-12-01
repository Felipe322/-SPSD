Característica: Modificar un gasto
    Como administrador de la secretaría de prevención del delito
    requiero modificar un gasto
    para poder asignarle un nuevo precio unitario y otro cantidad.

    Escenario: Datos correctos
        Dado que estoy dentro del sistema como administrador
        Y entro a la sección de Modificar Gasto
        Y selecciono el gasto "Se compraron muchos lapízes 750.0"
        Y remplazo el Precio Unitario por "2.7"
        Y la cantidad por "325"
        Cuando presiono el botón Guardar del gasto
        Entonces puedo ver el gasto "Se compraron muchos lapízes 877.5" modificada en la lista de gastos.