#-*- coding:utf-8 -*-
"""
@note:
	20. 在线情况
@author: Qred
@file: stat_onlineSituation.py
@time: 2020/04/08
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)

# print (host)

def onlineSituation(session):
	'''
	20. 在线情况
	'''
	url = host + '/yundeng/stat/onlineSituation'
	raw = session.get(url)

	print(raw.json())

	return raw