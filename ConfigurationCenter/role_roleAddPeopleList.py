#-*- coding:utf-8 -*-
"""
@note:
	17. 角色添加人员
@author: Qred
@file: role_roleAddPeopleList.py
@time: 2020/04/08
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)

# print (host)

def roleAddPeopleList(session, userIds='', roleId='' ):
	'''
	17. 角色添加人员
	:param session:
	:param userIds:operatorIds
	:param roleId:角色id（不包含已经存在这个角色的用户）
	:return:
	'''
	url = host + '/yundeng/role/roleAddPeopleList'
	value = {"userIds": userIds, "roleId": roleId}
	raw = session.post(url, data=value)

	print(raw.json())

	return raw