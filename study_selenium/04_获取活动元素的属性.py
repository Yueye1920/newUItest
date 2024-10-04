import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() # 调起了一个浏览器回话

driver.get("http://120.25.127.201:18001/")
driver.maximize_window()  # 把浏览器放到最大

driver.find_element(By.XPATH, "//input").send_keys("111")
attr=driver.switch_to.active_element.get_attribute("id")   #获取id的属性
print(attr)