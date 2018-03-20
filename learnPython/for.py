fruits = ['banana','apple','mango']
for index in range(len(fruits)):
    print('当前水果:',fruits[index])# banana apple mango



for number in range(3):
    print('当前索引:',number)# 0 1 2


for num in range(10,20):
    for i in range(2,num):
        if(num%i)==0:
            j=num/i
            print(num,'等于',i * j)
            break
    else:
        print(num,'是一个质数')

    n= 2
    while(n<100):
        j=2
        while(j<=(n/j)):
            if not(n%j):break
            j=j+1    
        if(j>n/j):
            print(n,'是素数')
        n=n+1
            

        




    