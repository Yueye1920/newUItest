import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/upload")
time.sleep(3)

# input输入框选择文件可以使用send.keys上传
driver.find_element(By.ID,"file-upload").send_keys(
    r"D:\dome\newuitest\study_selenium\yzm\yzm.png"
)

time.sleep(3)

driver.find_element(By.ID,"file-submit").click()
time.sleep(3)


# 获取网页源代码
content=driver.page_source
print(content)

# 在源码中招关键字
if driver.page_source.find("File Uploaded!")!=-1:
    print("File Uploaded success")
else:
    print("File Uploaded  not success")