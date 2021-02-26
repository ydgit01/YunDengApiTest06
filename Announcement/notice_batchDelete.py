#-*- coding:utf-8 -*-
"""
@note:
	1.7 删除公告(支持批量)
@author: Qred
@file: notice_batchDelete.py
@time: 2020/03/30
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
print (host)

def batchDelete(session, Ids=[1,], reason=''):

	url = host + '/yundeng/notice/batchDelete'
	value = { "reason" : reason, "noticeIds" : Ids}
	raw = session.post(url, data = value)

	print(raw.json())

	return raw