import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://120.25.127.201:18001/")
time.sleep(3)

width =driver.get_window_size().get("width")
height =driver.get_window_size().get("height")
print(width,height)


# 设置指定窗口大小
driver.set_window_size(1024,768)
time.sleep(2)

# 将窗口移动到显示器左上角
driver.set_window_position(0,0)


# 设置最大化窗口
driver.maximize_window()
time.sleep(2)

width1 =driver.get_window_size().get("width")
height2 =driver.get_window_size().get("height")
print(width1,height2)

# 设置最小化窗口
driver.minimize_window()
time.sleep(2)

# 设置全屏窗口
driver.fullscreen_window()
time.sleep(2)

# 屏幕截图
driver.save_screenshot("image/image.png")
time.sleep(2)

# 元素屏幕截图
element=driver.find_element(By.PARTIAL_LINK_TEXT,"神医")
element.screenshot("image/image2.png")
time.sleep(2)

text=driver.execute_script('return arguments[0].innerText',element)
print(text)