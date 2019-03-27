import unittest
import requests
from selenium import webdriver
import time



class TestBaidu(unittest.TestCase):
    def setUp(self):
        self.d = webdriver.Firefox(executable_path="d:\\geckodriver.exe")
        self.d.get("https://www.baidu.com")
        print("开始")

    def tearDown(self):
        print("结束")


    def test_GUI(self):
        self.d.find_element_by_id("kw").send_keys("今日新鲜事")
        self.d.find_element_by_xpath("html/body/div/div[3]/div[1]/div[1]/table/tbody/tr/td/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/a[2]").click()
    if __name__=='__main__':
        unittest.main()



