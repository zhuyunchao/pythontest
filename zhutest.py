#coding=utf-8
from selenium import webdriver
import time
browser = webdriver.Firefox()
first_url='http://baidu.com'
time.sleep(3)
browser.get(first_url)
time.sleep(2)
browser.find_element_by_id('kw').send_keys('seleniumm')
time.sleep(3)
browser.find_element_by_id('su').click()
time.sleep(5)
browser.close()

