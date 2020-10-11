# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 5, 3, 3, 2]
length = len(my_list)
print(f"Есть список элеметов {my_list}")
while True:
    num = input("Сколько элементов Вы планируете добавить? ")
    if num.isdigit():
        num = int(num)
        break
    else:
        print("Что-то не то указали...")
        continue

min_in_list = min(my_list)
index_min = my_list.index(min_in_list)

while len(my_list) < length + num:
    while True:
        new_element = input("Введите новый элемент списка (натуральное число)")
        if new_element.isdigit():
            new_element = int(new_element)
            break
        else:
            print(f"{new_element} - Ошибочка вышла")
            continue
    for i in my_list:
        if new_element < min_in_list:
            my_list.append(float(new_element))
            print(f"Список после добавления нового элемента: {my_list} 1 условие")
            break
        if new_element < i:
            i += 1
        elif new_element == i:
            count = my_list.count(i)
            my_list.insert(my_list.index(i) + count, float(new_element))
            print(f"Список после добавления нового элемента: {my_list} 2 условие")
            break
        elif new_element > i:
            my_list.insert(my_list.index(i), float(new_element))
            print(f"Список после добавления нового элемента: {my_list} 3 условие")
            break
