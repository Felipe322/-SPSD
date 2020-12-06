from behave import given, when, then
from login import login
import time

@given(u'que estoy dentro del sistema como administrador')
def step_impl(context):
    login(context)

@given(u'entro a la sección de Agregar Capítulo')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element_by_xpath('//*[@id="navbarDropdownMenuLink"]').click()
    context.driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[2]/div/a[1]').click()

@given(u'capturo los datos: Clave "{clave}", Nombre "{nombre}"')
def step_impl(context, clave, nombre):
    context.driver.find_element_by_xpath('//*[@id="id_clave"]').send_keys(clave)
    context.driver.find_element_by_xpath('//*[@id="id_nombre"]').send_keys(nombre)
    time.sleep(0.5)

@when(u'presiono el botón Agregar')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div/div/form/button[1]').click()

@then(u'puedo ver el capítulo "{capitulo}" agregado en la lista de capítulos.')
def step_impl(context, capitulo): 
    cap = context.driver.find_element_by_xpath('//*[text() = "'+capitulo+'"]')
    #context.test.assertEqual(capitulo, cap)