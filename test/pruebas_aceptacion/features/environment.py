from behave import fixture, use_fixture
from unittest import TestCase
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


@fixture
def browser_chrome(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(5)
    context.keys = Keys
    context.test = TestCase()

    context.url = 'http://192.168.33.10:8000'
    yield context.driver
    context.driver.quit()


def before_all(context):
    use_fixture(browser_chrome, context)
