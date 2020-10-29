"""Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, name, param_1):
        self.name = name
        self.param_1 = param_1

    @abstractmethod
    def material_calc(self):
        pass

    def __add__(self, other):
        return self.material_calc + other.material_calc

class Coat(Clothes):
    @property
    def material_calc(self):
        return round(self.param_1/6.5 + 0.5, 2)

class Costume(Clothes):
    @property
    def material_calc(self):
        return round(2 * self.param_1 + 0.3, 2)

coat_1 = Coat("Грация", 22)
costum_1 = Costume("Кимоно", 5)
print(coat_1.name, coat_1.material_calc)
print(costum_1.name, costum_1.material_calc)
print("Общий подсчет расхода ткани:", coat_1 + costum_1)
