"""
Моя реализация класса рациональных чисел 16.07.2019
AVasilyev1998
"""


class Fractal:
    def __init__(self, value=0):
        self.value = value

    def __repr__(self):
        return f'Fractal({self.value})'

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


if __name__ == '__main__':
    f1 = Fractal(1)
    num = 3
    print(num + f1)
    print(f1 + num)
    print(f1 + 'asd')
