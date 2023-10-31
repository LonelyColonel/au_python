"""
Классификация правильных многоугольников
"""


class RegularPolygon:
    """Класс правильного многоугольника"""
    """количество углов у многоугольника (в следущих использованиях всегда n)"""
    n: int
    """возвращаемое впоследствии значение угла"""
    a: float

    def __init__(self, n):
        self.n = n

    def get_the_angle_of_a_regular_polygon(self):
        """Функция для возвращения размера угла по их количеству"""
        a = ((self.n - 2)*180)/self.n
        return a

    def get_count_angle(self):
        """Функция, возвращающая количество углов у многоугольника"""
        return self.n

    def __repr__(self):
        """Специальный метод для человекочитаемого вывода"""
        return f'RegularPolygon n = {self.n}'


class Quadrilateral(RegularPolygon):
    """Класс прямоугольника (наследуется от класса правильного многоугольника)"""
    n: int
    """стороны a и b исходного прямоугольника"""
    a: float
    b: float

    def __init__(self, a, b):
        self.n = 4
        self.a = a
        self.b = b

    def get_quadril_perimeter(self):
        """Функция, возвращающая периметр произвольного прямоугольника"""
        return 2*(self.a + self.b)

    def get_quadril_area(self):
        """Функция, возвращающая площадь произвольного прямоугольника"""
        return self.a*self.b

    def __repr__(self):
        return f'Quadrilateral a = {self.a} b = {self.b}'


class Square(Quadrilateral):
    """Класс квадрата (наследуется от класса прямоугольника)"""
    n: int
    """сторона квадрата"""
    side: float

    def __init__(self, side):
        self.n = 4
        self.side = side

    def get_perimeter(self):
        """Функция, возвращаемая периметр квадрата"""
        return 4*self.side

    def get_square_area(self):
        """Функция, возвращаяющая площадь квадрата"""
        return self.side**2

    def __repr__(self):
        return f'Square side = {self.side}'


class Triangle(RegularPolygon):
    """Класс треугольника (наследуется от класса правильного многоугольника)"""
    n: int
    """стороны a и b и c исходного треугольника"""
    a: float
    b: float
    c: float

    def __init__(self, a, b, c):
        self.n = 3
        self.a = a
        self.b = b
        self.c = c

    def is_equilateral_triangle(self):
        """Функция, проверяющая равносторонний ли треугольник"""
        if self.a == self.b and self.b == self.c:
            return True
        else:
            return False

    def is_isosceles_triangle(self):
        """Функция, проверяющая равнобедренность исходного треугольника"""
        """Если треугольник уже равносторонни, то проверять дальше не нужно, он точно равнобедренный"""
        """Иначе проверяем все стороны попарно"""
        if self.is_equilateral_triangle():
            return True
        elif (self.a == self.b) or (self.b == self.c) or (self.c == self.a):
            return True
        else:
            return False

    def get_triangle_area(self):
        """Функция для вывода площади исходного треугольника по формуле Герона"""
        """Вычисляем полупериметр"""
        p = (self.a + self.b + self.c)/2
        """Вычисляем площадь"""
        s = (p*(p - self.a)*(p - self.b)*(p - self.c))**0.5
        return s

    def get_triangle_perimeter(self):
        """Функция для вывода периметра исходного треугольника"""
        return self.a + self.b + self.c

    def __repr__(self):
        return f'Triangle a = {self.a} b = {self.b} c = {self.c}'
