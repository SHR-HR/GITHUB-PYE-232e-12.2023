# Дата ПЯТНИЦА 10 ноября 2023 год.
# Урок №3.

# Практическая работа - №1.


# Задание №1.

# Дано:

# Напишите программу, в которой я ввожу два целостных
# числа, и если первое число больше второго, то программа выведет true,
# иначе false.

# Решение:

# Ввод двух целых чисел
num1 = int(input("Введите первое целое число: "))
num2 = int(input("Введите второе целое число: "))

# Проверка условия и вывод результата
if num1 > num2:
    print(True)
else:
    print(False)


# Задание №2.

# Дано:

# Напишите программу, в которой я ввожу три целостных чисел a, b и c,
# и если сумма a и b больше c, то программа выведет true,
# # иначе false.

# Решение:

# Ввод трех целых чисел
a = int(input("Введите первое целое число (a): "))
b = int(input("Введите второе целое число (b): "))
c = int(input("Введите третье целое число (c): "))

# Проверка условия и вывод результата
if a + b > c:
    print(True)
else:
    print(False)


# Задание №3.

# Дано:

# Напишите программу, в которой я ввожу число a. Если число, а является четным,
# то программа выведет true, иначе false.

# Решение:

# Ввод целого числа
a = int(input("Введите целое число: "))

# Проверка условия и вывод результата
if a % 2 == 0:
    print(True)
else:
    print(False)


# Задание №4.

# Дано:

# Определите, является ли введенное пользователем число четным.
# 0 является четным числом.

# Решение:

# Ввод целого числа
number = int(input("Введите целое число: "))

# Проверка условия и вывод результата
if number % 2 == 0:
    print("четное")
else:
    print("нечетное")


# Задание №5.

# Дано:

# Напишите программу, которая по введенному номеру дня недели (понедельник – первый день недели – 1,
# вторник – второй день недели – 2) определяет выходной это или будний день.


# Решение:

# Ввод номера дня недели
day_number = int(input("Введите номер дня недели (1 - понедельник, 2 - вторник, и так далее): "))

# Проверка условия и вывод результата
if day_number >= 1 and day_number <= 5:
    print("будний")
elif day_number >= 6 and day_number <= 7:
    print("выходной")
else:
    print("Некорректный номер дня недели. Введите число от 1 до 7.")

