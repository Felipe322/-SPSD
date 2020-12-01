from behave import given, when, then
import time


@given(u'entro a la sección de Modificar Partida')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="content-main"]/div[3]/table/tbody/tr[2]/td[2]/a').click()

@given(u'selecciono la partida "{partida}"')
def step_impl(context, partida):
    context.driver.find_element_by_xpath('//*[text() = "'+partida+'"]').click()
    time.sleep(0.5)

@then(u'puedo ver la partida "{partida}" modificada en la lista de partidas.')
def step_impl(context, partida):
    tbody = context.driver.find_element_by_tag_name('tbody')
    trs = tbody.find_elements_by_tag_name('tr')
    lista_partida = []
    for tr in trs:
        ths = tr.find_elements_by_tag_name('th')
        partida = ths[0].text
        lista_partida.append(partida)
    context.test.assertIn(partida, lista_partida)