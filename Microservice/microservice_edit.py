# -*- coding:utf-8 -*-
"""
@note:
	3.2服务修改
@author: Qred
@file: microservice_edit.py
@time: 2020/04/02
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)


# print (host)

def edit(session, key='', name='ss', id=1,type='', microserviceCreateType='', modelCreateType='', desc='', viewCreateType='',
         parentId='', microserviceClassifyId='', gitVersion=''):
	'''

	:param session:
	:param key:服务唯一标识
	:param name:服务名称
	:param id:服务ID 主键
	:param type:微服务类型 bdomain 业务微服务/子领域  undary 边界微服务 siness 商业能力微服务 foreground 前台微服务
	:param microserviceCreateType:微服务创建方式 online 线上（web前端写死该值） offline 线下（插件侧写死该值）
	:param modelCreateType:模型实体创建方式 online 线上 offline 线下
	:param desc:服务描述
	:param viewCreateType:视图创建方式 online 线上 offline 线下
	:param parentId: 父级服务ID 商业能力微服务中，bundle对应的父级spi【多态场景】
	:param microserviceClassifyId: 服务所属分类
	:param gitVersion: 版本号
	:return:
	'''
	url = host + '/yundeng/microservice/edit/'
	url += str(id)
	value = {"id": id, "key": key, "name": name, "desc": desc, "type": type, "modelCreateType": modelCreateType,
	         "microserviceCreateType": microserviceCreateType, "viewCreateType": viewCreateType, "parentId": parentId,
	         "microserviceClassifyId": microserviceClassifyId, "version": gitVersion}

	raw = session.post(url, data=value)

	print(raw.json())

	return raw
