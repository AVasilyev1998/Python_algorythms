#
# f = open('123.jpg', 'rb')
# res = f.read()
# with open('new.jpg','wb') as jpeg_file:
#     jpeg_file.write(res)


from kurs_channel.Hamming_module import hamming_code, hamming_decode, binary_array_to_int, push_nulls
from kurs_channel.other_methods import old_int_to_binary_array, int_to_binary_array


f = open('test.txt','rb')
res = f.read()
res_bytes = []
for i in range(len(res)):
    res_bytes.extend(int_to_binary_array(8, res[i]))
print(res_bytes)
end_of_i = 0
while len(res_bytes) > 11:
    tmp_arr = res_bytes[0:10]
    print(tmp_arr)
    # TODO: do smth with tmp_arr
    res_bytes = res_bytes[10:].copy()


# def get_subarray(_from, _to, arr):
#     return arr[_from:_to]
#
#
# print(get_subarray(0, 10, res_bytes))
print(res_bytes[0:10])

