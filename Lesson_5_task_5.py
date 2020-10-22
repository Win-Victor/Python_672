"""5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле
и выводить ее на экран."""

try:
    with open("task_5.txt", "w+", encoding="utf-8") as f:
        new_line = input("Введите набор чисел, разделяя числа пробелом \n")
        f.writelines(new_line)
        my_list = new_line.split()
        my_sum = sum(map(float, my_list))
        f.writelines(f"\nСумма всех введенных чисел: {my_sum}")
        print(f"Сумма всех введенных чисел: {my_sum}")
except IOError:
    print("Ошибка файла")
except ValueError:
    print("Ошибка вводимых значений. Пишите числа")
