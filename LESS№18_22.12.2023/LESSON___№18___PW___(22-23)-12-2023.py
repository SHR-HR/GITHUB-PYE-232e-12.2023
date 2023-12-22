# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
""""
Дата выполнения практической работы: 22-23 - ДЕКАБРЯ 2023
""""
'''
Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
Дисциплина: Основы программирования на Python
'''
'''
Урок от 22.12.2023
Практическая работа №18: ООП. Полиморфизм
'''
'''
Выполните следующие задания: # ЕСЛИ ХОТИТЕ ТО СРАЗУ ПЕРЕХОДИТЕ НА 1120 СТРОЧКУ
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''' # ЕСЛИ ХОТИТЕ ТО СРАЗУ ПЕРЕХОДИТЕ НА 1120 СТРОЧКУ
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Задание № 1

В качестве практической работы попробуйте самостоятельно перегрузить оператор сложения.

Для его перегрузки используется метод __add__(). 
Он вызывается, когда объекты класса, имеющего данный метод, фигурируют в операции сложения, причем с левой стороны.
Это значит, что в выражении a + b у объекта a должен быть метод __add__().
Объект b может быть чем угодно, но чаще всего он бывает объектом того же класса. 
Объект b будет автоматически передаваться в метод __add__() в качестве второго аргумента (первый – self).

Отметим, в Python также есть правосторонний метод перегрузки сложения - __radd__().
Согласно полиморфизму ООП, возвращать метод __add__() может что угодно. 
Может вообще ничего не возвращать, а "молча" вносить изменения в какие-то уже существующие объекты. 
Допустим, в вашей программе метод перегрузки сложения будет возвращать новый объект того же класса.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Задания №2

Пересмотрите алгоритм решения прошлой практической работы, с использованием инкапсуляции.
Реализуйте старый алгоритм с использованием полиморфизма.

Написать программу, в которой есть главный класс Games со статическим полем Year, опишите конструктор присваивающий
значение полю Year, также опишите метод getName, который возвращает имя игры. На основе главного класса путем 
наследования опишите четыре класса PCGames, PS4Games, XboxGames, MobileGames. Добавьте каждому классу дополнительные 
поля и переопределите у всех классов метод getName.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Задания №3

Пересмотрите алгоритм решения прошлой практической работы, с использованием инкапсуляции.
Реализуйте старый алгоритм с использованием полиморфизма.

Напишите программу с пустым классом Country. Опишите наследуемые от класса Country классы Russia, Canada, Germany.
Добавьте каждому классу поле population и опишите метод setPopulation и getPopulation.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание № 1 - Вариант № 1
'''
class MyClass:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, MyClass):
            # Если other того же класса, создаем новый объект с суммой значений
            new_value = self.value + other.value
            return MyClass(new_value)
        else:
            # Иначе выводим сообщение об ошибке
            print("Нельзя сложить объекты разных классов")

# Создаем два объекта
obj1 = MyClass(5)
obj2 = MyClass(10)

# Пробуем сложить их
result = obj1 + obj2

# Выводим результат
print(result.value)  # Выведет: 15
'''
Пояснение:

В данном примере при сложении объектов класса MyClass создается новый объект с атрибутом value, равным сумме 
значений атрибута value слагаемых объектов. Обратите внимание на использование метода isinstance, чтобы убедиться,
что второй операнд того же класса.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1. Определение класса MyClass и его конструктора (__init__):
'''
class MyClass:
    def __init__(self, value):
        self.value = value
'''
Описание:

MyClass - это определение класса, который мы создаем.
__init__ - это конструктор класса, который вызывается при создании нового объекта. Он принимает два аргумента: 
self (представляющий создаваемый объект) и value (значение, которое будет установлено в атрибут value объекта).
'''
'''
Шаг №2. Перегрузка оператора сложения (__add__):
'''
def __add__(self, other):
    if isinstance(other, MyClass):
        new_value = self.value + other.value
        return MyClass(new_value)
    else:
        print("Нельзя сложить объекты разных классов")
'''
Описание:

__add__ - это метод, который перегружает оператор сложения (+). 
Он принимает два аргумента: self (представляющий вызываемый объект) и other (другой объект, с которым выполняется
сложение).
Внутри метода проверяется, является ли other объектом того же класса (MyClass).
Если да, то создается новый объект класса MyClass с атрибутом value, равным сумме значений атрибута value текущего
и переданного объектов. Этот новый объект затем возвращается.
Если other не принадлежит к классу MyClass, выводится сообщение об ошибке.
'''
'''
Шаг №3. Создание объектов и использование перегруженного оператора сложения:
'''
# Создаем два объекта
obj1 = MyClass(5)
obj2 = MyClass(10)
# Пробуем сложить их
result = obj1 + obj2
# Выводим результат
print(result.value)  # Выведет: 15
'''
Описание:

