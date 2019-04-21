
# def int_to_binary_array(target_length, num): # TODO: refactor this shit
#     """
#         :param target_length int
#         :param num int
#         :return binary_array
#     """
#     s = str(bin(num))
#     binary = []
#     for i in s[2:]:
#         if i == '1':
#             binary.append(1)
#         else:
#             binary.append(0)
#     corrected_binary = []
#     if binary.__len__() != target_length:
#         for i in range(target_length - binary.__len__()):
#             corrected_binary.append(0)
#         corrected_binary.extend(binary)
#         print(corrected_binary)
#     return corrected_binary
#
#
# print(int_to_binary_array(12, 32))


def int_to_binary_array(num): # TODO: write target vector length add 0 to front 00....
    """
    :param num int
    :return binary_array
    """
    s = str(bin(num))
    binary = []
    for i in s[2:]:
        if i == '1':
            binary.append(1)
        else:
            binary.append(0)
    return binary


# print('TEST 1 32 - ', int_to_binary_array(32))


def binary_array_to_int(arr):
    """
    :param arr array
    :return int
    """
    res = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            res += 2**(len(arr)-1-i)
    return res


# print('TEST 2', binary_array_to_int([1, 0, 1, 0]))
