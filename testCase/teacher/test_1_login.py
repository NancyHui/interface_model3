#!/usr/bin/python
# coding=utf-8

from common.reqMethod import RequestMethod
from common.getParams import *
import unittest


class Login(unittest.TestCase):

    """登录接口测试"""

    def setUp(self):
        self.url = 'login'
        self.sheet = 'login'

    def tearDown(self):
        print(self.req_result)

    def test_login_success(self):
        """
        测试正常登录
        :return:
        """
        case = 'test_login_success'
        param = get_req_params(self.sheet, case)
        self.req_result = RequestMethod().post(self.url, param).json()
        self.assertEqual(self.req_result['code'], get_resp_params(self.sheet, case, 'code'))
        self.assertEqual(self.req_result['msg'], get_resp_params(self.sheet, case, 'msg'))
        self.assertEqual(self.req_result['data']['user_name'], get_resp_params(self.sheet, case, 'user_name'))

    def test_account_err(self):
        """
        手机空或者错误
        :return:
        """
        case = 'test_account_err'
        param = get_req_params(self.sheet, case)
        self.req_result = RequestMethod().post(self.url, param).json()
        self.assertEqual(self.req_result['code'], get_resp_params(self.sheet, case, 'code'))
        self.assertEqual(self.req_result['msg'], get_resp_params(self.sheet, case, 'msg'))

    def test_passwd_err(self):
        """
        密码空或者错误
        :return:
        """
        case = 'test_passwd_err'
        param = get_req_params(self.sheet, case)
        self.req_result = RequestMethod().post(self.url, param).json()
        self.assertEqual(self.req_result['code'], get_resp_params(self.sheet, case, 'code'))
        self.assertEqual(self.req_result['msg'], get_resp_params(self.sheet, case, 'msg'))

    def test_role_err(self):
        """
        角色错误或者空
        :return:
        """
        case = 'test_role_err'
        param = get_req_params(self.sheet, case)
        self.req_result = RequestMethod().post(self.url, param).json()
        self.assertEqual(self.req_result['code'], get_resp_params(self.sheet, case, 'code'))
        self.assertEqual(self.req_result['msg'], get_resp_params(self.sheet, case, 'msg'))


if __name__ == '__main__':

    Login().test_login_success()
    Login().test_account_err()
    Login().test_passwd_err()
    Login().test_role_err()