Создаются два объекта класса MyClass с атрибутами value равными 5 и 10 соответственно.
Оператор сложения + применяется к объектам obj1 и obj2. Так как мы перегрузили оператор сложения для класса MyClass,
вызывается метод __add__.
Метод __add__ выполняет сложение значений атрибута value двух объектов и создает новый объект с результатом.
Результат выводится на экран, и он равен 15, что является суммой значений атрибутов объектов obj1 и obj2.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание № 1 - Вариант № 2
'''
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            # Если other тоже объект класса Vector, создаем новый объект Vector
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Vector(new_x, new_y)
        else:
            # Иначе выводим сообщение об ошибке
            print("Нельзя сложить объекты разных классов")

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Пример использования
v1 = Vector(1, 2)
v2 = Vector(3, 4)

# Перегрузка оператора сложения
result_vector = v1 + v2

# Вывод результата
print(result_vector)  # Выведет: Vector(4, 6)
'''
Пояснение:

В этом примере создается класс Vector для представления двумерных векторов.
Метод __add__ перегружает оператор сложения так, что он создает новый объект Vector,
содержащий сумму соответствующих координат. Метод __str__ используется для определения строкового представления
объекта Vector при его выводе.

Этот код так-же демонстрирует, как перегрузить оператор сложения для конкретного класса
(в данном случае, для векторов), что позволяет более естественно и интуитивно использовать операцию сложения
для объектов этого класса.
'''
'''
Шаг №1. Определение класса Vector и его конструктора (__init__):
'''
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
'''
Описание:

Vector - это класс, представляющий двумерные векторы.
__init__ - конструктор класса, который вызывается при создании нового объекта. 
Принимает три аргумента: self (представляющий создаваемый объект), x и y (координаты вектора).
'''
'''
Шаг №2. Перегрузка оператора сложения (__add__):
'''
def __add__(self, other):
    if isinstance(other, Vector):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)
    else:
        print("Нельзя сложить объекты разных классов")
'''
Описание:

__add__ - метод, который перегружает оператор сложения (+). 
Принимает два аргумента: self (текущий объект) и other (другой объект, с которым выполняется сложение).
Проверяет, является ли other объектом того же класса (Vector). Если да, то создает новый объект Vector с координатами,
равными сумме соответствующих координат текущего и переданного объектов. Этот новый объект затем возвращается.
Если other не принадлежит к классу Vector, выводится сообщение об ошибке.
'''
'''
Шаг №3. Метод для строкового представления объекта (__str__):
'''
def __str__(self):
    return f"Vector({self.x}, {self.y})"
'''
Описание:

__str__ - метод, который возвращает строковое представление объекта при вызове функции str().
В данном случае, он возвращает строку, представляющую объект Vector в виде "Vector(x, y)".
'''
'''
Шаг №4. Пример использования класса:
'''
# Пример использования
v1 = Vector(1, 2)
v2 = Vector(3, 4)

# Перегрузка оператора сложения
result_vector = v1 + v2

# Вывод результата
print(result_vector)  # Выведет: Vector(4, 6)
'''
Описание:

Создаются два объекта класса Vector с координатами (1, 2) и (3, 4).
Оператор сложения + применяется к объектам v1 и v2. Так как мы перегрузили оператор сложения для класса Vector,
вызывается метод __add__.
Метод __add__ создает новый объект Vector с координатами (4, 6) (сумма соответствующих координат v1 и v2).
Результат выводится на экран с использованием метода __str__.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание № 1 - Вариант № 3
'''
class MyClass:
    """Пример класса с перегруженным оператором сложения."""

    def __init__(self, value):
        """Инициализация объекта."""
        self.value = value

    def __add__(self, other):
        """Перегрузка оператора сложения."""
        try:
            if isinstance(other, MyClass):
                new_value = self.value + other.value
                return MyClass(new_value)
        except AttributeError:
            pass
        return None

    def __str__(self):
        """Строковое представление объекта."""
        return f"MyClass({self.value})"
'''
Пояснение:

В этом коде try блок используется для выполнения операции сложения, а except блок будет выполнен в случае,
если произойдет исключение (например, AttributeError, если other не имеет атрибута value).

Однако, как говорит GOOGLE стоит помнить, что использование try и except для контроля логики программы,
а не для обработки исключений, может сделать код менее предсказуемым и сложным для отладки.
Поэтому лучше использовать такие конструкции с осторожностью и в ситуациях,
где они действительно улучшают читаемость и логику кода.
'''
'''
Шаг №1. Инициализация объекта:
'''
def __init__(self, value):
    self.value = value
'''
Описание:

Название: __init__ - это конструктор класса, который вызывается при создании нового объекта.
Выполнение функции: Метод инициализирует атрибут value объекта значением, переданным при создании объекта.
'''
'''
Шаг №2. Перегрузка оператора сложения:
'''
def __add__(self, other):
    try:
        if isinstance(other, MyClass):
            new_value = self.value + other.value
            return MyClass(new_value)
    except AttributeError:
        pass
    return None
'''
Описание:

Название: __add__ - перегружает оператор сложения (+).

Выполнение функции:
В блоке try, проверяется, является ли other объектом класса MyClass.
Если это так, то создается новый объект MyClass с атрибутом value, равным сумме значений атрибутов value текущего и
переданного объектов.
В блоке except AttributeError, обрабатывается случай, если у объекта other нет атрибута value.
Возвращается новый объект MyClass или None, если other не является объектом MyClass.
'''
'''
Шаг №3. Строковое представление объекта:
'''
def __str__(self):
    return f"MyClass({self.value})"
'''
Описание:

