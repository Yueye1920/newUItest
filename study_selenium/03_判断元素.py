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


#  title_is 直到标题出现“会员登录_读书屋”
# WebDriverWait(driver, 3).until(EC.title_is("会员登录_读书屋"))
# time.sleep(3)

# title_contains 直到标题包含“会员登录_读书屋”
# WebDriverWait(driver, 3).until(EC.title_contains("读书屋"))
# time.sleep(3)

# visibility_of_element_located 判断某个元素是否可见，代表元素非隐藏，且元素的宽和高都不等于0
element=WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
    (By.XPATH,"//*[@id='txtUName']")))
element.send_keys(username)

element=WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
    (By.XPATH,"//*[@id='txtPassword']")))
element.send_keys(password)
time.sleep(3)

# visibility_of(element) 判断袁术将会加载到页面dom中，并可用
element=WebDriverWait(driver, 3).until(EC.visibility_of(driver.find_element
    (By.XPATH,"//input[@id='btnLogin']")))
element.click()

#
element=WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located(
    (By.LINK_TEXT,book)))





time.sleep(3)