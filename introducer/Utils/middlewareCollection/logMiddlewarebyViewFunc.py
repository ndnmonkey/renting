# -*-coding:utf-8 -*-

"""
# File       : logMiddlewarebyViewFunc.py
# Time       :2021/11/19 16:34
# Author     :zhengyong
# Description:
"""

from django.utils.deprecation import MiddlewareMixin


# 需要在settings中配置自定义中间件，视图函数中的异常会被打印出来
class CustomerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # print('1，中间件process_request--')
        return None

    def process_exception(self, request, exception):
        # print('2，中间件process_exception--', exception)
        return None

    def process_view(self, request, callback, callback_args, callback_kwargs):
        # print("3，callback-", callback)  # 拿到函数
        # print("3，callback_args--", callback_args)  # 函数位置参数
        # print("3，callback_kwargs--", callback_kwargs)  # 函数关键字参数
        # ret = callback
        return None

    def process_response(self, request, response):
        # print('4，中间件process_response--', response)
        return response
