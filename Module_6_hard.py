# Дополнительное практическое задание по модулю: "Наследование классов."
#
# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
#
# Задание "Они все так похожи":
# 2D? 3D? Даже 4D?.... Настолько глубоко мы заходить конечно же не будем, 4D подождёт,
# но вот с двумерными и трёхмерными фигурами можем поэкспериментировать.
# Вы когда-нибудь задумывались как устроены графические библиотеки для языков программирования?
# Безусловно, там выполняются огромные расчёты при помощи вашей видеокарты, но...
# Что лежит в основе удобного использования таких объектов?
# По названию задачи можно понять, что все геометрические фигуры обладают схожими свойствами,
# такими как: длины сторон, цвет и др.
# Давайте попробуем реализовать простейшие классы для некоторых таких фигур и при этом применить наследование
# (в будущем, изучая сторонние библиотеки, вы будете замечать схожие классы, уже написанные кем-то ранее):
# Общее ТЗ:
# Реализовать классы Figure(родительский), Circle, Triangle и Cube,
# объекты которых будут обладать методами изменения размеров, цвета и т.д.
# Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны
# интерфейсы взаимодействия (методы) - геттеры и сеттеры.
#
# Подробное ТЗ:

# Атрибуты класса Figure: sides_count = 0
#
# Каждый объект класса Figure должен обладать следующими атрибутами:
#
# Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
# Атрибуты(публичные): filled(закрашенный, bool)
# И методами:
#
# Метод get_color, возвращает список RGB цветов.
# Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных
# значений перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне
# от 0 до 255 (включительно).
# Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
# предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
# Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны
# целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
# Метод get_sides должен возвращать значение я атрибута __sides.
# Метод __len__ должен возвращать периметр фигуры.
# Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count,
# то не изменять, в противном случае - менять.
#
# Атрибуты класса Circle: sides_count = 1
# Каждый объект класса Circle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
# Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
#
# Атрибуты класса Triangle: sides_count = 3
# Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)

# Атрибуты класса Cube: sides_count = 12
# Каждый объект класса Cube должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure.
# Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
# Метод get_volume, возвращает объём куба.
#
# ВАЖНО!
#
# При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count,
# то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
# Пример: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]

# Код для проверки:
#
# circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
# cube1 = Cube((222, 35, 130), 6)
#
# # Проверка на изменение цветов:
#
# circle1.set_color(55, 66, 77) # Изменится
# print(circle1.get_color())
# cube1.set_color(300, 70, 15) # Не изменится
# print(cube1.get_color())
#
# # Проверка на изменение сторон:
#
# cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
# print(cube1.get_sides())
# circle1.set_sides(15) # Изменится
# print(circle1.get_sides())
#
# # Проверка периметра (круга), это и есть длина:
#
# print(len(circle1))
#
# # Проверка объёма (куба):
#
# print(cube1.get_volume())
#
# Выходные данные (консоль):
#
# [55, 66, 77]
# [222, 35, 130]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [15]
# 15
# 216
#
#=======================

import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled=False):
        self.__sides = list(sides)
        self.__color = color
        self.filled = filled
        if len(self.__sides) != self.sides_count:
            self.__sides = [1] * self.sides_count

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        valid_values = 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255
        valid_types = isinstance(r, int) and isinstance(g, int) and isinstance(b, int)
        return valid_types and valid_values

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b

    def __is_valid_sides(self, *sides):
        is_valid_sides = True

        if len(sides) == self.sides_count:
            for side in sides:
                if not isinstance(side, int) or side <= 0:
                    is_valid_sides = False
                    break
        else:
            is_valid_sides = False

        return is_valid_sides

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            valid_sides = []
            for side in new_sides:
                valid_sides.append(side)

            self.__sides = valid_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, length, filled=False):
        super().__init__(color, length, filled=filled)
        self.radius = length / (2 * math.pi)

    def get_square(self):
        return math.pi * self.radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides, filled=False):
        super().__init__(color, *sides, filled=filled)

    def get_square(self):
        p = len(self) / 2
        sides = self.get_sides()
        return math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side, filled=False):
        sides = [side] * self.sides_count
        super().__init__(color, *sides, filled=filled)

    def get_volume(self):
        return self.get_sides()[0] ** 3


# Код для проверки:

circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:

circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:

cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:

print(len(circle1))

# Проверка объёма (куба):

print(cube1.get_volume())
