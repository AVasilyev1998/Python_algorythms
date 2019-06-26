import math


def square(side):
    return side * 4, side * side, math.sqrt(side * side * 2)


# TEST1
if square(2) == (8, 4, math.sqrt(2 * 2 * 2)):
    print("TEST1 OK")
else:
    print("TEST1 ERROR")

# TEST2
if square(6) == (6 * 4, 6 * 6, math.sqrt(6 * 6 * 2)):
    print("TEST2 OK")
else:
    print("TEST2 ERROR")
