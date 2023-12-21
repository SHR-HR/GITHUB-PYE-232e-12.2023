# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''  ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓
Дата выполнения практической работы: 20-21 - ДЕКАБРЯ 2023
''''  ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓
'''
Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
Дисциплина: Основы программирования на Python
'''
'''
Урок от 18.12.2023
Домашняя работа №17: Объектно-ориентированное программирование
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполните следующие задания:   
'''
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
• Задание №1

Реализуйте класс «Автомобиль».
Необходимо хранить в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену.
Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
• Задание №2

Реализуйте класс «Книга».
Необходимо хранить в полях класса: название книги, год выпуска, издателя, жанр, автора, цену.
Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
• Задание №3

Реализуйте класс «Стадион». 
Необходимо хранить в полях класса: название стадиона, дату открытия, страну, город, вместимость.
Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
class Car:
    def __init__(self, model="", year=0, manufacturer="", engine_volume=0.0, color="", price=0.0):
        # Инициализация атрибутов
        self._model = model
        self._year = year
        self._manufacturer = manufacturer
        self._engine_volume = engine_volume
        self._color = color
        self._price = price

    def __str__(self):
        # Возвращение строкового представления объекта
        return f"Car(Model: {self._model}, Year: {self._year}, Manufacturer: {self._manufacturer}, " \
               f"Engine Volume: {self._engine_volume}, Color: {self._color}, Price: {self._price})"

    def input_data(self):
        # Задание №1: Метод для ввода данных
        try:
            self._model = input("Введите название модели автомобиля: ")
            self._year = int(input("Введите год выпуска автомобиля: "))
            self._manufacturer = input("Введите производителя автомобиля: ")
            self._engine_volume = float(input("Введите объем двигателя автомобиля: "))
            self._color = input("Введите цвет машины: ")
            self._price = float(input("Введите цену автомобиля: "))
        except ValueError as e:
            print(f"Ошибка ввода данных: {e}")

    def display_data(self):
        # Задание №1: Метод для вывода данных
        print(f"Название модели: {self._model}")
        print(f"Год выпуска: {self._year}")
        print(f"Производитель: {self._manufacturer}")
        print(f"Объем двигателя: {self._engine_volume}")
        print(f"Цвет машины: {self._color}")
        print(f"Цена: {self._price}")

    @property
    def model(self):
        # Задание №1: Свойство для доступа к полю "Название модели"
        return self._model

    @model.setter
    def model(self, value):
        # Задание №1: Свойство для установки значения в поле "Название модели"
        try:
            if not value:
                raise ValueError("Поле 'Название модели' не может быть пустым.")
            self._model = value
        except ValueError as e:
            print(f"Ошибка установки значения: {e}")


class Book:
    def __init__(self, title="", year=0, publisher="", genre="", author="", price=0.0):
        # Инициализация атрибутов
        self._title = title
        self._year = year
        self._publisher = publisher
        self._genre = genre
        self._author = author
        self._price = price

    def __str__(self):
        # Возвращение строкового представления объекта
        return f"Book(Title: {self._title}, Year: {self._year}, Publisher: {self._publisher}, " \
               f"Genre: {self._genre}, Author: {self._author}, Price: {self._price})"

    def input_data(self):
        # Задание №2: Метод для ввода данных
        try:
            self._title = input("Введите название книги: ")
            self._year = int(input("Введите год выпуска книги: "))
            self._publisher = input("Введите издателя книги: ")
            self._genre = input("Введите жанр книги: ")
            self._author = input("Введите автора книги: ")
            self._price = float(input("Введите цену книги: "))
        except ValueError as e:
            print(f"Ошибка ввода данных: {e}")

    def display_data(self):
        # Задание №2: Метод для вывода данных
        print(f"Название книги: {self._title}")
        print(f"Год выпуска: {self._year}")
        print(f"Издатель: {self._publisher}")
        print(f"Жанр: {self._genre}")
        print(f"Автор: {self._author}")
        print(f"Цена: {self._price}")

    @property
    def title(self):
        # Задание №2: Свойство для доступа к полю "Название книги"
        return self._title

    @title.setter
    def title(self, value):
        # Задание №2: Свойство для установки значения в поле "Название книги"
        try:
            if not value:
                raise ValueError("Поле 'Название книги' не может быть пустым.")
            self._title = value
        except ValueError as e:
            print(f"Ошибка установки значения: {e}")


class Stadium:
    def __init__(self, name="", opening_date="", country="", city="", capacity=0):
        # Инициализация атрибутов
        self._name = name
        self._opening_date = opening_date
        self._country = country
        self._city = city
        self._capacity = capacity

    def __str__(self):
        # Возвращение строкового представления объекта
        return f"Stadium(Name: {self._name}, Opening Date: {self._opening_date}, Country: {self._country}, " \
               f"City: {self._city}, Capacity: {self._capacity})"

    def input_data(self):
        # Задание №3: Метод для ввода данных
        try:
            self._name = input("Введите название стадиона: ")
            self._opening_date = input("Введите дату открытия стадиона: ")
            self._country = input("Введите страну, в которой находится стадион: ")
            self._city = input("Введите город, в котором построен стадион: ")
            self._capacity = int(input("Введите вместимость стадиона: "))
        except ValueError as e:
            print(f"Ошибка ввода данных: {e}")

    def display_data(self):
        # Задание №3: Метод для вывода данных
        print(f"Название стадиона: {self._name}")
        print(f"Дата открытия: {self._opening_date}")
        print(f"Страна: {self._country}")
        print(f"Город: {self._city}")
        print(f"Вместимость: {self._capacity}")

    @property
    def name(self):
        # Задание №3: Свойство для доступа к полю "Название стадиона"
        return self._name

    @name.setter
    def name(self, value):
        # Задание №3: Свойство для установки значения в поле "Название стадиона"
        try:
            if not value:
                raise ValueError("Поле 'Название стадиона' не может быть пустым.")
            self._name = value
        except ValueError as e:
            print(f"Ошибка установки значения: {e}")


# Пример использования:

# Создание объекта класса Car
car = Car()
car.input_data()
print("\nИнформация об автомобиле:")
car.display_data()

# Создание объекта класса Book
book = Book()
book.input_data()
print("\nИнформация о книге:")
book.display_data()

# Создание объекта класса Stadium
stadium = Stadium()
stadium.input_data()
print("\nИнформация о стадионе:")
stadium.display_data()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1: Объявление класса "Car"
'''
class Car:
''''
Описание: 

На этом шаге объявляется класс "Car", представляющий автомобиль. 
Класс содержит атрибуты, методы и свойства, которые описывают характеристики автомобиля.
''''
'''
Шаг №2: Конструктор класса "Car"
'''
def __init__(self, model="", year=0, manufacturer="", engine_volume=0.0, color="", price=0.0):
    # Инициализация атрибутов
    self._model = model
    self._year = year
    self._manufacturer = manufacturer
    self._engine_volume = engine_volume
    self._color = color
    self._price = price
