#-*- coding:utf-8 -*-
"""
@note:
	2.3 编辑公告栏目
@author: Qred
@file: noticeColumn_edit.py
@time: 2020/03/31
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def edit(session, Id=1, columnName='', isActive= 1, remark=''):
	'''
	查询公告详情
	:param session:
	:param Id: 栏目id
	:param columnName: 栏目名称
	:param isActive: 是否启用
	:param remark:
	:return:
	'''
	url = host + '/yundeng/noticeColumn/edit'
	url += str(Id)
	value = {'id': Id, "remark": remark, "columnName": columnName, "isActive": isActive}
	raw = session.post(url, data= value)

	print(raw.json())

	return raw