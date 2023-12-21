# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''  ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓
Дата выполнения практической работы: 20-21 - ДЕКАБРЯ 2023
''''  ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓
'''
Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
Дисциплина: Основы программирования на Python
'''
'''
Урок от 20.12.2023
Практическая работа №17: Объектно-ориентированное программирование
'''
'''
Выполните следующие задания:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Задание № 1

Реализуйте класс «Человек».
Необходимо хранить в полях класса: ФИО, дату рождения, контактный телефон, город, страну, домашний адрес.
Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Задание № 2

Создайте класс «Город». 
Необходимо хранить в полях класса: название города, название региона, название страны, 
количество жителей в городе, почтовый индекс города, телефонный код города. 
Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Задание № 3

Создайте класс «Страна».
Необходимо хранить в полях класса: название страны, название континента, количество жителей в стране,
телефонный код страны, название столицы, название городов страны. Реализуйте методы класса для ввода данных,
вывода данных, реализуйте доступ к отдельным полям через методы класса.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Задание № 4

Создайте класс «Дробь». 
Необходимо хранить в полях класса: числитель и знаменатель.
Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
Также создайте методы класса для выполнения арифметических операций (сложение, вычитание, умножение, деление).
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''ООП. Инкапсуляция'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполните следующие задания:
'''
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Задания №1
Разработайте класс с "полной инкапсуляцией", доступ к атрибутам которого и изменение данных реализуются через вызовы
методов. 
В объектно-ориентированном программировании принято имена методов для извлечения данных начинать со слова get (взять),
а имена методов, в которых свойствам присваиваются значения, – со слова set (установить). Например, get_field, set_field.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Задания №2
Написать программу, в которой есть главный класс Games со статическим полем Year, опишите конструктор присваивающий 
значение полю Year, также опишите метод getName, который возвращает имя игры. 
На основе главного класса путем наследования опишите четыре класса PCGames, PS4Games, XboxGames, MobileGames.
Добавьте каждому классу дополнительные поля и переопределите у всех классов метод getName.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Задания №3
Напишите программу с пустым классом Country. Опишите наследуемые от класса Country классы Russia, Canada, Germany.
Добавьте каждому классу поле population и опишите метод setPopulation и getPopulation.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Решения ВСЕХ заданий:

'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
На этот код я потратил более 7-ми часов.

Этот код демонстрирует использование основных концепций объектно-ориентированного программирования,
таких как инкапсуляция, наследование и полиморфизм. 
Каждый класс представляет сущность (человек, город, страна, дробь), и для каждого класса реализованы 
методы для ввода данных, отображения информации и, где необходимо, выполнения операций.


Инкапсуляция:

В каждом классе (Person, City, Country, Fraction) данные инкапсулированы в полях класса,
обозначенных символом подчеркивания (_). Методы классов используются для работы с этими полями, 
обеспечивая контроль доступа и защиту данных.


Наследование:

Классы City и Country наследуют от класса Person, что означает, что они могут использовать его методы и поля,
а также расширять или изменять их при необходимости.


Полиморфизм:

Методы input_data, display_data и другие в каждом классе имеют одинаковые имена,
что упрощает использование этих методов в единой структуре кода.
Методы add, subtract, multiply, divide в классе Fraction демонстрируют полиморфизм,
поскольку они реализуют одни и те же арифметические операции для разных типов данных.
'''
class Person:
    def __init__(self):
        self._full_name = ""
        self._birth_date = ""
        self._contact_phone = ""
        self._city = ""
        self._country = ""
        self._home_address = ""

    def input_data(self):
        try:
            self._full_name = input("Введите ФИО: ")
            self._birth_date = input("Введите дату рождения (в формате дд. мм. гг): ")
            self._contact_phone = input("Введите контактный телефон (в формате +7 (XXX) XXX-XX-XX): ")
            self._city = input("Введите город: ")
            self._country = input("Введите страну: ")
            self._home_address = input("Введите домашний адрес: ")
        except Exception as e:
            print(f"Ошибка ввода данных: {e}")

    def display_data(self):
        print("ФИО:", self._full_name)
        print("Дата рождения:", self._birth_date)
        print("Контактный телефон:", self._contact_phone)
        print("Город:", self._city)
        print("Страна:", self._country)
        print("Домашний адрес:", self._home_address)

    # Методы доступа к полям через методы класса
    def get_full_name(self):
        return self._full_name

    def set_full_name(self, value):
        try:
            if not value:
                raise ValueError("Поле 'ФИО' не может быть пустым.")
            self._full_name = value
        except ValueError as e:
            print(f"Ошибка установки значения: {e}")


