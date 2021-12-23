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
from renting import settings


# 登录表单
class LoginForm(forms.Form):
    username = forms.CharField(label='账号：', strip=True, max_length=16, min_length=2, required=True,  error_messages={
            "required": "用户名必填",
            "invalid": "格式错误",
            "min_length": "用户名最短2位"
        })
    password = forms.CharField(label='密码：', strip=True, max_length=50, min_length=settings.MinlenthOfPwd,
        required=True, error_messages={
            "required": "密码必填",
            "invalid": "格式错误",
            "min_length": "用户名最短{}位".format(settings.MinlenthOfPwd)
        })
    # chekme = forms.fields.CharField(
    #     label='记住我',
    #     widget=forms.widgets.CheckboxInput
    # )
    chekme = forms.BooleanField(label='记住我：', required=False)

    # fields = ['username', 'password']


# 上架房源
class OnShelfHouseForm(forms.Form):
    housename = forms.CharField(label='房屋名称：', strip=True, max_length=50, required=True,  error_messages={
            "required": "用户名必填",
            "invalid": "格式错误",
            "max_length": "用户名最长50位"
        })
    community = forms.CharField(label='社区：', max_length=200, required=True,  error_messages={
            "required": "密码必填",
            "invalid": "格式错误",
            "max_length": "用户名最长200位"
        })
    price = forms.DecimalField(label='房租（元）/每月：', required=True)
    housearea = forms.CharField(label='面积：', required=True)
    floor = forms.CharField(label='楼层：', required=False)
    building_age = forms.CharField(label='楼龄：', required=False)
    house_type = forms.CharField(label='房屋类型：', required=False)
    address = forms.CharField(label='地址：', required=True)
    surrounding_facilities = forms.CharField(label='周边：', required=False)
    subway = forms.BooleanField(label='地铁：', required=False)
    washer = forms.BooleanField(label='洗衣机：', required=False)
    heater = forms.BooleanField(label='热水器：', required=False)
    refrigerator = forms.BooleanField(label='冰箱：', required=False)
    air_conditioner = forms.BooleanField(label='空调：', required=False)
    lift = forms.BooleanField(label='电梯：', required=False)
    kitchen_room = forms.BooleanField(label='厨房：', required=False)
    deposit = forms.BooleanField(label='押金：', required=False)
    house_origin_type = forms.ChoiceField(label='房源类型：', required=True, initial='transfer', choices=(
        ('direct', '直租'),
        ('transfer', '转租'),
        ('mediator', '中介'),
        ('others', '其他'),
    ))
    rent_type = forms.ChoiceField(label='出租类型：', required=True, choices=(
        ('share', '合租'),
        ('full', '整租'),
    ))
    housevideo = forms.FileField(label='videos:', allow_empty_file=True, required=False)
    # fields = ['username', 'password']


