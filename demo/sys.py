from sys import argv,path #导入特定的成员
print('================Python import mode==========================')
print('path:',path)

counter = 100

print('================Python import mode==========================')

#允许同时为多个变量赋值
# a = b = c = 1
# print('a:',a,'b:',b,'c:',c)

#可以为多个对象指定多个变量
a,b,c = 1,2,'runoob'
print('a:',a,'b:',b,'c:',c)
#int float bool complex(复数)
print(type(a),type(c))