class City:
    def __init__(self):
        self._city_name = ""
        self._region_name = ""
        self._country_name = ""
        self._population = 0
        self._postal_code = ""
        self._phone_code = ""

    def input_data(self):
        try:
            self._city_name = input("Введите название города: ")
            self._region_name = input("Введите название региона: ")
            self._country_name = input("Введите название страны: ")
            self._population = int(input("Введите количество жителей в городе: "))
            self._postal_code = input("Введите почтовый индекс города: ")
            self._phone_code = input("Введите телефонный код города: ")
        except ValueError as e:
            print(f"Ошибка ввода данных: {e}")

    def display_data(self):
        print("Название города:", self._city_name)
        print("Название региона:", self._region_name)
        print("Название страны:", self._country_name)
        print("Количество жителей:", self._population)
        print("Почтовый индекс:", self._postal_code)
        print("Телефонный код:", self._phone_code)

    # Методы доступа к полям через методы класса
    def get_city_name(self):
        return self._city_name

    def set_city_name(self, value):
        try:
            if not value:
                raise ValueError("Поле 'Название города' не может быть пустым.")
            self._city_name = value
        except ValueError as e:
            print(f"Ошибка установки значения: {e}")


class Country:
    def __init__(self):
        self._country_name = ""
        self._continent_name = ""
        self._population = 0
        self._phone_code = ""
        self._capital_name = ""
        self._cities = []

    def input_data(self):
        try:
            self._country_name = input("Введите название страны: ")
            self._continent_name = input("Введите название континента: ")
            self._population = int(input("Введите количество жителей в стране: "))
            self._phone_code = input("Введите телефонный код страны: ")
            self._capital_name = input("Введите название столицы: ")
            cities_input = input("Введите названия городов через запятую: ")
            self._cities = [city.strip() for city in cities_input.split(',')]
        except ValueError as e:
            print(f"Ошибка ввода данных: {e}")

    def display_data(self):
        print("Название страны:", self._country_name)
        print("Название континента:", self._continent_name)
        print("Количество жителей:", self._population)
        print("Телефонный код:", self._phone_code)
        print("Столица:", self._capital_name)
        print("Города:", ', '.join(self._cities))

    # Методы доступа к полям через методы класса
    def get_country_name(self):
        return self._country_name

    def set_country_name(self, value):
        try:
            if not value:
                raise ValueError("Поле 'Название страны' не может быть пустым.")
            self._country_name = value
        except ValueError as e:
            print(f"Ошибка установки значения: {e}")


