#!/usr/bin/python
# coding=utf-8

import os

base_path = str(os.path.dirname(os.path.dirname(__file__)))
base_path = base_path.replace('\\', '/')
txt_path = base_path + '/testFile/user_id.txt'


def write_txt(params):

    fo = open(txt_path, 'w')
    fo.write(params)
    fo.close()


def read_uid():
    if os.path.exists(txt_path):
        fo = open(txt_path, 'r')
        return fo.readline().split(':')[1]
    else:
        print('The txt file is not exists!')

