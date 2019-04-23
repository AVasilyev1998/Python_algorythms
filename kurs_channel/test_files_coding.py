#
# f = open('123.jpg', 'rb')
# res = f.read()
# with open('new.jpg','wb') as jpeg_file:
#     jpeg_file.write(res)


from kurs_channel.Hamming_module import hamming_code, hamming_decode, binary_array_to_int, push_nulls
from kurs_channel.other_methods import old_int_to_binary_array, int_to_binary_array


def code_file(file_name):

    # f = open('test.txt','rb')
    f = open(file_name,'rb')
    res = f.read()
    res_bytes = []
    for i in range(len(res)):
        res_bytes.extend(int_to_binary_array(8, res[i]))
    print(res_bytes)
    res_arr = []
    l = len(res_bytes)
    while len(res_bytes) > 11:
        tmp_arr = res_bytes[0:11]
        # print(tmp_arr)
        # TODO: do smth with tmp_arr
        tmp_arr = hamming_code(11, 15, tmp_arr)
        res_arr.extend(tmp_arr)
        print(res_arr)
        res_bytes = res_bytes[11:].copy()
    res_bytes = hamming_code(11, 15, int_to_binary_array(11, binary_array_to_int(res_bytes)))
    res_arr.extend(res_bytes)
    print(res_arr)
    print(len(res_arr), '  ', l)
# def get_subarray(_from, _to, arr):
#     return arr[_from:_to]
#
#
# print(get_subarray(0, 10, res_bytes))


