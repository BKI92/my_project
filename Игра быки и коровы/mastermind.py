# -*- coding: utf-8 -*-

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9

from mastermind_engine import get_number, check_number
from termcolor import cprint, colored
cprint('Загадано четырехзначное число, попробуй отгадать!', color='green')
counter = 0


while True:
    print('Ход', counter + 1)
    user_number = input(colored('Какое число загадано?', color='cyan'))
    if user_number.isdigit() and int(user_number) in range(1000, 10000):
        checking_number = check_number(user_number)
        print('Быки -', checking_number['bulls'],
              'Коровы -', checking_number['cows'])
        if checking_number['bulls'] == 4:
            print('Вы победили! Чило ходов -', counter + 1)
            user_choose = input(colored('Хотите еще? Y/N ', color='blue'))
            if user_choose == 'Y' or user_choose == 'y':
                get_number()
                counter = 0
                continue
            else:
                break
        counter += 1
    else:
        cprint('Некорректный ввод!', color='red')