class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self._numerator = numerator
        self._denominator = denominator

    def input_data(self):
        try:
            self._numerator = int(input("Введите числитель: "))
            self._denominator = int(input("Введите знаменатель (не равен 0): "))
            while self._denominator == 0:
                print("Знаменатель не может быть равен 0.")
                self._denominator = int(input("Введите знаменатель (не равен 0): "))
        except ValueError as e:
            print(f"Ошибка ввода данных: {e}")

    def display_data(self):
        print(f"{self._numerator}/{self._denominator}")

    # Методы доступа к полям через методы класса
    def get_numerator(self):
        return self._numerator

    def set_numerator(self, value):
        try:
            self._numerator = value
        except ValueError as e:
            print(f"Ошибка установки значения: {e}")

    def get_denominator(self):
        return self._denominator

    def set_denominator(self, value):
        try:
            if value != 0:
                self._denominator = value
            else:
                raise ValueError("Знаменатель не может быть равен 0.")
        except ValueError as e:
            print(f"Ошибка установки значения: {e}")

    # Арифметические операции
    def add(self, other):
        result = Fraction()
        result._numerator = self._numerator * other._denominator + other._numerator * self._denominator
        result._denominator = self._denominator * other._denominator
        return result

    def subtract(self, other):
        result = Fraction()
        result._numerator = self._numerator * other._denominator - other._numerator * self._denominator
        result._denominator = self._denominator * other._denominator
        return result

    def multiply(self, other):
        result = Fraction()
        result._numerator = self._numerator * other._numerator
        result._denominator = self._denominator * other._denominator
        return result

    def divide(self, other):
        result = Fraction()
        result._numerator = self._numerator * other._denominator
        result._denominator = self._denominator * other._numerator
        return result


# Пример использования:

# Создание объекта класса Person
person = Person()
person.input_data()
print("\nИнформация о человеке:")
person.display_data()

# Создание объекта класса City
city = City()
city.input_data()
print("\nИнформация о городе:")
city.display_data()

# Создание объекта класса Country
country = Country()
country.input_data()
print("\nИнформация о стране:")
country.display_data()

# Создание объекта класса Fraction
fraction1 = Fraction()
fraction1.input_data()
print("\nДробь 1:")
fraction1.display_data()

fraction2 = Fraction()
fraction2.input_data()
print("\nДробь 2:")
fraction2.display_data()

sum_result = fraction1.add(fraction2)
print("\nСложение:")
sum_result.display_data()

diff_result = fraction1.subtract(fraction2)
print("\nВычитание:")
diff_result.display_data()

prod_result = fraction1.multiply(fraction2)
print("\nУмножение:")
prod_result.display_data()

div_result = fraction1.divide(fraction2)
print("\nДеление:")
div_result.display_data()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг 1: Определение класса Person
'''
class Person:
    def __init__(self):
        self._full_name = ""
        self._birth_date = ""
        self._contact_phone = ""
        self._city = ""
        self._country = ""
        self._home_address = ""
'''
Описание:

Создается класс Person, представляющий человека.
В конструкторе (__init__) определены атрибуты (поля) класса с защищенным доступом (переменные с _ перед именем).
'''
'''
Шаг 2: Метод input_data класса Person
'''
def input_data(self):
    try:
        self._full_name = input("Введите ФИО: ")
        self._birth_date = input("Введите дату рождения (в формате дд. мм. гг): ")
        self._contact_phone = input("Введите контактный телефон (в формате +7 (XXX) XXX-XX-XX): ")
        self._city = input("Введите город: ")
        self._country = input("Введите страну: ")
        self._home_address = input("Введите домашний адрес: ")
    except ValueError as e:
        print(f"Ошибка ввода данных: {e}")
'''
Описание:

Метод input_data предназначен для ввода данных о человеке с клавиатуры.
Каждое поле заполняется пользователем, и ввод обернут в блок try-except для обработки возможных ошибок 
(например, некорректного ввода).
'''
'''
Шаг 3: Метод display_data класса Person
'''
def display_data(self):
    print("ФИО:", self._full_name)
    print("Дата рождения:", self._birth_date)
    print("Контактный телефон:", self._contact_phone)
    print("Город:", self._city)
    print("Страна:", self._country)
    print("Домашний адрес:", self._home_address)
'''
Описание:

Метод display_data выводит информацию о человеке в консоль.
Используется функция print для вывода каждого поля.
'''
'''
Шаг 4: Методы доступа get и set для поля full_name класса Person
'''
def get_full_name(self):
    return self._full_name

def set_full_name(self, value):
    try:
        if not value:
            raise ValueError("Поле 'ФИО' не может быть пустым.")
        self._full_name = value
    except ValueError as e:
        print(f"Ошибка установки значения: {e}")
'''
Описание:

