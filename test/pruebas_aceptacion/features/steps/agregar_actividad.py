from selenium.common.exceptions import NoSuchElementException
from behave import given, when, then
import time


@given(u'entro a la sección de Agregar Actividad')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '/html/body/nav/div/ul/li[5]/a').click()
    context.driver.find_element_by_xpath(
        '//*[@id="navbarSupportedContent"]/ul/li[5]/div/a[1]').click()
    time.sleep(0.5)

@given(u'capturo los datos: Programa "{programa}", Componente "{componente}", Actividad "{actividad}", Monto "{monto}", Descripcion "{descripcion}", Mes "{mes}", Partida "{partida}", Año "{anio}"')
def step_impl(context, programa, componente, actividad, monto,
              descripcion, mes, partida, anio):
    context.driver.find_element_by_xpath(
        '//*[@id="id_programa"]').send_keys(programa)
    context.driver.find_element_by_xpath(
        '//*[@id="id_componente"]').send_keys(componente)
    context.driver.find_element_by_xpath(
        '//*[@id="id_actividad"]').send_keys(actividad)
    context.driver.find_element_by_xpath(
        '//*[@id="id_monto"]').send_keys(monto)
    context.driver.find_element_by_xpath(
        '//*[@id="id_descripcion"]').send_keys(descripcion)
    context.driver.find_element_by_xpath('//*[@id="id_mes"]').send_keys(mes)
    context.driver.find_element_by_xpath(
        '//*[@id="id_partida"]').send_keys(partida)
    context.driver.find_element_by_xpath('//*[@id="id_anio"]').send_keys(anio)
    time.sleep(0.5)

@when(u'presiono el botón Agregar de la actividad')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '/html/body/div/div/form/div[9]/button[1]').click()

@then(u'puedo ver la actividad agregada, con la descripción "{descripcion}".')
def step_impl(context, descripcion):
    bandera = True
    try:
        context.driver.find_elements_by_xpath('//td[contains(text(), "' + descripcion + '")]')
    except NoSuchElementException:
        bandera = False
    context.test.assertTrue(bandera)
