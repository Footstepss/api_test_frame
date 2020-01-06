#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, time, logging
from base_data import *

class log_message():
    '''
    参考：百度搜索 'python logger模块' http://www.cnblogs.com/i-honey/p/8052579.html
    '''

    def __init__(self, class_name):
        '''

        :param class_name: 实例化时传入 函数简介
        '''
        self.class_name = class_name
        day = time.strftime("%Y-%m-%d_%H", time.localtime(time.time()))
        file_dir = root_path + '/logs'
        file = os.path.join(file_dir, (day + '.log'))
        self.logger = logging.Logger(self.class_name)
        self.logger.setLevel(logging.INFO)
        self.logfile = logging.FileHandler(file, encoding='utf-8')
        self.logfile.setLevel(logging.INFO)
        self.control = logging.StreamHandler()
        self.control.setLevel(logging.INFO)
        self.formater = logging.Formatter(
            '[%(asctime)s] - %(filename)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s')
        self.logfile.setFormatter(self.formater)
        self.control.setFormatter(self.formater)
        self.logger.addHandler(self.logfile)
        self.logger.addHandler(self.control)