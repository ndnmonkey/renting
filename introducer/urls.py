# -*-coding:utf-8 -*-
# Author  : zhengyong
# Time    : 2021/10/3 10:48
# FileName: urls.py
import django.contrib.auth.views
from django.urls import path
from . import views


urlpatterns = [
    path('register', views.register, name='register'),
    path('loginold', views.login, name='login'),
    path('login', views.loginByForm, name='loginnew'),

    path('my/myprofile', views.myProfile, name='myprofile'),
    path('my/updateInfomation', views.updateInfomation, name='updateInfomation'),
    path('my/logout', views.logout, name='logout'),
    path('my/order', views.myOrder, name='order'),
    path('my/myhouse', views.myHouse, name='myHouse'),
    path('my/transferhousestatus/<houseID>', views.transferHouseStatus, name='transferhousestatus'),
    path('my/uploadavatar', views.uploadAvatar, name='uploadavatar'),

    path('onshelfhouse', views.onShelfHouse, name='onshelfhouse'),
    path('house/onshelfhouse', views.newonShelfHouse, name='newonshelfhouse'),

    path('houseinfomation/<houseID>', views.houseInfomation, name='houseinfomation'),
    path('addtohouseorder/<houseID>', views.addToHouseOrder, name='addtohouseorder'),

    path('index', views.index, name='index'),
    path('test', views.test, name='test'),
    path('index1', views.index1, name='index1'),
    path('ajax', views.ajax, name='ajax'),


    path('recommend', views.recommend, name='recommend'),
    path('infomation', views.infomation, name='infomation'),
    path('messages', views.messagesInWeb, name='messages'),


]