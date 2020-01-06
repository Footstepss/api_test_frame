#!/usr/bin/python
# -*- coding: utf-8 -*-

from utils.logs import log_message
from suits_dict import SuitDict
from api_dict import api_dict
import abc
from api_factory.api_factory import ApiFactory
from utils.json_templates import JsonTemplateReader

#from collections import Iterable



class DependentException(Exception):
    """
    Raise this exception in a debug to skip it.
    """

"""
class _LordDependentSuitData():

    def __init__(self,dependence = _non_dependence):
        self.dependence = dependence

    def __enter__(self):
        try:
            dependence_data = self.dependence()
        except Exception as e:
            log_message('前置流程').logger.error('前置流程发生错误')
            raise DependentException()
        else:
            return dependence_data

    def __exit__(self, exc_type, exc_val, exc_tb):
        if isinstance(exc_type,Exception):
            log_message('数据渲染').logger.error('渲染发生错误')
            log_message('数据渲染').logger.error(exc_val)
            log_message('数据渲染').logger.error(exc_tb)
            return False
        return True
"""

class BaseSuitMeta(type):

    def __new__(mcs, name, bases, attrs):
        attrs['_DependentException'] = DependentException
        #attrs['JsonTemplateReader'] = JsonTemplateReader
        return type.__new__(mcs, name, bases, attrs)


class ApiPropertyAbstractBase:
    '''属性描述符类'''
    def __init__(self,attrname):
        self.attrname = attrname

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:

            return instance.__dict__[self.attrname]

    def __set__(self, instance, value):
        instance.__dict__[self.attrname] = value

class Validated(abc.ABC,ApiPropertyAbstractBase):
    '''判断传入的值,抽象基类'''
    def __set__(self, instance, value):
        value = self.validate(instance, value)
        super().__set__(instance, value)

    @abc.abstractmethod
    def validate(self, instance, value):
        '''返回经过验证的值或抛出异常'''


class RequestTypeValidated(Validated):
    '''继承抽象基类,判断请求类型'''
    def validate(self, instance, value):
        if isinstance(value,list):
            _temp = list()
            count = 2
            for item in value:
                if item in api_dict.keys():
                    if item not in instance.__dict__.keys():
                        #instance.__dict__[item] = ApiFactory(**api_dict[item])
                        _temp.append(ApiFactory(**api_dict[item]))
                    else:
                        #instance.__dict__[item+str(count)] = ApiFactory(**api_dict[item])
                        #count += 1
                        _temp.append(ApiFactory(**api_dict[item]))
                    #print(instance.__dict__)
                else:
                    raise ValueError('api is not requied')
            instance.__dict__['api_class_list'] = _temp
        else:
            raise TypeError
        return value


class BaseSuit(metaclass=BaseSuitMeta):
    """基类"""

    #托管属性描述符
    api_list = RequestTypeValidated('api_list')

    def __init__(self,api_list = api_list,dependence = {}):
        self.api_list = api_list
        self.dependence_data = dependence
        self.cursor = 0
        self.test_data = {item:{} for item in api_list}
        self.header = [{'Content-type': 'application/json;charset=UTF-8'} for item in api_list]
        self.JsonTemplateReader = JsonTemplateReader

    def DependentException(self):
        raise self._DependentException()

    def __len__(self):
        return len(self.api_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor < len(self):
            data = self.JsonTemplateReader.json_template_api(self.api_list[self.cursor],**self.test_data[self.api_list[self.cursor]])
            self.api_class_list[self.cursor].header = self.header[self.cursor]
            response = self.api_class_list[self.cursor]().send_request(data = data)
            assert response.status_code == 200
            self.cursor += 1
            return response


