# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Дата: 04-05 ДЕКАБРЯ 2023
'''''
'''
Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
Дисциплина: Основы программирования на Python
'''
'''
Урок №12 от 04.12.2023
Домашнее задание №11: Работа с датой и временем
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполните следующие задания:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Задание №1.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Реализуйте программу, чтобы получить номер недели.
'''
'''
Date: 2015, 6, 16
Output: 25
'''
'''
Решение:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Вариант №1. ↓ 
'''
from datetime import datetime
def get_week_number(year, month, day):
    date_obj = datetime(year, month, day)
    week_number = date_obj.isocalendar()[1]
    return week_number
# Пример использования
week_number = get_week_number(2015, 6, 16)
print(f"Номер недели: {week_number}")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Шаг №1. - Импорт модуля
''''
from datetime import datetime
'''
В этом шаге происходит импорт класса datetime из модуля datetime.
Этот класс предоставляет возможности для работы с датой и временем.
'''
''''
Шаг №2. - Определение функции
''''
def get_week_number(year, month, day):
    date_obj = datetime(year, month, day)
    week_number = date_obj.isocalendar()[1]
    return week_number
'''
Эта функция называется get_week_number и принимает три аргумента: year (год), month (месяц) и day (день).
Внутри функции создается объект datetime с переданными аргументами. Затем вызывается метод isocalendar(),
возвращающий кортеж (год, номер недели, день недели), и из этого кортежа извлекается номер недели,
который затем возвращается из функции.
'''
''''
Шаг №3. - Пример использования функции
''''
# Пример использования
week_number = get_week_number(2015, 6, 16)
'''
В этом шаге функция get_week_number используется с конкретными значениями аргументов (год 2015, месяц 6, день 16),
и результат (номер недели) сохраняется в переменной week_number.
'''
''''
Шаг №4. - Вывод результата на экран
''''
print(f"Номер недели: {week_number}")
'''
Затем результат (номер недели) выводится на экран с использованием функции print.
'''
'''
Дополнительное пояснение:

Функция get_week_number принимает год, месяц и день в качестве аргументов,
создает объект datetime, извлекает номер недели, и возвращает его.
В примере использования функции эта неделя для даты 16 июня 2015 года сохраняется в переменной и выводится на экран.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Вариант №2. ↓ 
'''
from datetime import datetime

def get_week_number(year, month, day):
    try:
        date_obj = datetime(year, month, day)
        week_number = date_obj.isocalendar()[1]
        return week_number
    except ValueError:
        print("Некорректная дата. Пожалуйста, введите корректные значения.")

def get_user_input():
    while True:
        try:
            year = int(input("Введите год: "))
            if 1 <= year <= 9999:
                break
            else:
                print("Некорректный год. Год должен быть в диапазоне от 1 до 9999.")
        except ValueError:
            print("Пожалуйста, введите корректное значение для года.")

    while True:
        try:
            month = int(input("Введите месяц (число от 1 до 12): "))
            if 1 <= month <= 12:
                break
            else:
                print("Некорректный месяц. Месяц должен быть в диапазоне от 1 до 12.")
        except ValueError:
            print("Пожалуйста, введите корректное значение для месяца.")

    while True:
        try:
            day = int(input("Введите день (число от 1 до 31): "))
            if 1 <= day <= 31:
                break
            else:
                print("Некорректный день. День должен быть в диапазоне от 1 до 31.")
        except ValueError:
            print("Пожалуйста, введите корректное значение для дня.")

    return year, month, day

# Пример использования
user_input = get_user_input()
week_number = get_week_number(*user_input)
if week_number is not None:
    print(f"Номер недели: {week_number}")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Шаг №1. - Определение функции get_week_number
''''
'''
Пример строчки кода:
'''
def get_week_number(year, month, day):
    try:
        date_obj = datetime(year, month, day)
        week_number = date_obj.isocalendar()[1]
        return week_number
    except ValueError:
        print("Некорректная дата. Пожалуйста, введите корректные значения.")
'''
Подробное описание функции get_week_number:
'''
'''
Функция get_week_number принимает три аргумента: year (год), month (месяц) и day (день).
Внутри функции создается объект datetime с использованием переданных аргументов.
Затем вызывается метод isocalendar(), который возвращает кортеж (год, номер недели, день недели).
Извлекается второй элемент кортежа (номер недели) и возвращается как результат функции.
Если при создании объекта datetime возникает исключение ValueError (например, если введена некорректная дата),
выводится сообщение об ошибке.
'''
''''
Шаг №2. - Определение функции get_user_input
''''
'''
Пример строчки кода:
'''
def get_user_input():
    while True:
        try:
            year = int(input("Введите год: "))
            if 1 <= year <= 9999:
                break
            else:
                print("Некорректный год. Год должен быть в диапазоне от 1 до 9999.")
        except ValueError:
            print("Пожалуйста, введите корректное значение для года.")
'''
Подробное описание функции get_user_input:
'''
'''
Функция get_user_input используется для получения от пользователя ввода года, месяца и дня.
В цикле while True выполняется ввод года, который должен быть целым числом. 
Если ввод не является целым числом или не попадает в диапазон от 1 до 9999, программа выводит соответствующее 
сообщение об ошибке и повторяет запрос. По аналогии с годом, вводится месяц и день с аналогичными проверками.
Функция возвращает кортеж из трех значений: года, месяца и дня.
'''
''''
Шаг №3. - Пример использования функций и вывод результата
''''
'''
Пример строчки кода:
'''
# Пример использования
user_input = get_user_input()
week_number = get_week_number(*user_input)
if week_number is not None:
    print(f"Номер недели: {week_number}")
'''
Подробное описание:
'''
'''
Запрашивается ввод пользователя с помощью функции get_user_input, и результат сохраняется в переменной user_input.
Вызывается функция get_week_number с передачей распакованного кортежа user_input в качестве аргументов.
Если результат не является None (т.е., введенная дата корректна), выводится номер недели. В противном случае 
выводится сообщение об ошибке, которое было бы выведено внутри функции get_week_number, если введена некорректная дата.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Задание №2.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Реализуйте программу, чтобы найти дату первого понедельника данной недели.
'''
'''
Date: 2015, 50
Output: пн 14 декабря 00:00:00 2015
'''
'''
Решение:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Вариант №1. ↓ - Думаю то что нужно!
'''
from datetime import datetime, timedelta
def find_first_monday(year, week):
    # Используем формат ISO для получения первого дня недели
    first_day_of_week = datetime.strptime(f'{year}-W{week}-1', '%G-W%V-%u')
    # Рассчитываем разницу в днях до понедельника
    days_until_monday = (first_day_of_week.weekday() - 0 + 7) % 7
    # Получаем дату первого понедельника
    first_monday = first_day_of_week - timedelta(days=days_until_monday)
    return first_monday
# Пример использования
year = 2015
week = 50
result = find_first_monday(year, week)
# Выводим результат в требуемом формате
print(result.strftime('%a %d %B %H:%M:%S %Y'))
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Проблема связана с тем, что модуль datetime в Python может иметь проблемы с корректным определением начала недели
в случае, если первый день года приходится на позапрошлый год.

И!

Используя формат %G-W%V-%u вместо %Y-W%W-%w, мы более точно учитываем начало недели в соответствии с ISO.
'''
''''
Шаг №1. - Импорт библиотек:
''''
from datetime import datetime, timedelta
''''
В этой строке мы импортируем два класса из модуля datetime: datetime для работы с датами и временем
и timedelta для работы с разницей между датами.
''''
''''
Шаг №2. - Определение функции find_first_monday:
''''
def find_first_monday(year, week):
''''
Эта функция принимает два аргумента: year (год) и week (неделя), и возвращает объект datetime, представляющий первый 
понедельник указанной недели.
''''
''''
Шаг №3. - Создание объекта first_day_of_week:
''''
first_day_of_week = datetime.strptime(f'{year}-W{week}-1', '%G-W%V-%u')
''''
Мы используем метод strptime (строка-во-время) для создания объекта datetime из строки в формате ISO,
представляющей первый день указанной недели. Формат %G-W%V-%u обеспечивает правильное представление года,
недели и дня недели.
''''
''''
Шаг №4. - Расчет разницы до понедельника:
''''
days_until_monday = (first_day_of_week.weekday() - 0 + 7) % 7
''''
Мы рассчитываем разницу в днях между днем недели первого дня и понедельником, учитывая, что понедельник имеет индекс 0.
''''
''''
Шаг №5. - Создание объекта first_monday:
''''
first_monday = first_day_of_week - timedelta(days=days_until_monday)
''''
Используя объект timedelta, мы вычитаем разницу в днях из первого дня недели,
получая тем самым объект datetime для первого понедельника.
''''
''''
Шаг №6. - Возврат результата:
''''
return first_monday
''''
Функция возвращает объект datetime, представляющий первый понедельник указанной недели.
''''
''''
Шаг №7. - Пример использования функции:
''''
year = 2015
week = 50
result = find_first_monday(year, week)
print(result.strftime('%a %d %B %H:%M:%S %Y'))
''''
Мы передаем значения year и week в функцию, получаем объект datetime для первого понедельника,
и затем выводим его в заданном формате.
''''
'''
Дополнительное пояснение:

Этот код учитывает високосные года и использует правильный формат для определения начала недели в соответствии с ISO.
Пожалуйста, используйте его, и он должен корректно работать для нахождения первого понедельника указанной недели.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓
БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓
БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓
'''
from datetime import datetime, timedelta
def find_first_monday(year, week):
    # Используем формат ISO для получения первого дня недели
    first_day_of_week = datetime.strptime(f'{year}-W{week}-1', '%G-W%V-%u')
    # Рассчитываем разницу в днях до понедельника
    days_until_monday = (first_day_of_week.weekday() - 0 + 7) % 7
    # Получаем дату первого понедельника
    first_monday = first_day_of_week - timedelta(days=days_until_monday)
    return first_monday
