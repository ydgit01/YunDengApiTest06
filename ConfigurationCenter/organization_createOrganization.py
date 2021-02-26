#-*- coding:utf-8 -*-
"""
@note:
	2. 创建组织
@author: Qred
@file: organization_createOrganization.py
@time: 2020/04/07
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def createOrganization(session, orgname = 'tets',parentorgid = 12, remark="scopeType"):
	'''
	2. 创建组织
	:param session:
	:param orgname: 组织名称
	:param parentorgid: 父组织id
	:param remark:备注
	:return:
	'''
	url = host + '/yundeng/organization/createOrganization'
	value = {"orgname": orgname,"parentorgid":parentorgid,"remark":remark}
	raw = session.post(url, data = value)

	print(raw.json())

	return raw