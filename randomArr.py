import random


def genArr(num,begin,end):
    lst = []
    for i in range(num):
        lst.append(random.randint(begin,end))
    return lst