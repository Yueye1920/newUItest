from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.example.com")

# 检查页面上是否存在一个id为"element_id"的元素
assert "element_id" in driver.page_source

# 检查标题是否匹配
assert driver.title == "My Page Title"

# 检查标题中是否包含指定内容
assert "第3章" in driver.title

# 检查元素文本是否匹配
element = driver.find_element(By.ID,"element_id")
assert "expected_text" in element.text

# 检查元素是否可见
element = driver.find_element(By.ID,"element_id")
assert element.is_displayed()

# 检查元素是否被选中
element = driver.find_element(By.ID,"element_id")
assert element.is_selected()

# 检查元素是否可点击
element = driver.find_element(By.ID,"element_id")
assert element.is_enabled()

# 检查元素的属性（例如，链接的URL）
element = driver.find_element(By.ID,"element_id")
assert element.get_attribute("href") == "http://www.example.com"