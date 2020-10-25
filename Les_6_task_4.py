'''4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.'''


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name}, цвет {self.color} поехала со скоростью {self.speed} км/ч\n")

    def stop(self):
        print(f"{self.name} остановилась\n")

    def turn(self, direction):
        if direction == "right":
            print(f"{self.name} повернула направо\n")
        elif direction == "left":
            print(f"{self.name} повернула налево\n")

    def show_speed(self):
        print(f"Скорость машины {self.name}, цвет {self.color}: {self.speed}\n")

    def police(self):
        if self.is_police is True:
            print("Данный автомобиль является специальным транспортным средством полиции г. Москва")
        else:
            print("Данный автомобиль не является специальным транспортным средством МВД России")


class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if int(self.speed) > 60:
            print(
                f"Скорость машины {self.name}: {self.speed}"
                f"- Превышение скорости!!!\nМаксимально допустимая скорость - 60 км/ч\n")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if int(self.speed) > 40:
            print(
                f"Скорость машины {self.name}: {self.speed}"
                f" - Превышение скорости!!!\nМаксимально допустимая скорость - 40 км/ч\n")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, flashing_beacons):
        self.flashing_beacons = flashing_beacons
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.flashing_beacons == "off":
            if int(self.speed) > 60:
                print(
                    f"На ТС отключены проблесковые маячки. Скорость машины: {self.speed} км/ч - Превышение скорости!!!"
                    f"\nМаксимально допустимая скорость без включенных проблесковых маячков - 60 км/ч\n")
            else:
                print(f"Скорость машины {self.name}: {self.speed} км/ч\n")
        else:
            print(
                f"На ТС {self.name} включены проблесковые маячки. Скорость машины: {self.speed} км/ч\n")


t = TownCar(90, "белый", "ВАЗ 2109", False)
t.police()
t.go()
t.stop()
t.turn("left")
t.show_speed()

w = WorkCar(75, "баклажан", "Лада седан", False)
w.police()
w.go()
w.stop()
w.turn("left")
w.show_speed()

s = SportCar(320, "yellow", "Lamborghini Diablo", False)
s.police()
s.go()
s.stop()
s.turn("right")
s.show_speed()

niva = PoliceCar(60, "Белый", "Chevrolet Niva", True, "off")
niva.police()
niva.go()
niva.turn("left")
niva.show_speed()
niva.stop()

patriot = PoliceCar(95, "Черный", "УАЗ Патриот", True, "off")
patriot.go()
patriot.police()
patriot.turn("left")
patriot.show_speed()
patriot.flashing_beacons = 'on'
patriot.show_speed()
patriot.stop()

uaz = PoliceCar(120, "Green", "Козик", True, "on")
uaz.go()
uaz.police()
uaz.turn("left")
uaz.show_speed()
uaz.stop()

u = TownCar(45, "Фиолетовый", "NoName", False)
u.go()
u.turn("right")
u.stop()
u.show_speed()
u.police()
