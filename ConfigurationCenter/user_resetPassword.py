#-*- coding:utf-8 -*-
"""
@note:
	14. 重置密码
@author: Qred
@file: user_resetPassword.py
@time: 2020/04/08
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)

# print (host)

def resetPassword(session, operatorIds='', reason=''):
	'''
	14. 重置密码
	:param session:
	:param operatorIds:用户ids(多个用逗号隔开)
	:param reason: 修改原因
	:return:
	'''
	url = host + '/yundeng/user/resetPassword'
	value = {"operatorIds": operatorIds, "reason": reason }
	raw = session.post(url, params=value)

	print(raw.json())

	return raw
