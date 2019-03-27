import unittest
import requests


class TestCaipu(unittest.TestCase):
    def testCai(self):
        '''测试菜谱正确'''
        url = "http://apis.juhe.cn/cook/query.php"

        par = {"key":"ba1824c0e3450f7c66b44b5e45666a0b",
                "menu":u"白菜"}

        r = requests.get(url,params=par)
        print(r.status_code)
        print(r.text)

    def test_Cai_keycuo(self):
        '''测试菜谱错误'''
        url = "http://apis.juhe.cn/cook/query.php"

        par = {"key": "ba1824ce45666a0b",
               "menu": u"白菜"}

        r = requests.get(url, params=par)
        print(r.status_code)
        print(r.text)

    if __name__ == '__main__':
        unittest.main()