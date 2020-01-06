#!/usr/bin/python
# -*- coding: utf-8 -*-

from api_suits.api_suit import BaseSuit
from utils.logs import log_message
from suits_dict import SuitDict
from utils.enum_class import EnumResult
import traceback
import sys

def _non_dependence():
    return None


class PreConditionException(Exception):
    '''前置条件发生错误'''

class SkipException(Exception):
    '''跳过用例'''

class _LordPreCondition():

    def __init__(self,dependence = _non_dependence):
        self.dependence = dependence

    def __enter__(self):
        try:
            pre_condition = self.dependence()
        except Exception as e:
            log_message('前置条件').logger.error('上下文条件发生错误')
            raise PreConditionException()
        else:
            return pre_condition

    def __exit__(self, exc_type, exc_val, exc_tb):
        if isinstance(exc_type,Exception):
            log_message('数据渲染').logger.error('中间层错误')
            log_message('数据渲染').logger.error(exc_val)
            log_message('数据渲染').logger.error(exc_tb)
            return False
        return True

class ApiIter:

    def __init__(self,dependence = {}):
        # super(ApiIter, self).__init__()
        if dependence == None:
            raise PreConditionException('前置条件发生错误')
        else:
            self.response = dependence
        self.iter = BaseSuit(SuitDict[self.__class__.__name__],dependence = dependence)
        self._cursor = 0
        self._result = []
        self._tag = True
        self.json = __import__('json')
        self.base_data = __import__('base_data')

    def methods(self):
        '''获取iter开头的方法，返回集合'''
        return list(filter(lambda m: m.startswith("iter") and callable(getattr(self, m)), dir(self)))

    def skipIter(self,description = None):
        raise SkipException(description)

    def __repr__(self):
        return "result -----{} \ncase -----{} \nresponse -----{} \nheader -----{}".format(str(self._result),self.methods(),self.response,self.iter.header)

    def __call__(self, *args, **kwargs):
        iter_list = self.methods()
        for item in iter_list:
            func = getattr(self,item)
            try:
                func()
            except SkipException:
                self._result.append(EnumResult.SKIP.value)
                self._tag = False
                print(traceback.format_exc())
            except AssertionError:
                self._result.append(EnumResult.FAILURE.value)
                self._tag = False
                print(traceback.format_exc())
            except Exception:
                self._result.append(EnumResult.ERROR.value)
                self._tag = False
                print(traceback.format_exc())
            else:
                self._result.append(EnumResult.PASS.value)
            print(self)
        return self.response if self._tag == True else False

if __name__ == '__main__':
    pass