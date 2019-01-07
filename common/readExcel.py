#!/usr/bin/python
# coding=utf-8

import xlrd


def cell_value(fp, sheet_name, row, col):
    """
    获取单元格的值
    :param fp:
    :param sheet_name:
    :param row:
    :param col:
    :return:
    """
    test_data = xlrd.open_workbook(fp)
    sheet_name = test_data.sheet_by_name(sheet_name)
    return sheet_name.cell_value(row-1, col-1)


def row_value(fp, sheet_name, case_name):
    """
    获取整行的值
    :param fp:
    :param sheet_name:
    :param case_name:
    :return:
    """
    test_data = xlrd.open_workbook(fp, 'br')
    sheet_name = test_data.sheet_by_name('%s' % sheet_name)
    cases = sheet_name.col_values(0)
    for case_i in range(len(cases)):
        if cases[case_i] == case_name:
            return sheet_name.row_values(case_i)


def col_value(fp, sheet_name, col):
    """
    获取整列的值
    :param fp:
    :param sheet_name:
    :param col:
    :return:
    """
    test_data = xlrd.open_workbook(fp)
    sheet_name = test_data.sheet_by_name('%s' % sheet_name)
    return sheet_name.col_values(col - 1)