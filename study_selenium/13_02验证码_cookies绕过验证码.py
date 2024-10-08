import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

"""
1)先手动登录，获取cookies
2)使用driver.add_cookie添加
3)刷新页签

"""

driver.get("http://120.25.127.201:18001/")
time.sleep(3)
driver.add_cookie({'name': 'Authorization',
                   'value': 'eyJhbGciOiJIUzUxMiJ9.eyJleHAiOjE3Mjg5NzYxNDIsInN1YiI6IntcImlkXCI6MTgzOTkzOTYwNTQxMzc1NjkyOCxcInVzZXJuYW1lXCI6XCIxMzg0NTY3ODkwMVwiLFwibmlja05hbWVcIjpcIjEzODQ1Njc4OTAxXCJ9IiwiY3JlYXRlZCI6MTcyODM3MTM0MjM5Nn0.97CuvoPXlPO28Ai5sD7cQorw-G8Byaxp8K5zhd0Sakw6zBVsacm6wl7fiI-z_ipXk45Cq1QFuGueCEup8kySGw'
                   })

driver.refresh()

time.sleep(3)