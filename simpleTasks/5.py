def bank(a, years):
    summary = a
    for i in range(years):
        summary *= 1.1
    return summary


# TEST1
v = 300000
if bank(v, 5) == (v * 1.1 * 1.1 * 1.1 * 1.1 * 1.1):
    print("TEST1 OK")
else:
    print("TEST1 ERROR")



