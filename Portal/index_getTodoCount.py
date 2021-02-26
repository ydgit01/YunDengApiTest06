#-*- coding:utf-8 -*-
"""
@note:
	0.2获取待办事项数量
@author: Qred
@file: index_getTodoCount.py
@time: 2020/03/30
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)


def getTodoCount(session):

	url = host + '/yundeng/index/getTodoCount'
	raw = session.get(url)

	print(raw.json())

	return raw