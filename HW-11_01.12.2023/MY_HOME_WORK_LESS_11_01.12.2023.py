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
Домашнее задание №10: Итераторы, контейнеры и перечисления
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
→ Этап № 1. из [1,2,3,4,5,6,7] получить {1: 1, 3: 27, 5: 125, 7: 343}.
→ Этап № 2. из [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7] получить {2, 4, 6}.
→ Этап № 3. получить список [0, 10, 20, 30, 40, 50, 60, 70, 80, 90] без исходного.
→ Этап № 4. написать функцию-генератор с yield, которая может перебирать числа, делящиеся на 7, в диапазоне от 0 до n.
'''
'''
Решение:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Вариант №1. ↓ 
'''
# Задание 1
def generator_1(input_list):
    return {x: x**3 for x in input_list if x % 2 != 0}

# Задание 2
def generator_2(input_list):
    return {x for x in input_list if x % 2 == 0}

# Задание 3
def generator_3():
    return [i * 10 for i in range(10)]

# Задание 4
def divisor_generator(n):
    for i in range(n + 1):
        if i % 7 == 0:
            yield i

# Примеры использования
input_list_1 = [1, 2, 3, 4, 5, 6, 7]
input_list_2 = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

result_1 = generator_1(input_list_1)
result_2 = generator_2(input_list_2)
result_3 = generator_3()
result_4 = list(divisor_generator(100))

print(result_1)
print(result_2)
print(result_3)
print(result_4)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
→ Задание №1. из [1,2,3,4,5,6,7] получить {1: 1, 3: 27, 5: 125, 7: 343}.
'''
''''
Шаг №1. - Определение функции generator_1, которая принимает входной список.
''''
def generator_1(input_list):
''''
Шаг №2. - Использование генератора словаря для создания нового словаря.
В этом случае, мы берем каждый элемент из исходного списка, проверяем, является ли он нечетным,
и создаем новую пару ключ-значение.
''''
return {x: x ** 3 for x in input_list if x % 2 != 0}
''''
Шаг №3. - Применение генератора к исходному списку.
'''''
input_list_1 = [1, 2, 3, 4, 5, 6, 7]
result_1 = generator_1(input_list_1)
print(result_1)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
→ Задание №2. из [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7] получить {2, 4, 6}.
'''
''''
Шаг №1. - Определение функции generator_2, которая принимает входной список.
''''
def generator_2(input_list):
''''
Шаг №2. -  Использование генератора множества для создания нового множества.
В этом случае, мы берем каждый элемент из исходного списка, проверяем, является ли он четным,
и добавляем его в новое множество.
''''
return {x for x in input_list if x % 2 == 0}
''''
Шаг №3. -  Применение генератора к исходному списку.
''''
input_list_2 = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
result_2 = generator_2(input_list_2)
print(result_2)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
→ Задание №3. получить список [0, 10, 20, 30, 40, 50, 60, 70, 80, 90] без исходного.
'''
''''
Шаг №1. - Определение функции generator_3.
''''
def generator_3():
''''
Шаг №2. - Использование генератора списка для создания нового списка. 
В этом случае, мы используем цикл for для создания списка, содержащего элементы, равные i * 10, 
где i изменяется от 0 до 9.
''''
return [i * 10 for i in range(10)]
''''
Шаг №3. -  Применение генератора.
''''
result_3 = generator_3()
print(result_3)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
→ Задание №4. написать функцию-генератор с yield, которая может перебирать числа, делящиеся на 7,
в диапазоне от 0 до n.
'''
''''
Шаг №1. - Определение функции divisor_generator, принимающей параметр n.
''''
def divisor_generator(n):
''''
Шаг №2. - Использование оператора yield в цикле для создания генератора,
который возвращает числа, делящиеся на 7 в диапазоне от 0 до n.
''''
for i in range(n + 1):
    if i % 7 == 0:
        yield i
''''
Шаг №3. - Применение генератора и преобразование его в список для вывода результатов.
''''
result_4 = list(divisor_generator(100))
print(result_4)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Вариант №2. ↓ 
'''
'''
→ Задание №1. из [1,2,3,4,5,6,7] получить {1: 1, 3: 27, 5: 125, 7: 343}.
'''
def generator_1(input_list):
    return {x: x**3 for x in input_list if x % 2 != 0}

