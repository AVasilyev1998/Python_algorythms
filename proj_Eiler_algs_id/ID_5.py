from isSimple import is_simple

def factorize(number):
    """
    алгоритм факторизации числа (разложения на простые множители)
    :param number:
    :return: array
    """
    # delims_array = set()
    delims_array = []
    if number < 0:
        return ArithmeticError
    elif number == 0 or number == 1:
        return list([number])
    elif is_simple(number):
        delims_array.append(1)
        delims_array.append(number)
        return delims_array
    iter = number-1
    while number > 1 and iter > 0:
        if number == 1:
            break
        if number % iter == 0:
            number /= iter
            if is_simple(iter):
                delims_array.append(iter)
            else:
                arr = list(factorize(iter))
                for i in arr:
                    delims_array.append(i)
        iter -= 1
    return delims_array



for i in range(20):
    print(i,'  -  ',factorize(i))


def nok(arr):
    """
    2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

    Какое самое маленькое число делится нацело на все числа от 1 до 20?
    :return: int
    """
    delimiters_set = set()


