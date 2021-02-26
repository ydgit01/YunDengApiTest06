#-*- coding:utf-8 -*-
"""
@note:
	0.3获取工作项总览
@author: Qred
@file: index_getMyIssueSummary.py
@time: 2020/03/30
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def getMyIssueSummary(session):

	url = host + '/yundeng/index/getMyIssueSummary'
	raw = session.get(url)

	print(raw.json())

	return raw