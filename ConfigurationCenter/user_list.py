# -*- coding:utf-8 -*-
"""
@note:
	12. 用户列表
@author: Qred
@file: user_list.py
@time: 2020/04/08
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)

# print (host)

def list(session, userName='', status='', email='', mobileNo='', roleId='', orgId='', pageNum='', pageSize=''):
	'''
	12. 用户列表
	:param session:
	:param userName:姓名
	:param status:状态 0-禁用|1-启用|2-冻结
	:param email:邮箱
	:param mobileNo:手机号
	:param roleId:角色id
	:param orgId:组织id
	:param pageNum:当前页
	:param pageSize:分页大小
	:return:
	'''
	url = host + '/yundeng/user/list'
	value = {"userName": userName, "oemail": email, "pageNum": pageNum, "pageSize": pageSize, "mobileno": mobileNo,
	         "orgId": orgId, "status": status, "roleId": roleId}
	raw = session.get(url, params=value)

	print(raw.json())

	return raw
