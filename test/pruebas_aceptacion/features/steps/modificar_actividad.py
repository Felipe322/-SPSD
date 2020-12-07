from selenium.common.exceptions import NoSuchElementException
from behave import given, then
import time


@given(u'entro a la sección de Modificar Actividad')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '/html/body/nav/div/ul/li[5]/a').click()
    context.driver.find_element_by_xpath(
        '//*[@id="navbarSupportedContent"]/ul/li[5]/div/a[2]').click()
    time.sleep(0.5)


@given(u'selecciono la actividad "{activida}"')
def step_impl(context, activida):
    context.driver.find_element_by_xpath(
        "//a[@href='/actividades/editar/"+activida+"']").click()
    time.sleep(0.5)


@given(u'remplazo el Programa por "{programa}"')
def step_impl(context, programa):
    context.driver.find_element_by_xpath('//*[@id="id_programa"]').clear()
    context.driver.find_element_by_xpath(
        '//*[@id="id_programa"]').send_keys(programa)


@when(u'presiono el botón Guardar de la actividad')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '/html/body/div/div/form/button[1]').click()


@then(u'puedo ver la actividad "{actividad}" modificada en la lista de actividades.')
def step_impl(context, actividad):
    bandera = True
    try:
        context.driver.find_elements_by_xpath(
            '//td[contains(text(), "' + actividad + '")]')
    except NoSuchElementException:
        bandera = False
    context.test.assertTrue(bandera)
