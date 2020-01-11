# _*_coding:utf-8 _*_

'''
    @Function:
    @Time　　 :2020/1/10 14:54
    @Author　 :laoli0201
    @ File　　:TestNoral7and11.py
    @Software :PyCharm
'''
import time
import unittest
import HTMLTestRunner
from TestAPICase.TestPhoneNoral7 import TestPhoneNoral7
from TestAPICase.TestPhoneNoral import TestPhoneNoral11


class TestNoral7and11(unittest.TestCase):
    def testnoral7and11(self):
        # 创建测试套
        s7and11 = unittest.TestSuite()
        # 将用例添加到测试套
        caselist = [TestPhoneNoral7,TestPhoneNoral11]
        for i in caselist:
            s7and11.addTest(unittest.makeSuite(i))
        # 执行测试套
        # unittest.TextTestRunner.run(s7and11)
        # now = str(time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time())))
        now = str(time.strftime('%Y-%m-%d %X', time.localtime(time.time())))
        print(now)
        fpfile = '/Users/yenuo/Desktop/APICheckPhone03/TestAPIReporter/' + now + '.html'
        fp = open(fpfile, "wb")
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title=u'集群文件系统测试报告',
            description=u'用例执行情况：'
        )
        # 执行测试
        runner.run(s7and11)
        fp.close()


if __name__ == '__main__':
    unittest.main()