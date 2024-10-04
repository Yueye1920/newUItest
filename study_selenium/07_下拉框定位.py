import time
from tkinter.tix import Select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

"""
https://sahitest.com/demo/selectTest.htm
"""
driver = webdriver.Chrome()
driver.get("https://sahitest.com/demo/selectTest.htm")
time.sleep(2)

# 创建一个select对象
# select_element = driver.find_element(By.ID,"s1Id")
# select_object=Select(select_element)  #实例化对象
# time.sleep(3)

# 有三种方法选择选项
# 选项索引
# select_object.select_by_index(1)
# time.sleep(3)

# 选项value值
# select_object.select_by_value("o3")
# time.sleep(3)

# 选项文本
# select_object.select_by_visible_text('o2')
# time.sleep(3)

# 检查被选择钓的选项
# all_selectd_options=select_object.all_selected_options
# print(all_selectd_options)

# 返回第一个备选项被选项
# first_selectd_options=select_object.first_selected_option
# print(first_selectd_options)

# 返回所有选项
# alls_selectd_options=select_object.options
# print(alls_selectd_options)

select_element=driver.find_element(By.XPATH,"//*[@multiple='multiple']")
select_multple_object=Select(select_element)
select_multple_object.select_by_index(3)
select_multple_object.select_by_index(1)
time.sleep(2)

# 确定是否运行多选
# allow=select_multple_object.is_multiple
# print("确认是否允许多选")
# print(allow)

# 验证正向选择以及反选选择
# 根据索引进行反选
# select_multple_object.deselect_by_index(3)
# time.sleep(2)

# 根据value进行反选
# select_multple_object.deselect_by_value("o1val")
# time.sleep(3)

# 根据文本进行反选
# select_multple_object.deselect_by_visible_text("o1")
# time.sleep(3)

# 全部反选
select_multple_object.deselect_all()
time.sleep(3)