# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''  ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓
Дата выполнения ДОМАШНЕЙ РАБОТЫ: 29-30 - ДЕКАБРЯ 2023
''''  ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓
'''
Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
Дисциплина: Основы программирования на Python
'''
'''
Урок от 29.12.2023
Домашняя работа №21: ООП.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполните следующее задания:
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Создайте класс Roman (РимскоеЧисло), представляющий римское число и поддерживающий операции +, -, *, /.

При реализации класса:

операции +, -, *, / реализуйте как специальные методы
методы преобразования как статические методы.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Далее решение этого задания ↑
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Вариант №1.
'''
class Roman:
    roman_numerals = {
        'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10,
        'XL': 40, 'L': 50, 'XC': 90, 'C': 100,
        'CD': 400, 'D': 500, 'CM': 900, 'M': 1000
    }

    def __init__(self, value):
        self.roman_str = value.upper()

    @staticmethod
    def parse_input(input_str):
        try:
            return Roman.roman_numerals[input_str]
        except KeyError:
            raise ValueError(f"Invalid Roman numeral: {input_str}")

    @staticmethod
    def int_to_roman(num):
        if not 0 < num < 4000:
            raise ValueError("Number out of range (1 to 3999)")

        result = ''
        for roman, value in sorted(Roman.roman_numerals.items(), key=lambda x: x[1], reverse=True):
            while num >= value:
                result += roman
                num -= value
        return result

    def to_int(self):
        result = 0
        i = 0
        while i < len(self.roman_str):
            if i + 1 < len(self.roman_str) and self.roman_str[i:i + 2] in Roman.roman_numerals:
                result += Roman.roman_numerals[self.roman_str[i:i + 2]]
                i += 2
            else:
                result += Roman.roman_numerals[self.roman_str[i]]
                i += 1
        return result

    def __add__(self, other):
        if isinstance(other, Roman):
            result = self.to_int() + other.to_int()
            return Roman(self.int_to_roman(result))
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Roman):
            result = self.to_int() - other.to_int()
            return Roman(self.int_to_roman(result))
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, Roman):
            result = self.to_int() * other.to_int()
            return Roman(self.int_to_roman(result))
        else:
            raise TypeError("Unsupported operand type for *")

    def __truediv__(self, other):
        if isinstance(other, Roman):
            result = self.to_int() / other.to_int()
            return Roman(self.int_to_roman(int(result)))
        else:
            raise TypeError("Unsupported operand type for /")

    def __str__(self):
        return self.roman_str

# Пример использования
try:
    a = Roman("XII")
    b = Roman("V")

    result_add = a + b
    result_sub = a - b
    result_mul = a * b
    result_div = a / b

    print(f"{a} + {b} = {result_add}")
    print(f"{a} - {b} = {result_sub}")
    print(f"{a} * {b} = {result_mul}")
    print(f"{a} / {b} = {result_div}")

except ValueError as e:
    print(f"Ошибка: {e}")
except TypeError as e:
    print(f"Ошибка: {e}")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1. Инициализация класса Roman
'''
class Roman:
    roman_numerals = {
        'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10,
        'XL': 40, 'L': 50, 'XC': 90, 'C': 100,
        'CD': 400, 'D': 500, 'CM': 900, 'M': 1000
    }

    def __init__(self, value):
        self.roman_str = value.upper()
'''
Описание: 
Класс Roman представляет римское число. 
Внутри класса определен словарь roman_numerals, сопоставляющий римские цифры и их арабские эквиваленты. 
В конструкторе (__init__) инициализируется объект римского числа, приводя входное значение к верхнему регистру.
'''
'''
Шаг №2. Статический метод parse_input
'''
@staticmethod
def parse_input(input_str):
    try:
        return Roman.roman_numerals[input_str]
    except KeyError:
        raise ValueError(f"Invalid Roman numeral: {input_str}")
'''
Описание: 
Статический метод parse_input преобразует римское число в арабское число. 
Если входное значение не является допустимым римским числом, генерируется исключение ValueError.
'''
'''
Шаг №3. Статический метод int_to_roman
'''
@staticmethod
def int_to_roman(num):
    if not 0 < num < 4000:
        raise ValueError("Number out of range (1 to 3999)")

    result = ''
    for roman, value in sorted(Roman.roman_numerals.items(), key=lambda x: x[1], reverse=True):
        while num >= value:
            result += roman
            num -= value
    return result
