# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''  ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓
Дата выполнения ДОМАШНЕЙ РАБОТЫ: 27-28 - ДЕКАБРЯ 2023
''''  ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓
'''
Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
Дисциплина: Основы программирования на Python
'''
'''
Урок от 27.12.2023
Домашняя работа №20: ООП.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполните следующие задания:
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Задания №1
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Создайте класс Circle (окружность). Для данного класса реализуйте ряд перегруженных операторов:
Проверка на равенство радиусов двух окружностей (операция = =);
Сравнения длин двух окружностей (операции >, <, <=,>=);
Пропорциональное изменение размеров окружности, путем изменения ее радиуса (операции + - += -=).
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Задание №2
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Создайте класс Complex (комплексное число).
Создайте перегруженные операторы для реализации арифметических операций для по работе с комплексными числами
(операции +, -, *, /).
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Задание №3
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Вам необходимо создать класс Airplane (самолет).
С помощью перегрузки операторов реализовать:
Проверка на равенство типов самолетов (операция = =);
Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции > < <= >=).
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Задание №4
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Создать класс Flat (квартира). Реализовать перегруженные операторы:
Проверка на равенство площадей квартир (операция ==);
Проверка на неравенство площадей квартир (операция !=);
Сравнение двух квартир по цене (операции > < <= >=).
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Далее решение этих заданий ↑   ↑   ↑   ↑
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание №1: Класс Circle
'''
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return False

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Circle):
            return self.radius <= other.radius
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.radius >= other.radius
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, (int, float)):
            return Circle(self.radius + value)
        return NotImplemented

    def __sub__(self, value):
        if isinstance(value, (int, float)):
            return Circle(self.radius - value)
        return NotImplemented

    def __iadd__(self, value):
        if isinstance(value, (int, float)):
            self.radius += value
            return self
        return NotImplemented

    def __isub__(self, value):
        if isinstance(value, (int, float)):
            self.radius -= value
            return self
        return NotImplemented
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1: Определение класса Circle
'''
class Circle:
    def __init__(self, radius):
        self.radius = radius
'''
Подробное описание (шаг №1):

1. Определение класса Circle: Создается класс Circle, представляющий круг.
Конструктор __init__ принимает радиус круга и инициализирует соответствующий атрибут объекта.
'''
'''
Шаг №2: Перегрузка операторов сравнения (__eq__, __gt__, __lt__, __le__, __ge__)
'''
def __eq__(self, other):
    if isinstance(other, Circle):
        return self.radius == other.radius
    return False

def __gt__(self, other):
    if isinstance(other, Circle):
        return self.radius > other.radius
    return NotImplemented

def __lt__(self, other):
    if isinstance(other, Circle):
        return self.radius < other.radius
    return NotImplemented

def __le__(self, other):
    if isinstance(other, Circle):
        return self.radius <= other.radius
    return NotImplemented

def __ge__(self, other):
    if isinstance(other, Circle):
        return self.radius >= other.radius
    return NotImplemented
'''
Подробное описание (шаг №2):

1. Перегрузка оператора равенства (__eq__): 
Сравнивает два объекта Circle по радиусу. Возвращает True, если радиусы равны, и False в противном случае.
2. Перегрузка операторов сравнения (__gt__, __lt__, __le__, __ge__): 
Сравнивают два объекта Circle по радиусу и возвращают соответствующие булевы значения (True/False). 
Если операнд не является объектом Circle, возвращается NotImplemented.
'''
'''
Шаг №3: Перегрузка операторов сложения и вычитания (__add__, __sub__)
'''
def __add__(self, value):
    if isinstance(value, (int, float)):
        return Circle(self.radius + value)
    return NotImplemented

def __sub__(self, value):
    if isinstance(value, (int, float)):
        return Circle(self.radius - value)
    return NotImplemented
