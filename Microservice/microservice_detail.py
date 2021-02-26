#-*- coding:utf-8 -*-
"""
@note:
	3.4服务详情
@author: Qred
@file: microservice_detail.py
@time: 2020/04/02
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)

# print (host)

def detail(session, id=1):
	'''

	:param session:
	:param id:服务ID 主键
	:return:
	'''
	url = host + '/yundeng/microservice/detail/'
	url += str(id)

	raw = session.delete(url)

	print(raw.json())

	return raw