'''
Описание: 
Статический метод int_to_roman преобразует арабское число в римское число. 
В случае, если число находится вне диапазона (1 до 3999), генерируется исключение ValueError.
'''
'''
Шаг №4. Метод to_int
'''
def to_int(self):
    result = 0
    i = 0
    while i < len(self.roman_str):
        if i + 1 < len(self.roman_str) and self.roman_str[i:i + 2] in Roman.roman_numerals:
            result += Roman.roman_numerals[self.roman_str[i:i + 2]]
            i += 2
        else:
            result += Roman.roman_numerals[self.roman_str[i]]
            i += 1
    return result
'''
Описание: 
Метод to_int преобразует римское число объекта в арабское число, используя словарь roman_numerals. 
Обрабатываются случаи, когда в римском числе есть комбинации (например, 'IV' для 4).
'''
'''
Шаг №5. Перегрузка операторов (__add__, __sub__, __mul__, __truediv__)
'''
def __add__(self, other):
    if isinstance(other, Roman):
        result = self.to_int() + other.to_int()
        return Roman(self.int_to_roman(result))
    else:
        raise TypeError("Unsupported operand type for +")


def __sub__(self, other):
    if isinstance(other, Roman):
        result = self.to_int() - other.to_int()
        return Roman(self.int_to_roman(result))
    else:
        raise TypeError("Unsupported operand type for -")


def __mul__(self, other):
    if isinstance(other, Roman):
        result = self.to_int() * other.to_int()
        return Roman(self.int_to_roman(result))
    else:
        raise TypeError("Unsupported operand type for *")


def __truediv__(self, other):
    if isinstance(other, Roman):
        result = self.to_int() / other.to_int()
        return Roman(self.int_to_roman(int(result)))
    else:
        raise TypeError("Unsupported operand type for /")
'''
Описание: 
Операторы сложения, вычитания, умножения и деления перегружены для класса Roman. 
Каждый из них проверяет тип второго операнда (other). Если он также является объектом класса Roman, 
выполняется соответствующая операция, а результат преобразуется обратно в римское число.
'''
'''
Шаг №6. Метод __str__
'''
def __str__(self):
    return self.roman_str
'''
Описание: Метод __str__ возвращает строковое представление объекта, используя римское число.
'''
'''
Пример использования
'''
# Пример использования
try:
    a = Roman("XII")
    b = Roman("V")

    result_add = a + b
    result_sub = a - b
    result_mul = a * b
    result_div = a / b

    print(f"{a} + {b} = {result_add}")
    print(f"{a} - {b} = {result_sub}")
    print(f"{a} * {b} = {result_mul}")
    print(f"{a} / {b} = {result_div}")

except ValueError as e:
    print(f"Ошибка: {e}")
except TypeError as e:
    print(f"Ошибка: {e}")
'''
Описание: 
Создаются два объекта римских чисел a и b. 
Затем выполняются операции сложения, вычитания, умножения и деления, и результаты выводятся на экран. 
Если возникают ошибки (например, некорректное римское число или несовместимый операнд), выводится соответствующее 
сообщение об ошибке.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Вариант №2.
'''
import roman

class Roman:
    word_to_number = {
        'one': 1, 'first': 1, 'two': 2, 'second': 2, 'three': 3, 'third': 3,
        # Добавьте остальные числа по мере необходимости
    }

    roman_numerals = {
        'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10,
        'XL': 40, 'L': 50, 'XC': 90, 'C': 100,
        'CD': 400, 'D': 500, 'CM': 900, 'M': 1000
    }

    def __init__(self, value):
        self.value = self.parse_input(value)

    @staticmethod
    def parse_input(input_str):
        if isinstance(input_str, int):
            return input_str
        input_str_lower = input_str.lower()
        if input_str_lower in Roman.word_to_number:
            return Roman.word_to_number[input_str_lower]
        else:
            try:
                # Попробуем преобразовать введенное значение как римскую цифру
                if input_str_upper := input_str.upper():
                    return roman.fromRoman(input_str_upper)
                else:
                    raise ValueError("Invalid input: empty string")
            except roman.InvalidRomanNumeralError:
                raise ValueError(f"Invalid input: {input_str}")

    def __add__(self, other):
        if isinstance(other, Roman):
            result = self.value + other.value
            return Roman(result)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Roman):
            result = self.value - other.value
            return Roman(result)
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, Roman):
            result = self.value * other.value
            return Roman(result)
        else:
            raise TypeError("Unsupported operand type for *")

    def __truediv__(self, other):
        if isinstance(other, Roman):
            result = self.value / other.value
            return Roman(int(result))
        else:
            raise TypeError("Unsupported operand type for /")

    def __str__(self):
        return str(self.value)

