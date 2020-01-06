#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from utils.enum_class import EnumResult
from functools import wraps
from utils.logs import log_message

def getSubstrNum(str1,str2):
    '''字符串中含有某子字符串的个数'''
    return (len(str1) - len(str1.replace(str2,""))) // len(str2)

def get_api_para_template_path():
    func_path = os.path.dirname(__file__)
    start = func_path.find('my_api_test_frame')
    return str(func_path[0:start+17]+'/api_para_template')

#依赖装饰器
def dependence_decoration(dependence):
    def decorator(func):
        def wrapper(self,*args,**kwargs):
            if self._result[self.methods().index(dependence)] == EnumResult.PASS.value:
                func(self, *args, **kwargs)
            else:
                self._cursor += 1
                self.skipIter('有前置流程发生错误')
        return wrapper
    return  decorator