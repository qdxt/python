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
# #注意一下例子：
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

#================分割线==========================
#list中的方法
a = ['I','like','python']
#反转方法1
# print(a[::-1]) #['python', 'like', 'I']
#反转方法2 需要把上面的list变量注释
# print(list(reversed(a))) #['python', 'like', 'I']
# print(list(reversed("abcd"))) #['d', 'c', 'b', 'a']

list1 = ['good','python','i']
list1.append('like')
list1.append(100)
list1[len(list1):] = [5]
print(list1)
print(len(list1))

#================分割线==========================

la = [1,2,3]
lb = [4,'5',6,True]
la.extend(lb)# [1,2,3,4,'5',True]
c = 5
la.extend(c)# 报错，如果extend的对象是数值型，则报错

#看看extend 和append的区别
laa = [1,2,3]
lbb = ['456']
laa.extend(lbb)#[1,2,3,'4','5','6']
lcc = ['456']
laa.append(lcc)#[1,2,3,['456']]
#append是整体的追加，extend是个体化圹编

#================分割线==========================
#list.count(x)数一下x在list中出现了多少次
laa = [1,2,3,4,1,2]
laa.count(1)#2
laa.count(4)#1
laa.count(6)#0

#================分割线==========================
#list.index(x)找到x在list中的位置
laaa = [1,2,3,'ling','du']
laaa.index(3)#2
laaa.index('hello')#报错

#================分割线==========================
#list.insert(i,x) i代表的是index x代表的是要添加的元素
# 将新的元素x 插入到原list中的list[i]前面
laaaaaa = [1,2,3]
laaaaaa.insert('lingdu')#报错 没有填写index
laaaaaa.insert(1,'lingdu')#[1,'lingdu',2,3]
#================分割线==========================
#list.remove(x)在list中找到x元素并且进行删除操作
laaaaaaaa = [1,2,3,'x','y','z']
laaaaaaaa.remove(x)#报错找不到x变量 注意在这里x是变量 如果想换成字符串需要
laaaaaaaa.remove('x')#[1,2,3,'y','z'] 这里是删除字符串'x'的正确写法

#================分割线==========================
#list.pop([i])在list中找到索引为i的元素并且进行删除操作
ll = [1,2,3,4,5,6]
lll=ll.pop()# 如果什么都不填写默认删除最后一项并且将结果返回
#ll->   [1,2,3,4,5]
#lll -> 6
ll.pop()#5
ll.pop()#4
ll.pop()#3
ll.pop()#2
ll.pop()#1
ll.pop()#报错 就剩下一个元素了

#================分割线==========================
#x in list 判断元素x是不是在list中
lll = [1,2,3,4]
1 in ll # True
5 in ll #False

#================分割线==========================
#如果想知道关于list的函数以及该函数的使用办法 直接用命令 help(list)






