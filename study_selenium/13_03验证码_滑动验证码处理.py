from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://layui.dev/docs/2/slider/index.html")

# 滚动条上原点
slider_btn=driver.find_element(By.CLASS_NAME,"layui-slider-wrap-btn")

# 获取滑动条长度
slider=driver.find_element(By.CLASS_NAME,"layui-slider ")
delta_x=slider.size['width']
print(delta_x)

# 快速移动滑动条
# ActionChains(driver).click_and_hold(slider_btn).move_by_offset(delta_x,0).perform()
# time.sleep(4)

# 慢速移动滑动条
ActionChains(driver).click_and_hold(slider_btn).perform()
while   True:
    try:
        #移动鼠标，第一个参数为x距离
        action=ActionChains(driver).move_by_offset(100,0).perform()
    except BaseException as e:
        print(e)
        break
    time.sleep(0.01)

ActionBuilder(driver).clear_actions()