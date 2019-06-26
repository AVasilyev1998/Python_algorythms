from kurs_channel.Hamming_module import hamming_code, hamming_decode, binary_array_to_int, push_nulls
from kurs_channel.other_methods import int_to_binary_array
import time

#
# def code_file(file_name):
#     file = open(file_name, 'rb')
#     res = file.read()
#     res_bytes = []
#     for i in range(len(res)):
#         res_bytes.extend(int_to_binary_array(8, res[i]))
#     res_arr = []
#     for i in range(0, len(res_bytes)-11, 11):
#         tmp_arr = res_bytes[i:i+11]
#         tmp_arr = hamming_code(11, 15, binary_array_to_int(tmp_arr))
#         res_arr.extend(int_to_binary_array(15, tmp_arr))
#     while len(res_bytes) < 11:
#         res_bytes.append(0)
#     res_bytes = hamming_code(11, 15, binary_array_to_int(res_bytes))
#     res_arr.extend(int_to_binary_array(15, res_bytes))
#     return res_arr


def code_file(file_name):
    file = open(file_name, 'rb')
    res = file.read()
    print(res)
    res_bytes = []
    for i in range(len(res)):
        res_bytes.append(res[i])
    print(res_bytes)
    res_arr = []
    for i in range(0, len(res_bytes), 8):
        tmp_arr = res_bytes[i:i+8]
        bytes_arr = []
        for j in tmp_arr:
            bytes_arr.extend(int_to_binary_array(8, j))
        for k in range(1, len(bytes_arr)-11, 11):
            new_tmp = bytes_arr[i:i+11]
            res_arr.append(hamming_code(11, 15, binary_array_to_int(new_tmp)))
    ost = res_bytes[len(res_bytes)-len(res_bytes)%8:len(res_bytes)]
    ost_binary = []
    for m in ost:
        ost_binary.extend(int_to_binary_array(8, m))
    coded = []
    for each in range(0,len(ost_binary)-11,11):
        tmp = ost_binary[each:each+11]
        coded.extend(int_to_binary_array(15, hamming_code(11, 15, binary_array_to_int(tmp))))
    ost_ost = ost_binary[len(ost_binary)-len(ost_binary)%11:]
    while len(ost_ost) < 11:
        ost_ost.append(0)
    last = hamming_code(11, 15, binary_array_to_int(ost_ost))
    coded.extend(int_to_binary_array(15, last))
    res_arr.extend(coded)
    result = []
    for elem in res_arr:
        result.extend(int_to_binary_array(15, elem))
    print(result)
    return result


def decode_file(bin_arr):
    res_arr = []
    for i in range(0, len(bin_arr)-15, 15):
        tmp_arr = bin_arr[i:i+15]
        # res_arr.extend(hamming_decode(11, 15, tmp_arr))
        res_arr.extend(int_to_binary_array(15, hamming_decode(11, 15, binary_array_to_int(tmp_arr))))
    res_arr = res_arr[0:len(res_arr) - len(res_arr) % 8]
    res_arr = get_str(res_arr)
    return res_arr


def get_str(_arr):
    res_str = []
    tmp = []
    for i in range(0, len(_arr), 8):
        tmp = _arr[i:i+8]
        res_str.append(binary_array_to_int(tmp))
    result = bytes(res_str)
    return result


# now = time.time()
# res = code_file('test2.txt')
# res2 =
# after = time.time()
# print(after - now)

# def func_test(func_code,func_decode, in_file, res_file):
#     before = time.time()
#     coded = func_code(in_file)
#     decoded = func_decode(coded)
#     f = open(res_file, 'wb')
#     f.write(decoded)
#     after = time.time()
#     return after - before
#
#
# test_arr = []
# for i in range(10):
#     test_arr.append(func_test(code_file,decode_file, '2kb.txt', 'test_result.txt'))
# test_arr_res = open('test_time.txt', 'a')
# test_arr_res.write('\n')
# for i in test_arr:
#     test_arr_res.write(str(i))

now = time.time()
coded = code_file('text_encode.txt')
print(len(coded))
# decoded = decode_file(coded)
# res = get_str(decoded)
# f = open('new_res.txt', 'wb')
# f.write(res)
# after = time.time()
# print(after - now)