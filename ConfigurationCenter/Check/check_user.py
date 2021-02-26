# -*- coding:utf-8 -*-
"""
@note:
	账号相关接口测试
@author: Qred
@file: check_user.py
@time: 2020/04/10
"""
import sys

from Common import DB_foura
from Common import ToSize
from Common import cas_login_phone_checklastLogin
from ConfigurationCenter import user_add
from ConfigurationCenter import user_modify
from ConfigurationCenter import user_list
from ConfigurationCenter import user_updatePassword
from ConfigurationCenter import user_resetPassword
from ConfigurationCenter import user_updateState
from ConfigurationCenter import user_detail
from ConfigurationCenter import user_listAll
from ConfigurationCenter import user_modifyUserRoles
from ConfigurationCenter import user_userModificationOrganization


class check_user():
	def __init__(self, session):
		self.session = session

	def t_add(self, userName='12', accountName='qreds', email='12111@163.com', orgidList='123', mobileNo='15588809999',
	          roleIds=87, sex=0, birthdate='', dingding='', graduateSchool='', graduateTime='', education='',
	          empcode='', otel='', remark='', major='', haddress=''):
		# 创建用户
		user = user_add.add(self.session, userName, accountName, email, orgidList, mobileNo, roleIds, sex, birthdate,
		                    dingding, graduateSchool, graduateTime, education, empcode, otel, remark, major, haddress)
		assert "200" == user['statusCode'], "create user fail."

		user_sql = DB_foura.userByUserid(accountName)
		assert userName == user_sql['user_name'], 'sql-user data is not : {} . '.format(userName)
		assert email == user_sql['email'], 'sql-user data is not : {} . '.format(email)
		if sex is not "":
			assert sex == user_sql['sex'], 'sql-user data is not : {} . '.format(sex)

		# db中员工信息
		user_info_sql = DB_foura.userInfoByUserid(accountName)
		assert userName == user_info_sql['realname'], 'sql-info data is not : {} . '.format(userName)
		assert mobileNo == user_info_sql['mobileno'], 'sql-info data is not : {} . '.format(mobileNo)

		if birthdate is not "":
			birthdate = birthdate.split("T")[0]
			assert birthdate == user_info_sql['birthdate'].strftime('%Y-%m-%d'), 'sql-info data is not : {} . '.format(
				birthdate)
		if dingding is not "":
			assert dingding == user_info_sql['dingding'], 'sql-info data is not : {} . '.format(dingding)
		if graduateSchool is not "":
			assert graduateSchool == user_info_sql['graduate_school'], 'sql-info data is not : {} . '.format(graduateSchool)
		if graduateTime is not "":
			graduateTime = birthdate.split("T")[0]
			assert graduateTime == user_info_sql['graduate_time'].strftime(
				'%Y-%m-%d'), 'sql-info data is not : {} . '.format(graduateTime)
		if education is not "":
			assert education == user_info_sql['education'], 'sql-info data is not : {} . '.format(education)
		if empcode is not "":
			assert empcode == user_info_sql['empcode'], 'sql-info data is not : {} . '.format(empcode)
		if otel is not "":
			assert otel == user_info_sql['otel'], 'sql-info data is not : {} . '.format(otel)
		if major is not "":
			assert major == user_info_sql['major'], 'sql-info data is not : {} . '.format(major)
		if haddress is not "":
			assert haddress == user_info_sql['haddress'], 'sql-info data is not : {} . '.format(haddress)
		if remark is not "":
			assert remark == user_info_sql['remark'], 'sql-info data is not : {} . '.format(remark)

		# 用户所属组织
		empid = user_info_sql['empid']
		user_org_sql = DB_foura.userOrgByEmpid(empid)
		assert orgidList == user_org_sql['orgid'], 'sql-user-employee data is not : {} . '.format(orgidList)

		# 用户所属角色
		operatorid = user_info_sql['operatorid']
		user_role_sql = DB_foura.userRoleByOperateid(operatorid)
		assert roleIds == user_role_sql['role_id'], 'sql-user-role data is not : {} . '.format(roleIds)

	def t_modify(self, userName='12', empid='111', accountName='qreds', email='12111@163.com', orgidList='123',
	             mobileNo='15588809999', roleIds=87, sex=0, birthdate='', dingding='', graduateSchool='',
	             graduateTime='', education='', empcode='', otel='', remark='', major='', haddress=''):
		# 用户修改信息
		user = user_modify.modify(self.session, userName, empid, accountName, email, orgidList, mobileNo, roleIds, sex,
		                       birthdate, dingding, graduateSchool, graduateTime, education, empcode, otel, remark,
		                       major, haddress)
		assert "200" == user['statusCode'], "modify user fail."

		user_sql = DB_foura.userByUserid(accountName)
		assert userName == user_sql['user_name'], 'sql-user data is not : {} . '.format(userName)
		assert email == user_sql['email'], 'sql-user data is not : {} . '.format(email)
		if sex is not "":
			assert sex == user_sql['sex'], 'sql-user data is not : {} . '.format(sex)

		# db中员工信息
		user_info_sql = DB_foura.userInfoByUserid(accountName)
		assert userName == user_info_sql['realname'], 'sql-info data is not : {} . '.format(userName)
		assert mobileNo == user_info_sql['mobileno'], 'sql-info data is not : {} . '.format(mobileNo)

		if birthdate is not "":
			birthdate = birthdate.split("T")[0]
			assert birthdate == user_info_sql['birthdate'].strftime('%Y-%m-%d'), 'sql-info data is not : {} . '.format(
				birthdate)
		if dingding is not "":
			assert dingding == user_info_sql['dingding'], 'sql-info data is not : {} . '.format(dingding)
		if graduateSchool is not "":
			assert graduateSchool == user_info_sql['graduate_school'], 'sql-info data is not : {} . '.format(
				graduateSchool)
		if graduateTime is not "":
			graduateTime = birthdate.split("T")[0]
			assert graduateTime == user_info_sql['graduate_time'].strftime(
				'%Y-%m-%d'), 'sql-info data is not : {} . '.format(graduateTime)
		if education is not "":
			assert education == user_info_sql['education'], 'sql-info data is not : {} . '.format(education)
		if empcode is not "":
			assert empcode == user_info_sql['empcode'], 'sql-info data is not : {} . '.format(empcode)
		if otel is not "":
			assert otel == user_info_sql['otel'], 'sql-info data is not : {} . '.format(otel)
		if major is not "":
			assert major == user_info_sql['major'], 'sql-info data is not : {} . '.format(major)
		if haddress is not "":
			assert haddress == user_info_sql['haddress'], 'sql-info data is not : {} . '.format(haddress)
		if remark is not "":
			assert remark == user_info_sql['remark'], 'sql-info data is not : {} . '.format(remark)

		# 用户所属组织
		empid = user_info_sql['empid']
		user_org_sql = DB_foura.userOrgByEmpid(empid)
		assert orgidList == user_org_sql['orgid'], 'sql-user-employee data is not : {} . '.format(orgidList)

		# 用户所属角色
		operatorid = user_info_sql['operatorid']
		user_role_sql = DB_foura.userRoleByOperateid(operatorid)
		assert roleIds == user_role_sql['role_id'], 'sql-user-role data is not : {} . '.format(roleIds)

	def t_list(self, userName='', status=1, email='', mobileNo='', roleId='', orgId='', pageNum=1, pageSize=10):
		# 用户列表
		users = user_list.list(self.session, userName, status, email, mobileNo, roleId, orgId, pageNum, pageSize)
		assert "200" == users['statusCode'], "get users list fail."

		sql_params = {}
		if userName is not "":
			sql_params['userName'] = userName
		if status is not "":
			sql_params['status'] = status
		if email is not "":
			sql_params['oemail'] = email
		if mobileNo is not "":
			sql_params['mobileNo'] = mobileNo
		if roleId is not "":
			sql_params['roleId'] = roleId
		if orgId is not "":
			sql_params['orgId'] = orgId
		start = (pageNum - 1) * pageSize
		# sql_params['start'] = start
		end = pageNum * pageSize
		# sql_params['end'] = end

		# 取出所有数据
		users_all_sql = DB_foura.userListByStatus(0, 1000, **sql_params)
		users_all_sql_count = users_all_sql.__len__()
		user_totalCount = users['totalCount']
		assert user_totalCount == users_all_sql_count, 'totalCount api({}) is different from sql({}).'.format(user_totalCount, users_all_sql_count)

		users = users['datas']
		users_sql = DB_foura.userListByStatus(start, end, **sql_params)

		for i in pageSize:
			user = users[i]
			user_sql = users_sql[i]

			assert user['empid'] == user_sql['empid'], 'empid api({}) is different from sql({}).'.format(user['empid'] , user_sql['empid'])
			assert user['oemail'] == user_sql['oemail'], 'oemail api({}) is different from sql({}).'.format(user['oemail'] , user_sql['oemail'])
			assert user['gender'] == str(user_sql['gender']), 'gender api({}) is different from sql({}).'.format(user['gender'] , user_sql['gender'])
			assert user['accountName'] == user_sql['accountName'], 'accountName api({}) is different from sql({}).'.format(user['accountName'] , user_sql['accountName'])
			# 最后一次登录
			assert user['lastlogin'] == user_sql['lastlogin'].strftime('%Y-%m-%d %H:%M:%S'), 'lastlogin api({}) is different from sql({}).'.format(user['lastlogin'] , user_sql['lastlogin'].strftime('%Y-%m-%d %H:%M:%S'))
			assert user['mobileno'] == user_sql['mobileno'], 'mobileno api({}) is different from sql({}).'.format(user['mobileno'] , user_sql['mobileno'])
			assert user['userName'] == user_sql['userName'], 'userName api({}) is different from sql({}).'.format(user['userName'] , user_sql['userName'])
			# 创建时间
			assert user['createTime'] == user_sql['createTime'].strftime('%Y-%m-%d %H:%M:%S'), 'createTime api({}) is different from sql({}).'.format(user['createTime'] , user_sql['createTime'].strftime('%Y-%m-%d %H:%M:%S'))
			assert user['operatorId'] == user_sql['operatorId'], 'operatorId api({}) is different from sql({}).'.format(user['operatorId'] , user_sql['operatorId'])
			assert user['status'] == user_sql['status'], 'status api({}) is different from sql({}).'.format(user['status'] , user_sql['status'])
			assert user['userFrom'] == user_sql['userFrom'], 'userFrom api({}) is different from sql({}).'.format(user['userFrom'] , user_sql['userFrom'])


			# orgNameList
			orgNameList_sql = DB_foura.organizationByOrgid(user_sql['orgId'])
			assert user['orgNameList'] == orgNameList_sql, 'orgNameList api({}) is different from sql({}).'.format(user['orgNameList'] , orgNameList_sql)

	def t_updatePassword(self, oldPassword='', password=''):
		# 修改用户密码
		user = user_updatePassword.updatePassword(self.session, oldPassword, password)
		assert "200" == user['statusCode'], "user updatePassword fail."

		# 需要使用登录验证

	def t_resetPassword(self, operatorIds='', reason=''):
		# 重置用户密码
		user = user_resetPassword.resetPassword(self.session, operatorIds, reason)
		assert "200" == user['statusCode'], "user resetPassword fail."

		# 需要使用登录验证

	def t_updateState(self, operatorIds='', status='', reason=''):
		# 更改用户状态
		user = user_updateState.updateState(self.session, operatorIds, status, reason)
		assert "200" == user['statusCode'], "{} fail.".format(sys._getframe().f_code.co_name )

		# 转换为列表
		operatorIds = operatorIds.split(',')
		for operatorId in operatorIds :
			status_sql = DB_foura.userByOperatorId(operatorId)['status']
			assert status == status_sql, 'status api({}) is different from sql({}).'.format(status , status_sql)

	# def t_detail(self, operatorIds='' ):
	# 	# 用户详情
	# 	user = user_detail.detail(self.session, operatorIds)

	def t_listAll(self, orgId='', roleId='' ):
		users = user_listAll.listAll(self.session, orgId, roleId)
		assert "200" == users['statusCode'], "{} fail.".format(sys._getframe().f_code.co_name)

		# 取出所有数据
		users_all_sql = DB_foura.userListByStatus(0, 1000, status = 1)
		users_all_sql_count = users_all_sql.__len__()

		for i in users_all_sql_count:
			user = users[i]
			user_sql = users_all_sql[i]

			assert user['empid'] == user_sql['empid'], 'empid api({}) is different from sql({}).'.format(user['empid'] , user_sql['empid'])
			assert user['oemail'] == user_sql['oemail'], 'oemail api({}) is different from sql({}).'.format(user['oemail'] , user_sql['oemail'])
			assert user['gender'] == str(user_sql['gender']), 'gender api({}) is different from sql({}).'.format(user['gender'] , user_sql['gender'])
			assert user['accountName'] == user_sql['accountName'], 'accountName api({}) is different from sql({}).'.format(user['accountName'] , user_sql['accountName'])
			# 最后一次登录
			# assert user['lastlogin'] == user_sql['lastlogin'].strftime('%Y-%m-%d %H:%M:%S'), 'lastlogin api({}) is different from sql({}).'.format(user['lastlogin'] , user_sql['lastlogin'].strftime('%Y-%m-%d %H:%M:%S'))
			assert user['mobileno'] == user_sql['mobileno'], 'mobileno api({}) is different from sql({}).'.format(user['mobileno'] , user_sql['mobileno'])
			assert user['userName'] == user_sql['userName'], 'userName api({}) is different from sql({}).'.format(user['userName'] , user_sql['userName'])
			# 创建时间
			# assert user['createTime'] == user_sql['createTime'].strftime('%Y-%m-%d %H:%M:%S'), 'createTime api({}) is different from sql({}).'.format(user['createTime'] , user_sql['createTime'].strftime('%Y-%m-%d %H:%M:%S'))
			assert user['operatorId'] == user_sql['operatorId'], 'operatorId api({}) is different from sql({}).'.format(user['operatorId'] , user_sql['operatorId'])
			assert user['status'] == user_sql['status'], 'status api({}) is different from sql({}).'.format(user['status'] , user_sql['status'])
			assert user['userFrom'] == user_sql['userFrom'], 'userFrom api({}) is different from sql({}).'.format(user['userFrom'] , user_sql['userFrom'])

			# orgNameList
			orgNameList_sql = DB_foura.organizationByOrgid(user_sql['orgId'])
			assert user['orgNameList'] == orgNameList_sql, 'orgNameList api({}) is different from sql({}).'.format(user['orgNameList'] , orgNameList_sql)

	def t_modifyUserRoles(self, operatorIdList='', roleId='' ):
		# 批量新修改用户角色
		users = user_modifyUserRoles.modifyUserRoles(self.session, operatorIdList, roleId)
		assert "200" == users['statusCode'], "{} fail.".format(sys._getframe().f_code.co_name)

		for operatorId in operatorIdList:
			roleId_sql = DB_foura.userRoleByOperateid(operatorId)
			assert roleId == roleId_sql['role_id'], 'roleId({}) is different from sql({}).'.format(roleId , roleId_sql['role_id'])

	def t_userModificationOrganization(self, orgId='', empIdList='',reason='' ):
		# 批量修改用户组织
		users = user_userModificationOrganization.userModificationOrganization(self.session, orgId, empIdList, reason)
		assert "200" == users['statusCode'], "{} fail.".format(sys._getframe().f_code.co_name)

		for empId in empIdList:
			orgId_sql = DB_foura.userOrgByEmpid(empId)
			assert orgId == orgId_sql['orgid'], 'orgId({}) is different from sql({}).'.format(orgId, orgId_sql['orgid'])