Название: __str__ - возвращает строковое представление объекта.
Выполнение функции: Возвращает строку, представляющую объект MyClass в формате "MyClass(value)".

Эти методы совместно обеспечивают функциональность класса MyClass для инициализации, сложения с другими объектами
того же класса и предоставления строкового представления объекта.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание № 1 - Вариант № - "уже пошел далеко в дебри" (наверное)
'''
class MyNumber:
    """Класс, представляющий числовое значение."""

    def __init__(self, value):
        """Инициализация объекта."""
        self.value = value

    def __add__(self, other):
        """Перегрузка оператора сложения."""
        if isinstance(other, MyNumber):
            # Создаем новый объект MyNumber с суммой значений
            return MyNumber(self.value + other.value)
        else:
            # Если объект other не является MyNumber, возвращаем None
            return None

    def __radd__(self, other):
        """Правосторонняя перегрузка оператора сложения."""
        # В данном примере правосторонняя перегрузка идентична левосторонней
        return self.__add__(other)

    def __str__(self):
        """Строковое представление объекта."""
        return f"MyNumber({self.value})"


# Пример использования
a = MyNumber(5)
b = MyNumber(10)

# Левосторонняя перегрузка оператора сложения (a + b)
result1 = a + b
print(result1)  # Выведет: MyNumber(15)

# Правосторонняя перегрузка оператора сложения (10 + a)
result2 = 10 + a
print(result2)  # Выведет: MyNumber(15)
'''
Пояснение:

В этом коде класс MyNumber представляет числовое значение.
Метод __add__ перегружает оператор сложения, создавая новый объект MyNumber с суммой значений.
Метод __radd__ обеспечивает правостороннюю перегрузку оператора сложения.

Пример использования демонстрирует, как объекты класса могут использоваться в операции сложения,
как с левой, так и с правой стороны.
'''
'''
Шаг №1. Инициализация объекта:

Пример кода:
'''
def __init__(self, value):
    self.value = value
'''
Описание:

Название: __init__ - это конструктор класса, который вызывается при создании нового объекта.
Выполнение функции: Метод инициализирует атрибут value объекта значением, переданным при создании объекта.
'''
'''
Шаг №2. Перегрузка оператора сложения:

Пример кода:
'''
def __add__(self, other):
    if isinstance(other, MyNumber):
        return MyNumber(self.value + other.value)
    else:
        return None
'''
Описание:

Название: __add__ - перегружает оператор сложения (+).
Выполнение функции:
Проверяется, является ли other объектом класса MyNumber.
Если это так, то создается новый объект MyNumber с атрибутом value, равным сумме значений атрибутов value текущего
и переданного объектов.
Если other не является объектом MyNumber, возвращается None.
'''
'''
Шаг №3. Правосторонняя перегрузка оператора сложения:

Пример кода:
'''
def __radd__(self, other):
    return self.__add__(other)
'''
Описание:

Название: __radd__ - перегружает правосторонний оператор сложения (+).
Выполнение функции:
В данном примере правосторонняя перегрузка просто вызывает метод __add__, обеспечивая симметричность операции сложения.
'''
'''
Шаг №4. Строковое представление объекта:

Пример кода:
'''
def __str__(self):
    return f"MyNumber({self.value})"
'''
Описание:

