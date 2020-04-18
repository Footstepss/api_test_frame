#!/usr/bin/python
# -*- coding: utf-8 -*-
from base_data import root_path
import importlib
import inspect
from iters.base_case import ApiIter
import os,re

class Run:

    def __init__(self, start_dir = root_path+'/test_case', pattern='^test.*.py$'):
        self._module = 'test_case'
        needed_excute_list = self.get_all_files(start_dir,pattern=pattern,module=self._module)
        self.needed_excute_list = set()
        if len(needed_excute_list) != 0:
            self._needed_excute_list = [importlib.import_module(item[0:-3]) for item in needed_excute_list]
            for module in self._needed_excute_list:
                for name,obj in inspect.getmembers(module,inspect.isclass):
                    if issubclass(obj,ApiIter) and name != ApiIter.__name__:
                        self.needed_excute_list.add(obj)
        if len(self.needed_excute_list) != 0:
            for case in self.needed_excute_list:
                case()()

    def _pattern(self,string,pattern):
        pattern_result = re.search(pattern,string)
        return bool(pattern_result)

    def get_all_files(self,dir,pattern,module):
        '''DFS查找文件'''
        module_list = []
        list = os.listdir(dir)
        for i in range(0, len(list)):
            path = os.path.join(dir, list[i])
            _module = module + '.' + list[i]
            if os.path.isdir(path):
                module_list.extend(self.get_all_files(path,pattern,_module))
            if os.path.isfile(path):
                if self._pattern(list[i],pattern):
                    module_list.append(_module)
        return module_list

main = Run


####