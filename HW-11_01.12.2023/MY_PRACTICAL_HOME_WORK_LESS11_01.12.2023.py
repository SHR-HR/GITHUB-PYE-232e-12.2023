# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Дата: 01-02 ДЕКАБРЯ 2023
'''''
'''
Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
Дисциплина: Основы программирования на Python
'''
'''
Урок №11 от 29.11.2023 (по факту с 6.11.2023 по 01.12.2023 - Урок №12)
Практическая работа №10 Итераторы, контейнеры и перечисления
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''

'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполните следующие задания:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Задание №1
Создать генератор списка из исходного, который:
'''
'''
→ Этап № 1. Берет только четные значения, отрицательные возводит в куб, остальные в квадрат.
→ Этап № 2. Считает длину строк для списка из строк.
→ Этап № 3. Список квадратов четных чисел.
→ Этап № 4. Только положительные, кратные 5, отрицательные заменить на 0.
→ Этап № 5. Из строки – только гласные буквы.
'''
'''
Решение:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Вариант №1. ↓ 
'''
'''
→ Этап № 1. Берет только четные значения, отрицательные возводит в куб, остальные в квадрат.
'''
original_list = [-2, -1, 0, 1, 2, 3, 4, 5]
modified_list = [x ** 3 if x < 0 else x ** 2 for x in original_list if x % 2 == 0]
print(modified_list)
'''
original_list: Исходный список чисел.
modified_list: Новый список, созданный с использованием спискового включения.
Четные числа возводятся в квадрат, отрицательные возводятся в куб.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
→ Этап № 2. Считает длину строк для списка из строк.
'''
string_list = ["apple", "banana", "cherry"]
lengths = [len(s) for s in string_list]
print(lengths)
'''
string_list: Исходный список строк.
lengths: Новый список, содержащий длины строк из string_list.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
→ Этап № 3. Список квадратов четных чисел.
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares_of_evens = [x ** 2 for x in numbers if x % 2 == 0]
print(squares_of_evens)
'''
numbers: Исходный список чисел.
squares_of_evens: Новый список, содержащий квадраты четных чисел из numbers.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
→ Этап № 4. Только положительные, кратные 5, отрицательные заменить на 0.
'''
numbers = [-10, -7, -5, 0, 3, 6, 9, 15]
modified_numbers = [x if x > 0 and x % 5 == 0 else 0 for x in numbers]
print(modified_numbers)
'''
numbers: Исходный список чисел.
modified_numbers: Новый список, в котором положительные числа, кратные 5, оставлены без изменений,
а отрицательные заменены на 0.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
→ Этап № 5. Из строки – только гласные буквы.
'''
my_string = "Hello, World!"
vowels_only = [char.lower() for char in my_string if char.lower() in "aeiou"]
print(vowels_only)
'''
smy_string: Исходная строка.
vowels_only: Новый список, содержащий только гласные буквы из my_string.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Вариант №2. ↓ 
'''
'''
→ Этап № 1. Берет только четные значения, отрицательные возводит в куб, остальные в квадрат.
'''
original_list = [-2, -1, 0, 1, 2, 3, 4, 5]
modified_list = [x ** 3 if x < 0 else x ** 2 for x in original_list if x % 2 == 0]
print(modified_list)
'''
original_list: Исходный список чисел.
[x ** 3 if x < 0 else x ** 2 for x in original_list if x % 2 == 0]: Создание нового списка с использованием спискового
включения. Четные числа возводятся в квадрат, отрицательные четные возводятся в куб.
print(modified_list): Вывод измененного списка.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
→ Этап № 2. Считает длину строк для списка из строк.
'''
string_list = ["apple", "banana", "cherry"]
lengths = list(map(len, string_list))
print(lengths)
'''
string_list: Исходный список строк.
list(map(len, string_list)): Создание нового списка с использованием map для применения функции len к каждой строке.
print(lengths): Вывод списка длин строк.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
→ Этап № 3. Список квадратов четных чисел.
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares_of_evens = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(squares_of_evens)
'''
numbers: Исходный список чисел.
filter(lambda x: x % 2 == 0, numbers): Фильтрация только четных чисел.
map(lambda x: x ** 2, ...): Применение функции lambda x: x ** 2 к каждому четному числу.
list(...): Преобразование результатов в список.
print(squares_of_evens): Вывод списка квадратов четных чисел.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
→ Этап № 4. Только положительные, кратные 5, отрицательные заменить на 0.
'''
numbers = [-10, -7, -5, 0, 3, 6, 9, 15]
modified_numbers = [x if x > 0 and x % 5 == 0 else 0 for x in numbers]
print(modified_numbers)
'''
numbers: Исходный список чисел.
[x if x > 0 and x % 5 == 0 else 0 for x in numbers]: Создание нового списка с использованием спискового включения.
Положительные числа, кратные 5, остаются без изменений, отрицательные заменяются на 0.
print(modified_numbers): Вывод измененного списка.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
→ Этап № 5. Из строки – только гласные буквы.
'''
my_string = "Hello, World!"
vowels_only = [char.lower() for char in my_string if char.lower() in "aeiou"]
print(vowels_only)
'''
my_string: Исходная строка.
[char.lower() for char in my_string if char.lower() in "aeiou"]: Создание нового списка с использованием
спискового включения. Включаются только гласные буквы (в нижнем регистре).
print(vowels_only): Вывод списка гласных букв.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Вариант №3. ↓ 
'''
from itertools import count, cycle, repeat
# 1. Берем только четные значения, отрицательные возводим в куб, остальные в квадрат
original_list = [-2, -1, 0, 1, 2, 3, 4, 5]
modified_list_1 = [x ** 3 if x < 0 else x ** 2 for x in original_list if x % 2 == 0]
# 2. Считаем длину строк для списка из строк
string_list = ["apple", "banana", "cherry"]
lengths = list(map(len, string_list))
# 3. Список квадратов четных чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares_of_evens = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
# 4. Только положительные, кратные 5, отрицательные заменяем на 0
numbers_4 = [-10, -7, -5, 0, 3, 6, 9, 15]
modified_numbers_4 = [x if x > 0 and x % 5 == 0 else 0 for x in numbers_4]
# 5. Из строки – только гласные буквы
my_string = "Hello, World!"
vowels_only = [char.lower() for char in my_string if char.lower() in "aeiou"]
# Вывод результатов
print("1. Модифицированный список:", modified_list_1)
print("2. Длины строк:", lengths)
print("3. Квадраты четных чисел:", squares_of_evens)
print("4. Модифицированные числа:", modified_numbers_4)
print("5. Только гласные:", vowels_only)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1. ↓ - Создание списка с модификацией четных значений:
'''
'''
original_list: Исходный список чисел.
[x ** 3 if x < 0 else x ** 2 for x in original_list if x % 2 == 0]: Создание нового списка с использованием спискового
включения. Четные числа возводятся в квадрат, отрицательные четные возводятся в куб.
'''
'''
Шаг №2. ↓ - Считаем длину строк для списка из строк:
'''
'''
string_list: Исходный список строк.
list(map(len, string_list)): Создание нового списка с использованием map для применения функции len к каждой строке.
'''
'''
Шаг №3. ↓ - Список квадратов четных чисел:
'''
'''
numbers: Исходный список чисел.
filter(lambda x: x % 2 == 0, numbers): Фильтрация только четных чисел.
map(lambda x: x ** 2, ...): Применение функции lambda x: x ** 2 к каждому четному числу.
'''
'''
Шаг №4. ↓ - Только положительные, кратные 5, отрицательные заменяем на 0:
'''
'''
numbers_4: Исходный список чисел.
[x if x > 0 and x % 5 == 0 else 0 for x in numbers_4]: Создание нового списка с использованием спискового включения.
Положительные числа, кратные 5, остаются без изменений, отрицательные заменяются на 0.
'''
'''
Шаг №5. ↓ - Из строки – только гласные буквы:
'''
'''
my_string: Исходная строка.
[char.lower() for char in my_string if char.lower() in "aeiou"]: Создание нового списка с использованием
спискового включения. Включаются только гласные буквы (в нижнем регистре).
'''
'''
Шаг №6. ↓ - Вывод результатов:
'''
'''
print("1. Модифицированный список:", modified_list_1): Вывод измененного списка из Шага 1.
print("2. Длины строк:", lengths): Вывод списка длин строк из Шага 2.
print("3. Квадраты четных чисел:", squares_of_evens): Вывод списка квадратов четных чисел из Шага 3.
print("4. Модифицированные числа:", modified_numbers_4): Вывод измененного списка из Шага 4.
print("5. Только гласные:", vowels_only): Вывод списка гласных букв из Шага 5.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Итераторы, контейнеры и перечисления
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
                    ↓   ↓   ↓   ↓   Выполните следующие задания:    ↓   ↓   ↓   ↓

Задание №1. - Написать декоратор, который оборачивает строку в теги <i></i>.
Задание №2. - Написать декоратор, который оборачивает строку в теги <strong></strong>.
Задание №3. - Применить оба декоратора.
Задание №4. - Написать декоратор, который в любую функцию, в __doc__ дописывает имя и фамилию автора.
                                                                                                      @createdbyme
                                                                                                      def a():
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #                              # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Декоратор для оборачивания строки в теги <i></i>
'''
def italic_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<i>{result}</i>"
    return wrapper
