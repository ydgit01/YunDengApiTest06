#-*- coding:utf-8 -*-
"""
@note:
	18. 获取组织详情
@author: Qred
@file: organization_detail.py
@time: 2020/04/08
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)

# print (host)

def detail(session, orgId= '' ):
	'''
	18. 获取组织详情
	:param session:
	:param orgId:组织id
	:return:
	'''
	url = host + '/yundeng/organization/detail/'
	url += str(orgId)
	raw = session.get(url)

	print(raw.json())

	return raw