import time
<<<<<<< HEAD
from selenium import webdriver

def login(context):
	context.driver.get(context.url + 'admin/login')
	context.driver.find_element_by_name('username').send_keys("felipito")
	context.driver.find_element_by_name('password').send_keys("felipito")
	time.sleep(1)
	context.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/form/div[3]/input').click()
	time.sleep(1)
=======


def login(context):
    context.driver.get(context.url + '/admin/login/')
    context.driver.find_element_by_name('username').send_keys('Felipe')
    context.driver.find_element_by_name('password').send_keys('#Vagrant159753')
    context.driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    time.sleep(0.5)
>>>>>>> 7e05e0b2a6c74336e0ec1bf7e99dd020c59ec6f2