'''
Описание: 

В этом шаге определен конструктор класса "Car", который инициализирует атрибуты объекта. 
Атрибуты включают в себя модель автомобиля, год выпуска, производителя, объем двигателя, цвет и цену.
'''
'''
Шаг №3: Метод "str" класса "Car"
'''
def __str__(self):
    # Возвращение строкового представления объекта
    return f"Car(Model: {self._model}, Year: {self._year}, Manufacturer: {self._manufacturer}, " \
           f"Engine Volume: {self._engine_volume}, Color: {self._color}, Price: {self._price})"
'''
Описание: 

Этот метод позволяет получить строковое представление объекта класса "Car".
Он возвращает информацию о модели, годе выпуска, производителе, объеме двигателя, цвете и цене автомобиля.
'''
'''
Шаг №4: Метод "input_data" класса "Car"
'''
def input_data(self):
    # Метод для ввода данных
    try:
        self._model = input("Введите название модели автомобиля: ")
        self._year = int(input("Введите год выпуска автомобиля: "))
        self._manufacturer = input("Введите производителя автомобиля: ")
        self._engine_volume = float(input("Введите объем двигателя автомобиля: "))
        self._color = input("Введите цвет машины: ")
        self._price = float(input("Введите цену автомобиля: "))
    except ValueError as e:
        print(f"Ошибка ввода данных: {e}")
'''
Описание: 

Этот метод позволяет пользователю ввести данные о модели, годе выпуска, производителе, объеме двигателя,
цвете и цене автомобиля. В случае ошибки ввода, выводится сообщение об ошибке.
'''
'''
Шаг №5: Метод "display_data" класса "Car"
'''
def display_data(self):
    # Метод для вывода данных
    print(f"Название модели: {self._model}")
    print(f"Год выпуска: {self._year}")
    print(f"Производитель: {self._manufacturer}")
    print(f"Объем двигателя: {self._engine_volume}")
    print(f"Цвет машины: {self._color}")
    print(f"Цена: {self._price}")
'''
Описание: 

Этот метод выводит на экран данные об автомобиле, включая название модели, год выпуска, производителя,
объем двигателя, цвет и цену.
'''
'''
Шаг №6: Свойство "model" класса "Car"
'''
@property
def model(self):
    # Свойство для доступа к полю "Название модели"
    return self._model
@model.setter
def model(self, value):
    # Свойство для установки значения в поле "Название модели"
    try:
        if not value:
            raise ValueError("Поле 'Название модели' не может быть пустым.")
        self._model = value
    except ValueError as e:
        print(f"Ошибка установки значения: {e}")
'''
Описание: 

Эти свойства позволяют получать и устанавливать значение поля "Название модели" объекта класса "Car". 
Если передаваемое значение пусто, генерируется исключение ValueError.
'''
'''
Шаг №7: Объявление класса "Book"
'''
def __init__(self, title="", year=0, publisher="", genre="", author="", price=0.0):
    # Инициализация атрибутов
    self._title = title
    self._year = year
    self._publisher = publisher
    self._genre = genre
    self._author = author
    self._price = price
'''
Описание: 

В этом шаге определен конструктор класса "Book", который инициализирует атрибуты объекта. 
Атрибуты включают в себя название книги, год выпуска, издателя, жанр, автора и цену.
'''
'''
Шаг №8: Метод "str" класса "Book"
'''
def __str__(self):
    # Возвращение строкового представления объекта
    return f"Book(Title: {self._title}, Year: {self._year}, Publisher: {self._publisher}, " \
           f"Genre: {self._genre}, Author: {self._author}, Price: {self._price})"
