from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from study_frame.driver.driver_download import Chrome_driver

class Locator:
    def __init__(self):
        """
        初始化 Locator 类，接收一个 WebDriver 实例。

        :param driver: WebDriver 实例，用于操作浏览器。
        """
        driver = Chrome_driver().chrome_base()
        self.driver = driver


    def find_element(self, by, value, timeout=10):
        """
        查找单个元素，支持显式等待。

        :param by: 定位方式，如 By.ID, By.CSS_SELECTOR 等。
        :param value: 定位的值。
        :param timeout: 最大等待时间，默认为 10 秒。
        :return: 找到的元素，如果未找到则返回 None。
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except Exception as e:
            print(f"元素查找失败: {e}")
            return None

    def find_elements(self, by, value, timeout=10):
        """
        查找多个元素，支持显式等待。

        :param by: 定位方式，如 By.ID, By.CSS_SELECTOR 等。
        :param value: 定位的值。
        :param timeout: 最大等待时间，默认为 10 秒。
        :return: 找到的元素列表，如果未找到则返回空列表。
        """
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((by, value))
            )
            return elements
        except Exception as e:
            print(f"元素查找失败: {e}")
            return []

    def id(self, value, timeout=10):
        """
        通过 ID 定位单个元素。

        :param value: 元素的 ID 值。
        :param timeout: 最大等待时间，默认为 10 秒。
        :return: 找到的元素，如果未找到则返回 None。
        """
        return self.find_element(By.ID, value, timeout)

    def class_name(self, value, timeout=10):
        """
        通过类名定位单个元素。

        :param value: 元素的类名。
        :param timeout: 最大等待时间，默认为 10 秒。
        :return: 找到的元素，如果未找到则返回 None。
        """
        return self.find_element(By.CLASS_NAME, value, timeout)

    def css_selector(self, value, timeout=10):
        """
        通过 CSS 选择器定位单个元素。

        :param value: CSS 选择器的值。
        :param timeout: 最大等待时间，默认为 10 秒。
        :return: 找到的元素，如果未找到则返回 None。
        """
        return self.find_element(By.CSS_SELECTOR, value, timeout)

    def xpath(self, value, timeout=10):
        """
        通过 XPath 定位单个元素。

        :param value: XPath 表达式。
        :param timeout: 最大等待时间，默认为 10 秒。
        :return: 找到的元素，如果未找到则返回 None。
        """
        return self.find_element(By.XPATH, value, timeout)

    def link_text(self, value, timeout=10):
        """
        通过链接文本定位单个元素。

        :param value: 链接的文本内容。
        :param timeout: 最大等待时间，默认为 10 秒。
        :return: 找到的元素，如果未找到则返回 None。
        """
        return self.find_element(By.LINK_TEXT, value, timeout)

    def partial_link_text(self, value, timeout=10):
        """
        通过部分链接文本定位单个元素。

        :param value: 部分链接的文本内容。
        :param timeout: 最大等待时间，默认为 10 秒。
        :return: 找到的元素，如果未找到则返回 None。
        """
        return self.find_element(By.PARTIAL_LINK_TEXT, value, timeout)

    def name(self, value, timeout=10):
        """
        通过元素的 name 属性定位单个元素。

        :param value: 元素的 name 属性值。
        :param timeout: 最大等待时间，默认为 10 秒。
        :return: 找到的元素，如果未找到则返回 None。
        """
        return self.find_element(By.NAME, value, timeout)

    def tag_name(self, value, timeout=10):
        """
        通过标签名定位单个元素。

        :param value: 元素的标签名。
        :param timeout: 最大等待时间，默认为 10 秒。
        :return: 找到的元素，如果未找到则返回 None。
        """
        return self.find_element(By.TAG_NAME, value, timeout)
