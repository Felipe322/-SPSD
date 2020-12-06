import time
from selenium import webdriver


def login(context):
    context.driver.get(context.url + '/login/')
    context.driver.find_element_by_name('username').send_keys('Felipe')
    context.driver.find_element_by_name('password').send_keys('#Vagrant159753')
    context.driver.find_element_by_xpath(
        '/html/body/div/div[2]/div/form/div[3]/div[2]/button').click()
    time.sleep(0.5)
