def helloWorld():
    print('hello world')
    return 

helloWorld()

def printStr(str):
    print(str)
    return 
printStr('打印一个字符串吧')

# def changeme(list):
#     list.append([1,2,3])
#     print(list)
#     return 
# changeme([4,5,6,7]) #[4, 5, 6, 7, [1, 2, 3]]

def changeme(list):
    list.append(1)
    print(list)
    return 

changeme([8,9]) #[8,9,1]
#关键字参数
def printinfo(name,age):
    print('name:',name)
    print('age:',age)
    return;

printinfo(age=7,name='lingdu')
# name: lingdu
# age: 7

#缺省参数
def printinfoo(age,name='lin'):
    print('name:',name)
    print('age:',age)
    return 
printinfoo(age=25)
# name: lin
# age: 25

#不定长参数

def printin(arg1,*vartuples):
    print('输出:',arg1)
    for var in vartuples:
        print(var)

    return 

printin(10)

printin(20,30,40,60)
# 输出: 10
# 输出: 20
# 30
# 40
# 60



