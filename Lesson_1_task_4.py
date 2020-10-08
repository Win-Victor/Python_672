# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Введите целое положительное число: "))
end_number = number % 10
max_number = end_number
while number != 0:
    if max_number == 9:
        break
    if end_number > max_number:
        max_number = end_number
    number //= 10
    end_number = number % 10
print(f"Cамая большая цифра в числе - {max_number}")
