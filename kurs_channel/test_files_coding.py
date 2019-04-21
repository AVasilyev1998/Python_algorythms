#
# f = open('123.jpg', 'rb')
# res = f.read()
# with open('new.jpg','wb') as jpeg_file:
#     jpeg_file.write(res)


from kurs_channel.Hamming_module import hamming_code,hamming_decode,binary_array_to_int,int_to_binary_array,push_nulls


f = open('test.txt','rb')
res = f.read()
kfc_bytes = []
for i in range(len(res)):
    # print(hamming_code(4, 7, res[i]))
    # print(push_nulls(7, 11, int_to_binary_array(res[i])))
    print(int_to_binary_array(res[i]))