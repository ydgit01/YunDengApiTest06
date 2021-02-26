#-*- coding:utf-8 -*-
"""
@note:
	0.5 获取指定用户拥有的菜单权限
@author: Qred
@file: userAuth_querySpecifiesTheUserSExistingRoles.py
@time: 2020/04/07
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)

# print (host)

def querySpecifiesTheUserSExistingRoles(session, id=1):
	'''
	0.5 获取指定用户拥有的菜单权限
	:param session:
	:param id:用户ID
	:return:
	'''
	url = host + '/yundeng/userAuth/querySpecifiesTheUserSExistingRoles'
	url += str(id)

	raw = session.delete(url)

	print(raw.json())

	return raw