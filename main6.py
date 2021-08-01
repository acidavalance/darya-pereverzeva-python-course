# Задание 1


import time
import itertools


class Traffic:
    __color = [['red', [7, 31]], ['yellow', [2, 33]], ['green', [5, 32]]]

    def running(self):
        for light in itertools.cycle(self.__color):
            print(f'\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m', end="")
            time.sleep(light[1][0])


traffic1 = Traffic()
traffic1.running()


# Задание 2


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_full_profit(self, weight=25, thickness=5):
        return f'{self._length} m * {self._width} m * {weight} kg * {thickness} sm =' \
               f' {(self._length * self._width * weight * thickness) / 1000} t'


road1 = Road(3000, 10)
print(road1.get_full_profit())


# Задание 3


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{sum(self._income.values())}'


stuff = Position('John', 'Brown', 'S1', 20000, 10000)
print(stuff.get_full_name())
print(stuff.position)
print(stuff.get_total_income())


# Задание 4
# Тут я не поняла ошибки...


class Car:
    '''Машинка'''

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Машина: {self.name} (цвет {self.color}) полицейская - {self.is_police}')

    def run(self):
        print(f'{self.name}: Едет')

    def stop(self):
        print(f'{self.name}: Стоит')

    def turn(self, direction):
        print(f'{self.name}: Свернула {"налево" if direction == 0 else "направо"}')

    def total_speed(self):
        return f'{self.name}: Скорость: {self.speed}'


class TownCar:
    '''Городская тачка'''

    def total_speed(self):
        return f'{self.name}: Скорость: {self.speed}. Превышение!' \
            if self.speed > 60 else f'{self.name}: Скорость: {self.speed}'


class WorkCar:
    '''Рабочая машина'''

    def total_speed(self):
        return f'{self.name}: Скорость: {self.speed}. Превышение!' \
            if self.speed > 40 else f'{self.name}: Скорость: {self.speed}'


class SportCar:
    '''Спортивное авто'''


class PoliceCar:
    '''Полицейская машина'''

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police = PoliceCar('"Тюрьма на колесах"', 'белая', 80)
police.run()
print(police.total_speed())
police.turn(0)
police.stop()
print()

worky = WorkCar('"Рабочая лошадка"', 'зеленая', 40)
worky.run()
worky.turn(1)
print(worky.total_speed())
worky.turn(0)
worky.stop()
print()

print()
sporty = SportCar('"Спиди-тачка"', 'красная', 120)
sporty.run()
sporty.turn(0)
print(sporty.total_speed())
sporty.stop()
print()

towny = TownCar('"Автошка"', 'серебристая', 55)
towny.run()
towny.turn(1)
towny.turn(0)
print(towny.total_speed())
towny.stop()
print()

print(f'\nАвтомобиль {towny.name} (цветом {towny.color}')
print(f'Автомобиль {police.name} (цветом {police.color}')


# Задание 5

class Stationery:
    def __init__(self, title='Инструмент рисования: '):
        self.title = title

    def draw(self):
        print(f'Приступил к рисованию! {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Начал рисовать {self.title} ручкой!')


class Pencil(Stationery):
    def draw(self):
        print(f'Начал рисовать {self.title} карандашом!')


class Handle(Stationery):
    def draw(self):
        print(f'Начал рисовать {self.title} маркером!')


stat = Stationery()
stat.draw()
pen = Pen('гелевой')
pen.draw()
pencil = Pencil('мягким')
pencil.draw()
handle = Handle('ярким')
handle.draw()