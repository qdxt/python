import time #引入time模块
ticks = time.time()

print('当前时间戳:',ticks)  #1521706427.8093681

localtime = time.localtime(time.time())

print('本地时间为:',localtime)
#time.struct_time(tm_year=2018, tm_mon=3, tm_mday=22, tm_hour=16, 
# tm_min=15, tm_sec=0, tm_wday=3, tm_yday=81, tm_isdst=0)

localtime1 = time.asctime(time.localtime(time.time()))

print('本地时间1',localtime1)#Thu Mar 22 16:16:07 2018

print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
#2018-03-22 16:17:32



