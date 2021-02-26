#-*- coding:utf-8 -*-
"""
@note:
	角色管理
@author: Qred
@file: check_role.py
@time: 2020/04/09
"""
import sys

from Common import DB_foura
from Common import ToSize
from Common import cas_login_phone_checklastLogin
from ConfigurationCenter import role_save
from ConfigurationCenter import role_list
from ConfigurationCenter import role_getRoleTree
from ConfigurationCenter import competence_getCompetenceList
from ConfigurationCenter import role_roleAddPeopleList

class check_role():
	def __init__(self, session):
		self.session = session

	def t_save(self, roleName = 'tets', roleDesc = ''):
		# 创建角色
		role = role_save.save(self.session, roleName, roleDesc)
		assert "200" == role['statusCode'], "create role fail."

		# 数据库数据检查
		role_sql = DB_foura.roleByRolename(roleName)
		assert roleName == role_sql['role_name'], 'DB no data about {roleName}'.format(roleName=roleName)

		return role_sql

	def t_list(self, pageNum=1, pageSize=1000, roleName = ''):
		# 角色列表
		role = role_list.list(self.session, pageNum, pageSize, roleName)
		assert "200" == role['statusCode'], "get role list fail."

		# 接口返回角色总数
		totalCount = role['totalCount']
		# 接口返回角色的ids
		role_ids = ToSize.GetAggregate(role['datas'], 'roleId')

		start = (pageNum - 1) * pageSize
		end = pageNum * pageSize
		role_sql = DB_foura.roleByNum(end, start)
		# 数据库返回角色总数
		totalCount_sql = role_sql.__len__()
		assert totalCount == totalCount_sql, 'api totalCount({}) is different from sql totalCount({}) '.format(totalCount, totalCount_sql)

		# 数据库返回数据
		role_sql_role_ids = ToSize.GetAggregate(role_sql, 'role_id')
		result = role_ids.symmetric_difference(role_sql_role_ids)
		assert 0 == result.__len__(), 'api data symmetric_difference sql data : {}'.format(result)

	def t_changeRole(self, roleName = 'tets', roleDesc = '', roleId = '', reason='', funccode=''):
		# 编辑角色
		role = role_save.save(self.session, roleName, roleDesc, roleId, reason, funccode)
		assert "200" == role['statusCode'], "change role fail."
		assert roleId == role['data']['roleId'], "role id fail."

		# 角色表数据
		role_sql = DB_foura.roleByRoleid(roleId)
		assert roleName == role_sql['role_name'], 'DB no data about {roleName}'.format(roleName=roleName)

		if roleDesc is not "":
			assert roleDesc == role_sql['role_desc'], 'DB no data about {roleDesc}'.format(roleDesc=roleDesc)

		# 角色权限
		role_rsauth_sql = DB_foura.roleResauthByRoleid(roleId)
		if funccode is not "":
			# 将funccode转换为集合
			list_funccode = funccode.split(',')
			Aggregate = set(list_funccode)
			assert list_funccode.__len__() == Aggregate.__len__()

			# 数据库中存储的角色权限
			Aggregate_sql = ToSize.GetAggregate(role_rsauth_sql, 'res_id')
			result = Aggregate.symmetric_difference(Aggregate_sql)
			assert 0 == result.__len__(), 'params funccode symmetric_difference sql funccode : {}'.format(result)

		if reason is not "":
			pass

	def t_getRoleTree(self, roleId=1):
		# 获取角色详情
		role = role_getRoleTree.getRoleTree(self.session, roleId)
		assert "200" == role['statusCode'], "create role fail."

		# 角色信息
		role_capRole = role['data']['capRole']
		assert roleId == role_capRole['roleId'], "role id fail."

		roleName = role_capRole['roleName']
		role_sql = DB_foura.roleByRoleid(roleId)
		assert roleName == role_sql['role_name'], 'DB no data about {roleName}'.format(roleName=roleName)

		# 角色的权限
		# 接口
		Aggregate = ToSize.GetAggregate(role_capRole['selectedResources'], 'funccode')
		# 数据库
		role_rsauth_sql = DB_foura.roleResauthByRoleid(roleId)
		Aggregate_sql = ToSize.GetAggregate(role_rsauth_sql, 'res_id')
		result = Aggregate.symmetric_difference(Aggregate_sql)
		assert 0 == result.__len__(), 'api funccode symmetric_difference sql funccode : {}'.format(result)

		# 未知返回数据
		role_dict = role['data']['dict']

		role_list = role['data']['list']

	def t_getCompetenceList(self):
		# 获取权限树
		data = competence_getCompetenceList.getCompetenceList(self.session)
		assert "200" == data['statusCode'], "create role fail."

		Aggregate = ToSize.GetAggregate(data['data']['children'], 'funccode')
		# Aggregate_sql = {'100', '101', '102', '103', '104', '105', '106', '107', '128' }
		Aggregate_sql = DB_foura.functionAll()
		Aggregate_sql = ToSize.GetAggregate(Aggregate_sql, 'funccode')
		result = Aggregate.symmetric_difference(Aggregate_sql)
		assert 0 == result.__len__(), 'api funccode symmetric_difference data funccode : {}'.format(result)

	def t_roleAddPeopleList(self, userIds='', roleId='' ):
		# 角色添加人员
		role = role_roleAddPeopleList.roleAddPeopleList(self.session, userIds, roleId)
		assert "200" == role['statusCode'], "{} fail.".format(sys._getframe().f_code.co_name)

		if isinstance(userIds,list):
			for userId in userIds :
				roleId_sql = DB_foura.userRoleByOperateid(userId)
				assert roleId == roleId_sql['role_id'], 'roleId({}) is different from sql({}).'.format(roleId , roleId_sql['role_id'])
		else:
			print("{} fail.".format(sys._getframe().f_code.co_name))


