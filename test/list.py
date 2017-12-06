#列表是python中使用最频繁的数据类型
#和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需列表的新列表
#列表截取的语法格式如下：
#变量[头下标：尾下标]
#索引值以 0 为开始值，-1 为从末尾的开始位置。
#加号（+）是列表连接运算符，星号（*）是重复操作
# 举个例子:
list = ['abcd',786,2.23,True,'hello']
tinylist = [123,'hello']
print(list)#['abcd',786,2.23,True,'hello']
#注意一下例子：
print(list[0])#'abcd'
print(type(list[0]))#str
print(list[1:3])#[786,2.23]
print(type(list[1:3]))#list
print(list[2:])#[2.23,True,'hello'
print(tinylist*2)#[123,'hello',123,'hello']
print(list+tinylist)#['abcd',786,2.23,True,'hello',123,'hello']

#================分割线==========================
#注意 列表中的元素是可以改变的
list = [1,2,3,4,5]
print('原来的list:',list)
list[0] = 6
print('改变后的list:',list)
list[2:5] = [12,13,14]
print('再次改变后的list:',list)
list[2:5] = []#将对应的元素值设置为[]
print('最后的list:',list)