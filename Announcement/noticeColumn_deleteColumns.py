#-*- coding:utf-8 -*-
"""
@note:
	2.5 删除栏目
@author: Qred
@file: noticeColumn_deleteColumns.py
@time: 2020/03/31
"""
from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def deleteColumns(session, Ids=1):
	# 删除栏目
	url = host + '/yundeng/noticeColumn/deleteColumns'
	url += str(Ids)
	raw = session.delete(url)

	print(raw.json())

	return raw