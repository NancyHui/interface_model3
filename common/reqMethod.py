#!/usr/bin/python
# coding=utf-8

import configparser as cparser
import requests
import os

# ------------------读取配置文件----------------------
base_path = str(os.path.dirname(os.path.dirname(__file__)))
base_path = base_path.replace('\\', '/')
cfg_path = base_path + '/config.ini'
cf = cparser.ConfigParser()
cf.read(cfg_path, encoding='utf-8')


class RequestMethod:
    """ 定义请求类型 """

    def __init__(self):

        """初始化参数"""
        self.base_url = cf.get('URL', 'base_url')
        self.data = {}
        self.files = {}

    def get(self, url, params):
        """
        定义get方法请求
        :return:
        """
        test_url = self.base_url + url
        try:
            return requests.get(url=test_url, params=params, timeout=60)
        except TimeoutError:
            return print('%s get request timeout!' % url)

    def post(self, url, params):
        """
        定义post方法请求
        :return:
        """
        test_url = self.base_url + url
        try:
            return requests.post(url=test_url, data=params, timeout=60)
        except TimeoutError:
            return print('%s post request timeout!' % url)

    def post_with_file(self, url, params, fp):
        """
        定义post方法请求
        :return:
        """
        test_url = self.base_url + url
        file = {
            'head_img': open(fp, 'rb')
        }
        try:
            return requests.post(url=test_url, data=params, files=file, timeout=60)
        except TimeoutError:
            return print('%s post request timeout!' % url)