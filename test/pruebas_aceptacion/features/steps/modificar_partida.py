from selenium.common.exceptions import NoSuchElementException
from behave import given, when, then
import time


@given(u'entro a la sección de Modificar Partida')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element_by_xpath(
        '/html/body/nav/div/ul/li[3]/a').click()
    context.driver.find_element_by_xpath(
        '//*[@id="navbarSupportedContent"]/ul/li[3]/div/a[2]').click()


@given(u'selecciono la partida "{partida}"')
def step_impl(context, partida):
    context.driver.find_element_by_xpath(
        "//a[@href='/partidas/editar/"+partida+"']").click()
    time.sleep(0.5)


@when(u'presiono el botón Guardar de la partida')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '/html/body/div/div/form/button[1]').click()


@then(u'puedo ver la partida "{partida}" modificada en la lista de partidas.')
def step_impl(context, partida):
    bandera = True
    try:
        context.driver.find_elements_by_xpath(
            '//td[contains(text(), "' + partida + '")]')
    except NoSuchElementException:
        bandera = False
    context.test.assertTrue(bandera)
