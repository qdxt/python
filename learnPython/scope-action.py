# i = 10
# def func():
#     print(i)
# print(i,)#10
# func()#10
#这里涉及作用域的概念
# 全局变量是可以在局部（函数）中取到的
#局部变量是不可以在全局中获取到的

# def func1():
#     index = 100
#     print(index)#100

#print(index,'index') #index is not defined

# index = 10
#
# def func2():
#     #index+=1
#     print(index,'index')
# print(index)
# func2()#local variable 'index' referenced before assignment
#全局变量在局部变量中可以引用但是不能修改值


#解决方案:

index = 10

def func2():
    global index
    index+=1
    print(index,'index')#无法打印
print(index)

func2()