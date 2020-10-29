"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
матрицы складываем с первым элементом первой строки второй матрицы и т.д."""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def print_matrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print("{:4d}".format(self.matrix[i][j]), end="")
            print()

    def __str__(self):
        return '\n'.join([' '.join([str(i) for i in line]) for line in self.matrix])

    def __add__(self, other):
        new_matrix = []
        for i in range(len(self.matrix)):
            new_matrix.append([])
            for j in range(len(self.matrix[i])):
                new_matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
        return '\n'.join(map(str, new_matrix))


m_1 = Matrix([[1, 2], [2, 3], [3, 4]])
m_2 = Matrix([[3, 4], [4, 5], [5, 6]])

print("Первая матрица: \n", m_1)
print("*" * 30)
print(m_2)
print("*" * 30)
print(m_1 + m_2)