input_list_1 = [1, 2, 3, 4, 5, 6, 7]
result_1 = generator_1(input_list_1)
print(result_1)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Шаг №1. - Определение функции generator_1, принимающей входной список.
''''
def generator_1(input_list):
''''
Шаг №2. - Использование генератора словаря для создания нового словаря. В данном случае, создается словарь,
в котором ключами являются нечетные числа из исходного списка, а значениями — кубы этих чисел.
''''
return {x: x ** 3 for x in input_list if x % 2 != 0}
''''
Шаг №3. - Применение генератора к исходному списку.
''''
input_list_1 = [1, 2, 3, 4, 5, 6, 7]
result_1 = generator_1(input_list_1)
print(result_1)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
→ Задание №2. из [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7] получить {2, 4, 6}.
'''
def generator_2(input_list):
    return {x for x in input_list if x % 2 == 0}

input_list_2 = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
result_2 = generator_2(input_list_2)
print(result_2)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Шаг №1. - Определение функции generator_2, принимающей входной список.
''''
def generator_2(input_list):
''''
Шаг №2. - Использование генератора множества для создания нового множества.
В данном случае, создается множество, содержащее только четные числа из исходного списка.
''''
return {x for x in input_list if x % 2 == 0}
''''
Шаг №3. - Применение генератора к исходному списку.
''''
input_list_2 = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
result_2 = generator_2(input_list_2)
print(result_2)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
→ Задание №3. получить список [0, 10, 20, 30, 40, 50, 60, 70, 80, 90] без исходного.
'''
def generator_3():
    return list(range(0, 91, 10))

result_3 = generator_3()
print(result_3)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Шаг №1. - Определение функции generator_3.
''''
def generator_3():
''''
Шаг №2. - Использование генератора списка для создания нового списка.
В данном случае, создается список, содержащий элементы, равные i * 10, где i изменяется от 0 до 9.
''''
return list(range(0, 91, 10))
''''
Шаг №3. - Применение генератора.
''''
result_3 = generator_3()
print(result_3)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
→ Задание №4. написать функцию-генератор с yield, которая может перебирать числа, делящиеся на 7,
в диапазоне от 0 до n.
'''
def divisor_generator(n):
    current_num = 0
    while current_num <= n:
        if current_num % 7 == 0:
            yield current_num
        current_num += 1

result_4 = list(divisor_generator(100))
print(result_4)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Шаг №1. - Определение функции divisor_generator, принимающей параметр n.
''''
def divisor_generator(n):
''''
Шаг №2. - Использование оператора yield в цикле для создания генератора,
который возвращает числа, делящиеся на 7 в диапазоне от 0 до n.
''''
current_num = 0
while current_num <= n:
    if current_num % 7 == 0:
        yield current_num
    current_num += 1
''''
Шаг №3. - Применение генератора и преобразование его в список для вывода результатов.
''''
result_4 = list(divisor_generator(100))
print(result_4)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Итераторы, контейнеры и перечисления в Python.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполните следующие задания:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
На вход подается последовательность символов (символы могут быть любыми, в том числе и не буквенными,
могут повторяться).

Выведите все слова, которые можно составить из букв данной последовательности и их количество.

Если в последовательности буква повторяется, то и в словах она может повторяться,
но количество повторений в слове должно быть не более количества повторений в последовательности.

Если в последовательности буква встречается 1 раз, то и в словах буква может встречаться не более 1 раза.

Слова должны выводиться в порядке возрастания длины, в последовательности не должно быть двух одинаковых слов.

Помните, что в словах позиция буквы имеет значение, т.е. слова dog и god – 2 разных слова.
 
Воспользуйтесь средствами модуля itertools.
'''
'''
Input: k98.ok

Output:

8
o
k
ok
kk
ko
okk
kko
kok

'''

'''
Решение:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Вариант №1. ↓ 
'''
import re
from itertools import permutations


def generate_words(input_str):
    # Фильтрация символов, оставляем только буквы
    filtered_str = re.sub(r'[^a-zA-Z]', '', input_str)

    words = set()

    for r in range(1, len(filtered_str) + 1):
        # Генерация перестановок букв заданной длины
        perms = permutations(filtered_str, r)
        for perm in perms:
            word = ''.join(perm)
            words.add(word)

    # Сортировка слов по длине и лексикографическому порядку, с числами и цифрами впереди
    sorted_words = sorted(words, key=lambda x: (not x.isdigit(), len(x), x))

    for w in sorted_words:
        print(w)

    # Вывод общего количества слов
    print(len(sorted_words))


# Пример использования
input_str = "k98.ok"
generate_words(input_str)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Шаг №1. - Импорт модулей.
''''
import re
from itertools import permutations
''''
В этом шаге импортируются два модуля: re (регулярные выражения) и permutations из модуля itertools.
Регулярные выражения будут использоваться для фильтрации символов в строке, а permutations для генерации перестановок.
''''
''''
Шаг №2. - Определение функции generate_words.
''''
def generate_words(input_str):
''''
Это определение функции generate_words, которая принимает в качестве аргумента строку input_str.
''''
''''
Шаг №3. - Фильтрация символов в строке.
''''
filtered_str = re.sub(r'[^a-zA-Z]', '', input_str)
''''
В этом шаге используется регулярное выражение для удаления всех символов,
кроме букв (как строчных, так и заглавных) из входной строки input_str.
Результат сохраняется в переменной filtered_str.
''''
''''
Шаг №4. - Инициализация множества words.
''''
words = set()
''''
Создается пустое множество words, в котором будут храниться уникальные слова.
''''
''''
Шаг №5. - Генерация перестановок букв.
''''
for r in range(1, len(filtered_str) + 1):
    perms = permutations(filtered_str, r)
    for perm in perms:
        word = ''.join(perm)
        words.add(word)
''''
Здесь используется цикл for, чтобы генерировать перестановки букв в строке filtered_str различной
длины (от 1 до длины строки). Для каждой перестановки создается строка word, которая добавляется в множество words.
''''
''''
Шаг №6. - Сортировка слов.
''''
sorted_words = sorted(words, key=lambda x: (not x.isdigit(), len(x), x))
''''
Слова в множестве words сортируются по следующему ключу:

Сначала идут слова, не состоящие только из цифр (not x.isdigit()).
Затем идет сортировка по длине слова (len(x)).
Наконец, сортировка по самим словам в лексикографическом порядке (x).
''''
''''
Шаг №7. - Вывод отсортированных слов.
''''
for w in sorted_words:
    print(w)
''''
Каждое отсортированное слово выводится на экран.
''''
''''
Шаг №8. - Вывод отсортированных слов.
''''
print(len(sorted_words))
''''
Печать общего количества отсортированных слов.
''''
''''
Шаг №9. - Пример использования функции.
''''
# Пример использования
input_str = "k98.ok"
generate_words(input_str)
''''
Пример вызова функции generate_words с аргументом "k98.ok". Функция будет выполнять все шаги выше для данной строки.
''''
''''
Таким образом, код выполняет генерацию всех возможных комбинаций букв в строке,
фильтрует их и сортирует для последующего вывода.
''''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Вариант №2. ↓ 
'''
import re
from itertools import permutations

def generate_words(input_str):
    # Фильтрация символов, оставляем только буквы
    filtered_str = re.sub(r'[^a-zA-Z]', '', input_str)

    words = set()

    # Создание итератора для всех возможных перестановок букв
    perms_iter = permutations(filtered_str)

    for r in range(1, len(filtered_str) + 1):
        # Генерация перестановок букв заданной длины
        perms = permutations(filtered_str, r)
        for perm in perms:
            word = ''.join(perm)
            words.add(word)

    # Фильтрация слов по правилам задачи
    filtered_words = [word for word in words if all(word.count(char) <= filtered_str.count(char) for char in set(word))]

    # Сортировка слов по длине и лексикографическому порядку
    sorted_words = sorted(filtered_words, key=lambda x: (len(x), x))

    # Вывод количества слов
    print(len(sorted_words))

    # Вывод отсортированных слов
    for w in sorted_words:
        print(w)

# Пример использования
input_str = "k98.ok"
generate_words(input_str)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Шаг №1. - Импорт модулей
''''
import re
from itertools import permutations
''''
Здесь мы импортируем модуль re для работы с регулярными выражениями 
и модуль permutations из itertools для генерации перестановок.
''''
''''
Шаг №2. - Определение функции generate_words
''''
def generate_words(input_str):
''''
Это определение функции generate_words, которая принимает входную строку input_str.
''''
''''
Шаг №3. - Фильтрация символов в строке
''''
filtered_str = re.sub(r'[^a-zA-Z]', '', input_str)
''''
Здесь мы используем регулярное выражение, чтобы оставить только буквы в строке и убрать все остальные символы.
''''
''''
Шаг №4. - Инициализация пустого множества words
''''
words = set()
''''
Создаем пустое множество words, в котором будем хранить уникальные слова.
''''
''''
Шаг №5. - Генерация перестановок букв
''''
for r in range(1, len(filtered_str) + 1):
    perms = permutations(filtered_str, r)
    for perm in perms:
        word = ''.join(perm)
        words.add(word)
''''
Здесь мы используем цикл для генерации перестановок букв различной длины от 1 до длины отфильтрованной строки.
Полученные слова добавляются в множество words.
''''
''''
Шаг №6. - Фильтрация слов по правилам задачи
''''
filtered_words = [word for word in words if all(word.count(char) <= filtered_str.count(char) for char in set(word))]
''''
Мы фильтруем слова по условиям задачи: количество каждой буквы в слове не должно превышать количество этой буквы
в отфильтрованной строке.
''''
''''
Шаг №7. - Сортировка слов
''''
sorted_words = sorted(filtered_words, key=lambda x: (len(x), x))
''''
Сортируем отфильтрованные слова по длине и лексикографическому порядку.
''''
''''
Шаг №8. - Вывод количества слов
''''
print(len(sorted_words))
''''
Выводим количество отсортированных слов.
''''
''''
Шаг №9. - Вывод отсортированных слов
''''
for w in sorted_words:
    print(w)
''''
Выводим сами слова в отсортированном порядке.
''''
''''
Шаг №10. - Пример использования функции
''''
# Пример использования
input_str = "k98.ok"
generate_words(input_str)
''''
Вызываем функцию с примером входных данных.
''''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Вариант №3. ↓ - подумал, можно ли немного упростить код.
'''
import re
from itertools import permutations

def generate_words(input_str):
    # Фильтрация символов, оставляем только буквы
    filtered_str = re.sub(r'[^a-zA-Z]', '', input_str)

    # Генерация перестановок и фильтрация слов по правилам задачи
    words = {word for r in range(1, len(filtered_str) + 1)
             for perm in permutations(filtered_str, r)
             if (word := ''.join(perm)) and all(word.count(char) <= filtered_str.count(char) for char in set(word))}

    # Сортировка слов по длине и лексикографическому порядку
    sorted_words = sorted(words, key=lambda x: (len(x), x))

    # Вывод количества слов
    print(len(sorted_words))

    # Вывод отсортированных слов
    for w in sorted_words:
        print(w)

# Пример использования
input_str = "k98.ok"
generate_words(input_str)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Изменения:

1. Используется множество (set) для автоматического устранения дубликатов слов.
2. Вложенные циклы объединены в одну генераторную выражение.
3. Использовано выражение с условием (if (word := ''.join(perm))) для создания и фильтрации слов в одном выражении.
4. Убраны лишние переменные и структуры данных, такие как filtered_words.
''''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Шаг №1. - Фильтрация символов
''''
filtered_str = re.sub(r'[^a-zA-Z]', '', input_str)
''''
Эта строка использует регулярное выражение, чтобы удалить все символы, кроме букв.
''''
''''
Шаг №2. - Генерация и фильтрация слов
''''
words = {word for r in range(1, len(filtered_str) + 1)
         for perm in permutations(filtered_str, r)
         if (word := ''.join(perm)) and all(word.count(char) <= filtered_str.count(char) for char in set(word))}
''''
Это генераторное выражение объединяет два цикла в один. Он генерирует все возможные перестановки букв 
заданной длины и фильтрует их с помощью условия if. 
Оператор := используется для создания переменной word внутри генератора.
''''
''''
Шаг №3. - Сортировка слов
''''
sorted_words = sorted(words, key=lambda x: (len(x), x))
''''
Слова сортируются по длине и лексикографическому порядку.
''''
''''
Шаг №4. - Вывод результатов
''''
print(len(sorted_words))
for w in sorted_words:
    print(w)
''''
Выводится количество слов и сами слова.
''''
''''
Итак:

В итоге, код создает множество уникальных слов, проходя по всем возможным перестановкам букв из входной строки, 
фильтрует их по заданным условиям, сортирует и выводит результаты. Использование генераторных выражений и 
функциональных возможностей Python делает код более компактным и выразительным.
''''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Вариант №4. ↓ - тернарник
'''
import re
from itertools import permutations


def generate_words(input_str):
    filtered_str = re.sub(r'[^a-zA-Z]', '', input_str)

    words = {word for r in range(1, len(filtered_str) + 1) for perm in permutations(filtered_str, r) if
             (word := ''.join(perm)) and all(word.count(char) <= filtered_str.count(char) for char in set(word))}

    sorted_words = sorted(words, key=lambda x: (len(x), x))

    print(len(sorted_words), *[w for w in sorted_words], sep='\n')


# Пример использования
input_str = "k98.ok"
generate_words(input_str)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Изменения:

Использован однострочный оператор для создания множества words.
Сокращен вывод результатов в одну строку с использованием sep='\n'.
''''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Шаг №1. - Фильтрация символов
''''
filtered_str = re.sub(r'[^a-zA-Z]', '', input_str)
''''
Эта строка использует регулярное выражение для удаления из input_str всех символов, кроме букв.
Результат сохраняется в переменной filtered_str.
''''
''''
Шаг №2. - Генерация и фильтрация слов
''''
words = {word for r in range(1, len(filtered_str) + 1)
         for perm in permutations(filtered_str, r)
         if (word := ''.join(perm)) and all(word.count(char) <= filtered_str.count(char) for char in set(word))}
''''
Это генераторное выражение создает множество (set) уникальных слов.
Оно проходит по всем возможным перестановкам букв заданной длины, используя вложенные циклы и фильтрует их,
применяя условие if. Используется оператор := для создания переменной word внутри выражения.
''''
''''
Шаг №3. - Сортировка слов
''''
sorted_words = sorted(words, key=lambda x: (len(x), x))
''''
Слова сортируются по длине и лексикографическому порядку с использованием функции sorted.
Ключ сортировки задается лямбда-функцией, которая учитывает и сначала сортирует по длине, а затем по самим словам.
''''
''''
Шаг №4. - Вывод результатов
''''
print(len(sorted_words), *[w for w in sorted_words], sep='\n')
''''
Выводится количество слов и сами слова. Здесь используется распаковка списков * для передачи элементов списка
в качестве аргументов функции print, а sep='\n' устанавливает разделитель между словами как новую строку.
''''
''''
Итак, что в ИТОГЕ:

В итоге, код преобразует входную строку, генерирует и фильтрует все возможные слова, сортирует их и выводит результаты.
Использование множества (set), генераторных выражений и компактных структур кода делает
его более читаемым и эффективным.
''''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
                                    ↓ЭТО возможно не те РЕШЕНИЯ которые необходимы↓
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Вариант №1. ↓ 
'''
from itertools import permutations

def generate_words(sequence):
    unique_chars = set(sequence)
    result_words = set()

    for length in range(1, len(sequence) + 1):
        for perm in permutations(sequence, length):
            word = ''.join(perm)
            if set(word) <= unique_chars:
                result_words.add(word)

    result_words = sorted(result_words, key=lambda x: (len(x), x))

    return result_words

# Пример использования
input_sequence = "k98.ok"
result = generate_words(input_sequence)

# Выводим количество слов и сами слова
print(len(result))
for word in result:
    print(word)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Шаг №1. - Импорт модуля permutations из itertools.
''''
from itertools import permutations
'''
Здесь мы импортируем функцию permutations,
которая будет использоваться для создания всех возможных перестановок символов.
'''
''''
Шаг №2. - Определение функции generate_words для создания слов из последовательности.
''''


def generate_words(sequence):
    unique_chars = set(sequence)
    result_words = set()

    for length in range(1, len(sequence) + 1):
        for perm in permutations(sequence, length):
            word = ''.join(perm)
            if set(word) <= unique_chars:
                result_words.add(word)

    result_words = sorted(result_words, key=lambda x: (len(x), x))

    return result_words
'''
В этой функции:

unique_chars - это множество уникальных символов в последовательности.
result_words - это множество для хранения уникальных слов.
Далее идет два вложенных цикла. Внешний цикл итерируется по длине слова от 1 до длины последовательности. 
Внутренний цикл создает все возможные перестановки символов данной длины.
word = ''.join(perm) - создаем слово, объединяя символы из текущей перестановки.
if set(word) <= unique_chars - проверяем, что все символы в слове не превосходят символы в исходной последовательности. 
Если условие выполняется, то добавляем это слово в result_words.
'''
''''
Шаг №3. - Пример использования кода.
''''
# Пример использования
input_sequence = "k98.ok"
result = generate_words(input_sequence)

# Выводим количество слов и сами слова
print(len(result))
for word in result:
    print(word)
'''
В этом примере:

input_sequence - это входная последовательность "k98.ok".
result - это результат работы функции generate_words для данной последовательности.
Затем выводится количество уникальных слов и сами слова.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Вариант №2. ↓ 
'''
from itertools import permutations

def generate_words(sequence):
    unique_chars = set(sequence)
    result_words = set()

    for length in range(1, len(sequence) + 1):
        for perm in permutations(sequence, length):
            word = ''.join(perm)
            if set(word) <= unique_chars:
                result_words.add(word)

    result_words = sorted(result_words, key=lambda x: (len(x), x))

    return result_words

def count_and_print_words(words):
    unique_words = set(words)
    print(len(unique_words))
    for word in sorted(unique_words, key=lambda x: (len(x), x)):
        print(word)

# Пример использования
input_sequence = "abracadabra"
result = generate_words(input_sequence)

# Выводим количество уникальных слов и сами слова
count_and_print_words(result)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Шаг №1. - Импорт модуля permutations из itertools.
''''
from itertools import permutations
'''
Этот шаг импортирует функцию permutations,
которая будет использоваться для создания всех возможных перестановок символов.
'''
''''
Шаг №2. - Определение функции generate_words для создания слов из последовательности.
''''
def generate_words(sequence):
    unique_chars = set(sequence)
    result_words = set()

    for length in range(1, len(sequence) + 1):
        for perm in permutations(sequence, length):
            word = ''.join(perm)
            if set(word) <= unique_chars:
                result_words.add(word)

    result_words = sorted(result_words, key=lambda x: (len(x), x))

    return result_words
'''
В этой функции:

unique_chars - это множество уникальных символов в исходной последовательности.
result_words - это множество для хранения уникальных слов.
Двойной цикл создает все возможные перестановки символов заданной длины,
где внешний цикл идет по длине слова от 1 до длины последовательности.
word = ''.join(perm) - создаем слово, объединяя символы из текущей перестановки.
if set(word) <= unique_chars - проверяем, что все символы в слове не превосходят символы в исходной последовательности.
Если условие выполняется, то добавляем это слово в result_words.
'''
''''
Шаг №3: Определение функции count_and_print_words для вывода уникальных слов.
''''
def count_and_print_words(words):
    unique_words = set(words)
    print(len(unique_words))
    for word in sorted(unique_words, key=lambda x: (len(x), x)):
        print(word)
'''
Эта функция:

unique_words - это множество уникальных слов из входного списка words.
Затем выводится количество уникальных слов и сами слова, сортированные по длине и лексикографически.
'''
''''
Шаг №4: Пример использования кода.
''''
# Пример использования
input_sequence = "abracadabra"
result = generate_words(input_sequence)

# Выводим количество уникальных слов и сами слова
count_and_print_words(result)
'''
Этот пример:

Задает входную последовательность "abracadabra".
Вызывает функцию generate_words для создания слов.
Затем вызывает функцию count_and_print_words для вывода уникальных слов.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Вариант №3. ↓ 
'''
from itertools import permutations

def generate_words(sequence):
    unique_chars = set(sequence)
    result_words = set()

    for length in range(1, len(sequence) + 1):
        for perm in permutations(sequence, length):
            word = ''.join(perm)
            if set(word) <= unique_chars:
                result_words.add(word)

    result_words = sorted(result_words, key=lambda x: (len(x), x))

    return result_words

def count_and_print_words(words):
    unique_words = set(words)
    print(len(unique_words))
    for word in sorted(unique_words, key=lambda x: (len(x), x)):
        print(word)

# Пример использования
input_sequence = "aA1bB2cC3"
result = generate_words(input_sequence)

# Выводим количество уникальных слов и сами слова
count_and_print_words(result)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Шаг №1. - Импорт модуля permutations из itertools.
''''
from itertools import permutations
'''
Этот шаг импортирует функцию permutations,
которая будет использоваться для создания всех возможных перестановок символов.
'''
''''
Шаг №2. - Определение функции generate_words для создания слов из последовательности.
''''
def generate_words(sequence):
    unique_chars = set(sequence)
    result_words = set()

    for length in range(1, len(sequence) + 1):
        for perm in permutations(sequence, length):
            word = ''.join(perm)
            if set(word) <= unique_chars:
                result_words.add(word)

    result_words = sorted(result_words, key=lambda x: (len(x), x))

    return result_words
'''
В этой функции:

unique_chars - это множество уникальных символов в исходной последовательности.
result_words - это множество для хранения уникальных слов.
Двойной цикл создает все возможные перестановки символов заданной длины,
где внешний цикл идет по длине слова от 1 до длины последовательности.
word = ''.join(perm) - создаем слово, объединяя символы из текущей перестановки.
if set(word) <= unique_chars - проверяем, что все символы в слове не превосходят символы в исходной последовательности.
Если условие выполняется, то добавляем это слово в result_words.
'''
''''
Шаг №3. - Определение функции count_and_print_words для вывода уникальных слов.
''''
def count_and_print_words(words):
    unique_words = set(words)
    print(len(unique_words))
    for word in sorted(unique_words, key=lambda x: (len(x), x)):
        print(word)
'''
Эта функция:

unique_words - это множество уникальных слов из входного списка words.
Затем выводится количество уникальных слов и сами слова, сортированные по длине и лексикографически.
'''
''''
Шаг №4. - Пример использования кода.
''''
# Пример использования
input_sequence = "aA1bB2cC3"
result = generate_words(input_sequence)

# Выводим количество уникальных слов и сами слова
count_and_print_words(result)
'''
Этот пример:

Задает входную последовательность "aA1bB2cC3".
Вызывает функцию generate_words для создания слов.
Затем вызывает функцию count_and_print_words для вывода уникальных слов.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Вариант №4. ↓ 
'''
from itertools import permutations
from enum import Enum

class CharacterType(Enum):
    UPPERCASE = 1
    LOWERCASE = 2
    DIGIT = 3

def get_character_type(char):
    if char.isupper():
        return CharacterType.UPPERCASE
    elif char.islower():
        return CharacterType.LOWERCASE
    elif char.isdigit():
        return CharacterType.DIGIT

def generate_words(sequence):
    unique_chars = set(sequence)
    result_words = set()

    for length in range(1, len(sequence) + 1):
        for perm in permutations(sequence, length):
            word = ''.join(perm)
            if set(map(get_character_type, word)) <= set(map(get_character_type, unique_chars)):
                result_words.add(word)

    result_words = sorted(result_words, key=lambda x: (len(x), x))

    return result_words

def count_and_print_words(words):
    unique_words = set(words)
    print(len(unique_words))
    for word in sorted(unique_words, key=lambda x: (len(x), x)):
        print(word)

# Пример использования
input_sequence = "aA1bB2cC3"
result = generate_words(input_sequence)

# Выводим количество уникальных слов и сами слова
count_and_print_words(result)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Шаг №1. - Импорт модулей permutations и Enum из библиотек itertools и enum.
''''
from itertools import permutations
from enum import Enum
'''
Этот шаг импортирует функцию permutations для создания всех
возможных перестановок и класс Enum для создания перечислений.
'''
''''
Шаг №2. - Определение перечисления CharacterType для типов символов.
''''
class CharacterType(Enum):
    UPPERCASE = 1
    LOWERCASE = 2
    DIGIT = 3
'''
Здесь создается перечисление CharacterType с тремя элементами: UPPERCASE, LOWERCASE и DIGIT,
которые представляют типы символов.
'''
''''
Шаг №3. - Определение функции get_character_type для определения типа символа.
''''
def get_character_type(char):
    if char.isupper():
        return CharacterType.UPPERCASE
    elif char.islower():
        return CharacterType.LOWERCASE
    elif char.isdigit():
        return CharacterType.DIGIT
'''
Эта функция принимает символ char и возвращает соответствующий тип символа на основе проверок на то,
является ли символ заглавной буквой, строчной буквой или цифрой.
'''
''''
Шаг №4. - Определение функции generate_words для создания слов из последовательности.
''''
def generate_words(sequence):
    unique_chars = set(sequence)
    result_words = set()

    for length in range(1, len(sequence) + 1):
        for perm in permutations(sequence, length):
            word = ''.join(perm)
            if set(map(get_character_type, word)) <= set(map(get_character_type, unique_chars)):
                result_words.add(word)

    result_words = sorted(result_words, key=lambda x: (len(x), x))

    return result_words
