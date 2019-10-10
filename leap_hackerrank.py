def is_leap(year):
    leap = True

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
    else:
        leap = False
    return leap


for year in range(1800, 10000):
    if is_leap(year):
        print(year)
