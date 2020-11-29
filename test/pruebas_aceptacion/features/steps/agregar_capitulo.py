from behave import given, when, then
from login import login
import time


@given(u'que estoy dentro del sistema como administrador')
def step_impl(context):
    login(context)

@given(u'entro a la sección de Agregar Capítulo')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element_by_xpath('//*[@id="content-main"]/div[3]/table/tbody/tr[1]/td[1]/a').click()

@given(u'capturo los datos: Clave "{clave}", Nombre "{nombre}"')
def step_impl(context, clave, nombre):
    context.driver.find_element_by_xpath('//*[@id="id_clave"]').send_keys(clave)
    context.driver.find_element_by_xpath('//*[@id="id_nombre"]').send_keys(nombre)

@when(u'presiono el botón Guardar')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="capitulo_form"]/div/div/input[1]').click()

@then(u'puedo ver el capítulo "{capitulo}" agregado en la lista de capítulos.')
def step_impl(context, capitulo): 
    tbody = context.driver.find_element_by_tag_name('tbody')
    trs = tbody.find_elements_by_tag_name('tr')
    lista_capitulo = []
    for tr in trs:
        ths = tr.find_elements_by_tag_name('th')
        capitulo = ths[0].text
        lista_capitulo.append(capitulo)
    context.test.assertIn(capitulo, lista_capitulo)