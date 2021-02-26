#-*- coding:utf-8 -*-
"""
@note:
@author: Qred
@file: organization_updateOrganization.py
@time: 2020/04/07
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def updateOrganization(session, orgname = 'tets', orgid = 23, parentorgid = 12, remark="", empIds="",reason=""):
	'''
	3. 编辑组织
	:param session:
	:param orgname:组织名称
	:param orgid:本级组织id
	:param parentorgid:父组织id
	:param remark:备注
	:param empIds:组织领导用户ids
	:param reason:修改原因
	:return:
	'''
	url = host + '/yundeng/organization/updateOrganization'
	value = {"orgname": orgname,"parentorgid":parentorgid, "orgid":orgid, "remark":remark, "reason":reason, "empIds":empIds}
	raw = session.post(url, data = value)

	print(raw.json())

	return raw