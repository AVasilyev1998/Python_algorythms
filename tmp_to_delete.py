from kurs_channel.other_methods import int_to_binary_array, binary_array_to_int


summary = 0
for i in range(15):
    if i != 7 and i != 11 and i != 13 and i != 14:
        summary += 2**i
print(summary)
print(int_to_binary_array(15, summary))
int_num = int_to_binary_array(15, 21111)
print(int_num)
res = 21111 & summary
print(int_to_binary_array(15, res))

mask_to_get_control_bits = 2**14+2**13+2**11+2**7
print(mask_to_get_control_bits)