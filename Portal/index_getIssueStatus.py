#-*- coding:utf-8 -*-
"""
@note:
	0.6获取工作项状态
@author: Qred
@file: index_getIssueStatus.py
@time: 2020/03/30
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def getIssueStatus(session, issueId=1):

	url = host + '/yundeng/index/myIssueList/'
	url += str(issueId)
	raw = session.get(url)

	print(raw.json())

	return raw