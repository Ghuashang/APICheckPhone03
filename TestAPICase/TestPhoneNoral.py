# _*_coding:utf-8 _*_

'''
    @Function:手机号为11位+86移动运营商，其他参数正确
    @Time　　:2020/1/6   14:36
    @Author　 : laoli0201
    @ File　　  :TestPhoneNoral.py
    @Software  :PyCharm
'''

import unittest
from Utils.Get_Response import Get_Response


class TestPhoneNoral11(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        _url = "http://apis.juhe.cn/mobile/get"
        _par={
            "phone":"15238072751",
            "key":"e225109493b04738eafb0d3019d63ec1",
            "dtype":"json"
        }
        cls.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
        }
        # 获取返回值
        cls._response = Get_Response(url=_url, par=_par, header=cls.header, method='get').get_response
        # 获取返回值转换Json格式
        cls._responseJson = cls._response.json()

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    # 手机号为11位+86移动运营商，其他参数正确
    def testNoral01(self):
        # 验证http协议状态码为200
        _expValue = 200
        _actValue = self._response.status_code
        self.assertEqual(_expValue, _actValue, msg= "验证http协议状态码Error")

    def testNoral02(self):
        # 验证resultcode:"200"
        _expValue = "200"
        _actValue = str(self._responseJson['resultcode'])
        self.assertEqual(_expValue, _actValue, msg= "验证resultcode为\"200\"Error")

    def testNoral03(self):
        # 验证'reason': 'Return Successd!',
        _expValue = "Return Successd!"
        _actValue = self._responseJson['reason']
        self.assertEqual(_expValue, _actValue, msg= "验证reason\"Return Successd!\"Error")

    def testNoral04(self):
        # 验证.error_code：0,
        _expValue = 0
        _actValue = self._responseJson['error_code']
        self.assertEqual(_expValue, _actValue, msg= "验证error_code：0,Error")

    def testNoral05(self):
        # 验证.province：河南,
        _expValue = "河南"
        _actValue = self._responseJson['result']['province']
        self.assertEqual(_expValue, _actValue, msg="验证province：河南,Error")


if __name__ == '__main__':
    unittest.main()
