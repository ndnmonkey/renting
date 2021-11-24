# -*- coding : utf-8-*-
from django.contrib import admin
from introducer.models import User, House
# Register your models here.


class UserManager(admin.ModelAdmin):
    # չʾ�ֶ�
    list_display = ['username', 'password', 'is_delete', 'is_valid', 'role_type', 'user_level', 'create_time',
                    'update_time']
    # ��ѯ�ֶ�
    search_fields = ['username']
    # �����ֶ�(�Ҳ�չʾ)
    list_filter = ['username']
    # ��ҳ����ҳ���������²�
    list_per_page = 10


class HouseManager(admin.ModelAdmin):
    # չʾ�ֶ�
    list_display = ['housename', 'community', 'describe', 'univalent', 'housearea', 'address', 'floor', 'building_age',
                    'house_type', 'surrounding_facilities', 'is_delete', 'shelf_status', 'create_time', 'update_time']
    # ��ѯ�ֶ�
    search_fields = ['housename']
    # �����ֶ�(�Ҳ�չʾ)
    list_filter = ['housename', 'community', 'univalent', 'housearea', 'address', 'building_age', 'house_type']
    # ��ҳ����ҳ���������²�
    list_per_page = 10


admin.site.register(User, UserManager)
admin.site.register(House, HouseManager)
