from random import randint
from copy import copy


def get_number():
    global list_numerals
    list_numerals = []
    number = randint(1000, 10000)
    for numeral in str(number):
        list_numerals.append(numeral)
    return list_numerals


list_numerals = get_number()


def check_number(user_number):
    bulls = 0
    cows = 0
    user_list_numerals = []
    for user_numeral in str(user_number):
        user_list_numerals.append(user_numeral)
    list_numerals_1 = copy(list_numerals)
    for i in range(4):
        if list_numerals_1[i] == user_list_numerals[i]:
            bulls += 1
            list_numerals_1.pop(i)
            list_numerals_1.insert(i, 'bull')
            user_list_numerals.pop(i)
            user_list_numerals.insert(i, 'u_bull')
    for item, value in enumerate(list_numerals_1):
        if value in user_list_numerals:
            list_numerals_1.remove(value)
            list_numerals_1.insert(item, 'cow')
            user_list_numerals.remove(value)
            user_list_numerals.insert(item, 'u_cow')
            cows += 1
    return {'bulls': bulls, 'cows': cows}


