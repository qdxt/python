# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
list = [];
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j) and (i!=k) and(j!=k):
                list.append([i,j,k])
print("总数量",len(list))
print("它们分别是:",list)