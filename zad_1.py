"""

"""
def make2019():
    arr = [False]*2019
    return arr

def goThrough2019(array):
    for i in range(1,2020): # i e [1,2020)
        for k in range(0,2019):
            if k % i == 0:
                if array[k] == True:
                    array[k] = False
                else:
                    array[k] = True

nullArr = make2019()
goThrough2019(nullArr)
kol = 0
for i in range(0,2019):
    if nullArr[i] != False:
        print(i)
        kol += 1
print(kol)

