from behave import given, when, then
import time


@given(u'entro a la sección de Modificar Actividad')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="content-main"]/div[4]/table/tbody/tr[1]/th/a').click()
    time.sleep(0.5)

@given(u'selecciono la actividad "{activida}"')
def step_impl(context, activida):
    context.driver.find_element_by_xpath('//*[text() = "'+activida+'"]').click()
    time.sleep(0.5)

@given(u'remplazo el Programa por "{programa}"')
def step_impl(context, programa):
    context.driver.find_element_by_xpath('//*[@id="id_programa"]').clear()
    context.driver.find_element_by_xpath('//*[@id="id_programa"]').send_keys(programa)

@given(u'la actividad por "{actividad}"')
def step_impl(context, actividad):
    context.driver.find_element_by_xpath('//*[@id="id_actividad"]').clear()
    context.driver.find_element_by_xpath('//*[@id="id_actividad"]').send_keys(actividad)

@then(u'puedo ver la actividad "{actividad}" modificada en la lista de actividades.')
def step_impl(context, actividad): 
    tbody = context.driver.find_element_by_tag_name('tbody')
    trs = tbody.find_elements_by_tag_name('tr')
    lista_actividad = []
    for tr in trs:
        ths = tr.find_elements_by_tag_name('th')
        actividad = ths[0].text
        lista_actividad.append(actividad)
    context.test.assertIn(actividad, lista_actividad)