# Пользовательский ввод для года и номера недели
year_input = input("Введите год: ")
week_input = input("Введите номер недели: ")
# Преобразуем введенные тексты в целые числа
year_number = int(year_input)
week_number = int(week_input)
# Получаем дату первого понедельника
result = find_first_monday(year_number, week_number)
# Выводим результат в требуемом формате
print(result.strftime('%a %d %B %H:%M:%S %Y'))
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Шаг №1. - Импорт необходимых модулей
''''
from datetime import datetime, timedelta
'''
На этом шаге импортируются два класса из модуля datetime: datetime для работы с датами и временем, 
и timedelta для работы с разницей во времени.
'''
''''
Шаг №2. - Определение функции find_first_monday
''''
def find_first_monday(year, week):
    # Используем формат ISO для получения первого дня недели
    first_day_of_week = datetime.strptime(f'{year}-W{week}-1', '%G-W%V-%u')
    # Рассчитываем разницу в днях до понедельника
    days_until_monday = (first_day_of_week.weekday() - 0 + 7) % 7
    # Получаем дату первого понедельника
    first_monday = first_day_of_week - timedelta(days=days_until_monday)
    return first_monday
'''
1. Функция find_first_monday принимает два аргумента: year (год) и week (номер недели).

2. В строке first_day_of_week = datetime.strptime(f'{year}-W{week}-1', '%G-W%V-%u') используется формат ISO для 
получения даты первого дня недели. Эта строка создает объект datetime на основе года и номера недели.

3. Рассчитывается разница в днях до понедельника с 
использованием days_until_monday = (first_day_of_week.weekday() - 0 + 7) % 7. Это выражение позволяет определить,
сколько дней нужно отнять от первого дня недели, чтобы получить понедельник.

4. Дата первого понедельника вычисляется как first_monday = first_day_of_week - timedelta(days=days_until_monday).

5. Функция возвращает объект datetime представляющий первый понедельник указанной недели.
'''
''''
Шаг №3. - Ввод данных и вызов функции
''''
# Пользовательский ввод для года и номера недели
year_input = input("Введите год: ")
week_input = input("Введите номер недели: ")
# Преобразуем введенные тексты в целые числа
year_number = int(year_input)
week_number = int(week_input)
# Получаем дату первого понедельника
result = find_first_monday(year_number, week_number)
'''
1. Пользователь вводит год и номер недели с клавиатуры.
2. Введенные значения преобразуются в целые числа.
'''
''''
Шаг №4. - Вывод результата
''''
# Выводим результат в требуемом формате
print(result.strftime('%a %d %B %H:%M:%S %Y'))
'''
1. Вызывается метод strftime объекта result, который форматирует дату в строку в соответствии с указанным 
форматом %a %d %B %H:%M:%S %Y.
2. Результат выводится на экран. Например, "Tue 20 December 00:00:00 2022" - это форматированная строка,
представляющая день недели, число, месяц, час, минуту, секунду и год соответственно.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Задание №3.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Реализуйте программу, чтобы выбрать все воскресенья определенного года.
'''
'''
Решение:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Вариант №1. ↓ - Думаю то что нужно!
'''
from datetime import datetime, timedelta
def find_sundays(year):
    sundays = []
    # Устанавливаем начальную дату первого дня года
    current_date = datetime(year, 1, 1)
    # Проходим через все дни года
    while current_date.year == year:
        # Если текущий день - воскресенье, добавляем его в список
        if current_date.weekday() == 6:  # 6 представляет воскресенье
            sundays.append(current_date)
        # Переходим к следующему дню
        current_date += timedelta(days=1)
    return sundays
# Пример использования
year_to_find = 2015
sundays_of_year = find_sundays(year_to_find)
# Выводим результат в требуемом формате
for sunday in sundays_of_year:
    print(sunday.strftime('%a %d %B %H:%M:%S %Y'))
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Шаг №1. - Импорт библиотек:
''''
from datetime import datetime, timedelta
''''
Здесь мы импортируем два класса из модуля datetime: datetime для работы с датами и временем
и timedelta для работы с разницей между датами.
''''
''''
Шаг №2. - Определение функции find_sundays:
''''
def find_sundays(year):
''''
Эта функция принимает год в качестве аргумента и возвращает список объектов datetime,
представляющих все воскресенья в указанном году.
''''
''''
Шаг №3. - Создание пустого списка sundays:
''''
sundays = []
''''
Здесь мы создаем пустой список, в который будем добавлять все воскресенья.
''''
''''
Шаг №4. - Установка начальной даты:
''''
current_date = datetime(year, 1, 1)
''''
Устанавливаем начальную дату 1 января указанного года.
''''
''''
Шаг №5. - Проход по всем дням года:
''''
while current_date.year == year:
''''
Этот цикл выполняется, пока текущая дата принадлежит указанному году.
''''
''''
Шаг №6. - Проверка, является ли текущий день воскресеньем:
''''
if current_date.weekday() == 6:
''''
Метод weekday() возвращает номер дня недели, где 0 - понедельник, 1 - вторник, ..., 6 - воскресенье. 
Если текущий день - воскресенье, добавляем его в список sundays.
''''
''''
Шаг №7. - Добавление воскресенья в список и переход к следующему дню:
''''
sundays.append(current_date)
current_date += timedelta(days=1)
''''
Мы добавляем текущее воскресенье в список и переходим к следующему дню.
''''
''''
Шаг №8. - Возврат списка воскресений:
''''
return sundays
''''
Функция возвращает список всех воскресений в указанном году.
''''
''''
Шаг №9. - Пример использования функции:
''''
year_to_find = 2015
sundays_of_year = find_sundays(year_to_find)

for sunday in sundays_of_year:
    print(sunday.strftime('%a %d %B %H:%M:%S %Y'))
