from behave import given, when, then
from login import login
import time

@given(u'entro a la sección de Capítulos')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[1]/th/a'),click()
    time.sleep(1)

@given(u'selecciono el capitulo "2000 - MATERIALES Y SUMINISTROS"')
def step_impl(context):
    pass


@given(u'remplazo el Nombre por "MATERIALES Y SUMINISTROS 2"')
def step_impl(context):
    pass


@then(u'puedo ver en capitulo "2000 - MATERIALES Y SUMINISTROS 2" modificado en la lista de capítulos')
def step_impl(context):
	pass