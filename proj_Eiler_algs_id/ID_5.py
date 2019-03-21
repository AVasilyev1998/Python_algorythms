from isSimple import is_simple





# def nok(arr):
#     """
#     2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
#
#     Какое самое маленькое число делится нацело на все числа от 1 до 20?
#     :return: int
#     """
#     delimiters_set = set()
#

# def factorize(number):
#     """
#     алгоритм факторизации числа (разложения на простые множители)
#     :param number:
#     :return: array
#     """
#     # delims_array = set()
#     delims_array = []
#     if number < 0:
#         return ArithmeticError
#     elif number == 0 or number == 1:
#         return list([number])
#     elif is_simple(number):
#         delims_array.append(1)
#         delims_array.append(number)
#         return delims_array
#     iter = number-1
#     while number > 1 and iter > 0:
#         if number == 1:
#             break
#         if number % iter == 0:
#             number /= iter
#             if is_simple(iter):
#                 delims_array.append(iter)
#             else:
#                 arr = list(factorize(iter))
#                 for i in arr:
#                     delims_array.append(i)
#         iter -= 1
#     return delims_array

def factorize(number):
    delims_arr = []
    if number % 2 == 0:
        number /= 2
        delims_arr.append(2)
    iter = 3
    if is_simple(number):
        return list([1,number])
    else:
        while number > 1 and iter <= number:
            if number % iter == 0:
                number /= iter
                delims_arr.append(iter)
            iter += 2
    return delims_arr


result_set = set()
for i in range(21):
    for j in factorize(i):
        result_set.add(j)
print(result_set)

res = 1

for i in range(1,11):
    res *= i
print(res)
