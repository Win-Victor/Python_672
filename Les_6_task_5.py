'''5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.'''


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"В руках {self.title}. Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print(f"В руках {self.title}, \x1B[3mрисуем ручкой.\x1B[23m")


class Pencil(Stationery):
    def draw(self):
        print(f"В руках {self.title}, р и с у е м   к а р а н д а ш о м.")


class Handle(Stationery):
    def draw(self):
        print(f"В руках {self.title}, Р И С У Е М   М А Р К Е Р О М.")


my_sing = Stationery("Моя канцелярская принадлежность")
my_sing.draw()

my_pen = Pen("Parker")
my_pen.draw()

my_pensil = Pencil("luxor")
my_pensil.draw()

my_handle = Handle("Office_mag")
my_handle.draw()


class IncomprehensibleThing(Pen, Pencil, Handle):
    pass


new_stat = IncomprehensibleThing("IT")
new_stat.draw()
