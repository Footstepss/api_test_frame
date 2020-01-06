#!/usr/bin/python
# -*- coding: utf-8 -*-

from enum import Enum

class EnumResult(Enum):
    '''枚举类，枚举测试结果'''
    PASS =  'P'
    FAILURE = 'F'
    ERROR = 'E'
    SKIP =  'S'

if __name__ == '__main__':
    print(EnumResult.PASS.value is 'P')