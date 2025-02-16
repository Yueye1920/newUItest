import pytest
from selenium.webdriver.common.by import By

from study_frame.POM.LoginPage import LoginPage
from study_frame.utils.BasePage import  SeleniumHelper
from study_frame.driver.driver_download import Chrome_driver

import time

# pytest类Tset开头命名
# pytest方法test开头命名
class Testcase:

    # def __init__(self):
    #     driver = Chrome_driver().chrome_base()
    #     self.driver = driver

    def test_login(self):
        LoginPage().login()

    # def test_serch(self,driver):
    #     SeleniumHelper().send_element(By.ID,"searchKey","111")
    #     time.sleep(3)


if __name__ == "__main__":
    pytest.main()