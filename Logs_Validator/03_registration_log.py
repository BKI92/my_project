# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


class LogsValidator:

    def __init__(self):
        self.line = None
        self.name = None
        self.email = None
        self.age = None

    def validation(self, line):
        self.line = line
        self.name, self.email, self.age = self.line.split(' ')
        if (self.name_validation() and self.email_validation() and
                self.age_validation()):
            return True

    def name_validation(self):
        if self.name.isalpha():
            return True
        else:
            raise NotNameError('Поле имени содержит не только буквы')

    def email_validation(self):
        if '.' and '@' in self.email:
            return True
        else:
            raise NotEmailError('Поле email не содержит @ или .')

    def age_validation(self):
        if 10 <= int(self.age) <= 99:
            return True
        else:
            raise ValueError('Поле возраст не является числом от 10 до 99')


lv = LogsValidator()
with open(file='registrations.txt', mode='r') as file, \
        open(file='registrations_good.log', mode='a') as good_log:
    for line in file:
        try:
            if lv.validation(line):
                # Для корректной работы программы, лучше будет 1 раз открыть
                # файл в начале цикла
                good_log.write(f'{line}')
        except (NotNameError, NotEmailError, ValueError) as exc:
            with open(file='registrations_bad.log', mode='a') as ff:
                ff.write(f'{exc} in line: {line}')

# Зачет!


