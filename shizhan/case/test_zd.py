import unittest
import requests
from selenium import webdriver

class TestZd(unittest.TestCase):
    def testZd(self):
        d = webdriver.Firefox(executable_path="D:\\geckodriver")
        d.get("http://localhost:8080/gouwu/login.do?method=logout")
        d.find_element_by_name("btn").click()
        d.find_element_by_xpath("html/body/table/tbody/tr[3]/td[2]/form/table/tbody/tr[2]/td[2]/select/option[3]").click()
        d.find_element_by_name("memberName").send_keys("li005")
        d.find_element_by_name("loginName").send_keys("li005")
        d.find_element_by_name("loginPwd").send_keys("123")
        d.find_element_by_xpath(".//*[@id='reLoginPwd']").send_keys("123")
        d.find_element_by_name("phone").send_keys("13012345678")
        d.find_element_by_name("address").send_keys(u"北京通州")
        d.find_element_by_name("zip").send_keys("123456")
        d.find_element_by_name("email").send_keys("123@qq.com")
        d.find_element_by_class_name("C_Input").click()

        d.find_element_by_class_name("whiteTitle").click()
        d.find_element_by_name("loginName").send_keys("li005")
        d.find_element_by_name("loginPwd").send_keys("123")
        d.find_element_by_xpath("html/body/table/tbody/tr[3]/td[2]/table/tbody/tr/td[1]/table[1]/tbody/tr[2]/td/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td/input[2]").click()


    if __name__=='__main__':
        unittest.main()