#!/usr/bin/python
# coding=utf-8

from pymysql import connect
from pymysql.err import OperationalError
import os
import configparser as cparser

# ------------------读取配置文件及数据库配置----------------------
base_path = str(os.path.dirname(os.path.dirname(__file__)))
base_path = base_path.replace('\\', '/')
cfg_path = base_path + '/config.ini'
cf = cparser.ConfigParser()
cf.read(cfg_path, encoding='utf-8')
host = cf.get('MYSQL', 'host')
port = cf.get('MYSQL', 'port')
user = cf.get('MYSQL', 'user')
password = cf.get('MYSQL', 'password')
db_name = cf.get('MYSQL', 'db_name')
charset = cf.get('MYSQL', 'charset')

# -----------封装MySQL数据库基本操作-----------------


class DB:

    def __init__(self):

        try:
            # 连接数据库
            self.conn = connect(
                host=host,
                port=int(port),
                user=user,
                password=password,
                db=db_name,
                charset=charset
            )
        except OperationalError as e:
            print('MySQL error %d: %s' % (e.args[0], e.args[1]))
        else:
            self.cursor = self.conn.cursor()

    def execute_sql(self, command, sql):
        """
        插入表数据
        :param command:
        :param sql:
        :return:
        """
        if command in ('SELECT', 'select'):
            # 如果为查询指令
            sql = sql.encode('utf-8')
            try:
                self.cursor.execute(sql)
                result = self.cursor.fetchall()
                return result
            except Exception as e:
                print(e)
            finally:
                self.conn.close()
        elif command in ('delete', 'DELETE', 'update', 'UPDATE', 'insert', 'INSERT'):
            # 如果为增删改
            sql = sql.encode('utf-8')
            try:
                self.cursor.execute(sql)
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
            finally:
                self.conn.close()
        else:
            print('Command Error!')


if __name__ == '__main__':

    # sel_sql = cf.get('SQL', 'SELECT')
    # s = DB().execute_sql('select', sel_sql)
    print(DB().execute_sql('select', cf.get('SQL', 'SELECT'))[0][0])
