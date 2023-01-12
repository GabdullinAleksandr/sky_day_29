import math


class Derivative:
    def __init__(self, f):
        self.f = f

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.f(x + dx) - self.f(x)) / dx


@Derivative
def sin_(x):
    return math.sin(x)


# print(sin_(math.pi/3))


class Flight:
    def __init__(self, city_from, city_to):
        self.__city_from = city_from
        self.__city_to = city_to

    def __str__(self):
        return f'Flight from {self.__city_from} to {self.__city_to}'


# print(Flight(input(), input()))


class MyInt(int):
    def __add__(self, other):
        return super().__add__(int(other))
    def __sub__(self, other):
        return super().__sub__(int(other))
    def __mul__(self, other):
        return super().__mul__(int(other))
    def __truediv__(self, other):
        return super().__truediv__(int(other))
    def __floordiv__(self, other):
        return super().__floordiv__(int(other))
    def __mod__(self, other):
        return super().__mod__(int(other))
    def __eq__(self, other):
        return super().__eq__(int(other))
    def __ne__(self, other):
        return super().__ne__(int(other))
    def __lt__(self, other):
        return super().__lt__(int(other))
    def __gt__(self, other):
        return super().__gt__(int(other))
    def __le__(self, other):
        return super().__le__(int(other))
    def __ge__(self, other):
        return super().__le__(int(other))


# a = MyInt(3)
#
# print(a == 0)
# print(a != '2')
# print(a >= '1')
# x = a * 5
# s = a * '5'
# d = a + '1'
# f = a / 10
# print(x, s, d, f, sep='\n')
