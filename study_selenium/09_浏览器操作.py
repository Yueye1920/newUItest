import time

from selenium import webdriver

driver = webdriver.Chrome()

# 打开网站
driver.get("http://120.25.127.201:18001/")
time.sleep(3)

# 后退
driver.back()
time.sleep(3)

# 前进
driver.forward()
time.sleep(3)

# 刷新
driver.refresh()
time.sleep(3)

# 关闭
driver.close()
time.sleep(3)