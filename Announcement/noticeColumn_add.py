#-*- coding:utf-8 -*-
"""
@note:
	2.1 创建公告栏目
@author: Qred
@file: noticeColumn_add.py
@time: 2020/03/31
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def add(session, columnName='', isActive= 1, remark=''):
	'''
	2.1 创建公告栏目
	:param session:
	:param columnName:公告名称
	:param isActive: 是否启用（0 否, 1 是）
	:param reason:原因
	:return:
	'''
	# noticeState 公告状态(1-已发布,2-下线)
	url = host + '/yundeng/noticeColumn/add'
	value = { "remark" : remark, "columnName" : columnName, "isActive" : isActive}
	raw = session.post(url, data = value)

	print(raw.json())

	return raw