Название: __str__ - возвращает строковое представление объекта.
Выполнение функции: Возвращает строку, представляющую объект MyNumber в формате "MyNumber(value)".
'''
'''
Эти методы совместно обеспечивают функциональность класса MyNumber для инициализации, сложения с другими 
объектами того же класса и предоставления строкового представления объекта.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание № 2 - Вариант № 1
'''
class Games:
    Year = 0  # Статическое поле

    def __init__(self, year, name, rating=0, players=1):
        if players < 1:
            raise ValueError("Players must be at least 1")
        self.__year = year  # Приватное поле
        self.__name = name
        self.__rating = rating
        self.__players = players

    def get_name(self):
        return self.__name

    def get_year(self):
        return self.__year

    def get_rating(self):
        return self.__rating

    def get_players(self):
        return self.__players


class PCGames(Games):
    def __init__(self, year, name, platform, rating=0, players=1):
        super().__init__(year, name, rating, players)
        self.__platform = platform

    def get_name(self):
        return f"{self.__name} (PC)"

    def get_platform(self):
        return self.__platform


class PS4Games(Games):
    def __init__(self, year, name, exclusive_title, rating=0, players=1):
        super().__init__(year, name, rating, players)
        self.__exclusive_title = exclusive_title

    def get_name(self):
        return f"{self.__name} (PS4 Exclusive)"


class XboxGames(Games):
    def __init__(self, year, name, online_multiplayer, rating=0, players=1):
        super().__init__(year, name, rating, players)
        self.__online_multiplayer = online_multiplayer

    def get_name(self):
        return f"{self.__name} (Xbox)"


class MobileGames(Games):
    def __init__(self, year, name, genre, rating=0, players=1):
        super().__init__(year, name, rating, players)
        self.__genre = genre

    def get_name(self):
        return f"{self.__name} (Mobile)"


class NintendoSwitchGames(Games):
    def __init__(self, year, name, exclusive_title, portable_mode=False, rating=0, players=1):
        super().__init__(year, name, rating, players)
        self.__exclusive_title = exclusive_title
        self.__portable_mode = portable_mode

    def get_name(self):
        return f"{self.__name} (Nintendo Switch)"

    def is_portable(self):
        return self.__portable_mode


# Добавим метод для сортировки списка игр по году выпуска
def sort_games_by_year(games_list):
    return sorted(games_list, key=lambda x: x.get_year())


# Пример использования с играми 2022 и 2023 годов, онлайн-шутерами и Diablo IV
games_list = [
    PCGames(2022, "Cyberpunk 2077", "Windows", 9.0, 1),
    PS4Games(2022, "Horizon Forbidden West", True),
    XboxGames(2022, "Starfield", True),
    MobileGames(2023, "Elden Ring", "Action RPG", 9.5, 1),
    PCGames(2023, "Diablo IV", "Windows", 9.8, 1),
    PCGames(2022, "Battlefield 2042", "Windows", 8.5, 64),
    PS4Games(2022, "Call of Duty: Vanguard", True),
    XboxGames(2023, "Halo Infinite", True),
    MobileGames(2023, "PUBG: New State", "Battle Royale", 8.0, 100),
    NintendoSwitchGames(2022, "Metroid Prime 4", True, True),
]

# Обработка ошибок при создании объектов
try:
    invalid_game = PCGames(2023, "Invalid Game", "Windows", 9.5, -5)
except ValueError as e:
    print(f"Error: {e}")

# Сортировка и вывод списка игр
sorted_games = sort_games_by_year(games_list)
for game in sorted_games:
    print(f"Year: {game.get_year()}, Name: {game.get_name()}, Rating: {game.get_rating()}, Players: {game.get_players()},"
          f" Platform: {getattr(game, 'get_platform', lambda: '')()}, Portable: {getattr(game,
                                                                                         'is_portable', lambda: '')()}")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг 1: Создание базового класса Games
'''
class Games:
    Year = 0  # Статическое поле

    def __init__(self, year, name, rating=0, players=1):
        if players < 1:
            raise ValueError("Players must be at least 1")
        self.__year = year  # Приватное поле
        self.__name = name
        self.__rating = rating
        self.__players = players

    def get_name(self):
        return self.__name

    def get_year(self):
        return self.__year

    def get_rating(self):
        return self.__rating

    def get_players(self):
        return self.__players
'''
Объяснение:

class Games - это базовый класс для всех игр. В нем определены основные свойства и методы, которые будут общими для
всех подклассов.
Year - это статическое поле класса, которое общее для всех экземпляров класса и доступное через класс,
а не через объект.
__init__ - конструктор класса, инициализирующий основные свойства (год, имя, рейтинг, количество игроков).
Проверка if players < 1 используется для гарантии, что количество игроков не меньше 1.
Методы get_name, get_year, get_rating, get_players используются для получения соответствующих свойств.
'''
'''
Шаг 2: Создание подклассов
'''
class PCGames(Games):
    def __init__(self, year, name, platform, rating=0, players=1):
        super().__init__(year, name, rating, players)
        self.__platform = platform

    def get_name(self):
        return f"{self.__name} (PC)"

    def get_platform(self):
        return self.__platform
'''
Объяснение:

class PCGames(Games) - это подкласс, который наследует все свойства и методы от базового класса Games.
super().__init__ - вызов конструктора родительского класса (Games) для инициализации общих свойств.
get_name - переопределенный метод, который добавляет к имени игры информацию о платформе.
Аналогично создаются и остальные подклассы (PS4Games, XboxGames, MobileGames, NintendoSwitchGames),
каждый из которых имеет свои дополнительные поля и переопределение метода get_name.
'''
'''
Шаг 3: Добавление метода для сортировки
'''
def sort_games_by_year(games_list):
    return sorted(games_list, key=lambda x: x.get_year())
'''
Объяснение:

sort_games_by_year - это функция, которая принимает список игр и возвращает его, отсортированный по году выпуска с
использованием метода get_year. Здесь используется встроенная функция sorted, которая сортирует элементы на основе
заданного ключа (в данном случае, метода get_year).
'''
'''
Шаг 4: Пример использования
'''
games_list = [
    PCGames(2022, "Cyberpunk 2077", "Windows", 9.0, 1),
    PS4Games(2022, "Horizon Forbidden West", True),
    XboxGames(2022, "Starfield", True),
    MobileGames(2023, "Elden Ring", "Action RPG", 9.5, 1),
    PCGames(2023, "Diablo IV", "Windows", 9.8, 1),
    PCGames(2022, "Battlefield 2042", "Windows", 8.5, 64),
    PS4Games(2022, "Call of Duty: Vanguard", True),
    XboxGames(2023, "Halo Infinite", True),
    MobileGames(2023, "PUBG: New State", "Battle Royale", 8.0, 100),
    NintendoSwitchGames(2022, "Metroid Prime 4", True, True),
]

# Обработка ошибок при создании объектов
try:
    invalid_game = PCGames(2023, "Invalid Game", "Windows", 9.5, -5)
