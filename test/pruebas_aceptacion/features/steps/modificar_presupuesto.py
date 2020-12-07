from selenium.common.exceptions import NoSuchElementException
from behave import given, then
import time


@given(u'entro a la sección de Modificar Presupuesto')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '/html/body/nav/div/ul/li[4]/a').click()
    context.driver.find_element_by_xpath(
        '//*[@id="navbarSupportedContent"]/ul/li[4]/div/a[2]').click()

@given(u'selecciono el presupuesto "{presupuesto}"')
def step_impl(context, presupuesto):
    context.driver.find_element_by_xpath("//a[@href='/presupuestos/editar/"+presupuesto+"']").click()
    time.sleep(0.5)

@given(u'remplazo la fecha por "{fecha}"')
def step_impl(context, fecha):
    context.driver.find_element_by_xpath('//*[@id="id_fecha"]').clear()
    context.driver.find_element_by_xpath(
        '//*[@id="id_fecha"]').send_keys(fecha)
    time.sleep(0.5)

@when(u'presiono el botón Guardar del presupuesto')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div/div/form/button[1]').click()

@then(u'puedo ver el presupuesto con la fecha "{fecha}" modificada en la lista de presupuestos.')
def step_impl(context, fecha):
    bandera = True
    try:
        context.driver.find_elements_by_xpath('//td[contains(text(), "' + fecha + '")]')
    except NoSuchElementException:
        bandera = False
    context.test.assertTrue(bandera)