'''
Подробное описание (шаг №3):

1. Перегрузка оператора сложения (__add__): 
Позволяет сложить объект Circle с числовым значением (int или float). 
Возвращает новый объект Circle с радиусом, увеличенным на значение операнда.
2. Перегрузка оператора вычитания (__sub__): 
Позволяет вычесть из объекта Circle числовое значение (int или float). 
Возвращает новый объект Circle с радиусом, уменьшенным на значение операнда.
'''
'''
Шаг №4: Перегрузка операторов присваивания с добавлением и вычитанием (__iadd__, __isub__)
'''
def __iadd__(self, value):
    if isinstance(value, (int, float)):
        self.radius += value
        return self
    return NotImplemented

def __isub__(self, value):
    if isinstance(value, (int, float)):
        self.radius -= value
        return self
    return NotImplemented
'''
Подробное описание (шаг №4):

1. Перегрузка оператора присваивания с добавлением (__iadd__):
Позволяет добавить к радиусу объекта Circle числовое значение (int или float). 
Изменяет текущий объект и возвращает его.
2. Перегрузка оператора присваивания с вычитанием (__isub__):
Позволяет вычесть из радиуса объекта Circle числовое значение (int или float). 
Изменяет текущий объект и возвращает его.
'''
'''
Общее использование:
'''
# Пример использования
circle1 = Circle(5)
circle2 = Circle(3)

result_eq = circle1 == circle2
result_gt = circle1 > circle2
result_lt = circle1 < circle2
result_add = circle1 + 2
result_sub = circle1 - 1

print(result_eq)  # False
print(result_gt)  # True
print(result_lt)  # False
print(result_add.radius)  # 7
print(result_sub.radius)  # 4

circle1 += 3
circle2 -= 1

print(circle1.radius)  # 8
print(circle2.radius)  # 2
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание №2: Класс Complex
'''
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Complex):
            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.real * other.imag + self.imag * other.real
            return Complex(real_part, imag_part)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Complex):
            denominator = other.real**2 + other.imag**2
            real_part = (self.real * other.real + self.imag * other.imag) / denominator
            imag_part = (self.imag * other.real - self.real * other.imag) / denominator
            return Complex(real_part, imag_part)
        return NotImplemented
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1: Определение класса Complex
'''
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
'''
Подробное описание (шаг №1):

1. Определение класса Complex: 
Создается класс Complex, представляющий комплексное число. 
Конструктор __init__ принимает два аргумента: real (действительная часть) и imag (мнимая часть), и инициализирует
соответствующие атрибуты объекта.
'''
'''
Шаг №2: Перегрузка оператора сложения (__add__)
'''
def __add__(self, other):
    if isinstance(other, Complex):
        return Complex(self.real + other.real, self.imag + other.imag)
    return NotImplemented
'''
Подробное описание (шаг №2):

1. Перегрузка оператора сложения (__add__): 
Позволяет складывать два комплексных числа. Если второй операнд является объектом Complex, возвращается новый объект
Complex с суммой соответствующих действительных и мнимых частей. В случае, если второй операнд не является 
объектом Complex, возвращается NotImplemented.
'''
'''
Шаг №3: Перегрузка оператора вычитания (__sub__)
'''
def __sub__(self, other):
    if isinstance(other, Complex):
        return Complex(self.real - other.real, self.imag - other.imag)
    return NotImplemented
'''
Подробное описание (шаг №3):

1. Перегрузка оператора вычитания (__sub__): 
Позволяет вычитать из одного комплексного числа другое. 
Если второй операнд является объектом Complex, возвращается новый объект Complex с разностью соответствующих 
действительных и мнимых частей. В случае, если второй операнд не является объектом Complex, 
возвращается NotImplemented.
'''
'''
Шаг №4: Перегрузка оператора умножения (__mul__)
'''
def __mul__(self, other):
    if isinstance(other, Complex):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)
    return NotImplemented