# Пример использования
try:
    a = Roman(input("Введите первое число: "))
    b = Roman(input("Введите второе число: "))

    result_add = a + b
    result_sub = a - b
    result_mul = a * b
    result_div = a / b

    print(f"{a} + {b} = {result_add}")
    print(f"{a} - {b} = {result_sub}")
    print(f"{a} * {b} = {result_mul}")
    print(f"{a} / {b} = {result_div}")

except ValueError as e:
    print(f"Ошибка: {e}")
except TypeError as e:
    print(f"Ошибка: {e}")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

X и I - I и X

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг 1: Импорт библиотеки roman
'''
import roman
'''
Этот шаг просто импортирует библиотеку roman, 
которая предоставляет функциональность для преобразования римских чисел в арабские и обратно.
'''
'''
Шаг 2: Определение класса Roman
'''
class Roman:
''''
Здесь создается класс Roman.
''''
'''
Шаг 3: Статические переменные класса
'''
word_to_number = {
    'one': 1, 'first': 1, 'two': 2, 'second': 2, 'three': 3, 'third': 3,
    # Добавьте остальные числа по мере необходимости
}

roman_numerals = {
    'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10,
    'XL': 40, 'L': 50, 'XC': 90, 'C': 100,
    'CD': 400, 'D': 500, 'CM': 900, 'M': 1000
}
'''
Здесь определены статические переменные класса, 
которые используются для преобразования словесных чисел в арабские (word_to_number) и для представления римских 
цифр в виде словаря (roman_numerals).
'''
'''
Шаг 4: Конструктор класса
'''
def __init__(self, value):
    self.value = self.parse_input(value)
'''
Конструктор класса принимает значение и вызывает метод parse_input, чтобы преобразовать его в числовое значение.
'''
'''
Шаг 5: Метод parse_input
'''


@staticmethod
def parse_input(input_str):
    if isinstance(input_str, int):
        return input_str
    input_str_lower = input_str.lower()
    if input_str_lower in Roman.word_to_number:
        return Roman.word_to_number[input_str_lower]
    else:
        try:
            # Попробуем преобразовать введенное значение как римскую цифру
            if input_str_upper := input_str.upper():
                return roman.fromRoman(input_str_upper)
            else:
                raise ValueError("Invalid input: empty string")
        except roman.InvalidRomanNumeralError:
            raise ValueError(f"Invalid input: {input_str}")
'''
Этот метод преобразует входные данные в числовое значение. Если входное значение является целым числом, оно 
возвращается как есть. 
В противном случае проверяется, является ли входное слово числом на языке (например, 'one') или римским числом.
'''
'''
Шаг 6-9: Перегрузка операторов
'''


def __add__(self, other):
    if isinstance(other, Roman):
        result = self.value + other.value
        return Roman(result)
    else:
        raise TypeError("Unsupported operand type for +")


def __sub__(self, other):
    if isinstance(other, Roman):
        result = self.value - other.value
        return Roman(result)
    else:
        raise TypeError("Unsupported operand type for -")


def __mul__(self, other):
    if isinstance(other, Roman):
        result = self.value * other.value
        return Roman(result)
    else:
        raise TypeError("Unsupported operand type for *")


def __truediv__(self, other):
    if isinstance(other, Roman):
        result = self.value / other.value
        return Roman(int(result))
    else:
        raise TypeError("Unsupported operand type for /")
'''
Эти методы перегружают операторы сложения, вычитания, умножения и деления для объектов класса Roman.
'''
'''
Шаг 10: Перегрузка метода __str__
'''
def __str__(self):
    return str(self.value)
'''
Этот метод перегружает метод __str__ и возвращает строковое представление числового значения.
'''
'''
Шаг 11-14: Пример использования
'''
# Пример использования
try:
    a = Roman(input("Введите первое число: "))
    b = Roman(input("Введите второе число: "))

    result_add = a + b
    result_sub = a - b
    result_mul = a * b
    result_div = a / b

    print(f"{a} + {b} = {result_add}")
    print(f"{a} - {b} = {result_sub}")
    print(f"{a} * {b} = {result_mul}")
    print(f"{a} / {b} = {result_div}")

except ValueError as e:
    print(f"Ошибка: {e}")
except TypeError as e:
    print(f"Ошибка: {e}")
'''
Здесь пользователю предлагается ввести два числа (либо римские, либо словесные),
а затем выполняются операции сложения, вычитания, умножения и деления с выводом результатов.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Вариант №3.
'''
import roman
import re

class Roman:
    MIN_ROMAN_NUMERAL = 1
    MAX_ROMAN_NUMERAL = 9999999999

    word_to_number = {
        'one': 1, 'first': 1, 'один': 1,
        'two': 2, 'second': 2, 'два': 2,
        'three': 3, 'third': 3, 'три': 3,
        'four': 4, 'четыре': 4,
        'five': 5, 'пять': 5,
        'six': 6, 'шесть': 6,
        'seven': 7, 'семь': 7,
        'eight': 8, 'восемь': 8,
        'nine': 9, 'девять': 9,
        'ten': 10, 'десять': 10,
        'eleven': 11, 'одиннадцать': 11,
        'twelve': 12, 'двенадцать': 12,
        'thirteen': 13, 'тринадцать': 13,
        'fourteen': 14, 'четырнадцать': 14,
        'fifteen': 15, 'пятнадцать': 15,
        'sixteen': 16, 'шестнадцать': 16,
        'seventeen': 17, 'семнадцать': 17,
        'eighteen': 18, 'восемнадцать': 18,
        'nineteen': 19, 'девятнадцать': 19,
        'twenty': 20, 'двадцать': 20,
        'thirty': 30, 'тридцать': 30,
        'forty': 40, 'сорок': 40,
        'fifty': 50, 'пятьдесят': 50,
        'sixty': 60, 'шестьдесят': 60,
        'seventy': 70, 'семьдесят': 70,
        'eighty': 80, 'восемьдесят': 80,
        'ninety': 90, 'девяносто': 90,
        'hundred': 100, 'сто': 100,
    }

    roman_numerals = {
        'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10,
        'XL': 40, 'L': 50, 'XC': 90, 'C': 100,
        'CD': 400, 'D': 500, 'CM': 900, 'M': 1000
    }

    def __init__(self, value):
        self.value = self.parse_input(value)

    @staticmethod
    def parse_input(input_str):
        if isinstance(input_str, int):
            return input_str

        input_str_lower = input_str.lower()  # Приводим к нижнему регистру
        input_str_normalized = re.sub(r'\s', '', input_str_lower)  # Удаляем пробелы

        if input_str_normalized in Roman.word_to_number:
            return Roman.word_to_number[input_str_normalized]
        else:
            try:
                return roman.fromRoman(input_str_normalized)
            except roman.InvalidRomanNumeralError:
                try:
                    return int(input_str_normalized)
                except ValueError:
                    raise ValueError(f"Invalid input: {input_str}")

    @staticmethod
    def int_to_roman(num):
        if not Roman.MIN_ROMAN_NUMERAL <= num <= Roman.MAX_ROMAN_NUMERAL:
            raise ValueError(f"Number out of range ({Roman.MIN_ROMAN_NUMERAL} to {Roman.MAX_ROMAN_NUMERAL})")

        result = ''
        for numeral, integer in sorted(Roman.roman_numerals.items(), key=lambda x: x[1], reverse=True):
            while num >= integer:
                result += numeral
                num -= integer

        return result

    def to_roman_string(self):
        result = ''
        remaining = self.value

        for numeral, integer in sorted(Roman.roman_numerals.items(), key=lambda x: x[1], reverse=True):
            while remaining >= integer:
                result += numeral
                remaining -= integer

        return result

    def to_word_number(self):
        for word, number in Roman.word_to_number.items():
            if number == self.value:
                return word.capitalize()
        return str(self.value)

    def __add__(self, other):
        if isinstance(other, Roman):
            result = self.value + other.value
            return Roman(result)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Roman):
            result = self.value - other.value
            return Roman(result)
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, Roman):
            result = self.value * other.value
            return Roman(result)
        else:
            raise TypeError("Unsupported operand type for *")

    def __truediv__(self, other):
        if isinstance(other, Roman):
            result = self.value / other.value
            return Roman(int(result))
        else:
            raise TypeError("Unsupported operand type for /")

    def __str__(self):
        if self.value in Roman.roman_numerals.values():
            return roman.toRoman(self.value)
        elif self.value in Roman.word_to_number.values():
            return Roman.int_to_roman(self.value)
        else:
            return str(self.value)

# Пример использования
try:
    a = Roman(input("Введите первое число: "))
    b = Roman(input("Введите второе число: "))

    result_add = a + b
    result_sub = a - b
    result_mul = a * b
    result_div = a / b

    print(f"Исходные числа: {a} и {b}")
    print(f"{a.to_roman_string()} + {b.to_roman_string()} = {result_add.to_roman_string()}")
    print(f"{a.to_roman_string()} - {b.to_roman_string()} = {result_sub.to_roman_string()}")
    print(f"{a.to_roman_string()} * {b.to_roman_string()} = {result_mul.to_roman_string()}")
    print(f"{a.to_roman_string()} / {b.to_roman_string()} = {result_div.to_roman_string()}")

except ValueError as e:
    print(f"Ошибка: {e}")
except TypeError as e:
    print(f"Ошибка: {e}")


# Желательно первое число писать больше 0 или 1. (т.е первое число должно быть больше второго числа)
# Пока только понимает (один, 1 и I)

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
1. Импорт библиотек:
'''
import roman
import re
'''
Импортируются библиотеки roman для работы с римскими числами и re для работы с регулярными выражениями.
'''
'''
2. Определение класса Roman:
'''
class Roman:
''''
Класс содержит атрибуты, методы и операторы для работы с римскими числами.
'''''
'''
3. Определение констант и словарей:
'''
MIN_ROMAN_NUMERAL = 1
MAX_ROMAN_NUMERAL = 9999999999
'''
Эти константы используются для ограничения диапазона арабских чисел, которые можно преобразовывать в римские.
'''
word_to_number = {...}
roman_numerals = {...}
'''
Словари word_to_number и roman_numerals содержат соответствия слов и римских цифр арабским числам.
'''
'''
4. Метод __init__:
'''
def __init__(self, value):
    self.value = self.parse_input(value)
