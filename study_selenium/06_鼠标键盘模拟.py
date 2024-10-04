import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() # 调起了一个浏览器回话

driver.get("http://120.25.127.201:18001/")
# driver.maximize_window()  # 把浏览器放到最大



# 发送键位：send_keys("大"+Keys.ENTER)

# driver.find_element(By.ID,"searchKey").send_keys("大"+Keys.ENTER)
# time.sleep(3)

# 清除 .clear()
# element=driver.find_element(By.ID,"searchKey")
# element.send_keys("大")
# time.sleep(3)
# element.clear()
# time.sleep(3)

element=driver.find_element(By.ID, "searchKey")

# 键盘操作，move_to_element()移动到对象上，send_keys()输入，perform()提交
ActionChains(driver).move_to_element(element).click_and_hold().send_keys("abc").perform()


# 键盘操作,按下shift
ActionChains(driver).key_down(Keys.SHIFT).perform()

# 释放所以Action
ActionBuilder(driver).clear_actions()

# 键盘操作,未释放大写Z，释放是小写z
ActionChains(driver).send_keys("z").perform()
time.sleep(3)