''''
Мы вызываем функцию find_sundays для года 2015, получаем список воскресений,
и затем выводим каждое воскресенье в заданном формате с использованием метода strftime.
''''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓
БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓
БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓
'''
from datetime import datetime, timedelta
def find_sundays(year):
    sundays = []
    # Устанавливаем начальную дату первого дня года
    current_date = datetime(year, 1, 1)
    # Проходим через все дни года
    while current_date.year == year:
        # Если текущий день - воскресенье, добавляем его в список
        if current_date.weekday() == 6:  # 6 представляет воскресенье
            sundays.append(current_date)
        # Переходим к следующему дню
        current_date += timedelta(days=1)
    return sundays
# Пользовательский ввод для года
year_to_find = int(input("Введите год: "))
# Получаем список воскресений
sundays_of_year = find_sundays(year_to_find)
# Выводим результат в требуемом формате
for sunday in sundays_of_year:
    print(sunday.strftime('%a %d %B %H:%M:%S %Y'))
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1. - Использование функции:
'''
'''
Пример кода:
'''
from datetime import datetime, timedelta
def find_sundays(year):
    sundays = []
    current_date = datetime(year, 1, 1)
    while current_date.year == year:
        if current_date.weekday() == 6:
            sundays.append(current_date)
        current_date += timedelta(days=1)
    return sundays
year_to_find = int(input("Введите год: "))
sundays_of_year = find_sundays(year_to_find)
for sunday in sundays_of_year:
    print(sunday.strftime('%a %d %B %H:%M:%S %Y'))
'''
Подробное описание:
'''
'''
На этом этапе мы используем функцию find_sundays, чтобы найти и получить список воскресений в заданном году.
Функция принимает год в качестве аргумента и возвращает список объектов даты, представляющих воскресенья в этом году.
'''
'''
Шаг №2. - Определение функции find_sundays:
'''
'''
Пример кода:
'''
from datetime import datetime, timedelta
def find_sundays(year):
    sundays = []
    current_date = datetime(year, 1, 1)
    while current_date.year == year:
        if current_date.weekday() == 6:
            sundays.append(current_date)
        current_date += timedelta(days=1)
    return sundays
'''
Подробное описание:
'''
'''
В этом шаге мы определяем функцию find_sundays, которая принимает год в качестве аргумента и возвращает список дат
воскресений для этого года. Внутри функции мы создаем пустой список sundays для хранения дат воскресений и 
устанавливаем начальную дату на 1 января заданного года. Затем мы используем цикл while, чтобы пройти через все дни
года. Если текущий день является воскресеньем (его номер в неделе равен 6), то мы добавляем текущую дату в список.
Затем мы увеличиваем текущую дату на один день с помощью timedelta.
Функция возвращает окончательный список воскресений.
'''
'''
Шаг №3. - Получение пользовательского ввода и вывод результата:
'''
'''
Пример кода:
'''
year_to_find = int(input("Введите год: "))
sundays_of_year = find_sundays(year_to_find)

for sunday in sundays_of_year:
    print(sunday.strftime('%a %d %B %H:%M:%S %Y'))
'''
Подробное описание:
'''
'''
Здесь пользователь вводит год, который затем используется для вызова функции find_sundays. 
Результат (список воскресений) сохраняется в переменной sundays_of_year. Затем используется цикл for, 
чтобы пройти по каждой дате в списке и вывести ее в заданном формате с использованием метода strftime.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓ БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓ БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓
БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓ БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓ БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓
БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓ БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓ БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓
БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓ БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓ БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓
БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓ БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓ БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓
'''
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
def find_sundays(year):
    sundays = []
    current_date = datetime(year, 1, 1)
    while current_date.year == year:
        if current_date.weekday() == 6:
            sundays.append(current_date)
        current_date += timedelta(days=1)
    return sundays
# Пользовательский ввод для года
year_to_find = int(input("Введите год: "))
sundays_of_year = find_sundays(year_to_find)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
days_of_month = [sunday.day for sunday in sundays_of_year]
month_counts = [days_of_month.count(day) for day in set(days_of_month)]
days_of_month_list = list(set(days_of_month))
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
axs[0, 0].bar(days_of_month_list, month_counts, color='blue')
axs[0, 0].set_title('Столбчатая диаграмма')
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
axs[0, 1].plot(days_of_month_list, month_counts, marker='o', color='green')
axs[0, 1].set_title('Линейный график')
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
axs[1, 0].scatter(days_of_month_list, month_counts, color='red')
axs[1, 0].set_title('Точечная диаграмма')
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
axs[1, 1].pie(month_counts, labels=days_of_month_list, autopct='%1.1f%%', colors=['purple', 'orange', 'pink'])
axs[1, 1].set_title('Круговая диаграмма')
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
plt.tight_layout()
plt.show()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1. - Импорт необходимых библиотек:
'''
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
'''
Подробное описание:
'''
'''
В этом шаге мы импортируем библиотеку для создания графиков matplotlib.pyplot и два 
класса из модуля datetime: datetime для работы с датами и временем и timedelta для работы с разницей во времени.
'''
'''
Шаг №2. - Определение функции find_sundays:
'''
def find_sundays(year):
    sundays = []
    current_date = datetime(year, 1, 1)
    while current_date.year == year:
        if current_date.weekday() == 6:
            sundays.append(current_date)
        current_date += timedelta(days=1)
    return sundays
'''
Подробное описание:
'''
'''
В этом шаге мы определяем функцию find_sundays, которая принимает год в качестве аргумента и возвращает 
список объектов даты, представляющих воскресенья в этом году. Функция использует цикл while, чтобы проходить 
через дни года, и добавляет в список sundays объекты даты, представляющие воскресенья.
'''
'''
Шаг №3. - Получение года от пользователя:
'''
year_to_find = int(input("Введите год: "))
'''
Подробное описание:
'''
'''
На этом этапе программа запрашивает у пользователя ввод года с клавиатуры с помощью функции input.
Полученная строка затем преобразуется в целое число с помощью int().
'''
'''
Шаг №4. - Поиск воскресений и подготовка данных:
'''
sundays_of_year = find_sundays(year_to_find)
days_of_month = [sunday.day for sunday in sundays_of_year]
month_counts = [days_of_month.count(day) for day in set(days_of_month)]
days_of_month_list = list(set(days_of_month))
'''
Подробное описание:
'''
'''
Здесь программа использует функцию find_sundays, чтобы получить список воскресений для указанного года. Затем
создаются списки days_of_month и month_counts. Первый содержит дни месяца для каждого воскресенья, а второй содержит 
количество воскресений для каждого дня месяца. Список days_of_month_list содержит уникальные дни месяца.
'''
'''
Шаг №5. - Создание графиков с использованием Matplotlib:
'''
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
axs[0, 0].bar(days_of_month_list, month_counts, color='blue')
axs[0, 0].set_title('Столбчатая диаграмма')
axs[0, 1].plot(days_of_month_list, month_counts, marker='o', color='green')
axs[0, 1].set_title('Линейный график')
axs[1, 0].scatter(days_of_month_list, month_counts, color='red')
axs[1, 0].set_title('Точечная диаграмма')
axs[1, 1].pie(month_counts, labels=days_of_month_list, autopct='%1.1f%%', colors=['purple', 'orange', 'pink'])
axs[1, 1].set_title('Круговая диаграмма')
plt.tight_layout()
plt.show()
'''
Подробное описание:
'''
'''
Здесь мы используем библиотеку Matplotlib для создания графиков. 
Создается 2x2 сетка подграфиков с помощью subplots. Далее создаются четыре разных типа графиков (столбчатая диаграмма,
линейный график, точечная диаграмма и круговая диаграмма), каждый из которых размещается на соответствующем подграфике.
Наконец, с помощью plt.tight_layout() и plt.show() графики выводятся на экран.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Задание №4.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Реализуйте программу на Python, чтобы добавить год (ы) с заданной датой и отобразить новую дату.
'''
'''
Example: (addYears - это имя пользовательской функции)

print (addYears (datetime.date (2015,1,1), -1))
print (addYears (datetime.date (2015,1,1), 0))
print (addYears (datetime.date (2015,1,1), 2))
print (addYears (datetime.date (2000,2,29), 1))
'''
'''
Output:
2014-01-01
2015-01-01
2017-01-01
2001-03-01
'''
'''
Решение:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Вариант №1. ↓ - Думаю то что нужно!

