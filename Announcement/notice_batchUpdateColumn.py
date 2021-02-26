#-*- coding:utf-8 -*-
"""
@note:
	1.11 批量更改公告栏目
@author: Qred
@file: notice_batchUpdateColumn.py
@time: 2020/03/31
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def batchUpdateColumn(session, Ids=[1,], columnId= 1,reason=''):
	"""
	批量更改公告栏目
	:param session:
	:param Ids: 公告ID列表
	:param columnId:栏目ID
	:param reason:原因备注
	:return:
	"""
	# noticeState 公告状态(1-已发布,2-下线)
	url = host + '/yundeng/notice/batchUpdateColumn'
	value = { "reason" : reason, "noticeIds" : Ids, "columnId" : columnId}
	raw = session.post(url, data = value)

	print(raw.json())

	return raw