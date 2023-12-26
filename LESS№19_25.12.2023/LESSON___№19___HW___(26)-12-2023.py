# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''  ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓
Дата выполнения ДОМАШНЕЙ РАБОТЫ: 26 - ДЕКАБРЯ 2023
''''  ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓
'''
Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
Дисциплина: Основы программирования на Python
'''
'''
Урок от 25.12.2023
Домашняя работа №19: ООП.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполните следующие задания:   
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание №1

Создайте класс Device, который содержит информацию об устройстве.

С помощью механизма наследования, реализуйте класс CoffeeMachine (содержит информацию о кофемашине),
класс Blender (содержит информацию о блендере), класс MeatGrinder (содержит информацию о мясорубке).

Каждый из классов должен содержать необходимые для работы методы.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание №2

Создайте класс Ship, который содержит информацию о корабле.

С помощью механизма наследования, реализуйте класс Frigate (содержит информацию о фрегате),
класс Destroyer (содержит информацию об эсминце), класс Cruiser (содержит информацию о крейсере).
Каждый из классов должен содержать необходимые для работы методы.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
ООП. Множественное следование
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Выполните следующее задания:
'''
'''
Задание №1

Используя понятие множественного наследования, разработайте класс «Окружность, вписанная в квадрат».
'''
'''
Задание №2

Используя механизм множественного наследования разработайте класс “Автомобиль”.
Должны быть классы «Колеса», «Двигатель», «Двери».
'''
'''
Задание №3

Создайте базовый класс Shape для рисования плоских фигур.

Определите методы:
Show() — вывод на экран информации о фигуре;
Save() — сохранение фигуры в файл;
Load() — считывание фигуры из файла.

Определите производные классы:

Square — квадрат, который характеризуется координатами левого верхнего угла и длиной стороны;
Rectangle — прямоугольник с заданными координатами верхнего левого угла и размерами;
Circle — окружность с заданными координатами центра и радиусом;
Ellipse — эллипс с заданными координатами верхнего угла, описанного вокруг него прямоугольника со сторонами,
параллельными осям координат, и размерами этого прямоугольника.

Создайте список фигур, сохраните фигуры в файл, загрузите в другой список и отобразите информацию о каждой из фигур.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Задание №1 - Создайте класс Device, который содержит информацию об устройстве.
'''
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} is starting")

    def stop(self):
        print(f"{self.brand} {self.model} is stopping")


class CoffeeMachine(Device):
    def __init__(self, brand, model, coffee_type):
        super().__init__(brand, model)
        self.coffee_type = coffee_type

    def make_coffee(self):
        print(f"{self.brand} {self.model} is making {self.coffee_type} coffee")


class Blender(Device):
    def __init__(self, brand, model, speed_levels):
        super().__init__(brand, model)
        self.speed_levels = speed_levels

    def blend(self):
        print(f"{self.brand} {self.model} is blending at {self.speed_levels} speed levels")


class MeatGrinder(Device):
    def __init__(self, brand, model, grind_type):
        super().__init__(brand, model)
        self.grind_type = grind_type

    def grind_meat(self):
        print(f"{self.brand} {self.model} is grinding meat with {self.grind_type} grind")


# Пример использования

coffee_machine = CoffeeMachine("КОФЕВАРИТЕЛЬ", "ЗЯК-КРЯК9000", "Espresso")
blender = Blender("КРУЧУВЕРЧУВКАШУПРЕВРАЩУ", "ХРЯСЬ-БАЦ9000", 5)
meat_grinder = MeatGrinder("ФАРШАДЕЛКА", "МУ-МЯУ-ГАФ9000", "Fine")

devices = [coffee_machine, blender, meat_grinder]

for device in devices:
    device.start()
    device.stop()
    if isinstance(device, CoffeeMachine):
        device.make_coffee()
    elif isinstance(device, Blender):
        device.blend()
    elif isinstance(device, MeatGrinder):
        device.grind_meat()
    print()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1: Определение базового класса Device:
'''
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} is starting")

    def stop(self):
        print(f"{self.brand} {self.model} is stopping")
