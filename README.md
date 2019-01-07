# InterfaceTest

#### 项目介绍
接口测试框架

#### 软件架构
Python3.6 + requests + unittest

#### 脚本结构

1. common：通用模块/方法
2. testCase：测试用例
3. testFile：测试数据/图片
4. testResult：测试报告
5. config.ini：配置文件
6. runAll.py：主程序

#### 更新日志
- **zhtyInterfaceTestPublic V1.0**
- **Date：2018.09.10**
- **Function & Modifies：**
1. 接口测试框架
2. 测试用例包括：登陆接口 ...*...
3. 接口测试前通过数据库初始化测试数据，完成后删除数据库数据

#### 涉及到的第三方库
1. 接口加密方法*AES*，安装方法请参考[Python3常用加密方法使用总结](https://www.jianshu.com/p/bdadf8607a3b)
2. 读取Excel，*xlrd* - `pip install xlrd`
3. 连接MySQL，*PyMySQL* - `pip install PyMySQL`
