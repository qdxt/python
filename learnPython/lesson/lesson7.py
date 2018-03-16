#题目：将一个列表的数据复制到另一个列表中。

list1 = [1,2,3,4]
list2 = list1.copy()
print(list2) #[1,2,3,4]
#第二种办法
a = [1,2,3]
b = a[:]
print(b)