'''
Описание: 

Этот метод позволяет получить строковое представление объекта класса "Book". 
Он возвращает информацию о названии, годе выпуска, издателе, жанре, авторе и цене книги.
'''
'''
Шаг №9: Метод "input_data" класса "Book"
'''
def input_data(self):
    # Метод для ввода данных
    try:
        self._title = input("Введите название книги: ")
        self._year = int(input("Введите год выпуска книги: "))
        self._publisher = input("Введите издателя книги: ")
        self._genre = input("Введите жанр книги: ")
        self._author = input("Введите автора книги: ")
        self._price = float(input("Введите цену книги: "))
    except ValueError as e:
        print(f"Ошибка ввода данных: {e}")
'''
Описание: 

Этот метод позволяет пользователю ввести данные о книге, такие как название, год выпуска, издатель, жанр, автор и цена.
В случае ошибки ввода, выводится сообщение об ошибке.
'''
'''
Шаг №10: Метод "display_data" класса "Book"
'''
def display_data(self):
    # Метод для вывода данных
    print(f"Название книги: {self._title}")
    print(f"Год выпуска: {self._year}")
    print(f"Издатель: {self._publisher}")
    print(f"Жанр: {self._genre}")
    print(f"Автор: {self._author}")
    print(f"Цена: {self._price}")
'''
Описание: 

Этот метод выводит на экран данные о книге, включая название, год выпуска, издатель, жанр, автора и цену.
'''
'''
Шаг №11: Свойство "title" класса "Book"
'''
@property
def title(self):
    # Свойство для доступа к полю "Название книги"
    return self._title
@title.setter
def title(self, value):
    # Свойство для установки значения в поле "Название книги"
    try:
        if not value:
            raise ValueError("Поле 'Название книги' не может быть пустым.")
        self._title = value
    except ValueError as e:
        print(f"Ошибка установки значения: {e}")
'''
Описание: 

Эти свойства позволяют получать и устанавливать значение поля "Название книги" объекта класса "Book".
Если передаваемое значение пусто, генерируется исключение ValueError.
'''
'''
Шаг №11 (продолжение): Объявление класса "Stadium"
'''
class Stadium:
''''
Описание: 

На этом шаге объявляется класс "Stadium", представляющий стадион. Класс содержит атрибуты, методы и свойства для
описания характеристик стадиона.
''''
'''
Шаг №12: Конструктор класса "Stadium"
'''
def __init__(self, name="", opening_date="", country="", city="", capacity=0):
    # Инициализация атрибутов
    self._name = name
    self._opening_date = opening_date
    self._country = country
    self._city = city
    self._capacity = capacity
'''
Описание: 

В этом шаге определен конструктор класса "Stadium", который инициализирует атрибуты объекта. 
Атрибуты включают в себя название стадиона, дату открытия, страну, город и вместимость.
'''
'''
Шаг №13: Метод "str" класса "Stadium"
'''
def __str__(self):
    # Возвращение строкового представления объекта
    return f"Stadium(Name: {self._name}, Opening Date: {self._opening_date}, Country: {self._country}, " \
           f"City: {self._city}, Capacity: {self._capacity})"
'''
Описание: 

Этот метод позволяет получить строковое представление объекта класса "Stadium". 
Он возвращает информацию о названии, дате открытия, стране, городе и вместимости стадиона.
'''
'''
Шаг №14: Метод "input_data" класса "Stadium"
'''
def input_data(self):
    # Метод для ввода данных
    try:
        self._name = input("Введите название стадиона: ")
        self._opening_date = input("Введите дату открытия стадиона: ")
        self._country = input("Введите страну, в которой находится стадион: ")
        self._city = input("Введите город, в котором построен стадион: ")
        self._capacity = int(input("Введите вместимость стадиона: "))
    except ValueError as e:
        print(f"Ошибка ввода данных: {e}")
'''
Описание: 

Этот метод позволяет пользователю ввести данные о стадионе, такие как название,
дата открытия, страна, город и вместимость. В случае ошибки ввода, выводится сообщение об ошибке.
'''
'''
Шаг №15: Метод "display_data" класса "Stadium"
'''
def display_data(self):
    # Метод для вывода данных
    print(f"Название стадиона: {self._name}")
    print(f"Дата открытия: {self._opening_date}")
    print(f"Страна: {self._country}")
    print(f"Город: {self._city}")
    print(f"Вместимость: {self._capacity}")
'''
Описание: 

Этот метод выводит на экран данные о стадионе, включая название, дату открытия, страну, город и вместимость.
'''
'''
Шаг №16: Свойство "name" класса "Stadium"
'''
@property
def name(self):
    # Свойство для доступа к полю "Название стадиона"
    return self._name
@name.setter
def name(self, value):
    # Свойство для установки значения в поле "Название стадиона"
    try:
        if not value:
            raise ValueError("Поле 'Название стадиона' не может быть пустым.")
        self._name = value
    except ValueError as e:
        print(f"Ошибка установки значения: {e}")
