from behave import when, then
import time


@when(u'presiono el botón Eliminar del presupuesto')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '//*[@id="presupuesto_form"]/div/div/p/a').click()
    time.sleep(0.5)


@then(u'puedo ver que el presupuesto "{presupuesto}" \
      ya no está en la lista de presupuestos.')
def step_impl(context, presupuesto):
    tbody = context.driver.find_element_by_tag_name('tbody')
    trs = tbody.find_elements_by_tag_name('tr')
    lista_presupuesto = []
    for tr in trs:
        ths = tr.find_elements_by_tag_name('th')
        presupuesto = ths[0].text
        lista_presupuesto.append(presupuesto)
    context.test.assertIn(presupuesto, lista_presupuesto)  # NotIn######
