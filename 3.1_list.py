# !/usr/bin/python3
# -*-coding:utf-8-*-

# 以下为《Python编程 从入门到实践》 第3章 学习笔记


# 以下为 3.1 课文中的例子
# 创建一个列表
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# 按照从前到后的顺序，依次打印列表中的每一个元素
print("\n" + bicycles[0])
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])

# 按照从后向前的顺序，依次打印列表中的每一个元素
print("\n" + bicycles[-1])
print(bicycles[-2])
print(bicycles[-3])
print(bicycles[-4])
print("\n")

# 按照从后向前的顺序，依次打印列表中的每一个元素，且每一个元素的首字母大写
print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[2].title())
print(bicycles[3].title())
print("\n")

# 按照从后向前的顺序，依次打印列表中的每一个元素，同时打印一句话
print("My first bicycles was a " + bicycles[0].title() + ".")
print("My second bicycles was a " + bicycles[1].title() + ".\n")
print("My third bicycles was a " + bicycles[2].title() + ".")
print("My fourth bicycles was a " + bicycles[3].title() + ".\n\n\n")



# 以下为 3.1 动手试一试 的练习

# 3-1 姓名 新建一个好友姓名的列表，并依次打印每个人的姓名
names = ['guan zhiwei', 'zhang haifeng', 'shao jiajia', 'zhao yakun', 'mai tengfei', 'liu xiangda', 'chen jinling', 'duan yunkai']
print(names)
print("\n" + names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])
print(names[6])
print(names[7] + "\n")

# 3-2 问候语，使用3-1 的列表，给每个朋友打印一句问候语
print(names[0].title() + ",you are my friend!")
print(names[1].title() + ",you are my friend!")
print(names[2].title() + ",you are my friend!")
print(names[3].title() + ",you are my friend!")
print(names[4].title() + ",you are my friend!")
print(names[5].title() + ",you are my friend!")
print(names[6].title() + ",you are my friend!")
print(names[7].title() + ",you are my friend!")
print("\n")

# 3-3 自己的列表 打印自己喜欢的通勤方式
trafics = ['cycle', 'bus', 'metro', 'taxi', 'car']
print(trafics)
print("I would like to own a " + trafics[0] + ".")
print("I would like to own a " + trafics[-1] + ".")
print("I would like to own a " + trafics[2] + ".")

