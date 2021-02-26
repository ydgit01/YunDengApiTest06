# -*- coding:utf-8 -*-
"""
@note:
	13. 修改密码
@author: Qred
@file: user_updatePassword.py
@time: 2020/04/08
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)

# print (host)

def updatePassword(session, oldPassword='', password=''):
	'''
	13. 修改密码
	:param session:
	:param oldPassword:原始密码
	:param password: 新密码 *1 密码控制只能输入字母、数字、特殊符号(~!@#$%^&*()_+[]{}|\;:'",./<>?) *2 长度 6-16 位，必须包括字母、数字、特殊符号;
	:return:
	'''
	url = host + '/yundeng/user/updatePassword'
	value = {"oldPassword": oldPassword, "password": password}
	raw = session.post(url, params=value)

	print(raw.json())

	return raw
