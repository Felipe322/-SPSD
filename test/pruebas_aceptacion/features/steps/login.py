import time
from selenium import webdriver

def login(context):
    context.driver.get(context.url + '/admin/login/')
    context.driver.find_element_by_name('username').send_keys('Felipe')
    context.driver.find_element_by_name('password').send_keys('#Vagrant159753')
    context.driver.find_element_by_xpath(
        '//*[@id="login-form"]/div[3]/input').click()
    time.sleep(0.5)