'''
Описание:

Создан базовый класс Device, представляющий общие характеристики устройства (бренд и модель).
Конструктор __init__ принимает бренд и модель, и инициализирует соответствующие атрибуты.
Методы start и stop выводят сообщения о запуске и остановке устройства.
'''
'''
Шаг №2: Создание производных классов CoffeeMachine, Blender, MeatGrinder:
'''
class CoffeeMachine(Device):
    def __init__(self, brand, model, coffee_type):
        super().__init__(brand, model)
        self.coffee_type = coffee_type

    def make_coffee(self):
        print(f"{self.brand} {self.model} is making {self.coffee_type} coffee")


class Blender(Device):
    def __init__(self, brand, model, speed_levels):
        super().__init__(brand, model)
        self.speed_levels = speed_levels

    def blend(self):
        print(f"{self.brand} {self.model} is blending at {self.speed_levels} speed levels")


class MeatGrinder(Device):
    def __init__(self, brand, model, grind_type):
        super().__init__(brand, model)
        self.grind_type = grind_type

    def grind_meat(self):
        print(f"{self.brand} {self.model} is grinding meat with {self.grind_type} grind")
'''
Описание:

Созданы три производных класса: CoffeeMachine, Blender, MeatGrinder,
каждый из которых наследует характеристики и методы базового класса Device.
Каждый производный класс имеет свои уникальные атрибуты (например, coffee_type, speed_levels, grind_type) и методы
(make_coffee, blend, grind_meat), соответствующие функциональности устройства.
'''
'''
Шаг №3: Пример использования классов:
'''
coffee_machine = CoffeeMachine("КОФЕВАРИТЕЛЬ", "ЗЯК-КРЯК9000", "Espresso")
blender = Blender("КРУЧУВЕРЧУВКАШУПРЕВРАЩУ", "ХРЯСЬ-БАЦ9000", 5)
meat_grinder = MeatGrinder("ФАРШАДЕЛКА", "МУ-МЯУ-ГАФ9000", "Fine")

devices = [coffee_machine, blender, meat_grinder]

for device in devices:
    device.start()
    device.stop()
    if isinstance(device, CoffeeMachine):
        device.make_coffee()
    elif isinstance(device, Blender):
        device.blend()
    elif isinstance(device, MeatGrinder):
        device.grind_meat()
    print()
'''
Описание:

Создаются объекты каждого класса, представляющие конкретные устройства (кофеварку, блендер, мясорубку).
Объекты добавляются в список devices.
В цикле вызываются методы start и stop для каждого устройства.
Для каждого устройства проверяется его тип, и в зависимости от типа вызывается соответствующий метод 
(make_coffee, blend, grind_meat).
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание №2 - Создайте класс Ship, который содержит информацию о корабле.
'''
class Ship:
    def __init__(self, name, displacement):
        self.name = name
        self.displacement = displacement

    def start_engine(self):
        print(f"{self.name} для несения боевой службы, запускает свой двигатель, во имя РОДИНЫ!")

    def stop_engine(self):
        print(f"{self.name} обнаружив врага отечества и готовясь к бою, при необходимости, останавливает свой двигатель")

    def perform_special_action(self):
        pass


class Frigate(Ship):
    def __init__(self, name, displacement, missile_count):
        super().__init__(name, displacement)
        self.missile_count = missile_count

    def perform_special_action(self):
        print(f"{self.name} (Фрегат) запускает {self.missile_count} ракеты что-бы уничтожить врага!")


class Destroyer(Ship):
    def __init__(self, name, displacement, torpedo_tubes):
        super().__init__(name, displacement)
        self.torpedo_tubes = torpedo_tubes

    def perform_special_action(self):
        print(f"{self.name} (Эсминец) выпускает {self.torpedo_tubes} торпед с пусковой установки что-бы уничтожить врага!")


class Cruiser(Ship):
    def __init__(self, name, displacement, gun_caliber):
        super().__init__(name, displacement)
        self.gun_caliber = gun_caliber

    def perform_special_action(self):
        print(f"{self.name} (Крейсер) стреляет из своего главного {self.gun_caliber} -го калибра что-бы уничтожить врага!")


