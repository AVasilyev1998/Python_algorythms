def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


# TEST1
if not is_year_leap(200):
    print("TEST1 OK")
else:
    print("TEST1 ERROR")

# TEST2
if is_year_leap(816):
    print("TEST2 OK")
else:
    print("TEST2 ERROR")


# TEST3
if is_year_leap(1600):
    print("TEST3 OK")
else:
    print("TEST3 ERROR")