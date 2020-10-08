# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

name = "Ivan"
age = 24
has_car = True
print(name)
print(age)
print(has_car)

name = input("укажите свое имя: ")
age = int(input("Укажите свой возраст, " + name + " "))
weight = int(input("Укажите свой вес, " + " "))
print(name, age, weight)
print("name", type(name) == str)
print("age", type(age) == int)
print("weight", type(weight) == int)
