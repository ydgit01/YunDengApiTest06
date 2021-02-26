#-*- coding:utf-8 -*-
"""
@note:
	23. 员工用户列表
@author: Qred
@file: user_selectEmployeePage.py
@time: 2020/04/08
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def selectEmployeePage(session, pageNum=1, pageSize=10, roleId = '', orgId='', userName=''):
	'''
	23. 员工用户列表
	:param session:
	:param pageNum:当前页
	:param pageSize:分页大小
	:param roleId:角色id
	:param orgId:组织id
	:param userName:用户名
	:return:
	'''
	url = host + '/yundeng/user/selectEmployeePage'
	value = {"roleId": roleId, "orgId": orgId, "userName":userName, "pageNum":pageNum, "pageSize":pageSize }
	raw = session.get(url, params = value)

	print(raw.json())

	return raw