# Пример использования

admiral_golovko = Frigate("Адмирал Головко", 4500, 32)
admiral_ushakov = Destroyer("Адмирал Ушаков", 8000, 16)
peter_the_great = Cruiser("Петр Великий", 25000, 130)

ships = [admiral_golovko, admiral_ushakov, peter_the_great]

for ship in ships:
    ship.start_engine()
    ship.stop_engine()
    ship.perform_special_action()
    print()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1: Определение базового класса Ship:
'''
class Ship:
    def __init__(self, name, displacement):
        self.name = name
        self.displacement = displacement

    def start_engine(self):
        print(f"{self.name} для несения боевой службы, запускает свой двигатель, во имя РОДИНЫ!")

    def stop_engine(self):
        print(f"{self.name} обнаружив врага отечества и готовясь к бою, при необходимости, останавливает свой двигатель")

    def perform_special_action(self):
        pass
'''
Описание:

Создан базовый класс Ship, представляющий корабль с атрибутами name (имя корабля) и displacement (водоизмещение).
Конструктор __init__ инициализирует атрибуты name и displacement.
Методы start_engine и stop_engine выводят сообщения о запуске и остановке двигателя корабля.
Метод perform_special_action оставлен абстрактным (пустым), так как действие специального действия может 
различаться для каждого типа корабля.
'''
'''
Шаг №2: Создание производных классов Frigate, Destroyer, Cruiser:
'''
class Frigate(Ship):
    def __init__(self, name, displacement, missile_count):
        super().__init__(name, displacement)
        self.missile_count = missile_count

    def perform_special_action(self):
        print(f"{self.name} (Фрегат) запускает {self.missile_count} ракеты что-бы уничтожить врага!")


class Destroyer(Ship):
    def __init__(self, name, displacement, torpedo_tubes):
        super().__init__(name, displacement)
        self.torpedo_tubes = torpedo_tubes

    def perform_special_action(self):
        print(f"{self.name} (Эсминец) выпускает {self.torpedo_tubes} торпед с пусковой установки что-бы уничтожить врага!")


class Cruiser(Ship):
    def __init__(self, name, displacement, gun_caliber):
        super().__init__(name, displacement)
        self.gun_caliber = gun_caliber

    def perform_special_action(self):
        print(f"{self.name} (Крейсер) стреляет из своего главного {self.gun_caliber} -го калибра что-бы уничтожить врага!")
'''
Описание:

Созданы три производных класса: Frigate, Destroyer, Cruiser, каждый из которых наследует характеристики и 
методы базового класса Ship.
Каждый производный класс имеет свои уникальные атрибуты (missile_count, torpedo_tubes, gun_caliber) и 
переопределенный метод perform_special_action для каждого типа корабля.
'''
'''
Шаг №3: Пример использования классов:
'''
admiral_golovko = Frigate("Адмирал Головко", 4500, 32)
admiral_ushakov = Destroyer("Адмирал Ушаков", 8000, 16)
peter_the_great = Cruiser("Петр Великий", 25000, 130)

ships = [admiral_golovko, admiral_ushakov, peter_the_great]

for ship in ships:
    ship.start_engine()
    ship.stop_engine()
    ship.perform_special_action()
    print()
'''
Описание:

Создаются объекты каждого класса, представляющие конкретные типы кораблей (фрегат, эсминец, крейсер).
Объекты добавляются в список ships.
В цикле вызываются методы start_engine и stop_engine для каждого корабля.
Для каждого корабля вызывается метод perform_special_action, который выводит сообщение о выполнении специального
действия (запуск ракет, выпуск торпед, стрельба из орудий).
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
ООП. Множественное следование
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание №1: Класс "Окружность, вписанная в квадрат"
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2


class CircleInSquare(Square):
    def __init__(self, side_length):
        super().__init__(side_length)

    def radius(self):
        return self.side_length / 2

    def area(self):
        return 3.14 * self.radius() ** 2


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Значение должно быть больше 0")
            return value
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите положительное число.")


# Ввод данных с клавиатуры
try:
    side_length = get_positive_float("Введите длину стороны квадрата: ")
