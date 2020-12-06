from behave import when, then
import time


@when(u'presiono el botón Eliminar de la actividad')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '//*[@id="actividad_form"]/div/div/p/a').click()
    time.sleep(0.5)


@then(u'puedo ver que la actividad "{actividad}" ya no está \
    en la lista de actividades.')
def step_impl(context, actividad):
    tbody = context.driver.find_element_by_tag_name('tbody')
    trs = tbody.find_elements_by_tag_name('tr')
    lista_actividad = []
    for tr in trs:
        ths = tr.find_elements_by_tag_name('th')
        actividad = ths[0].text
        lista_actividad.append(actividad)
    context.test.assertIn(actividad, lista_actividad)
