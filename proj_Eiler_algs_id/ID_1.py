def get_multiple(max):
    """
    Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.

    Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
    """
    result = 0
    for i in range(max):
        if i % 3 == 0 or i % 5 == 0:
            result += i;
    if result == 0:
        result = -1
    return result


print(get_multiple(1000))