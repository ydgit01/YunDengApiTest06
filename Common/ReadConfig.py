#-*- coding:utf-8 -*-
"""
@note:
	读取配置文件中的数据
@author: Qred
@file: ReadConfig.py
@time: 2020/03/25
"""
import yaml
import os

# 获得private文件的地址
dirname, filename = os.path.split(os.path.abspath(__file__))

# 配置文件路径

def GetOptions(param, yamlPath = dirname +'\IPs'):

	# 读取配置文件
	with open(yamlPath,'rb') as f:
	    content = yaml.load(f)

	# 通过key获取对应的数据
	options = content[param]

	return options

