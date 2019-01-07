#!/usr/bin/python
# coding=utf-8
from common.cryptoMethod import Encryption
from common.readExcel import *
import configparser as cparser
from common.mysqlCfg import DB
from common.txt import *
import os

proj_path = str(os.path.dirname(__file__).split('common')[0])
proj_path = proj_path.replace('\\', '/')
excel_path = proj_path + 'testFile/case/teacherCase.xlsx'
cfg_path = proj_path + '/config.ini'
cf = cparser.ConfigParser()
cf.read(cfg_path, encoding='utf-8')


def get_req_params(sheet, case):
    """
    获取请求参数
    :param sheet: sheet name
    :param case: 用例名
    :return:
    """
    req_len = 0
    param_key = row_value(excel_path, sheet, 'case_name')
    param_value = row_value(excel_path, sheet, case)
    # 获取request参数长度
    for i in range(len(param_key)):
        if param_key[i] == 'Response':
            req_len = i
            break

    params = dict()
    for key_i in range(1, req_len):
        if param_key[key_i] == 'password':
            params['password'] = Encryption().aspire_aes_crypt(param_value[key_i])
        elif param_key[key_i] in ('user_id', 'teacher_id') and param_value[key_i] == 'uid_from_tb_user':
            params[param_key[key_i]] = DB().execute_sql('select', cf.get('SQL', 'sel_tb_user'))[0][0]
        else:
            params[param_key[key_i]] = param_value[key_i]
    params['sign'] = Encryption().sign(params)
    return params


def get_resp_params(sheet, case, resp_key):
    """
    获取响应参数
    :param resp_key: 响应名
    :param sheet: sheet name
    :param case: 用例名
    :return:
    """
    resp_len = 0
    param_key = row_value(excel_path, sheet, 'case_name')
    param_value = row_value(excel_path, sheet, case)
    # 获取request参数长度
    for i in range(len(param_key)):
        if param_key[i] == 'Response':
            resp_len = i + 1
            break
    for key_i in range(resp_len, len(param_key)):
        if param_key[key_i] == resp_key:
            return param_value[key_i]


if __name__ == '__main__':

    req = get_req_params('login', 'test_login_success')
    resp_c = get_resp_params('login', 'test_login_success', 'code')
    resp_m = get_resp_params('login', 'test_login_success', 'msg')
    print(req)
    print(resp_c, resp_m)
