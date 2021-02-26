#-*- coding:utf-8 -*-
"""
@note:
	2.6 公告栏目列表-全量
@author: Qred
@file: noticeColumn_queryAll.py
@time: 2020/03/31
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def queryAll(session, isActive=1, columnName=10):
	'''
	2.4 公告栏目列表
	:param session:
	:param isActive:是否启用（0 否, 1是）
	:param columnName:栏目名称
	:return:
	'''
	url = host + '/yundeng/noticeColumn/queryAll'
	value = {"columnName": columnName, "isActive": isActive}
	raw = session.get(url, params=value)

	print(raw.json())

	return raw