#-*- coding:utf-8 -*-
"""
@note:
	0.1获取待办事项
@author: Qred
@file: index_getTodo.py
@time: 2020/03/30
"""


from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)


def getTodo(session, pageStart=1, pageSize=1000):
	"""
	获取待办事项
	:param session: 带cookeie的请求
	:param pageStart: 开始页码
	:param pageSize: 页面大小
	:return:
	"""
	url = host + '/yundeng/index/getTodo'
	value = {"pageSize": pageSize, "pageStart" : pageStart}
	raw = session.get(url,params=value)

	print(raw.json())

	return raw