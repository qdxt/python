fo = open("file.txt",'wb')
print('文件名:',fo.name)
print('是否关闭:',fo.closed)
print('访问模式:',fo.mode)
# 文件名: file.txt
# 是否关闭: False
# 访问模式: r
str = 'www.baidu.com'
bytes_utf_8 = str.encode(encoding="utf-8")
fo.write(bytes_utf_8)
#python3wirte方法是将一个字节缓冲区写入到目标文件中，而不支持string类型

# str1 = fo.read()
# print(str1)
#读取文件内容



