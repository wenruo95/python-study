#!/usr/bin/python
# encoding: utf-8

filename = 'data.log'

# 打开文件(a+ 追加读写模式)
# 用 with 关键字的方式打开文件，会自动关闭文件资源
with open(filename, 'w+', encoding='utf-8') as file:
    print('文件名称: {}'.format(file.name))
    print('文件编码: {}'.format(file.encoding))
    print('文件打开模式: {}'.format(file.mode))
    print('文件是否可读: {}'.format(file.readable()))
    print('文件是否可写: {}'.format(file.writable()))
    print('此时文件指针位置为: {}'.format(file.tell()))
    # 写入内容
    num = file.write("第一行内容\n")
    print('写入文件 {} 个字符'.format(num))
    # 文件指针在文件尾部，故无内容
    print(file.readline(), file.tell())
    # 改变文件指针到文件头部
    file.seek(0)
    # 改变文件指针后，读取到第一行内容
    print(file.readline(), file.tell())
    # 但文件指针的改变，却不会影响到写入的位置
    file.write('第二次写入的内容\n')
    # 文件指针又回到了文件尾
    print(file.readline(), file.tell())
    # file.read() 从当前文件指针位置读取指定长度的字符
    file.seek(0)
    print(file.read(9))
    # 按行分割文件，返回字符串列表
    file.seek(0)
    print(file.readlines())
    # 迭代文件对象，一行一个元素
    file.seek(0)

    for line in file:
        print(line, end='')

# 关闭文件资源
if not file.closed:
    file.close()
