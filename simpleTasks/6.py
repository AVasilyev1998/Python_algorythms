import math
from time import clock_gettime


def is_prime(num):
    if 0 < num < 2:
        return True
    elif num == 2:
        return True
    i = 2
    limit = int(math.sqrt(num))

    while i <= limit:
        if num % i == 0:
            return False
        i += 1
    return True

# TEST1 - massive test
# for i in range(100):
#     print(i, ' - res: - ', is_prime(i))


for i in range(1,29):
    print(i,' is - ', is_prime(i))
