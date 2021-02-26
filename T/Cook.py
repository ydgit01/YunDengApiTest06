#-*- coding:utf-8 -*-
"""
@note:
@author: Qred
@file: Cook.py
@time: 2020/03/30
"""
import time
import urllib

import requests

from Common import ReadConfig


def loginV(username='17801130126', password='2493f190d57de99da0ba181cf5acc191', token='187b44095bea45914819f90ac021a05af207a5a87559db9f7570fa0ba479b5d4'):

	url = 'http://www.baidu.com'
	# jar = requests.cookies.RequestsCookieJar()
	# processor = urllib.request.HTTPCookieProcessor(jar)
	# opener = urllib.request.build_opener(processor)
	# urllib.request.install_opener(opener)
	# opener.open(url)
	#
	# for cookie in jar:
	# 	print(cookie)
	#
	# time.sleep(1)
	#
	# for i in range(10):
	# 	f = opener.open(url)
	#
	# 	for cookie in jar:
	# 		print(cookie)

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
	opener.open('http://yundeng-console.gw.test.com/yundeng/4A/validateTicket')
	opener.open(url, bytes(data,encoding='utf8'))

	for cookie in jar:
		print("___________________________")
		print(cookie)

	time.sleep(1)

	# return opener

from Common import cas_login_phone_checklastLogin as Session
def login():

	temp = Session.GetSession()
	session = temp.getCookie()
	url = 'http://cas.gw.test.com/cas/login?service=http%3A%2F%2Fyundeng-console.gw.test.com%2Fyundeng%2F4A%2FreceiveTicket/yundeng/4A/validateTicket'
	values = {'token': temp.token, 'username': temp.username, 'password': temp.password}
	raw = session.post(url, data=values)
	print(raw.text)

if __name__ == '__main__':
    login()