except KeyboardInterrupt:
    print("\nПользователь прервал ввод.")
    exit()

# Создание объекта
try:
    circle_in_square = CircleInSquare(side_length)
except ValueError as e:
    print(f"Ошибка: {e}")
    exit()

# Вывод результатов
print(f"Площадь квадрата: {circle_in_square.area()}")
print(f"Радиус вписанной окружности: {circle_in_square.radius()}")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1: Определение класса Square:
'''
class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2
'''
Описание:

Создан класс Square, представляющий квадрат.
Конструктор __init__ инициализирует атрибут side_length (длина стороны квадрата).
Метод area возвращает площадь квадрата, вычисляемую как квадрат длины стороны.
'''
'''
Шаг №2: Определение класса CircleInSquare (наследуется от Square):
'''
class CircleInSquare(Square):
    def __init__(self, side_length):
        super().__init__(side_length)

    def radius(self):
        return self.side_length / 2

    def area(self):
        return 3.14 * self.radius() ** 2
'''
Описание:

Создан класс CircleInSquare, который наследует от класса Square.
Конструктор __init__ вызывает конструктор родительского класса для инициализации длины стороны квадрата.
Метод radius возвращает радиус вписанной окружности (половина длины стороны квадрата).
Метод area переопределен и возвращает площадь окружности вписанной в квадрат.
'''
'''
Шаг №3: Определение функции get_positive_float:
'''
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Значение должно быть больше 0")
            return value
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите положительное число.")
'''
Описание:

Создана функция get_positive_float, которая запрашивает у пользователя ввод положительного числа.
Используется цикл для обработки некорректного ввода.
Если ввод не является положительным числом, возбуждается исключение ValueError.
'''
'''
Шаг №4: Ввод данных с клавиатуры:
'''
try:
    side_length = get_positive_float("Введите длину стороны квадрата: ")
except KeyboardInterrupt:
    print("\nПользователь прервал ввод.")
    exit()
'''
Описание:

Пользователь вводит длину стороны квадрата с клавиатуры, используя функцию get_positive_float.
Обработан случай прерывания пользователем (KeyboardInterrupt), в этом случае программа завершается.
'''
'''
Шаг №5: Создание объекта CircleInSquare:
'''
try:
    circle_in_square = CircleInSquare(side_length)
except ValueError as e:
    print(f"Ошибка: {e}")
    exit()
'''
Описание:

Создается объект circle_in_square класса CircleInSquare с заданной длиной стороны.
Обработан случай возникновения исключения ValueError, если произошла ошибка при создании объекта.
'''
'''
Шаг №6: Вывод результатов:
'''
print(f"Площадь квадрата: {circle_in_square.area()}")
print(f"Радиус вписанной окружности: {circle_in_square.radius()}")
'''
Описание:

Выводится площадь квадрата и радиус вписанной окружности, используя методы объекта circle_in_square.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание №2: Класс "Автомобиль" с подклассами "Колеса", "Двигатель", "Двери"
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
class Wheels:
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def start(self):
        print("Двигатель завелся и мы поехали!! СЧАСТЛИВОГО ПУТИ - кричали нам РИПТИЛОЙДЫ")


class Doors:
    def __init__(self, door_count):
        self.door_count = door_count


class Car(Wheels, Engine, Doors):
    def __init__(self, wheel_count, fuel_type, door_count):
        Wheels.__init__(self, wheel_count)
        Engine.__init__(self, fuel_type)
        Doors.__init__(self, door_count)


# Пример использования

my_car = Car(wheel_count=4, fuel_type="Gasoline", door_count=4)
print(f"У моей машины {my_car.wheel_count} колеса, она работает на {my_car.fuel_type}, и имеет {my_car.door_count} двери.")
my_car.start()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1: Определение класса Wheels:
'''
class Wheels:
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count
'''
Описание:

Создан класс Wheels, представляющий количество колес.
Конструктор __init__ инициализирует атрибут wheel_count (количество колес).
'''
'''
Шаг №2: Определение класса Engine:
'''
class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def start(self):
        print("Двигатель завелся и мы поехали!! СЧАСТЛИВОГО ПУТИ - кричали нам РИПТИЛОЙДЫ")
'''
Описание:

