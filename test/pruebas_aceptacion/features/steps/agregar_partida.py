from behave import given, when, then
import time


@given(u'entro a la sección de Agregar Partida')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '/html/body/nav/div/ul/li[3]/a').click()
    context.driver.find_element_by_xpath(
        '//*[@id="navbarSupportedContent"]/ul/li[3]/div/a[1]').click()
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


@when(u'presiono el botón Agregar de la partida')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '/html/body/div/div/form/button[1]').click()


@then(u'puedo ver la partida "{partida}" agregado en la lista de partidas.')
def step_impl(context, partida):
    context.driver.find_element_by_xpath('//*[text() = "'+partida+'"]')
