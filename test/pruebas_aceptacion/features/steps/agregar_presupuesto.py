from behave import given, when, then
import time


@given(u'entro a la sección de Agregar Presupuesto')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '//*[@id="content-main"]/div[4]/table/tbody/tr[2]/td[1]/a').click()
    time.sleep(0.5)


@given(u'capturo los datos: Año "{anio}", Fecha "{fecha}"')
def step_impl(context, anio, fecha):
    context.driver.find_element_by_xpath('//*[@id="id_anio"]').send_keys(anio)
    context.driver.find_element_by_xpath('//*[@id="id_fecha"]').clear()
    context.driver.find_element_by_xpath(
        '//*[@id="id_fecha"]').send_keys(fecha)
    time.sleep(0.5)


@when(u'presiono el botón Guardar del presupuesto')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '//*[@id="presupuesto_form"]/div/div/input[1]').click()


@then(u'puedo ver el presupuesto "{presupuesto}" agregado en \
    la lista de presupuestos.')
def step_impl(context, presupuesto):
    tbody = context.driver.find_element_by_tag_name('tbody')
    trs = tbody.find_elements_by_tag_name('tr')
    lista_presupuesto = []
    for tr in trs:
        ths = tr.find_elements_by_tag_name('th')
        presupuesto = ths[0].text
        lista_presupuesto.append(presupuesto)
    context.test.assertIn(presupuesto, lista_presupuesto)
