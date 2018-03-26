#记事本的功能
#1、实现命令行输入需要记录的内容
#2、自动创建文件，并且把输入的内容添加进去
#3、用户自动选择查看记事本还是记录内容
print('查看记事本内容选择请输入1')
print('输入记录内容请选择输入2')
number = input('主人，请选择:')
if number == '1':
    fo = open("notepad.txt",'r')#创建文件
    fo.seek(0, 0)
    cont = fo.read()
    if cont == None:
        print('当前还没有内容哦，快去记一笔吧')
    else:
        print('当前记事本内容为:',cont)
elif number == '2':
    content = input('主人，请输入您要记录的内容:')
    fo = open("notepad.txt",'a+')#创建文件
    fo.write(content+'\n')
    print('主人，我帮您记录下了,',content,'这条内容')





