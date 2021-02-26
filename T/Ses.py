#-*- coding:utf-8 -*-
"""
@note:
@author: Qred
@file: Ses.py
@time: 2020/03/28
"""
import requests
HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',}
session = requests.session()
session.headers = HEADER
q = session.get("http://httpbin.org/cookies/set/sessioncookie/123456789")
# session.cookies = q.cookies
a = session.get("https://goldprice.org/zh-hant/live-gold-price.html")
print(a.text)