'''
Описание: 

Эти свойства позволяют получать и устанавливать значение поля "Название стадиона" объекта класса "Stadium".
Если передаваемое значение пусто, генерируется исключение ValueError.
'''
'''
Шаг №17: Пример использования классов
'''
# Создание объекта класса Car
car = Car()
car.input_data()
print("\nИнформация об автомобиле:")
car.display_data()

# Создание объекта класса Book
book = Book()
book.input_data()
print("\nИнформация о книге:")
book.display_data()

# Создание объекта класса Stadium
stadium = Stadium()
stadium.input_data()
print("\nИнформация о стадионе:")
stadium.display_data()
'''
Описание: 

Этот шаг содержит пример использования созданных классов. 
Объекты классов "Car", "Book" и "Stadium" создаются, заполняются данными с помощью метода input_data, а затем выводятся
на экран с помощью метода display_data.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
                         '''    НУ И КАК Я МОГ ЗАБЫТЬ О # def __del__(self): ???    '''
                            '''     ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓    '''
# Задание №1: Реализация класса "Автомобиль"
class Car:
    def __init__(self, model="", year=0, manufacturer="", engine_volume=0.0, color="", price=0.0):
        # Инициализация атрибутов
        self._model = model
        self._year = year
        self._manufacturer = manufacturer
        self._engine_volume = engine_volume
        self._color = color
        self._price = price

    def __str__(self):
        # Возвращение строкового представления объекта
        return f"Car(Model: {self._model}, Year: {self._year}, Manufacturer: {self._manufacturer}, " \
               f"Engine Volume: {self._engine_volume}, Color: {self._color}, Price: {self._price})"

    def input_data(self):
        # Метод для ввода данных
        try:
            self._model = input("Введите название модели автомобиля: ")
            self._year = int(input("Введите год выпуска автомобиля: "))
            self._manufacturer = input("Введите производителя автомобиля: ")
            self._engine_volume = float(input("Введите объем двигателя автомобиля: "))
            self._color = input("Введите цвет машины: ")
            self._price = float(input("Введите цену автомобиля: "))
        except ValueError as e:
            print(f"Ошибка ввода данных: {e}")

    def display_data(self):
        # Метод для вывода данных
        print(f"Название модели: {self._model}")
        print(f"Год выпуска: {self._year}")
        print(f"Производитель: {self._manufacturer}")
        print(f"Объем двигателя: {self._engine_volume}")
        print(f"Цвет машины: {self._color}")
        print(f"Цена: {self._price}")

    @property
    def model(self):
        # Свойство для доступа к полю "Название модели"
        return self._model

    @model.setter
    def model(self, value):
        # Свойство для установки значения в поле "Название модели"
        try:
            if not value:
                raise ValueError("Поле 'Название модели' не может быть пустым.")
            self._model = value
        except ValueError as e:
            print(f"Ошибка установки значения: {e}")

    def __del__(self):
        print(f"Автомобиль {self._model} удален")


# Задание №2: Реализация класса "Книга"
class Book:
    def __init__(self, title="", year=0, publisher="", genre="", author="", price=0.0):
        # Инициализация атрибутов
        self._title = title
        self._year = year
        self._publisher = publisher
        self._genre = genre
        self._author = author
        self._price = price

    def __str__(self):
        # Возвращение строкового представления объекта
        return f"Book(Title: {self._title}, Year: {self._year}, Publisher: {self._publisher}, " \
               f"Genre: {self._genre}, Author: {self._author}, Price: {self._price})"

    def input_data(self):
        # Метод для ввода данных
        try:
            self._title = input("Введите название книги: ")
            self._year = int(input("Введите год выпуска книги: "))
            self._publisher = input("Введите издателя книги: ")
            self._genre = input("Введите жанр книги: ")
            self._author = input("Введите автора книги: ")
            self._price = float(input("Введите цену книги: "))
        except ValueError as e:
            print(f"Ошибка ввода данных: {e}")

    def display_data(self):
        # Метод для вывода данных
        print(f"Название книги: {self._title}")
        print(f"Год выпуска: {self._year}")
        print(f"Издатель: {self._publisher}")
        print(f"Жанр: {self._genre}")
        print(f"Автор: {self._author}")
        print(f"Цена: {self._price}")

    @property
    def title(self):
        # Свойство для доступа к полю "Название книги"
        return self._title

    @title.setter
    def title(self, value):
        # Свойство для установки значения в поле "Название книги"
        try:
            if not value:
                raise ValueError("Поле 'Название книги' не может быть пустым.")
            self._title = value
        except ValueError as e:
            print(f"Ошибка установки значения: {e}")

    def __del__(self):
        print(f"Книга {self._title} удалена")


