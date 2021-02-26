#-*- coding:utf-8 -*-
"""
@note:
	登录
@author: Qred
@file: cas_login_phone_checklastLogin.py
@time: 2020/03/25
"""
import urllib
import urllib3
import requests

from Common import ReadConfig

HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
	'Access-Encoding': 'gzip, deflate',
	'Access-Language': 'zh-CN,zh;q=0.9',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Connection': 'keep-alive',
	'X-Requested-With': 'XMLHttpRequest',
}


class GetSession():
	def __init__(self, username='17801130126', password='2493f190d57de99da0ba181cf5acc191', token='187b44095bea45914819f90ac021a05af207a5a87559db9f7570fa0ba479b5d4'):
		self.username = username
		self.password = password
		self.token = token

	def getCookie(self):
		url = ReadConfig.GetOptions("LoginUrl") + '/cas/login/phone/checklastLogin'
		# url = "http://cas.gw.test.com/cas/login?service=http%3A%2F%2Fyundeng-console.gw.test.com%2Fyundeng%2F4A%2FreceiveTicket/yundeng/4A/getUserInfo"
		# url = 'http://cas.gw.test.com/cas/login?service=http%3A%2F%2Fyundeng-console.gw.test.com%2Fyundeng%2F4A%2FreceiveTicket/yundeng/notice/countMyUnRead'
		values = {'token': self.token, 'username': self.username, 'password': self.password}
		session = requests.session()
		session.headers = HEADER
		a = session.post(url, data=values)

		print(a.text)
		# print(a.json()['session_id'])
		print(a.cookies)
		print(session.cookies)
		print(session)
		print(a.cookies.keys())
		return session


def loginV(username='17801130126', password='2493f190d57de99da0ba181cf5acc191', token='187b44095bea45914819f90ac021a05af207a5a87559db9f7570fa0ba479b5d4'):
	url = ReadConfig.GetOptions("LoginUrl") + '/cas/login/phone/checklastLogin'
	values = {'token': token, 'username': username, 'password': password}
	jar = requests.cookies.RequestsCookieJar()
	data = urllib.parse.urlencode(values)
	req = urllib.request.Request(url, bytes(data,encoding='utf8'))

	processor = urllib.request.HTTPCookieProcessor(jar)
	opener = urllib.request.build_opener(processor)
	urllib.request.install_opener(opener)
	# req = urllib.request.urlopen(req )
	# print (req.read().decode())
	opener.open(url, bytes(data,encoding='utf8'))

	return opener