Проблема заключается в том, что вы пытаетесь увеличить дату на 1 год, 
начиная с 29 февраля в невисокосном году (например, 2001 год), что приводит к недопустимой дате
(29 февраля следующего года, который тоже невисокосный).

Нам же нужно более аккуратно обрабатывать такие случаи.
Можно использовать библиотеку dateutil.relativedelta, 
которая обеспечивает более гибкое и безопасное добавление лет к дате.
'''
from datetime import datetime
from dateutil.relativedelta import relativedelta
def add_years(original_date, num_years):
    try:
        # Используем relativedelta для корректного добавления лет к дате
        new_date = original_date + relativedelta(years=num_years)
        return new_date
    except ValueError:
        # Если происходит ошибка из-за недопустимой даты, просто возвращаем None
        return None
# Пример использования
date1 = datetime(2015, 1, 1)
date2 = datetime(2015, 1, 1)
date3 = datetime(2015, 1, 1)
date4 = datetime(2000, 2, 29)
# Вызываем функцию add_years с разными аргументами
result1 = add_years(date1, -1)
result2 = add_years(date2, 0)
result3 = add_years(date3, 2)
result4 = add_years(date4, 1)
# Выводим результаты
print(f"Задание №4 - {result1}")
print(f"Задание №4 - {result2}")
print(f"Задание №4 - {result3}")
print(f"Задание №4 - {result4}")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Шаг №1. - Импорт библиотек:
''''
from datetime import datetime
from dateutil.relativedelta import relativedelta
'''
Мы импортируем datetime для работы с датами и relativedelta из библиотеки dateutil,
чтобы обеспечить корректное добавление лет к дате.
'''
''''
Шаг №2. - Определение функции:
''''
def add_years(original_date, num_years):
    try:
        new_date = original_date + relativedelta(years=num_years)
        return new_date
    except ValueError:
        return None
'''
Функция add_years принимает два аргумента: original_date (исходная дата) и num_years 
(количество лет, которое нужно добавить). Внутри функции используется relativedelta для корректного выполнения операции.
'''
''''
Шаг №3. - Пример использования:
''''
date1 = datetime(2015, 1, 1)
date2 = datetime(2015, 1, 1)
date3 = datetime(2015, 1, 1)
date4 = datetime(2000, 2, 29)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
result1 = add_years(date1, -1)
result2 = add_years(date2, 0)
result3 = add_years(date3, 2)
result4 = add_years(date4, 1)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
print(f"Задание №4 - {result1}")
print(f"Задание №4 - {result2}")
print(f"Задание №4 - {result3}")
print(f"Задание №4 - {result4}")
'''
Создаем несколько объектов datetime для тестирования функции и вызываем add_years с разными аргументами.
Результаты выводятся на экран.
'''
''''
Шаг №4. - Пример вывода результатов:
''''
print(f"Задание №4 - {result1}")
print(f"Задание №4 - {result2}")
print(f"Задание №4 - {result3}")
print(f"Задание №4 - {result4}")
'''
Результаты выводятся на экран с использованием print.
Это могут быть либо корректные даты, либо None, если возникает ошибка из-за недопустимой даты.
'''
'''
Итог:

В задании №4 приведены примеры использования, которые предполагают, что использование replace для добавления года может
быть безопасным для большинства случаев. В этих примерах не учитываются возможные ошибки, связанные с високосными
годами и добавлением года к дате с 29 февраля.

И:

Примеры использования предоставлены в учебных целях и могут не покрывать все возможные сценарии использования.
В реальном мире, чтобы обеспечить корректную обработку високосных годов и других крайних случаев, рекомендуется 
использовать более продвинутые методы, такие как dateutil.relativedelta или библиотеку arrow. Эти инструменты 
обеспечивают более гибкое и безопасное выполнение операций с датами.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓
БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓
БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓  БОНУСНЫЙ ВАРИАНТ ↓
'''
from datetime import datetime
from dateutil.relativedelta import relativedelta
def add_years(original_date, num_years):
    try:
        new_date = original_date + relativedelta(years=num_years)
        return new_date
    except ValueError:
        return None
def get_user_input():
    try:
        year = int(input("Введите год: "))
        month = int(input("Введите месяц (число от 1 до 12): "))
        day = int(input("Введите день (число от 1 до 31): "))
        return datetime(year, month, day)
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите корректные числа.")
        return None
# Пример использования с вводом данных с клавиатуры
user_date = get_user_input()
if user_date:
    # Примеры из задания с использованием пользовательских данных
    result1 = add_years(user_date, -1)
    result2 = add_years(user_date, 0)
    result3 = add_years(user_date, 2)
    result4 = add_years(user_date, 1)
    # Вывод результатов
    print(f"1. {result1}")
    print(f"2. {result2}")
    print(f"3. {result3}")
    print(f"4. {result4}")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Шаг №1. - Импорт библиотек:
''''
from datetime import datetime
from dateutil.relativedelta import relativedelta
''''
Мы импортируем datetime для работы с датами и relativedelta для корректного добавления лет к дате.
''''
''''
Шаг №2. - Определение функции add_years:
''''
def add_years(original_date, num_years):
    try:
        new_date = original_date + relativedelta(years=num_years)
        return new_date
    except ValueError:
        return None
'''
Функция add_years принимает два аргумента: original_date (исходная дата) и num_years 
(количество лет, которое нужно добавить). Используется relativedelta для корректного выполнения операции.
'''
''''
Шаг №3. - Определение функции get_user_input:
''''
def get_user_input():
    try:
        year = int(input("Введите год: "))
        month = int(input("Введите месяц (число от 1 до 12): "))
        day = int(input("Введите день (число от 1 до 31): "))
        return datetime(year, month, day)
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите корректные числа.")
        return None
'''
Функция get_user_input запрашивает у пользователя ввод года, месяца и дня и возвращает объект datetime.
'''
''''
Шаг №4. - Пример использования с вводом данных с клавиатуры:
''''
user_date = get_user_input()
'''
Пользователь вводит данные, и если введенные данные корректны, создается объект datetime для дальнейшего использования.
'''
''''
Шаг №5. - Примеры из задания с использованием пользовательских данных:
''''
result1 = add_years(user_date, -1)
result2 = add_years(user_date, 0)
result3 = add_years(user_date, 2)
result4 = add_years(user_date, 1)
'''
Мы используем введенные пользователем данные для вызова функции add_years с различными значениями num_years.
'''
''''
Шаг №6. - Пример вывода результатов:
''''
print(f"1. {result1}")
print(f"2. {result2}")
print(f"3. {result3}")
print(f"4. {result4}")
'''
Результаты выводятся на экран с использованием print, и пользователь видит, как изменяется дата при добавлении годов
в соответствии с условиями задания.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓ БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓ БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓
БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓ БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓ БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓
БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓ БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓ БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓
БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓ БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓ БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓
БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓ БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓ БОНУСНЫЙ ВАРИАНТ ↓ БОНУСНОГО ВАРИАНТА ↓
'''
from datetime import datetime
from dateutil.relativedelta import relativedelta
def add_years(original_date, num_years):
    try:
        new_date = original_date + relativedelta(years=num_years)
        return new_date
    except ValueError:
        return None
def get_user_input():
    try:
        year = int(input("Введите год: "))
        month = int(input("Введите месяц (число от 1 до 12): "))
        day = int(input("Введите день (число от 1 до 31): "))
        return datetime(year, month, day)
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите корректные числа.")
        return None
def main():
    user_dates = []
    for _ in range(4):
        user_date = get_user_input()
        if user_date:
            user_dates.append(user_date)
    for i, date in enumerate(user_dates, 1):
        result = add_years(date, i)
        print(f"Результат для введенной даты {i}: {result}")
if __name__ == "__main__":
    main()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Шаг №1. - Импортируем необходимые библиотеки
''''
from datetime import datetime
from dateutil.relativedelta import relativedelta
'''
datetime используется для работы с датой и временем, 
а relativedelta — для корректного выполнения операций с датами, включая сложение годов.
'''
''''
Шаг №2. - Определяем функцию add_years(original_date, num_years)
''''
def add_years(original_date, num_years):
    try:
        new_date = original_date + relativedelta(years=num_years)
        return new_date
    except ValueError:
        return None