'''
Конструктор класса, который вызывает метод parse_input для преобразования входного значения.
'''
'''
5. Метод parse_input:
'''
@staticmethod
def parse_input(input_str):
    ...
'''
Метод для преобразования входного значения (строки, слова или числа) в арабское число.
'''
'''
6. Метод int_to_roman:
'''
@staticmethod
def int_to_roman(num):
    ...
'''
Метод для преобразования арабского числа в римское.
'''
'''
7. Метод to_roman_string:
'''
def to_roman_string(self):
    ...
'''
Метод для преобразования текущего значения в строку римского числа.
'''
'''
8. Метод to_word_number:
'''
def to_word_number(self):
    ...
'''
Метод для преобразования текущего значения в слово (например, "один").
'''
'''
9. Операторы арифметических операций:
'''
def __add__(self, other):
    ...
def __sub__(self, other):
    ...
def __mul__(self, other):
    ...
def __truediv__(self, other):
    ...
'''
Перегруженные операторы для выполнения арифметических операций.
'''
'''
10. Метод __str__:
'''
def __str__(self):
    ...
'''
Метод для преобразования текущего значения в строку.
'''
'''
11. Пример использования:
'''
try:
    a = Roman(input("Введите первое число: "))
    b = Roman(input("Введите второе число: "))
    ...
