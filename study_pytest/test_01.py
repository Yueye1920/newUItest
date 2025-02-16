import pytest
from selenium import webdriver
import time

def test_case01():
    driver = webdriver.Chrome()
    driver.get("http://120.25.127.201:18001/")
    time.sleep(1)
    assert 1==1


def test_case02():
    driver = webdriver.Chrome()
    driver.get("http://baidu.com")
    time.sleep(1)
    assert 1 == 2

def test_aaa_03():
    assert 1==3


if __name__ == '__main__':
    # pytest.main(['v','test_01.py'])
    # pytest.main(['s','test_01.py'])
    # pytest.main(['-v','-s','test_01.py'])
    pytest.main(['vs','-k','aaa','test_01.py'])
# -s 输出打印信息到控制台
# -v 详细输出
# -k 运行名称中包含字符串的测试用例
# -n 将测试执行发送给多个CPU