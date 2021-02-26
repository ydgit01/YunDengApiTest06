#-*- coding:utf-8 -*-
"""
@note:
	组织相关的测试
@author: Qred
@file: check_organization.py
@time: 2020/04/09
"""
from Common import cas_login_phone_checklastLogin
from Common import DB_foura
from ConfigurationCenter import organization_createOrganization
from ConfigurationCenter import organization_updateOrganization
from ConfigurationCenter import organization_deleteOrganization
from ConfigurationCenter import organization_detail
from ConfigurationCenter import organization_dorganizationAddPeople

class check_organization():
	def __init__(self, session):
		self.session = session

	def t_createOrganization(self, orgName = 'tets',parentOrgid = 12, remark="test"):
		# 组织创建
		Organization = organization_createOrganization.createOrganization(self.session, orgName, parentOrgid, remark)
		assert "200" == Organization['statusCode'], "createOrganization fail."

		# 数据库数据检查
		Organization_sql = DB_foura.organizationByOrgname(orgName)
		assert orgName == Organization_sql['orgname'], 'DB no data about {orgName}'.format(orgName=orgName)

		return Organization_sql

	def t_detail(self, orgid= 23 ):
		# 组织详情
		Organization = organization_detail.detail(self.session, orgid)
		assert "200" == Organization['statusCode'], "detail Organization fail."
		# 接口数据校验
		assert orgid == Organization['data']['orgid'], 'api no data about {orgid}'.format(orgid=orgid)

		# 数据库数据检查
		Organization_sql = DB_foura.organizationByOrgid(orgid)
		assert orgid == Organization_sql['orgid'], 'DB no data about {orgid}'.format(orgid=orgid)


	def t_updateOrganization(self, orgname = 'tets', orgid = 23, parentorgid = 12, remark="", empIds="",reason=""):
		# 编辑组织
		Organization = organization_updateOrganization.updateOrganization(self.session, orgname, orgid, parentorgid, remark, empIds, reason)
		assert "200" == Organization['statusCode'], "update Organization fail."

		# 数据库数据检查
		Organization_sql = DB_foura.organizationByOrgid(orgid)
		assert orgname == Organization_sql['orgname'], 'DB no data about {orgname}'.format(orgname=orgname)
		assert parentorgid == Organization_sql['parentorgid'], 'DB no data about {parentorgid}'.format(parentorgid=parentorgid)
		if remark is not "":
			assert remark == Organization_sql['remark'], 'DB no data about {remark}'.format(remark=remark)
		if empIds is not "":
			assert empIds == Organization_sql['empIds'], 'DB no data about {empIds}'.format(empIds=empIds)
		if reason is not "":
			assert reason == Organization_sql['reason'], 'DB no data about {reason}'.format(reason=reason)

	def t_dorganizationAddPeople(self, orgId='', empIdList='' ):
		# 该接口未使用
		# 组织添加人员
		Organization = organization_dorganizationAddPeople.dorganizationAddPeople(self.session, orgId, empIdList)
		assert "200" == Organization['statusCode'], "update Organization fail."


	def t_deleteOrganization(self, orgid=23):
		# 删除组织
		Organization = organization_deleteOrganization.deleteOrganization(self.session, orgid)
		assert "200" == Organization['statusCode'], "delete Organization fail."

		# 数据库数据检查
		Organization_sql = DB_foura.organizationByOrgid(orgid)
		assert None == Organization_sql, 'DB has data about {orgid}'.format(orgid=orgid)


if __name__ == '__main__':
	Login = cas_login_phone_checklastLogin.GetSession()
	session = Login.getCookie()


