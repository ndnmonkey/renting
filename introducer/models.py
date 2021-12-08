# -*-coding:utf-8 -*-

"""
# File       : models.py
# Time       :2021/11/8 21:09
# Author     :author name
# Description:
"""

import json
from decimal import Decimal
from django.db import models

# Create your models here.


# 兼职中介，可以上架房源，也可
class User(models.Model):
    """用户信息表"""
    username = models.CharField('username', max_length=30, unique=True)
    # email = models.EmailField('email', default='renting@rent.com')
    password = models.CharField('password', max_length=32)
    telephone = models.IntegerField('telephone', default='0000')
    is_delete = models.BooleanField('if deleted', default=False)
    is_valid = models.BooleanField('if valid', default=True)
    role_type = models.IntegerField('role type', default=1)
    user_level = models.IntegerField('user level', default=1)
    signature = models.CharField('personal signature', max_length=200, default='This is my personal signature in a word!')
    create_time = models.DateTimeField('created time', auto_now_add=True)
    update_time = models.DateTimeField('updated time', auto_now=True)
    avatar = models.ImageField(upload_to='media/introducer/profile/', default='media/introducer/profile/default.jpg')

    def __str__(self):
        return json.dumps({
            'username': self.username,
            'password': self.password,
            'telephone': self.telephone,
            'is_delete': self.is_delete,
            'is_valid': self.is_valid,
            'role_type': self.role_type,
            'user_level': self.user_level,
            'signature': self.signature,
            'create_time': str(self.create_time),
            'update_time': str(self.update_time),
            # 'avatar': self.avatar,
        })


class House(models.Model):
    """房屋信息表"""
    housename = models.CharField('house name', max_length=50, default='House name.')
    community = models.CharField('community', max_length=200, default='The community where the house is located.')
    describe = models.CharField('describe', max_length=500, default='Describe about the house.')
    price = models.DecimalField('price', max_digits=15, decimal_places=2)

    housearea = models.CharField('housearea', max_length=50, default='The size of the house.')
    address = models.CharField('address', max_length=50, default='Where is the house.')
    floor = models.CharField('floor', max_length=50, default='How many floors is the house on.')
    building_age = models.CharField('building_age', max_length=5, default='The age of the house.')
    house_type = models.CharField('house_type', max_length=5, default='The type of house.')
    surrounding_facilities = models.CharField('surrounding_facilities', max_length=500, default='Facilities around the house.')
    is_delete = models.BooleanField('if deleted', default=False)
    shelf_status = models.BooleanField('shelf_status', default=True)
    create_time = models.DateTimeField('created time', auto_now_add=True)
    update_time = models.DateTimeField('updated time', auto_now=True)
    housevideo = models.ImageField(upload_to='media/introducer/housevideos/', default='media/introducer/housevideos/')

    # 外键，发布者
    foreigtousersubscriber = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    '''
    租住类型：合租、整租
    入住时间
    '''
    # 新增字段
    subway = models.BooleanField('subway', default=False)
    washer = models.BooleanField('washer', default=False)
    heater = models.BooleanField('heater', default=False)
    refrigerator = models.BooleanField('refrigerator', default=False)
    air_conditioner = models.BooleanField('air_conditioner', default=False)
    lift = models.BooleanField('lift', default=False)
    kitchen_room = models.BooleanField('kitchen_room', default=False)
    deposit = models.BooleanField('deposit', default=False)
    house_origin_type = models.CharField('rent type', max_length=20, default='', choices=[
                                                            ('di', 'direct'),
                                                            ('tr', 'transfer'),
                                                            ('me', 'mediator'),
                                                            ('ot', 'others'),
                                                        ])
    rent_type = models.CharField('rent type', max_length=20, default='', choices=[
                                                            ('sh', 'share'),
                                                            ('fu', 'full'),
                                                        ])

    def __str__(self):
        return json.dumps({
            'housename': self.housename,
            'community': self.community,
            'describe': self.describe,
            'price': str(self.price),
            'housearea': self.housearea,
            'address': self.address,
            'floor': self.floor,
            'building_age': self.building_age,
            'house_type': self.house_type,
            'surrounding_facilities': self.surrounding_facilities,
            'is_delete': self.is_delete,
            'shelf_status': self.shelf_status,
            'create_time': str(self.create_time),
            'update_time': str(self.update_time),
            'foreigtousersubscriber': self.foreigtousersubscriber,
        })


class Test(models.Model):
    community = models.CharField('community', max_length=200, default='Nothing to fill in about the house.')


class IMG(models.Model):
    img = models.ImageField(upload_to='media/introducer/profile', default='media/introducer/profile')
    name = models.CharField(max_length=20)
