# coding=utf-8
import logging
import os
import datetime


class UserLog(object):
    def __init__(self):
        self.logger = logging.getLogger()
        # self.logger.setLevel(logging.DEBUG)
        self.logger.setLevel(logging.INFO)
        # log流
        # consle = logging.StreamHandler()

        dir_name = os.path.dirname(os.path.abspath(__file__))
        dir_path = os.path.join(dir_name, 'logs')
        file_name = datetime.datetime.now().strftime('%Y-%m-%d')+'.log'
        file_path = dir_path + '/' + file_name

        # log文件
        self.file_handle = logging.FileHandler(file_path)
        # 格式化文件内容
        formatter = logging.Formatter('%(asctime)s---->%(filename)s %(funcName)s %(levelno)s:%(levelname)s---->%(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)

    def get_log(self):
        return self.logger

    def close_log(self):
        # 关闭文件流
        self.file_handle.close()
        # 关闭logger
        self.logger.removeHandler(self.file_handle)

