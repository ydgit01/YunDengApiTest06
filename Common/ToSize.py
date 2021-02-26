#-*- coding:utf-8 -*-
"""
@note:
	将数据转换成集合
@author: Qred
@file: ToSize.py
@time: 2020/04/09
"""
def GetAggregate(kw, key):
	# 转换为集合
	temp = []
	for dic in kw :
		temp.append(dic[key])

	Aggregate = set(temp)
	return Aggregate


# if __name__ == '__main__':
    # ls  = [
    #     {
    #         "appid": 0,
    #         "appname": "",
    #         "createtime": None,
    #         "createuser": "",
    #         "dictid": 0,
    #         "empCount": 1,
    #         "key": 0,
    #         "roleCode": "1",
    #         "roleDesc": "公共管理员2223",
    #         "roleId": "274",
    #         "roleLevel": "",
    #         "roleName": "公共管理员",
    #         "roleType": "",
    #         "roleTypeName": "",
    #         "selectedResources": [],
    #         "state": "1",
    #         "status": "",
    #         "tenantId": ""
    #     },
    #     {
    #         "appid": 0,
    #         "appname": "",
    #         "createtime": None,
    #         "createuser": "",
    #         "dictid": 0,
    #         "empCount": 1,
    #         "key": 0,
    #         "roleCode": "1",
    #         "roleDesc": "基础管理员",
    #         "roleId": "273",
    #         "roleLevel": "",
    #         "roleName": "基础管理员",
    #         "roleType": "",
    #         "roleTypeName": "",
    #         "selectedResources": [],
    #         "state": "1",
    #         "status": "",
    #         "tenantId": ""
    #     },
    #     {
    #         "appid": 0,
    #         "appname": "",
    #         "createtime": None,
    #         "createuser": "",
    #         "dictid": 0,
    #         "empCount": 0,
    #         "key": 0,
    #         "roleCode": "1",
    #         "roleDesc": "基础管理员2",
    #         "roleId": "272",
    #         "roleLevel": "",
    #         "roleName": "基础管理员",
    #         "roleType": "",
    #         "roleTypeName": "",
    #         "selectedResources": [],
    #         "state": "1",
    #         "status": "",
    #         "tenantId": ""
    #     }]
	#
    # ls2 = [
	#     {
	# 	    "appid": 0,
	# 	    "appname": "",
	# 	    "createtime": None,
	# 	    "createuser": "",
	# 	    "dictid": 0,
	# 	    "empCount": 1,
	# 	    "key": 0,
	# 	    "roleCode": "1",
	# 	    "roleDesc": "公共管理员2223",
	# 	    "roleId": "274",
	# 	    "roleLevel": "",
	# 	    "roleName": "公共管理员",
	# 	    "roleType": "",
	# 	    "roleTypeName": "",
	# 	    "selectedResources": [],
	# 	    "state": "1",
	# 	    "status": "",
	# 	    "tenantId": ""
	#     },
	#     {
	# 	    "appid": 0,
	# 	    "appname": "",
	# 	    "createtime": None,
	# 	    "createuser": "",
	# 	    "dictid": 0,
	# 	    "empCount": 1,
	# 	    "key": 0,
	# 	    "roleCode": "1",
	# 	    "roleDesc": "基础管理员",
	# 	    "roleId": "273",
	# 	    "roleLevel": "",
	# 	    "roleName": "基础管理员",
	# 	    "roleType": "",
	# 	    "roleTypeName": "",
	# 	    "selectedResources": [],
	# 	    "state": "1",
	# 	    "status": "",
	# 	    "tenantId": ""
	#     },
	#     {
	# 	    "appid": 0,
	# 	    "appname": "",
	# 	    "createtime": None,
	# 	    "createuser": "",
	# 	    "dictid": 0,
	# 	    "empCount": 0,
	# 	    "key": 0,
	# 	    "roleCode": "1",
	# 	    "roleDesc": "基础管理员2",
	# 	    "roleId": "272",
	# 	    "roleLevel": "",
	# 	    "roleName": "基础管理员",
	# 	    "roleType": "",
	# 	    "roleTypeName": "",
	# 	    "selectedResources": [],
	# 	    "state": "1",
	# 	    "status": "",
	# 	    "tenantId": ""
	#     }]
    # se1 = GetAggregate(ls, 'roleDesc')
    # se2 = GetAggregate(ls2, 'roleDesc')
    # result = se1.symmetric_difference(se2)
    # print (result.__len__())

