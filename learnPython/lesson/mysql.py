#数据库连接

import pymysql

con = pymysql.connect(host="",user="",passwd="",db="")
#执行sql语句
con.query()
con.commit()

#执行sql语句有返回
cs = con.cursor()
cs.execute('select * from mytb')

for i in cs:
    print('当前是第'+str(cs.rownumber)+'行')
    print('标题是:'+i[0])
    print('关键词:'+i[1])
con.close()
