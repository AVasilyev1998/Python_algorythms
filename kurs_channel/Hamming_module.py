from kurs_channel.other_methods import int_to_binary_array, binary_array_to_int


def hamming_code(_in, _out, int_num):
    """

    :param _in: bin_arr
    :param _out: int
    :param int_num: int
    :return: binary_arr
    """
    # binary_arr = int_to_binary_array(vector)
    nulled = push_nulls(_in, _out, int_num)
    coded_control_arr = code_control_bits(_out, nulled)
    res_control_bits_iter = 0
    for i in range(1, 15):
        if step(i):
            if coded_control_arr[res_control_bits_iter]:
                nulled += 2**(15-i)
            res_control_bits_iter += 1
        if res_control_bits_iter > coded_control_arr.__len__():
            break
    return nulled


# def hamming_decode(_in, _out, bin_arr):
#     """
#
#     :param _in: int
#     :param _out: int
#     :param bin_arr: ...
#     :return: bin_arr
#     """
#     in_bin_arr = bin_arr.copy()
#     count = 0
#     for i in range(0, _out):
#         if 2**i < _out:
#             count += 1
#     for i in [2**i for i in range(count)]:
#         bin_arr[i-1] = 0
#     # if in_bin_arr == hamming_code(_in, _out, binary_array_to_int(in_bin_arr)):
#     check_array = hamming_code(_in, _out, pop_nulls(_in, _out, bin_arr))
#     if in_bin_arr != check_array: # error cause of nulls pushed to vector casts it to wrong int
#         return 'Vector is broken'  # TODO: return exception or smth more useful than this
#     bin_arr = pop_nulls(11, 15, bin_arr)
#     return bin_arr


def hamming_decode(_in, _out, int_num):
    """

    :param _in: int
    :param _out: int
    :param int_num: ...
    :return: bin_arr??
    """
    input_int_num = int_num
    count = 0
    mask_to_get_control_bits = 26752  # !HARDCODE ALARM!
    mask_to_get_non_control_bits = 6015
    non_control_bits = int_num & mask_to_get_non_control_bits
    control_bits = int_num & mask_to_get_control_bits
    check_int = hamming_code(_in, _out, pop_nulls(_in, _out, int_num))
    if int_num != check_int:  # error cause of nulls pushed to vector casts it to wrong int
        return 'Vector is broken'  # TODO: return exception or smth more useful than this
    result_int = pop_nulls(11, 15, non_control_bits)
    return result_int


def step(num):
    if num in [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]:  # TODO: correct
        return True
    else:
        return False


def push_nulls(_in, _out, int_num):
        result = 0
        if int_num & 2**10:
            result += 2**12
        left_mask = 896
        left = int_num & left_mask
        left <<= 1
        result += left
        right_mask = 127
        right = int_num & right_mask
        result += right
        return result


# sum = 0
# for i in range(11):
#     sum += 2**i
# print(sum)
# print(int_to_binary_array(15, sum))
# print(int_to_binary_array(15, push_nulls(11, 15, 2047)))
# print( 2**9 + 2**8 + 2**7)


# print(push_nulls(11, 15, [1, 1, 0, 1, 0, 0, 0, 0, 1, 0]))


# def pop_nulls(_in, _out, vector):
#     result = []
#     for i in range(1, _out+1):
#         if not step(i):
#             result.append(vector[i-1])
#     return result


def pop_nulls(_in, _out, int_num):
    result = 0
    if _in == 11 and _out == 15:
        if int_num & 2**12:
            result += 2**10
        left = int_num & 1792  # mask left bits near 8th control - 2**10 + 2**9 + 2**8
        left >>= 1  # left shift(facepalm)  to pop one more control bit
        result += left
        right = int_num & 127  # mask right bits near 8th control - 2**6 + 2**5 + 2**4 + 2**3 + 2**2 + 2**1 + 1
        result += right
        return result
    else:
        return -1


def code_control_bits(_out, int_num):  # TODO: do
    int_vector = int_num
    res_masks: int = []
    # res_masks = []
    res_control_bits = []
    for i in generate_masks(_out):
        res_masks.append(int_vector & i)  # vector - array
        # print(res_masks)
    # print(locals())
    for j in res_masks:
        mask = j
        # print(mask)
        summary = 0
        for k in int_to_binary_array(_out, mask):
            if k == 1:
                summary += 1
        if summary % 2 == 0:
            res_control_bits.append(0)
        else:
            res_control_bits.append(1)
    return res_control_bits


def generate_masks(_out):
    # masks = [6148914691236517205, 3689348814741910323, 1085102592571150095,
    #          71777214294589695, 281470681808895, 4294967295]
    masks = [5461, 13107, 3855, 255]
    count_of_masks = 0
    i = 0
    while 2**i <= _out:
        count_of_masks += 1
        i += 1
    return masks[:count_of_masks]



# sum = 0
# for i in range(11):
#     sum += 2**i
# # print(sum)
# nulled = push_nulls(11, 15, 2074)
# print(int_to_binary_array(15, nulled))
# # print(15, push_nulls(11, 15, 2074))
# print(int_to_binary_array(15, hamming_code(11, 15, 2074)))
#
#

# TESTS
#
# if 90 == binary_array_to_int(hamming_code(4, 7, 10)):
#     print('TEST1 OK')
# else:
#     print('TEST1 ERROR')
#
# if 30737 == binary_array_to_int(hamming_code(11, 15, 1041)):
#     print('TEST2 OK')
# else:
#     print('TEST2 ERROR')
#
#
# if hamming_decode(4, 7, hamming_code(4, 7, 10)) == push_nulls(4, 7, [1, 0, 1, 0]):
#     print('OK')
#



