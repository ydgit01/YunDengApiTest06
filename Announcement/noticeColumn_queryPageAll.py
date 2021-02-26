#-*- coding:utf-8 -*-
"""
@note:
	2.4 公告栏目列表
@author: Qred
@file: noticeColumn_queryPageAll.py
@time: 2020/03/31
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def queryPageAll(session, pageNum=1, pageSize=10):
	'''
	2.4 公告栏目列表
	:param session:
	:param pageNum:当前
	:param pageSize:分页大小
	:return:
	'''
	url = host + '/yundeng/noticeColumn/queryPageAll'
	value = {"pageSize": pageSize, "pageNum": pageNum}
	raw = session.get(url, params=value)

	print(raw.json())

	return raw