except ValueError as e:
    print(f"Error: {e}")

# Сортировка и вывод списка игр
sorted_games = sort_games_by_year(games_list)
for game in sorted_games:
    print(f"Year: {game.get_year()}, Name: {game.get_name()}, Rating: {game.get_rating()}, Players: {game.get_players()},"
          f" Platform: {getattr(game, 'get_platform', lambda: '')()}")
'''
Объяснение:

games_list - это список объектов различных типов игр, созданных с использованием подклассов.
Обработка ошибок демонстрирует, как можно обрабатывать исключения при создании объектов с недопустимыми значениями.
Список игр сортируется по году выпуска и выводится информация о каждой игре с использованием методов объектов.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание № 2 - Вариант № 2
'''
class Games:
    Year = 0

    def __init__(self, year, name, rating=0, players=1):
        if players < 1:
            raise ValueError("Players must be at least 1")
        self.__year = year
        self.__name = name
        self.__rating = rating
        self.__players = players

    def get_name(self):
        return self.__name

    def get_year(self):
        return self.__year

    def get_rating(self):
        return self.__rating

    def get_players(self):
        return self.__players


class PS5Games(Games):
    def __init__(self, year, name, exclusive_title, ray_tracing_enabled=False, rating=0, players=1):
        super().__init__(year, name, rating, players)
        self.__exclusive_title = exclusive_title
        self.__ray_tracing_enabled = ray_tracing_enabled

    def get_name(self):
        return f"{super().get_name()} (PS5 Exclusive)"

    def is_ray_tracing_enabled(self):
        return self.__ray_tracing_enabled


class XboxSeriesXGames(Games):
    def __init__(self, year, name, online_multiplayer, game_pass_available=False,
                 smart_delivery_supported=False, rating=0, players=1):
        super().__init__(year, name, rating, players)
        self.__online_multiplayer = online_multiplayer
        self.__game_pass_available = game_pass_available
        self.__smart_delivery_supported = smart_delivery_supported

        if (not isinstance(online_multiplayer, bool) or not isinstance(game_pass_available, bool) or
                not isinstance(smart_delivery_supported, bool)):
            raise ValueError("Invalid input for boolean fields")

    def get_name(self):
        return f"{super().get_name()} (Xbox Series X)"

    def is_game_pass_available(self):
        return self.__game_pass_available

    def is_smart_delivery_supported(self):
        return self.__smart_delivery_supported


class ActionRPGGames(Games):
    def __init__(self, year, name, single_player=True, open_world=True, rating=0, players=1):
        super().__init__(year, name, rating, players)
        self.__single_player = single_player
        self.__open_world = open_world

    def get_name(self):
        return f"{super().get_name()} (Action RPG)"

    def is_single_player(self):
        return self.__single_player

    def is_open_world(self):
        return self.__open_world


class StrategyGames(Games):
    def __init__(self, year, name, single_player=True, multiplayer=True, rating=0, players=1):
        super().__init__(year, name, rating, players)
        self.__single_player = single_player
        self.__multiplayer = multiplayer

    def get_name(self):
        return f"{super().get_name()} (Strategy)"

    def is_single_player(self):
        return self.__single_player

    def is_multiplayer(self):
        return self.__multiplayer


class PCGames(Games):
    def __init__(self, year, name, operating_system, rating=0, players=1):
        super().__init__(year, name, rating, players)
        self.__operating_system = operating_system

    def get_name(self):
        return f"{super().get_name()} (PC)"

    def get_platform(self):
        return "PC"

    def is_portable(self):
        return False


class PS4Games(Games):
    def __init__(self, year, name, exclusive_title, rating=0, players=1):
        super().__init__(year, name, rating, players)
        self.__exclusive_title = exclusive_title

    def get_name(self):
        return f"{super().get_name()} (PS4 Exclusive)"

    def get_platform(self):
        return "PS4"

    def is_portable(self):
        return False


class XboxGames(Games):
    def __init__(self, year, name, online_multiplayer, rating=0, players=1):
        super().__init__(year, name, rating, players)
        self.__online_multiplayer = online_multiplayer

    def get_name(self):
        return f"{super().get_name()} (Xbox)"

    def get_platform(self):
        return "Xbox"

    def is_portable(self):
        return False


class MobileGames(Games):
    def __init__(self, year, name, genre, rating=0, players=1):
        super().__init__(year, name, rating, players)
        self.__genre = genre

    def get_name(self):
        return f"{super().get_name()} (Mobile)"

    def get_platform(self):
        return "Mobile"

    def is_portable(self):
        return True


class NintendoSwitchGames(Games):
    def __init__(self, year, name, exclusive_title, rating=0, players=1):
        super().__init__(year, name, rating, players)
        self.__exclusive_title = exclusive_title

    def get_name(self):
        return f"{super().get_name()} (Nintendo Switch Exclusive)"

    def get_platform(self):
        return "Nintendo Switch"

    def is_portable(self):
        return True


