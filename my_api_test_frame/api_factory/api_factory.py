#!/usr/bin/python
# -*- coding: utf-8 -*-

from utils.util import getSubstrNum
from utils.logs import log_message
import requests
#from time import sleep
#import abc

REQUEST_TYPE_TUPLE = ('GET', 'POST', 'PUT', 'GET_RESTFUL', 'POST_RESTFUL','PUT_RESTFUL')
MUDULE_TUPLE = ('TMS','PMS','FMS','RMS','EMS','SIGN','LOGIN')

"""
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
    def validate(self, instance, value): # 6
        if value not in REQUEST_TYPE_TUPLE:
            raise ValueError('the type is not required')
        return value

class ModuleValidated(Validated):
    '''继承抽象基类,判断模块'''
    def validate(self, instance, value): # 6
        if value not in MUDULE_TUPLE:
            raise ValueError('the type is not required')
        return value
"""

def ApiFactory(cls_name,url,module,request_type):     #print(cls_name,url,module)

    header = {'Content-type': 'application/json;charset=UTF-8'}
    _module = None
    _request_type = None

    if request_type in REQUEST_TYPE_TUPLE:
        _request_type = request_type
    else:
        raise ValueError('the request_type is not required')

    if module in MUDULE_TUPLE:
        _module = module
    else:
        raise ValueError('the module is not required')

    def __repr__(self):
        return 'class_name -> {} \n url -> {} \n '.format(cls_name,url)


    def _send_post(self,data):
        log_message('发送请求').logger.info('发送%s请求'%self.url)
        response = requests.post(url = self.url,json = data,headers = self.header)
        return response


    def _send_get(self,data):
        log_message('发送请求').logger.info('发送%s请求'%self.url)
        response = requests.get(url = self.url,params = data,headers = self.header)
        return response


    def _send_get_restful(self,data):
        self._revise_result_url(data)
        log_message('发送请求').logger.info('发送%s请求'%self.url)
        response = requests.get(url = self.url,headers = self.header)
        return response


    def _send_put_restful(self,data):
        self._revise_result_url(data)
        log_message('发送请求').logger.info('发送%s请求'%self.url)
        response = requests.put(url = self.url,headers = self.header)
        return response

    def _send_post_restful(self,data):
        self._revise_result_url(data['url'])
        log_message('发送请求').logger.info('发送%s请求'%self.url)
        response = requests.post(url = self.url,json  = data['data'],headers = self.header)
        return response


    def _get_sends_list(self):
        #return sorted(filter(lambda x:'_send_' in x,self.__dict__.keys()))
        return list(filter(lambda m: m.startswith('_send_') and callable(getattr(self, m)), dir(self)))

    def send_request(self,data=None):
        send_switch = dict(zip(sorted(REQUEST_TYPE_TUPLE),self._get_sends_list()))
        print(send_switch)
        #response = self.__dict__[send_switch[self.request_type]](data)
        response = getattr(self,send_switch[self.request_type])(data)
        log_message('响应信息').logger.info(response.text)
        return response


    def _revise_result_url(self,data):
        '''将restful风格的接口参数数据,填入url'''
        if self.request_type != 'GET_RESTFUL' and self.request_type != 'POST_RESTFUL' and self.request_type != 'PUT_RESTFUL':
            log_message('请求错误').logger.error('请求类型不是restful风格')
            raise AssertionError
        elif not isinstance(data,dict):
            log_message('类型错误').logger.error('传入restful的请求的参数不是字典数据')
            raise TypeError
        elif getSubstrNum(self.url,'%s') != len(data):
            log_message('参数错误').logger.error('传入restful的请求的参数个数不对,需要%d个'%getSubstrNum(self.url,'%s'))
            raise ValueError
        else:
            self.url = self.url%tuple(data.values())

    cls_attrs = dict(
        __repr__  = __repr__,
        header = header,
        url = url,
        cls_name = cls_name,
        module = _module,
        request_type = _request_type,
        _send_post = _send_post,
        _send_get = _send_get,
        _send_get_restful = _send_get_restful,
        _send_put_restful = _send_put_restful,
        _send_post_restful = _send_post_restful,
        _get_sends_list = _get_sends_list,
        send_request = send_request,
        _revise_result_url = _revise_result_url
    )

    return type(cls_name, (object,), cls_attrs)

#ApiFactory(**d)
"""
d = {'module':'LOGIN','cls_name':'Login','url':'www.1111.com','request_type':'GET'}
class A:
    def fun(self):
        print('A')

B = ApiFactory(**d)

C = ApiFactory(**d)

print(B is C)
import copy
#B().request_type = 1

"""