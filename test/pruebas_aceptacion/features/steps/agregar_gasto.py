from behave import given, when, then
import time


@given(u'entro a la sección de Agregar Gasto')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="content-main"]/div[2]/table/tbody/tr/td[1]/a').click()
    time.sleep(0.5)

@given(u'capturo los datos: Descripcion "{descripcion}", Proveedor "{proveedor}", Precio Unitario "{precio}", Cantidad "{cantidad}", Fecha "{fecha}", Actividad "{actividad}"')
def step_impl(context, descripcion, proveedor, precio, cantidad, fecha, actividad):
    context.driver.find_element_by_xpath('//*[@id="id_descripcion"]').send_keys(descripcion)
    context.driver.find_element_by_xpath('//*[@id="id_proveedor"]').send_keys(proveedor)
    context.driver.find_element_by_xpath('//*[@id="id_precio_unitario"]').send_keys(precio)
    context.driver.find_element_by_xpath('//*[@id="id_cantidad"]').send_keys(cantidad)
    context.driver.find_element_by_xpath('//*[@id="id_fecha"]').clear()
    context.driver.find_element_by_xpath('//*[@id="id_fecha"]').send_keys(fecha)
    context.driver.find_element_by_xpath('//*[@id="id_id_actividad"]').send_keys(actividad)
    time.sleep(0.5)

@when(u'presiono el botón Guardar del gasto')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="gasto_form"]/div/div/input[1]').click()

@then(u'puedo ver el gasto "{gasto}" agregado en la lista de gastos.')
def step_impl(context, gasto): 
    tbody = context.driver.find_element_by_tag_name('tbody')
    trs = tbody.find_elements_by_tag_name('tr')
    lista_gasto = []
    for tr in trs:
        ths = tr.find_elements_by_tag_name('th')
        gasto = ths[0].text
        lista_gasto.append(gasto)
    context.test.assertIn(gasto, lista_gasto)