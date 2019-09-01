def is_leap(year):
    leap = False

    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = False

    return leap


for year in range(1800, 10000):
    print(f'||year-{year:^4}|%4-{year%4:^2}|%100-{year%100:^2}|%400-{year%6:^2}|{is_leap(year)}||')
    print('-' * 54)