Метод get_full_name возвращает значение поля _full_name.
Метод set_full_name устанавливает новое значение поля _full_name, предварительно проверяя,
чтобы значение не было пустым. В случае ошибки выводится сообщение.
'''
'''
Шаг 5: Пример использования класса Person
'''
# Создание объекта класса Person
person = Person()
person.input_data()
print("\nИнформация о человеке:")
person.display_data()
'''
Описание:

Создается объект класса Person с именем person.
Вызывается метод input_data для ввода данных с клавиатуры.
Затем вызывается метод display_data для вывода информации о человеке.
'''
'''
Шаг 6: Класс City и наследование от Person
'''
class City(Person):
    def __init__(self):
        super().__init__()
        self._city_name = ""
        self._region_name = ""
        self._country_name = ""
        self._population = 0
        self._postal_code = ""
        self._phone_code = ""
'''
Описание:

Создается класс City, который наследует атрибуты и методы класса Person.
В конструкторе вызывается конструктор родительского класса super().__init__() для инициализации унаследованных полей.
'''
'''
Шаг 7: Метод input_data для класса City
'''
def input_data(self):
    try:
        super().input_data()  # Вызов метода input_data родительского класса
        self._city_name = input("Введите название города: ")
        self._region_name = input("Введите название региона: ")
        self._country_name = input("Введите название страны: ")
        self._population = int(input("Введите количество жителей в городе: "))
        self._postal_code = input("Введите почтовый индекс города: ")
        self._phone_code = input("Введите телефонный код города: ")
    except ValueError as e:
        print(f"Ошибка ввода данных: {e}")
'''
Описание:

Метод input_data класса City расширяет метод input_data родительского класса Person, добавляя дополнительные поля.
'''
'''
Шаг 8: Метод display_data для класса City
'''
def display_data(self):
    super().display_data()  # Вызов метода display_data родительского класса
    print("Название города:", self._city_name)
    print("Название региона:", self._region_name)
    print("Название страны:", self._country_name)
    print("Количество жителей в городе:", self._population)
    print("Почтовый индекс города:", self._postal_code)
    print("Телефонный код города:", self._phone_code)
'''
Описание:

Метод display_data класса City также расширяет метод display_data родительского класса Person,
добавляя вывод дополнительных полей.
'''
'''
Шаг 9: Класс Country и наследование от City
'''
class Country(City):
    def __init__(self):
        super().__init__()
        self._continent_name = ""
        self._capital_name = ""
        self._cities_names = []
'''
Описание:

Создается класс Country, который наследует атрибуты и методы класса City.
В конструкторе вызывается конструктор родительского класса super().__init__() для инициализации унаследованных полей.
'''
'''
Шаг 10: Метод input_data для класса Country
'''
def input_data(self):
    try:
        super().input_data()  # Вызов метода input_data родительского класса
        self._continent_name = input("Введите название континента: ")
        self._capital_name = input("Введите название столицы: ")
        cities_count = int(input("Введите количество городов в стране: "))
        self._cities_names = [input(f"Введите название города {i + 1}: ") for i in range(cities_count)]
    except ValueError as e:
        print(f"Ошибка ввода данных: {e}")
'''
Описание:

Метод input_data класса Country расширяет метод input_data родительского класса City, добавляя дополнительные поля.
'''
'''
Шаг 11: Метод display_data для класса Country
'''
def display_data(self):
    super().display_data()  # Вызов метода display_data родительского класса
    print("Название континента:", self._continent_name)
    print("Название столицы:", self._capital_name)
    print("Названия городов страны:", ", ".join(self._cities_names))
'''
Описание:

Метод display_data класса Country также расширяет метод display_data родительского класса City,
добавляя вывод дополнительных полей.
'''
'''
Шаг 12: Класс Fraction для работы с дробями
'''
class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self._numerator = numerator
        self._denominator = denominator
'''
Описание:

