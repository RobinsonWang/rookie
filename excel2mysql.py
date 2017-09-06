#coding=utf-8
'''
将excel数据导入到mysql
python 2.7
'''
import xlrd
import MySQLdb

# open the workbook and define the worksheet
book = xlrd.open_workbook("test.xls")

sheet = book.sheet_by_index(0)
print sheet.name,sheet.nrows

# 建立mysql连接
targetdb = MySQLdb.connect(
	host='', 
	port=3306, 
	user='root', 
	passwd='', 
	db='',
	use_unicode=True, 
    charset="utf8"
    )

# 获得游标对象
cur = targetdb.cursor()

cur.execute("set names utf8")

# 创建待执行sql语句
sqlStr = "insert into student(name, grade, age) values(%s, %s, %s)"

# # 创建for循环读取xls文件每行的数据
for r in range(1, sheet.nrows):
	name = sheet.cell(r, 0).value
	grade = sheet.cell(r, 1).value
	age = sheet.cell(r, 2).value

	values = (name, grade, age)

	cur.execute(sqlStr, values)


# 关闭游标
cur.close()

# 提交
targetdb.commit()
# 关闭数据库连接
targetdb.close()
