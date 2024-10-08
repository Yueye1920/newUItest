import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui

"""
使用系统窗口下方的输入框指定目录文件进行上传（简单有效）
"""

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/upload")
time.sleep(3)

driver.find_element(By.ID,"drag-drop-upload").click()
time.sleep(3)

# pyautogui.press("backspace")
file1=r"D:\dome\newuitest\study_selenium\yzm\yzm.png"
pyautogui.write(file1)
# 按下enter，按两次回车选择文件
pyautogui.press("enter")
pyautogui.press("enter")

time.sleep(3)

driver.find_element(By.ID,"drag-drop-upload").click()
time.sleep(3)
file2=r"D:\dome\newuitest\study_selenium\yzm\yzm.png"
pyautogui.write(file2)
# 按下enter，按两次回车选择文件
pyautogui.press("enter")
pyautogui.press("enter")



# 获取源码
content=driver.page_source
print(content)

# 在源码中招关键字
if driver.page_source.find("yzm.png")!=-1:
    print("File Uploaded success")
else:
    print("File Uploaded  not success")

time.sleep(8)
