<<<<<<< HEAD
# -- FILE: behave4my_project/fixtures.py  (or in: features/environment.py)
=======
>>>>>>> 7e05e0b2a6c74336e0ec1bf7e99dd020c59ec6f2
from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import TestCase

@fixture
def browser_chrome(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(5)
    context.keys = Keys
    context.test = TestCase()

<<<<<<< HEAD
    context.url = 'http://127.0.0.1:8000/'
    yield context.driver
    context.driver.quit()


def before_all(context):
	use_fixture(browser_chrome, context)
=======
    context.url = 'http://192.168.33.10:8000'
    yield context.driver
    context.driver.quit()

def before_all(context):
    use_fixture(browser_chrome, context)
>>>>>>> 7e05e0b2a6c74336e0ec1bf7e99dd020c59ec6f2