Создан класс Engine, представляющий тип топлива и содержащий метод start.
Конструктор __init__ инициализирует атрибут fuel_type (тип топлива).
Метод start выводит сообщение о том, что двигатель завелся и началось путешествие.
'''
'''
Шаг №3: Определение класса Doors:
'''
class Doors:
    def __init__(self, door_count):
        self.door_count = door_count
'''
Описание:

Создан класс Doors, представляющий количество дверей.
Конструктор __init__ инициализирует атрибут door_count (количество дверей).
'''
'''
Шаг №4: Определение класса Car (множественное наследование):
'''
class Car(Wheels, Engine, Doors):
    def __init__(self, wheel_count, fuel_type, door_count):
        Wheels.__init__(self, wheel_count)
        Engine.__init__(self, fuel_type)
        Doors.__init__(self, door_count)
'''
Описание:

Создан класс Car, который наследует от классов Wheels, Engine, и Doors.
Конструктор __init__ инициализирует атрибуты wheel_count, fuel_type, и door_count, вызывая конструкторы родительских классов.
'''
'''
Шаг №5: Пример использования класса Car:
'''
# Пример использования
my_car = Car(wheel_count=4, fuel_type="Gasoline", door_count=4)
print(f"У моей машины {my_car.wheel_count} колеса, она работает на {my_car.fuel_type}, и имеет {my_car.door_count} двери.")
my_car.start()
'''
Описание:

Создается объект my_car класса Car с указанными параметрами.
Выводится информация о количестве колес, типе топлива и количестве дверей.
Вызывается метод start объекта my_car, выводящий сообщение о запуске двигателя.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание №3: Классы для рисования фигур
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# Определение базового класса Shape
class Shape:
    def __init__(self, x=0, y=0):
        """
        Инициализация базового класса для рисования плоских фигур.

        :param x: Координата x
        :param y: Координата y
        """
        self.x = x
        self.y = y

    def show(self):
        """
        Вывод информации о фигуре на экран.
        """
        print(f"Местоположение: ({self.x}, {self.y})")

    def save(self, filename):
        """
        Сохранение информации о фигуре в файл.

        :param filename: Имя файла для сохранения
        """
        with open(filename, 'w') as file:
            file.write(f"{self.__class__.__name__} {self.x} {self.y}\n")

    def load(self, filename):
        """
        Загрузка информации о фигуре из файла.

        :param filename: Имя файла для загрузки
        """
        with open(filename, 'r') as file:
            data = file.read().split()
            self.x, self.y = int(data[1]), int(data[2])


# Определение производных классов

class Square(Shape):
    def __init__(self, x=0, y=0, side_length=0):
        """
        Инициализация класса для рисования квадрата.

        :param x: Координата x верхнего левого угла квадрата
        :param y: Координата y верхнего левого угла квадрата
        :param side_length: Длина стороны квадрата
        """
        super().__init__(x, y)
        self.side_length = side_length

    def show(self):
        """
        Вывод информации о квадрате на экран.
        """
        super().show()
        print(f"Тип: Квадрат, Длина стороны: {self.side_length}")


class Rectangle(Shape):
    def __init__(self, x=0, y=0, width=0, height=0):
        """
        Инициализация класса для рисования прямоугольника.

        :param x: Координата x верхнего левого угла прямоугольника
        :param y: Координата y верхнего левого угла прямоугольника
        :param width: Ширина прямоугольника
        :param height: Высота прямоугольника
        """
        super().__init__(x, y)
        self.width = width
        self.height = height

    def show(self):
        """
        Вывод информации о прямоугольнике на экран.
        """
        super().show()
        print(f"Тип: Прямоугольник, Ширина: {self.width}, Высота: {self.height}")


class Circle(Shape):
    def __init__(self, x=0, y=0, radius=0):
        """
        Инициализация класса для рисования окружности.

        :param x: Координата x центра окружности
        :param y: Координата y центра окружности
        :param radius: Радиус окружности
        """
        super().__init__(x, y)
        self.radius = radius

    def show(self):
        """
        Вывод информации о окружности на экран.
        """
        super().show()
        print(f"Тип: Окружность, Радиус: {self.radius}")