except ValueError as e:
    print(f"Ошибка: {e}")
except TypeError as e:
    print(f"Ошибка: {e}")
'''
Запрашивается ввод двух чисел и выполняются арифметические операции между ними, результаты выводятся на экран.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Вариант №4. - чуть чуть доработанный код.
'''
import roman
import re

class Roman:
    MIN_ROMAN_NUMERAL = 1
    MAX_ROMAN_NUMERAL = 9999999999

    word_to_number = {
        'one': 1, 'first': 1, 'один': 1,
        'two': 2, 'second': 2, 'два': 2,
        'three': 3, 'third': 3, 'три': 3,
        'four': 4, 'четыре': 4,
        'five': 5, 'пять': 5,
        'six': 6, 'шесть': 6,
        'seven': 7, 'семь': 7,
        'eight': 8, 'восемь': 8,
        'nine': 9, 'девять': 9,
        'ten': 10, 'десять': 10,
        'eleven': 11, 'одиннадцать': 11,
        'twelve': 12, 'двенадцать': 12,
        'thirteen': 13, 'тринадцать': 13,
        'fourteen': 14, 'четырнадцать': 14,
        'fifteen': 15, 'пятнадцать': 15,
        'sixteen': 16, 'шестнадцать': 16,
        'seventeen': 17, 'семнадцать': 17,
        'eighteen': 18, 'восемнадцать': 18,
        'nineteen': 19, 'девятнадцать': 19,
        'twenty': 20, 'двадцать': 20,
        'thirty': 30, 'тридцать': 30,
        'forty': 40, 'сорок': 40,
        'fifty': 50, 'пятьдесят': 50,
        'sixty': 60, 'шестьдесят': 60,
        'seventy': 70, 'семьдесят': 70,
        'eighty': 80, 'восемьдесят': 80,
        'ninety': 90, 'девяносто': 90,
        'hundred': 100, 'сто': 100,
    }

    roman_numerals = {
        'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10,
        'XL': 40, 'L': 50, 'XC': 90, 'C': 100,
        'CD': 400, 'D': 500, 'CM': 900, 'M': 1000
    }

    def __init__(self, value):
        self.value = self.parse_input(value)

    @staticmethod
    def parse_input(input_str):
        if isinstance(input_str, int):
            return input_str

        input_str_lower = input_str.lower()  # Приводим к нижнему регистру
        input_str_normalized = re.sub(r'\s', '', input_str_lower)  # Удаляем пробелы

        if input_str_normalized in Roman.word_to_number:
            return Roman.word_to_number[input_str_normalized]
        else:
            try:
                return roman.fromRoman(input_str_normalized)
            except roman.InvalidRomanNumeralError:
                try:
                    return int(input_str_normalized)
                except ValueError:
                    raise ValueError(f"Invalid input: {input_str}")

    @staticmethod
    def int_to_roman(num):
        if not Roman.MIN_ROMAN_NUMERAL <= num <= Roman.MAX_ROMAN_NUMERAL:
            raise ValueError(f"Number out of range ({Roman.MIN_ROMAN_NUMERAL} to {Roman.MAX_ROMAN_NUMERAL})")

        result = ''
        for numeral, integer in sorted(Roman.roman_numerals.items(), key=lambda x: x[1], reverse=True):
            while num >= integer:
                result += numeral
                num -= integer

        return result

    def to_roman_string(self):
        result = ''
        remaining = self.value

        for numeral, integer in sorted(Roman.roman_numerals.items(), key=lambda x: x[1], reverse=True):
            while remaining >= integer:
                result += numeral
                remaining -= integer

        return result

    def to_word_number(self):
        for word, number in Roman.word_to_number.items():
            if number == self.value:
                return word.capitalize()
        return str(self.value)

    def to_arabic_string(self):
        for word, number in Roman.word_to_number.items():
            if number == self.value:
                return f"{number} ({word}, {self.to_word_number()})"
        return str(self.value)

    def __add__(self, other):
        if isinstance(other, Roman):
            result = self.value + other.value
            return Roman(result)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Roman):
            result = self.value - other.value
            return Roman(result)
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, Roman):
            result = self.value * other.value
            return Roman(result)
        else:
            raise TypeError("Unsupported operand type for *")

    def __truediv__(self, other):
        if isinstance(other, Roman):
            result = self.value / other.value
            return Roman(int(result))
        else:
            raise TypeError("Unsupported operand type for /")

    def __str__(self):
        if self.value in Roman.roman_numerals.values():
            return roman.toRoman(self.value)
        elif self.value in Roman.word_to_number.values():
            return Roman.int_to_roman(self.value)
        else:
            return str(self.value)

