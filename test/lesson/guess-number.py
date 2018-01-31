# 题目：猜数字游戏
import random

print('------开始猜数字游戏------')
print('数字范围在0-10之间')
number = random.randint(0, 10)
inputNumber = int(input('请输入整数: '))
while inputNumber != number:
    inputNumber = int(input('猜错了，请重新输入: '))
if (inputNumber == number):
    print('恭喜你猜对了')

