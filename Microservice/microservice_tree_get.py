#-*- coding:utf-8 -*-
"""
@note:
	1.1服务总览树查询
@author: Qred
@file: microservice_tree_get.py
@time: 2020/04/02
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def treeGet(session, classTypes=["domain","business"], searchKey=''):
	'''

	:param session:
	:param classTypes:分类类型  domain 领域服务； business 商业能力服务； foreground 敏捷前台服务;
	:param searchKey:搜索关键字，根据关键字模糊匹配分类名称、服务名称
	:return:
	'''
	url = host + '/yundeng/microservice/tree/get'
	value = {"classTypes": classTypes, "searchKey": searchKey}

	raw = session.get(url, params=value)

	print(raw.json())

	return raw