#-*- coding:utf-8 -*-
"""
@note:
	1.8 修改公告状态(支持批量)
@author: Qred
@file: notice_batchUpdateState.py
@time: 2020/03/31
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def batchUpdateState(session, Ids=[1,], noticeState= 1,reason=''):

	# noticeState 公告状态(1-已发布,2-下线)
	url = host + '/yundeng/notice/batchUpdateStatee'
	value = { "reason" : reason, "noticeIds" : Ids, "noticeState" : noticeState}
	raw = session.post(url, data = value)

	print(raw.json())

	return raw