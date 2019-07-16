"""
Моя реализация класса рациональных чисел 16.07.2019
AVasilyev1998
"""


class Fractal:
    def __init__(self, value=0, dop=0):
        if dop == 0:
            self.value = value
        else:
            self.value = value / dop

    def __repr__(self):
        print('__repr__')
        return f'Fractal({self.value})'

    def __str__(self):
        print('__str__')
        return str(self.value)

    def __add__(self, other):
        print('__add__')
        if type(other) in (int, float):
            return Fractal(self.value + other)
        elif isinstance(other, Fractal):
            return Fractal(self.value + other.value)
        else:
            # не определено поведение для данных типов аргументов
            return NotImplemented

    def __radd__(self, other):
        print('__radd__')
        if type(other) in (int, float):
            return Fractal(other + self.value)
        else:
            return NotImplemented

    def __sub__(self, other):
        print('__sub__')
        if type(other) in (int, float):
            return Fractal(self.value - other)
        elif isinstance(other, Fractal):
            return Fractal(self.value - other.value)
        else:
            return NotImplemented

    def __rsub__(self, other):
        print('__rsub__')
        if type(other) in (int, float):
            return Fractal(other - self.value)
        else:
            return NotImplemented

    def __mul__(self, other):
        print('__mul__')
        if type(other) in (int, float):
            return Fractal(self.value * other)
        elif isinstance(other, Fractal):
            return Fractal(self.value * other.value)
        else:
            return NotImplemented

    def __rmul__(self, other):
        print('__rmul__')
        if type(other) in (int, float):
            return Fractal(other * self.value)
        elif isinstance(other, Fractal):
            return Fractal(other.value * self.value)
        else:
            return NotImplemented

    def __truediv__(self, other):
        print('__mul__')
        if type(other) in (int, float):
            return Fractal(self.value / other)
        elif isinstance(other, Fractal):
            return Fractal(self.value / other.value)
        else:
            return NotImplemented
    
    def __rtruediv__(self, other):
        print('__rtruediv__')
        if type(other) in (int, float):
            return Fractal(other / self.value)
        elif isinstance(other, Fractal):
            return Fractal(other.value / self.value)
        else:
            return NotImplemented
        
    def __pos__(self):
        print('__pos__')
        return self

    def __neg__(self):
        print('__neg__')
        return Fractal(-1 * self.value)

    def __abs__(self):
        print('__abs__')
        if self.value >= 0:
            return self
        else:
            return Fractal(-1 * self.value)

    def __mod__(self, other):
        print('__mod__')
        if type(other) in (int, float):
            return self.value % other
        elif isinstance(other, Fractal):
            return self.value % other.value
        else:
            return NotImplemented

    def __rmod__(self, other):
        print('__rmod__')
        if type(other) in (int, float):
            return other % self.value
        elif isinstance(other, Fractal):
            return other.value % self.value
        else:
            return NotImplemented

    def __lt__(self, other):
        print('__lt__')
        if type(other) in (int, float):
            if self.value < other:
                return True
            else:
                return False
        elif isinstance(other, Fractal):
            if self.value < other.value:
                return True
            else:
                return False
        else:
            return NotImplemented

    def __le__(self, other):
        print('__le__')
        if type(other) in (int, float):
            if self.value <= other:
                return True
            else:
                return False
        elif isinstance(other, Fractal):
            if self.value <= other.value:
                return True
            else:
                return False
        else:
            return NotImplemented

    def __gt__(self, other):
        print('__gt__')
        if type(other) in (int, float):
            if self.value > other:
                return True
            else:
                return False
        elif isinstance(other, Fractal):
            if self.value > other.value:
                return True
            else:
                return False
        else:
            return NotImplemented

    def __ge__(self, other):
        print('__ge__')
        if type(other) in (int, float):
            if self.value >= other:
                return True
            else:
                return False
        elif isinstance(other, Fractal):
            if self.value >= other.value:
                return True
            else:
                return False
        else:
            return NotImplemented

    def __eq__(self, other):
        print('__eq__')
        if type(other) in (int, float):
            if self.value == other:
                return True
            else:
                return False
        elif isinstance(other, Fractal):
            if self.value == other.value:
                return True
            else:
                return False
        else:
            return NotImplemented

    def __ne__(self, other):
        print('__ne__')
        if type(other) in (int, float):
            if self.value != other:
                return True
            else:
                return False
        elif isinstance(other, Fractal):
            if self.value != other.value:
                return True
            else:
                return False
        else:
            return NotImplemented


if __name__ == '__main__':
    f1 = Fractal(1)
    num = 3
    print(num + f1)
    print(f1 + num)
    # print(f1 + 'asd')
    print(f1 * 3)
    print(3 * f1)
    print(f1 / 2)
    print(2 / f1)

    # num = 3
    # otr_num = -3
    # print(num.__neg__())
    # print(otr_num.__neg__())
    # print(otr_num.__pos__())

    print(f1.__pos__())
    print(f1.__neg__())
    neg_f = Fractal(-230)
    print(neg_f.__abs__())
    print(neg_f.__neg__())
    print(neg_f.__pos__())

    print(Fractal(2, 4))

    print(Fractal(3) < 2)
    print(Fractal(3) < 6)
    print(Fractal(3) > 6)
    print(Fractal(3) >= 6)
    print(Fractal(3) <= 6)

    f = Fractal(2, 3)
    print(repr(f))
    print(Fractal(10.5) % 10)
    print(5 % Fractal(2.2))
    f -= 1
    print(f)