# Задание №3: Реализация класса "Стадион"
class Stadium:
    def __init__(self, name="", opening_date="", country="", city="", capacity=0):
        # Инициализация атрибутов
        self._name = name
        self._opening_date = opening_date
        self._country = country
        self._city = city
        self._capacity = capacity

    def __str__(self):
        # Возвращение строкового представления объекта
        return f"Stadium(Name: {self._name}, Opening Date: {self._opening_date}, Country: {self._country}, " \
               f"City: {self._city}, Capacity: {self._capacity})"

    def input_data(self):
        # Метод для ввода данных
        try:
            self._name = input("Введите название стадиона: ")
            self._opening_date = input("Введите дату открытия стадиона: ")
            self._country = input("Введите страну, в которой находится стадион: ")
            self._city = input("Введите город, в котором построен стадион: ")
            self._capacity = int(input("Введите вместимость стадиона: "))
        except ValueError as e:
            print(f"Ошибка ввода данных: {e}")

    def display_data(self):
        # Метод для вывода данных
        print(f"Название стадиона: {self._name}")
        print(f"Дата открытия: {self._opening_date}")
        print(f"Страна: {self._country}")
        print(f"Город: {self._city}")
        print(f"Вместимость: {self._capacity}")

    @property
    def name(self):
        # Свойство для доступа к полю "Название стадиона"
        return self._name

    @name.setter
    def name(self, value):
        # Свойство для установки значения в поле "Название стадиона"
        try:
            if not value:
                raise ValueError("Поле 'Название стадиона' не может быть пустым.")
            self._name = value
        except ValueError as e:
            print(f"Ошибка установки значения: {e}")

    def __del__(self):
        print(f"Стадион {self._name} удален")


# Пример использования:

# Создание объекта класса Car
car = Car()
car.input_data()
print("\nИнформация об автомобиле:")
car.display_data()
del car  # Это приведет к вызову метода __del__ и удалению объекта

# Создание объекта класса Book
book = Book()
book.input_data()
print("\nИнформация о книге:")
book.display_data()
del book  # Это приведет к вызову метода __del__ и удалению объекта

# Создание объекта класса Stadium
stadium = Stadium()
stadium.input_data()
print("\nИнформация о стадионе:")
stadium.display_data()
del stadium  # Это приведет к вызову метода __del__ и удалению объекта
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
@property и @<attribute>.setter - это декораторы в Python, которые используются для создания свойств (properties) в
классах. Они обеспечивают доступ к атрибутам объекта через синтаксис доступа к свойствам, что позволяет использовать
объекты класса как атрибуты, а не методы.
'''
'''
@property: Этот декоратор позволяет использовать метод как свойство объекта. 
Это означает, что можно обращаться к методу, как если бы это было атрибутом, а не вызывать его явно как функцию.
'''
'''
Пример:
'''
class Example:
    def __init__(self):
        self._value = 0

    @property
    def value(self):
        return self._value

# Использование
obj = Example()
print(obj.value)  # Обращение к методу value как к свойству
'''
@<attribute>.setter: Этот декоратор позволяет установить значение атрибута через метод.
Он вызывается при присваивании значения свойству.
'''
'''
Пример:
'''
class Example:
    def __init__(self):
        self._value = 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

# Использование
obj = Example()
obj.value = 42  # Установка значения через свойство
print(obj.value)  # Получение значения через свойство
'''
В моем коде:

@property используется для создания свойства доступа к атрибутам класса без явного вызова методов.
@<attribute>.setter используется для создания метода, который будет вызываться при установке значения атрибута. 
В коде это используется, например, для проверки и обработки данных, прежде чем установить значение атрибута.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
                              '''     КАК вариант просто оставлю это ТУТ     '''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Задание №1: Реализация класса "Автомобиль"
class Car:
    def __init__(self):
        # Приватные атрибуты
        self._model = ""
        self._year = 0
        self._manufacturer = ""
        self._engine_volume = 0.0
        self._color = ""
        self._price = 0.0

    # Метод для ввода данных
    def input_data(self):
        try:
            self._model = input("Введите название модели: ")
            self._year = int(input("Введите год выпуска: "))
            self._manufacturer = input("Введите производителя: ")
            self._engine_volume = float(input("Введите объем двигателя: "))
            self._color = input("Введите цвет машины: ")
            self._price = float(input("Введите цену: "))
        except ValueError as e:
            print(f"Ошибка ввода данных: {e}")

    # Метод для форматированного вывода данных
    def display_data(self):
        print(f"\nИнформация об автомобиле {self._model}:")
        print(f"Год выпуска: {self._year}")
        print(f"Производитель: {self._manufacturer}")
        print(f"Объем двигателя: {self._engine_volume}")
        print(f"Цвет машины: {self._color}")
        print(f"Цена: {self._price}")

    # Методы доступа к полям через свойства
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        try:
            if not value:
                raise ValueError("Поле 'Название модели' не может быть пустым.")
            self._model = value
        except ValueError as e:
            print(f"Ошибка установки значения: {e}")


# Задание №2: Реализация класса "Книга"
class Book:
    def __init__(self):
        # Приватные атрибуты
        self._title = ""
        self._year = 0
        self._publisher = ""
        self._genre = ""
        self._author = ""
        self._price = 0.0

    # Метод для ввода данных
    def input_data(self):
        try:
            self._title = input("Введите название книги: ")
            self._year = int(input("Введите год выпуска: "))
            self._publisher = input("Введите издателя: ")
            self._genre = input("Введите жанр: ")
            self._author = input("Введите автора: ")
            self._price = float(input("Введите цену: "))
        except ValueError as e:
            print(f"Ошибка ввода данных: {e}")

    # Метод для форматированного вывода данных
    def display_data(self):
        print(f"\nИнформация о книге '{self._title}':")
        print(f"Год выпуска: {self._year}")
        print(f"Издатель: {self._publisher}")
        print(f"Жанр: {self._genre}")
        print(f"Автор: {self._author}")
        print(f"Цена: {self._price}")

    # Методы доступа к полям через свойства
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        try:
            if not value:
                raise ValueError("Поле 'Название книги' не может быть пустым.")
            self._title = value
        except ValueError as e:
            print(f"Ошибка установки значения: {e}")


