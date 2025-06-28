import math


def square(side):
    if isinstance(side, int):
        return side ** 2
    else:
        # Округляем вверх площадь, если сторона была дробная
        return math.ceil(side ** 2)


print(square(5))
print(square(7.8))
