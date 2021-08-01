# Задание 1

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'All right'
                else:
                    return f'Несуществующий год'
            else:
                return f'Несуществующий месяц'
        else:
            return f'Несуществующий день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('11 - 3 - 2001')
print(today)
print(Data.valid(11, 11, 2022))
print(today.valid(11, 13, 2011))
print(Data.extract('11 - 11 - 2010'))
print(today.extract('11 - 11 - 2021'))
print(Data.valid(1, 11, 2000))


# Задание 2

class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"На ноль делить нельзя")


div = DivisionByNull(10, 100)
print(DivisionByNull.divide(10, 0))
print(DivisionByNull.divide(10, 0.1))
print(div.divide(100, 0))


# Задание 3

class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        self.my_list = [int(i) for i in input('Введите значения через пробел: ').split()]
        val = int(input('Введите значения: '))
        self.my_list.append(val)
        while True:
            try:
                val = int(input('Введите значения: '))
                self.my_list.append(val)
                print(f'Ваш список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка и логическое значение")
                y_or_n = input(f'Попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'


try_except = Error(1)
print(try_except.my_input())


# Задание 4, 5, 6

class StoreMashines:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    # @classmethod
    # @staticmethod
    def reception(self):
        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите цену за ед '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Цена за штуку': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Данные: \n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Ваш склад: \n {self.my_store_full}')
            return f'Выход'
        else:
            return StoreMashines.reception(self)


class Printer(StoreMashines):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(StoreMashines):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(StoreMashines):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('HP', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())


# Задание 7

class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.x = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма x1 и x2 равна')
        return f'x = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение x1 и x2 равно')
        return f'x = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'x = {self.a} + {self.b} * i'


x_1 = ComplexNumber(5, 7)
x_2 = ComplexNumber(8, -4)
print(x_1)
print(x_1 + x_2)
print(x_1 * x_2)
