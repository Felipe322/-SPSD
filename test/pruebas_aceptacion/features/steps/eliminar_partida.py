from behave import given, when, then
import time


@when(u'presiono el botón Eliminar de la partida')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="partida_form"]/div/div/p/a').click()
    time.sleep(0.5)

@then(u'puedo ver que la partida "{partida}" ya no está en la lista de partidas.')
def step_impl(context, partida):
    tbody = context.driver.find_element_by_tag_name('tbody')
    trs = tbody.find_elements_by_tag_name('tr')
    lista_partida = []
    for tr in trs:
        ths = tr.find_elements_by_tag_name('th')
        partida = ths[0].text
        lista_partida.append(partida)
    context.test.assertIn(partida, lista_partida)#NotIn######
