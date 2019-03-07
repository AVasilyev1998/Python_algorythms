def even_fibonacci(max):
    """
    Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
    """
    first = 1
    second = 2
    res = 2
    while second <= max:
        f = second
        second = first + second
        first = f
        if second % 2 == 0:
            res += second
    return res


print(even_fibonacci(4000000))