from randomArr import genArr

def bin_search(data, searched):
    counter = 0
    low = 0
    high = data.__len__()
    while low <= high:
        counter += 1
        mid = round((low+high)/2)
        guess = data[mid]
        if guess == searched:
            return mid
        if guess > searched:
            high = mid - 1
        else:
            low = mid + 1
    print('counter',counter)
    return mid


arr = genArr(20,-10,1000)
print(arr)
bin_search(arr, arr[19])


"""
    test 1
"""
a = list(range(100));
n = 20;
if a[bin_search(a,n)] == n:
    print('test 1  - OK')
else:
    print(bin_search(a, n))
    print('test 1 - ERROR')

"""
    test 2
"""
a = list(range(100));
n = 0;
if a[bin_search(a,n)] == n:
    print('test 2  - OK')
else:
    print(bin_search(a, n))
    print('test 2 - ERROR')

"""
    test 3
"""
a = list(range(-50,51));
n = 50;
if a[bin_search(a,n)] == n:
    print('test 3  - OK')
else:
    print(bin_search(a, n))
    print('test 3 - ERROR')

"""
    test 4
"""
a = list(range(-50,50));
n = -50;
if a[bin_search(a, n)] == n:
    print('test 4  - OK')
else:
    print(bin_search(a, n))
    print('test 4 - ERROR')


