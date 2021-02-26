#-*- coding:utf-8 -*-
"""
@note:
	0.4获取工作项详情
@author: Qred
@file: index_myIssueList.py
@time: 2020/03/30
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def myIssueList(session, type=1, stamp=1000):

	url = host + '/yundeng/index/myIssueList'
	value = {"type" : type, "stamp" : stamp}
	raw = session.get(url, params = value)

	print(raw.json())

	return raw