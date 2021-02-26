#-*- coding:utf-8 -*-
"""
@note:
	foura库数据查询
@author: Qred
@file: DB_foura.py
@time: 2020/04/01
"""

from Common import ConnectDB

foura = ConnectDB.DbManager(user='gtssolution', passwd='DevGtsSolution0731!', db='foura',
	             host='rm-8vbjo79cr5mc867pqxo.mysql.zhangbei.rds.aliyuncs.com', port=3306,)
foura.getConn()

def organizationByOrgname(name):
	# 根据组织名，查询组织信息
	sql = 'SELECT * FROM `org_organization` WHERE  orgname = "{name}";'.format(name=name)
	raw = foura.resultRow(1,sql)
	# print (raw)
	return raw

def organizationByOrgid(orgid):
	# 根据组织ID，查询组织信息
	sql = 'SELECT * FROM `org_organization` WHERE  orgid = {orgid};'.format(orgid=orgid)
	raw = foura.resultRow(1,sql)
	# print (raw)
	return raw

def organizationCount():
	# 获取组织数量
	sql = 'SELECT COUNT(*) countAllOrg FROM `org_organization` ;'
	raw = foura.resultRow(1, sql)
	# print (raw)
	return raw

def roleByRolename(roleName):
	# 根据角色名查找角色
	sql = 'SELECT * FROM `cap_role` WHERE  role_name = {roleName};'.format(roleName=roleName)
	raw = foura.resultRow(1, sql)
	print(raw)
	return raw

def roleByRoleid(role_id):
	# 根据角色名查找组织
	sql = 'SELECT * FROM `cap_role` WHERE  role_id = {role_id};'.format(role_id=role_id)
	raw = foura.resultRow(1, sql)
	# print(raw)
	return raw

def roleByNum(end=1, start = 0):
	# 获取角色列表
	sql = 'SELECT * FROM `cap_role` ORDER BY updatetime DESC LIMIT {start}, {end};'.format(start=start,end=end)
	raw = foura.resultRow(2, sql)
	# print(raw)
	return raw

def roleResauthByRoleid(role_id):
	# 获取角色权限列表
	sql = 'SELECT * FROM  `cap_resauth` WHERE  party_id = {} AND res_type = "function" ;'.format(role_id)
	raw = foura.resultRow(2, sql)
	# print(raw)
	return raw

def functionAll():
	sql = 'SELECT * FROM  `app_function` ;'
	raw = foura.resultRow(2, sql)
	print(raw)
	return raw

def userByUserid(userId):
	# 通过登录名查询用户信息
	sql = 'SELECT * FROM  `cap_user`  WHERE user_id = "{}" ;'.format(userId)
	raw = foura.resultRow(1, sql)
	print(raw)
	return raw

def userByOperatorId(operatorId):
	# 通过登录名查询用户信息
	sql = 'SELECT * FROM  `cap_user`  WHERE operatorIds = "{}" ;'.format(operatorId)
	raw = foura.resultRow(1, sql)
	print(raw)
	return raw

def userInfoByUserid(userId):
	# 通过登录名查询用户信息
	sql = 'SELECT * FROM  `org_employee`  WHERE userid = "{}" ;'.format(userId)
	raw = foura.resultRow(1, sql)
	print(raw)
	return raw

def userOrgByEmpid(empid):
	# 根据用户的员工id查询所在组织id
	sql = 'SELECT * FROM  `org_emporg`  WHERE empid = {};'.format(empid)
	raw = foura.resultRow(1, sql)
	print(raw)
	return raw

def userRoleByOperateid(operatorid):
	# 根据用户operateid 查询拥有的角色
	sql = 'SELECT * FROM `cap_partyauth` WHERE party_id = {};'.format(operatorid)
	raw = foura.resultRow(1, sql)
	print(raw)
	return raw

def userListByStatus(start, end, **kwargs):
	# 根据状态，获取的用户列表
	sql_base = 'SELECT org.`empid`, org.`oemail` email, org.`realname` userName, org.`userid` accountName, emp.`orgid` orgId, org.`mobileno` mobileNo,auth.`role_id` roleId, auth.`createtime`, org.`operatorid`, cap.`sex`, cap.`user_from` userFrom , cap.`lastlogin`, cap.`status` FROM  `cap_user` cap, org_employee org, `org_emporg` emp, `cap_partyauth` auth WHERE emp.`empid` = org.`empid` AND   org.`operatorid` = cap.`operator_id` AND auth.`party_id` = cap.`operator_id` ORDER BY auth.`createtime` DESC LIMIT {start} ,{end} '.format( start=start, end=end)
	sql_temp = 'SELECT * FROM ({}) {} WHERE `{}` = "{}"'
	length = kwargs.__len__()
	if length == 0:
		sql_end = sql_base
	else:
		for key, value in kwargs.items():
			if length == kwargs.__len__() :
				sql_end = sql_temp.format(sql_base,key, key, value)
			else:
				sql_end = sql_temp.format(sql_end, key, key, value)
			length -=1

	# print(sql_end)
	raw = foura.resultRow(2, sql_end)
	print(raw)
	return raw

def userCount():
	# 获取账号数量 countAllUser
	sql = 'SELECT COUNT(*) countAllUser FROM `cap_user` ;'
	raw = foura.resultRow(1, sql)
	# print (raw)
	return raw

# assert None != organizationByName("90"), "error1111"
# print (userInfoByUserid('lisi5')['birthdate'].strftime('%Y-%m-%d'))
# roleResauthByRoleid(310)
# print(userOrgByEmpid(1292)['empid'])
# userListByStatus(0, 100, status=1, roleId = 242, userName='云效测试2',mobileno='13611111112')