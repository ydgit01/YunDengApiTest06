#-*- coding:utf-8 -*-
"""
@note:
	1.12 置顶/取消置顶公告(支持批量)
@author: Qred
@file: notice_batchTop.py
@time: 2020/03/31
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def batchTop(session, noticeIds=[1,], isTop= 1,reason=''):
	'''

	:param session:
	:param noticeIds:公告ID列表
	:param isTop: 0 取消置顶 1 置顶
	:param reason:原因
	:return:
	'''
	# noticeState 公告状态(1-已发布,2-下线)
	url = host + '/yundeng/notice/batchTop'
	value = { "reason" : reason, "noticeIds" : noticeIds, "isTop" : isTop}
	raw = session.post(url, data = value)

	print(raw.json())

	return raw