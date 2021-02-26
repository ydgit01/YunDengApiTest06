#-*- coding:utf-8 -*-
"""
@note:
	获取当前用户拥有的菜单权限
@author: Qred
@file: userAuth_queryUserOwnRole.py
@time: 2020/04/07
"""

from Common import ReadConfig
from Common import cas_login_phone_checklastLogin as Login
from ConfigurationCenter import yundeng_4A_validateTicket as Ticket

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
print (host)


def queryUserOwnRole(session):
    # 0.3 获取当前用户拥有的菜单权限
    url = host + '/yundeng/userAuth/queryUserOwnRole'
    raw = session.get(url)

    print (raw.json())

    return raw
