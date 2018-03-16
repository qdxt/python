#数据转换
#int(x, base=10) 讲x转换为一个整数  base -- 进制数，默认十进制。
str1 = '01234'
print(int(str1,base=10))#1234

#float(x)#讲x转换到一个浮点数
number1 = 1
print(float(number1))#1.0

#complex([real[, imag]])
# real -- int, long, float或字符串；
# imag -- int, long, float；
# complex(1,2)
# (1+2j)

#str(x)讲对象x转换为字符串
# str({'runoob': 'runoob.com', 'google': 'google.com'})
# "{'google': 'google.com', 'runoob': 'runoob.com'}"

#repr(x)将对象 x 转换为表达式字符串
#repr({'runoob': 'runoob.com', 'google': 'google.com'})
#"{'google': 'google.com', 'runoob': 'runoob.com'}"

#eval(str)用来计算在字符串中的有效Python表达式,并返回一个对象
# x = 7
# eval('3*x') #21
# eval('pow(2,2)')#4

#tuple(s) 将序列 s 转换为一个元组
list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
tuple1=tuple(list1)
tuple1
('Google', 'Taobao', 'Runoob', 'Baidu')
#set(s)转换为可变集合
# x = set('runoob')
# y = set('google')
# x, y
# (set(['b', 'r', 'u', 'o', 'n']), set(['e', 'o', 'g', 'l']))   # 重复的被删除

#dict(d)创建一个字典。d 必须是一个序列 (key,value)元组。
# dict(a='a', b='b', t='t')     # 传入关键字
# {'a': 'a', 'b': 'b', 't': 't'}
# >>> dict(zip(['one', 'two', 'three'], [1, 2, 3]))   # 映射函数方式来构造字典
# {'three': 3, 'two': 2, 'one': 1}
# >>> dict([('one', 1), ('two', 2), ('three', 3)])    # 可迭代对象方式来构造字典
# {'three': 3, 'two': 2, 'one': 1}


#frozenset(s)转换为不可变集合
# a = frozenset(range(10))     # 生成一个新的不可变集合
# >>> a
# frozenset([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# >>> b = frozenset('runoob')
# >>> b
# frozenset(['b', 'r', 'u', 'o', 'n'])   # 创建不可变集合

#chr(x)将一个整数转换为一个字符
# print chr(0x30), chr(0x31), chr(0x61)   # 十六进制
# 0 1 a
# print chr(48), chr(49), chr(97)         # 十进制
# 0 1 a
#unichr(x)将一个整数转换为Unicode字符
# unichr(97)
# u'a'
# unichr(98)
# u'b'
# unichr(99)
# u'c'

#ord(x)将一个字符转换为它的整数值
# ord('a')
# 97

#hex(x)	将一个整数转换为一个十六进制字符串
# hex(255)
# '0xff'
#oct(x)将一个整数转换为一个八进制字符串
# oct(20)
# '024'