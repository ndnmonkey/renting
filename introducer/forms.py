# -*-coding:utf-8 -*-

"""
# File       : forms.py
# Time       :2021/12/14 21:15
# Author     :zhengyong
# Description:
"""
from django import forms
from django.forms import fields, widgets
from . import models


# 登录表单
class LoginForm(forms.Form):
    username = forms.CharField(label='登录：', max_length=16, min_length=2, required=True,  error_messages={
            "required": "用户名必填",
            "invalid": "格式错误",
            "min_length": "用户名最短2位"
        })
    password = forms.CharField(label='密码：', max_length=50, min_length=1, required=True,  error_messages={
            "required": "密码必填",
            "invalid": "格式错误",
            "min_length": "用户名最短1位"
        })
    chekme = forms.fields.CharField(
        label='记住我',
        widget=forms.widgets.CheckboxInput
    )
    # fields = ['username', 'password']


