#-*- coding:utf-8 -*-
"""
@note:
	获取用户信息
@author: Qred
@file: 4A_getUserInfo.py
@time: 2020/03/25
"""

from Common import ReadConfig
from Common import cas_login_phone_checklastLogin as Login
from ConfigurationCenter import yundeng_4A_validateTicket as Ticket

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
print (host)


def GetInfo(session):

    url = host + '/yundeng/4A/getUserInfo'
    raw = session.get(url)

    print (raw.json())

    return raw

if __name__ == '__main__':
    temp = Login.GetSession()
    session = temp.getCookie()
    Ticket.GetInfo(session)
    raw = GetInfo(session)
    # print(session.get(raw['data']).text)