#-*- coding:utf-8 -*-
"""
@note:
	1.9 公告列表
@author: Qred
@file: notice_list.py
@time: 2020/03/31
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def list(session, pageNum = 1, pageSize = 10, searchKey = '', publishStartTime = '', publishEndTime = "", columnIds = [], publisherIds = [], noticeState = '', creatorIds = [], createStartTime = '', createEndTime = ''):

	url = host + '/yundeng/notice/list'
	value = {"pageSize": pageSize, "pageNum": pageNum}
	if searchKey is not "":
		value.update({ 'searchKey' : searchKey})
	if publishStartTime is not "":
		value.update({ 'publishStartTime' : publishStartTime})
	if publishEndTime is not "":
		value.update({ 'publishEndTime' : publishEndTime})
	if columnIds.__len__() > 0:
		value.update({ 'columnIds' : columnIds})
	if publisherIds.__len__() > 0:
		value.update({ 'publisherIds' : publisherIds})
	if noticeState is not "":
		value.update({ 'noticeState' : noticeState})
	if creatorIds is not "":
		value.update({ 'creatorIds' : creatorIds})
	if createStartTime is not "":
		value.update({ 'createStartTime' : createStartTime})
	if createEndTime is not "":
		value.update({ 'createEndTime' : createEndTime})

	raw = session.post(url, data = value)

	print(raw.json())

	return raw