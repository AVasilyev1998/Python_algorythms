def is_simple(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    elif number == 3:
        return True
    elif number % 2 == 0:
        return False
    else:
        i = 3  # minimal simple num after 2
        while i*i <= number:
            if number % i == 0:
                return False
            i += 2

    return True


def factorize(number):
    """
    алгоритм факторизации числа (разложения на простые множители)
    :param number:
    :return: array
    """
    delims_array = set()
    iter = number-1
    remember_number = number
    while number > 1 and iter > 0:
        if number == 1:
            break
        if number % iter == 0:
            number /= iter
            delims_array.add(iter)
        iter -= 1
    if delims_array.__len__() == 1:
        delims_array.add(remember_number)
    return delims_array

print(factorize(1))






def nok(arr):
    """
    2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

    Какое самое маленькое число делится нацело на все числа от 1 до 20?
    :return: int
    """
    delimiters_set = set()


