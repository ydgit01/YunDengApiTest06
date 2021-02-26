#-*- coding:utf-8 -*-
"""
@note:
	0.5获取我的收藏
@author: Qred
@file: index_getMyWatched.py
@time: 2020/03/30
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def getMyWatched(session):

	url = host + '/yundeng/index/getMyWatched'
	raw = session.get(url)

	print(raw.json())

	return raw