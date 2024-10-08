import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
from pyautogui import position

"""
使用ctrl+鼠标左键多选文件进行上传
"""


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/upload")
time.sleep(3)

driver.find_element(By.ID,"drag-drop-upload").click()
time.sleep(3)

# 获取当前鼠标位置的坐标
# x,y = position()
# print(x,y)

# pyautogui.moveTo(400, 51)
pyautogui.click(400, 51)
file_path=r"D:\dome\newuitest\study_selenium\image"
pyautogui.write(file_path)

pyautogui.press('enter')
pyautogui.press('enter')
time.sleep(3)

x,y = position()
print(x,y)

# 按下ctrl
pyautogui.keyDown('ctrl')

# 多选文件点击
pyautogui.click(238, 137)
pyautogui.click(360, 137)

# 松开ctrl
pyautogui.keyUp('ctrl')

# 两次回车生效
pyautogui.press('enter')
pyautogui.press('enter')
time.sleep(3)