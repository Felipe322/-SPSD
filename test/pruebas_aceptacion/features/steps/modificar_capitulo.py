from selenium.common.exceptions import NoSuchElementException
from behave import given, when, then
import time


@given(u'entro a la sección de Capítulos')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element_by_xpath(
        '//*[@id="navbarDropdownMenuLink"]').click()
    context.driver.find_element_by_xpath(
        '//*[@id="navbarSupportedContent"]/ul/li[2]/div/a[2]').click()


@given(u'selecciono el capítulo "{capitulo}"')
def step_impl(context, capitulo):
    context.driver.find_element_by_xpath(
        "//a[@href='/capitulos/editar/"+capitulo+"']").click()
    time.sleep(0.5)


@given(u'remplazo el Nombre por "{nombre}"')
def step_impl(context, nombre):
    context.driver.find_element_by_xpath('//*[@id="id_nombre"]').clear()
    context.driver.find_element_by_xpath(
        '//*[@id="id_nombre"]').send_keys(nombre)
    time.sleep(0.5)


@when(u'presiono el botón Guardar')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '/html/body/div/div/form/button[1]').click()


@then(u'puedo ver el capítulo con el nombre "{nombre}" modificado en la lista de capítulos.')
def step_impl(context, nombre):
    bandera = True
    try:
        context.driver.find_elements_by_xpath(
            '//td[contains(text(), "' + nombre + '")]')
    except NoSuchElementException:
        bandera = False
    context.test.assertTrue(bandera)
