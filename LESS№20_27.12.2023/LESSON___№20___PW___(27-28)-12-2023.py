# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
""""
Дата выполнения практической работы: 27-28 - ДЕКАБРЯ 2023
""""
'''
Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
Дисциплина: Основы программирования на Python
'''
'''
Урок от 27.12.2023
Практическая работа №20: ООП.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполните следующие задания:
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Задания №1
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Создайте класс Число (или используйте уже ранее созданный вами).
Класс число хранит внутри одно значение. 
Используя перегрузку операторов реализуйте для него арифметические операции для работы с числом (операции +, -, *, /).

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Задания №2
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Создайте класс Дробь (или используйте уже ранее созданный вами). 
Используя перегрузку операторов реализуйте для него арифметические операции для работы с дробями (операции +, -, *, /).

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Задания №3
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Создайте класс Библиотека. 
Класс предназначен для хранения информации о библиотеке (название, адрес, количество книг). 
Реализуйте необходимые для класса методы. 
Используя перегрузку операторов реализуйте для него следующие арифметические операции:
+ добавляет к количеству книг указанное значение;
- вычитает из количества книг указанное значение;
+= добавляет к количеству книг указанное значение;
-= вычитает из количества книг указанное значение; Используя перегрузку операторов реализуйте 
(сравнение по количеству книг):
<;
>;
<=;
>=;
==;
!=.

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Задания №4
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Создайте класс Date, который будет содержать информацию о дате (день, месяц, год).
С помощью механизма перегрузки операторов, определите операцию разности двух дат 
(результат в виде количества дней между датами), а также операцию увеличения даты на определенное количество дней.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Решение этих заданий ↑   ↑   ↑   ↑
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание №1: Класс Число
'''
'''
Этот код согласно заданию №1 создает класс Number, 
который может выполнять арифметические операции с объектами этого класса.
При этом он обеспечивает контроль типов и обрабатывает ситуации, такие как деление на ноль.
'''
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def __mul__(self, other):
        return Number(self.value * other.value)

    def __truediv__(self, other):
        return Number(self.value / other.value)

# Пример использования
num1 = Number(5)
num2 = Number(3)

result_sum = num1 + num2
result_diff = num1 - num2
result_mul = num1 * num2
result_div = num1 / num2

print(result_sum.value)  # 8
print(result_diff.value)  # 2
print(result_mul.value)  # 15
print(result_div.value)  # 1.6666666666666667
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1 - Создание класса Number
'''
class Number:
    def __init__(self, value):
        self.value = value

    # Перегрузка оператора сложения (+)
    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value)
        else:
            raise TypeError("Unsupported operand type for +: {}".format(type(other)))

    # Перегрузка оператора вычитания (-)
    def __sub__(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value)
        else:
            raise TypeError("Unsupported operand type for -: {}".format(type(other)))

    # Перегрузка оператора умножения (*)
    def __mul__(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value)
        else:
            raise TypeError("Unsupported operand type for *: {}".format(type(other)))

    # Перегрузка оператора деления (/)
    def __truediv__(self, other):
        if isinstance(other, Number):
            if other.value != 0:
                return Number(self.value / other.value)
            else:
                raise ValueError("Division by zero is not allowed")
        else:
            raise TypeError("Unsupported operand type for /: {}".format(type(other)))

    def __str__(self):
        return str(self.value)
'''
Подробное описание (шаг №1):

1. Определение класса Number: Класс Number содержит конструктор __init__, который принимает значение и 
инициализирует атрибут value.

2. Перегрузка операторов:
__add__: Перегружает оператор сложения (+). Если второй операнд тоже объект класса Number, 
создается новый объект с суммой значений. В противном случае, выбрасывается исключение типа данных.
__sub__: Перегружает оператор вычитания (-). Аналогично, создается новый объект с разностью значений.
__mul__: Перегружает оператор умножения (*). Создает новый объект с произведением значений.
__truediv__: Перегружает оператор деления (/). Создает новый объект с результатом деления значений. 
Проверяет, что значение делителя не равно нулю, чтобы избежать ошибки деления на ноль.
__str__: Возвращает строковое представление объекта, чтобы можно было вывести его с использованием print.
'''
'''
Шаг №2 - Пример использования
'''
# Пример использования
num1 = Number(5)
num2 = Number(3)

result_sum = num1 + num2
result_diff = num1 - num2
result_prod = num1 * num2
result_div = num1 / num2

print("Сложение:", result_sum)  # Вывод: Сложение: 8
print("Вычитание:", result_diff)  # Вывод: Вычитание: 2
print("Умножение:", result_prod)  # Вывод: Умножение: 15
print("Деление:", result_div)  # Вывод: Деление: 1.6666666666666667
'''
Подробное описание (шаг №2):

