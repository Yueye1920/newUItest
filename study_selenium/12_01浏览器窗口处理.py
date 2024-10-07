import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.get("http://120.25.127.201:18001/")
time.sleep(3)
# hd=driver.window_handles
# print(hd)
wait = WebDriverWait(driver, 10)
ori_window = driver.current_window_handle
print("原始窗口句柄id：",ori_window)

# 检查有没其他窗口
print(driver.window_handles)
# assert len(driver.window_handles)==1
print(len(driver.window_handles))

driver.find_element(By.LINK_TEXT,"作家专区").click()

# 等待新窗口被打开
wait.until(EC.number_of_windows_to_be(2))

# 获取所有窗口句柄
all_handles = driver.window_handles
print("所有窗口句柄",all_handles)

time.sleep(3)


# 遍历所有窗口，判断有没有新窗口
for window_handle in driver.window_handles:
    if window_handle !=ori_window:
        driver.switch_to.window(window_handle)
        break
print("当前窗口句柄id",driver.current_window_handle)

wait.until(EC.title_is("会员登录_读书屋"))
driver.close()
time.sleep(3)
driver.switch_to.window(ori_window)
print("当前窗口句柄id",driver.current_window_handle)
time.sleep(3)