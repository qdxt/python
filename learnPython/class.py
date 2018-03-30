#coding=utf-8
# class Employee:
#     '员工的基类'
#     empCount = 0
#     def __int__(self,name,salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
# def displayCount(self):
#     print("Total Employee %d" % Employee.empCount)
#
# def displayEmployee(self):
#     print ("Name : ", self.name,  ", Salary: ", self.salary)

# class cl2:
#     def __init__(self,name,job):
#         print('mu name is',name,'my job is',job)
# #__init__ 是初始化功能 self 代表的是初始化的"自己"
# a = cl2('xiaozhang','qianduan')

# class cl3:
#     def __init__(self,name):
#         self.name = name
#         print('hello')
#     def hello(self):
#         print('hello',self.name)
#
# a = cl3('lingdu')#hello
#
# a.hello()#hello lingdu

#继承 单继承 多继承 重写（重载）

#父亲类(基类)
#类名后边的括号是继承使用的
class father():
    def speak(self):
        print('i can speak')

#单继承
class son(father):
    pass

#母亲类
class mother():
    def write(self):
        print('i can write')

#多继承
class daughter(father,mother):
    def listen(self):
        print('i can listen')

#重写
class son2(father):
    def speak(self):
        print('I can speak!')


s = son2()

s.speak()# I can speak!
