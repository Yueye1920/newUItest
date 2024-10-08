import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 使用with关键字，执行时自动退出程序
with webdriver.Chrome() as driver:
    driver.get("http://120.25.127.201:18001/")
    time.sleep(3)
    wait = WebDriverWait(driver, 10)
    ori_window = driver.current_window_handle
    print("原始窗口句柄id", ori_window)

    # 检查有没其他窗口
    # print(driver.window_handles)
    # assert len(driver.window_handles)==1
    # print(len(driver.window_handles))

    driver.find_element(By.LINK_TEXT, "作家专区").click()

    # 等待新窗口被打开
    wait.until(EC.number_of_windows_to_be(2))

    # 获取所有窗口句柄
    all_handles = driver.window_handles
    print("所有窗口句柄", all_handles)

    time.sleep(3)

    # 切换到最后一个窗口
    driver.switch_to.window(all_handles[-1])
    print("当前窗口句柄id", driver.current_window_handle)

    wait.until(EC.title_is("会员登录_读书屋"))
    # driver.close()
    # time.sleep(3)

    # 切换值原来第一个窗口
    # driver.switch_to.window(ori_window)
    # print("当前窗口句柄id", driver.current_window_handle)
    # time.sleep(3)

    driver.find_element(By.ID, "txtUName").send_keys("123456789")