# Задание №3: Реализация класса "Стадион"
class Stadium:
    def __init__(self):
        # Приватные атрибуты
        self._name = ""
        self._opening_date = ""
        self._country = ""
        self._city = ""
        self._capacity = 0

    # Метод для ввода данных
    def input_data(self):
        try:
            self._name = input("Введите название стадиона: ")
            self._opening_date = input("Введите дату открытия: ")
            self._country = input("Введите страну: ")
            self._city = input("Введите город: ")
            self._capacity = int(input("Введите вместимость: "))
        except ValueError as e:
            print(f"Ошибка ввода данных: {e}")

    # Метод для форматированного вывода данных
    def display_data(self):
        print(f"\nИнформация о стадионе '{self._name}':")
        print(f"Дата открытия: {self._opening_date}")
        print(f"Страна: {self._country}")
        print(f"Город: {self._city}")
        print(f"Вместимость: {self._capacity}")

    # Методы доступа к полям через свойства
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        try:
            if not value:
                raise ValueError("Поле 'Название стадиона' не может быть пустым.")
            self._name = value
        except ValueError as e:
            print(f"Ошибка установки значения: {e}")


# Пример использования:

# Создание объекта класса Car
car = Car()
car.input_data()
car.display_data()

# Создание объекта класса Book
book = Book()
book.input_data()
book.display_data()

# Создание объекта класса Stadium
stadium = Stadium()
stadium.input_data()
stadium.display_data()
'''
Общий принцип действия:

В каждом классе есть приватные атрибуты,
которые инициализируются в конструкторе (__init__).

Методы input_data используются для
ввода данных с клавиатуры.

Методы display_data используются для
вывода данных в консоль.

Для каждого атрибута есть методы доступа через свойства (@property и @<attribute>.setter),
позволяющие устанавливать и получать значения атрибутов с определенными правилами.



Так же:

Методы форматированного вывода:
Добавлен форматированный вывод в методах display_data для улучшения читаемости вывода информации о каждом объекте.

Использование свойств (properties):
Заменены методы get_ и set_ на свойства (properties) для более естественного доступа к полям класса.

Другие изменения: 
Незначительные изменения в структуре кода для более удобного чтения.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
ООП. Инкапсуляция
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполните следующие задания:   
'''
'''
Напишите программу, в которой есть главный класс с текстовым полем.
В главное классе должен быть метод для присваивания значения полю: без аргументов и с одним текстовым аргументом.
Объект главного класса создаётся передачей одного текстового аргумента конструктору. 
На основе главного класса создается класса потомок. В классе-потомке нужно добавить числовое поле. 
У конструктора класса-потомка два аргумента.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
# Главный класс
class MainClass:
    def __init__(self, text_field):
        # Текстовое поле
        self._text_field = text_field

    # Метод для присваивания значения полю (без аргументов)
    def set_text_field(self):
        self._text_field = input("Введите текст: ")

    # Метод для присваивания значения полю (с текстовым аргументом)
    def set_text_field_with_argument(self, text):
        self._text_field = text


# Класс-потомок
class SubClass(MainClass):
    def __init__(self, text_field, numeric_field):
        # Вызов конструктора родительского класса
        super().__init__(text_field)
        # Числовое поле
        self._numeric_field = numeric_field


# Пример использования:

# Создание объекта главного класса с передачей текстового аргумента
main_obj = MainClass("Initial Text")

# Вывод текущего значения текстового поля
print(main_obj._text_field)

# Изменение текстового поля с использованием метода без аргументов
main_obj.set_text_field()
print(main_obj._text_field)

# Изменение текстового поля с использованием метода с текстовым аргументом
main_obj.set_text_field_with_argument("New Text")
print(main_obj._text_field)

# Создание объекта класса-потомка с передачей текстового и числового аргументов
sub_obj = SubClass("Sub Text", 42)

# Вывод текущих значений текстового и числового полей класса-потомка
print(sub_obj._text_field)
print(sub_obj._numeric_field)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Главный класс (MainClass):
'''
# Главный класс
class MainClass:
    def __init__(self, text_field):
        # Текстовое поле
        self._text_field = text_field

    # Метод для присваивания значения полю (без аргументов)
    def set_text_field(self):
        self._text_field = input("Введите текст: ")

    # Метод для присваивания значения полю (с текстовым аргументом)
    def set_text_field_with_argument(self, text):
        self._text_field = text
