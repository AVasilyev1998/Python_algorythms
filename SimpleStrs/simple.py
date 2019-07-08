import random

file = open('pwd.txt', 'r')

content = file.read().splitlines()
# print(content)
res_dict = {}
pas_set = set()
pas_dict = dict()
for i in content:
    tmp = i.split(';')
    res_dict[tmp[0]] = tmp[1]
    pas_set.add(tmp[1])
    if pas_dict.get(tmp[1]):
        pas_dict[tmp[1]] += 1
    else:
        pas_dict[tmp[1]] = 1
# print(pas_set)
print(pas_dict)

famous_pas = ''
famous_max = 0
for k,v in pas_dict.items():
    # print(k,v)
    if v > famous_max:
        famous_pas = k
        famous_max = v


print(famous_pas,' ', famous_max)