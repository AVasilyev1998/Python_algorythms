
def int_to_binary_array(num):
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