class Ellipse(Shape):
    def __init__(self, x=0, y=0, major_axis=0, minor_axis=0):
        """
        Инициализация класса для рисования эллипса.

        :param x: Координата x верхнего угла описанного прямоугольника
        :param y: Координата y верхнего угла описанного прямоугольника
        :param major_axis: Большая полуось эллипса
        :param minor_axis: Малая полуось эллипса
        """
        super().__init__(x, y)
        self.major_axis = major_axis
        self.minor_axis = minor_axis

    def show(self):
        """
        Вывод информации об эллипсе на экран.
        """
        super().show()
        print(f"Тип: Эллипс, Большая полуось: {self.major_axis}, Малая полуось: {self.minor_axis}")


# Пример использования

shapes = []

try:
    # Ввод данных с клавиатуры и обработка ошибок
    x = int(input("Введите координату x: "))
    y = int(input("Введите координату y: "))
    side_length = int(input("Введите длину стороны квадрата: "))
    shapes.append(Square(x, y, side_length))

    x = int(input("Введите координату x: "))
    y = int(input("Введите координату y: "))
    width = int(input("Введите ширину прямоугольника: "))
    height = int(input("Введите высоту прямоугольника: "))
    shapes.append(Rectangle(x, y, width, height))

    x = int(input("Введите координату x: "))
    y = int(input("Введите координату y: "))
    radius = int(input("Введите радиус окружности: "))
    shapes.append(Circle(x, y, radius))

    x = int(input("Введите координату x: "))
    y = int(input("Введите координату y: "))
    major_axis = int(input("Введите большую полуось эллипса: "))
    minor_axis = int(input("Введите малую полуось эллипса: "))
    shapes.append(Ellipse(x, y, major_axis, minor_axis))
except ValueError:
    print("Ошибка ввода данных. Введите целые числа.")

# Сохранение в файлы
for i, shape in enumerate(shapes):
    shape.save(f'shape_{i}.txt')

# Загрузка из файлов
loaded_shapes = [Square(), Rectangle(), Circle(), Ellipse()]

for i, shape in enumerate(loaded_shapes):
    shape.load(f'shape_{i}.txt')
    shape.show()
    print()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1: Определение базового класса Shape:
'''
class Shape:
    def __init__(self, x=0, y=0):
        """
        Инициализация базового класса для рисования плоских фигур.

        :param x: Координата x
        :param y: Координата y
        """
        self.x = x
        self.y = y

    def show(self):
        """
        Вывод информации о фигуре на экран.
        """
        print(f"Местоположение: ({self.x}, {self.y})")

    def save(self, filename):
        """
        Сохранение информации о фигуре в файл.

        :param filename: Имя файла для сохранения
        """
        with open(filename, 'w') as file:
            file.write(f"{self.__class__.__name__} {self.x} {self.y}\n")

    def load(self, filename):
        """
        Загрузка информации о фигуре из файла.

        :param filename: Имя файла для загрузки
        """
        with open(filename, 'r') as file:
            data = file.read().split()
            self.x, self.y = int(data[1]), int(data[2])
'''
Описание:

