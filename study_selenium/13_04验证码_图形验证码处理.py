
import pytesseract
from PIL import Image
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://120.25.127.201:18001/user/register.html")

# 将验证码保存到本地
element_yzm=driver.find_element(By.CLASS_NAME,"code_pic")
element_yzm.screenshot("yzm/yzm.png")
time.sleep(2)

# 使用PIL打开图像转为图像对象，并使用pytesseract进行图形识别
image=Image.open('yzm/yzm.png')
# 获取验证码
img_str = pytesseract.image_to_string(image)
# print(img_str)

username="13845678902"
password="123456"

driver.find_element(By.ID,"txtUName").send_keys(username)
driver.find_element(By.ID,"txtPassword").send_keys(password)
driver.find_element(By.ID,"TxtChkCode").send_keys(img_str)
driver.find_element(By.ID,"btnRegister").click()
time.sleep(3)