"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""

with open("for_les_5_task_2.txt", encoding="utf-8") as f:
    print(f'Текст выбранного файла:\n"{f.read()}"')
    f.seek(0)
    my_list_str = f.readlines()
    print(f"\nВ файле содержится текст, состоящий из {len(my_list_str)} строк(а,и).\n")

    for num, i in enumerate(my_list_str):
        print(f"Количество слов в {num + 1}-й строке -  {len(my_list_str[num].split())}")
