#-*- coding:utf-8 -*-
"""
@note:
	2.2分类修改
@author: Qred
@file: microservice_class_edit.py
@time: 2020/04/02
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)


# print (host)

def classEdit(session, key='', name='ss', id=1, desc=''):
	'''

	:param session:
	:param key:服务唯一标识
	:param name:服务名称
	:param id:分类ID 主键
	:param desc:服务描述
	:return:
	'''
	url = host + '/yundeng/microservice/class/edit'
	value = {"key": key, "name": name, 'desc': desc, 'id': id}

	raw = session.post(url, data=value)

	print(raw.json())

	return raw