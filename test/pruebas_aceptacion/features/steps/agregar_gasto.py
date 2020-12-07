from selenium.common.exceptions import NoSuchElementException
from behave import given, when, then
import time


@given(u'entro a la sección de Agregar Gasto')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '/html/body/nav/div/ul/li[6]/a').click()
    context.driver.find_element_by_xpath(
        '//*[@id="navbarSupportedContent"]/ul/li[6]/div/a[1]').click()
    time.sleep(0.5)


@given(u'capturo los datos: Descripcion "{descripcion}", Proveedor "{proveedor}", Precio Unitario "{precio}", Cantidad "{cantidad}", Fecha "{fecha}", Actividad "{actividad}"')
def step_impl(context, descripcion, proveedor, precio, cantidad,
              fecha, actividad):
    context.driver.find_element_by_xpath(
        '//*[@id="id_descripcion"]').send_keys(descripcion)
    context.driver.find_element_by_xpath(
        '//*[@id="id_proveedor"]').send_keys(proveedor)
    context.driver.find_element_by_xpath(
        '//*[@id="id_precio_unitario"]').send_keys(precio)
    context.driver.find_element_by_xpath(
        '//*[@id="id_cantidad"]').send_keys(cantidad)
    context.driver.find_element_by_xpath('//*[@id="id_fecha"]').clear()
    context.driver.find_element_by_xpath(
        '//*[@id="id_fecha"]').send_keys(fecha)
    context.driver.find_element_by_xpath(
        '//*[@id="id_id_actividad"]').send_keys(actividad)
    time.sleep(0.5)


@when(u'presiono el botón Agregar del gasto')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '/html/body/div/div/form/button[1]').click()


@then(u'puedo ver el gasto "{gasto}" agregado en la lista de gastos.')
def step_impl(context, gasto):
    bandera = True
    try:
        context.driver.find_elements_by_xpath(
            '//td[contains(text(), "' + gasto + '")]')
    except NoSuchElementException:
        bandera = False
    context.test.assertTrue(bandera)
