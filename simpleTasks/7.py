def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


def date(day, month, year):
    dict_month = dict()
    dict_month[1] = 31
    if is_year_leap(year):
        dict_month[2] = 29
    else:
        dict_month[2] = 28
    dict_month[3] = 31
    dict_month[4] = 30
    dict_month[5] = 31
    dict_month[6] = 30
    dict_month[7] = 31
    dict_month[8] = 31
    dict_month[9] = 30
    dict_month[10] = 31
    dict_month[11] = 30
    dict_month[12] = 31

    if day < 0 or month < 0 or year < 0:
        return False
    elif day > 31 or month > 12 or year > 2050:
        return False
    elif day > dict_month.get(month):
        return False
    return True


# дней 29 28 30 31
# месяцев 12
# лет 0 - 2050


# TEST1
print(date(29, 2, 2000))
