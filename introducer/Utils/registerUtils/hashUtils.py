# -*-coding:utf-8 -*-
# Author  : zhengyong
# Time    : 2021/10/3 11:07
# FileName: hashUtils.py


import hashlib


def hashEncrptString(string):
    '''
    :param string: the string need to be encpripted.
    :return: encpripted string.
    '''
    hashObj = hashlib.md5()
    hashObj.update(str(string).encode())
    hashstring = hashObj.hexdigest()
    return hashstring

