#-*- coding:utf-8 -*-
"""
@note:
	16. 用户列表所有
@author: Qred
@file: user_listAll.py
@time: 2020/04/08
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)

# print (host)

def listAll(session, orgId='', roleId='' ):
	'''
	16. 用户列表所有
	:param session:
	:param orgId:组织id（不包含这个已经存在这个组织的用户）
	:param roleId:角色id（不包含已经存在这个角色的用户）
	:return:
	'''
	url = host + '/yundeng/user/listAll'
	value = {"orgId": orgId, "roleId": roleId}
	raw = session.get(url, params=value)

	print(raw.json())

	return raw