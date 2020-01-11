# _*_coding:utf-8 _*_

'''
    @Function:手机号为11位+86移动运营商，其他参数正确
    @Time　　:2020/1/6   14:36
    @Author　 : laoli0201
    @ File　　  :TestPhoneNoral.py
    @Software  :PyCharm
'''

import unittest
from Utils.Get_Response import *
from Utils.AnalysisBusinessUtils import AnalysisBusinessUtils


class TestPhoneNoral7(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._url = "http://apis.juhe.cn/mobile/get"
        cls._par={
            "phone":"1523807",
            "key":"e225109493b04738eafb0d3019d63ec1",
            "dtype":"json"
        }
        cls.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
        }

        cls.P = AnalysisBusinessUtils()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    # 手机号为11位+86移动运营商，其他参数正确
    @unittest.skip("暂时不执行")
    def testNoral01(self):
        # 验证http协议状态码为200
        _expValue = 200

        self.assertEqual(_expValue, _actValue, msg= "验证http协议状态码Error")

    def testNoral02(self):
        # 验证resultcode:"200"
        key = "resultcode"
        _expValue = "200"
        self.P.assertresultcode(self._url, self._par, key,_expValue)

    def testNoral03(self):
        # 验证'reason': 'Return Successd!',
        _expValue = "Return Successd!"
        self.P.assertreason(self._url, self._par, _expValue)

    def testNoral04(self):
        # 验证.error_code：0,
        _expValue = 0
        self.P.asserterror_code(self._url, self._par,  _expValue)


if __name__ == '__main__':
    unittest.main()
