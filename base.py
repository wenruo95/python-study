# encoding: utf-8

import keyword

# 关键字
print(keyword.kwlist)

# 单行注释

'''
    多行注释
    ddd
'''


"""
    多行注释
    ffff
"""

# 多行语句
a = 1
b = 2
c = 3
d = a + \
        b + \
        c
print(a, b, c, d)


# input : 运行时记得删除注释
'''
str = input("\n\nPlease Input Your Name:")
print("Welcome, ", str, "!\n")
'''

# output
print('默认换行:123')
print('默认不换行123', end = '')
print('新123')

# 算数运算符 + - * / % ** // 分别为加减乘除、取模、幂、取整除
# 比较运算符 == != > < >= <=
# 赋值运算符 = += -= *= /= %= //=
# 位运算符 & | ^ ~ << >>
# 逻辑 and or not
# 成员运算符 in、not in             in表示指定序列中找到值返回true
# 身份运算符 is、not is             is是判断两个标识符是不是引用同一个对象

# 运算符优先级 同等优先级从左至右依次执行，养成使用小括号习惯,与人方便自己方便。

import math
print("a / b:\t", a / b)
print("a // b:\t",a // b)
print("a % b:\t", a % b)
print("math.ceil(a / b):\t", math.ceil(a / b))