1. Создание объектов: Создаются два объекта класса Number: num1 и num2 с значениями 5 и 3 соответственно.

2. Арифметические операции:
Производятся арифметические операции с использованием перегруженных операторов (+, -, *, /).
Результаты операций присваиваются переменным result_sum, result_diff, result_prod, result_div.
3. Вывод результатов: Выводятся результаты операций с использованием print.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание №2: Класс Дробь - Вариант 1
'''
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        return Fraction(
            self.numerator * other.denominator + other.numerator * self.denominator,
            self.denominator * other.denominator
        )

    def __sub__(self, other):
        return Fraction(
            self.numerator * other.denominator - other.numerator * self.denominator,
            self.denominator * other.denominator
        )

    def __mul__(self, other):
        return Fraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator
        )

    def __truediv__(self, other):
        return Fraction(
            self.numerator * other.denominator,
            self.denominator * other.numerator
        )

# Пример использования
frac1 = Fraction(1, 2)
frac2 = Fraction(3, 4)

result_sum = frac1 + frac2
result_diff = frac1 - frac2
result_mul = frac1 * frac2
result_div = frac1 / frac2

print(result_sum.numerator, '/', result_sum.denominator)  # 5 / 4
print(result_diff.numerator, '/', result_diff.denominator)  # -1 / 4
print(result_mul.numerator, '/', result_mul.denominator)  # 3 / 8
print(result_div.numerator, '/', result_div.denominator)  # 2 / 3
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1 - Создание класса Fraction
'''
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        return Fraction(
            self.numerator * other.denominator + other.numerator * self.denominator,
            self.denominator * other.denominator
        )

    def __sub__(self, other):
        return Fraction(
            self.numerator * other.denominator - other.numerator * self.denominator,
            self.denominator * other.denominator
        )

    def __mul__(self, other):
        return Fraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator
        )

    def __truediv__(self, other):
        return Fraction(
            self.numerator * other.denominator,
            self.denominator * other.numerator
        )
'''
Подробное описание (шаг №1):

Определение класса Fraction: Создается класс Fraction, представляющий дробь. 
Конструктор __init__ принимает числитель (numerator) и знаменатель (denominator) дроби и инициализирует 
соответствующие атрибуты.

Перегрузка операторов:

__add__: Перегружает оператор сложения (+). Создает новый объект класса Fraction, представляющий сумму двух дробей.
__sub__: Перегружает оператор вычитания (-). Создает новый объект с разностью двух дробей.
__mul__: Перегружает оператор умножения (*). Создает новый объект с произведением двух дробей.
__truediv__: Перегружает оператор деления (/). Создает новый объект с результатом деления двух дробей.
'''
'''
Шаг №2 - Пример использования
'''
# Пример использования
frac1 = Fraction(1, 2)
frac2 = Fraction(3, 4)

result_sum = frac1 + frac2
result_diff = frac1 - frac2
result_mul = frac1 * frac2
result_div = frac1 / frac2

