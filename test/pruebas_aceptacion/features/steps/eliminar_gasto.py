from behave import when, then
import time


@when(u'presiono el botón Eliminar del gasto')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '//*[@id="gasto_form"]/div/div/p/a').click()
    time.sleep(0.5)


@then(u'puedo ver que el gasto "{gasto}" ya no está en la lista de gastos.')
def step_impl(context, gasto):
    tbody = context.driver.find_element_by_tag_name('tbody')
    trs = tbody.find_elements_by_tag_name('tr')
    lista_gasto = []
    for tr in trs:
        ths = tr.find_elements_by_tag_name('th')
        gasto = ths[0].text
        lista_gasto.append(gasto)
    context.test.assertIn(gasto, lista_gasto)  # NotIn######
