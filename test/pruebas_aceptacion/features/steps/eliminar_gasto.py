from selenium.common.exceptions import NoSuchElementException
from behave import given, when, then
import time


@when(u'presiono el botón Eliminar del gasto "{gasto}"')
def step_impl(context, gasto):
    context.driver.find_element_by_xpath("//a[@href='/gastos/eliminar/"+gasto+"']").click()
    time.sleep(0.5)

@then(u'puedo ver que el gasto "{gasto}" ya no está en la lista de gastos.')
def step_impl(context, gasto):
    bandera = True
    try:
        context.driver.find_element_by_xpath('//*[text() = "'+gasto+'"]')
    except NoSuchElementException:
        bandera = False
    context.test.assertFalse(bandera)
