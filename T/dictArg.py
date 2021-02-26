#-*- coding:utf-8 -*-
"""
@note:
@author: Qred
@file: dictArg.py
@time: 2020/04/13
"""
def fun1(**kwargs):
	print (kwargs.items().__len__())



if __name__ == '__main__':
    dit = { 'qq':11111220 }
    fun1(**dit)