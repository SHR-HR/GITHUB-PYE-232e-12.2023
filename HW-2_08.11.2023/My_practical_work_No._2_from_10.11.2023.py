# Дата ПЯТНИЦА 10 ноября 2023 год.
# Урок №3.

# Практическая работа - №2.

# Задание №1.

# Дано:

# Напишите программу, где я ввожу целое число n, и, если оно больше 20, поделите его на 6, иначе
# умножьте на 6.

# Выведите полученное число.

# Решение:

# Ввод целого числа от пользователя
n = int(input("Введите целое число: "))

# Проверка условия
if n > 20:
    result = n / 6
else:
    result = n * 6

# Вывод результата
print("Результат:", result)


# Задание №2.

# Дано:

# Напишите программу, где я ввожу целое число n, и если оно является положительным,
# то прибавьте к нему 1; если отрицательным, то вычесть из него 2; если нулевым,
# то заменить его на 10.

# Выведите полученное число.

# Решение:

# Ввод целого числа от пользователя
n = int(input("Введите целое число: "))

# Проверка условий
if n > 0:
    result = n + 1
elif n < 0:
    result = n - 2
else:
    result = 10

# Вывод результата
print("Результат:", result)


#  Задание №3.

# Дано:

# Напишите программу, где я ввожу целые числа a и b, если их значения не равны, то присвоить
# каждой переменной сумму этих значении, а если равны, то присвоить переменным нулевые значения.

# Вывести новые значения переменных.

# Решение:

# Ввод двух целых чисел от пользователя
a = int(input("Введите первое целое число (a): "))
b = int(input("Введите второе целое число (b): "))

# Проверка условия
if a != b:
    # Если значения не равны, присваиваем каждой переменной сумму этих значений
    a = a + b
    b = a  # Мы можем использовать a, так как уже присвоили ей сумму

else:
    # Если значения равны, присваиваем переменным нулевые значения
    a = 0
    b = 0

# Вывод новых значений переменных
print("Новое значение a:", a)
print("Новое значение b:", b)


# Задание №4.

# Дано:

# Напишите программу, где ввожу число n, и если оно является положительным, то прибавьте к нему 1;
# в противном случае не изменять его.

# Выведите полученное число.

# Решение:

# Ввод целого числа от пользователя
n = int(input("Введите целое число: "))

# Проверка условия
if n > 0:
    n = n + 1

# Вывод результата
print("Результат:", n)


# Задание №5.

# Дано:

# Напишите программу, где ввожу число n, и если оно является положительным, то прибавьте к нему 1;
# в противном случае не изменять его.

# Выведите полученное число.

# Решение:

# Ввод двух целых чисел от пользователя
a = int(input("Введите целое число a: "))
b = int(input("Введите целое число b: "))

# Проверка деления a на b
if a % b == 0:
    print("divisible")
else:
    print("not divisible")
