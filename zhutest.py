#coding=utf-8
from selenium import webdriver
import time
browser = webdriver.Firefox()
first_url='http://baidu.com'
print u'进入第一个网页 %s' % (first_url)
browser.get(first_url)
time.sleep(3)
seconr_url='http://v.baidu.com/'
print u'进入第二个视频网页 %s' %(seconr_url)
time.sleep(5)

browser.quit()
