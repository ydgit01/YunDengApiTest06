# -*- coding:utf-8 -*-
"""
@note:
	1.1 获取全量组织树列表
@author: Qred
@file: organization_getOrganizationList.py
@time: 2020/04/07
"""

from Common import ReadConfig
from Common import cas_login_phone_checklastLogin as Login
from ConfigurationCenter import yundeng_4A_validateTicket as Ticket

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
print(host)


def getOrganizationList(session):
	'''
	1.1 获取全量组织树列表
	:param session:
	:return:
	'''
	url = host + '/yundeng/organization/getOrganizationList'
	raw = session.get(url)

	print(raw.json())

	return raw
