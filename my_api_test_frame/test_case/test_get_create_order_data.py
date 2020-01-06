#!/usr/bin/python
# -*- coding: utf-8 -*-

from iters.base_case import *
from utils.util import dependence_decoration
from test_case.test_login import LoginSuit

class GetCreatOrderData(ApiIter):

    def __init__(self):
        super().__init__(dependence=LoginSuit()())

    def iter_a(self):
        self.iter.cursor = self._cursor
        data = {
            'customer_company_name':self.response['LoginSuit_iter_a']['data']['companyName']
        }
        self.iter.test_data[self.iter.api_list[self._cursor]] = data
        self.iter.header[self._cursor]['Authorization'] = self.base_data.token + self.response['LoginSuit_iter_a']['data']['token']
        result = next(self.iter).text
        self.response[self.__class__.__name__+'_'+sys._getframe().f_code.co_name] = self.json.loads(result)
        self._cursor += 1

if __name__ == '__main__':
    GetCreatOrderData()()