'''
Она принимает два аргумента: original_date (исходная дата) и num_years (количество лет, которое нужно добавить).
Внутри функции используется relativedelta для корректного выполнения операции сложения годов.
Если в результате операции возникает исключение ValueError (например, из-за некорректной даты), функция возвращает None.
'''
''''
Шаг №3. - Определяем функцию get_user_input()
''''
def get_user_input():
    try:
        year = int(input("Введите год: "))
        month = int(input("Введите месяц (число от 1 до 12): "))
        day = int(input("Введите день (число от 1 до 31): "))
        return datetime(year, month, day)
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите корректные числа.")
        return None
'''
Она запрашивает у пользователя ввод года, месяца и дня, преобразует введенные строки в целые числа, создает объект
datetime и возвращает его. Если во время ввода происходит ошибка (ValueError),
функция сообщает об этом и возвращает None.
'''
''''
Шаг №4. - Определяем функцию main()
''''
def main():
    user_dates = []

    for _ in range(4):
        user_date = get_user_input()
        if user_date:
            user_dates.append(user_date)

    for i, date in enumerate(user_dates, 1):
        result = add_years(date, i)
        print(f"Результат для введенной даты {i}: {result}")

if __name__ == "__main__":
    main()
'''
Внутри нее создаем пустой список user_dates. Затем в цикле for _ in range(4): запрашиваем у пользователя ввод 
четырех дат и добавляем их в список user_dates.
'''
'''
После этого используем цикл for i, date in enumerate(user_dates, 1):, чтобы пройти по списку введенных дат и вывести
результаты добавления года к каждой из них. Выводим результат в формате "Результат для введенной даты {i}: {result}".
'''
'''
И наконец, запускаем функцию main() только в том случае, если этот скрипт запущен непосредственно
(а не импортирован как модуль). 
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
from datetime import datetime
def add_years(original_date, num_years):
    try:
        new_date = original_date.replace(year=original_date.year + num_years)
        return new_date
    except ValueError as e:
        print(f"Ошибка при добавлении лет: {e}")
        return None
def get_user_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input < 1:
                print("Пожалуйста, введите положительное число.")
            else:
                return user_input
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите целое число.")
def main():
    user_dates = []
    for i in range(1, 5):
        print(f"\nВведите данные для даты {i}:")
        year = get_user_input("Год: ")
        month = get_user_input("Месяц (число от 1 до 12): ")
        day = get_user_input("День (число от 1 до 31): ")
        user_date = datetime(year, month, day)
        user_dates.append(user_date)
    for i, date in enumerate(user_dates, 1):
        result = add_years(date, i)
        if result:
            print(f"Результат для введенной даты {i}: {result}")
if __name__ == "__main__":
    main()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Шаг №1. - Импорт необходимых модулей
''''
from datetime import datetime
'''
Подробное описание:
'''
'''
На этом шаге импортируется класс datetime из модуля datetime. Этот класс используется для работы с датой и временем.
'''
''''
Шаг №2. - Определение функции add_years
''''
def add_years(original_date, num_years):
    try:
        new_date = original_date.replace(year=original_date.year + num_years)
        return new_date
    except ValueError as e:
        print(f"Ошибка при добавлении лет: {e}")
        return None
'''
Подробное описание:
'''
'''
Эта функция принимает два аргумента: original_date (исходная дата) и num_years 
(количество лет, которое нужно добавить). В блоке try используется метод replace для создания новой даты, 
увеличивая значение года на num_years. Если операция выполнена успешно, функция возвращает новую дату. 
В случае возникновения ошибки ValueError (например, если результат выходит за допустимый диапазон года), 
функция выводит сообщение об ошибке и возвращает None.
'''
''''
Шаг №3. - Определение функции get_user_input
''''
def get_user_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input < 1:
                print("Пожалуйста, введите положительное число.")
            else:
                return user_input
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите целое число.")
'''
Подробное описание:
'''
'''
Эта функция принимает строку prompt в качестве аргумента, которая используется для запроса ввода у пользователя. 
В бесконечном цикле while True происходит попытка преобразовать введенное значение в целое число. 
Если ввод успешен и число положительное, функция возвращает введенное значение. 
В противном случае выводится сообщение об ошибке, и пользователю предлагается ввести данные заново.
'''
''''
Шаг №4. - Определение функции main
''''
def main():
    user_dates = []

    for i in range(1, 5):
        print(f"\nВведите данные для даты {i}:")
        year = get_user_input("Год: ")
        month = get_user_input("Месяц (число от 1 до 12): ")
        day = get_user_input("День (число от 1 до 31): ")

        user_date = datetime(year, month, day)
        user_dates.append(user_date)

    for i, date in enumerate(user_dates, 1):
        result = add_years(date, i)
        if result:
            print(f"Результат для введенной даты {i}: {result}")
'''
Подробное описание:
'''
'''
Эта функция является основной частью программы. 
В ней создается пустой список user_dates, в который будут добавлены введенные пользователем даты. 
Затем используется цикл for, чтобы четыре раза запросить пользователя ввести год, 
месяц и день для каждой из четырех дат. Введенные данные преобразуются в объекты datetime и добавляются в список.

После ввода всех дат программа использует цикл for для перебора введенных дат и вызова функции add_years для каждой
из них. Результаты выводятся на экран в формате "Результат для введенной даты {i}: {result}".
'''
''''
Шаг №5. - Запуск программы
''''
if __name__ == "__main__":
    main()
'''
Подробное описание:
'''
'''
Этот блок кода проверяет, запущен ли скрипт напрямую, а не импортирован ли он в другой скрипт. 
Если скрипт запущен напрямую, вызывается функция main(), и программа начинает выполнение.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''                                  ПОСТАРАЛСЯ СДЕЛАТЬ ВСЕ ЗАДАНИЯ В ОДНОМ КОДЕ                                  '''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def get_week_number(year, month, day):
    try:
        date_obj = datetime(year, month, day)
        week_number = date_obj.isocalendar()[1]
        return week_number
    except ValueError:
        print("Некорректная дата. Пожалуйста, введите корректные значения.")

def find_first_monday(year, week):
    try:
        first_day_of_week = datetime.strptime(f'{year}-W{week}-1', '%G-W%V-%u')
        days_until_monday = (first_day_of_week.weekday() - 0 + 7) % 7
        first_monday = first_day_of_week - timedelta(days=days_until_monday)
        return first_monday
    except ValueError:
        print("Некорректная дата. Пожалуйста, введите корректные значения.")

def find_sundays(year):
    try:
        sundays = []
        current_date = datetime(year, 1, 1)
        while current_date.year == year:
            if current_date.weekday() == 6:
                sundays.append(current_date)
            current_date += timedelta(days=1)
        return sundays
    except ValueError:
        print("Некорректный год. Пожалуйста, введите корректный год.")

def add_years(original_date, num_years):
    try:
        new_date = original_date + relativedelta(years=num_years)
        return new_date
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите корректные числа.")
        return None

def get_user_input():
    try:
        year = int(input("Введите год: "))
        month = int(input("Введите месяц (число от 1 до 12): "))
        day = int(input("Введите день (число от 1 до 31): "))
        return datetime(year, month, day)
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите корректные числа.")
        return None

