#-*- coding:utf-8 -*-
"""
@note:
	5. 新增角色 7. 修改角色
@author: Qred
@file: role_save.py
@time: 2020/04/07
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def save(session, roleName = 'tets', roleDesc = '', roleId = '', reason='', funccode=''):
	'''
	5. 新增角色 7. 修改角色
	:param session:
	:param roleName:角色名称
	:param roleId:角色id
	:param roleDesc:角色描述
	:param reason:修改原因
	:param funccode:资源id，如果选择多个资源以逗号隔开
	:return:
	'''
	url = host + '/yundeng/role/save'
	value = {"roleName": roleName,"roleDesc":roleDesc}
	if roleId is not '':
		value.update({"roleId":roleId, "reason":reason, "funccode":funccode})
	raw = session.post(url, data = value)

	print(raw.json())

	return raw