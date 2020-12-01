from behave import given, when, then
import time


@given(u'entro a la sección de Modificar Presupuesto')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="content-main"]/div[4]/table/tbody/tr[2]/th/a').click()

@given(u'selecciono el presupuesto "{presupuesto}"')
def step_impl(context, presupuesto):
    context.driver.find_element_by_xpath('//*[text() = "'+presupuesto+'"]').click()
    time.sleep(0.5)

@given(u'remplazo la fecha por "{fecha}"')
def step_impl(context, fecha):
    context.driver.find_element_by_xpath('//*[@id="id_fecha"]').clear()
    context.driver.find_element_by_xpath('//*[@id="id_fecha"]').send_keys(fecha)
    time.sleep(0.5)

@then(u'puedo ver el presupuesto "{presupuesto}" modificada en la lista de presupuestos.')
def step_impl(context, presupuesto): 
    tbody = context.driver.find_element_by_tag_name('tbody')
    trs = tbody.find_elements_by_tag_name('tr')
    lista_presupuesto = []
    for tr in trs:
        ths = tr.find_elements_by_tag_name('th')
        presupuesto = ths[0].text
        lista_presupuesto.append(presupuesto)
    context.test.assertIn(presupuesto, lista_presupuesto)