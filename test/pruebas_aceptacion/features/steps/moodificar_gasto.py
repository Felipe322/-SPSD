from selenium.common.exceptions import NoSuchElementException
from behave import given, then
import time


@given(u'entro a la sección de Modificar Gasto')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '/html/body/nav/div/ul/li[6]/a').click()
    context.driver.find_element_by_xpath(
        '//*[@id="navbarSupportedContent"]/ul/li[6]/div/a[2]').click()


@given(u'selecciono el gasto "{gasto}"')
def step_impl(context, gasto):
    context.driver.find_element_by_xpath(
        "//a[@href='/gastos/editar/"+gasto+"']").click()
    time.sleep(0.5)


@given(u'remplazo el Precio Unitario por "{precio}"')
def step_impl(context, precio):
    context.driver.find_element_by_xpath(
        '//*[@id="id_precio_unitario"]').clear()
    context.driver.find_element_by_xpath(
        '//*[@id="id_precio_unitario"]').send_keys(precio)
    time.sleep(0.5)


@given(u'la cantidad por "{cantidad}"')
def step_impl(context, cantidad):
    context.driver.find_element_by_xpath('//*[@id="id_cantidad"]').clear()
    context.driver.find_element_by_xpath(
        '//*[@id="id_cantidad"]').send_keys(cantidad)
    time.sleep(0.5)


@when(u'presiono el botón Guardar del gasto')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '/html/body/div/div/form/button[1]').click()


@then(u'puedo ver el gasto "{gasto}" modificada en la lista de gastos.')
def step_impl(context, gasto):
    bandera = True
    try:
        context.driver.find_elements_by_xpath(
            '//td[contains(text(), "' + gasto + '")]')
    except NoSuchElementException:
        bandera = False
    context.test.assertTrue(bandera)