Создан базовый класс Shape, содержащий координаты x и y.
Конструктор __init__ инициализирует координаты. По умолчанию они равны 0.
Метод show выводит информацию о местоположении фигуры.
Метод save сохраняет информацию о фигуре в файл, используя имя класса, x и y.
Метод load загружает информацию о фигуре из файла и устанавливает соответствующие координаты.
'''
'''
Шаг №2: Определение производных классов (Square, Rectangle, Circle, Ellipse):
'''
class Square(Shape):
    def __init__(self, x=0, y=0, side_length=0):
        """
        Инициализация класса для рисования квадрата.

        :param x: Координата x верхнего левого угла квадрата
        :param y: Координата y верхнего левого угла квадрата
        :param side_length: Длина стороны квадрата
        """
        super().__init__(x, y)
        self.side_length = side_length

    def show(self):
        """
        Вывод информации о квадрате на экран.
        """
        super().show()
        print(f"Тип: Квадрат, Длина стороны: {self.side_length}")


class Rectangle(Shape):
    def __init__(self, x=0, y=0, width=0, height=0):
        """
        Инициализация класса для рисования прямоугольника.

        :param x: Координата x верхнего левого угла прямоугольника
        :param y: Координата y верхнего левого угла прямоугольника
        :param width: Ширина прямоугольника
        :param height: Высота прямоугольника
        """
        super().__init__(x, y)
        self.width = width
        self.height = height

    def show(self):
        """
        Вывод информации о прямоугольнике на экран.
        """
        super().show()
        print(f"Тип: Прямоугольник, Ширина: {self.width}, Высота: {self.height}")


class Circle(Shape):
    def __init__(self, x=0, y=0, radius=0):
        """
        Инициализация класса для рисования окружности.

        :param x: Координата x центра окружности
        :param y: Координата y центра окружности
        :param radius: Радиус окружности
        """
        super().__init__(x, y)
        self.radius = radius

    def show(self):
        """
        Вывод информации о окружности на экран.
        """
        super().show()
        print(f"Тип: Окружность, Радиус: {self.radius}")


class Ellipse(Shape):
    def __init__(self, x=0, y=0, major_axis=0, minor_axis=0):
        """
        Инициализация класса для рисования эллипса.

        :param x: Координата x верхнего угла описанного прямоугольника
        :param y: Координата y верхнего угла описанного прямоугольника
        :param major_axis: Большая полуось эллипса
        :param minor_axis: Малая полуось эллипса
        """
        super().__init__(x, y)
        self.major_axis = major_axis
        self.minor_axis = minor_axis

    def show(self):
        """
        Вывод информации об эллипсе на экран.
        """
        super().show()
        print(f"Тип: Эллипс, Большая полуось: {self.major_axis}, Малая полуось: {self.minor_axis}")
'''
Описание:

Созданы производные классы Square, Rectangle, Circle, и Ellipse, наследующие от базового класса Shape.
Каждый из производных классов имеет свои собственные атрибуты и метод show,
который переопределяет метод из базового класса.
'''
'''
Шаг №3: Пример использования:
'''
# Пример использования
shapes = []

try:
    # Ввод данных с клавиатуры и обработка ошибок
    x = int(input("Введите координату x: "))
    y = int(input("Введите координату y: "))
    side_length = int(input("Введите длину стороны квадрата: "))
    shapes.append(Square(x, y, side_length))

    x = int(input("Введите координату x: "))
    y = int(input("Введите координату y: "))
    width = int(input("Введите ширину прямоугольника: "))
    height = int(input("Введите высоту прямоугольника: "))
    shapes.append(Rectangle(x, y, width, height))

    x = int(input("Введите координату x: "))
    y = int(input("Введите координату y: "))
    radius = int(input("Введите радиус окружности: "))
    shapes.append(Circle(x, y, radius))

    x = int(input("Введите координату x: "))
    y = int(input("Введите координату y: "))
    major_axis = int(input("Введите большую полуось эллипса: "))
    minor_axis = int(input("Введите малую полуось эллипса: "))
    shapes.append(Ellipse(x, y, major_axis, minor_axis))
except ValueError:
    print("Ошибка ввода данных. Введите целые числа.")

# Сохранение в файлы
for i, shape in enumerate(shapes):
    shape.save(f'shape_{i}.txt')

# Загрузка из файлов
loaded_shapes = [Square(), Rectangle(), Circle(), Ellipse()]

for i, shape in enumerate(loaded_shapes):
    shape.load(f'shape_{i}.txt')
    shape.show()
    print()
'''
Описание:

Создается список shapes, в который добавляются объекты разных фигур (в данном случае, только квадрат).
Происходит ввод данных с клавиатуры, создание объектов и добавление их в список shapes.
Фигуры сохраняются в файлы (с именами shape_0.txt, shape_1.txt, и т.д.).
Затем создается список loaded_shapes для загрузки фигур из файлов.
Происходит загрузка фигур из файлов и вывод их информации с помощью метода show.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