# Пример использования
try:
    a = Roman(input("Введите первое число: "))
    b = Roman(input("Введите второе число: "))

    result_add = a + b
    result_sub = a - b
    result_mul = a * b
    result_div = a / b

    print("\nВспомогательная информация:")
    print("\nОтображение чисел в арабском виде:")
    print(f"Исходные числа: {a.to_arabic_string()} и {b.to_arabic_string()}")
    print(f"{a.to_arabic_string()} + {b.to_arabic_string()} = {result_add.to_arabic_string()}")
    print(f"{a.to_arabic_string()} - {b.to_arabic_string()} = {result_sub.to_arabic_string()}")
    print(f"{a.to_arabic_string()} * {b.to_arabic_string()} = {result_mul.to_arabic_string()}")
    print(f"{a.to_arabic_string()} / {b.to_arabic_string()} = {result_div.to_arabic_string()}")

    print("\nОтображение чисел в римском виде:")
    print(f"Исходные числа: {a} и {b}")
    print(f"{a.to_roman_string()} + {b.to_roman_string()} = {result_add.to_roman_string()}")
    print(f"{a.to_roman_string()} - {b.to_roman_string()} = {result_sub.to_roman_string()}")
    print(f"{a.to_roman_string()} * {b.to_roman_string()} = {result_mul.to_roman_string()}")
    print(f"{a.to_roman_string()} / {b.to_roman_string()} = {result_div.to_roman_string()}")

