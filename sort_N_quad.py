
def insert_sort(A):
    """insert sort function"""
    n = len(A)
    for top in range(1, n):   # range(1,n) = [1,n) math equivalent
        k = top
        while k > 0 and A[k-1] > A[k]: # A[-1] wont calculate because of k > 0 when k > 0 python wont calculate A[k-1]
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1


def choice_sort(A):
    """choice sort function"""
    n = len(A)
    for pos in range(0, n-1): # n-1 cause last elem`ll be on right pos because others are on their positions already
        for k in range(pos+1, n):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


def bubble_sort(A):
    """bubble sort function"""
    n = len(A)
    for bypass in range(1,n):
        for k in range(0, n-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]


def test_sort(sort__function):
    """ testing function of sort functions"""
    print('#testing: ', sort__function.__doc__)

    print('testcase #1: ', end='')
    A = [4,2,5,1,3]
    A_sorted = [1,2,3,4,5]
    sort__function(A)
    print('Ok' if A == A_sorted else 'Failed')

    print('testcase #2: ', end='')
    A = list(range(10, 20)) + list(range(0,10))
    A_sorted = list(range(20))
    sort__function(A)
    print('Ok' if A == A_sorted else 'Failed')

    print('testcase #3: ', end='')
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort__function(A)
    print('Ok' if A == A_sorted else 'Failed')
    print('#End testing: ', sort__function.__doc__)
    print()


test_sort(insert_sort)
test_sort(choice_sort)
test_sort(bubble_sort)
