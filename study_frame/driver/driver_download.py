#1.打开浏览器
#打开浏览器需要对应浏览器和对应版本的驱动
#让代码根据浏览器需求自动下载驱动
from selenium import webdriver
from selenium.webdriver.firefox.service import service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# 下载谷歌驱动
class Chrome_driver(object):
    def chrome_init(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # 自动下载对应的驱动
        return driver
    def chrome_base(self):
        # 指定驱动路径
        service=ChromeService(executable_path=r'D:\dome\newuitest\study_frame\driver\chromedriver.exe')
        driver=webdriver.Chrome(service=service)
        return driver

# 下载火狐驱动
class Firefox_driver(object):
    def browser_init(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        return driver

# 下载Edge驱动
class Edge_driver(object):
    def browser_init(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        return driver
#2.让浏览器打开页面
#3.操作页面元素