'''
Подробное описание (шаг №4):

1. Перегрузка оператора умножения (__mul__): 
Позволяет умножать два комплексных числа. Если второй операнд является объектом Complex, вычисляются действительная
и мнимая части произведения, и возвращается новый объект Complex с этими значениями. В случае, если второй операнд не
является объектом Complex, возвращается NotImplemented.
'''
'''
Шаг №5: Перегрузка оператора деления (__truediv__)
'''
def __truediv__(self, other):
    if isinstance(other, Complex):
        denominator = other.real ** 2 + other.imag ** 2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real_part, imag_part)
    return NotImplemented
'''
Подробное описание (шаг №5):

1. Перегрузка оператора деления (__truediv__): 
Позволяет делить одно комплексное число на другое. Если второй операнд является объектом Complex, вычисляются
действительная и мнимая части частного, и возвращается новый объект Complex с этими значениями. 
В случае, если второй операнд не является объектом Complex, возвращается NotImplemented.
'''
'''
Общее использование:
'''
# Пример использования
complex1 = Complex(2, 3)
complex2 = Complex(1, 2)

result_add = complex1 + complex2
result_sub = complex1 - complex2
result_mul = complex1 * complex2
result_div = complex1 / complex2

print(result_add.real, "+", result_add.imag, "i")  # 3 + 5i
print(result_sub.real, "-", result_sub.imag, "i")  # 1 + 1i
print(result_mul.real, "+", result_mul.imag, "i")  # -4 + 7i
print(result_div.real, "+", result_div.imag, "i")  # 1.6 - 0.2i
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание №3: Класс Airplane
'''
class Airplane:
    def __init__(self, passengers, max_passengers):
        self.passengers = passengers
        self.max_passengers = max_passengers

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers == other.max_passengers
        return False

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers > other.max_passengers
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers < other.max_passengers
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers <= other.max_passengers
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers >= other.max_passengers
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, int):
            return Airplane(self.passengers + value, self.max_passengers)
        return NotImplemented

    def __sub__(self, value):
        if isinstance(value, int):
            return Airplane(self.passengers - value, self.max_passengers)
        return NotImplemented

    def __iadd__(self, value):
        if isinstance(value, int):
            self.passengers += value
            return self
        return NotImplemented

    def __isub__(self, value):
        if isinstance(value, int):
            self.passengers -= value
            return self
        return NotImplemented

# Пример использования
airplane1 = Airplane(50, 100)
airplane2 = Airplane(75, 150)

# Примеры операций
print(airplane1 == airplane2)  # False
print(airplane1 > airplane2)   # False
print(airplane1 < airplane2)   # True
print(airplane1 + 20)          # Airplane(passengers=70, max_passengers=100)
print(airplane2 - 10)          # Airplane(passengers=65, max_passengers=150)

# Примеры операций с присваиванием
airplane1 += 30
airplane2 -= 15

print(airplane1.passengers)    # 80
print(airplane2.passengers)    # 60
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1:
'''
# Определение класса Airplane
class Airplane:
    # Инициализация объекта класса
    def __init__(self, passengers, max_passengers):
        self.passengers = passengers  # Количество пассажиров
        self.max_passengers = max_passengers  # Максимальное количество пассажиров
'''
Описание: 
В этом шаге создается класс Airplane, представляющий объект "самолет". 
Класс имеет два атрибута: passengers (количество пассажиров) и max_passengers (максимальное количество пассажиров).
'''
'''
Шаг 2:
'''
# Перегрузка оператора равенства
def __eq__(self, other):
    if isinstance(other, Airplane):
        return self.max_passengers == other.max_passengers
    return False
'''
Описание: 
В этом шаге добавляется перегрузка оператора равенства (__eq__). 
Метод сравнивает максимальное количество пассажиров текущего самолета с максимальным количеством пассажиров 
другого самолета и возвращает True, если они равны, иначе False.
'''
'''
Шаг 3:
'''
# Перегрузка оператора больше
def __gt__(self, other):
    if isinstance(other, Airplane):
        return self.max_passengers > other.max_passengers
    return NotImplemented