print(result_sum.numerator, '/', result_sum.denominator)  # 5 / 4
print(result_diff.numerator, '/', result_diff.denominator)  # -1 / 4
print(result_mul.numerator, '/', result_mul.denominator)  # 3 / 8
print(result_div.numerator, '/', result_div.denominator)  # 2 / 3
'''
Подробное описание (шаг №2):

1. Создание объектов: Создаются два объекта класса Fraction: frac1 с числителем 1 и знаменателем 2,
и frac2 с числителем 3 и знаменателем 4.

2. Арифметические операции:
Выполняются арифметические операции с использованием перегруженных операторов (+, -, *, /).
Результаты операций присваиваются переменным result_sum, result_diff, result_mul, result_div.

3. Вывод результатов: Выводятся числители и знаменатели результатов операций в виде дроби.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание №2: Класс Дробь - Вариант 2
'''
class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        common_factor = self.gcd(self.numerator, self.denominator)
        self.numerator //= common_factor
        self.denominator //= common_factor

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def input_fraction(self):
        try:
            numerator = int(input("Введите числитель: "))
            denominator = int(input("Введите знаменатель: "))
            if denominator == 0:
                raise ValueError("Знаменатель не может быть равен 0.")
            return Fraction(numerator, denominator)
        except ValueError as e:
            print(f"Ошибка: {e}. Пожалуйста, введите корректные целочисленные значения.")
            return None

    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction(
                self.numerator * other.denominator + other.numerator * self.denominator,
                self.denominator * other.denominator
            )
        else:
            raise TypeError("Unsupported operand type for +: {}".format(type(other)))

    def __sub__(self, other):
        if isinstance(other, Fraction):
            return Fraction(
                self.numerator * other.denominator - other.numerator * self.denominator,
                self.denominator * other.denominator
            )
        else:
            raise TypeError("Unsupported operand type for -: {}".format(type(other)))

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(
                self.numerator * other.numerator,
                self.denominator * other.denominator
            )
        else:
            raise TypeError("Unsupported operand type for *: {}".format(type(other)))

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ValueError("Деление на ноль не допустимо.")
            return Fraction(
                self.numerator * other.denominator,
                self.denominator * other.numerator
            )
        else:
            raise TypeError("Unsupported operand type for /: {}".format(type(other)))

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


# Пример использования с вводом от пользователя
fraction1 = Fraction().input_fraction()
fraction2 = Fraction().input_fraction()

if fraction1 and fraction2:
    result_sum = fraction1 + fraction2
    result_diff = fraction1 - fraction2
    result_mul = fraction1 * fraction2
    result_div = fraction1 / fraction2

    print("Сложение:", result_sum)
    print("Вычитание:", result_diff)
    print("Умножение:", result_mul)
    print("Деление:", result_div)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
