#-*- coding:utf-8 -*-
"""
@note:
	19. 组织添加人员
@author: Qred
@file: organization_dorganizationAddPeople.py
@time: 2020/04/08
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)

# print (host)

def dorganizationAddPeople(session, orgId='', empIdList='' ):
	'''
	19. 组织添加人员
	:param session:
	:param orgId:组织id
	:param empIdList:用户ids
	:return:
	'''
	url = host + '/yundeng/organization/dorganizationAddPeople'
	value = {"orgId": orgId, "empIdList": empIdList}
	raw = session.post(url, data=value)

	print(raw.json())

	return raw