def main():
    # Задание №1 - Получение номера недели
    user_input = get_user_input()
    week_number = get_week_number(user_input.year, user_input.month, user_input.day)
    if week_number is not None:
        print(f"Задание №1 - Номер недели: {week_number}")

    # Задание №2 - Нахождение даты первого понедельника недели
    user_year = int(input("Введите год для задания №2: "))
    user_week = int(input("Введите номер недели для задания №2: "))
    first_monday = find_first_monday(user_year, user_week)
    if first_monday:
        print(f"Задание №2 - Дата первого понедельника: {first_monday.strftime('%a %d %B %H:%M:%S %Y')}")

    # Задание №3 - Выбор всех воскресений определенного года
    user_year_sundays = int(input("Введите год для задания №3: "))
    sundays_of_year = find_sundays(user_year_sundays)
    print("Задание №3 - Все воскресенья выбранного года:")
    for sunday in sundays_of_year:
        print(sunday.strftime('%a %d %B %H:%M:%S %Y'))

    # Задание №4 - Добавление года к заданной дате и отображение новой даты
    user_date = get_user_input()
    num_years_to_add = int(input("Введите количество лет для добавления (задание №4): "))
    new_date = add_years(user_date, num_years_to_add)
    if new_date:
        print(f"Задание №4 - Новая дата после добавления {num_years_to_add} лет: {new_date.strftime('%a %d %B %H:%M:%S %Y')}")

if __name__ == "__main__":
    main()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1. ↓ - Импорт необходимых модулей
'''
from datetime import datetime, timedelta
'''
На этом шаге мы импортируем два класса из модуля datetime. datetime позволяет нам работать 
с датами и временем, а timedelta — с разницей во времени.
'''
'''
Шаг №2. ↓ - Определение функции find_first_monday
'''
def find_first_monday(year, week):
    first_day_of_week = datetime.strptime(f'{year}-W{week}-1', '%G-W%V-%u')
    days_until_monday = (first_day_of_week.weekday() - 0 + 7) % 7
    first_monday = first_day_of_week - timedelta(days=days_until_monday)
    return first_monday
'''
1. - Функция find_first_monday принимает два аргумента: year (год) и week (номер недели).

2. - Мы используем datetime.strptime для создания объекта datetime для первого дня недели с заданным годом 
и номером недели (%G-W%V-%u — формат для ISO-недели).

3. - first_day_of_week.weekday() возвращает номер дня недели для первого дня недели.

4. - days_until_monday вычисляет, сколько дней нужно прибавить к первому дню недели, 
чтобы получить понедельник (используя формулу (first_day_of_week.weekday() - 0 + 7) % 7).

5. - Затем мы вычитаем этот интервал из первого дня недели, чтобы получить дату первого понедельника.

6. - Функция возвращает дату первого понедельника.
'''
'''
Шаг №3. ↓ - Получение пользовательского ввода
'''
user_year = int(input("Введите год: "))
user_week = int(input("Введите номер недели: "))
'''
Пользователю предлагается ввести год и номер недели.
'''
'''
Шаг №4 ↓ - Вызов функции и вывод результата
'''
result = find_first_monday(user_year, user_week)
print(result.strftime('%a %d %B %H:%M:%S %Y'))
'''
1. - Мы вызываем функцию find_first_monday с введенными пользователем данными.
2. - Результат (дата первого понедельника) форматируется с использованием метода strftime и выводится на экран.
'''
'''
Итог:

Этот код принимает от пользователя год и номер недели, затем использует эти данные
для определения и вывода даты первого понедельника указанной недели.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Работа с датой и временем
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполните следующие задания:
'''
'''
Задание №1 - Реализуйте программу, чтобы узнать время по Гринвичу и местное время.

Задание №2 - Реализуйте программу, для вычисления количества дней между двумя датами.

Задание №3 - Реализуйте программу, для преобразования двух разностей дат в дни, часы, минуты и секунды.

Задание №4 - Реализуйте программу на Python, для создания HTML-календаря с данными за определенный год и месяц.
'''
'''
Решение:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Задание №1 - Реализуйте программу, чтобы узнать время по Гринвичу и местное время.
'''
from datetime import datetime, timedelta
import pytz
# Задание №1
def get_gmt_local_time():
    # Получаем текущее время по Гринвичу
    gmt_time = datetime.utcnow()
    # Получаем местное время
    local_timezone = pytz.timezone('Europe/Moscow')  # Пример: Московское время
    local_time = gmt_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)
    return gmt_time, local_time
# Вызываем функцию
gmt_time, local_time = get_gmt_local_time()
# Выводим результат
print(f"Время по Гринвичу: {gmt_time}")
print(f"Местное время: {local_time}")
'''
Этот код использует библиотеку pytz для работы с часовыми поясами. 
Он выводит текущее время по Гринвичу и местное время (в данном случае, Московское время).
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1 ↓ - Импорт необходимых модулей
'''
from datetime import datetime, timedelta
import pytz
'''
Описание: 

В этом шаге происходит импорт двух модулей - datetime для работы с датой 
и временем, и pytz для работы с часовыми поясами.
'''
'''
Шаг №2 ↓ - Определение функции get_gmt_local_time()
'''
def get_gmt_local_time():
    # Получаем текущее время по Гринвичу
    gmt_time = datetime.utcnow()

    # Получаем местное время
    local_timezone = pytz.timezone('Europe/Moscow')  # Пример: Московское время
    local_time = gmt_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)

    return gmt_time, local_time
'''
Описание: 

Функция get_gmt_local_time() возвращает два объекта времени - текущее время по Гринвичу (gmt_time)
и местное время (local_time). Сначала она получает текущее время по Гринвичу с помощью datetime.utcnow(),
затем определяет местное время для конкретного часового пояса (в данном случае, для Европы/Москвы).
'''
'''
Шаг №3 ↓ - Вызов функции и присвоение результатов переменным
'''
gmt_time, local_time = get_gmt_local_time()
'''
Описание: 

Здесь функция get_gmt_local_time() вызывается, и ее результаты (текущее время по Гринвичу и местное время)
присваиваются переменным gmt_time и local_time соответственно.
'''
'''
Шаг №4 ↓ - Вывод результатов
'''
print(f"Время по Гринвичу: {gmt_time}")
print(f"Местное время: {local_time}")
'''
Описание: 

В последнем шаге выводятся результаты в консоль с использованием функции print().
Отображается текущее время по Гринвичу и местное время.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Задание №2: Вычисление количества дней между двумя датами.
'''
from datetime import datetime
# Задание №2
def days_between_dates(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    # Вычисляем разницу в днях
    days_difference = (date2 - date1).days
    return days_difference
# Вызываем функцию
date_str1 = input("Введите первую дату (ГГГГ-ММ-ДД): ")
date_str2 = input("Введите вторую дату (ГГГГ-ММ-ДД): ")
result_days = days_between_dates(date_str1, date_str2)
# Выводим результат
print(f"Количество дней между датами: {result_days} дней")
'''
Этот код принимает от пользователя две даты и выводит количество дней между ними.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1 ↓ - Импорт необходимого модуля
'''
from datetime import datetime
'''
Описание: 

В этом шаге происходит импорт модуля datetime для работы с датой и временем.
'''
'''
Шаг №2 ↓ - Определение функции days_between_dates(date_str1, date_str2)
'''
def days_between_dates(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    # Вычисляем разницу в днях
    days_difference = (date2 - date1).days
    return days_difference
'''
Описание: 

Функция days_between_dates() принимает две строки, представляющие даты в формате "ГГГГ-ММ-ДД" (например, "2023-12-07").
Затем она использует метод strptime() модуля datetime для преобразования этих строк в объекты datetime. 
После этого вычисляется разница в днях между двумя датами с помощью (date2 - date1).days, и результат возвращается.
'''
'''
Шаг №3 ↓ - Ввод данных и вызов функции
'''
date_str1 = input("Введите первую дату (ГГГГ-ММ-ДД): ")
date_str2 = input("Введите вторую дату (ГГГГ-ММ-ДД): ")
result_days = days_between_dates(date_str1, date_str2)
'''
Описание: 

Пользователю предлагается ввести две даты, после чего эти даты передаются в функцию days_between_dates(), 
и результат (разница в днях) сохраняется в переменной result_days.
'''
'''
Шаг №4 ↓ - Вывод результата
'''
print(f"Количество дней между датами: {result_days} дней")
'''
Описание: 

