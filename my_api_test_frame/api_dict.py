#!/usr/bin/python
# -*- coding: utf-8 -*-

import os



base_url_dict = {
    'pro_env': 'https://gateway.wlyuan.com.cn',
    'test_env': None
}

base_url = base_url_dict['pro_env']



#cls_name,url,module,request_type
api_dict = {
    'Login':{
        'cls_name': 'Login',
        'url': base_url + '/auth/open/login',
        'module': 'LOGIN',
        'request_type': 'POST'
    },
    'PersonDriverLogin':{
        'cls_name': 'PersonDriverLogin',
        'url': base_url + '/auth/open/login/driver',
        'module': 'LOGIN',
        'request_type': 'POST'
    },
    'SearchCustomer':{
        'cls_name': 'SearchCustomer',
        'url': base_url + '/tms/order/customercheck',
        'module': 'TMS',
        'request_type': 'POST'
    },
    'SearchShipper':{
        'cls_name': 'SearchShipper',
        'url': base_url + '/tms/order/tocheck',
        'module': 'TMS',
        'request_type': 'POST'
    },
    'SearchReceiver':{
        'cls_name': 'SearchReceiver',
        'url': base_url + '/tms/order/endcheck',
        'module': 'TMS',
        'request_type': 'POST'
    },
    'SearchGoods':{
        'cls_name': 'SearchGoods',
        'url': base_url + '/tms/order/goodscheck',
        'module': 'TMS',
        'request_type': 'POST'
    }
}