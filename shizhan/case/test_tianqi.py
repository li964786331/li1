import unittest
import requests
from selenium import webdriver

class TestTianqi(unittest.TestCase):
    def testTianqi(self):
        url = "http://v.juhe.cn/weather/index"
        par = {
                     "format" : "2",
                       "cityname" : "北京",
                                    "key" : "cd6683503a32b475ed36e8d31a628973"
        }
        r = requests.post(url,params=par)
        print(r.status_code)
        print(r.text)

    if __name__ == '__main__':
        unittest.main()