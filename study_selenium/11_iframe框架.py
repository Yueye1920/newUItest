import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/click_tests/click_in_iframe.html")
time.sleep(2)

# 点击框架直接进去了，带确定原因
# driver.find_element(By.ID,"ifr").click()
# time.sleep(3)

def test_ifame01():
    # 第一种切换框架写法
    # 获取iframe框架
    iframe=driver.find_element(By.ID,"ifr")
    print(iframe)
    # 切换到选择的 iframe
    driver.switch_to.frame(iframe)

    driver.find_element(By.LINK_TEXT, "Click me").click()
    time.sleep(2)

# def test_ifame02():
#     # 第二种切换框架写法
#     # 通过id或者name得到值，切换框架
#     driver.switch_to.frame('ifr')
#
#     driver.find_element(By.LINK_TEXT,"Click me").click()
#     time.sleep(2)


# def test_ifame03():
#     # 第三种切换框架写法
#     # 通过索引切换框架
#     driver.switch_to.frame(0)
#     driver.find_element(By.LINK_TEXT,"Click me").click()
#     time.sleep(2)

