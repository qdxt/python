# 写一个判断闰年的函数参数为年  把相关信息打印出来

print('这是一个判断是否为闰年的小游戏')
_year = int(input('请输入年份：'))
def LeapYear(year):
    if year%4 == 0:
        if year%100 == 0 and year%400!=0:
            print(year,'不是闰年')
        else:
            print(year, '是闰年')
    else:
        print(year, '不是闰年')

LeapYear(_year)