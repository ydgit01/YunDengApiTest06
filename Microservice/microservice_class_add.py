#-*- coding:utf-8 -*-
"""
@note:
	2.1分类创建
@author: Qred
@file: microservice_class_add.py
@time: 2020/04/02
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def classAadd(session, key='', name='ss', type='domain', desc = ''):
	'''

	:param session:
	:param key:服务分类唯一标识
	:param name:服务分类名称
	:param desc:服务分类描述
	:param type:分类类型  domain 领域服务； business 商业能力服务； foreground 敏捷前台服务;
	:return:
	'''
	url = host + '/yundeng/microservice/class/add'
	value = {"key": key, "name": name, 'desc': desc,'type':type}

	raw = session.post(url, data=value)

	print(raw.json())

	return raw