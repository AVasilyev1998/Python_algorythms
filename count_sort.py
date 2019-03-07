res = [0]*10
a = [1,3,4,3,2,2,1,2,4,6,7,8,9,4,3,2,1]

for i in a:
    res[i] += 1

print(res)

lst = []

for l in range(len(res)):
    for e in range(res[l]):
        print(l, end=' ')



print()
func = lambda a: a*2
print(func(4))