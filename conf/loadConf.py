# coding: utf-8
# author: Holly


import os
import sys
import configparser

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)


class OperateIni(object):

    def __init__(self, file_name=None, node=None):
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = "./conf.ini"

        if node:
            self.node = node
        else:
            self.node = "First"

        self.cf = self.read_ini()

    def read_ini(self):
        cf = configparser.ConfigParser()
        cf.read(self.file_name)
        return cf

    def get_value(self, node, key):
        value = self.cf.get(node, key)
        return value


if __name__ == "__main__":
    oi = OperateIni()
    data = oi.get_value(node="Second", key='second_id')
    key = data.split(">")[0]
    value = data.split(">")[1]
    print(key, value)
    print("获取节点 %s 的 %s 参数的值为：%s" % ("Second", "second_id", oi.get_value(node="Second", key='second_id')))

