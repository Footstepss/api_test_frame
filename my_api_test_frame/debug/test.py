#!/usr/bin/python
# -*- coding: utf-8 -*-


def class_factory(cls_name, field_names):

        field_names = field_names.replace(',', ' ').split()  # 1
        field_names = tuple(field_names)  # 2

        def __init__(self, *args, **kwargs):  # 3
            attrs = dict(zip(self.__slots__, args))
            for name, value in attrs.items():
                setattr(self, name, value)

        def __iter__(self):  # 4
            for name in self.__slots__:
                yield getattr(self, name)

        def __repr__(self):  # 5
            values = ', '.join('{}={!r}'.format(*i) for i
                               in zip(self.__slots__, self))
            return '{}({})'.format(self.__class__.__name__, values)

        @staticmethod
        def test():
            print('A')

        cls_attrs = dict(__slots__ = field_names,  # 6
                         __init__  = __init__,
                         __iter__  = __iter__,
                         __repr__  = __repr__,
                         test = test)

        return type(cls_name, (object,), cls_attrs)  # 7


Fruits = class_factory("Fruits","description weight price")
Fruits().test()

class A:
    a = 1
    def fun(self):
        print(self.b)

class B(A):
    b = 0


def flatten(nested):
    if type(nested)==list:
        for sublist in nested:
            for i in flatten(sublist):
                yield i
    else:
        yield nested
print(list(flatten([[[1],2],3,4,[5,[6,7]],8])))

[[[1],2],3,4,[5,[6,7]],8]