#Set 集合
#集合（set）是一个无序不重复元素的序列
#基本功能是进行成员关系测试和删除重复元素
#可以使用大括号{}或者set（）函数创建集合，注意 ：创建一个空集合必须用set（）而不是{}，因为{}是用来创建一个空字典
#创建格式：
#parame = {value01,value02,value03,....}
#或者
#set(value)
student = {'tom','jim','mary','tom','jack','rose'}
print(student) #输出集合，重复的元素会被自动去掉

#成员测试
if('rose' in student):
    print('rose在集合中')
else:
    print('rose不在集合中')

#set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)#无需列表 每次打印不同数值 但是都是无序的不重复的一个集合
print(a-b)#a和b的差集
print(a|b)#a和b的并集
print(a&b) #a和b的交集
print(a^b)#a和b中不同时存在的元素
