#-*- coding:utf-8 -*-
"""
@note:
	1.5 查询公告详情
@author: Qred
@file: notice_detail.py
@time: 2020/03/30
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)


def detail(session, Id=1):
	'''
	查询公告详情
	:param session:
	:param Id:
	:return:
	'''
	url = host + '/yundeng/noticeColumn/detail'
	url += str(Id)

	raw = session.get(url)

	print(raw.json())

	return raw