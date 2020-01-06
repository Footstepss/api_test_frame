#!/usr/bin/python
# -*- coding: utf-8 -*-

from iters.base_case import *
from utils.util import dependence_decoration
from base_data import account_api,driver_account
from utils.frozen_json import FrozenJSON

class LoginSuit(ApiIter):

    def iter_a(self):
        self.iter.cursor = self._cursor
        data = {
            'user':self.base_data.account_api['发货方'][0],
            'password':self.base_data.account_api['发货方'][1],
        }
        self.iter.test_data[self.iter.api_list[self._cursor]] = data
        result = next(self.iter).text
        self.response[self.__class__.__name__+'_'+sys._getframe().f_code.co_name] = self.json.loads(result)
        self._cursor += 1

    @dependence_decoration('iter_a')
    def iter_b(self):
        self.iter.cursor = self._cursor
        data = {
            'user':self.base_data.account_api['承运商'][0],
            'password':self.base_data.account_api['承运商'][1],
        }
        self.iter.test_data[self.iter.api_list[self._cursor]] = data
        print(next(self.iter).text)
        self._cursor += 1

    def iter_c(self):
        self.iter.cursor = self._cursor
        data = {
            'user':self.base_data.account_api['发货方企业管理员'][0],
            'password':self.base_data.account_api['发货方企业管理员'][1],
        }
        self.iter.test_data[self.iter.api_list[self._cursor]] = data
        print(next(self.iter).text)
        self._cursor += 1

    def iter_d(self):
        self.iter.cursor = self._cursor
        data = {
            'driver_openID':self.base_data.driver_account[0]
        }
        self.iter.test_data[self.iter.api_list[self._cursor]] = data
        print(next(self.iter).text)
        self._cursor += 1

if __name__ == '__main__':
    a = LoginSuit()()
    a = FrozenJSON(a)
    print(a.LoginSuit_iter_a.code)