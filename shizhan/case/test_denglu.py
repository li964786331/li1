import unittest
import requests
from selenium import webdriver

class TestDenglu(unittest.TestCase):
    def testDeng(self):
        url = "http://localhost:8080/gouwu/login.do?method=logout"
        par = {
                  "loginName":"li_00001",
                  "loginPwd":"123"
        }
        r = requests.post(url,params=par)
        print(r.status_code)
        print(r.text)

        if __name__ == '__main__':
            unittest.main()