Наконец, выводится результат в консоль с использованием функции print(). 
Отображается количество дней между введенными датами.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Задание №3: Преобразование разностей дат в дни, часы, минуты и секунды.
'''
from datetime import timedelta
# Задание №3
def convert_timedeltas(delta1, delta2):
    # Преобразуем разности дат в секунды
    seconds1 = delta1.total_seconds()
    seconds2 = delta2.total_seconds()
    # Вычисляем дни, часы, минуты и секунды
    days = int(abs(seconds2 - seconds1) // 86400)
    hours, remainder = divmod(abs(seconds2 - seconds1), 3600)
    minutes, seconds = divmod(remainder, 60)
    return days, int(hours), int(minutes), int(seconds)
# Вызываем функцию
delta1 = timedelta(days=5, hours=8, minutes=30)
delta2 = timedelta(days=10, hours=15, minutes=45)
result_days, result_hours, result_minutes, result_seconds = convert_timedeltas(delta1, delta2)
# Выводим результат
print(f"Разница во времени: {result_days} дней, {result_hours} часов, {result_minutes} минут, {result_seconds} секунд")
'''
Этот код принимает два объекта timedelta и вычисляет разницу между ними в днях, часах, минутах и секундах.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1 ↓ - Импорт необходимого модуля
'''
from datetime import timedelta
'''
Описание: 

В этом шаге происходит импорт класса timedelta из модуля datetime. timedelta представляет разницу 
между двумя моментами времени.
'''
'''
Шаг №2 ↓ - Определение функции convert_timedeltas(delta1, delta2)
'''
def convert_timedeltas(delta1, delta2):
    # Преобразуем разности дат в секунды
    seconds1 = delta1.total_seconds()
    seconds2 = delta2.total_seconds()
    # Вычисляем дни, часы, минуты и секунды
    days = int(abs(seconds2 - seconds1) // 86400)
    hours, remainder = divmod(abs(seconds2 - seconds1), 3600)
    minutes, seconds = divmod(remainder, 60)
    return days, int(hours), int(minutes), int(seconds)
'''
Описание: 

Функция convert_timedeltas() принимает два объекта timedelta (delta1 и delta2). 
Затем она преобразует разности дат в секунды с помощью метода total_seconds(). 
Далее, используя операции деления и остатка от деления (divmod), вычисляются дни, часы, минуты и секунды между двумя 
промежутками времени.
'''
'''
Шаг №3 ↓ - Вызов функции и присвоение результатов переменным
'''
delta1 = timedelta(days=5, hours=8, minutes=30)
delta2 = timedelta(days=10, hours=15, minutes=45)
result_days, result_hours, result_minutes, result_seconds = convert_timedeltas(delta1, delta2)
'''
Описание: 

Создаются два объекта timedelta (delta1 и delta2), представляющие разные временные интервалы. 
Затем функция convert_timedeltas() вызывается с этими интервалами, и результаты (дни, часы, минуты, секунды) 
присваиваются соответствующим переменным.
'''
'''
Шаг №4 ↓ - Вывод результата
'''
print(f"Разница во времени: {result_days} дней, {result_hours} часов, {result_minutes} минут, {result_seconds} секунд")
'''
Описание: 

Наконец, результаты выводятся в консоль с использованием функции print(). 
Отображается разница во времени между двумя заданными интервалами в виде дней, часов, минут и секунд.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Задание №4: Создание HTML-календаря.
'''
import calendar
# Задание №4
def create_html_calendar(year, month):
    cal = calendar.HTMLCalendar()
    html_calendar = cal.formatmonth(year, month)
    return html_calendar
# Вызываем функцию
user_year = int(input("Введите год для создания HTML-календаря: "))
user_month = int(input("Введите месяц для создания HTML-календаря: "))
result_calendar = create_html_calendar(user_year, user_month)
# Выводим результат
print(result_calendar)
'''
Этот код принимает от пользователя год и месяц, затем создает HTML-календарь для указанного месяца и года.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1 ↓ - Импорт необходимого модуля
'''
import calendar
'''
Описание: 

В этом шаге происходит импорт модуля calendar, который предоставляет функциональность для работы с календарями.
'''
'''
Шаг №2 ↓ - Определение функции create_html_calendar(year, month)
'''
def create_html_calendar(year, month):
    cal = calendar.HTMLCalendar()
    html_calendar = cal.formatmonth(year, month)
    return html_calendar
'''
Описание: 

Функция create_html_calendar() принимает год (year) и месяц (month), затем создает объект HTMLCalendar из 
модуля calendar. Далее, с использованием метода formatmonth(), форматирует календарь для указанного месяца и года в 
виде HTML строки и возвращает ее.
'''
'''
Шаг №3 ↓ - Ввод данных и вызов функции
'''
user_year = int(input("Введите год для создания HTML-календаря: "))
user_month = int(input("Введите месяц для создания HTML-календаря: "))
result_calendar = create_html_calendar(user_year, user_month)
'''
Описание: 

Пользователю предлагается ввести год и месяц для создания HTML-календаря. Затем функция create_html_calendar() 
вызывается с введенными данными, и результат (HTML-строка календаря) сохраняется в переменной result_calendar.
'''
'''
Шаг №4 ↓ - Вывод результата
'''
print(result_calendar)
'''
Описание: 

Наконец, HTML-строка календаря выводится в консоль с использованием функции print().
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''                                  ПОСТАРАЛСЯ СДЕЛАТЬ ВСЕ ЗАДАНИЯ В ОДНОМ КОДЕ                                  '''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
from datetime import datetime, timedelta
import calendar
import pytz
from dateutil.relativedelta import relativedelta
from PyQt5.QtWidgets import QApplication, QCalendarWidget, QVBoxLayout, QWidget
import sys


def get_gmt_local_time():
    gmt_time = datetime.utcnow()
    local_timezone = pytz.timezone('Europe/Moscow')  # Пример: Московское время
    local_time = gmt_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)
    return gmt_time, local_time


def days_between_dates(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    days_difference = (date2 - date1).days
    return days_difference


def convert_timedeltas(delta1, delta2):
    seconds1 = delta1.total_seconds()
    seconds2 = delta2.total_seconds()
    days = int(abs(seconds2 - seconds1) // 86400)
    hours, remainder = divmod(abs(seconds2 - seconds1), 3600)
    minutes, seconds = divmod(remainder, 60)
    return days, int(hours), int(minutes), int(seconds)


def create_text_calendar(year, month):
    cal = calendar.TextCalendar()
    text_calendar = cal.formatmonth(year, month)
    return text_calendar


def get_user_input_date():
    try:
        date_str = input("Введите дату (ГГГГ-ММ-ДД): ")
        date_format = "%Y-%m-%d"
        user_date = datetime.strptime(date_str, date_format)
        return user_date
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите корректную дату.")
        return None


class CalendarApp(QWidget):
    def __init__(self, year, month):
        super().__init__()

        layout = QVBoxLayout(self)

        calendar = QCalendarWidget(self)
        calendar.setSelectedDate(calendar.selectedDate().addMonths(month - 1).addYears(year - 1))

        layout.addWidget(calendar)

        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("Графический календарь (PyQt5)")


def main():
    while True:
        print("\nВыберите действие:")
        print("1. Узнать время по Гринвичу и местное время.")
        print("2. Вычислить количество дней между двумя датами.")
        print("3. Преобразовать разности дат в дни, часы, минуты и секунды.")
        print("4. Создать HTML-календарь.")
        print("5. Выйти из программы.")

        choice = input("Введите номер действия (1-5): ")

        if choice == "1":
            gmt_time, local_time = get_gmt_local_time()
            print(f"Время по Гринвичу: {gmt_time}")
            print(f"Местное время: {local_time}")

        elif choice == "2":
            date_str1 = input("Введите первую дату (ГГГГ-ММ-ДД): ")
            date_str2 = input("Введите вторую дату (ГГГГ-ММ-ДД): ")
            result_days = days_between_dates(date_str1, date_str2)
            print(f"Количество дней между датами: {result_days} дней")

        elif choice == "3":
            date1 = get_user_input_date()
            date2 = get_user_input_date()
            if date1 and date2:
                delta = date2 - date1
                days = delta.days
                hours, remainder = divmod(delta.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                print(f"Разница во времени: {days} дней, {hours} часов, {minutes} минут, {seconds} секунд")

        elif choice == "4":
            while True:
                user_year = int(input("Введите год для создания HTML-календаря: "))
                user_month = int(input("Введите месяц для создания HTML-календаря: "))

                # Используйте функцию create_text_calendar вместо create_html_calendar
                result_calendar = create_text_calendar(user_year, user_month)
                print(result_calendar)

                # Интеграция с графическим календарем
                app = QApplication(sys.argv)
                window = CalendarApp(user_year, user_month)
                window.show()
                sys.exit(app.exec_())

                continue_program = input("Хотите создать еще HTML-календарь? (y/n): ").lower()
                if continue_program != 'y':
                    break

        elif choice == "5":
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Пожалуйста, введите число от 1 до 5.")


if __name__ == "__main__":
    main()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1 ↓ - Определение функции get_gmt_local_time
'''
def get_gmt_local_time():
    gmt_time = datetime.utcnow()
    local_timezone = pytz.timezone('Europe/Moscow')  # Пример: Московское время
    local_time = gmt_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)
    return gmt_time, local_time
