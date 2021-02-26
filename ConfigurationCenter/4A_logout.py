#-*- coding:utf-8 -*-
"""
@note:
	0.4 退出登录
@author: Qred
@file: 4A_logout.py
@time: 2020/04/07
"""

from Common import ReadConfig
from Common import cas_login_phone_checklastLogin as Login
from ConfigurationCenter import yundeng_4A_validateTicket as Ticket

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
print (host)


def logout(session):
    # 退出登录
    url = host + '/yundeng/4A/logout'
    raw = session.get(url)

    print (raw.json())

    return raw
