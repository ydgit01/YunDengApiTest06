#-*- coding:utf-8 -*-
"""
@note:
	21. 批量修改用户角色
@author: Qred
@file: user_modifyUserRoles.py
@time: 2020/04/08
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)

# print (host)

def modifyUserRoles(session, operatorIdList='', roleId='' ):
	'''
	21. 批量修改用户角色
	:param session:
	:param operatorIdList:operatorIds
	:param roleId:角色id（不包含已经存在这个角色的用户）
	:return:
	'''
	url = host + '/yundeng/user/modifyUserRoles'
	value = {"operatorIdList": operatorIdList, "roleId": roleId}
	raw = session.post(url, data=value)

	print(raw.json())

	return raw