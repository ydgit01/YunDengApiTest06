#-*- coding:utf-8 -*-
"""
@note:
	9. 获取权限树
@author: Qred
@file: competence_getCompetenceList.py
@time: 2020/04/07
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def getCompetenceList(session):
	# 9. 获取权限树
	url = host + '/yundeng/competence/getCompetenceList'
	raw = session.get(url)

	print(raw.json())

	return raw
