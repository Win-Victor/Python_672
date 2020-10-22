"""3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
with open("salary.txt", encoding="utf-8") as f:
    my_list = f.readlines()
    new_list = []
    salary_list = []
    for i in range(len(my_list)):
        new_list.append(my_list[i].split())
    print("Список сотрудников и их оклады:")
    for i in range(len(new_list)):
        print(f"{str(new_list[i][0])}:  {float(new_list[i][1])} $")
    print("*" * 50)
    print("Менее 20 тыс. оклад имеют:")
    for i in range(len(new_list)):
        if float(new_list[i][1]) < 20000.0:
            print(str(new_list[i][0]))
    for i in range(len(new_list)):
        if float(new_list[i][1]) > 0:
            salary_list.append(float(new_list[i][1]))
    average_salary = (sum(salary_list)) / len(salary_list)
    print("*" * 50)
    print(f"Средний оклад составляет: {round(average_salary, 2)}")
