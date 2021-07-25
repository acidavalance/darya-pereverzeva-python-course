# Задание 1

class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))


matrixx = Matrix([[7, 12, 11],
                  [5, 17, 18],
                  [27, 6, 1]],
                 [[49, 8, 3],
                  [9, 10, 56],
                  [35, 14, 82]])

print(matrixx.__add__())


# Задание 2

class Cloth:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_c(self):
        return self.width / 6.5 + 0.5

    def get_square_j(self):
        return self.height * 2 + 0.3

    @property
    def get_square(self):
        return str(f'Размер ткани: \n'
                   f'{(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Cloth):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Размер ткани для пальто: {self.square_c}'


class Jacket(Cloth):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Размер ткани для жакета: {self.square_j}'


coat = Coat(2, 4)
jacket = Jacket(1, 2)
print(coat)
print(jacket)
print(coat.get_square)
print(jacket.get_square)
print(jacket.get_square_c())
print(jacket.get_square_j())


# Задание 3

class Cell:
    def __init__(self, nums):
        self.nums = nums

    def order(self, rows):
        return '\n'.join(['*' * rows for i in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return f'{self.nums}'

    def __add__(self, other):
        print('Сумма клеток равна: ')
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print('Вычитание клеток равно: ')
        return Cell(self.nums - other.nums)

    def __mul__(self, other):
        print('Умножение клеток равно: ')
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print('Деление клеток равно: ')
        return Cell(self.nums // other.nums)


cell_1 = Cell(12)
cell_2 = Cell(5)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
