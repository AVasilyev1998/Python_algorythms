#
# arr: bool = []
# for i in range(0, 63):
#     if i % 2 == 0:
#         arr.append(1)
#     else:
#         arr.append(0)
#
# print(arr)
# print(len(arr))
#
# #
# # buffer = str(arr)
# #
# # buffer = buffer[1:len(buffer)]
# # print(buffer)
#
# buffer = 0
# for i in range(63):
#     if arr[i] == 1:
#         buffer += 2**(62-i)
# print(buffer)

# second mask
# buffer = 0
# for i in range(1, 63, 4):
#     buffer += 2**(62-i) + 2**(61-i)
# print(buffer)
#end second mask


# third mask
# buffer = 0
# for i in range(3, 64, 8):
#     buffer += 2**(62-i) + 2**(61-i) + 2**(60-i) + 2**(59-i)
# print(buffer)
# end third mask

# fourth mask
# buffer = 0
# for i in range(7, 64, 16):
#     buffer += 2**(62-i) + 2**(61-i) + 2**(60-i) + 2**(59-i) + 2**(58-i) + 2**(57-i) + 2**(56-i) + 2**(55-i)
# print(buffer)
#end fourth mask

# fifth mask
# buffer = 0
# for i in range(15, 64, 32):
#     buffer += 2**(62-i) + 2**(61-i) + 2**(60-i) + 2**(59-i) + 2**(58-i) + 2**(57-i) + 2**(56-i) + 2**(55-i) + 2 ** (54 - i) + 2 ** (53 - i) + 2 ** (52 - i) + 2 ** (51 - i) + 2 ** (50 - i) + 2 ** (49 - i) + 2 ** (
#                 48 - i) + 2 ** (47 - i)
# print(buffer)
#end fifth mask


# sixth mask
# buffer = 0
# i = 31
# buffer += 2**(62-i) + 2**(61-i) + 2**(60-i) + 2**(59-i) + 2**(58-i) + 2**(57-i) + 2**(56-i) + 2**(55-i) + 2 ** (54 - i) + 2 ** (53 - i) + 2 ** (52 - i) + 2 ** (51 - i) + 2 ** (50 - i) + 2 ** (49 - i) + 2 ** (
#                 48 - i) + 2 ** (47 - i) + 2**(46-i) + 2**(45-i) + 2**(44-i) + 2**(43-i) + 2**(42-i) + 2**(41-i) + 2**(40-i) + 2**(39-i) + 2 ** (38 - i) + 2 ** (37 - i) + 2 ** (36 - i) + 2 ** (35 - i) + 2 ** (34 - i) + 2 ** (33 - i) + 2 ** (
#                 32 - i) + 2 ** (31 - i)
# print(buffer)
#end sixth mask


# MASKS FOR 11 15

# buffer = 0
# for i in range(2, 15, 2):
#     buffer += 2**(14-i)
# print(buffer)
# #
# buffer = 0
# for i in range(1, 15, 4):
#     buffer += 2**(14-i) + 2**(13-i)
# print(buffer)
# # # end second mask
# #
# buffer = 0
# for i in range(3, 15, 8):
#     buffer += 2**(14-i) + 2**(13-i) + 2**(12-i) + 2**(11-i)
# print(buffer)
# #
# buffer = 0
# for i in range(7, 15, 16):
#     buffer += 2**(14-i) + 2**(13-i) + 2**(12-i) + 2**(11-i) + 2**(10-i) + 2**(9-i) + 2**(8-i) + 2**(7-i)
# print(buffer)