from selenium import webdriver
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys

driver = webdriver.Chrome()
driver.get("http://120.25.127.201:18001/")

driver.maximize_window()
wait = WebDriverWait(driver, 10,0.5)

driver.find_element(By.PARTIAL_LINK_TEXT,"登录").click()

driver.switch_to.window(driver.window_handles[-1])

username="13845678901"
password="123456"

driver.find_element(By.ID,"txtUName").send_keys(username)
driver.find_element(By.ID,"txtPassword").send_keys(password)
driver.find_element(By.ID,"btnLogin").click()

time.sleep(0.5)
# presence_of_all_elements_located 检查元素是否存在于页面
element_phb=wait.until(EC.presence_of_element_located((By.LINK_TEXT,"排行榜")))
element_phb.click()

# 判断元素是否可以点击
# click_status=element.is_enabled()
# print(click_status)
# element.click()

# 判断元素是否可以可见
# displyed_status=element.is_displayed()
# print(displyed_status)


element_bk=wait.until(EC.presence_of_element_located((By.LINK_TEXT,"全球大返祖时代")))
ActionChains(driver).scroll_to_element(element_bk).click(element_bk).perform()

driver.find_element(By.LINK_TEXT,"全部目录").click()

element_zj=wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"第1章")))
element_zj.click()

element=wait.until(EC.presence_of_element_located((By.LINK_TEXT,"下一章")))
ActionChains(driver).scroll_to_element(element).click(element).perform()

# assert "第3章" in driver.title
time.sleep(3)