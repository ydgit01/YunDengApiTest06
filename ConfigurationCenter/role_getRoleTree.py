#-*- coding:utf-8 -*-
"""
@note:
	8. 获取角色详情
@author: Qred
@file: role_getRoleTree.py
@time: 2020/04/07
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def getRoleTree(session, roleId=1):
	'''
	8. 获取角色详情
	:param session:
	:param roleId:角色id
	:return:
	'''
	url = host + '/yundeng/role/getRoleTree/'
	url += str(roleId)
	raw = session.get(url)

	print(raw.json())

	return raw
