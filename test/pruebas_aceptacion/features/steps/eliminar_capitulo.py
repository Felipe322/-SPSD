from behave import given, when, then
import time

@when(u'presiono el botón Eliminar')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="capitulo_form"]/div/div/p/a').click()
    time.sleep(0.5)

@when(u'confirmo la acción con el botón de Si, estoy seguro')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="content"]/form/div/input[2]').click()
    time.sleep(0.5)

@then(u'puedo ver que el capítulo "{capitulo}" ya no está en la lista de capítulos.')
def step_impl(context, capitulo):
    tbody = context.driver.find_element_by_tag_name('tbody')
    trs = tbody.find_elements_by_tag_name('tr')
    lista_capitulo = []
    for tr in trs:
        ths = tr.find_elements_by_tag_name('th')
        capitulo = ths[0].text
        lista_capitulo.append(capitulo)
    context.test.assertIn(capitulo, lista_capitulo)