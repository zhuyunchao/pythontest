#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
browser = webdriver.Firefox()
first_url='http://mail.163.com/'
browser.get(first_url)
time.sleep(5)
a = browser.find_element_by_xpath("//input[@name='email']")
a.send_keys('15210242844')
aaaaa3123