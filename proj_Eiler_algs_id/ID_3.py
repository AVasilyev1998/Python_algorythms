def even(number):
    """
        even -> True
        odd -> False
    :param number:
    :return: boolean
    """
    if number % 2 == 0:
        return True
    else:
        return False


def is_simple(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    elif number == 3:
        return True
    elif even(number):
        return False
    else:
        i = 3  # minimal simple num after 2
        while i*i <= number:
            if number % i == 0:
                return False
            i += 2

    return True


# print(6,is_simple(6))
# print(7,is_simple(7))
# print(8,is_simple(8))
# print(367,is_simple(367))


def nod(num):
    """
    Простые делители числа 13195 - это 5, 7, 13 и 29.

    Каков самый большой делитель числа 600851475143, являющийся простым числом?
    """
    variable = 1
    max_simple = 1

    while variable*variable < num:  # смотрим все var ограниченные данным значением тк далее множители будут повторяться
        if num % variable == 0 and max_simple < variable and is_simple(variable):
            max_simple = variable
        variable += 2  # идем по нечетным тк все четные больше 2 уже по определению не простые
    return max_simple


print(nod(600851475143))