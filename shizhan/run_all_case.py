import unittest
from shizhan.common.HtmlRunner import HTMLTestRunner    #自行封装并引用

# sdir:是用例存放的路径  由外到里编写
# rule：匹配规则“test*.py”指的是匹配所有以test开头的py文件

sdir = r'D:\Users\libing\PycharmProjects\untitled1\shizhan\case'   #这行为我程序的目录
rule = "test*.py"                         #这行为指引用所有的case中的文件

discover = unittest.defaultTestLoader.discover(sdir,rule)
print(discover)

#生成高级报告
fp = open("result.html","wb")
runer = HTMLTestRunner(fp,title="大哥大哥，别打我",
                        description="报告如下")
runer.run(discover)
fp.close()