'''
Описание:

MainClass - класс, который является основным (главным) в данной иерархии.
Конструктор __init__ принимает один аргумент text_field и устанавливает его в приватное поле _text_field.
Метод set_text_field присваивает новое значение полю _text_field, считывая его с клавиатуры (ввод пользователя).
Метод set_text_field_with_argument принимает текстовый аргумент text и устанавливает его в поле _text_field.
'''
'''
Класс-потомок (SubClass):
'''
# Класс-потомок
class SubClass(MainClass):
    def __init__(self, text_field, numeric_field):
        # Вызов конструктора родительского класса
        super().__init__(text_field)
        # Числовое поле
        self._numeric_field = numeric_field
'''
Описание:

SubClass - класс-потомок, который наследует от MainClass. 
Это означает, что SubClass получает все атрибуты и методы, определенные в MainClass.
Конструктор __init__ принимает два аргумента: text_field и numeric_field. 
Он вызывает конструктор родительского класса (MainClass) с аргументом text_field, чтобы установить текстовое поле,
и инициализирует свое числовое поле _numeric_field.
'''
'''
Пример использования:
'''
# Пример использования:

# Создание объекта главного класса с передачей текстового аргумента
main_obj = MainClass("Initial Text")

# Вывод текущего значения текстового поля
print(main_obj._text_field)

# Изменение текстового поля с использованием метода без аргументов
main_obj.set_text_field()
print(main_obj._text_field)

# Изменение текстового поля с использованием метода с текстовым аргументом
main_obj.set_text_field_with_argument("New Text")
print(main_obj._text_field)

# Создание объекта класса-потомка с передачей текстового и числового аргументов
sub_obj = SubClass("Sub Text", 42)

# Вывод текущих значений текстового и числового полей класса-потомка
print(sub_obj._text_field)
print(sub_obj._numeric_field)
'''
Описание:

Создается объект main_obj класса MainClass с начальным текстовым полем "Initial Text".
Выводится текущее значение текстового поля объекта main_obj.
Изменяется текстовое поле с использованием метода set_text_field и выводится новое значение.
Изменяется текстовое поле с использованием метода set_text_field_with_argument и выводится новое значение.
Создается объект sub_obj класса SubClass с текстовым полем "Sub Text" и числовым полем 42.
Выводятся текущие значения текстового и числового полей объекта sub_obj.
'''
'''
Замечания:

Приватное поле _text_field можно изменять напрямую, 
но использование методов set_text_field и set_text_field_with_argument является более "правильным" способом изменения
значения, так как они обеспечивают контроль над процессом.
Написанный код включает использование приватных полей (поле, начинающееся с _). 
Обычно такие поля предполагаются приватными и не изменяются напрямую извне класса.

Поэтому оставлю КАК ЕСТЬ.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
ЧТО ЗА - 42 ???

Число 42 часто используется в мире программирования и информатики как символ или "магическое число",
не несущее особого смысла, но часто используемое в примерах и шутках. 
Это стало традицией после культового научно-фантастического произведения Дугласа Адамса "Автостопом по галактике",
где компьютер Deep Thought пришел к выводу, что ответ на вопрос "о жизни, вселенной и всем" равен именно 42.

В мире программирования это число стало своеобразным элементом фольклора и символизирует некоторую произвольность
или неопределенность. В данном контексте я использовал 42 просто как пример числового значения для демонстрации
концепции класса-потомка с числовым полем. А так, мы, вы, они и тд. свободны выбирать любое другое число или 
значение в зависимости от контекста.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
''' Я ТУТ "КАПНУЛ чуть ГЛУБЖЕ" и '''                                           # (Если так можно выразится, вариант №2)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# Главный класс
class MainClass:
    def __init__(self, text_field):
        # Приватные атрибуты
        self.__text_field = text_field

    # Метод для присваивания значения текстовому полю (без аргументов)
    def set_text_field(self):
        try:
            # Валидация данных
            new_text = input("Введите текст: ")
            if not new_text:
                raise ValueError("Текст не может быть пустым.")
            self.__text_field = new_text
        except ValueError as e:
            print(f"Ошибка ввода данных: {e}")

    # Метод для присваивания значения текстовому полю (с текстовым аргументом)
    def set_text_field_with_argument(self, text):
        try:
            # Валидация данных
            if not text:
                raise ValueError("Текст не может быть пустым.")
            self.__text_field = text
        except ValueError as e:
            print(f"Ошибка ввода данных: {e}")

    # Метод доступа к текстовому полю через метод класса
    def get_text_field(self):
        return self.__text_field


# Класс-потомок
class SubClass(MainClass):
    def __init__(self, text_field, numeric_field):
        # Вызов конструктора родительского класса
        super().__init__(text_field)
        # Приватное числовое поле
        self.__numeric_field = numeric_field

    # Метод доступа к числовому полю через метод класса
    def get_numeric_field(self):
        return self.__numeric_field

    # Метод для присваивания значения числовому полю
    def set_numeric_field(self):
        try:
            # Валидация данных
            new_numeric = float(input("Введите числовое значение: "))
            self.__numeric_field = new_numeric
        except ValueError as e:
            print(f"Ошибка ввода данных: {e}")


# Пример использования:

# Создание объекта главного класса с передачей текстового аргумента
main_obj = MainClass("Initial Text")

# Вывод текущего значения текстового поля
print(main_obj.get_text_field())

# Изменение текстового поля с использованием метода без аргументов
main_obj.set_text_field()
print(main_obj.get_text_field())

# Изменение текстового поля с использованием метода с текстовым аргументом
main_obj.set_text_field_with_argument("New Text")
print(main_obj.get_text_field())

# Создание объекта класса-потомка с передачей текстового и числового аргументов
sub_obj = SubClass("Sub Text", 42)

# Вывод текущих значений текстового и числового полей класса-потомка
print(sub_obj.get_text_field())
print(sub_obj.get_numeric_field())
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1: Главный класс MainClass
'''
# Главный класс
class MainClass:
    def __init__(self, text_field):
        # Приватные атрибуты
        self.__text_field = text_field
