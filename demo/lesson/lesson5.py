# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))
list = [x,y,z]
list.sort()#升序
print('从大到小排列:',list)
list.sort(reverse=True)#降序
print('从小到大排列',list)