'''
Описание:


Эта функция создает объекты gmt_time и local_time, представляющие текущее время в UTC
и локальном времени соответственно.

datetime.utcnow() создает объект datetime с текущим временем в UTC.

pytz.timezone('Europe/Moscow') создает объект часового пояса для Москвы.

gmt_time.replace(tzinfo=pytz.utc) устанавливает часовой пояс объекта gmt_time в UTC.

astimezone(local_timezone) преобразует gmt_time в локальное время, используя часовой пояс Москвы.

Возвращает кортеж из gmt_time и local_time.
'''
'''
Шаг №2 ↓ - Определение функции days_between_dates
'''
def days_between_dates(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    days_difference = (date2 - date1).days
    return days_difference
'''
Описание:


Эта функция вычисляет разницу в днях между двумя датами.

datetime.strptime(date_str1, date_format) преобразует строку date_str1 в объект datetime с учетом формата даты.

Аналогично для date_str2.

(date2 - date1).days возвращает разницу в днях между двумя датами.

Возвращает количество дней между датами.
'''
'''
Шаг №3 ↓ - Определение функции convert_timedeltas
'''
def convert_timedeltas(delta1, delta2):
    seconds1 = delta1.total_seconds()
    seconds2 = delta2.total_seconds()
    days = int(abs(seconds2 - seconds1) // 86400)
    hours, remainder = divmod(abs(seconds2 - seconds1), 3600)
    minutes, seconds = divmod(remainder, 60)
    return days, int(hours), int(minutes), int(seconds)
'''
Описание:


Эта функция конвертирует разницу между двумя объектами timedelta в дни, часы, минуты и секунды.

delta.total_seconds() возвращает общее количество секунд в объекте timedelta.

abs(seconds2 - seconds1) // 86400 вычисляет количество дней.

divmod(abs(seconds2 - seconds1), 3600) вычисляет количество часов и остаток в секундах.

Аналогично для минут и секунд.

Возвращает кортеж из дней, часов, минут и секунд.
'''
'''
Шаг №4 ↓ - Определение функции create_text_calendar
'''
def create_text_calendar(year, month):
    cal = calendar.TextCalendar()
    text_calendar = cal.formatmonth(year, month)
    return text_calendar
'''
Описание:


Эта функция создает текстовое представление календаря на заданный месяц и год.

calendar.TextCalendar().formatmonth(year, month) возвращает текстовый календарь для указанного месяца и года.

Возвращает строку с текстовым календарем.
'''
'''
Шаг №5 ↓ - Определение функции get_user_input_date
'''
def get_user_input_date():
    try:
        date_str = input("Введите дату (ГГГГ-ММ-ДД): ")
        date_format = "%Y-%m-%d"
        user_date = datetime.strptime(date_str, date_format)
        return user_date
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите корректную дату.")
        return None
'''
Описание:


Эта функция запрашивает у пользователя ввод даты и возвращает объект datetime.

В случае ошибки ввода выводит сообщение и возвращает None.
'''
'''
Шаг №6 ↓ - Определение класса CalendarApp
'''
class CalendarApp(QWidget):
    def __init__(self, year, month):
        super().__init__()

        layout = QVBoxLayout(self)

        calendar = QCalendarWidget(self)
        calendar.setSelectedDate(calendar.selectedDate().addMonths(month - 1).addYears(year - 1))

        layout.addWidget(calendar)

        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("Графический календарь (PyQt5)")
'''
Описание:


Этот класс представляет графическое приложение для отображения календаря.

Использует библиотеку PyQt5.

QCalendarWidget - виджет для отображения календаря.

setGeometry устанавливает геометрию окна (размер и положение).

setWindowTitle устанавливает заголовок окна.
'''
'''
Шаг №7 ↓ -  Основная функция main
'''


def main():
    while True:
        print("\nВыберите действие:")
        print("1. Узнать время по Гринвичу и местное время.")
        print("2. Вычислить количество дней между двумя датами.")
        print("3. Преобразовать разности дат в дни, часы, минуты и секунды.")
        print("4. Создать HTML-календарь.")
        print("5. Выйти из программы.")

        choice = input("Введите номер действия (1-5): ")

        if choice == "1":
            gmt_time, local_time = get_gmt_local_time()
            print(f"Время по Гринвичу: {gmt_time}")
            print(f"Местное время: {local_time}")

        elif choice == "2":
            date_str1 = input("Введите первую дату (ГГГГ-ММ-ДД): ")
            date_str2 = input("Введите вторую дату (ГГГГ-ММ-ДД): ")
            result_days = days_between_dates(date_str1, date_str2)
            print(f"Количество дней между датами: {result_days} дней")

        elif choice == "3":
            date1 = get_user_input_date()
            date2 = get_user_input_date()
            if date1 and date2:
                delta = date2 - date1
                days = delta.days
                hours, remainder = divmod(delta.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                print(f"Разница во времени: {days} дней, {hours} часов, {minutes} минут, {seconds} секунд")

        elif choice == "4":
            while True:
                user_year = int(input("Введите год для создания HTML-календаря: "))
                user_month = int(input("Введите месяц для создания HTML-календаря: "))

                # Используйте функцию create_text_calendar вместо create_html_calendar
                result_calendar = create_text_calendar(user_year, user_month)
                print(result_calendar)

                # Интеграция с графическим календарем
                app = QApplication(sys.argv)
                window = CalendarApp(user_year, user_month)
                window.show()
                sys.exit(app.exec_())

                continue_program = input("Хотите создать еще HTML-календарь? (y/n): ").lower()
                if continue_program != 'y':
                    break

        elif choice == "5":
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Пожалуйста, введите число от 1 до 5.")


if __name__ == "__main__":
    main()
'''
Описание:


Эта функция представляет собой основной цикл программы.

Выводит меню с выбором действий.

В зависимости от выбора пользователя выполняет соответствующие действия, вызывая соответствующие функции
или создавая графический календарь.

Выход из программы осуществляется при выборе действия "5".
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
import calendar

def create_html_calendar(year, month):
    cal = calendar.HTMLCalendar()
    html_calendar = cal.formatmonth(year, month)
    return html_calendar

# Пример использования
user_year = 2023
user_month = 12
result_calendar = create_html_calendar(user_year, user_month)
print(result_calendar)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextBrowser
import sys

class CalendarApp(QWidget):
    def __init__(self, year, month):
        super().__init__()

        layout = QVBoxLayout(self)

        text_browser = QTextBrowser(self)
        html_calendar = create_html_calendar(year, month)
        text_browser.setHtml(html_calendar)

        layout.addWidget(text_browser)

        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("HTML-календарь (PyQt5)")

if __name__ == '__main__':
    user_year = 2023
    user_month = 12

    app = QApplication(sys.argv)
    window = CalendarApp(user_year, user_month)
    window.show()
    sys.exit(app.exec_())
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
