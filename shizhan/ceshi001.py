import unittest
from selenium import webdriver
import requests
import time


class TestMethod(unittest.TestCase):

    def setUp(self):
        self.d = webdriver.Firefox(executable_path="d:\\geckodriver.exe")
        self.d.get("https://www.baidu.com")
        print("开始")


    def tearDown(self):
        print("结束")
       # self.d.close()

    def test_GUI(self):
       shuchu = self.d.find_element_by_id("kw").send_keys("123")
       time.sleep(3)
       shuchu1 = self.d.find_element_by_class_name("toindex")
       text = shuchu1.text
       print(text)
       self.assertEqual(text, "百度首页", msg="结果错了")


if __name__=='__main__':
    unittest.main()