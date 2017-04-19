#Test how to load Wind data into mysql
#Python version 2.7

from WindPy import *
import MySQLdb

w.start()
result = w.edb("M0000705","2016-04-19","2017-04-19","Fill=Previous")
time = result.Times
data = result.Data

conn = MySQLdb.connect(
	host = 'localhost',
	port = 3306,
    user = 'root',
    passwd = '12345678',
    db = 'test',
	)

cur = conn.cursor()

for index in range(len(time)):
	values = [time[index].strftime('%Y%m%d'), data[0][index]]
	cur.execute('insert into cpi values(%s,%s)',values)

cur.close()
conn.commit()
conn.close()