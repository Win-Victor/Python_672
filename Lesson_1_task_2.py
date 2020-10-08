# 2. Пользователь вводит время в секундах.
#  Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
#   Используйте форматирование строк.

time = int(input("Укажите время в секундах: ")) # сначала такой вариант был
hours = time // 3600
minutes = (time % 3600) // 60
seconds = time % 60
if hours < 10:
    hours = "0" + str(hours)
if minutes < 10:
    minutes = "0" + str(minutes)
if seconds < 10:
    seconds = "0" + str(seconds)
print(f'{hours}.{minutes}.{seconds}')

time = int(input("Укажите время в секундах: ")) # потом к такому пришел (ради эксперимента)
hours = int(time / 3600)
minutes = int((time - hours * 3600) / 60)
seconds = time - hours * 3600 - minutes * 60
print(f'{hours:02.0f}.{minutes:02.0f}.{seconds:02.0f}')

# {seconds:02.0f} - "0" заполняет пустые пространства, а "2" после "0" обзначает сколько символов будет слева от точки,
# аналогично с 0f - которые обозначают сколько символов после точки справа