'''
Описание:
В этом шаге добавляется перегрузка оператора больше (__gt__). 
Метод сравнивает максимальное количество пассажиров текущего самолета с максимальным количеством пассажиров другого
самолета и возвращает True, если у текущего самолета больше мест, иначе False.
'''
'''
Шаг 4:
'''
# Перегрузка оператора меньше
def __lt__(self, other):
    if isinstance(other, Airplane):
        return self.max_passengers < other.max_passengers
    return NotImplemented
'''
Описание: 
В этом шаге добавляется перегрузка оператора меньше (__lt__). 
Метод сравнивает максимальное количество пассажиров текущего самолета с максимальным количеством пассажиров другого
самолета и возвращает True, если у текущего самолета меньше мест, иначе False.
'''
'''
Шаг 5:
'''
# Перегрузка оператора меньше или равно
def __le__(self, other):
    if isinstance(other, Airplane):
        return self.max_passengers <= other.max_passengers
    return NotImplemented
'''
Описание: 
В этом шаге добавляется перегрузка оператора меньше или равно (__le__). 
Метод сравнивает максимальное количество пассажиров текущего самолета с максимальным количеством пассажиров другого
самолета и возвращает True, если у текущего самолета меньше или равно мест, иначе False.
'''
'''
Шаг 6:
'''
# Перегрузка оператора больше или равно
def __ge__(self, other):
    if isinstance(other, Airplane):
        return self.max_passengers >= other.max_passengers
    return NotImplemented
'''
Описание: 
В этом шаге добавляется перегрузка оператора больше или равно (__ge__). 
Метод сравнивает максимальное количество пассажиров текущего самолета с максимальным количеством пассажиров другого
самолета и возвращает True, если у текущего самолета больше или равно мест, иначе False.
'''
'''
Шаг 7:
'''
# Перегрузка оператора сложения
def __add__(self, value):
    if isinstance(value, int):
        return Airplane(self.passengers + value, self.max_passengers)
    return NotImplemented
'''
Описание: 
В этом шаге добавляется перегрузка оператора сложения (__add__). 
Метод позволяет добавлять целочисленное значение к количеству пассажиров текущего самолета, создавая новый самолет
с обновленным количеством пассажиров.
'''
'''
Шаг 8:
'''
# Перегрузка оператора вычитания
def __sub__(self, value):
    if isinstance(value, int):
        return Airplane(self.passengers - value, self.max_passengers)
    return NotImplemented
'''
Описание: 
В этом шаге добавляется перегрузка оператора вычитания (__sub__). Метод позволяет вычитать целочисленное 
значение из количества пассажиров текущего самолета, создавая новый самолет с обновленным количеством пассажиров.
'''
'''
Шаг 9:
'''
# Перегрузка оператора присваивания суммы
def __iadd__(self, value):
    if isinstance(value, int):
        self.passengers += value
        return self
    return NotImplemented
'''
Описание: 
В этом шаге добавляется перегрузка оператора присваивания суммы (__iadd__). Метод позволяет присваивать
сумму целочисленного значения к количеству пассажиров текущего самолета, обновляя его в процессе.
'''
'''
Шаг 10:
'''
# Перегрузка оператора присваивания разности
def __isub__(self, value):
    if isinstance(value, int):
        self.passengers -= value
        return self
    return NotImplemented
'''
Описание: 
В этом шаге добавляется перегрузка оператора присваивания разности (__isub__).
Метод позволяет присваивать разность целочисленного значения из количества пассажиров текущего самолета,
обновляя его в процессе.
'''
'''
Шаг 11:
'''
# Пример использования
airplane1 = Airplane(50, 100)
airplane2 = Airplane(75, 150)

