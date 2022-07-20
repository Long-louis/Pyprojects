# -- coding:utf-8 -- #

"""
Project:PyProject
File:python并发编程.py
Author:halongbay
Date:2022/7/14 8:38

"""
def yield_return():
    test = 1
    while test < 10:
        a = yield test
        print(a)
        test += 1