# Создание экземпляров игр для демонстрации
games_list = [
    PCGames(2022, "Cyberpunk 2077", "Windows", 9.0, 1),
    PS4Games(2022, "Horizon Forbidden West", True),
    XboxGames(2022, "Starfield", True),
    MobileGames(2023, "Elden Ring", "Action RPG", 9.5, 1),
    PCGames(2023, "Diablo IV", "Windows", 9.8, 1),
    PS5Games(2022, "Ratchet & Clank: Rift Apart", True, True),
    XboxSeriesXGames(2023, "Fable", True, True),
    MobileGames(2023, "PUBG: New State", "Battle Royale", 8.0, 100),
    NintendoSwitchGames(2022, "Metroid Prime 4", True, True),
    ActionRPGGames(2022, "The Witcher 4", True, True),
    StrategyGames(2023, "Civilization VI", True, True),
]

# Вывод информации о каждой игре
for game in games_list:
    print(f"Year: {game.get_year()}, Name: {game.get_name()}, Rating: {game.get_rating()}, Players: {game.get_players()}")
    if isinstance(game, PS5Games):
        print(f"Ray Tracing Enabled: {game.is_ray_tracing_enabled()}")
    elif isinstance(game, XboxSeriesXGames):
        print(f"Game Pass Available: {game.is_game_pass_available()}, Smart Delivery Supported: {game.is_smart_delivery_supported()}")
    elif isinstance(game, ActionRPGGames):
        print(f"Single Player: {game.is_single_player()}, Open World: {game.is_open_world()}")
    elif isinstance(game, StrategyGames):
        print(f"Single Player: {game.is_single_player()}, Multiplayer: {game.is_multiplayer()}")
    print()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг 1: Создание базового класса Games
'''
class Games:
    Year = 0

    def __init__(self, year, name, rating=0, players=1):
        if players < 1:
            raise ValueError("Players must be at least 1")
        self.__year = year
        self.__name = name
        self.__rating = rating
        self.__players = players

    def get_name(self):
        return self.__name

    def get_year(self):
        return self.__year

    def get_rating(self):
        return self.__rating

    def get_players(self):
        return self.__players
'''
Описание:

Создается базовый класс Games, который содержит статическое поле Year.
Конструктор принимает год, название игры, рейтинг и количество игроков.
Реализованы методы get_name, get_year, get_rating, get_players для получения соответствующих свойств.
'''
'''
Шаг №2: Создание подклассов для различных типов игр и платформ
'''
# Пример подкласса
class PS5Games(Games):
    def __init__(self, year, name, exclusive_title, ray_tracing_enabled=False, rating=0, players=1):
        super().__init__(year, name, rating, players)
        self.__exclusive_title = exclusive_title
        self.__ray_tracing_enabled = ray_tracing_enabled

    def get_name(self):
        return f"{super().get_name()} (PS5 Exclusive)"

    def is_ray_tracing_enabled(self):
        return self.__ray_tracing_enabled
'''
Описание:

Создаются подклассы, представляющие различные платформы и типы игр (PS5Games, XboxSeriesXGames, ActionRPGGames,
StrategyGames, и др.).
В каждом подклассе добавляются дополнительные поля, специфичные для этого типа игры или платформы.
Переопределяется метод get_name для возвращения уникального названия игры, основанного на базовом названии и типе.
'''
'''
Шаг №3: Создание экземпляров игр и вывод информации
'''
# Создание экземпляров игр для демонстрации
games_list = [
    PCGames(2022, "Cyberpunk 2077", "Windows", 9.0, 1),
    PS4Games(2022, "Horizon Forbidden West", True),
    XboxGames(2022, "Starfield", True),
    MobileGames(2023, "Elden Ring", "Action RPG", 9.5, 1),
    PCGames(2023, "Diablo IV", "Windows", 9.8, 1),
    PS5Games(2022, "Ratchet & Clank: Rift Apart", True, True),
    XboxSeriesXGames(2023, "Fable", True, True),
    MobileGames(2023, "PUBG: New State", "Battle Royale", 8.0, 100),
    NintendoSwitchGames(2022, "Metroid Prime 4", True, True),
    ActionRPGGames(2022, "The Witcher 4", True, True),
    StrategyGames(2023, "Civilization VI", True, True),
]

# Вывод информации о каждой игре
for game in games_list:
    print(f"Year: {game.get_year()}, Name: {game.get_name()}, Rating: {game.get_rating()}, Players: {game.get_players()}")
    if isinstance(game, PS5Games):
        print(f"Ray Tracing Enabled: {game.is_ray_tracing_enabled()}")
    elif isinstance(game, XboxSeriesXGames):
        print(f"Game Pass Available: {game.is_game_pass_available()}, Smart Delivery Supported: {game.is_smart_delivery_supported()}")
    elif isinstance(game, ActionRPGGames):
        print(f"Single Player: {game.is_single_player()}, Open World: {game.is_open_world()}")
    elif isinstance(game, StrategyGames):
        print(f"Single Player: {game.is_single_player()}, Multiplayer: {game.is_multiplayer()}")
    print()
'''
Описание:

Создаются экземпляры различных игр с использованием созданных классов.
Выводится информация о каждой игре, используя методы классов.
Используется проверка типов для вывода дополнительной информации, специфичной для каждого типа игры или платформы.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
'''
Задание № 3 - Вариант № 1
'''
class Country:
    def __init__(self):
        self._population = None

    def set_population(self, population):
        if population >= 0:
            self._population = population
        else:
            print("Население не может быть отрицательным.")

    def get_population(self):
        return self._population