Создается класс Fraction, представляющий дробь.
'''
'''
Шаг 13: Методы доступа get и set для полей numerator и denominator класса Fraction
'''
def get_numerator(self):
    return self._numerator

def set_numerator(self, value):
    try:
        self._numerator = value
    except ValueError as e:
        print(f"Ошибка установки значения: {e}")

def get_denominator(self):
    return self._denominator

def set_denominator(self, value):
    try:
        if value != 0:
            self._denominator = value
        else:
            raise ValueError("Знаменатель не может быть равен 0.")
    except ValueError as e:
        print(f"Ошибка установки значения: {e}")
'''
Описание:

Методы get и set для полей numerator и denominator класса Fraction. Здесь также используется защищенный доступ.
'''
'''
Шаг 14: Арифметические операции для класса Fraction
'''
def add(self, other):
    result = Fraction()
    result._numerator = self._numerator * other._denominator + other._numerator * self._denominator
    result._denominator = self._denominator * other._denominator
    return result

def subtract(self, other):
    result = Fraction()
    result._numerator = self._numerator * other._denominator - other._numerator * self._denominator
    result._denominator = self._denominator * other._denominator
    return result

def multiply(self, other):
    result = Fraction()
    result._numerator = self._numerator * other._numerator
    result._denominator = self._denominator * other._denominator
    return result

def divide(self, other):
    result = Fraction()
    result._numerator = self._numerator * other._denominator
    result._denominator = self._denominator * other._numerator
    return result
'''
Описание:

Методы для выполнения арифметических операций (add, subtract, multiply, divide) для объектов класса Fraction.
'''
'''
Шаг 15: Пример использования всех классов
'''
# Создание объекта класса Person
person = Person()
person.input_data()
print("\nИнформация о человеке:")
person.display_data()

# Создание объекта класса City
city = City()
city.input_data()
print("\nИнформация о городе:")
city.display_data()

# Создание объекта класса Country
country = Country()
country.input_data()
print("\nИнформация о стране:")
country.display_data()

# Создание объекта класса Fraction
fraction1 = Fraction()
fraction1.input_data()
print("\nДробь 1:")
fraction1.display_data()

fraction2 = Fraction()
fraction2.input_data()
print("\nДробь 2:")
fraction2.display_data()

sum_result = fraction1.add(fraction2)
print("\nСложение:")
sum_result.display_data()

diff_result = fraction1.subtract(fraction2)
print("\nВычитание:")
diff_result.display_data()

prod_result = fraction1.multiply(fraction2)
print("\nУмножение:")
prod_result.display_data()

div_result = fraction1.divide(fraction2)
print("\nДеление:")
div_result.display_data()
'''
Описание:

Создаются объекты каждого класса (Person, City, Country, Fraction).
Вызываются соответствующие методы ввода данных и отображения информации.
Для класса Fraction также проводятся арифметические операции.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
                            ''' ЁЩЕ ОДИН вариант написания КОДА - для 1-го этапа ПЗ'''
                                            '''Я бы сказал ВАРИАНТ № 2.'''

