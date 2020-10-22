"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('text_4.txt', encoding="utf-8") as f:
    for i in f:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + ' ' + i[1])

with open('result_task_4.txt', 'w+', encoding="utf-8") as f:
    f.writelines(new_file)

print("\nПроверяем результат\n")

with open('result_task_4.txt', encoding="utf-8") as f:
    print(f.read())
