import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Chrome()
driver.get("http://120.25.127.201:18001/user/login.html")
driver.maximize_window()

"""
selenium 4.x版本新的定位方式
网格定位
above在上方，below在下方，Left of(左边)，Right(右边)，Near(附近)
driver.find_element(locate_with(By.TAG_NAME, "input").above({By.XPATH:"//*[@id='txtPassword']"}))
locate_with(写寻找的目标元素).above({By.XPATH:"已有的元素"})
"""

# 写的密码元素，实际定位账号元素
driver.find_element(locate_with(By.TAG_NAME, "input").above({By.XPATH:"//*[@id='txtPassword']"})).send_keys("111")



time.sleep(3)