'''
Все бы ХОРОШО..... Однако:                                            

Как Я выяснил, существует несколько вариантов дополнительных улучшений или изменений для структуры кода:

Это: - Обработка ошибок:
В коде уже итак присутствует обработка ошибок при вводе данных. Но, мы можем рассмотреть использование более конкретных
исключений для различных типов ошибок, чтобы предоставить более точные сообщения об ошибках.

Так-же это: - использование свойств (properties):
Вместо создания отдельных методов get_... и set_..., можно использовать свойства для более естественного доступа
к полям класса.

И конечно-же это: - использование конструктора для ввода данных: Можем рассмотреть возможность переноса логики ввода
данных в конструктор класса. Это может сделать код более чистым и упростить создание объектов.

Затем, это: - разделение на подклассы: Если у нас появятся дополнительные требования или поля для каждого из классов
(например, новые данные для человека, города, страны), мы можем рассмотреть создание подклассов для более специфических
типов объектов.

Ну и наконец, это: - Методы форматированного вывода: Вместо прямого вывода через print в методах display_data,
мы можем воспользоваться форматированным выводом, что может улучшить читаемость кода.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Задание №1: Реализация класса "Человек"
class Person:
    def __init__(self):
        self._full_name = ""
        self._birth_date = ""
        self._contact_phone = ""
        self._city = ""
        self._country = ""
        self._home_address = ""

    # Метод для ввода данных
    def input_data(self):
        try:
            # Доступ к полю через свойство full_name
            self.full_name = input("Введите ФИО: ")
            self._birth_date = input("Введите дату рождения (в формате дд. мм. гг): ")
            self._contact_phone = input("Введите контактный телефон (в формате +7 (XXX) XXX-XX-XX): ")
            self._city = input("Введите город: ")
            self._country = input("Введите страну: ")
            self._home_address = input("Введите домашний адрес: ")
        except Exception as e:
            print(f"Ошибка ввода данных: {e}")

    # Метод для вывода данных
    def display_data(self):
        print("ФИО:", self.full_name)
        print("Дата рождения:", self._birth_date)
        print("Контактный телефон:", self._contact_phone)
        print("Город:", self._city)
        print("Страна:", self._country)
        print("Домашний адрес:", self._home_address)

    # Свойство для доступа к полю full_name
    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        try:
            if not value:
                raise ValueError("Поле 'ФИО' не может быть пустым.")
            self._full_name = value
        except ValueError as e:
            print(f"Ошибка установки значения: {e}")


# Задание №2: Реализация класса "Город"
class City:
    def __init__(self):
        self._city_name = ""
        self._region_name = ""
        self._country_name = ""
        self._population = 0
        self._postal_code = ""
        self._phone_code = ""

    # Метод для ввода данных
    def input_data(self):
        try:
            self._city_name = input("Введите название города: ")
            self._region_name = input("Введите название региона: ")
            self._country_name = input("Введите название страны: ")
            self._population = int(input("Введите количество жителей в городе: "))
            self._postal_code = input("Введите почтовый индекс города: ")
            self._phone_code = input("Введите телефонный код города: ")
        except ValueError as e:
            print(f"Ошибка ввода данных: {e}")

    # Метод для вывода данных
    def display_data(self):
        print("Название города:", self._city_name)
        print("Название региона:", self._region_name)
        print("Название страны:", self._country_name)
        print("Количество жителей:", self._population)
        print("Почтовый индекс:", self._postal_code)
        print("Телефонный код:", self._phone_code)

    # Методы доступа к полям через методы класса
    def get_city_name(self):
        return self._city_name

    def set_city_name(self, value):
        try:
            if not value:
                raise ValueError("Поле 'Название города' не может быть пустым.")
            self._city_name = value
        except ValueError as e:
            print(f"Ошибка установки значения: {e}")


# Задание №3: Реализация класса "Страна"
class Country:
    def __init__(self):
        self._country_name = ""
        self._continent_name = ""
        self._population = 0
        self._phone_code = ""
        self._capital_name = ""
        self._cities = []

    # Метод для ввода данных
    def input_data(self):
        try:
            self._country_name = input("Введите название страны: ")
            self._continent_name = input("Введите название континента: ")
            self._population = int(input("Введите количество жителей в стране: "))
            self._phone_code = input("Введите телефонный код страны: ")
            self._capital_name = input("Введите название столицы: ")
            cities_input = input("Введите названия городов через запятую: ")
            self._cities = [city.strip() for city in cities_input.split(',')]
        except ValueError as e:
            print(f"Ошибка ввода данных: {e}")

    # Метод для вывода данных
    def display_data(self):
        print("Название страны:", self._country_name)
        print("Название континента:", self._continent_name)
        print("Количество жителей:", self._population)
        print("Телефонный код:", self._phone_code)
        print("Столица:", self._capital_name)
        print("Города:", ', '.join(self._cities))

    # Методы доступа к полям через методы класса
    def get_country_name(self):
        return self._country_name

    def set_country_name(self, value):
        try:
            if not value:
                raise ValueError("Поле 'Название страны' не может быть пустым.")
            self._country_name = value
        except ValueError as e:
            print(f"Ошибка установки значения: {e}")


# Задание №4: Реализация класса "Дробь"
class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self._numerator = numerator
        self._denominator = denominator

    # Метод для ввода данных
    def input_data(self):
        try:
            self._numerator = int(input("Введите числитель: "))
            self._denominator = int(input("Введите знаменатель (не равен 0): "))
            while self._denominator == 0:
                print("Знаменатель не может быть равен 0.")
                self._denominator = int(input("Введите знаменатель (не равен 0): "))
        except ValueError as e:
            print(f"Ошибка ввода данных: {e}")

    # Метод для вывода данных
    def display_data(self):
        print(f"{self._numerator}/{self._denominator}")

    # Методы доступа к полям через методы класса
    def get_numerator(self):
        return self._numerator

    def set_numerator(self, value):
        try:
            self._numerator = value
        except ValueError as e:
            print(f"Ошибка установки значения: {e}")

    def get_denominator(self):
        return self._denominator

    def set_denominator(self, value):
        try:
            if value != 0:
                self._denominator = value
            else:
                raise ValueError("Знаменатель не может быть равен 0.")
        except ValueError as e:
            print(f"Ошибка установки значения: {e}")

    # Арифметические операции
    def add(self, other):
        result = Fraction()
        result._numerator = self._numerator * other._denominator + other._numerator * self._denominator
        result._denominator = self._denominator * other._denominator
        return result

    def subtract(self, other):
        result = Fraction()
        result._numerator = self._numerator * other._denominator - other._numerator * self._denominator
        result._denominator = self._denominator * other._denominator
        return result

    def multiply(self, other):
        result = Fraction()
        result._numerator = self._numerator * other._numerator
        result._denominator = self._denominator * other._denominator
        return result

    def divide(self, other):
        result = Fraction()
        result._numerator = self._numerator * other._denominator
        result._denominator = self._denominator * other._numerator
        return result


# Пример использования:

# Создание объекта класса Person
person = Person()
person.input_data()
print("\nИнформация о человеке:")
person.display_data()

# Создание объекта класса City
city = City()
city.input_data()
print("\nИнформация о городе:")
city.display_data()

# Создание объекта класса Country
country = Country()
country.input_data()
print("\nИнформация о стране:")
country.display_data()

# Создание объекта класса Fraction
fraction1 = Fraction()
fraction1.input_data()
print("\nДробь 1:")
fraction1.display_data()

fraction2 = Fraction()
fraction2.input_data()
print("\nДробь 2:")
fraction2.display_data()

# Выполнение арифметических операций с дробями
sum_result = fraction1.add(fraction2)
print("\nСложение:")
sum_result.display_data()

diff_result = fraction1.subtract(fraction2)
print("\nВычитание:")
diff_result.display_data()

prod_result = fraction1.multiply(fraction2)
print("\nУмножение:")
prod_result.display_data()

div_result = fraction1.divide(fraction2)
print("\nДеление:")
div_result.display_data()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
                        '''ДАЛЕЕ ВТОРОЙ БОЛК выполнения ПРАКТИЧЕСКОГО ЗАДАНИЯ'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''ООП. Инкапсуляция'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Задание №1: Полная инкапсуляция
