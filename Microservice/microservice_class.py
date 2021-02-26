#-*- coding:utf-8 -*-
"""
@note:
	2.3分类删除
@author: Qred
@file: microservice_class.py
@time: 2020/04/02
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)

# print (host)

def classDelete(session, id=1):
	'''

	:param session:
	:param id: 分类ID 主键
	:return:
	'''
	url = host + '/yundeng/microservice/class/'
	url += str(id)

	raw = session.delete(url)

	print(raw.json())

	return raw