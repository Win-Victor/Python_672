# 5. Реализовать формирование списка, используя функцию range()
# и возможности генератора. В список должны войти четные числа от 100 до 1000
# (включая границы). Необходимо получить результат вычисления произведения
# всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

my_list = [el for el in range(100, 1001) if el % 2 == 0]


def new_func(el_prev, el_next):
    return el_prev * el_next


print(reduce(new_func, my_list))
print(reduce(new_func, [el for el in range(100, 1001) if el % 2 == 0]))
print(reduce(lambda x, y: x * y, my_list))
