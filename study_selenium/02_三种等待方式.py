import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
强制等待
time.sleep()
"""

"""
隐式等待,全局适用，10秒等待页面加载时间，超过10秒就不等了
只对当前会话有效
优点：代码精简，只需要设置一次
缺点：效率低，不够准确，耽误时间
隐式等待与显示等待不可同时使用
driver.implicitly_wait(10)
"""

"""
显示等待


WebDriverWait(driver, 10).until()
"""


driver = webdriver.Chrome()
driver.get("http://120.25.127.201:18001/user/login.html")
driver.maximize_window()

# 强制等待
# time.sleep(10)

# 隐式等待
# driver.implicitly_wait(10)

# 显示等待
"""
WebDriverWait(driver, timeout,poll_frequency,ignored_exceptions).until()
driver:浏览器驱动
timeout:
poll_frequency:
ignored_exceptions:
"""
"""
WebDriverWait有两个方法，until() 和 until_not()
显示等待需要每次设置
优化代码运行时间
"""

# until()   在时间内，直到这个元素出现
element=WebDriverWait(driver, 10,0.5,None).until(EC.presence_of_element_located((By.XPATH,"//*[@id='txtUName']")))
element.send_keys("USER")
# until_not()  在时间内，直到这个元素消失
element=WebDriverWait(driver, 10,0.5,None).until_not(EC.presence_of_element_located(
    (By.XPATH,"//*[@id='txtUName']")))
element.send_keys("USER")
time.sleep(5)