from behave import given, when, then
import time


@given(u'entro a la sección de Agregar Presupuesto')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '/html/body/nav/div/ul/li[4]/a').click()
    context.driver.find_element_by_xpath(
        '//*[@id="navbarSupportedContent"]/ul/li[4]/div/a[1]').click()
    time.sleep(0.5)


@given(u'capturo los datos: Año "{anio}", Fecha "{fecha}"')
def step_impl(context, anio, fecha):
    context.driver.find_element_by_xpath('//*[@id="id_anio"]').send_keys(anio)
    context.driver.find_element_by_xpath('//*[@id="id_fecha"]').clear()
    context.driver.find_element_by_xpath(
        '//*[@id="id_fecha"]').send_keys(fecha)
    time.sleep(0.5)


@when(u'presiono el botón Agregar del presupuesto')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '/html/body/div/div/form/button[1]').click()


@then(u'puedo ver el presupuesto "{presupuesto}" agregado en la lista de presupuestos.')
def step_impl(context, presupuesto):
    context.driver.find_element_by_xpath('//*[text() = "'+presupuesto+'"]')
