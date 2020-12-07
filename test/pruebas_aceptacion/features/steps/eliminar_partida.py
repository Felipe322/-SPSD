from selenium.common.exceptions import NoSuchElementException
from behave import given, when, then
import time


@when(u'presiono el botón Eliminar de la partida "{partida}"')
def step_impl(context, partida):
    context.driver.find_element_by_xpath("//a[@href='/partidas/eliminar/"+partida+"']").click()
    time.sleep(0.5)

@then(u'puedo ver que la partida "{partida}" ya no está en la lista de partidas.')
def step_impl(context, partida):
    bandera = True
    try:
        context.driver.find_element_by_xpath('//*[text() = "'+partida+'"]')
    except NoSuchElementException:
        bandera = False
    context.test.assertFalse(bandera)
