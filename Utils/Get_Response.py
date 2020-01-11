# _*_coding:utf-8 _*_

'''
    @Function:
    @Time　　:2020/1/8   10:02
    @Author　 : laoli0201
    @ File　　  :Get_Response.py
    @Software  :PyCharm
'''
import requests


class Get_Response:
    def __init__(self, url, par=None, header=None, method='get'):
        self.url = url
        self.par = par
        self.header = header
        self.method = method

    # 发送request
    @property
    def get_response(self):
        if self.method.lower() == "get":
            __reSponse = requests.get(self.url, params=self.par,headers=self.header)
            return __reSponse
        elif self.method.lower() == "post":
            __reSponse = requests.post(url=self.url, data=self.par)
            return __reSponse
        else:
            return False


# 解析协议层的response
class Analysis_Response:
    def __init__(self, response):
        self._response=response

    # 获取http协议状态码
    @property
    def get_status_code(self):
        __get_status_code = self._response.status_code
        return __get_status_code

    # 将response转换成DIC
    @property
    def dicresponse(self):
        __dicresponse = self._response.json()
        return __dicresponse

    # 获取cookie
    def get_cookie(self):
        self._response.cookies

    # 获取头信息
    def get_header(self):
        self._response.header

    # 获取url
    def get_url(self):
        self._response.url

