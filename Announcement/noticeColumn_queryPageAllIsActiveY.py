#-*- coding:utf-8 -*-
"""
@note:
	2.7 公告栏目列表-已启用-分页
@author: Qred
@file: noticeColumn_queryPageAllIsActiveY.py
@time: 2020/03/31
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def quequeryPageAllIsActiveYryAll(session, columnName='' ,pageNum=1, pageSize=10):
	'''
	2.7 公告栏目列表-已启用-分页
	:param session:
	:param isActive:是否启用（0 否, 1是）
	:param columnName:栏目名称
	:return:
	'''
	url = host + '/yundeng/noticeColumn/queryPageAllIsActiveY'
	value = {"columnName": columnName, "pageNum": pageNum, 'pageSize' : pageSize}
	raw = session.get(url, params=value)

	print(raw.json())

	return raw