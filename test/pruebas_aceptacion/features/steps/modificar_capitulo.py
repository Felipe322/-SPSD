from behave import given, when, then
import time


@given(u'entro a la sección de Capítulos')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="content-main"]/div[3]/table/tbody/tr[1]/th/a').click()
    time.sleep(0.5)

@given(u'selecciono el capítulo "{capitulo}"')
def step_impl(context, capitulo):
    context.driver.find_element_by_xpath('//*[text() = "'+capitulo+'"]').click()
    time.sleep(0.5)

@given(u'remplazo el Nombre por "{nombre}"')
def step_impl(context, nombre):
    context.driver.find_element_by_xpath('//*[@id="id_nombre"]').clear()
    context.driver.find_element_by_xpath('//*[@id="id_nombre"]').send_keys(nombre)

@then(u'puedo ver el capítulo "{capitulo}" modificado en la lista de capítulos.')
def step_impl(context, capitulo):
    tbody = context.driver.find_element_by_tag_name('tbody')
    trs = tbody.find_elements_by_tag_name('tr')
    lista_capitulo = []
    for tr in trs:
        ths = tr.find_elements_by_tag_name('th')
        capitulo = ths[0].text
        lista_capitulo.append(capitulo)
    context.test.assertIn(capitulo, lista_capitulo)