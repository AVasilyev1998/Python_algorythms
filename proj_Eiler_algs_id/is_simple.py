def is_simple(number):
    """
    идентификация простого числа
    :param number:
    :return: boolean
    """
    if type(number) != int:
        return None
    elif number < 0:
        return None
    elif number == 0:
        return None
    elif number == 1:
        return False
    elif number == 2 or number == 3:
        return True
    elif number % 2 == 0:
        return False
    else:
        i = 3  # 3 - второе простое число
        while i*i <= number:
            if number % i == 0:
                return False
            i += 2
    return True


# tests

# TEST 1 прогон массива простых чисел(первых 20)
simple_nums_array = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
test1_err_flag = False
for num in simple_nums_array:
    if not is_simple(num):
        print('TEST1 ',num,' - ERROR')
        test1_err_flag = True
if not test1_err_flag:
    print('TEST1 Successful')

# TEST 2 отрицательные числа
if is_simple(-20) is not None:
    print('TEST2', 'negative int exception')
else:
    print('TEST2', 'Successful')

# TEST 3 null
if is_simple(0) is not None:
    print('TEST3', ' null exception')
else:
    print('TEST3', 'Successful')

# TEST 4 double float ... (not int numbers)
if is_simple(1.2) and is_simple(1e2):
    print('TEST4', 'error type exception')
else:
    print('TEST4', 'Successful')

# TEST 5