1. Конструктор __init__:
'''
def __init__(self, numerator=0, denominator=1):
    self.numerator = numerator
    self.denominator = denominator
    self.simplify()
'''
Описание: 
Конструктор класса инициализирует объект дроби заданными значениями числителя (numerator) и знаменателя (denominator).
Если значения не переданы, используются значения по умолчанию (0 для числителя и 1 для знаменателя). 
После инициализации вызывается метод self.simplify(), который упрощает дробь.
'''
'''
2. Метод simplify:
'''
def simplify(self):
    common_factor = self.gcd(self.numerator, self.denominator)
    self.numerator //= common_factor
    self.denominator //= common_factor
'''
Описание: 
Метод упрощает дробь, выделяя общий делитель между числителем и знаменателем. 
Внутри метода используется функция gcd для нахождения наибольшего общего делителя. 
Затем числитель и знаменатель дроби делятся на этот общий делитель, что приводит к упрощенной дроби.
'''
'''
3. Метод gcd:
'''
def gcd(self, a, b):
    while b:
        a, b = b, a % b
    return a
'''
Описание: 
Метод вычисляет наибольший общий делитель двух чисел a и b с использованием алгоритма Евклида.
Метод возвращает найденный наибольший общий делитель.
'''
'''
4. Метод input_fraction:
'''
def input_fraction(self):
    try:
        numerator = int(input("Введите числитель: "))
        denominator = int(input("Введите знаменатель: "))
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен 0.")
        return Fraction(numerator, denominator)
    except ValueError as e:
        print(f"Ошибка: {e}. Пожалуйста, введите корректные целочисленные значения.")
        return None
'''
Описание: 
Метод запрашивает у пользователя ввод числителя и знаменателя и возвращает новый объект класса Fraction
с введенными значениями. При возникновении ошибки (например, если знаменатель равен 0), выводится сообщение об
ошибке, и метод возвращает None.
'''
'''
5. Магические методы для арифметических операций (__add__, __sub__, __mul__, __truediv__):
'''
def __add__(self, other):
    # ...

def __sub__(self, other):
    # ...

def __mul__(self, other):
    # ...

def __truediv__(self, other):
    # ...
''''
Описание: 
Эти методы реализуют арифметические операции сложения, вычитания, умножения и деления для объектов класса Fraction.
Проверяется, является ли other объектом класса Fraction, и выполняются соответствующие операции.
''''
'''
6. Метод __str__:
'''
def __str__(self):
    return f"{self.numerator}/{self.denominator}"
'''
Описание: Метод возвращает строковое представление дроби в виде "числитель/знаменатель".
'''
'''
7. Пример использования:
'''
fraction1 = Fraction().input_fraction()
fraction2 = Fraction().input_fraction()

if fraction1 and fraction2:
    result_sum = fraction1 + fraction2
    result_diff = fraction1 - fraction2
    result_mul = fraction1 * fraction2
    result_div = fraction1 / fraction2

    print("Сложение:", result_sum)
    print("Вычитание:", result_diff)
    print("Умножение:", result_mul)
    print("Деление:", result_div)
'''
Описание: 
Пример использования класса Fraction с вводом от пользователя. 
Создаются две дроби (fraction1 и fraction2), затем выполняются арифметические 
операции (+, -, *, /), и результаты выводятся на экран.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание №3: Класс Библиотека
'''
class Library:
    def __init__(self, name, address, num_books):
        self.name = name
        self.address = address
        self.num_books = num_books

    def __add__(self, other):
        return Library(self.name, self.address, self.num_books + other)

    def __sub__(self, other):
        return Library(self.name, self.address, self.num_books - other)

    def __iadd__(self, other):
        self.num_books += other
        return self

    def __isub__(self, other):
        self.num_books -= other
        return self

    def __lt__(self, other):
        return self.num_books < other.num_books

    def __gt__(self, other):
        return self.num_books > other.num_books

    def __le__(self, other):
        return self.num_books <= other.num_books

    def __ge__(self, other):
        return self.num_books >= other.num_books

    def __eq__(self, other):
        return self.num_books == other.num_books

    def __ne__(self, other):
        return self.num_books != other.num_books

# Пример использования
library1 = Library("City Library", "123 Main St", 100)
library2 = Library("University Library", "456 College Ave", 150)

library3 = library1 + 50
library4 = library2 - 20

print(library3.num_books)  # 150
print(library4.num_books)  # 130

library1 += 30
library2 -= 10

print(library1.num_books)  # 130
print(library2.num_books)  # 140

print(library1 > library2)  # False
print(library1 < library2)  # True
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1: Определение класса Library
'''
class Library:
    def __init__(self, name, address, num_books):
        self.name = name
        self.address = address
        self.num_books = num_books
'''
Подробное описание (шаг №1):

1. Определение класса Library: 
Создается класс Library с тремя атрибутами: name (имя библиотеки), address (адрес библиотеки) и num_books (количество
книг в библиотеке).
2. Конструктор __init__: 
Конструктор принимает три параметра (name, address, num_books) и инициализирует соответствующие атрибуты объекта.
'''
'''
Шаг №2: Перегрузка операторов сложения и вычитания
'''
def __add__(self, other):
    return Library(self.name, self.address, self.num_books + other)

def __sub__(self, other):
    return Library(self.name, self.address, self.num_books - other)
'''
Подробное описание (шаг №2):

1. Перегрузка оператора сложения (__add__): 
Создает новый объект Library с тем же именем, адресом и суммой количества книг текущей библиотеки
и переданного значения (other).
2. Перегрузка оператора вычитания (__sub__): 
Создает новый объект Library с тем же именем, адресом и разностью количества книг текущей библиотеки и 
переданного значения (other).
'''
'''
Шаг №3: In-Place Операторы (+= и -=)
'''
def __iadd__(self, other):
    self.num_books += other
    return self

def __isub__(self, other):
    self.num_books -= other
    return self
