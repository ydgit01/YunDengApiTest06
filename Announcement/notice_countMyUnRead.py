#-*- coding:utf-8 -*-
"""
@note:
	1.1 统计当前登录用户公告未读数量
@author: Qred
@file: notice_countMyUnRead.py
@time: 2020/03/30
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def countMyUnRead(session):

	url = host + '/yundeng/notice/countMyUnRead'
	raw = session.get(url)

	print(raw.json())

	return raw