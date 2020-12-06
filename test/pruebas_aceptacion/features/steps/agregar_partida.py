from behave import given, when, then
import time


@given(u'entro a la sección de Agregar Partida')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '//*[@id="content-main"]/div[3]/table/tbody/tr[2]/td[1]/a').click()
    time.sleep(0.5)


@given(u'capturo los datos de la partida como: Clave "{clave}", \
    Nombre "{nombre}", Descripción "{descripcion}", Capítulo "{capitulo}"')
def step_impl(context, clave, nombre, descripcion, capitulo):
    context.driver.find_element_by_xpath(
        '//*[@id="id_clave"]').send_keys(clave)
    context.driver.find_element_by_xpath(
        '//*[@id="id_nombre"]').send_keys(nombre)
    context.driver.find_element_by_xpath(
        '//*[@id="id_descripcion"]').send_keys(descripcion)
    context.driver.find_element_by_xpath(
        '//*[@id="id_capitulo"]').send_keys(capitulo)
    time.sleep(0.5)


@when(u'presiono el botón Guardar de la partida')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '//*[@id="partida_form"]/div/div/input[1]').click()


@then(u'puedo ver la partida "{partida}" agregado en la lista de partidas.')
def step_impl(context, partida):
    tbody = context.driver.find_element_by_tag_name('tbody')
    trs = tbody.find_elements_by_tag_name('tr')
    lista_partida = []
    for tr in trs:
        ths = tr.find_elements_by_tag_name('th')
        partida = ths[0].text
        lista_partida.append(partida)
    context.test.assertIn(partida, lista_partida)