'''
class MainClass:: Определение нового класса с именем MainClass.
def __init__(self, text_field):: Определение метода __init__, который является конструктором класса и вызывается при 
создании объекта. self указывает на экземпляр класса.
self.__text_field = text_field: Создание приватного атрибута __text_field и его инициализация значением, переданным 
при создании объекта.
'''
'''
Шаг №2: Методы класса MainClass
'''
# Метод для присваивания значения текстовому полю (без аргументов)
def set_text_field(self):
    try:
        # Валидация данных
        new_text = input("Введите текст: ")
        if not new_text:
            raise ValueError("Текст не может быть пустым.")
        self.__text_field = new_text
    except ValueError as e:
        print(f"Ошибка ввода данных: {e}")
'''
def set_text_field(self):: Определение метода set_text_field, который позволяет изменить значение текстового поля без
передачи аргумента.
try: ... except ValueError as e: ...: Использование конструкции для обработки возможных ошибок ввода данных.
new_text = input("Введите текст: "): Запрос ввода текста от пользователя.
if not new_text: raise ValueError("Текст не может быть пустым."): Проверка, что введенный текст не пустой.
self.__text_field = new_text: Присвоение нового значения текстовому полю.
'''
'''
Шаг №3: Методы класса MainClass (продолжение)
'''
# Метод для присваивания значения текстовому полю (с текстовым аргументом)
def set_text_field_with_argument(self, text):
    try:
        # Валидация данных
        if not text:
            raise ValueError("Текст не может быть пустым.")
        self.__text_field = text
    except ValueError as e:
        print(f"Ошибка ввода данных: {e}")
'''
def set_text_field_with_argument(self, text):: Определение метода set_text_field_with_argument,
который позволяет изменить значение текстового поля с передачей текстового аргумента.
if not text: raise ValueError("Текст не может быть пустым."): Проверка, что переданный текст не пустой.
self.__text_field = text: Присвоение нового значения текстовому полю.
'''
'''
Шаг №4: Метод доступа к текстовому полю
'''
# Метод доступа к текстовому полю через метод класса
def get_text_field(self):
    return self.__text_field
'''
def get_text_field(self):: Определение метода get_text_field, который возвращает значение текстового поля.
'''
'''
Шаг №5: Класс-потомок SubClass
'''
# Класс-потомок
class SubClass(MainClass):
    def __init__(self, text_field, numeric_field):
        # Вызов конструктора родительского класса
        super().__init__(text_field)
        # Приватное числовое поле
        self.__numeric_field = numeric_field
'''
class SubClass(MainClass):: Определение нового класса-потомка SubClass, наследующегося от MainClass.
def __init__(self, text_field, numeric_field):: Определение конструктора класса-потомка с двумя аргументами.
super().__init__(text_field): Вызов конструктора родительского класса для инициализации текстового поля.
self.__numeric_field = numeric_field: Создание приватного числового атрибута и его инициализация переданным значением.
'''
'''
Шаг №6: Методы класса SubClass
'''
# Метод доступа к числовому полю через метод класса
def get_numeric_field(self):
    return self.__numeric_field
# Метод для присваивания значения числовому полю
def set_numeric_field(self):
    try:
        # Валидация данных
        new_numeric = float(input("Введите числовое значение: "))
        self.__numeric_field = new_numeric
    except ValueError as e:
        print(f"Ошибка ввода данных: {e}")
'''
def get_numeric_field(self):: Метод для доступа к числовому полю.
def set_numeric_field(self):: Метод для изменения числового поля с вводом нового значения и валидацией данных.
'''
'''
Шаг №7: Пример использования
'''
# Пример использования:

# Создание объекта главного класса с передачей текстового аргумента
main_obj = MainClass("Initial Text")

# Вывод текущего значения текстового поля
print(main_obj.get_text_field())

# Изменение текстового поля с использованием метода без аргументов
main_obj.set_text_field()
print(main_obj.get_text_field())

# Изменение текстового поля с использованием метода с текстовым аргументом
main_obj.set_text_field_with_argument("New Text")
print(main_obj.get_text_field())

# Создание объекта класса-потомка с передачей текстового и числового аргументов
sub_obj = SubClass("Sub Text", 42)

# Вывод текущих значений текстового и числового полей класса-потомка
print(sub_obj.get_text_field())
print(sub_obj.get_numeric_field())
'''
Этот код как мне кажется демонстрирует создание объектов классов MainClass и SubClass,
изменение их полей и вывод текущих значений. При этом использованы концепции ООП, такие как наследование,
инкапсуляция и полиморфизм.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #


