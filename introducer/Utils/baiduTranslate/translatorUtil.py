# -*-coding:utf-8 -*-
# Author  : zhengyong
# Time    : 2021/10/5 2:31
# FileName: translatorUtil.py

import hashlib
import urllib
import random
import requests


class baiduTranslate():
    __doc__ = '''It is a function can translate a kind of language to another by changing parameters,
                 fromLang represent origin language,
                 toLang represent another language that tanslated to.    
                '''

    def __init__(self, fromLang, toLang, query):
        self.appid = '20171209000103453'  # your appid.
        self.secretKey = 'qBOMWvdudHT1knAiNV1b'   # your secretKey.
        self.fromLang = fromLang
        self.toLang = toLang
        self.query = query
        self.salt = random.randint(32768, 65536)

    def getEncodedSign(self):
        '''
        parameter: None, but sign_temp contains appid,query,secretKey and random salted string.
        :return: Getting a encryped string with 32 bits lowercase letters by md5,
        '''
        self.sign_temp = self.appid + self.query + str(self.salt) + self.secretKey
        self.sign = hashlib.md5(self.sign_temp.encode()).hexdigest().lower()
        return str(self.sign)

    def getUrl(self):
        '''
        parameter: None
        :return: Getting the api url can translate a word to another language by linking with the inputed parameters,
                 besides, query need to be url-encode by function quote.
        '''
        url_temp = '?appid=' + self.appid + '&q=' + urllib.parse.quote(self.query) + '&from=' + self.fromLang + '&to=' +self.toLang + '&salt=' + str(
            self.salt) + '&sign=' + self.getEncodedSign()
        self.url = 'http://api.fanyi.baidu.com/api/trans/vip/translate' + url_temp
        return str(self.url)

    def translate(self):
        '''
        parameter: The url in function getUrl.
        :return: Getting  the translated sentence or text.
        '''
        response = requests.get(url=self.getUrl())
        translated_data = response.json()['trans_result'][0]['dst']
        return str(translated_data)


# if __name__ == '__main__':
#     fromLang = 'zh'   #原文语种
#     toLang = 'en'   #译文语种
#     query= '获取被翻译后的句子'
#     translate_object = baiduTranslate(fromLang,toLang,query)
#     translate_object.translate()
