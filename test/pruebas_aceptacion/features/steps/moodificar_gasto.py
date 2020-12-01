from behave import given, when, then
import time


@given(u'entro a la sección de Modificar Gasto')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="content-main"]/div[2]/table/tbody/tr/th/a').click()

@given(u'selecciono el gasto "{gasto}"')
def step_impl(context, gasto):
    context.driver.find_element_by_xpath('//*[text() = "'+gasto+'"]').click()
    time.sleep(0.5)

@given(u'remplazo el Precio Unitario por "{precio}"')
def step_impl(context, precio):
    context.driver.find_element_by_xpath('//*[@id="id_precio_unitario"]').clear()
    context.driver.find_element_by_xpath('//*[@id="id_precio_unitario"]').send_keys(precio)
    time.sleep(0.5)

@given(u'la cantidad por "{cantidad}"')
def step_impl(context, cantidad):
    context.driver.find_element_by_xpath('//*[@id="id_cantidad"]').clear()
    context.driver.find_element_by_xpath('//*[@id="id_cantidad"]').send_keys(cantidad)
    time.sleep(0.5)

@then(u'puedo ver el gasto "{gasto}" modificada en la lista de gastos.')
def step_impl(context, gasto):
    tbody = context.driver.find_element_by_tag_name('tbody')
    trs = tbody.find_elements_by_tag_name('tr')
    lista_gasto = []
    for tr in trs:
        ths = tr.find_elements_by_tag_name('th')
        gasto = ths[0].text
        lista_gasto.append(gasto)
    context.test.assertIn(gasto, lista_gasto)