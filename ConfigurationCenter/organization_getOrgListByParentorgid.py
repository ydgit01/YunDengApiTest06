#-*- coding:utf-8 -*-
"""
@note:
@author: Qred
@file: organization_getOrgListByParentorgid.py
@time: 2020/04/07
"""

from Common import ReadConfig
from Common import cas_login_phone_checklastLogin as Login

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
print (host)


def getOrgListByParentorgid(session, pageNum = 1, pageSize = 10, parentId=23  ):
	# 4. 删除组织
    url = host + '/yundeng/organization/getOrgListByParentorgid'
    value =  { "parentId" : parentId, "pageNum" : pageNum, "pageSize" : pageSize}
    raw = session.post(url, params = value)

    print (raw.json())

    return raw