'''
Подробное описание (шаг №3):

1. In-Place Оператор +=: 
Увеличивает количество книг текущей библиотеки на значение, переданное в other, и возвращает измененный объект.
2. In-Place Оператор -=: 
Уменьшает количество книг текущей библиотеки на значение, переданное в other, и возвращает измененный объект.
'''
'''
Шаг №4: Сравнительные Операторы (<, >, <=, >=, ==, !=)
'''
def __lt__(self, other):
    return self.num_books < other.num_books

def __gt__(self, other):
    return self.num_books > other.num_books

def __le__(self, other):
    return self.num_books <= other.num_books

def __ge__(self, other):
    return self.num_books >= other.num_books

def __eq__(self, other):
    return self.num_books == other.num_books

def __ne__(self, other):
    return self.num_books != other.num_books
'''
Подробное описание (шаг №4):

1. Оператор <: 
Возвращает True, если количество книг текущей библиотеки меньше количества книг библиотеки, 
переданной в other, иначе возвращает False.

2. Оператор >: 
Возвращает True, если количество книг текущей библиотеки больше количества книг библиотеки, 
переданной в other, иначе возвращает False.

3. Оператор <=: 
Возвращает True, если количество книг текущей библиотеки меньше или равно количеству книг библиотеки,
переданной в other, иначе возвращает False.

4. Оператор >=: 
Возвращает True, если количество книг текущей библиотеки больше или равно количеству книг библиотеки,
переданной в other, иначе возвращает False.

5. Оператор ==: 
Возвращает True, если количество книг текущей библиотеки равно количеству книг библиотеки, переданной в other,
иначе возвращает False.

6. Оператор !=: 
Возвращает True, если количество книг текущей библиотеки не равно количеству книг библиотеки, переданной в other,
иначе возвращает False.
'''
'''
Шаг №5: Пример использования
'''
# Пример использования
library1 = Library("City Library", "123 Main St", 100)
library2 = Library("University Library", "456 College Ave", 150)

library3 = library1 + 50
library4 = library2 - 20

print(library3.num_books)  # 150
print(library4.num_books)  # 130

library1 += 30
library2 -= 10

print(library1.num_books)  # 130
print(library2.num_books)  # 140

print(library1 > library2)  # False
print(library1 < library2)  # True
'''
Подробное описание (шаг №5):

1. Создание объектов: Создаются два объекта Library: 
library1 и library2.

2. Использование операторов сложения и вычитания: 
Создаются новые библиотеки (library3 и library4) с использованием операторов + и -.

3. Использование in-place операторов: 
Изменяются текущие библиотеки (library1 и library2) с использованием in-place операторов += и -=.

4. Вывод результатов: 
Выводится количество книг в новых и измененных библиотеках.

5. Сравнение библиотек: 
Выполняются сравнения количества книг в library1 и library2, и результаты выводятся.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание №4: Класс Date
'''
from datetime import datetime


