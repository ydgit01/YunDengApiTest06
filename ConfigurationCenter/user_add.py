# -*- coding:utf-8 -*-
"""
@note:
	10. 新增用户
@author: Qred
@file: user_add.py
@time: 2020/04/07
"""

from Common import ReadConfig

# 获取云灯host
host = "YunDengUrl"
host = ReadConfig.GetOptions(host)

# print (host)

def add(session, userName='12', accountName='qreds', email='12111@163.com', orgidList='123', mobileNo='15588809999',
        roleIds=87, sex=0, birthdate='', dingding='', graduateSchool='', graduateTime='', education='', empcode='',
        otel='', remark='', major='', haddress=''):
	'''
	10. 新增用户
	:param session:
	:param userName:人员姓名
	:param accountName:登录账号
	:param email:邮箱
	:param orgidList:组织机构ids
	:param mobileNo:手机号
	:param roleIds:角色ids
	:param sex:性别 0:女，1：男，2：保密
	:param birthdate:出生日期
	:param dingding:钉钉账号
	:param graduateSchool:毕业学校
	:param graduateTime:毕业时间
	:param education:学历
	:param empcode:工号
	:param otel:办公电话
	:param remark:备注
	:param major:专业
	:param haddress:籍贯
	:return:
	'''
	url = host + '/yundeng/user/add'
	value = {"userName": userName, "accountName": accountName, "email": email, "orgidList": orgidList,
	         "mobileNo": mobileNo, "roleIds": roleIds, "sex": sex, "birthdate": birthdate, "dingding": dingding,
	         "graduateSchool": graduateSchool, "graduateTime": graduateTime, "education": education, "empcode": empcode,
	         "otel": otel, "remark": remark, "major": major, "haddress": haddress}
	raw = session.post(url, data=value)

	print(raw.json())

	return raw
