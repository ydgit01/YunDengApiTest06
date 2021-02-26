#-*- coding:utf-8 -*-
"""
@note:
@author: Qred
@file: MD5.py
@time: 2020/03/28
"""
import hashlib


def getSignValue_src(value, src):
    valueSort = sorted(value.iteritems(), key=lambda d: d[0], reverse=False)
    for vs in valueSort:
        src = src + "&" + str(vs[0]) + "=" + str(vs[1])
    _sign = get_md5_value(src)
    return _sign

def get_md5_value(src):
    myMd5 = hashlib.md5()
    myMd5.update(src)
    myMd5_Digest = myMd5.hexdigest()
    return myMd5_Digest


def get_sha1_value(src):
    mySha1 = hashlib.sha1()
    mySha1.update(src)
    mySha1_Digest = mySha1.hexdigest()
    return mySha1_Digest

if __name__ == '__main__':
    value = '200309mi@'
    by = bytes(value,encoding='utf8')
    print(get_md5_value(by))
    print(get_sha1_value(by))