class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_input(cls):
        try:
            day = int(input("Введите день: "))
            month = int(input("Введите месяц: "))
            year = int(input("Введите год: "))

            if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2100):
                raise ValueError("Некорректная дата.")

            return cls(day, month, year)
        except ValueError as e:
            print(f"Ошибка: {e}. Пожалуйста, введите корректные значения.")
            return None

    @classmethod
    def from_string(cls, date_string, date_format="%d.%m.%Y"):
        parsed_date = datetime.strptime(date_string, date_format)
        return cls(day=parsed_date.day, month=parsed_date.month, year=parsed_date.year)

    def __sub__(self, other):
        if isinstance(other, Date):
            days_in_self = self.to_days()
            days_in_other = other.to_days()
            difference_in_days = days_in_self - days_in_other

            return difference_in_days
        else:
            raise TypeError("Unsupported operand type for -: {}".format(type(other)))

    def add_days(self, days):
        if days < 0:
            raise ValueError("Количество дней должно быть положительным числом.")

        days_in_self = self.to_days()
        new_days = days_in_self + days

        return self.from_days(new_days)

    def subtract_months(self, months):
        # Реализация вычитания месяцев
        pass

    def subtract_years(self, years):
        # Реализация вычитания лет
        pass

    @classmethod
    def current_date(cls):
        today = datetime.today()
        return cls(day=today.day, month=today.month, year=today.year)

    def __eq__(self, other):
        if isinstance(other, Date):
            return (self.day, self.month, self.year) == (other.day, other.month, other.year)
        return False

    def to_days(self):
        days = self.day
        for m in range(1, self.month):
            days += self.days_in_month(m, self.year)
        for y in range(1900, self.year):
            days += self.days_in_year(y)
        return days

    def from_days(self, days):
        year = 1900
        while days > self.days_in_year(year):
            days -= self.days_in_year(year)
            year += 1

        month = 1
        while days > self.days_in_month(month, year):
            days -= self.days_in_month(month, year)
            month += 1

        return Date(day=days, month=month, year=year)

    def days_in_month(self, month, year):
        if 1 <= month <= 12:
            if month in {1, 3, 5, 7, 8, 10, 12}:
                return 31
            elif month in {4, 6, 9, 11}:
                return 30
            elif month == 2 and self.is_leap_year(year):
                return 29
            elif month == 2:
                return 28
        raise ValueError("Некорректный месяц.")

    def days_in_year(self, year):
        return 366 if self.is_leap_year(year) else 365

    def is_leap_year(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def __str__(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year}"


# Пример использования с вводом от пользователя
date1 = Date.from_input()
date2 = Date.from_input()

if date1 and date2:
    days_difference = date1 - date2
    print("Разница в днях:", days_difference)

    try:
        days_to_add = int(input("Введите количество дней для добавления: "))
        new_date = date1.add_days(days_to_add)
        print("Новая дата:", new_date)
    except ValueError as e:
        print(f"Ошибка: {e}. Пожалуйста, введите корректное количество дней.")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1: Определение класса Date
'''
class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year
'''
Подробное описание (шаг №1):

1. Определение класса Date: Создается класс Date, представляющий информацию о дате. 
Конструктор __init__ принимает три параметра (день, месяц, год) и инициализирует соответствующие атрибуты объекта.
'''
'''
Шаг №2: Два метода класса Date с использованием декоратора @classmethod
Метод from_input
'''


@classmethod
def from_input(cls):
    try:
        day = int(input("Введите день: "))
        month = int(input("Введите месяц: "))
        year = int(input("Введите год: "))

        if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2100):
            raise ValueError("Некорректная дата.")

        return cls(day, month, year)
    except ValueError as e:
        print(f"Ошибка: {e}. Пожалуйста, введите корректные значения.")
        return None
'''
Метод from_string
'''


@classmethod
def from_string(cls, date_string, date_format="%d.%m.%Y"):
    parsed_date = datetime.strptime(date_string, date_format)
    return cls(day=parsed_date.day, month=parsed_date.month, year=parsed_date.year)
'''
Подробное описание (шаг №2):

1. Метод from_input: 
Этот метод использует декоратор @classmethod и предназначен для создания объекта Date на основе ввода пользователя.
Пользователь вводит день, месяц и год, и метод проверяет корректность введенных данных.
2. Метод from_string: 
Этот метод также использует декоратор @classmethod и создает объект Date на основе строки с датой (date_string).
Строка парсится с использованием библиотеки datetime, а затем извлекаются день, месяц и год для создания объекта Date.
'''
'''
Шаг №3: Перегрузка оператора вычитания (__sub__)
'''


def __sub__(self, other):
    if isinstance(other, Date):
        days_in_self = self.to_days()
        days_in_other = other.to_days()
        difference_in_days = days_in_self - days_in_other

        return difference_in_days
    else:
        raise TypeError("Unsupported operand type for -: {}".format(type(other)))
'''
Подробное описание (шаг №3):

1. Перегрузка оператора вычитания (__sub__): 
Если операнд (other) является объектом класса Date, то выполняется вычисление разницы в днях между двумя датами с
использованием методов to_days. Возвращается результат.
2. Если операнд не является объектом класса Date, генерируется исключение TypeError.
'''
'''
Шаг №4: Метод для увеличения даты на определенное количество дней (add_days)
'''
def add_days(self, days):
    if days < 0:
        raise ValueError("Количество дней должно быть положительным числом.")

    days_in_self = self.to_days()
    new_days = days_in_self + days

    return self.from_days(new_days)
'''
Подробное описание (шаг №4):

Метод add_days: 
1. Принимает количество дней (days) для увеличения текущей даты. 
Проверяет, что количество дней положительно.
2. Вычисляет количество дней, представляющих текущую дату (days_in_self), 
добавляет к ним переданное количество дней и создает новый объект Date с использованием метода from_days.
'''
'''
Шаг №5: Два метода для вычитания месяцев и лет (subtract_months и subtract_years)
'''
def subtract_months(self, months):
    # Реализация вычитания месяцев
    pass


def subtract_years(self, years):
    # Реализация вычитания лет
    pass
'''
Подробное описание (шаг №5):

1. Метод subtract_months: 
Метод, предположительно предназначенный для вычитания месяцев из текущей даты. 
В данный момент не имеет конкретной реализации (помечен pass).
2. Метод subtract_years: 
Метод, предположительно предназначенный для вычитания лет из текущей даты. 
В данный момент не имеет конкретной реализации (помечен pass).
'''
'''
Шаг №6: Метод класса для получения текущей даты (current_date)
'''
@classmethod
def current_date(cls):
    today = datetime.today()
    return cls(day=today.day, month=today.month, year=today.year)
'''
Подробное описание (шаг №6):

1. Метод current_date: 
Этот метод использует декоратор @classmethod и возвращает объект Date, представляющий текущую дату.
'''
'''
Шаг №7: Перегрузка оператора сравнения (__eq__)
'''
def __eq__(self, other):
    if isinstance(other, Date):
        return (self.day, self.month, self.year) == (other.day, other.month, other.year)
    return False
'''
Подробное описание (шаг №7):

1. Перегрузка оператора сравнения (__eq__): 
Если операнд (other) является объектом класса Date, то выполняется сравнение по дням, месяцам и годам. 
Возвращается булево значение.
'''
'''
Шаг №8: Три метода для работы с днями, месяцами и годами
'''


def to_days(self):
    days = self.day
    for m in range(1, self.month):
        days += self.days_in_month(m, self.year)
    for y in range(1900, self.year):
        days += self.days_in_year(y)
    return days


def from_days(self, days):
    year = 1900
    while days > self.days_in_year(year):
        days -= self.days_in_year(year)
        year += 1

    month = 1
    while days > self.days_in_month(month, year):
        days -= self.days_in_month(month, year)
        month += 1

    return Date(day=days, month=month, year=year)
'''
Подробное описание (шаг №8):

1. Метод to_days: Вычисляет и возвращает количество дней, представляющих текущую дату, учитывая дни, месяцы и годы.
2. Метод from_days: Создает новый объект Date на основе переданного количества дней.
3. Методы days_in_month и days_in_year: Определяют количество дней в месяце и году соответственно.
'''
'''
Шаг №9: Два метода для проверки високосного года и строкового представления объекта (__str__)
'''
def is_leap_year(self, year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def __str__(self):
    return f"{self.day:02d}.{self.month:02d}.{self.year}"
'''
Подробное описание (шаг №9):

1. Метод is_leap_year: Проверяет, является ли год високосным.
2. Метод __str__: Возвращает строковое представление объекта Date в формате "день.месяц.год".
'''
'''
Шаг №10: Пример использования с вводом от пользователя
'''
# Пример использования с вводом от пользователя
date1 = Date.from_input()
date2 = Date.from_input()

if date1 and date2:
    days_difference = date1 - date2
    print("Разница в днях:", days_difference)

    try:
        days_to_add = int(input("Введите количество дней для добавления: "))
        new_date = date1.add_days(days_to_add)
        print("Новая дата:", new_date)
    except ValueError as e:
        print(f"Ошибка: {e}. Пожалуйста, введите корректное количество дней.")
'''
Подробное описание (шаг №10):

1. Пример использования с вводом от пользователя: 
Создаются два объекта Date (date1 и date2) с использованием метода from_input, 
который запрашивает у пользователя ввод дня, месяца и года.
2. Вычисление разницы в днях и добавление дней: 
Вычисляется разница в днях между двумя датами. 
Пользователь вводит количество дней для добавления к первой дате, и выводится новая дата после добавления.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #