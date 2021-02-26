# -*- coding:utf-8 -*-
"""
@note:
	3.5服务列表查询
@author: Qred
@file: microservice_list.py
@time: 2020/04/02
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)


# print (host)

def list(session, pageNum=1, pageSize=10, key='', name='ss', modelCreateType='',
         desc='', microserviceClassifyId='', gitVersion='', creatorIds='', createTimeStart='', createTimeEnd='',
         updateTimeStart='', updateTimeEnd=''):
	'''

	:param session:
	:param pageNum:第几页
	:param pageSize:每页显示条数
	:param key:服务唯一标识
	:param name:服务名称
	:param modelCreateType:模型实体创建方式 online 线上 offline 线下
	:param desc:服务描述
	:param microserviceClassifyId: 服务所属分类
	:param gitVersion: 版本号
	:param creatorIds:创建人
	:param createTimeStart:创建开始时间 yyyy-MM-dd
	:param createTimeEnd:创建结束时间 yyyy-MM-dd
	:param updateTimeStart:修改开始时间 yyyy-MM-dd
	:param updateTimeEnd:修改结束时间 yyyy-MM-dd
	:return:
	'''
	url = host + '/yundeng/microservice/list'
	value = {"pageNum": pageNum, "pageSize": pageSize, "key": key, "name": name, "desc": desc,
	         "modelCreateType": modelCreateType, "microserviceClassifyId": microserviceClassifyId,
	         "gitVersion": gitVersion, "creatorIds": creatorIds, "createTimeStart": createTimeStart,
	         "createTimeEnd": createTimeEnd, "updateTimeStart": updateTimeStart, "updateTimeEnd": updateTimeEnd}

	raw = session.post(url, data=value)

	print(raw.json())

	return raw
