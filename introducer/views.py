# -*-coding:utf-8 -*-
# Author  : zhengyong
# Time    : 2021/10/5 18:43
# FileName: views.py


import json
import logging
import sys
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.paginator import Paginator
from django.http import request, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .Utils.registerUtils import hashUtils
from .Utils.decorators import loginRequiredCheck
from .Utils.baiduTranslate import translatorUtil
from .models import User, House, Test
from django.views.generic import ListView
from introducer.models import House

# Create your views here.


# ----------------------------------------------------
# 注册、登录、 登出
# ----------------------------------------------------
def register(request):
    """
    Getting username and password from register page, then do something about register checking.
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'introducer/introducerRegister.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        firstPassword = request.POST.get('firstpassword')
        repeatPassword = request.POST.get('repeatpassword')
        hasUsername = User.objects.filter(username=username)
        # 是否存在该用户,不存在则注册，存在则跳转登录页
        if not hasUsername:
            # 密码相同可以注册
            if firstPassword == repeatPassword:
                encriptedPassword = hashUtils.hashEncrptString(repeatPassword)
                try:
                    # registeringUser = User.objects.create(username=username, password=encriptedPassword)
                    User.objects.create(username=username, password=encriptedPassword)
                except Exception as error:
                    messages.add_message(request, messages.INFO, 'Registering, %s'%(error))

                return render(request, 'introducer/introducerLogin.html')
            else:
                messages.add_message(request, messages.INFO, 'please input the same password, then make sure they are not null.')
                return render(request, 'introducer/introducerRegister.html')
        else:
            return render(request, 'introducer/introducerLogin.html')


def login(request):
    """
    The procedure that user login in the index page.
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'introducer/introducerLogin.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        hasLoginingUser = User.objects.filter(username=username).exists()
        if hasLoginingUser:
            loginUser = User.objects.get(username=username)
            if loginUser.password == hashUtils.hashEncrptString(password):
                # 1,存储到cookie
                # reverse函数直接带视图名
                reverseObj = reverse('index')
                responseWithCookieObj = redirect(reverseObj)
                responseWithCookieObj.set_cookie(
                    key='username',
                    value=loginUser.username,
                    max_age=60 * 30,
                )
                # 2,存储到session
                if remember == 'on':
                    request.session['username'] = username
                    request.session.set_expiry(60 * 60 * 24 * 1)
                return responseWithCookieObj
            else:
                messages.add_message(request, messages.INFO, 'Password is wrong.')
                return render(request, 'introducer/introducerLogin.html')
        else:
            messages.add_message(request, messages.INFO,
                                 "Your username has not registered,please register before loginin.")
            return render(request, 'introducer/introducerRegister.html')


def logout(request):
    """
    logout from logining status, delete cookie and session.
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            loginStatus = request.session.get('username')
            if loginStatus:
                # 1，删除cookie
                reverseObj = reverse('login')
                responseWithCookieObj = redirect(reverseObj)
                responseWithCookieObj.delete_cookie('username')
                # 2，删除session
                request.session.flush()
                return responseWithCookieObj
            else:
                return render(request, 'introducer/introducerLogin.html')
        except Exception as error:
            return render(request, 'introducer/introducerLogin.html')


# ----------------------------------------------------
# 首页及页面功能（上架房源）
# ----------------------------------------------------
# index页翻页
class HouseListView(ListView):
    paginate_by = 2
    model = House


def index(request):
    """
    The main page when you login in, shows the main data.
    N represents how many pieces of data per page.
    :param request:
    :return:
    """
    if request.method == 'GET':
        datasPerPage = 9
        housees_list = House.objects.all()
        paginator = Paginator(list(housees_list), datasPerPage)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # resultOfHouses = list(contact_list)
        # print("数据--", resultOfHouses)
        # print("数据个数--", paginator.count)
        # print("page_range--", paginator.page_range)
        # print("page(1)--", paginator.page(1))

        return render(request, 'introducer/introducerIndex.html', {'page_obj': page_obj})
    elif request.method == 'POST':
        return render(request, 'introducer/introducerIndex.html', locals())


@loginRequiredCheck.check_login
def onShelfHouse(request):
    """
    Custom decorator can check the status of login in, then go to the page you want by the status.
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'introducer/onShelfHouses.html')
    elif request.method == 'POST':
        # Ajaxtest for zhengjunyong
        # translatequery = request.POST.get('translatequery')
        # print('username:', translatequery)
        # data = {
        #     'dst': translatequery,
        # }
        # return JsonResponse(data)

        try:
            House.objects.create(
                housename=request.POST.get('housename'),
                community=request.POST.get('community'),
                price=request.POST.get('price'),
                housearea=request.POST.get('housearea'),
                floor=request.POST.get('floor'),
                building_age=request.POST.get('building_age'),
                house_type=request.POST.get('house_type'),
                address=request.POST.get('address'),
                surrounding_facilities=request.POST.get('surrounding_facilities'),
                housevideo=request.FILES.get('housevideo'),
                foreigtousersubscriber=User.objects.get(username=request.session.get('username')),
            )
            # addHouseInfo.save()
            print("video", request.FILES.get('housevideo'))

        except Exception as error:
            messages.add_message(request, messages.INFO, 'onShelfHouse, %s' % (error))

        return render(request, 'introducer/onShelfHouses.html')


