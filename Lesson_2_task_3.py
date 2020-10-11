# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons_dict = {
    "Весна": (3, 4, 5),
    "Лето": (6, 7, 8),
    "Осень": (9, 10, 11),
    "Зима": (12, 1, 2,)
}
month = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12: 'Декабрь'
}
while True:
    date = input(
        "Введите месяц в числовом выражении, от 1 до 12,\nгде цифре 1 соответствует месяц январь, 3 - март и т.д. ")
    if date.isdigit():
        date = int(date)
        if date < 1 or date > 12:
            print("Вы ввели не соответствующее значение")
            continue
        break
    else:
        print("Вы ввели не соответствующее значение")
        continue

values = seasons_dict.values()
items = seasons_dict.items()

for ind, i in enumerate(values):
    if date in i:
        user_season = (ind)

print(f"{date}'й месяц - {(month.get(date))} соответствует сезону '{list(items)[user_season][0]}'")
