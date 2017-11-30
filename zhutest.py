#coding=utf-8
from selenium import webdriver
import time
browser = webdriver.Firefox()
first_url='http://baidu.com'
print u'diyige %s' % (first_url)
browser.get(first_url)
time.sleep(3)
seconr_url='http://v.baidu.com/'
print u'dierge%s' %(seconr_url)
time.sleep(5)

