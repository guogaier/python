# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 课本 第4章 操作列表 学习记录

# 4.1 遍历列表 课文例子
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", this is a great trick!")
    print("I can't wait to see you next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That is a great magic show! \n")

# P50 动手试一试 4-1 比萨
pizzas = ['New York Style', 'Chicago Style', 'California Style',
          'Pan Pizza', 'Thick style', 'Cracker and Thin Style', 'Take and Bake Style']
for pizza in pizzas:
    print("I like " + pizza + " pizza")
print("I really love pizza!")

# P50 动手试一试 4-2 动物
animals = ['dog', 'cat', 'pig']
for animal in animals:
    print("\nA " + animal + " would make a great pet.")
print("\nAny of these animals would make a great pet!")
