#-*- coding:utf-8 -*-
"""
@note:
@author: Qred
@file: 4A_validateTicket.py
@time: 2020/03/25
"""
import requests

from Common import ReadConfig
from Common import cas_login_phone_checklastLogin as Login

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
print (host)

# headers = { 'Referer' : "http://yundeng-console.gw.test.com/?ticket=ST-592-zKLrZVO4FkHzCCOln-Val5YvJvU-aliyun-gtssolution-4a-cas-server-deployment-58fc86d65c-sm2s9"}

def GetInfo(session):

    url = host + '/yundeng/4A/validateTicket'
    jar = requests.cookies.RequestsCookieJar() # { 'Cookie':'SESSION=NzdkYzUwN2QtN2I4ZC00Y2U3LWJmZjItMjg4NDVhYzZlYjNj'}
    # jar.set("SESSION", session)
    session.headers.update(jar)
    raw = session.get(url)

    print(raw.text)

    # import urllib
    # req = urllib.request.Request(url, headers=Login.HEADER)
    # raw = session.open(req)
    # print (raw.read().decode())

    return session

temp = Login.GetSession()
session = temp.getCookie()
session = temp.getCookie()
session = GetInfo(session)
GetInfo(session)

# session = Login.loginV()
# print ("OK!!!")
# st = GetInfo(session)

# 'ticket=ST-592-zKLrZVO4FkHzCCOln-Val5YvJvU-aliyun-gtssolution-4a-cas-server-deployment-58fc86d65c-sm2s9'