# Пример использования декоратора
@italic_decorator
def some_text():
    return "Это текст, выделенный курсивом."
italicized_text = some_text()
print(italicized_text)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #                              # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1. ↓ - Декоратор italic_decorator:
'''
def italic_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<i>{result}</i>"
    return wrapper
'''
Декоратор italic_decorator принимает функцию func в качестве аргумента.
Внутренняя функция wrapper вызывает исходную функцию func, сохраняет её результат в переменной result,
и затем оборачивает этот результат в тег <i> (курсив).
wrapper возвращает новую строку с результатом выполнения func в теге <i>.
'''
'''
Шаг №2. ↓ - Применение декоратора к функции some_text:
'''
@italic_decorator
def some_text():
    return "Это текст, выделенный курсивом."
'''
Это ваша исходная функция some_text.
Она декорирована с использованием @italic_decorator.
'''
'''
Шаг №3. ↓ - Вызов функции some_text:
'''
italicized_text = some_text()
'''
Теперь мы вызываем функцию some_text после того, как она была декорирована.
'''
'''
Шаг №4. ↓ - Вывод строки с выделенным курсивом текстом:
'''
print(italicized_text)
'''
Затем выводится результат функции, который представляет собой строку "<i>Это текст, выделенный курсивом.</i>".
'''
'''
После выполнения этих шагов переменная italicized_text будет содержать отформатированный текст,
и при выводе её на экран мы увидим строку с выделенным курсивом текстом.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #                              # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Декоратор для оборачивания строки в теги <strong></strong>
'''
def strong_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<strong>{result}</strong>"
    return wrapper
# Пример использования декоратора
@strong_decorator
def some_text():
    return "Это ""жирный"" текст."
strong_text = some_text()
print(strong_text)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #                              # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1. ↓ - Декоратор strong_decorator:
'''
def strong_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<strong>{result}</strong>"
    return wrapper
