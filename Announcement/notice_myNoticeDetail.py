#-*- coding:utf-8 -*-
"""
@note:
	1.3 查询我的公告详情
@author: Qred
@file: notice_myNoticeDetail.py
@time: 2020/03/30
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def myNoticeDetail(session, Id=1):

	url = host + '/yundeng/notice/myNoticeDetail'
	url += str(Id)
	raw = session.get(url)

	print(raw.json())

	return raw