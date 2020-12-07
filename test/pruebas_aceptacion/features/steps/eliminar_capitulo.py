from selenium.common.exceptions import NoSuchElementException
from behave import given, when, then
import time


@when(u'presiono el botón Eliminar del capítulo "{capitulo}"')
def step_impl(context, capitulo):
    context.driver.find_element_by_xpath(
        "//a[@href='/capitulos/eliminar/"+capitulo+"']").click()
    time.sleep(0.5)


@then(u'puedo ver que el capítulo "{capitulo}" ya no está en la lista de capítulos.')
def step_impl(context, capitulo):
    bandera = True
    try:
        context.driver.find_element_by_xpath('//*[text() = "'+capitulo+'"]')
    except NoSuchElementException:
        bandera = False
    context.test.assertFalse(bandera)
