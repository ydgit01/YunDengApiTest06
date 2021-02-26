#-*- coding:utf-8 -*-
"""
@note:
	6. 角色列表
@author: Qred
@file: role_list.py
@time: 2020/04/07
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def list(session, pageNum=1, pageSize=10, roleName = ''):

	url = host + '/yundeng/role/list'
	value = {"roleName": roleName,"pageNum":pageNum, "pageSize":pageSize }
	raw = session.get(url, params = value)

	print(raw.json())

	return raw