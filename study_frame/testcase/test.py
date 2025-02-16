import pytest
from selenium.webdriver.common.by import By
from study_frame.POM.LoginPage import LoginPage
from study_frame.utils.BasePage import  SeleniumHelper
from study_frame.driver.driver_download import Chrome_driver

import time

# 生成唯一driver对象
driver = Chrome_driver().chrome_base()


# pytest类Tset开头命名
# pytest方法test开头命名
class Testcase:



    def test_login(self):
        LoginPage().login(driver)

    def test_serch(self):
        # SeleniumHelper(driver).send_element(By.ID,"searchKey","111")
        # SeleniumHelper(driver).click_element(By.ID,"btnSearch")

        SeleniumHelper(driver).id_send("searchKey","111")
        SeleniumHelper(driver).id_click("btnSearch")
        time.sleep(3)


if __name__ == "__main__":
    pytest.main()