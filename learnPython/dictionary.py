# Dictionary(字典)
#字典是python中另一个非常有用的内置数据类型
#列表是有序的对象集合，字典是无序的对象结合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通道偏移存取
#字典是一种映射类型，字典用"{}"标示，它是一个无序的键（key）:值（value）对集合
#注意⚠️ 键（key）必须使用不可变类型。
#在同一个字典中，键（key）必须是唯一的
dict = {}
dict['one'] = '菜鸟教程'
dict[2] = '菜鸟工具'
tinydict = {'name':'runobb','code':1,'site':'www.baidu.com'}
print(dict['one'])#输出键为 'one' 的值
print(dict[2])#输出键为 2 的值
print(tinydict)#输出完整的字典
print(tinydict.keys())#输出所有键
print(tinydict.values())# 输出所有值

#构造函数dict()可以直接从键值对序列中构建字典如下：
#在python命令中执行以下语句
# dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
# {'Taobao': 3, 'Runoob': 1, 'Google': 2}
# {x: x**2 for x in (2, 4, 6)}


# {2: 4, 4: 16, 6: 36}
# dict(Runoob=1, Google=2, Taobao=3)
# {'Taobao': 3, 'Runoob': 1, 'Google': 2}

#总结：
#1、字典是一种映射类型，它的元素是键值对
#2、字典的关键字必须为不可变类型，且不能重复
#3、创建空字典用{}

lingdu ={
    "name":'lingdu',
    "age":25,
    "sex":'men'
}
print(lingdu["name"])

lingdu.clear()  #清空字典所有条目
print(lingdu)  #{}空字典


#不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住

dicta = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'};
print(dicta["Name"]) #Manni
seq = {'name','age','sex'}
dicta = dicta.fromkeys(seq,10)
print(dicta,'hello')

#键必须不可变，所以可以用数，字符串或元组充当，所以用列表就不行

dictc = {['Name']: 'Zara', 'Age': 7};
 
print ("dict['Name']: ", dictc['Name']); 