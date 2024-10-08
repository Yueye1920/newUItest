import os
import subprocess
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
调用Chrome.exe启动浏览器
手动执行chrome.bat文件
chrome.bat设置：
chrome.exe --remote-debugging-port=9222

"""


options = webdriver.ChromeOptions()
options.debugger_address = "127.0.0.1:9222"
driver = webdriver.Chrome(options=options)

driver.get("https://cart.taobao.com/cart.htm")
username='15616246124'
password='huace6666..'
time.sleep(0.5)
driver.find_element(By.ID,"fm-login-id").send_keys(username)
driver.find_element(By.ID,"fm-login-password").send_keys(password)

# os.system('taskkill /f /im chromedriver.sh')
# os.system('taskkill /f /im chrome.sh')
# subprocess.call(["taskkill","/f","fim","chrome.exe"])