class EncapsulationExample:
    def __init__(self):
        # Приватные атрибуты
        self.__private_data = None

    # Метод для получения значения приватного атрибута
    def get_private_data(self):
        return self.__private_data

    # Метод для установки значения приватного атрибута
    def set_private_data(self, value):
        self.__private_data = value


# Задание №2: Классы игр с наследованием
class Games:
    Year = 2023  # Статическое поле

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


# Классы с наследованием
class PCGames(Games):
    def __init__(self, name, pc_feature):
        super().__init__(name)
        self.pc_feature = pc_feature

    # Переопределение метода
    def get_name(self):
        return f"{self.name} (PC)"


class PS4Games(Games):
    def __init__(self, name, exclusive_title):
        super().__init__(name)
        self.exclusive_title = exclusive_title

    # Переопределение метода
    def get_name(self):
        return f"{self.name} (PS4)"


class XboxGames(Games):
    def __init__(self, name, backward_compatible):
        super().__init__(name)
        self.backward_compatible = backward_compatible

    # Переопределение метода
    def get_name(self):
        return f"{self.name} (Xbox)"


class MobileGames(Games):
    def __init__(self, name, mobile_platform):
        super().__init__(name)
        self.mobile_platform = mobile_platform

    # Переопределение метода
    def get_name(self):
        return f"{self.name} (Mobile)"