'''
Этот декоратор strong_decorator принимает функцию func в качестве аргумента.
Внутренняя функция wrapper вызывает исходную функцию func, сохраняет её результат в переменной result,
и затем оборачивает этот результат в тег <strong> (жирный).
wrapper возвращает новую строку с результатом выполнения func в теге <strong>.
'''
'''
Шаг №2. ↓ - Применение декоратора к функции some_text:
'''
@strong_decorator
def some_text():
    return "Это жирный текст."
'''
Это ваша исходная функция some_text.
Она декорирована с использованием @strong_decorator.
'''
'''
Шаг №3. ↓ - Вызов функции some_text:
'''
strong_text = some_text()
'''
Теперь мы вызываем функцию some_text после того, как она была декорирована.
'''
'''
Шаг №4. ↓ - Вывод строки с жирным текстом:
'''
print(strong_text)
'''
Затем выводится результат функции, который представляет собой строку "<strong>Это жирный текст.</strong>".
'''
'''
После выполнения этих шагов переменная strong_text будет содержать отформатированный текст,
и при выводе её на экран мы увидим строку с жирным текстом.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #                              # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Применение обоих декораторов
'''
def italic_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<i>{result}</i>"
    return wrapper
def strong_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<strong>{result}</strong>"
    return wrapper
@strong_decorator
@italic_decorator
def some_text():
    return "Это выделенный курсивом и ""жирный"" текст."
formatted_text = some_text()
print(formatted_text)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #                              # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1. ↓ - Декоратор italic_decorator:
'''
def italic_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<i>{result}</i>"
    return wrapper
'''
Декоратор italic_decorator принимает функцию func в качестве аргумента.
Он определяет внутреннюю функцию wrapper, которая вызывает исходную функцию func и сохраняет её результат
в переменной result.
Затем wrapper возвращает новую строку, включающую результат выполнения func в тег <i> (курсив).
'''
'''
Шаг №2. ↓ - Декоратор strong_decorator:
'''
def strong_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<strong>{result}</strong>"
    return wrapper
'''
Декоратор strong_decorator также принимает функцию func в качестве аргумента.
Он определяет внутреннюю функцию wrapper, которая вызывает исходную функцию func и сохраняет её результат
в переменной result.
Затем wrapper возвращает новую строку, включающую результат выполнения func в тег <strong> (жирный).
'''
'''
Шаг №3. ↓ - Применение декораторов к функции some_text:
'''
@strong_decorator
@italic_decorator
def some_text():
    return "Это выделенный курсивом и жирный текст."
'''
Это ваша исходная функция some_text.
Она декорирована сначала @italic_decorator, а затем @strong_decorator.
Такой порядок означает, что сначала применится italic_decorator, а затем strong_decorator.
'''
'''
Шаг №4. ↓ - Вызов функции some_text:
'''
formatted_text = some_text()
'''
Теперь мы вызываем функцию some_text после того, как она была декорирована.
'''
'''
Шаг №5. ↓ - Вывод отформатированного текста:
'''
print(formatted_text)
'''
Затем выводится результат функции, который представляет собой строку, оформленную сначала курсивом, а затем жирным.
'''
'''
После выполнения этих шагов переменная formatted_text будет содержать строку
 "<strong><i>Это выделенный курсивом и жирный текст.</i></strong>", 
и при выводе её на экран мы увидим отформатированный текст.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #                              # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Декоратор для добавления информации об авторе в __doc__
'''
def createdbyme_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not func.__doc__:
            func.__doc__ = ""
        func.__doc__ += "\n\nCreated by: Ваше Имя и Фамилия"
        return result
    return wrapper
@createdbyme_decorator
def a():
    """
    Это документация для функции a.
    """
    return "Function a"
# Вывод документации после применения декоратора
print(a.__doc__)
'''
В Python, если функция не возвращает явно указанное значение (с помощью оператора return),
она возвращает None по умолчанию. В вашем коде функция a() не возвращает явно указанное значение,
поэтому её результат - None.

def wrapper(*args, **kwargs):
    result = func(*args, **kwargs)
    if not func.__doc__:
        func.__doc__ = ""
    func.__doc__ += "\n\nCreated by: Ваше Имя и Фамилия"
    return result
    
Если вы хотите, чтобы функция a() возвращала какое-то значение, вы можете явно указать return внутри функции. Например:

@createdbyme_decorator
def a():
    """
    Это документация для функции a.
    """
    return "Function a"

