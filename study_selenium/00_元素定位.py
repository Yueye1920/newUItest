import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://120.25.127.201:18001/")
driver.maximize_window()


# id 定位搜索框
# element=driver.find_element(By.ID,"searchKey")
# element.send_keys("111")

# name 定位搜索框
# element=driver.find_element(By.NAME,"searchKey")
# element.send_keys("222")

# class 定位搜索框
# element=driver.find_element(By.CLASS_NAME,"s_int")
# element.send_keys("333")

# tag_name 定位搜索框
# element=driver.find_element(By.TAG_NAME,"input")
# element.send_keys("444")

# link_text 超链接文本定位
# element=driver.find_element(By.LINK_TEXT,"神医毒妃帅炸了")
# element.click()

# PARTIAL_LINK_TEXT 模糊匹配文字定位
# element=driver.find_element(By.PARTIAL_LINK_TEXT,"神医")
# element.click()

# XPATH 路径定位
# element=driver.find_element(By.XPATH,"//*[@id='topBooks2']/dd/a[1]")
# element.click()

# CSS_SELECTOR 路径定位
element=driver.find_element(By.CSS_SELECTOR,"#topBooks2 > dd > a:nth-child(1)")
element.click()


time.sleep(3)