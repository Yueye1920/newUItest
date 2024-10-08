import pytest

from selenium import webdriver
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys

driver = webdriver.Chrome()
driver.get("http://120.25.127.201:18001/")

driver.maximize_window()
wait = WebDriverWait(driver, 10)

element=driver.find_element(By.LINK_TEXT,"云上夕轮")
url=element.get_attribute('herf')
print(url)
time.sleep(3)