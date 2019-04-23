#
# f = open('123.jpg', 'rb')
# res = f.read()
# with open('new.jpg','wb') as jpeg_file:
#     jpeg_file.write(res)


from kurs_channel.Hamming_module import hamming_code, hamming_decode, binary_array_to_int, push_nulls, pop_nulls
from kurs_channel.other_methods import int_to_binary_array


def code_file(file_name):
    # f = open('test.txt','rb')
    f = open(file_name, 'rb')
    res = f.read()
    res_bytes = []
    for i in range(len(res)):
        res_bytes.extend(int_to_binary_array(8, res[i]))
    print(res_bytes)
    res_arr = []
    # l = len(res_bytes)
    while len(res_bytes) > 11:
        tmp_arr = res_bytes[0:11]
        # print(tmp_arr)
        # TODO: do smth with tmp_arr
        tmp_arr = hamming_code(11, 15, tmp_arr)
        res_arr.extend(tmp_arr)
        # print(res_arr)
        res_bytes = res_bytes[11:].copy()
    while len(res_bytes) < 11:
        res_bytes.append(0)
    res_bytes = hamming_code(11, 15, res_bytes)
    res_arr.extend(res_bytes)
    # print(res_arr)
    # print(len(res_arr), '  ', l)
    return res_arr


# print(code_file('test.txt'))


# def decode_file(bin_arr):
#     res_arr = []
#     while len(bin_arr) >= 15:
#         tmp_arr = bin_arr[0:15]
#         # print(tmp_arr)
#         res_arr.extend(hamming_decode(11, 15, tmp_arr))
#         bin_arr = bin_arr[15:].copy()
#     # getting round amount of bytes
#     result_arr = []
#     while len(res_arr) >= 8:
#         result_arr.extend(res_arr[0:8])
#         res_arr = res_arr[8:].copy()
#     return result_arr

def decode_file(bin_arr):
    res_arr = []
    for i in range(0, len(bin_arr)-15,15):
        tmp_arr = bin_arr[i:i+15]
        res_arr.extend(hamming_decode(11, 15, tmp_arr))
    res_arr = res_arr[0:len(res_arr) - len(res_arr) % 8]
    return res_arr


def get_str(_arr):
    res_str = []
    while len(_arr) >= 8:
        res_str.append((binary_array_to_int(_arr[0:8])))
        _arr = _arr[8:].copy()
    result = bytes(res_str)
    return result


arr = code_file('test.txt')
decoded = decode_file(arr)
res = get_str(decoded)
# print(res)
f = open('test_result.txt', 'wb')
f.write(res)

# arr = code_file('123.jpg')
# print(len(arr))
# # decoded = decode_file(arr)
# # res = get_str(decoded)
# print(len(decoded))
# f = open('newJPG123.jpg', 'wb')
# f.write(res)

# def get_subarray(_from, _to, arr):
#     return arr[_from:_to]
#
#
# print(get_subarray(0, 10, res_bytes))


# arr: bool = []
# arr.append(True)
# print(type(arr[0]))
# print(type(arr))
