#-*- coding:utf-8 -*-
"""
@note:
@author: Qred
@file: user_updateState.py
@time: 2020/04/08
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)

# print (host)

def updateState(session, operatorIds='', status='', reason=''):
	'''
	15. 修改用户状态
	:param session:
	:param operatorIds:用户ids(多个用逗号隔开)
	:param status:0-禁用|1-启用|2-冻结
	:param reason: 修改原因
	:return:
	'''
	url = host + '/yundeng/user/updateState'
	value = {"operatorIds": operatorIds, "status":status, "reason": reason }
	raw = session.post(url, params=value)

	print(raw.json())

	return raw
