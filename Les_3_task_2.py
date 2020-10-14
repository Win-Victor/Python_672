# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def facebook(name, surname, birth_year, city, email, tel):
    return f'name: {name}, surname: {surname}, birth_year: {birth_year}, city: {city}, email: {email}, tel: {tel}'


print(facebook(city="Voronezh", surname="Vinnikov", name="Victor", birth_year=1982, email="win-victor@mail.ru",
               tel="230-20-69"))

print(facebook(input('Enter name: ').title(), input('Enter surname: ').title(), input('birth_year: '),
               input('city: ').title(), input('email: '), input('tel: ')))

def personal(**kwargs):
    return (kwargs)


print(personal(name=input('Укажите свое имя ').title(), surname=input('Укажите свою фамилию ').title(),
               birth_year=int(input('Укажите год рождения ')), city=input('Укажите город проживания ').title(),
               email=input('Укажите свой email ').lower(), tel=int(input('Укажите свой телефон '))))
