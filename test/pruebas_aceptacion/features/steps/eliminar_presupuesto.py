from selenium.common.exceptions import NoSuchElementException
from behave import given, when, then
import time


@when(u'presiono el botón Eliminar del presupuesto "{presupuesto}"')
def step_impl(context, presupuesto):
    context.driver.find_element_by_xpath(
        "//a[@href='/presupuestos/eliminar/"+presupuesto+"']").click()
    time.sleep(0.5)


@then(u'puedo ver que el presupuesto "{presupuesto}" ya no está en la lista de presupuestos.')
def step_impl(context, presupuesto):
    bandera = True
    try:
        context.driver.find_element_by_xpath('//*[text() = "'+presupuesto+'"]')
    except NoSuchElementException:
        bandera = False
    context.test.assertFalse(bandera)
