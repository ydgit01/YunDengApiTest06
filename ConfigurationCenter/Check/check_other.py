#-*- coding:utf-8 -*-
"""
@note:
	配置中心其他的接口
@author: Qred
@file: check_other.py
@time: 2020/04/13
"""
import sys

from Common import DB_foura
from Common import ToSize
from Common import cas_login_phone_checklastLogin
from ConfigurationCenter import stat_onlineSituation

class check_user():
	def __init__(self, session):
		self.session = session

	def t_onlineSituation(self):
		situation = stat_onlineSituation.onlineSituation(self.session)
		assert "200" == situation['statusCode'], "{} fail.".format(sys._getframe().f_code.co_name)

		data = situation['data']
		countAllOrg = DB_foura.organizationCount()['countAllOrg']
		assert data['countAllOrg'] == countAllOrg,'countAllOrg api({}) is different from sql({}).'.format(data['countAllOrg'] , countAllOrg)

		countAllUser =DB_foura.userCount()['countAllUser']
		assert data['countAllUser'] == countAllUser, 'countAllOrg api({}) is different from sql({}).'.format(data['countAllUser'], countAllUser)