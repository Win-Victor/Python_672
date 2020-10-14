# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(el_1, el_2, el_3):
    sum_1 = el_1 + el_2
    sum_2 = el_1 + el_3
    sum_3 = el_2 + el_3
    max_sum = max(sum_1, sum_2, sum_3)
    return (max_sum)


print(my_func(4, 5, 6))
print(my_func(11, 11, 11))
print(my_func(11, 22, -33))
print("*" * 100)
print(f'Сумма 2 наибольших аргументов: {my_func(int(input("Введите первый аргумент: ")), int(input("Введите второй аргумент: ")), int(input("Введите третий аргумент: ")))}')