except ValueError as e:
    print(f"Ошибка: {e}")
except TypeError as e:
    print(f"Ошибка: {e}")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
1. Определение класса Roman:
'''
class Roman:
''''
2. Определение констант и словарей:
''''
MIN_ROMAN_NUMERAL = 1
MAX_ROMAN_NUMERAL = 9999999999
'''
Эти константы ограничивают диапазон арабских чисел, которые можно преобразовывать в римские.
'''
word_to_number = {...}
roman_numerals = {...}
'''
Словари word_to_number и roman_numerals содержат соответствия слов и римских цифр арабским числам.
'''
'''
3. Определение метода __init__:
'''
def __init__(self, value):
    self.value = self.parse_input(value)
'''
Конструктор класса, который вызывает метод parse_input для преобразования входного значения.
'''
'''
4. Определение метода parse_input:
'''
@staticmethod
def parse_input(input_str):
    ...
'''
Метод для преобразования входного значения (строки, слова или числа) в арабское число.
'''
'''
5. Определение метода int_to_roman:
'''
@staticmethod
def int_to_roman(num):
    ...
'''
Метод для преобразования арабского числа в римское.
'''
'''
6. Определение методов для представления числа в различных форматах:
'''
def to_roman_string(self):
    ...

def to_word_number(self):
    ...

def to_arabic_string(self):
    ...
'''
Эти методы возвращают строковое представление числа в римском, словесном и арабском виде соответственно.
'''
'''
7. Определение перегруженных операторов арифметических операций:
'''
def __add__(self, other):
    ...

def __sub__(self, other):
    ...

def __mul__(self, other):
    ...

def __truediv__(self, other):
    ...
'''
Перегруженные операторы для выполнения арифметических операций между объектами класса.
'''
'''
8. Определение метода __str__:
'''
def __str__(self):
    ...
'''
Метод для преобразования текущего значения в строку.
'''
'''
9. Пример использования:
'''
try:
    a = Roman(input("Введите первое число: "))
    b = Roman(input("Введите второе число: "))

    result_add = a + b
    result_sub = a - b
    result_mul = a * b
    result_div = a / b

    print("\nВспомогательная информация:")
    print("\nОтображение чисел в арабском виде:")
    print(f"Исходные числа: {a.to_arabic_string()} и {b.to_arabic_string()}")
    print(f"{a.to_arabic_string()} + {b.to_arabic_string()} = {result_add.to_arabic_string()}")
    print(f"{a.to_arabic_string()} - {b.to_arabic_string()} = {result_sub.to_arabic_string()}")
    print(f"{a.to_arabic_string()} * {b.to_arabic_string()} = {result_mul.to_arabic_string()}")
    print(f"{a.to_arabic_string()} / {b.to_arabic_string()} = {result_div.to_arabic_string()}")

    print("\nОтображение чисел в римском виде:")
    print(f"Исходные числа: {a} и {b}")
    print(f"{a.to_roman_string()} + {b.to_roman_string()} = {result_add.to_roman_string()}")
    print(f"{a.to_roman_string()} - {b.to_roman_string()} = {result_sub.to_roman_string()}")
    print(f"{a.to_roman_string()} * {b.to_roman_string()} = {result_mul.to_roman_string()}")
    print(f"{a.to_roman_string()} / {b.to_roman_string()} = {result_div.to_roman_string()}")

except ValueError as e:
    print(f"Ошибка: {e}")
except TypeError as e:
    print(f"Ошибка: {e}")
'''
Пример использования класса Roman, включающий ввод пользователем двух чисел и выполнение арифметических операций,
а также вывод результата в различных форматах.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #