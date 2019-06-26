def season(m):
    if type(m) == int:
        if 1 <= m <= 12:
            season_dict = dict()
            season_dict[1] = 'Зима'
            season_dict[2] = 'Зима'
            season_dict[3] = 'Весна'
            season_dict[4] = 'Весна'
            season_dict[5] = 'Весна'
            season_dict[6] = 'Лето'
            season_dict[7] = 'Лето'
            season_dict[8] = 'Лето'
            season_dict[9] = 'Осень'
            season_dict[10] = 'Осень'
            season_dict[11] = 'Осень'
            season_dict[12] = 'Зима'
            return season_dict.get(m)
        else:
            return "M value error"  # should be in [1,12]
    else:
        raise TypeError  # m should be int


# TEST1
if season(3) == 'Весна':
    print("TEST1 OK")
else:
    print("TEST1 ERROR")

# TEST2
if season(13) == 'M value error':
    print("TEST2 OK")
else:
    print("TEST2 ERROR")

# TEST3
try:
    season('123')
except TypeError:
    print('TEST3 OK - TypeError raised')


