# -*-coding:utf-8 -*-
# Author  : zhengyong
# Time    : 2021/10/5 1:48
# FileName: loginRequiredCheck.py
import logging
from functools import wraps
from django.http import HttpResponseRedirect
from django.urls import reverse


# 检查是否登录
def check_login(function):
    def wrapper(request, *args, **kwargs):
        if request.session.get('username', False):
            return function(request, *args, *kwargs)
        else:
            # 获取用户当前访问的url，并传递给/user/login/
            next = request.get_full_path()
            revesedPath = reverse('login')
            print('check_login', revesedPath)
            responseRedict = HttpResponseRedirect(revesedPath + '?next=' + next)
            return responseRedict
    return wrapper


# 获取视图函数的日志
def getViewfuncName(functions):
    # @wraps(functions)
    def decration(request, *args, **kwargs):
        functionName = functions.__name__
        responseFromViewFunc = functions(request, *args, **kwargs)
        logging.log(logging.INFO, functionName)
        print(str(functionName) + '--')
        print(logging.error('logging'))
        return responseFromViewFunc
    return decration