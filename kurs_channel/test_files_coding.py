from kurs_channel.Hamming_module import hamming_code, hamming_decode, binary_array_to_int
from kurs_channel.other_methods import int_to_binary_array
import time


def code_file(file_name):
    file = open(file_name, 'rb')
    res = file.read()
    res_bytes = []
    for i in range(len(res)):
        res_bytes.extend(int_to_binary_array(8, res[i]))
    res_arr = []
    for i in range(0, len(res_bytes)-11, 11):
        tmp_arr = res_bytes[i:i+11]
        tmp_arr = hamming_code(11, 15, tmp_arr)
        res_arr.extend(tmp_arr)
    while len(res_bytes) < 11:
        res_bytes.append(0)
    res_bytes = hamming_code(11, 15, res_bytes)
    res_arr.extend(res_bytes)
    return res_arr


def decode_file(bin_arr):
    res_arr = []
    for i in range(0, len(bin_arr)-15, 15):
        tmp_arr = bin_arr[i:i+15]
        res_arr.extend(hamming_decode(11, 15, tmp_arr))
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


def func_test(func_code,func_decode, in_file, res_file):
    before = time.time()
    coded = func_code(in_file)
    decoded = func_decode(coded)
    f = open(res_file, 'wb')
    f.write(decoded)
    after = time.time()
    return after - before


test_arr = []
for i in range(10):
    test_arr.append(func_test(code_file,decode_file, '2kb.txt', 'test_result.txt'))
test_arr_res = open('test_time.txt', 'a')
test_arr_res.write('\n')
for i in test_arr:
    test_arr_res.write(str(i))
