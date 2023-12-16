# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Дата: 20-21 ноября 2023

# Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
# Дисциплина: Основы программирования на Python

# Домашнее задание №6.- Функции. Модули, библиотеки и пакеты

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Задание №1.

# Дано: ↓

# Напишите программу для создания списка, длина которого равна N.
# После создания списка нужно подсчитать нечетные и четные числа.
# Если нечетных чисел больше, чем четных, вывод должен быть «Нет», в остальных ключах «Да».

# Input                                                                     Output
# 5                                                                         19 31
# 4 16 19 31 2                                                              4 16 2
#                                                                           YES
# Решение:

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Вариант №1.

def count_odd_even(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    even_numbers = [num for num in numbers if num % 2 == 0]

    if len(odd_numbers) > len(even_numbers):
        return odd_numbers, even_numbers, "NO"
    else:
        return odd_numbers, even_numbers, "YES"

def main():
    # Вводим длину списка
    N = int(input())

    # Вводим элементы списка
    numbers = list(map(int, input().split()))

    # Проверяем, что длина списка равна N
    if len(numbers) == N:
        odd_numbers, even_numbers, result = count_odd_even(numbers)

        # Выводим нечетные числа
        print(" ".join(map(str, odd_numbers)))

        # Выводим четные числа
        print(" ".join(map(str, even_numbers)))

        # Выводим результат (YES или NO)
        print(result)
    else:
        print("Ошибка: длина списка не равна N.")

if __name__ == "__main__":
    main()

# Теперь попробую расписать пошагово, что к чему

# Шаг №1 - Функция count_odd_even:

def count_odd_even(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    even_numbers = [num for num in numbers if num % 2 == 0]

    if len(odd_numbers) > len(even_numbers):
        return odd_numbers, even_numbers, "NO"
    else:
        return odd_numbers, even_numbers, "YES"

# count_odd_even принимает список чисел и создает два новых списка:
# odd_numbers (нечетные числа) и even_numbers (четные числа).
# Затем функция сравнивает длины odd_numbers и even_numbers.
# Если длина odd_numbers больше, то возвращается кортеж из трех элементов: odd_numbers, even_numbers, и строка "NO".
# В противном случае возвращается "YES".

# Шаг №2 - Функция main:


def main():

    # Вводим длину списка

    N = int(input())

    # Вводим элементы списка

    numbers = list(map(int, input().split()))

    # Проверяем, что длина списка равна N

    if len(numbers) == N:
        odd_numbers, even_numbers, result = count_odd_even(numbers)

        # Выводим нечетные числа

        print(" ".join(map(str, odd_numbers)))

        # Выводим четные числа

        print(" ".join(map(str, even_numbers)))

        # Выводим результат (YES или NO)

        print(result)
    else:
        print("Ошибка: длина списка не равна N.")

if __name__ == "__main__":
    main()

# main начинается с ввода длины списка N.
# Затем вводятся числа для создания списка numbers.
# Проверяется, что длина списка равна N.
# Если условие выполняется, вызывается функция count_odd_even для подсчета нечетных и четных чисел, и выводятся
# результаты в соответствии с вашим требованием.
# Если длина списка не равна N, выводится сообщение об ошибке.



# Шаг №3 - Оператор if __name__ == "__main__"::

# Этот оператор проверяет, запущен ли скрипт напрямую (а не импортирован в другой скрипт).
# Если скрипт запущен напрямую, вызывается функция main.

# Таким образом, программа вводит данные, создает список, подсчитывает нечетные и четные числа,
# и выводит результат согласно заданным условиям.

# Далее подробнее об операторе - if __name__ == ")__main__"

# Оператор if __name__ == "__main__": используется в Python для определения, запущен ли скрипт напрямую, или же он был
# импортирован в другой скрипт. Это позволяет изолировать код, который должен выполняться только при запуске скрипта
# напрямую, а не при его импорте.

# Пример:

# Предположим, у вас есть два файла: main_script.py и module.py. Вот их содержимое:

# module.py:

def print_hello():
    print("Hello from module!")

# Этот код выполнится только при импорте, не при запуске напрямую

if __name__ == "__main__":
    print("Module is being run directly")
else:
    print("Module is being imported")

# main_script.py

import module

# Вызываем функцию из импортированного модуля

module.print_hello()

# Этот код выполнится только при запуске напрямую, не при импорте

if __name__ == "__main__":
    print("Main script is being run directly")
else:
    print("Main script is being imported")

# Теперь, если вы запустите module.py напрямую, вы увидите:

# Module is being run directly

# Если же вы запустите main_script.py, вы увидите:
# Module is being imported
# Hello from module!
# Main script is being run directly

# Получается, блок кода под if __name__ == "__main__": в module.py выполняется только при запуске module.py напрямую,
# но не при его импорте из другого скрипта. Это удобно, например, когда в модуле есть какие-то демонстрационные или
# тестовые части, которые нужно выполнять только при его запуске напрямую.


# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Вариант №2. - чуть-чуть по другому

def count_odd_even_numbers(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    even_numbers = [num for num in numbers if num % 2 == 0]

    if len(odd_numbers) > len(even_numbers):
        return odd_numbers, even_numbers, "NO"
    else:
        return odd_numbers, even_numbers, "YES"

def main():
    # Ввод длины списка
    n = int(input())

    # Ввод элементов списка
    numbers = list(map(int, input().split()))

    # Подсчет нечетных и четных чисел и определение ответа
    odd_numbers, even_numbers, result = count_odd_even_numbers(numbers)

    # Вывод результатов
    print(" ".join(map(str, odd_numbers)))
    print(" ".join(map(str, even_numbers)))
    print(result)

if __name__ == "__main__":
    main()

# Шаг №1. - Определение функции count_odd_even_numbers:

# Эта функция принимает список чисел в качестве аргумента.
# Создаются два списка: odd_numbers для нечетных чисел и even_numbers для четных чисел.
# Затем функция сравнивает длины двух списков и возвращает три значения: odd_numbers, even_numbers и
# строку "NO" или "YES", в зависимости от результата сравнения.

# Шаг №1. - Определение функции main:

# Эта функция выполняет основную логику программы.
# Сначала считывается длина списка n с помощью input().
# Затем считываются элементы списка через input() и split().
# Вызывается функция count_odd_even_numbers для подсчета нечетных и четных чисел и получения результата.
# Выводятся результаты на экран.

# Шаг №1. - Запуск программы:

# Пользователь вводит длину списка n.
# Пользователь вводит элементы списка через пробел.
# Программа выводит нечетные числа, четные числа и результат сравнения на экран.

# Шаг №1. - Пример работы программы:

# Допустим, пользователь вводит 5 в качестве длины списка и 4 16 19 31 2 в качестве элементов.
# Программа вычисляет и выводит нечетные числа (19 31), четные числа (4 16 2) и результат сравнения ("NO").


# Получается, программа принимает ввод от пользователя, создает список, а затем подсчитывает нечетные и четные
# числа в этом списке, определяет, каких чисел больше, и выводит результат.

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Вариант №3. - Более компактный код (как мне кажется)

def main():
    n = int(input("Введите длину списка: "))
    numbers = list(map(int, input("Введите элементы списка через пробел: ").split()))

    odd_numbers = [num for num in numbers if num % 2 != 0]
    even_numbers = [num for num in numbers if num % 2 == 0]

    result = "NO" if len(odd_numbers) > len(even_numbers) else "YES"

    print(" ".join(map(str, odd_numbers)))
    print(" ".join(map(str, even_numbers)))
    print(result)

if __name__ == "__main__":
    main()

# Теперь шаг за шагом:

# Шаг №1. - Определение функции main:

# n = int(input("Введите длину списка: ")): Здесь мы считываем длину списка, преобразуя
# введенное значение в целое число.
# numbers = list(map(int, input("Введите элементы списка через пробел: ").split())): Здесь мы считываем элементы списка,
# разделяя введенные числа пробелами и преобразуя их в список целых чисел.
# odd_numbers = [num for num in numbers if num % 2 != 0]: Эта строка создает список нечетных чисел с
# использованием генератора списка.
# even_numbers = [num for num in numbers if num % 2 == 0]: Эта строка создает список четных чисел.
# result = "NO" if len(odd_numbers) > len(even_numbers) else "YES": Это использование тернарного
# оператора для установки значения переменной result в "NO", если нечетных чисел больше, и "YES" в противном случае.

# Шаг №1. - Вывод результатов:

# print(" ".join(map(str, odd_numbers))): Эта строка выводит нечетные числа, объединяя их в строку с
# использованием пробела.
# print(" ".join(map(str, even_numbers))): Эта строка выводит четные числа, также объединяя их в строку.
# print(result): Эта строка выводит значение result.

# Шаг №1. - Запуск программы:

# Пользователь вводит длину списка и элементы списка.
# Программа выводит нечетные числа, четные числа и результат сравнения.


# Таким образом, более компактная версия остается логически аналогичной более подробной версии, но использует
# более сжатый синтаксис для достижения того же результата.

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Задание №2.

# Дано: ↓

# Создайте вложенный список размером 3*3 через функцию. И посчитайте сумму элементов главной диагонали.

# Input:
# 1 2 3
# 4 5 6
# 7 8 9

# Diagonals : 1 + 5 + 9 = 15

# Решение:

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Вариант №1. - Который создает вложенный список размером 3x3 через функцию и затем считает
# сумму элементов главной диагонали:

def create_nested_list():
    nested_list = []
    for i in range(3):
        row = list(map(int, input().split()))
        nested_list.append(row)
    return nested_list

def main():
    # Создание вложенного списка
    matrix = create_nested_list()

    # Сумма элементов главной диагонали
    diagonal_sum = sum(matrix[i][i] for i in range(3))

    # Вывод результата
    print("Diagonals:", "+".join(str(matrix[i][i]) for i in range(3)), "=", diagonal_sum)

if __name__ == "__main__":
    main()

# Снова по пунктам:

# Шаг №1. - Определение функции create_nested_list:

# nested_list = []: Создаем пустой список nested_list, который будет представлять собой вложенный список размером 3x3.
# for i in range(3):: Начинаем цикл, который выполняется три раза для каждой строки вложенного списка.

# row = list(map(int, input().split())): Считываем строку чисел из ввода пользователя, разделяем их с использованием
# split() и преобразуем в список целых чисел с помощью map и int.
# Эта строка представляет собой одну строку вложенного списка.

# nested_list.append(row): Добавляем текущую строку вложенного списка в общий список.


# Шаг №2. - Определение функции main:

# matrix = create_nested_list(): Вызываем функцию create_nested_list() для создания вложенного списка matrix.
# diagonal_sum = sum(matrix[i][i] for i in range(3)): Вычисляем сумму элементов главной диагонали.
# matrix[i][i] обращается к элементам, находящимся на главной диагонали (элементы с одинаковыми индексами
# строки и столбца).

# print("Diagonals:", "+".join(str(matrix[i][i]) for i in range(3)), "=", diagonal_sum): Выводим результат.
# Сначала выводим элементы главной диагонали, объединяя их с помощью join и преобразуя в строки с str. Затем выводим
# знак "равно" и результат суммы.


# Шаг №3. - Запуск программы:

# Пользователь вводит 9 чисел (3 строки по 3 числа в каждой).
# Программа создает вложенный список и вычисляет сумму элементов главной диагонали.
# Результат выводится на экран в формате "Diagonals: 1+5+9 = 15" или аналогичном, в зависимости от введенных чисел.

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Вариант №2. - Вместо использования цикла и ввода данных пользователем,
# можно предопределить вложенный список и затем вычислить сумму элементов главной диагонали.

def create_nested_list():
    return [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

def main():
    # Создание предопределенного вложенного списка
    matrix = create_nested_list()

    # Сумма элементов главной диагонали
    diagonal_sum = sum(matrix[i][i] for i in range(3))

    # Вывод результата
    print("Diagonals:", "+".join(map(str, matrix[i][i] for i in range(3))), "=", diagonal_sum)

if __name__ == "__main__":
    main()

# Подробненько:

# Шаг №1. - Определение функции create_nested_list:

# return [...]: Здесь создается и возвращается вложенный список размером 3x3.
# Вы можете изменить числа в этом списке по своему усмотрению.

# Шаг №2. - Определение функции main:

# matrix = create_nested_list(): Вызывается функция create_nested_list(), чтобы получить
# предопределенный вложенный список.
# diagonal_sum = sum(matrix[i][i] for i in range(3)): Вычисляется сумма элементов главной диагонали,
# используя генератор списка.
# print("Diagonals:", "+".join(map(str, matrix[i][i] for i in range(3))), "=", diagonal_sum): Выводится результат.
# Этот код аналогичен предыдущему, но вместо ввода пользователем, используется предопределенный вложенный список.

# Шаг №3. - Запуск программы:

# Программа создает предопределенный вложенный список.
# Вычисляется и выводится сумма элементов главной диагонали.
# Вот пример вывода для предопределенного вложенного списка:
Diagonals: 1+5+9 = 15

# Если все верно, то программа решает задачу, используя предопределенный вложенный список вместо
# ввода данных пользователем.

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Вариант №3. - Можно решить еще эту задачку используя библиотеку NumPy, которая предоставляет удобные инструменты
# для работы с многомерными массивами.

import numpy as np

def main():
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    diagonal_sum = np.trace(matrix)

    print(f"Diagonals: {'+'.join(map(str, np.diagonal(matrix)))} = {diagonal_sum}")

if __name__ == "__main__":
    main()

# Тут буду расписывать все, как обычно, по вариантам:

# Шаг №1. - Импорт библиотеки NumPy:

# import numpy as np: Здесь мы импортируем библиотеку NumPy и используем сокращение np для удобства.

# Шаг №2. - # Определение функции main:


# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]): Создаем матрицу 3x3 с помощью NumPy.
# Эта строка эквивалентна предыдущему определению вложенного списка.
# diagonal_sum = np.trace(matrix): Вычисляем сумму элементов главной диагонали с использованием функции np.trace.
# print(f"Diagonals: {'+'.join(map(str, np.diagonal(matrix)))} = {diagonal_sum}"): Выводим результат.
# С использованием np.diagonal(matrix) получаем элементы главной диагонали, а с использованием
# f-строки форматируем вывод.

# Шаг №3. - # Запуск программы:

# Программа создает матрицу 3x3.
# Вычисляет и выводит сумму элементов главной диагонали.

# Этот код компактнее, читаемее и эффективнее благодаря использованию NumPy,
# который предоставляет множество функций для работы с массивами и матрицами.

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Задание №2.

# Дано: ↓

# Напишите программу СV (резюме), которая будет считывать данные пользователя,
# через функцию, и выведет полученные данные, при вызове в основном теле программы.

# Решение:

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Вариант №1.
    def get_resume_data():
        name = input("Введите ваше имя: ")
        age = input("Введите ваш возраст: ")
        experience = input("Введите ваш опыт работы: ")
        education = input("Введите ваш уровень образования: ")
        skills = input("Введите ваши навыки через запятую: ")

        # Возвращаем данные в виде словаря
        resume_data = {
            "Имя": name,
            "Возраст": age,
            "Опыт работы": experience,
            "Образование": education,
            "Навыки": skills.split(",")  # Разделяем навыки на список
        }

        return resume_data

    def main():
        print("Добро пожаловать в программу резюме!")
        resume = get_resume_data()

        # Выводим полученные данные
        print("\nВаше резюме:")
        for key, value in resume.items():
            print(f"{key}: {value}")

    if __name__ == "__main__":
        main()

# Теперь шаг за шагом:

# Этап №1. - get_resume_data()
    def get_resume_data():
        name = input("Введите ваше имя: ")
        age = input("Введите ваш возраст: ")
        experience = input("Введите ваш опыт работы: ")
        education = input("Введите ваш уровень образования: ")
        skills = input("Введите ваши навыки через запятую: ")

        # Возвращаем данные в виде словаря
        resume_data = {
            "Имя": name,
            "Возраст": age,
            "Опыт работы": experience,
            "Образование": education,
            "Навыки": skills.split(",")  # Разделяем навыки на список
        }

        return resume_data
# Шаг №1.
def get_resume_data():
# -  Здесь определена функция get_resume_data, которая предназначена для получения данных
# пользователя для составления резюме.

# Шаг №2.
name = input("Введите ваше имя: ")
# С помощью input() программа запрашивает у пользователя ввести своё имя и сохраняет введенное
# значение в переменной name.

# Шаг №3.
age = input("Введите ваш возраст: ")
# Точно так же, как и с именем, программа запрашивает у пользователя ввести свой возраст и сохраняет
# введенное значение в переменной age.

# Шаг №4.
experience = input("Введите ваш опыт работы: ")
# Программа запрашивает у пользователя ввести свой опыт работы и сохраняет введенное значение в переменной experience.

# Шаг №5.
education = input("Введите ваш уровень образования: ")
# Пользователь вводит свой уровень образования, и программа сохраняет значение в переменной education.

# Шаг №6.
skills = input("Введите ваши навыки через запятую: ")
# Пользователь вводит свои навыки, разделяя их запятой, и программа сохраняет значение в переменной skills.

# Шаг №7.
resume_data = {
    "Имя": name,
    "Возраст": age,
    "Опыт работы": experience,
    "Образование": education,
    "Навыки": skills.split(",")  # Разделяем навыки на список
}
# Создается словарь resume_data с ключами, представляющими различные категории резюме,
# и значениями, представляющими введенные пользователем данные. Навыки разделяются на список с помощью split(",").

# Шаг №8.
return resume_data
# Функция возвращает словарь resume_data, содержащий данные, введенные пользователем для резюме.

# Шаг №9.
def main():
# Здесь определена функция main, которая представляет собой основное тело программы.

# Шаг №10.
print("Добро пожаловать в программу резюме!")
# Выводится приветственное сообщение, которое сообщает пользователю о том,
# что они находятся в программе для создания резюме.

# Шаг №11.
resume = get_resume_data()
# Вызывается функция get_resume_data(), чтобы получить данные от пользователя и сохранить их в переменной resume.

# Шаг №12.
print("\nВаше резюме:")
# Выводится заголовок "Ваше резюме:" для отделения приветственного сообщения от данных резюме.

# Шаг №13.
for key, value in resume.items():
# Здесь начинается цикл for, который будет использоваться для итерации по ключам и значениям словаря resume.

# Шаг №14.
print(f"{key}: {value}")
# Для каждой пары ключ-значение в словаре resume программа выводит информацию о резюме в формате "Ключ: Значение".

# Шаг №15.
if __name__ == "__main__":
    main()
# Это условие проверяет, запущен ли скрипт напрямую (а не импортирован ли он в другой скрипт).
# Если скрипт запущен напрямую, то вызывается функция main().

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Вариант №2.
    def get_resume_data():
        return {
            "Имя": input("Введите ваше имя: "),
            "Возраст": input("Введите ваш возраст: "),
            "Опыт работы": input("Введите ваш опыт работы: "),
            "Образование": input("Введите ваш уровень образования: "),
            "Навыки": input("Введите ваши навыки через запятую: ").split(","),
        }

    def main():
        print("Добро пожаловать в программу резюме!\nВаше резюме:")
        print("\n".join([f"{key}: {value}" for key, value in get_resume_data().items()]))

    if __name__ == "__main__":
        main()

# Шаг №1.
def get_resume_data():
# Определение функции get_resume_data.

# Шаг №2.
return {
    "Имя": input("Введите ваше имя: "),
    "Возраст": input("Введите ваш возраст: "),
    "Опыт работы": input("Введите ваш опыт работы: "),
    "Образование": input("Введите ваш уровень образования: "),
    "Навыки": input("Введите ваши навыки через запятую: ").split(","),
}
# Функция get_resume_data возвращает словарь, который создается на лету. Ключи словаря представляют
# различные категории резюме, а значения заполняются данными, введенными пользователем.

# Шаг №3.
def main():
# Определение функции main.

# Шаг №4.
print("Добро пожаловать в программу резюме!\nВаше резюме:")
# Выводится приветственное сообщение, разделительная строка и заголовок резюме.

# Шаг №5.
print("\n".join([f"{key}: {value}" for key, value in get_resume_data().items()]))
# Вывод резюме с использованием генератора списков и метода join. Программа получает данные резюме,
# преобразует их в строки и объединяет их в одну строку с использованием символа новой строки.

# Шаг №6.
if __name__ == "__main__":
    main()
# Это условие проверяет, запущен ли скрипт напрямую (а не импортирован ли он в другой скрипт).
# Если скрипт запущен напрямую, то вызывается функция main().

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Вариант №3.
    def get_resume_data():
        return {category.capitalize(): input(f"Введите ваш {category.lower()}: ") for category in
                ["Имя", "Возраст", "Опыт работы", "Образование", "Навыки"].split()}

    def main():
        print("Добро пожаловать в программу резюме!\nВаше резюме:")
        print("\n".join([f"{key}: {value}" for key, value in get_resume_data().items()]))

    if __name__ == "__main__":
        main()

# В этом варианте:

# Шаг №1. - Ввод данных пользователя в функции get_resume_data() осуществляется с использованием генератора словаря
# и форматирования строк.

# Шаг №2. - Вместо перечисления категорий напрямую, используется метод split() для разделения строки на
# список категорий.

# Шаг №3. - Используется метод capitalize() для форматирования заголовков категорий.

# Шаг №4. - Генератор списка для вывода резюме в функции main() также остается компактным.

                    # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Функции ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
        # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Выполните следующие задания: ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Задание №1.

# Дано: ↓

# Написать рекурсивную функцию, которая по заданному целому числу возвращает n-e
# число Фибоначчи. Ряд Фибоначчи 0, 1, 1, 2, 3, 5, 8, 13,……

# Output:
# fibonacci number 1 = 1
# fibonacci number 2 = 1
# fibonacci number 3 = 2
# fibonacci number 4 = 3
# fibonacci number 5 = 5
# fibonacci number 6 = 8
# fibonacci number 7 = 13
# fibonacci number 8 = 21
# fibonacci number 9 = 34
# fibonacci number 10 = 55

# Решение:

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Вариант №1.
def fibonacci(n):
    if n <= 0:
        return "Введите число больше 0"
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Вывод чисел Фибоначчи для первых 10 элементов
for i in range(1, 11):
    print(f"fibonacci number {i} = {fibonacci(i)}")

# Шаг №1.
def fibonacci(n):
# Определение функции fibonacci, которая принимает аргумент n, представляющий номер числа Фибоначчи.

# Шаг №2.
if n <= 0:
    return "Введите число больше 0"
# Проверка, если n меньше или равно 0, то функция возвращает строку "Введите число больше 0".
# Это базовый случай для некорректного ввода.

# Шаг №3.
elif n == 1:
    return 1
#  Если n равно 1, то функция возвращает 1. Это базовый случай для первого числа Фибоначчи.

# Шаг №4.
elif n == 2:
    return 1
# Если n равно 2, то функция возвращает 1. Это базовый случай для второго числа Фибоначчи.

# Шаг №5.
else:
    return fibonacci(n - 1) + fibonacci(n - 2)
# Если n не равно 1 или 2, то функция возвращает сумму двух предыдущих чисел Фибоначчи,
# вычисленных с использованием рекурсивных вызовов.

# Шаг №6.
for i in range(1, 11):
    print(f"fibonacci number {i} = {fibonacci(i)}")
# Цикл, в котором для каждого числа от 1 до 10 вызывается функция fibonacci, и результат выводится на экран
# в формате "fibonacci number i = значение".

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Вариант №2.

def fibonacci(n, memo={}):
    if n <= 0:
        return "Введите число больше 0"
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n in memo:
        return memo[n]
    else:
        result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        memo[n] = result
        return result

# Вывод чисел Фибоначчи для первых 10 элементов
for i in range(1, 11):
    print(f"fibonacci number {i} = {fibonacci(i)}")

# Шаг №1.
def fibonacci(n, memo={}):
# Определение функции fibonacci с двумя параметрами: n (число, для которого вычисляется число Фибоначчи)
# и memo (словарь для кэширования результатов).

# Шаг №2.
if n <= 0:
    return "Введите число больше 0"
# Проверка, если n меньше или равно 0, то функция возвращает строку "Введите число больше 0".
# Это базовый случай для некорректного ввода.

# Шаг №3.
elif n == 1:
    return 1
# Если n равно 1, то функция возвращает 1. Это базовый случай для первого числа Фибоначчи.

# Шаг №4.
elif n == 2:
     return 1
# Если n равно 2, то функция возвращает 1. Это базовый случай для второго числа Фибоначчи.

# Шаг №5.
elif n in memo:
    return memo[n]
# Если значение n уже присутствует в memo (словаре для кэширования), то функция возвращает сохраненное значение,
# избегая повторных вычислений.

# Шаг №6.
else:
    result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    memo[n] = result
    return result
# Если n не соответствует ни одному из базовых случаев и не находится в memo, то функция вычисляет значение
# fibonacci(n - 1) и fibonacci(n - 2) с использованием рекурсии. Затем результат суммируется,
# сохраняется в memo и возвращается.

# Шаг №7.
# Вывод чисел Фибоначчи для первых 10 элементов
for i in range(1, 11):
    print(f"fibonacci number {i} = {fibonacci(i)}")

# Цикл, в котором для каждого числа от 1 до 10 вызывается функция fibonacci, и результат выводится на экран в формате
# "fibonacci number i = значение".

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Вариант №3. - Это вариант мне подсказал гугл.
from functools import lru_cache
@lru_cache
def fibonacci(n):
    return 1 if n <= 2 else fibonacci(n - 1) + fibonacci(n - 2)
# Вывод чисел Фибоначчи для первых 10 элементов
for i in range(1, 11):
    print(f"fibonacci number {i} = {fibonacci(i)}")

# Шаг №1.
from functools import lru_cache
# Импортируем только lru_cache из модуля functools.

# Шаг №2.
@lru_cache
# Применяем декоратор lru_cache к функции fibonacci.
# Теперь maxsize=None по умолчанию, что означает, что размер кэша не ограничен.

# Шаг №3.
def fibonacci(n):
    return 1 if n <= 2 else fibonacci(n - 1) + fibonacci(n - 2)
# Используем тернарный оператор для более короткой записи выражения. Если n меньше или равно 2, возвращаем 1,
# в противном случае вычисляем сумму двух предыдущих чисел Фибоначчи.

# Шаг №4.
# Вывод чисел Фибоначчи для первых 10 элементов
for i in range(1, 11):
    print(f"fibonacci number {i} = {fibonacci(i)}")
# Цикл, в котором для каждого числа от 1 до 10 вызывается функция fibonacci, и результат выводится на экран в формате
# "fibonacci number i = значение".

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Задание №2.

# Дано: ↓

# Задание №2.
# Напишите функцию, которая проверяет является ли число степенью двойки. Если истинно выведите True, иначе False.
# Input
# 8
# Output
# True

# Решение:

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Вариант №1.
def is_power_of_two(num):
# Используем поразрядное "и" для проверки, является ли число степенью двойки
    return num > 0 and (num & (num - 1)) == 0
# Входные данные
number = int(input("Введите число: "))
# Проверка и вывод результата
result = is_power_of_two(number)
print(result)

# Что под капотом?:
# Шаг №1. - В функции is_power_of_two мы используем поразрядное "и" (&) между числом и его предшественником (num - 1).
# Если результат равен 0, то число является степенью двойки.

# Шаг №2. - В num > 0 мы проверяем, что число положительное, так как степени двойки начинаются с 2^0 = 1.

# Шаг №3. - Пользователю предлагается ввести число, и результат функции выводится на экран.

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Вариант №2.
def is_power_of_two(num):
    return num > 0 and (num & -num) == num
# Входные данные
number = int(input("Введите число: "))
# Проверка и вывод результата
result = is_power_of_two(number)
print(result)
# Этот вариант использует битовое представление отрицательного числа -num для получения самого младшего установленного
# бита в числе. Если результат равен исходному числу, то число является степенью двойки.

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Вариант №3.
def is_power_of_two(num):
    return num > 0 and (num & (num - 1)) == 0
# Входные данные
number = int(input("Введите число: "))
# Проверка и вывод результата
print(is_power_of_two(number))
# Этот код проверяет, что число положительное и использует (num & (num - 1)) == 0 для определения,
# является ли число степенью двойки.

