def invert_arr_brute_var(A:list):
    B = [0]*A.__len__()
    for k in range(A.__len__()):
        B[k] = A[A.__len__()-k-1]
    return B


def invert_arr_One_arr(A:list):
    for k in range(A.__len__() // 2):
        A[k], A[A.__len__() - k-1] = A[A.__len__() - k -1], A[k]
    return A


def test_invert_arr():
    A1 = [1,2,3]

    A1 = invert_arr_brute_var(A1)
    if A1 == [3,2,1]:
        print('#test 1 - ok')
    else:
        print('#err test 1')


print(invert_arr_brute_var([1,2,3]))