# @loginRequiredCheck.check_login
def houseInfomation(request, id):
    """

    :param request:
    :return:
    """
    if request.method == "GET":
        houseResult = House.objects.filter(id=id)
        return render(request, "introducer/houseInfomation.html", locals())

    elif request.method == "POST":
        pass


def recommend(request):
    """
    推荐页主页
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'introducer/introducerRecommend.html')
    elif request.method == 'POST':
        return render(request, 'introducer/introducerRecommend.html')


def infomation(request):
    if request.method == 'GET':
        return render(request, 'introducer/introducerInformation.html')
    elif request.method == 'POST':
        return render(request, 'introducer/introducerInformation.html')


# ----------------------------------------------------
# 我的页（个人功能）
# ----------------------------------------------------
@loginRequiredCheck.check_login
@csrf_exempt
def myProfile(request):
    """
    个人页的主页
    :param request:
    :return:
    """
    if request.method == 'GET':
        currentUser = request.session.get('username')
        if currentUser:
            userResult = User.objects.get(username=currentUser)
            houseResult = House.objects.filter(foreigtousersubscriber=userResult.id).order_by('-create_time')[:5]
            # print(userResult.avatar.url)
            isDefaultAvatat = 1 if ((str(userResult.avatar.url).split('.'))[-1].lower() in settings.ALLOW_AVTAR_FORMAT) else 0
        return render(request, 'introducer/myProfile.html', locals())
    # elif request.method == 'POST':
    #     pass


@loginRequiredCheck.check_login
def updateInfomation(request):
    """
    修改个人页的个人信息
    :param request:
    :return:
    """
    if request.method == 'POST':
        currentUser = request.session.get('username')
        updateUserObj = User.objects.get(username=currentUser)
        updateUserObj.username = request.POST.get('updateUsername')
        updateUserObj.telephone = request.POST.get('updateTelephone')
        updateUserObj.signature = request.POST.get('updateSignature')
        updateUserObj.save()
        userResult = User.objects.filter(username=currentUser)
        # 更新后重定向，使得修改后的值仍然在页面上。
        return redirect(myProfile)
        # return render(request, 'introducer/myProfile.html', locals())

    elif request.method == 'GET':
        currentUser = request.session.get('username')
        userResult = User.objects.filter(username=currentUser)
        return render(request, 'introducer/myProfile.html', locals())


@csrf_exempt
def uploadAvatar(request):
    """
    我的主页上传头像
    :param request:
    :return:
    """
    if request.method == 'POST':
        currentUser = request.session.get('username')
        updateUserObj = User.objects.get(username=currentUser)
        updateUserObj.avatar = request.FILES.get('img')
        print(request.FILES.get('img').name)
        updateUserObj.save()
    return redirect(myProfile)


@loginRequiredCheck.getViewfuncName
# @loginRequiredCheck.check_login
def messagesInWeb(request):
    """
    站内信，全站消息推送
    :param request:
    :return:
    """
    if request.method == 'GET':
        # a = 1/0
        return render(request, 'introducer/introducerMessages.html')
    elif request.method == 'POST':
        pass


# ----------------------------------------------------
# ajax测试
# ----------------------------------------------------
def test(request):
    if request.method == 'GET':
        return render(request, 'introducer/ajaxtest.html')
    elif request.method == 'POST':
        translate_query = request.POST.get('input1')
        input2 = request.POST.get('input2')
        print(translate_query, input2)

        fromLang = 'zh'   # 原文语种
        toLang = 'en'   # 译文语种
        query = ''
        translate_object = translatorUtil.baiduTranslate(fromLang, toLang, translate_query)
        translatedString = translate_object.translate()
        # data = {}
        # print("translatedString:", trans
        # latedString)
        # data['dst'] = translatedString,

        data = {
            'dst': str(translatedString)
        }
        print(data, type(data), data['dst'])
        return JsonResponse(data)


def index1(request):
    return render(request, "introducer/ajaxtest.html")


def ajax(request):
    if request.method == 'POST':
        num1 = request.POST.get("num1", default=1)
        num2 = request.POST.get("num12", default=5)
        print("num1:", num1)
        ret = num1 + num2
        print(ret)
        return HttpResponse(ret)

