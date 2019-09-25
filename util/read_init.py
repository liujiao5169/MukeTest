# coding=utf-8

import configparser


class ReadInit(object):

    def __init__(self, file_name=None, node=None):
        if file_name == None:
            file_name ="C:\\Users\\TSDLJ\\PycharmProjects\\UITest_muke\\config\\Locate_element.ini"
        else:
            self.file_name = file_name
        self.cf = self.load_init(file_name)
        if node == None:
            self.node = "RegisterConfig"
        else:
            self.node = node

    def load_init(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    def get_value(self, key):
        data = self.cf.get(self.node, key)
        return data