# Примеры операций
print(airplane1 == airplane2)  # False
print(airplane1 > airplane2)   # False
print(airplane1 < airplane2)   # True
print(airplane1 + 20)          # Airplane(passengers=70, max_passengers=100)
print(airplane2 - 10)          # Airplane(passengers=65, max_passengers=150)

# Примеры операций с присваиванием
airplane1 += 30
airplane2 -= 15

print(airplane1.passengers)    # 80
print(airplane2.passengers)    # 60
'''
Описание:
Приведен пример использования класса Airplane с различными операторами и операциями с присваиванием.
Создаются два объекта Airplane и выполняются операции равенства, сравнения, сложения и вычитания, а также операции
с присваиванием для изменения количества пассажиров.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание №4: Класс Flat
'''
class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Flat):
            return self.area == other.area
        return False

    def __ne__(self, other):
        if isinstance(other, Flat):
            return self.area != other.area
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Flat):
            return self.price > other.price
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Flat):
            return self.price < other.price
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Flat):
            return self.price <= other.price
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Flat):
            return self.price >= other.price
        return NotImplemented
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг 1:
'''
class Flat:
''''
Описание: Создается класс Flat, представляющий объект "квартира".
'''''
'''
Шаг 2:
'''
def __init__(self, area, price):
    self.area = area
    self.price = price
'''
Описание: 
В конструкторе класса инициализируются два атрибута area (площадь квартиры) и price (цена квартиры). 
Эти атрибуты будут храниться в каждом созданном объекте класса.
'''
'''
Шаг 3:
'''
def __eq__(self, other):
    if isinstance(other, Flat):
        return self.area == other.area
    return False
'''
Описание: 
Перегружается оператор равенства (==). 
Метод сравнивает объект с другим объектом типа Flat по значению атрибута area. 
Возвращает True, если атрибуты area обоих объектов равны, и False в противном случае.
'''
'''
Шаг 4:
'''
def __ne__(self, other):
    if isinstance(other, Flat):
        return self.area != other.area
    return NotImplemented
'''
Описание: 
Перегружается оператор неравенства (!=). 
Метод сравнивает объект с другим объектом типа Flat по значению атрибута area. 
Возвращает True, если атрибуты area обоих объектов не равны, и False в противном случае.
'''
'''
Шаг 5:
'''
def __gt__(self, other):
    if isinstance(other, Flat):
        return self.price > other.price
    return NotImplemented
'''
Описание:
Перегружается оператор больше (>). 
Метод сравнивает объект с другим объектом типа Flat по значению атрибута price. 
Возвращает True, если атрибут price текущего объекта больше, чем у другого объекта, и False в противном случае.
'''
'''
Шаг 6:
'''
def __lt__(self, other):
    if isinstance(other, Flat):
        return self.price < other.price
    return NotImplemented
'''
Описание: 
Перегружается оператор меньше (<). 
Метод сравнивает объект с другим объектом типа Flat по значению атрибута price. 
Возвращает True, если атрибут price текущего объекта меньше, чем у другого объекта, и False в противном случае.
'''
'''
Шаг 7:
'''
def __le__(self, other):
    if isinstance(other, Flat):
        return self.price <= other.price
    return NotImplemented
'''
Описание: 
Перегружается оператор меньше или равно (<=). 
Метод сравнивает объект с другим объектом типа Flat по значению атрибута price. 
Возвращает True, если атрибут price текущего объекта меньше или равен, чем у другого объекта, и False в противном случае.
'''
'''
Шаг 8:
'''
def __ge__(self, other):
    if isinstance(other, Flat):
        return self.price >= other.price
    return NotImplemented
'''
Описание: 
Перегружается оператор больше или равно (>=). 
Метод сравнивает объект с другим объектом типа Flat по значению атрибута price. 
Возвращает True, если атрибут price текущего объекта больше или равен, чем у другого объекта, и False в противном случае.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
