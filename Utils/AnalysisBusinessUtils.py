# _*_coding:utf-8 _*_

'''
    @Function:
    @Time　　 :2020/1/9 8:41
    @Author　 :laoli0201
    @ File　　:AnalysisBusinessUtils.py
    @Software :PyCharm
'''
from Utils.Get_Response import Get_Response
from Utils.Get_Response import Analysis_Response


class AnalysisBusinessUtils:
    def analysisbusinessutils(self, url, par, method='get'):
        __response = Get_Response(url,par).get_response
        __responseJson = Analysis_Response(__response).dicresponse
        return __responseJson

    # 验证'reason':
    def assertreason(self,url, par, _expValue):
        _actValue = self.analysisbusinessutils(url, par, method='get')
        assert _expValue == _actValue['reason'], "验证reason\"Return Successd!\"Error"

    # 验证.error_code
    def asserterror_code(self,url, par, _expValue):
        _actValue = self.analysisbusinessutils(url, par)
        assert _expValue == _actValue['error_code'], "验证error_code ,0 Error"

    # 验证.province：
    def assertprovince(self):
        pass

    # 验证resultcode
    def assertresultcode(self,url, par, key,_expValue):
        _actValue = self.analysisbusinessutils(url, par)
        assert _expValue == _actValue[key], "验证resultcode ,0 Error"