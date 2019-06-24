from time import monotonic as mono


def analysis(lst):
    count_dict2 = {}
    for i in lst:
        if i in count_dict2:
            count_dict2[i] += 1
        else:
            count_dict2[i] = 1
    return count_dict2


def count(lst):
    countd = {}
    for i in lst:
        countd[i] = countd.get(i, 0) + 1
    return countd




now = mono()
res = count([4, 4, 7, 9])
end = mono()
print('my code ', end - now)

now_new = mono()
new_res = analysis([1, 1, 2, 3])
end_new = mono()
print('other code ', end_new - now_new)



my_tuple_lst = [(1,2), (2,3)]
my_dict = {key: value+1 for key,value in my_tuple_lst}
print(my_dict)