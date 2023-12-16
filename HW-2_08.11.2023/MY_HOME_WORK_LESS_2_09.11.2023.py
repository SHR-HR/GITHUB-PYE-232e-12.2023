# Дата: 09.11.2023
# Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
# Дисциплина: Основы программирования на Python

# Домашняя работа №2.

# - Задание №1.

# Дано:

# Напишите программу Резюме. На вход подается Имя, Фамилия, Отчество,
# Возраст и на выходы в консоль выдаем следующий текст: Здравствуйте!
# Меня зовут Имя Фамилия Отчество. Мне Возраст и я хочу у Вас работать.

# Решение:

# ВВОД НЕОБХОДИМЫХ ДАННЫХ

name = input("Введите имя: ")  # РОМАН
surname = input("Введите фамилию: ")  # ШАУНИН
patronymic = input("Введите отчество: ")  # ВЛАДИМИРОВИЧ
age = int(input("Введите возраст: "))  # 18

# ПРЕОБРАЗОВАНИЕ РЕЗЮМЕ
resume = f"Здравствуйте! Меня зовут {name} {surname} {patronymic}. Мне {age} и я хочу у Вас работать."

# ИТОГОВЫЙ РЕЗУЛЬТАТ

print(resume)


# Задание №2.

# Дано:

# Напишите программу, в которую на вход подается два числа a и b.
# На выходе получаем строку: Целая часть от деления N и остаток M

# Решение (Вариант №1):

L = 7
X = 5
N = L // X  # N = 1
M = L % X  # M = 2
print(N, M)

# Решение (Вариант №2 - учитывая последнюю полученную информацию на уроке №3 - 10.11.2023):

# Ввод данных
a = int(input("Введите первое число (a): "))
b = int(input("Введите второе число (b): "))

# Проверка деления на ноль
if b == 0:
    print("Делитель не может быть равен нулю")
else:
    # Вычисление целой части и остатка от деления
    whole_part = a // b
    remainder = a % b

    # Вывод результата
    result_string = f"Целая часть от деления {whole_part} и остаток {remainder}"
    print(result_string)

               # Введите первое число (a): 15
               # Введите второе число (b): 6
               # Целая часть от деления 2 и остаток 3


# Задание №3.

# Дано:

# Напишите программу, которая сравнивает две строки.
# На вход подается str1 и str2. И на выходе мы получаем True или False.

# Решение (Вариант №1):

o = "Hello!"
print(o.isdigit())  # строка состоит только из цифр?
# False
print(o.isalpha())  # строка состоит только из букв?
# False
print(o.isalnum())  # строка состоит только из цифр и букв?
# False

# Решение (Вариант №2):

print(2 * 2 == 4)
#True
print(1.57*3/1.5 == 3.14)
# True
print(3 ** 3 - 3 * (6 * 3 - 4.5 * 2) == 1)
#False

# Решение (Вариант №3 - учитывая последнюю полученную информацию на уроке №3 - 10.11.2023):

# Ввод данных
str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")

# Сравнение строк и вывод результата
if str1 == str2:
    print(True)
else:
    print(False)

# Решение (Вариант №4):

str1 = input("Введите 1 слово: ")
str2 = input("Введите 2 слово: ")
print(str1 == str2)


# Задание №4.

# Дано:

# Напишите программу, в которой есть константа MULTIPLE_VAL=6.4
# и на вход подается число M. На выходе получаем число M*MULTIPLE_VAL и
# все значения сконвертированные в integer, string.

# Решение (Вариант №1):

MULTIPLE_VAL = 6.4

def process_input(M):
    result_float = M * MULTIPLE_VAL
    result_int = int(result_float)
    result_str = str(result_float)

    return result_float, result_int, result_str

# Получаем ввод от пользователя
try:
    M = float(input("Введите число M: "))
except ValueError:
    print("Ошибка ввода. Пожалуйста, введите корректное число.")
    exit()

# Обработка ввода
result_float, result_int, result_str = process_input(M)

# Вывод результата
print("Output:")
print(result_float)
print(result_int)
print(result_str)

# Решение (Вариант №2): К примеру MULTIPLE_VAL не 6.4 а 55.07 - но, можно оставить и 6.4

MULTIPLE_VAL = 55.07

def process_input(M):
    result = M * MULTIPLE_VAL
    result_int = int(result)
    result_str = str(result)
    return result, result_int, result_str

# Ввод числа M
M = float(input("Введите число M: "))

# Обработка введенного числа
result, result_int, result_str = process_input(M)

# Вывод результатов
print("Результат в виде числа с плавающей точкой:", result)
print("Результат в виде целого числа:", result_int)
print("Результат в виде строки:", result_str)


# Данат, это совсем не решение. Это даже не совсем, то, что нужно, но, посмотрите, так можно делать?


INT_CONSTANT = 35 * 30
print(INT_CONSTANT)  #string
INT_CONSTANT = 1050
print(INT_CONSTANT)  #string
INT_CONSTANT = 1050 / 2.01
print(INT_CONSTANT)  #float
INT_CONSTANT = 522.3880597014926 * 2.01
print(INT_CONSTANT)  #float

number1 = "1050"
number2 = "522.3880597014926"
number3 = "1050.0"

print(number1.isdigit())  # строка состоит только из цифр?
# True

print(number2.isalpha())  # строка состоит только из букв?
# False

print(number3.isafloat())  # строка состоит только из цифр?
# True




