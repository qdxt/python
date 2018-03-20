str = 'Runoob'
#字符串的截取语法格式如下：
#变量[头下标:尾下标]   ----------> 注意⚠️如果存在尾下标的话------>不包括尾下标所代表的字符串
#索引值以 0 为开始值，-1 为从末尾的开始位置
#加号 (+) 是字符串的连接符， 星号 (*) 表示复制当前字符串，紧跟的数字为复制的次数
#如果以正数为头下标和尾下标  那么头下标比尾下标小
#如果以负数为头下标和尾下标  那么头下标比尾下标大
print(str)#Runoob
print(str[0:-1])#Runoo
print(str[0])#R
print(str[2:5])#noo 不包括尾下标所代表的字符串
print(str[2:])#noob
print(str*2)#RunoobRunoob
print(str+"TEST")#RunoobTEST

#Python 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串
print('Ru\noob')
#Ru
#oob

print(r'Ru\noob')#Ru\noob

#注意，Python 没有单独的字符类型，一个字符就是长度为1的字符串。

#Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误。

# word = 'python'
# word[0]='c'
# print(word)#报错

a = "hello"
b = "world"
if("h" in a):
    print('h in a')


print(a.capitalize(),'首字母大写')
print(a.center(10),'字符串居中显示')
print(a.count('l'))#返回 str 在 string 里面出现的次数，
print(a.find('0'))