class Russia(Country):
    def __init__(self):
        super().__init__()  # Вызывает конструктор родительского класса
        self._name = "Russia"  # Добавляет поле _name для хранения имени страны

    # Добавляет геттер и сеттер для имени страны
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


class Canada(Country):
    def __init__(self):
        super().__init__()
        self._name = "Canada"

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


class Germany(Country):
    def __init__(self):
        super().__init__()
        self._name = "Germany"

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


# Пример использования
russia = Russia()
russia.set_population(145000000000000)
print(f"{russia.get_name()} population: {russia.get_population()}")
# Вывод: Russia population: 145000000000000

canada = Canada()
canada.set_population(380000)
print(f"{canada.get_name()} population: {canada.get_population()}")
# Вывод: Canada population: 380000

germany = Germany()
germany.set_population(830000)
print(f"{germany.get_name()} population: {germany.get_population()}")
# Вывод: Germany population: 830000
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Определение базового класса Country:
'''
class Country:
    def __init__(self):
        self._population = None

    def set_population(self, population):
        if population >= 0:
            self._population = population
        else:
            print("Население не может быть отрицательным.")

    def get_population(self):
        return self._population
'''
Разбор базового класса Country:
__init__ метод: Инициализирует объект страны. В этом примере, устанавливается пустое значение для _population.

set_population метод: Позволяет установить значение населения для страны. Проверяет, что население неотрицательно.
Если передано отрицательное значение, выводит сообщение об ошибке.

get_population метод: Возвращает текущее значение населения страны.
'''
'''
Определение класса Russia:
'''
class Russia(Country):
    def __init__(self):
        super().__init__()  # Вызывает конструктор родительского класса
        self._name = "Russia"  # Добавляет поле _name для хранения имени страны

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
'''
Разбор класса Russia:
__init__ метод: Инициализирует объект класса Russia. Вызывает конструктор родительского класса Country.
Добавляет поле _name для хранения имени страны и устанавливает его значение по умолчанию как "Russia".

get_name метод: Возвращает текущее значение имени страны.

set_name метод: Позволяет установить новое значение для имени страны.
'''
'''
Определение класса Canada (аналогично классу Russia):
'''
class Canada(Country):
    def __init__(self):
        super().__init__()
        self._name = "Canada"

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
'''
Определение класса Germany (аналогично классу Russia):
'''
class Germany(Country):
    def __init__(self):
        super().__init__()
        self._name = "Germany"

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
'''
Пример использования:
'''
# Создание объекта Russia
russia = Russia()
russia.set_population(145000000000000)
print(f"{russia.get_name()} population: {russia.get_population()}")
# Вывод: Russia population: 145000000000000

# Создание объекта Canada
canada = Canada()
canada.set_population(380000)
print(f"{canada.get_name()} population: {canada.get_population()}")
# Вывод: Canada population: 380000

# Создание объекта Germany
germany = Germany()
germany.set_population(830000)
print(f"{germany.get_name()} population: {germany.get_population()}")
# Вывод: Germany population: 830000
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''ВСЕ СРАЗУ, СКОПОМ'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Задание №1: Перегрузка оператора сложения

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        # Перегрузка оператора сложения
        if isinstance(other, Number):
            return Number(self.value + other.value)
        else:
            return NotImplemented

    def __str__(self):
        return str(self.value)


a = Number(5)
b = Number(10)
result = a + b
print(result)  # Вывод: 15


# Задание №2: Инкапсуляция и полиморфизм для классов игр

class Games:
    Year = 2023

    def __init__(self, name):
        self._name = name

    def get_name(self):
        # Метод для получения имени игры
        return self._name


class PCGames(Games):
    def __init__(self, name, genre):
        super().__init__(name)
        self._genre = genre

    def get_name(self):
        # Переопределение метода для PCGames
        return f"{self._name} (PC)"


class PS4Games(Games):
    def __init__(self, name, exclusive_title):
        super().__init__(name)
        self._exclusive_title = exclusive_title

    def get_name(self):
        # Переопределение метода для PS4Games
        return f"{self._name} (PS4)"


class XboxGames(Games):
    def __init__(self, name, backward_compatible):
        super().__init__(name)
        self._backward_compatible = backward_compatible

    def get_name(self):
        # Переопределение метода для XboxGames
        return f"{self._name} (Xbox)"


class MobileGames(Games):
    def __init__(self, name, platform):
        super().__init__(name)
        self._platform = platform

    def get_name(self):
        # Переопределение метода для MobileGames
        return f"{self._name} (Mobile)"


# Пример использования
pc_game = PCGames("Cyberpunk 2077", "RPG")
ps4_game = PS4Games("The Last of Us Part II", True)
xbox_game = XboxGames("Halo Infinite", False)
mobile_game = MobileGames("Angry Birds", "iOS")

print(pc_game.get_name())    # Вывод: Cyberpunk 2077 (PC)
print(ps4_game.get_name())   # Вывод: The Last of Us Part II (PS4)
print(xbox_game.get_name())  # Вывод: Halo Infinite (Xbox)
print(mobile_game.get_name())  # Вывод: Angry Birds (Mobile)


# Задание №3: Инкапсуляция и полиморфизм для классов стран

class Country:
    def __init__(self):
        self._population = None

    def set_population(self, population):
        # Метод для установки населения
        if population >= 0:
            self._population = population
        else:
            print("Население не может быть отрицательным.")

    def get_population(self):
        # Метод для получения населения
        return self._population


class Russia(Country):
    def __init__(self):
        super().__init__()
        self._name = "Russia"

    def get_name(self):
        # Переопределение метода для Russia
        return self._name


class Canada(Country):
    def __init__(self):
        super().__init__()
        self._name = "Canada"

    def get_name(self):
        # Переопределение метода для Canada
        return self._name


class Germany(Country):
    def __init__(self):
        super().__init__()
        self._name = "Germany"

    def get_name(self):
        # Переопределение метода для Germany
        return self._name


# Пример использования
russia = Russia()
russia.set_population(145000000000000)
print(f"{russia.get_name()} population: {russia.get_population()}")
# Вывод: Russia population: 145000000000000

canada = Canada()
canada.set_population(380000)
print(f"{canada.get_name()} population: {canada.get_population()}")
# Вывод: Canada population: 380000

germany = Germany()
germany.set_population(830000)
print(f"{germany.get_name()} population: {germany.get_population()}")
# Вывод: Germany population: 830000
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1: Определение класса Number для перегрузки оператора сложения
'''
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value)
        else:
            return NotImplemented

    def __str__(self):
        return str(self.value)
