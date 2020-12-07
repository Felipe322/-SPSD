from selenium.common.exceptions import NoSuchElementException
from behave import given, when, then
import time


@when(u'presiono el botón Eliminar de la actividad "{actividad}"')
def step_impl(context, actividad):
    context.driver.find_element_by_xpath(
        "//a[@href='/actividades/eliminar/"+actividad+"']").click()
    time.sleep(0.5)


@then(u'puedo ver que la actividad "{actividad}" ya no está en la lista de actividades.')
def step_impl(context, actividad):
    bandera = True
    try:
        context.driver.find_element_by_xpath('//*[text() = "'+actividad+'"]')
    except NoSuchElementException:
        bandera = False
    context.test.assertFalse(bandera)
