def xor_cipher(str_in, key):
    full_key = ''
    j = 0
    for i in range(len(str_in)):
        full_key += key[j]
        j += 1
        if j >= len(key):
            j = 0

    coded = list(map(lambda x,y: chr(ord(x) ^ ord(y)), str_in, full_key))
    return ''.join(coded)



