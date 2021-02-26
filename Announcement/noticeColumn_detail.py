#-*- coding:utf-8 -*-
"""
@note:
	2.2 查看公告栏目详情
@author: Qred
@file: noticeColumn_detail.py
@time: 2020/03/31
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)
# print (host)

def detail(session, Id= 1):

	# noticeState 公告状态(1-已发布,2-下线)
	url = host + '/yundeng/noticeColumn/detail'
	url += str(Id)
	raw = session.get(url)

	print(raw.json())