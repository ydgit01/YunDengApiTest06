#-*- coding:utf-8 -*-
"""
@note:
	1.2 查询当前登录用户公告列表
@author: Qred
@file: notice_myList.py
@time: 2020/03/30
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def myList(session, pageNum=1, pageSize=10, columnId=''):

	url = host + '/yundeng/notice/myList'
	value = {"pageSize": pageSize, "pageNum": pageNum}
	if columnId is not '':
		value.update({"columnId" : columnId})
	raw = session.get(url, params=value)

	print(raw.json())

	return raw