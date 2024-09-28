import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
url=http://120.25.127.201:18001/
"""
"""
web自动化原理:通过w3c协议，使用接口方式来提供调用的方式，用接口的形式模拟用户的操作。
"""

driver = webdriver.Chrome() # 调起了一个浏览器回话

driver.get("http://120.25.127.201:18001/")
driver.maximize_window()  # 把浏览器放到最大

driver.find_element(By.CSS_SELECTOR, "input.s_int").send_keys("111")

# #searchKey



time.sleep(10) # 强制休眠
