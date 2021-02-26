#-*- coding:utf-8 -*-
"""
@note:
	15. 用户详情
@author: Qred
@file: user_detail.py
@time: 2020/04/08
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)

# print (host)

def detail(session, operatorIds='' ):
	'''
	15. 用户详情
	:param session:
	:param operatorIds:用户ids(多个用逗号隔开)
	:return:
	'''
	url = host + '/yundeng/user/detail/'
	url += str(operatorIds)
	raw = session.get(url)

	print(raw.json())

	return raw
