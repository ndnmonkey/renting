# -*- coding : utf-8-*-
from django.contrib import admin
from introducer.models import User, House
# Register your models here.


class UserManager(admin.ModelAdmin):
    # 展示字段
    list_display = ['username', 'password', 'is_delete', 'is_valid', 'role_type', 'user_level', 'create_time',
                    'update_time']
    # 查询字段
    search_fields = ['username']
    # 过滤字段(右侧展示)
    list_filter = ['username']
    # 分页，分页框会出现在下侧
    list_per_page = 10


class HouseManager(admin.ModelAdmin):
    # 展示字段
    list_display = ['housename', 'community', 'describe', 'univalent', 'housearea', 'address', 'floor', 'building_age',
                    'house_type', 'surrounding_facilities', 'is_delete', 'shelf_status', 'create_time', 'update_time']
    # 查询字段
    search_fields = ['housename']
    # 过滤字段(右侧展示)
    list_filter = ['housename', 'community', 'univalent', 'housearea', 'address', 'building_age', 'house_type']
    # 分页，分页框会出现在下侧
    list_per_page = 10


admin.site.register(User, UserManager)
admin.site.register(House, HouseManager)
