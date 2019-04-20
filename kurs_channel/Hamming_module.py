from kurs_channel.other_methods import int_to_binary_array, binary_array_to_int


def hamming_code(_in, _out, vector):
    binary_arr = int_to_binary_array(vector)
    nulled = push_nulls(_in, _out, binary_arr)
    res_masks = code_control_bits(_out, nulled)
    return res_masks


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


def step(num):
    if num in [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]:  # TODO: correct
        return True
    else:
        return False


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

if 90 == binary_array_to_int(hamming_code(4, 7, 10)):
    print('TEST1 OK')
else:
    print('TEST1 ERROR')

if 30737 == binary_array_to_int(hamming_code(11, 15, 1041)):
    print('TEST2 OK')
else:
    print('TEST2 ERROR')


