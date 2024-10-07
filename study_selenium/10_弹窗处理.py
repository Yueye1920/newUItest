import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

driver.get("https://www.selenium.dev/selenium/web/alerts.html#")
time.sleep(2)

# 警告弹窗
def test_alert():
    driver.find_element(By.ID, "alert").click()
    time.sleep(2)
    # 显示等待，等待元素
    alert = wait.until(EC.alert_is_present())
    # 获取弹窗的文本信息
    text = alert.text
    print(text)
    # 点击弹窗确认
    alert.accept()
    time.sleep(2)
    assert text == "cheese","发生错误"


# 确认弹窗
# def test_confirm():
#     driver.find_element(By.LINK_TEXT,"test confirm").click()
#     time.sleep(2)
#     alert = wait.until(EC.alert_is_present())
#     text = alert.text
#     print(text)
#     # 点击确定
#     alert.accept()
#     # 点击取消
#     # alert.dismiss()
#     time.sleep(3)


# def test_prompt():
#     driver.find_element(By.LINK_TEXT,"prompt happen").click()
#     time.sleep(2)
#     # 显示等待
#     # alert = wait.until(EC.alert_is_present())
#     # Alert代替switch_to.alert
#     alert=Alert(driver)
#     # alert=driver.switch_to.alert
#     print(alert.text)
#     alert.send_keys("123")
#     time.sleep(5)
#     alert.accept()
#     time.sleep(5)

# def test_prompt2():
#     driver.find_element(By.LINK_TEXT,"prompt happen").click()
#     time.sleep(2)
#     # pyautogui.write()模拟写入
#     pyautogui.write("456")
#     time.sleep(2)
#     # pyautogui.press()模拟按键
#     pyautogui.press("enter")
#     time.sleep(5)