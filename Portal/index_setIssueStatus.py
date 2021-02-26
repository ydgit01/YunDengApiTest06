#-*- coding:utf-8 -*-
"""
@note:
	0.7修改工作项状态
@author: Qred
@file: index_setIssueStatus.py
@time: 2020/03/30
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def setIssueStatus(session, issueId=1, statusId=0):

	url = host + '/yundeng/index/setIssueStatus/'
	url += str(issueId) + str(statusId)
	raw = session.get(url)

	print(raw.json())

	return raw