import time
from selenium import webdriver
import re
browser=webdriver.Chrome()
browser.get("http://www.baidu.com")
page =browser.page_source
print(page)
time.sleep(5)
browser.quit()
print("hello worl1d")
print("哈哈")
print("你好不好")
print('曹月旺')
print("haha1")
print("hahahahahahaha11")