Теперь, если вы вызовете a(), результатом будет строка "Function a", а не None.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #                              # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1. ↓ - Декоратор createdbyme_decorator:
'''
def createdbyme_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not func.__doc__:
            func.__doc__ = ""
        func.__doc__ += "\n\nCreated by: Ваше Имя и Фамилия"
        return result
    return wrapper
'''
Декоратор createdbyme_decorator принимает функцию func в качестве аргумента.
Он определяет внутреннюю функцию wrapper,
которая вызывает исходную функцию func и сохраняет её результат в переменной result.
Затем, если документация функции (func.__doc__) не существует, создается пустая строка.
В любом случае, к документации добавляется строка с информацией об авторе.
В конце wrapper возвращает результат выполнения исходной функции.
'''
'''
Шаг №2. ↓ - Функция a:
'''
@createdbyme_decorator
def a():
    """
    Это документация для функции a.
    """
    return "Function a"
'''
Это ваша исходная функция a.
Она декорирована с использованием @createdbyme_decorator, что означает,
что будет применен указанный декоратор к этой функции.
'''
'''
Шаг №3. ↓ - Вызов функции a:
'''
result = a()
'''
Теперь мы вызываем функцию a после того, как она была декорирована.
Результат выполнения функции сохраняется в переменной result.
'''
'''
Шаг №4. ↓ - Вывод документации:
'''
print(a.__doc__)
'''
Выводим документацию функции после применения декоратора.
'''
'''
Как я понял, после выполнения этих шагов в result будет сохранено значение "Function a",
и при выводе документации функции a (a.__doc__) мы увидим,
что к документации была добавлена строка "Created by: Ваше Имя и Фамилия".
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #      ~ ~ ~ ~ ~ ~ ~ ~ ~      # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
                                    А ЧТО ЕСЛИ НУЖНО БЫЛО ПИСАТЬ КОД ТАК!!!???                                    
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #      ~ ~ ~ ~ ~ ~ ~ ~ ~      # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
def italic_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"\033[3m{result}\033[0m"  # ANSI escape sequence for italics (ANSI для курсива)
    return wrapper

@italic_decorator
def some_text():
    return "Это текст, выделенный курсивом."

