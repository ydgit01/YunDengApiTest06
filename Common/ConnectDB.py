# encoding=utf8

import pymysql
from DBUtils.PooledDB import PooledDB


# 连接数据�?
class DbManager():
	"""数据库连接
	user：登录用户名
	passwd：登录密码
	db：数据库名
	host：数据库地址
	chartset:编码格式设置
	creator：数据库类型
	maxconnect：最大连接数
	"""

	def __init__(self, user='gtssolution', passwd='DevGtsSolution0731!', db='foura',
	             host='rm-8vbjo79cr5mc867pqxo.mysql.zhangbei.rds.aliyuncs.com', port=3306, charset='utf8',
	             creator=pymysql, cursorclass=pymysql.cursors.DictCursor, maxconnect=5):
		self.user = user
		self.passwd = passwd
		self.db = db
		self.host = host
		self.port = port
		self.charset = charset
		self.creator = creator
		self.cursorclass = cursorclass
		self.maxconnect = maxconnect

	# 连接数据�?
	def getConn(self):
		_pool = PooledDB(creator=self.creator, maxconnections=self.maxconnect, host=self.host, user=self.user,
		                 passwd=self.passwd, db=self.db, port=self.port, charset=self.charset,cursorclass=self.cursorclass
		                 )
		return _pool.connection()

	def queryOne(self, sql):
		""" 使用sql语句，调用数据库数据 """
		conn = self.getConn()
		cursor = conn.cursor()
		self.sql = sql
		rowcount = cursor.execute(self.sql)
		if rowcount > 0:
			res = cursor.fetchone()
		else:
			res = None

		return res

	def executeAndGetId(self, sql, param=None):
		""" 执行插入语句并获取自增id """
		conn = self.getConn()
		cursor = conn.cursor()
		if param == None:
			cursor.execute(sql)
		else:
			cursor.execute(sql, param)
		conn.commit()
		cursor.close()
		conn.close()

	def updateExecute(self, sql):
		""" 修改数据 """
		conn = self.getConn()
		cursor = conn.cursor()
		cursor.execute(sql)
		conn.commit()
		cursor.close()
		conn.close()

	def deleteExecute(self, sql):
		""" 删除数据 """
		conn = self.getConn()
		cursor = conn.cursor()
		cursor.execute(sql)
		conn.commit()
		cursor.close()
		conn.close()

	def execute(self, sql, param=None):
		""" 执行sql语句 """
		conn = self.getConn()
		cursor = conn.cursor()
		if param == None:
			rowcount = cursor.execute(sql)
		else:
			rowcount = cursor.execute(sql, param)
		cursor.close()
		conn.close()
		return rowcount

	def queryAll(self, sql):
		""" 获取�?有信�? """
		conn = self.getConn()
		cursor = conn.cursor()
		rowcount = cursor.execute(sql)
		if rowcount > 0:
			res = cursor.fetchall()
		else:
			res = None
		cursor.close()
		conn.close()

		return res

	def resultRow(self, n, sql):
		if n == 1:
			row = self.queryOne(sql)
			#         print "row=",row
			return row
		elif n == 2:
			rows = self.queryAll(sql)
			#         print "rows=",rows
			return rows
		elif n == 3:
			try:
				self.conn = self.getConn()
				self.cursor = self.conn.cursor()
				rowcount = self.cursor.execute(sql)
				return rowcount
			except BaseException as msg:
				print(msg)

			finally:
				self.cursor.close()
				self.conn.close()


# if __name__ == '__main__':
# 	# example:连接jellyfish_user数据库，查询user_real_record表数�? 'script_user', 'user_4_script', 'jellyfish_user', "116.62.166.81", 65332
# 	sqlCon = DbManager()
# 	sql = 'SELECT * FROM `foura`.`cap_user` LIMIT 0, 10'
# 	res = sqlCon.queryAll(sql)
# 	print(res)
