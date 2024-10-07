import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://120.25.127.201:18001/")
time.sleep(3)

# 打开新的浏览器窗口
driver.switch_to.new_window('tab')

# 打开并切换新窗口
driver.switch_to.new_window('window')
time.sleep(5)