'''
Описание:

Создается класс Number, представляющий объекты с числовыми значениями.
Метод __add__ перегружает оператор сложения (+). Если второй операнд (other) является объектом класса Number,
возвращается новый объект с суммой значений.
Метод __str__ используется для представления объекта в виде строки.
'''
'''
Шаг №2: Пример использования оператора сложения для объектов Number
'''
a = Number(5)
b = Number(10)
result = a + b
print(result)  # Вывод: 15
'''
Описание:

Создаются два объекта класса Number с числовыми значениями 5 и 10.
Используется оператор сложения для объектов a и b.
Результат (объект с числовым значением 15) выводится на экран.
'''
'''
Шаг №3: Определение базового класса Games
'''
class Games:
    Year = 2023

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name
'''
Описание:

Создается базовый класс Games, содержащий статическое поле Year и конструктор для установки имени игры.
Метод get_name возвращает имя игры.
'''
'''
Шаг №4: Определение подклассов PCGames, PS4Games, XboxGames, MobileGames
'''
class PCGames(Games):
    def __init__(self, name, genre):
        super().__init__(name)
        self._genre = genre

    def get_name(self):
        return f"{self._name} (PC)"
'''
Описание:

Создается подкласс PCGames, наследующийся от Games.
Добавляется поле _genre и конструктор для установки имени и жанра игры.
Метод get_name переопределен для возвращения имени игры с указанием платформы (PC).
Аналогичные шаги выполняются для подклассов PS4Games, XboxGames и MobileGames.
'''
'''
Шаг №5: Пример использования классов игр
'''
pc_game = PCGames("Cyberpunk 2077", "RPG")
ps4_game = PS4Games("The Last of Us Part II", True)
xbox_game = XboxGames("Halo Infinite", False)
mobile_game = MobileGames("Angry Birds", "iOS")

print(pc_game.get_name())    # Вывод: Cyberpunk 2077 (PC)
print(ps4_game.get_name())   # Вывод: The Last of Us Part II (PS4)
print(xbox_game.get_name())  # Вывод: Halo Infinite (Xbox)
print(mobile_game.get_name())  # Вывод: Angry Birds (Mobile)
'''
Описание:

Создаются объекты различных классов игр.
Вызываются методы get_name для каждого объекта, выводящие информацию о каждой игре на экран.
'''
'''
Шаг №6: Определение класса Country и его подклассов Russia, Canada, Germany
'''
class Country:
    def __init__(self):
        self._population = None

    def set_population(self, population):
        if population >= 0:
            self._population = population
        else:
            print("Население не может быть отрицательным.")

    def get_population(self):
        return self._population
'''
Описание:

Создается базовый класс Country для представления страны с полем _population и методами для установки и 
получения населения.
Аналогичные шаги выполняются для подклассов Russia, Canada и Germany, которые добавляют поле _name и
переопределяют метод get_name.
'''
'''
Шаг №7: Пример использования классов стран
'''
russia = Russia()
russia.set_population(145000000)
print(f"{russia.get_name()} population: {russia.get_population()}")
# Вывод: Russia population: 145000000

canada = Canada()
canada.set_population(38000000)
print(f"{canada.get_name()} population: {canada.get_population()}")
# Вывод: Canada population: 38000000

germany = Germany()
germany.set_population(83000000)
print(f"{germany.get_name()} population: {germany.get_population()}")
# Вывод: Germany population: 83000000
'''
Описание:

Создаются объекты различных классов стран.
Устанавливается население для каждой страны с использованием метода set_population.
Выводится информация о каждой стране, включая имя и население.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #




