# -*- coding: utf-8 -*-
"""variables_data_types_type_conversion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XIP9BhCH_EAX2okkJo0fqA0jk8cTnSX7
"""

name = 'Joe'

name

age = 25

age

print(name)
print(age)

print(type(name))
print(type(age))

name = 'Joe'

type(name)

age = 25
type(age)

pi = 3.14
type(pi)

store_items = ['Apple', 1.49, 'Banana', 1, 'Milk', 2.99, 'Cheese', 4.49]
print(store_items, type(store_items))

print(store_items[2])

print(store_items[0:4])

print(store_items[2:])

print(store_items[:2])

store_items[2] = 'Chocolate'
print(store_items)

age = 25
print(age, type(age))

age = 25
age += 0.5
print(age, type(age))

age = '25'
type(age)

age =int(age)
print (age, type(age))