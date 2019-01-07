#!/usr/bin/python
# coding=utf-8

from HTMLTestRunner import HTMLTestRunner
import configparser as cparser
from common.mysqlCfg import DB
import unittest
import time
import os


discover = unittest.defaultTestLoader.discover('./testCase/teacher', pattern='test*.py')


if __name__ == '__main__':

    # ------------------读取配置文件----------------------
    base_path = str(os.path.dirname(__file__))
    base_path = base_path.replace('\\', '/')
    cfg_path = base_path + '/config.ini'
    cf = cparser.ConfigParser()
    cf.read(cfg_path, encoding='utf-8')

    # 初始化测试数据
    ins_tb_user = cf.get('SQL', 'ins_tb_user')
    # 执行SQL
    DB().execute_sql('insert', ins_tb_user)

    now = time.strftime('%Y-%m-%d %H_%M_%S')  # 获取当前时间
    filename = now + ' testReport.html'
    fp = open('./testResult/{0}'.format(filename), 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='智慧体育教师版接口测试报告',
                            description='用例执行情况：')
    runner.run(discover)
    fp.close()

    # 删除数据
    del_tb_user = cf.get('SQL', 'del_tb_user')
    DB().execute_sql('delete', del_tb_user)