# Задание №3: Наследование для классов стран
class Country:
    def __init__(self, name):
        self.name = name
        self.population = None

    def set_population(self, population):
        self.population = population

    def get_population(self):
        return self.population


class Russia(Country):
    def __init__(self):
        super().__init__("Russia")


class Canada(Country):
    def __init__(self):
        super().__init__("Canada")


class Germany(Country):
    def __init__(self):
        super().__init__("Germany")


# Пример использования
# Задание №1
obj = EncapsulationExample()
obj.set_private_data(42)
print(obj.get_private_data())  # Вывод: 42

# Задание №2
pc_game = PCGames("Cyberpunk 2077", "Ray Tracing")
print(pc_game.get_name())  # Вывод: Cyberpunk 2077 (PC)

# Задание №3
russia = Russia()
russia.set_population(145000000)
print(f"{russia.name} population: {russia.get_population()}")  # Вывод: Russia population: 145000000
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1: Полная инкапсуляция

Пример кода:
'''
class EncapsulationExample:
    def __init__(self):
        # Приватные атрибуты
        self.__private_data = None

    # Метод для получения значения приватного атрибута
    def get_private_data(self):
        return self.__private_data

    # Метод для установки значения приватного атрибута
    def set_private_data(self, value):
        self.__private_data = value
'''
Описание:

Класс EncapsulationExample создается с приватным атрибутом __private_data. Для доступа к этому атрибуту
используются методы get_private_data и set_private_data, обеспечивающие полную инкапсуляцию данных.
'''
'''
Шаг №2: Классы игр с наследованием

Пример кода:
'''
class Games:
    Year = 2023  # Статическое поле

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class PCGames(Games):
    def __init__(self, name, pc_feature):
        super().__init__(name)
        self.pc_feature = pc_feature

    # Переопределение метода
    def get_name(self):
        return f"{self.name} (PC)"

# Аналогично для PS4Games, XboxGames, MobileGames
'''
Описание:

Базовый класс Games содержит статическое поле Year и метод get_name. Подклассы (PCGames, PS4Games, XboxGames,
MobileGames) наследуют этот функционал и расширяют его, добавляя дополнительные атрибуты и переопределяя метод get_name.
'''
'''
Шаг №3: Наследование для классов стран

Пример кода:
'''
class Country:
    def __init__(self, name):
        self.name = name
        self.population = None

    def set_population(self, population):
        self.population = population

    def get_population(self):
        return self.population


class Russia(Country):
    def __init__(self):
        super().__init__("Russia")

# Аналогично для Canada, Germany
'''
Описание:

Базовый класс Country содержит атрибуты name и population, а также методы set_population и get_population.
Подклассы (Russia, Canada, Germany) наследуют функционал базового класса.
'''
'''
Пример использования:

Пример кода:
'''
# Задание №1
obj = EncapsulationExample()
obj.set_private_data(42)
print(obj.get_private_data())  # Вывод: 42

# Задание №2
pc_game = PCGames("Cyberpunk 2077", "Ray Tracing")
print(pc_game.get_name())  # Вывод: Cyberpunk 2077 (PC)

# Задание №3
russia = Russia()
russia.set_population(145000000)
print(f"{russia.name} population: {russia.get_population()}")  # Вывод: Russia population: 145000000
'''
Описание:

Приведен пример использования созданных классов и методов. Создаются объекты, 
устанавливаются значения и выводится информация.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #


