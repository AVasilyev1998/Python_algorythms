def palindromic(num_of_bits):
    """
    Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром,
    полученное умножением двух двузначных чисел – 9009 = 91 × 99.

    Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
    :param num_of_bits:
    :return: number
    """
    






def is_palindromic(number):
    """

    :param number:
    :return: boolean
    """
    string = str(number)
    length = string.__len__()
    for i in range(int(length/2)+1):
        if string[i].__eq__(string[length-i-1]):
            pass
        else:
            return False
    return True


# tests for func is_palindromic
# print('test 1 - ', is_palindromic(10))
# print('test 2 - ', is_palindromic(9009))
# print('test 3 - ', is_palindromic(10))
# print('test 4 - ', is_palindromic(101))
# print('test 5 - ', is_palindromic(201))
# print('test 6 - ', is_palindromic(1))
# print('test 7 - ', is_palindromic(0))
# print('test 8 - ', is_palindromic(12300321))
