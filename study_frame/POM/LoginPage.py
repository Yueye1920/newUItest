import time
from study_frame.driver.driver_download import Chrome_driver
from study_frame.utils.BasePage import  SeleniumHelper
from study_frame.utils.ReadYaml import YamlHander



class LoginPage:
    def login(self,driver):
        # 打开网页
        self.SeleniumHelper=SeleniumHelper(driver)
        self.SeleniumHelper.open_url("http://novel.hctestedu.com/user/login.html")
        self.SeleniumHelper.driver.maximize_window()
        # time.sleep(3)

        # 读取yaml文件
        self.YamlHander=YamlHander()
        result=self.YamlHander.read_yaml()

        # 返回的result是元组，根据索引读取
        username1 = result[0]
        password1 = result[1]
        # self.SeleniumHelper.send_element(By.ID,"txtUName",username1)
        # self.SeleniumHelper.send_element(By.ID,"txtPassword",password1)
        # self.SeleniumHelper.click_element(By.ID,"btnLogin")

        self.SeleniumHelper.id_send("txtUName",username1)
        self.SeleniumHelper.id_send("txtPassword", password1)
        self.SeleniumHelper.id_click("btnLogin")
        time.sleep(3)

if __name__ == '__main__':
    LoginPage().login(driver=Chrome_driver().chrome_base())