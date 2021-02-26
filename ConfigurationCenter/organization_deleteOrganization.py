#-*- coding:utf-8 -*-
"""
@note:
@author: Qred
@file: organization_deleteOrganization.py
@time: 2020/04/07
"""

from Common import ReadConfig
from Common import cas_login_phone_checklastLogin as Login

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
print (host)


def deleteOrganization(session, orgid=23 ):
	# 4. 删除组织
    url = host + '/yundeng/organization/deleteOrganization'
    value =  { "orgid" : orgid}
    raw = session.get(url, params = value)

    print (raw.json())

    return raw