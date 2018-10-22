# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 课本 第4章 操作列表 学习记录

# 4.3 创建数值列表 课文例子
# 4.3.1 使用函数range()
for value in range(1, 5):
    print(value)

# 4.3.2 使用range()创建数字列表
numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 3))
print(even_numbers)

# 创建一个列表，包含前10个整数的平方
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)

# 优化上一段代码
squares = []
for value in range(1, 21):
    squares.append(value**2)

print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The smallest number in this list is:")
print(min(digits))
print("The bigest number in this list is:")
print(max(digits))
print("The sum of all the Numbers in this list is:")
print(sum(digits))