italicized_text = some_text()
print(italicized_text)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #                              # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1. ↓ - Декоратор italic_decorator:
'''
def italic_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"\033[3m{result}\033[0m"  # ANSI escape sequence for italics (ANSI для курсива)
    return wrapper
'''
Декоратор italic_decorator принимает функцию func в качестве аргумента.
Внутренняя функция wrapper вызывает исходную функцию func, сохраняет её результат в переменной result.
Затем wrapper возвращает новую строку, в которой результат выполнения func заключается в ANSI escape-последовательность
для курсива. В данном случае, \033[3m включает режим курсива, а \033[0m выключает его.
'''
'''
Шаг №2. ↓ - Применение декоратора к функции some_text:
'''
@italic_decorator
def some_text():
    return "Это текст, выделенный курсивом."
'''
Это ваша исходная функция some_text.
Она декорирована с использованием @italic_decorator.
'''
'''
Шаг №3. ↓ - Вызов функции some_text:
'''
italicized_text = some_text()
'''
Теперь мы вызываем функцию some_text после того, как она была декорирована.
'''
'''
Шаг №4. ↓ - Вывод строки с выделенным курсивом текстом:
'''
print(italicized_text)
'''
Затем выводится результат функции, который представляет собой строку с текстом,
выделенным курсивом с использованием ANSI escape-последовательности.
'''
'''
Этот код использует ANSI escape-последовательность для стилизации текста.
В данном случае, \033[3m включает режим курсива, а \033[0m выключает его.
Это может не поддерживаться всеми терминалами, но в большинстве случаев это будет работать, особенно в терминалах
с поддержкой ANSI escape-последовательностей, таких как большинство терминалов Unix и Linux.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #      ~ ~ ~ ~ ~ ~ ~ ~ ~      # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
def strong_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"\033[1m{result}\033[0m"  # ANSI escape sequence for bold
    return wrapper

@strong_decorator
def some_text():
    return "Это ""жирный"" текст."

strong_text = some_text()
print(strong_text)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #      ~ ~ ~ ~ ~ ~ ~ ~ ~      # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1. ↓ - Декоратор strong_decorator:
'''
def strong_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"\033[1m{result}\033[0m"  # ANSI escape sequence for bold
    return wrapper
'''
Декоратор strong_decorator принимает функцию func в качестве аргумента.
Внутренняя функция wrapper вызывает исходную функцию func, сохраняет её результат в переменной result.
Затем wrapper возвращает новую строку, в которой результат выполнения func заключается в ANSI
escape-последовательность для жирного шрифта. В данном случае,
\033[1m включает режим жирного шрифта, а \033[0m выключает его.
'''
'''
Шаг №2. ↓ - Применение декоратора к функции some_text:
'''
@strong_decorator
def some_text():
    return "Это жирный текст."
'''
Это ваша исходная функция some_text.
Она декорирована с использованием @strong_decorator.
'''
'''
Шаг №3. ↓ - Вызов функции some_text:
'''
strong_text = some_text()
'''
Теперь мы вызываем функцию some_text после того, как она была декорирована.
'''
'''
Шаг №4. ↓ - Вывод строки с жирным текстом:
'''
print(strong_text)
'''
Затем выводится результат функции, который представляет собой строку с текстом,
выделенным жирным шрифтом с использованием ANSI escape-последовательности.
'''
'''
Этот код также использует ANSI escape-последовательности для стилизации текста.
В данном случае, \033[1m включает режим жирного шрифта, а \033[0m выключает его.
Аналогично предыдущему коду, это может не поддерживаться всеми терминалами, но в большинстве случаев будет работать
в терминалах с поддержкой ANSI escape-последовательностей.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #      ~ ~ ~ ~ ~ ~ ~ ~ ~      # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
def italic_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"\033[3m{result}\033[0m"  # ANSI escape sequence for italics
    return wrapper

def strong_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"\033[1m{result}\033[0m"  # ANSI escape sequence for bold
    return wrapper

@strong_decorator
@italic_decorator
def some_text():
    return "Это выделенный курсивом и ""жирный"" текст."

formatted_text = some_text()
print(formatted_text)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #      ~ ~ ~ ~ ~ ~ ~ ~ ~      # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1. ↓ - Декоратор italic_decorator:
'''
def italic_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"\033[3m{result}\033[0m"  # ANSI escape sequence for italics
    return wrapper
'''
italic_decorator принимает функцию func в качестве аргумента.
wrapper вызывает func, сохраняет результат в result, и возвращает новую строку с результатом,
который заключается в ANSI escape-последовательность для курсива
(\033[3m включает режим курсива, а \033[0m выключает его).
'''
'''
Шаг №2. ↓ - Декоратор strong_decorator:
'''
def strong_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"\033[1m{result}\033[0m"  # ANSI escape sequence for bold
    return wrapper
'''
strong_decorator также принимает функцию func в качестве аргумента.
wrapper вызывает func, сохраняет результат в result, и возвращает новую строку с результатом, который заключается 
в ANSI escape-последовательность для жирного шрифта (\033[1m включает режим жирного шрифта, а \033[0m выключает его).
'''
'''
Шаг №3. ↓ - Применение декораторов к функции some_text:
'''
@strong_decorator
@italic_decorator
def some_text():
    return "Это выделенный курсивом и жирный текст."
'''
some_text - это ваша исходная функция.
Она сначала декорирована @italic_decorator, а затем @strong_decorator.
Такой порядок означает, что сначала применится italic_decorator, а затем strong_decorator.
'''
'''
Шаг №4. ↓ - Вызов функции some_text:
'''
formatted_text = some_text()
'''
Теперь мы вызываем функцию some_text после того, как она была декорирована обоими декораторами.
'''
'''
Шаг №5. ↓ - Вывод отформатированного текста:
'''
print(formatted_text)
'''
Затем выводится результат функции, который представляет собой строку с текстом,
выделенным и курсивом, и жирным шрифтом, используя соответствующие ANSI escape-последовательности.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #      ~ ~ ~ ~ ~ ~ ~ ~ ~      # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
                                                     ВСЕ В ОДНОМ
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #      ~ ~ ~ ~ ~ ~ ~ ~ ~      # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
def italic_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"\033[3m{result}\033[0m"  # ANSI escape sequence for italics
    return wrapper

def strong_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"\033[1m{result}\033[0m"  # ANSI escape sequence for bold
    return wrapper

def createdbyme_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not func.__doc__:
            func.__doc__ = ""
        func.__doc__ += "\n\nCreated by: Ваше Имя и Фамилия"
        return result
    return wrapper

# Примеры использования декораторов:

@italic_decorator
def some_italic_text():
    return "Это текст, выделенный курсивом."

italicized_text = some_italic_text()
print(italicized_text)

@strong_decorator
def some_strong_text():
    return "Это жирный текст."

strong_text = some_strong_text()
print(strong_text)

@strong_decorator
@italic_decorator
def some_combined_text():
    return "Это выделенный курсивом и жирный текст."

formatted_text = some_combined_text()
print(formatted_text)

@createdbyme_decorator
def function_a():
    """
    Это документация для функции a.
    """
    return "Function a"

# Вывод документации после применения декоратора
print(function_a.__doc__)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #      ~ ~ ~ ~ ~ ~ ~ ~ ~      # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1. ↓ - Декораторы:
'''
def italic_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"\033[3m{result}\033[0m"  # ANSI escape sequence for italics
    return wrapper

def strong_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"\033[1m{result}\033[0m"  # ANSI escape sequence for bold
    return wrapper

def createdbyme_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not func.__doc__:
            func.__doc__ = ""
        func.__doc__ += "\n\nCreated by: Ваше Имя и Фамилия"
        return result
    return wrapper
'''
italic_decorator:

Этот декоратор принимает функцию func и возвращает новую функцию wrapper.
wrapper вызывает func и добавляет ANSI escape-последовательность для курсива к результату.

strong_decorator:

Этот декоратор также принимает функцию func и возвращает новую функцию wrapper.
wrapper вызывает func и добавляет ANSI escape-последовательность для жирного шрифта к результату.

createdbyme_decorator:

Этот декоратор принимает функцию func и возвращает новую функцию wrapper.
wrapper вызывает func, проверяет наличие документации, и добавляет строку с информацией об авторе в документацию.
'''
'''
Шаг №2. ↓ - Примеры использования декораторов:
'''
@italic_decorator
def some_italic_text():
    return "Это текст, выделенный курсивом."

italicized_text = some_italic_text()
print(italicized_text)
'''
some_italic_text:
Функция some_italic_text декорирована italic_decorator.
Вызывается some_italic_text, результат сохраняется в italicized_text.
Выводится italicized_text.
'''
@strong_decorator
def some_strong_text():
    return "Это жирный текст."

strong_text = some_strong_text()
print(strong_text)
'''
some_strong_text:
Функция some_strong_text декорирована strong_decorator.
Вызывается some_strong_text, результат сохраняется в strong_text.
Выводится strong_text.
'''
@strong_decorator
@italic_decorator
def some_combined_text():
    return "Это выделенный курсивом и жирный текст."

formatted_text = some_combined_text()
print(formatted_text)
'''
some_combined_text:
Функция some_combined_text декорирована сначала italic_decorator, затем strong_decorator.
Вызывается some_combined_text, результат сохраняется в formatted_text.
Выводится formatted_text.
'''
@createdbyme_decorator
def function_a():
    """
    Это документация для функции a.
    """
    return "Function a"

# Вывод документации после применения декоратора
print(function_a.__doc__)
'''
function_a:
Функция function_a декорирована createdbyme_decorator.
Вызывается function_a, результат не сохраняется, но документация функции изменяется.
Выводится документация function_a после применения декоратора.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #      ~ ~ ~ ~ ~ ~ ~ ~ ~      # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #



