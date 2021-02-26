#-*- coding:utf-8 -*-
"""
@note:
	22. 批量修改用户组织
@author: Qred
@file: user_userModificationOrganization.py
@time: 2020/04/08
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)

# print (host)

def userModificationOrganization(session, orgId='', empIdList='',reason='' ):
	'''
	22. 批量修改用户组织
	:param session:
	:param orgId:组织id
	:param empIdList:用户ids
	:param reason:修改原因
	:return:
	'''
	url = host + '/yundeng/user/userModificationOrganization'
	value = {"orgId": orgId, "empIdList": empIdList, "reason":reason}
	raw = session.post(url, data=value)

	print(raw.json())

	return raw