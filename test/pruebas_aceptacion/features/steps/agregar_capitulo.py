from behave import given, when, then
from login import login
import time

@given(u'que estoy dentro del sistema como administrador')
def step_impl(context):
    login(context)


@given(u'entro a la sección de Agregar Capítulo')
def step_impl(context):
	time.sleep(1)
	context.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[1]/a').click()


@given(u'capturo los datos: Clave "{clave}" y nombre "{nombre}"')
def step_impl(context, clave, nombre):
    time.sleep(1)
    context.driver.find_element_by_xpath('/html/body/div/div[3]/div/div[1]/div/form/div/fieldset/div[1]/div/input').send_keys(clave)
    time.sleep(1)
    context.driver.find_element_by_xpath('/html/body/div/div[3]/div/div[1]/div/form/div/fieldset/div[2]/div/input').send_keys(nombre)


@when(u'presiono el botón Guardar')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_xpath('/html/body/div/div[3]/div/div[1]/div/form/div/div/input[1]').click()


@then(u'puedo ver en capitulo "2000" agregado en la lista de capítulos')
def step_impl(context, clave):
	tbody = context.driver.find_element_by_tag_name('tbody')
	trs = tbody.find_elements_by_tag_name('tr')
	lista_clave = []
	for tr in trs:
		tds = tr.find_elements_by_tag_name('th')
		nombre = ths[0].text
		lista_capitulos.append(clave)

	context.test.assertIn(clave, lista_clave)