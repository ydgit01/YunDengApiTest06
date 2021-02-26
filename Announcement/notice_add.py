#-*- coding:utf-8 -*-
"""
@note:
	1.4 创建公告
@author: Qred
@file: notice_add.py
@time: 2020/03/30
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def add(session, columnId = 49,noticeTitle = '12', noticeContent = 'qeqeq', noticeState = 1, noticeTargets = [{"scopeType":1,"targetId":"9999"}]):
	"""
	:param session:
	:param columnId: 栏目ID,Long,100
	:param noticeTitle: 公告标题,是,String
	:param noticeContent: 公告详情,是,String
	:param noticeState: 操作状态 0 暂存 1 发布,是,Integer
	:param noticeTargets: 公告发布对象节点,是,List,
						scopeType 公告发布范围,是,Long,1 按组织 2 按角色
						targetId  对象ID,是,String,scopeType为1时填 组织IDscopeType为2时填 角色ID
	:return:
	"""
	url = host + '/yundeng/notice/add'
	value = {"columnId": columnId,"noticeTitle":noticeTitle,"noticeContent":noticeContent,"noticeState":noticeState,"noticeTargets": noticeTargets}
	raw = session.post(url, data = value)

	print(raw.json())

	return raw