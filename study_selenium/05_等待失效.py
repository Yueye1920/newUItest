import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://120.25.127.201:18001/user/login.html")
driver.maximize_window()

username="13845678901"
password="123456"
book="神医毒妃帅炸了"

# 隐式等待失效的情况下，使用显示等待。


driver.implicitly_wait(10)
time.sleep(3)
driver.find_element(By.ID, "txtUName").send_keys(username)
driver.find_element(By.ID, "txtPassword").send_keys(password)
driver.find_element(By.ID, "btnLogin").click()
time.sleep(3)
driver.find_element(By.LINK_TEXT,"我的书架").click()
time.sleep(3)