'''
В этой функции используется перечисление CharacterType для определения типов символов.
Функция создает слова, проверяя, что типы символов в слове не превосходят типы символов в исходной последовательности.
'''
''''
Шаг №5. - Определение функции count_and_print_words для вывода уникальных слов.
''''
def count_and_print_words(words):
    unique_words = set(words)
    print(len(unique_words))
    for word in sorted(unique_words, key=lambda x: (len(x), x)):
        print(word)
'''
Эта функция выводит количество уникальных слов и сами слова, сортированные по длине и лексикографически.
'''
''''
Шаг №6. - Пример использования кода.
''''
# Пример использования
input_sequence = "aA1bB2cC3"
result = generate_words(input_sequence)

# Выводим количество уникальных слов и сами слова
count_and_print_words(result)
'''
Этот пример:

Задает входную последовательность "aA1bB2cC3".
Вызывает функцию generate_words для создания слов.
Затем вызывает функцию count_and_print_words для вывода уникальных слов.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Вариант №5. ↓ 
'''
from itertools import permutations, combinations

def generate_words(sequence):
    words = set()

    # Генерируем комбинации и перестановки для каждой длины
    for length in range(1, len(sequence) + 1):
        # Перестановки букв
        perms = permutations(sequence, length)
        # Комбинации букв
        combs = combinations(sequence, length)

        # Объединяем перестановки и комбинации
        all_combinations = set(perms) | set(combs)

        # Формируем слова и добавляем их в множество
        words.update("".join(word) for word in all_combinations)

    # Сортируем слова по длине и возвращаем результат
    return sorted(words, key=lambda x: (len(x), x))

# Ввод данных
input_sequence = input("Введите последовательность символов: ")

# Генерация и вывод слов
result = generate_words(input_sequence)

# Выводим количество уникальных слов и сами слова
print(len(result))
for word in result:
    print(word)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Шаг №1. - Импорт необходимых библиотек.
''''
from itertools import permutations, combinations
'''
В этой строке кода импортируются две функции permutations и combinations из модуля itertools.
Эти функции используются для генерации перестановок и комбинаций элементов.
'''
''''
Шаг №2. - Определение функции generate_words(sequence)
''''
def generate_words(sequence):
    words = set()
'''
Эта функция принимает на вход последовательность sequence и возвращает список уникальных слов,
сгенерированных из всех возможных перестановок и комбинаций букв в этой последовательности. words - это множество,
которое будет содержать уникальные слова.
'''
''''
Шаг №3. - Генерация комбинаций и перестановок для каждой длины.
''''
for length in range(1, len(sequence) + 1):
    perms = permutations(sequence, length)
    combs = combinations(sequence, length)
'''
Цикл проходится по всем длинам, начиная от 1 и заканчивая длиной всей последовательности.
Для каждой длины генерируются перестановки (perms) и комбинации (combs) букв в последовательности.
'''
''''
Шаг №4. - Объединение перестановок и комбинаций.
''''
all_combinations = set(perms) | set(combs)
'''
Перестановки и комбинации объединяются в множество all_combinations с использованием оператора "|".
'''
''''
Шаг №5. - Формирование слов и добавление их в множество.
''''
words.update("".join(word) for word in all_combinations)
'''
Для каждой комбинации и перестановки букв создаются слова, объединяя буквы, и эти слова добавляются в множество words.
'''
''''
Шаг №6. - Сортировка слов по длине и возврат результата.
''''
return sorted(words, key=lambda x: (len(x), x))
'''
В конце функции все слова сортируются сначала по их длине, а затем лексикографически.
Отсортированный список слов возвращается.
'''
''''
Шаг №7. - Ввод данных.
''''
input_sequence = input("Введите последовательность символов: ")
'''
Пользователю предлагается ввести последовательность символов.
'''
''''
Шаг №8. - Генерация и вывод слов.
''''
result = generate_words(input_sequence)

print(len(result))
for word in result:
    print(word)
'''
Функция generate_words вызывается с введенной пользователем последовательностью, результат сохраняется в result.
Затем выводится количество уникальных слов и сами слова.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ # # ~ ~ ~ ~ # # ~ ~ ~ ~ # # ~ ~ ~ ~ # # ~ ~ ~ ~ # # ~ ~ ~ ~ # # ~ ~ ~ ~ # # ~ ~ ~ ~ # # ~ ~ ~ ~ # # ~ ~ ~ ~ #



