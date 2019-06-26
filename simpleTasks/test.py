import collections
from datetime import datetime


# def get_seconds():
#     """Returns current seconds"""
#     return datetime.now().second
#
#
# help(get_seconds)
# print(get_seconds())
# print(get_seconds.__doc__)
# print(get_seconds.__name__)
#
# counter = collections.Counter([1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3])
# for elem, count in counter.items():
#     print("{}: {} times".format(elem, count))
# print()
# for elem, count in counter.most_common(3):
#     print("{}: {} times".format(elem, count))
#
#
# def_dict = collections.defaultdict(list)
# def_dict[1]


def split_tags(tag_string: str) -> list:
    return [item.strip() for item in tag_string.split(',')]


print(split_tags('funcs, classes , someshit  '))


def median(not_sorted_list: list) -> int:
    sorted_list = not_sorted_list[:]
    sorted_list.sort()
    if len(sorted_list) % 2 == 1:
        return sorted_list[len(sorted_list) // 2]
    else:
        return (sorted_list[len(sorted_list) // 2] + sorted_list[len(sorted_list) // 2 - 1]) / 2


not_sorted = [5, 4, 2, 1]
print(median(not_sorted))
print(not_sorted)


def nlogn_median(l: list) -> int:
    if not len(l):
        return None
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) / 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2


print(nlogn_median(not_sorted))