import time

import pytest
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(2)

# 鼠标点击并保持
def test_click_and_hold():
    driver.get("https://www.selenium.dev/selenium/web/mouse_interaction.html")
    time.sleep(3)
    click_elem = driver.find_element(By.ID,"clickable")
    ActionChains(driver).click_and_hold(click_elem).perform()
    time.sleep(1)
    assert driver.find_element(By.ID,"click-status").text=="focused"
    time.sleep(1)


"""
鼠标操作
click(element)单击鼠标左键；
double_click(element)双击鼠标左键；
context_click(element)单击鼠标右键；
click_and_hold(element)长按鼠标左键；
move_to_element(element)鼠标悬停到某个元素；
drag_and_drop(element)把元素拖动到另一个元素后松开；
drag_and_drop_by_offset(source, xoffset, yoffset)把元素拖到某个坐标然后松开；
move_by_offset(xoffset, yoffset)鼠标从当前位置移动到某个坐标；
"""
"""
滚轮操作
actions.scroll_to_element(element) 滚动到元素；
actions.scroll_by_amount(delta_x, delta_y) 从当前焦点直接滚动；
"""
"""
内嵌框架iframe
"""

# 滚动到元素
# def test_scroll_to_element():
#     driver.get(
#         "https://www.selenium.dev/selenium/web/scrolling_tests/frame_with_nested_scrolling_frame_out_of_view.html")
#     time.sleep(3)
#     iframe = driver.find_element(By.TAG_NAME, "iframe")
#     ActionChains(driver).scroll_to_element(iframe).perform()
#     time.sleep(3)


# 滚动到指定坐标
# def test_scroll_by_amount():
#     driver.get(
#         "https://www.selenium.dev/selenium/web/scrolling_tests/frame_with_nested_scrolling_frame_out_of_view.html")
#     time.sleep(3)
#     footer = driver.find_element(By.TAG_NAME, "footer")
#     delta_x = footer.rect['x']
#     delta_y = footer.rect['y']
#     print("坐标x{}:y{}".format(delta_x,delta_y))
#     # ActionChains(driver).scroll_by_amount(delta_x,delta_y).perform()
#     ActionChains(driver).scroll_by_amount(0, delta_y).perform()
#     time.sleep(3)

