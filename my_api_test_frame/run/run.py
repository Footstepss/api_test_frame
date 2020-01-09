#!/usr/bin/python
# -*- coding: utf-8 -*-
from base_data import root_path
from utils.util import latest_report
import importlib
import inspect
from iters.base_case import ApiIter

class Run:

    def __init__(self, start_dir = root_path+'/test_case', pattern='test*.py'):
        needed_excute_list = list(filter(lambda m: m.startswith('test'),latest_report(start_dir)))
        self.needed_excute_list = set()
        if len(needed_excute_list) != 0:
            self._needed_excute_list = [importlib.import_module('test_case.'+item[0:-3]) for item in needed_excute_list]
            a = self._needed_excute_list[0]
            for module in self._needed_excute_list:
                for name,obj in inspect.getmembers(module,inspect.isclass):
                    if issubclass(obj,ApiIter) and name != ApiIter.__name__:
                        self.needed_excute_list.add(obj)

        if len(self.needed_excute_list) != 0:
            for case in self.needed_excute_list:
                case()()

Run()
