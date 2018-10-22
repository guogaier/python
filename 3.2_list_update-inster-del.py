#!/usr/bin/python3
# -*-coding:utf-8-*-

# 以下为《Python编程 从入门到实践》 第3章 学习笔记


# 以下为 3.1 课文中的例子
# 创建一个列表
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 修改列表中第一个元素
motorcycles[0] = 'dayang'
print(motorcycles)

# 使用append()语句，在列表末尾插入一个元素
motorcycles.append('ducati')
print(motorcycles)

# 创建一个空列表，使用append()语句添加元素
motorSpaces = []

motorSpaces.append('honda')
motorSpaces.append('yamaha')
motorSpaces.append('suzuki')
print(motorSpaces)

# 在列表的任意指定的位置插入元素
print(motorSpaces)

motorSpaces.insert(0, 'ducati')
print(motorSpaces)
motorSpaces.insert(2, 'ducati')
print(motorSpaces)

# 从列表中删除元素
# 使用del语句，删除指定索引位置的元素
print(motorSpaces)
del motorSpaces[0]
print(motorSpaces)
del motorSpaces[-1]
print(motorSpaces)

# 使用pop()删除列表末尾的元素
print(motorSpaces)

popped_motorSpaces = motorSpaces.pop()
print(motorSpaces)
print(popped_motorSpaces)

# 使用pop()删除指定位置的元素
print(motorcycles)

first_owned = motorcycles.pop(0)
print(motorcycles)
print(first_owned)
print('The first motorcycles I owned was a ' + first_owned.title() + '.')
second_owned = motorcycles.pop(-1)
print(motorcycles)
print(second_owned)
print('The second motorcycles I owned was a ' + second_owned.title() + '.')
third_owned = motorcycles.pop(1)
print(motorcycles)
print(third_owned)
print('The third motorcycles I owned was a ' + third_owned.title() + '.')


# 使用remove()方法删除已知值的元素
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA ' + too_expensive.title() + ' is too expensive for me.')


# 以下是课本 3-2 动手试一试 的练习结果

# 3-4 嘉宾名单
