"""3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное
деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****."""

class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return f"Результат сложения клеток: {self.quantity + other.quantity}"

    def __sub__(self, other):
        rez = self.quantity - other.quantity
        if rez > 0:
            return f"Результат вычитания клеток: {rez}"
        else:
            return "Разность количества ячеек двух клеток не больше нуля"

    def __mul__(self, other):
        return f"Результат умножения клеток: {self.quantity * other.quantity}"

    def __truediv__(self, other):
        return f"Результат деления клеток: {self.quantity // other.quantity}"

    def make_order(self, size_line):
        line = f'{"*" * size_line}\n'
        line_count = self.quantity // size_line
        end_line = f'{"*" * (self.quantity % size_line)}\n'
        text = 'Rezult make_order: \n'
        if line_count < 1:
            print(text + end_line)
        else:
            print(text + (line * line_count) + end_line)

c1 = Cell(2)
c2 = Cell(5)
print(c1 + c2)
print(c2 - c1)
print(c2 * c1)
print(c2 / c1)
c3 = Cell(100)
c3.make_order(8)
