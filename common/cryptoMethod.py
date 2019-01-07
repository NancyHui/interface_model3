#!/usr/bin/python
# coding=utf-8


from Crypto.Cipher import AES
import hmac
import base64
import hashlib
import time


class Encryption:

    def __init__(self):
        # 密码加密参数：key:秘钥、iv:偏移
        self.aes_key = '...*...'
        self.aes_iv = '...*...'
        # 接口公共参数
        self.params = dict()
        self.params['app_key'] = '...*...'
        self.params['version'] = '...*...'
        self.params['time'] = time.time()

    def aspire_aes_crypt(self, passwd):
        """
        用户密码加密算法（key，iv，passwd输入均应为bytes类型）
        :param passwd: 密码
        :return: 返回base64加密后的password
        """
        key = self.aes_key
        iv = self.aes_iv
        BS = AES.block_size
        pad = (lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS))
        aes = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
        return base64.b64encode(aes.encrypt(pad(passwd).encode('utf-8'))).decode('utf-8')

    def sign(self, params):
        """
        计算签名
        :return:
        """
        lst = []
        for x in sorted(params.keys()):
            lst.append('%s=%s' % (x, params[x]))
        s = '&'.join(lst)
        key = '...*...'
        return base64.b64encode(hmac.new(key.encode('utf-8'), s.encode('utf-8'), hashlib.sha1).digest())


if __name__ == '__main__':

    pwd = '...*...'
    pwd_crypt = Encryption().aspire_aes_crypt(pwd)
    print(pwd_crypt)
