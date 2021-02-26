# -*- coding:utf-8 -*-
"""
@note:
@author: Qred
@file: microservice_del.py
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
	:param id: 服务ID 主键
	:return:
	'''
	url = host + '/yundeng/microservice/del/'
	url += str(id)

	raw = session.delete(url)

	print(raw.json())

	return raw
