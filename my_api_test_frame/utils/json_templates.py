#!/usr/bin/python
# -*- coding: utf-8 -*-

from jinja2 import Environment, FileSystemLoader
from utils.logs import log_message
from utils.util import get_api_para_template_path
import json

class JsonTemplateReader():
    #模板类封装,参考github https://github.com/zhangting85/SimpleApiTest
    def __init__(self,path = get_api_para_template_path()):
        self.env = Environment(loader=FileSystemLoader(path))
    def get_data(self,test_name,**kwargs):
        template = self.env.get_template(test_name + ".json")
        log_message('数据渲染').logger.info(template.render(**kwargs))
        data = json.loads(template.render(**kwargs))
        log_message('数据渲染').logger.info(data)
        return data

    def get_data_code_genaration(self,test_name,**kwargs):
        template = self.env.get_template(test_name + ".txt")
        #log_message('数据渲染').logger.info(json.loads(template.render(**kwargs)))
        return template.render(**kwargs)

    @staticmethod
    def json_template_api(class_name,**kwargs):
        '''读取数据'''
        return JsonTemplateReader().get_data(class_name, **kwargs)

    def json_template_code_generation(self,template,**kwargs):
        '''读取数据'''
        return self.get_data_code_genaration(template, **kwargs)