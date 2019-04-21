from kurs_channel.other_methods import int_to_binary_array, binary_array_to_int


def hamming_code(_in, _out, vector):
    """

    :param _in: int
    :param _out: int
    :param vector: int
    :return: binary_arr
    """
    binary_arr = int_to_binary_array(vector)
    nulled = push_nulls(_in, _out, binary_arr)
    coded_arr = code_control_bits(_out, nulled)
    return coded_arr


def hamming_decode(_in, _out, bin_arr):
    """

    :param _in: int
    :param _out: int
    :param bin_arr: ...
    :return: bin_arr
    """
    in_bin_arr = bin_arr.copy()
    count = 0
    for i in range(0, _out):
        if 2**i < _out:
            count += 1
    for i in [2**i for i in range(count)]:
        bin_arr[i-1] = 0
    # if in_bin_arr == hamming_code(_in, _out, binary_array_to_int(in_bin_arr)):
    check_array = hamming_code(_in, _out, binary_array_to_int(pop_nulls(_in, _out, bin_arr)))
    if not bin_arr_comparison(in_bin_arr, check_array): # error cause of nulls pushed to vector casts it to wrong int
        return 'Vector is broken' # TODO: return exception or smth more usefull than this
    return bin_arr


def bin_arr_comparison(lst1, lst2):
    if len(lst1) == len(lst2):
        for i in range(len(lst1)):
            if lst1[i] != lst2[i]:
                return False
    else:
        return False
    return True

# bin_arr_comparison tests:
# print(bin_arr_comparison([1, 0, 1], [1, 0, 1, 1]))
# print(bin_arr_comparison([1, 0, 1], [1, 0, 1]))
# print(bin_arr_comparison([1, 0, 1], [1, 0, 0]))
# print(bin_arr_comparison([0, 0, 1], [1, 0, 0]))
# print(bin_arr_comparison([1, 1, 1], [1, 0, 1]))


def step(num):
    if num in [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]:  # TODO: correct
        return True
    else:
        return False


def push_nulls(_in, _out, vector):
    # push nulls
    # nulled: bool = []
    nulled = []
    j = 0
    for i in range(1, _out+1):
        if step(i):
            nulled.append(0)
        else:
            nulled.append(vector[j])
            j += 1
    return nulled


def pop_nulls(_in, _out, vector):
    result = []
    for i in range(1, _out+1):
        if not step(i):
            result.append(vector[i-1])
    return result

#tests for pop nulls
# print(pop_nulls(4, 7, [0, 0, 1, 0, 0, 1, 0]))
# print(pop_nulls(11, 15, [0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1]))


def code_control_bits(_out, vector):  # TODO: do
    int_vector = binary_array_to_int(vector)
    # res_masks: int = []
    res_masks = []
    res_control_bits = []
    for i in generate_masks(_out):
        res_masks.append(int_vector & i)  # vector - array
        # print(res_masks)
    for j in res_masks:
        mask = j
        summary = 0
        for k in int_to_binary_array(mask):
            if k == 1:
                summary += 1
        if summary % 2 == 0:
            res_control_bits.append(0)
        else:
            res_control_bits.append(1)
    res_control_bits_iter = 0
    for i in range(1, len(vector)):
        if step(i):
            vector[i-1] = res_control_bits[res_control_bits_iter]
            res_control_bits_iter += 1
    return vector


def generate_masks(_out):
    # masks: int =
    masks = [6148914691236517205, 3689348814741910323, 1085102592571150095,
             71777214294589695, 281470681808895, 4294967295]
    count_of_masks = 0
    i = 0
    while 2**i <= _out:
        count_of_masks += 1
        i += 1
    return masks[:count_of_masks]



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



