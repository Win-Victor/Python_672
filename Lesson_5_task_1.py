"""1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
my_f = open("test_1.txt", "w", encoding="utf-8")
new_line = input("Введите какой-нибудь текст\n")
while new_line:
    my_f.writelines([new_line, "\n"])
    new_line = input("Введите еще какой-нибудь текст\n")
    if not new_line:
        break
my_f.close()

print("Для проверки кода посмотрим содержимое файла\n")

with open("test_1.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line, end="")

with open("test_1.txt", "r", encoding="utf-8") as f:
    print(f.readlines())
