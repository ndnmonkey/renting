# -*-coding:utf-8 -*-

"""
# File       : forms.py
# Time       :2021/12/14 21:15
# Author     :zhengyong
# Description:
"""
from django import forms
from . import models
from . import models


class LoginTestForm(forms.Form):
    username = forms.CharField(label='username', max_length=10, min_length=2,  error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "用户名最短8位"
        })
    password = forms.CharField(label='password')
    fields = ['username', 'password']



