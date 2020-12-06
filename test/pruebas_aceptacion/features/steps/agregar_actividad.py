from behave import given, when, then
import time


@given(u'entro a la sección de Agregar Actividad')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '//*[@id="content-main"]/div[4]/table/tbody/tr[1]/td[1]/a').click()
    time.sleep(0.5)


@given(u'capturo los datos: Programa "{programa}", Componente " + \
    {componente}", Actividad "{actividad}", Monto "{monto} \
        ", Descripcion "{descripcion}", Mes "{mes}", Partida " + \
            {partida}", Año "{anio}"')
def step_impl(context, programa, componente, actividad, monto,
              descripcion, mes, partida, anio):
    context.driver.find_element_by_xpath(
        '//*[@id="id_programa"]').send_keys(programa)
    context.driver.find_element_by_xpath(
        '//*[@id="id_componente"]').send_keys(componente)
    context.driver.find_element_by_xpath(
        '//*[@id="id_actividad"]').send_keys(actividad)
    context.driver.find_element_by_xpath(
        '//*[@id="id_monto"]').send_keys(monto)
    context.driver.find_element_by_xpath(
        '//*[@id="id_descripcion"]').send_keys(descripcion)
    context.driver.find_element_by_xpath('//*[@id="id_mes"]').send_keys(mes)
    context.driver.find_element_by_xpath(
        '//*[@id="id_partida"]').send_keys(partida)
    context.driver.find_element_by_xpath('//*[@id="id_anio"]').send_keys(anio)
    time.sleep(0.5)


@when(u'presiono el botón Guardar de la actividad')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '//*[@id="actividad_form"]/div/div/input[1]').click()


@then(u'puedo ver la actividad "{actividad}" agregado en la \
      lista de actividades.')
def step_impl(context, actividad):
    tbody = context.driver.find_element_by_tag_name('tbody')
    trs = tbody.find_elements_by_tag_name('tr')
    lista_actividad = []
    for tr in trs:
        ths = tr.find_elements_by_tag_name('th')
        actividad = ths[0].text
        lista_actividad.append(actividad)
        context.test.assertIn(actividad, lista_actividad)
