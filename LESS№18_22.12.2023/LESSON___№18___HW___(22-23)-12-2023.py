# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''  ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓
Дата выполнения ДОМАШНЕЙ РАБОТЫ: 22-23 - ДЕКАБРЯ 2023
''''  ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓
'''
Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
Дисциплина: Основы программирования на Python
'''
'''
Урок от 22.12.2023
Домашняя работа №18: ООП. Полиморфизм
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполните следующие задания:   
'''
'''
Пересмотрите алгоритм решения прошлой практической работы, с использованием инкапсуляции.
Реализуйте старый алгоритм с использованием полиморфизма.

Напишите программу, в которой есть главный класс с текстовым полем.
В главное классе должен быть метод для присваивания значения полю: без аргументов и с одним текстовым аргументом.
Объект главного класса создаётся передачей одного текстового аргумента конструктору. 
На основе главного класса создается класса потомок. 
В классе-потомке нужно добавить числовое поле. 
У конструктора класса-потомка два аргумента.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
''''Вариант № 0'''''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Этот пример демонстрирует использование инкапсуляции (сокрытия данных внутри класса), 
наследования (переиспользование кода из родительского класса) и полиморфизма (переопределение метода display_info).
'''
class MainClass:
    def __init__(self, text=None):
        self._text = text

    def set_text(self, text):
        self._text = text

    def display_info(self):
        print(f"MainClass: Text - {self._text}")


class SubClass(MainClass):
    def __init__(self, text=None, number=None):
        super().__init__(text)
        self._number = number

    def set_number(self, number):
        self._number = number

    def display_info(self):
        super().display_info()
        print(f"SubClass: Number - {self._number}")


# Пример использования
main_obj = MainClass("Hello, world!")
main_obj.display_info()

sub_obj = SubClass("Hi there!", 42)
sub_obj.display_info()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг 1: Определение MainClass
'''
class MainClass:
    def __init__(self, text=None):
        self._text = text

    def set_text(self, text):
        self._text = text

    def display_info(self):
        print(f"MainClass: Text - {self._text}")
'''
MainClass - это основной класс. Он имеет конструктор __init__, который принимает один аргумент text (по умолчанию None).
Этот аргумент инициализирует защищенное (по соглашению с одним подчеркиванием _) текстовое поле _text.
set_text - метод для установки значения _text.
display_info - метод для отображения информации о текущем объекте MainClass, включая значение _text.
'''
'''
Шаг 2: Определение SubClass
'''
class SubClass(MainClass):
    def __init__(self, text=None, number=None):
        super().__init__(text)
        self._number = number

    def set_number(self, number):
        self._number = number

    def display_info(self):
        super().display_info()
        print(f"SubClass: Number - {self._number}")
'''
SubClass - это класс-потомок MainClass. Он наследует все свойства и методы MainClass.
Конструктор __init__ класса SubClass принимает два аргумента, text и number. super().__init__(text) 
вызывает конструктор родительского класса, чтобы инициализировать текстовое поле. Затем self._number инициализируется 
значением number.
set_number - метод для установки значения _number.
display_info - переопределенный метод отображения информации. 
Сначала вызывается метод display_info родительского класса (super().display_info()), затем выводится информация 
о числовом поле _number.
'''
'''
Шаг 3: Пример использования
'''
# Пример использования
main_obj = MainClass("Hello, world!")
main_obj.display_info()

sub_obj = SubClass("Hi there!", 42)
sub_obj.display_info()
'''
Создается объект main_obj типа MainClass с текстовым значением "Hello, world!".
Выводится информация о main_obj с помощью display_info.
Создается объект sub_obj типа SubClass с текстовым значением "Hi there!" и числовым значением 42.
Выводится информация о sub_obj с помощью display_info, который теперь включает и текст, и число.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
''''Вариант № 1'''''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
class MainClass:
    def __init__(self, text_value):
        self._text_value = text_value

    def set_text_value(self, text_value=None):
        if text_value:
            self._text_value = text_value

    def display_info(self):
        print(f"Text Value: {self._text_value}")


class SubClass(MainClass):
    def __init__(self, text_value, numeric_value):
        super().__init__(text_value)
        self._numeric_value = numeric_value

    def set_numeric_value(self, numeric_value):
        self._numeric_value = numeric_value

    def display_info(self):
        super().display_info()
        print(f"Numeric Value: {self._numeric_value}")


# Пример использования
main_object = MainClass("Hello")
sub_object = SubClass("Polymorphism", 42)

# Вывод информации
main_object.display_info()
sub_object.display_info()

# Изменение значений полей
main_object.set_text_value("New Text Value")
sub_object.set_numeric_value(99)

# Повторный вывод информации
main_object.display_info()
sub_object.display_info()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Описание:
Создается класс MainClass с текстовым полем и методами для работы с этим полем.
Создается класс SubClass, который наследуется от MainClass и добавляет числовое поле.
Используется полиморфизм: метод display_info вызывается у объектов разных классов.
Демонстрируется возможность изменения значений полей с использованием соответствующих методов у разных объектов.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Класс MainClass:
'''
class MainClass:
    def __init__(self, text_value):
        self._text_value = text_value

    def set_text_value(self, text_value=None):
        if text_value:
            self._text_value = text_value

    def display_info(self):
        print(f"Text Value: {self._text_value}")
'''
Описание:
__init__ метод:

Это конструктор класса. Он вызывается при создании нового объекта класса.
Принимает два аргумента: self (ссылка на сам объект) и text_value (текстовое значение, которое будет присвоено полю).
Инициализирует поле _text_value переданным значением.

set_text_value метод:

Этот метод используется для изменения значения текстового поля.
Принимает self и text_value (по умолчанию None).
Если передан аргумент text_value, то он присваивается полю _text_value.

display_info метод:

Этот метод выводит информацию о текущем значении текстового поля.
Просто использует функцию print для вывода значения поля.
'''
'''
Класс SubClass (наследуется от MainClass):
'''
class SubClass(MainClass):
    def __init__(self, text_value, numeric_value):
        super().__init__(text_value)
        self._numeric_value = numeric_value

    def set_numeric_value(self, numeric_value):
        self._numeric_value = numeric_value

    def display_info(self):
        super().display_info()
        print(f"Numeric Value: {self._numeric_value}")
'''
Описание:
__init__ метод:

Вызывает конструктор родительского класса (MainClass) с передачей ему текстового значения.
Инициализирует свое числовое поле (_numeric_value) переданным числовым значением.

set_numeric_value метод:

Этот метод используется для изменения значения числового поля.
Принимает self и numeric_value.
Присваивает значение атрибуту _numeric_value.

display_info метод:

Переопределяет метод display_info из родительского класса.
Первым делом вызывает родительский display_info для вывода текстового значения.
Затем выводит информацию о числовом поле.
'''
'''
Пример использования:
'''
main_object = MainClass("Hello")
sub_object = SubClass("Polymorphism", 42)

main_object.display_info()
sub_object.display_info()

main_object.set_text_value("New Text Value")
sub_object.set_numeric_value(99)

main_object.display_info()
sub_object.display_info()
'''
Описание:
Создаются объекты классов MainClass и SubClass.
Вызываются методы для вывода информации о полях объектов.
Значения полей изменяются с использованием соответствующих методов.
Снова выводится информация о полях объектов, чтобы продемонстрировать изменения.
'''
'''
Общие замечания:
Применение инкапсуляции: Поля классов начинаются с символа подчеркивания (_), что указывает на их "защищенный" статус.
Такие поля не предназначены для прямого доступа извне класса, и их значения следует изменять только через методы класса.

Полиморфизм: 
Оба класса имеют метод с одинаковым именем (display_info), который используется в примере использования.
Однако, класс SubClass переопределяет этот метод, добавляя свой функционал к функционалу родительского класса.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
''''Вариант № Бонус (хотя все одно и тоже)'''''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
class MainClass:
    def __init__(self, text_field=""):
        self._text_field = text_field

    def set_text_field(self, text):
        self._text_field = text


class ChildClass(MainClass):
    def __init__(self, text_field, numeric_field):
        super().__init__(text_field)
        self._numeric_field = numeric_field

    def set_numeric_field(self, numeric_value):
        if numeric_value > 0:
            self._numeric_field = numeric_value
        else:
            print("Значение числового поля должно быть положительным.")

    def display_info(self):
        print(f"Текстовое поле: {self._text_field}")
        print(f"Числовое поле: {self._numeric_field}")


# Пример использования
main_obj = MainClass("Привет, это главный класс.")
print(main_obj._text_field)  # Выведет: Привет, это главный класс.

child_obj = ChildClass("Привет, это дочерний класс.", 42)
child_obj.display_info()
# Выведет:
# Текстовое поле: Привет, это дочерний класс.
# Числовое поле: 42

child_obj.set_text_field("Новый текст для дочернего класса.")
child_obj.set_numeric_field(100)

child_obj.display_info()
# Выведет:
# Текстовое поле: Новый текст для дочернего класса.
# Числовое поле: 100
'''
Здесь код включает в себя классы MainClass и ChildClass, 
а также метод display_info(), который выводит информацию о значениях
текстового и числового полей. Вы можете использовать этот код 
как отправную точку и настроить его под свои конкретные требования.
'''
'''
Теперь давайте рассмотрим, как он соответствует каждому из пунктов:

Инкапсуляция: 
В коде используется инкапсуляция с использованием приватных полей (поле, 
начинающееся с символа _). Например, _text_field и _numeric_field - это 
приватные поля, к которым можно обращаться только изнутри класса.

Полиморфизм: 
В примере есть два класса - MainClass и ChildClass. ChildClass является 
потомком MainClass и переопределяет метод display_info(). 
Это пример полиморфизма, где метод display_info() ведет себя по-разному 
для объектов MainClass и ChildClass.

Главный класс с текстовым полем и методом для присваивания значения:
Класс MainClass соответствует этим требованиям. У него есть текстовое 
поле _text_field и метод set_text_field для установки значения этого поля.

Объект главного класса создается с передачей текстового 
аргумента конструктору: 
Это выполняется в строке main_obj = MainClass("Привет, 
это главный класс.").

Создание класса-потомка с добавлением числового поля: 
Класс ChildClass является классом-потомком MainClass и добавляет 
числовое поле _numeric_field.

У конструктора класса-потомка два аргумента: 
Конструктор ChildClass имеет два аргумента: text_field и numeric_field.
'''
'''
Таким образом, написанный код соответствует всем требованиям 
домашнего задания задания. 
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполните следующие задания:   
'''
'''
Пересмотрите алгоритм решения прошлой практической работы, с использованием инкапсуляции.
Реализуйте старый алгоритм с использованием полиморфизма.

Напишите программу, в которой есть главный класс с текстовым полем.
В главное классе должен быть метод для присваивания значения полю: без аргументов и с одним текстовым аргументом.
Объект главного класса создаётся передачей одного текстового аргумента конструктору. 
На основе главного класса создается класса потомок. 
В классе-потомке нужно добавить числовое поле. 
У конструктора класса-потомка два аргумента.
'''
'''
Итак, у нас есть три задачи:

1. Пересмотрите алгоритм решения прошлой практической работы, с использованием инкапсуляции.

Это предполагает, что у вас уже есть какой-то алгоритм, и вам нужно его пересмотреть, добавив инкапсуляцию.
Инкапсуляция - это принцип объектно-ориентированного программирования, который предполагает упаковку данных и методов,
работающих с этими данными,в одном классе. Это делается для контроля доступа к данным и изоляции их от внешнего вмешательства.

Пример:
'''
class MyClass:
    def __init__(self):
        self._my_private_variable = 0  # приватная переменная с использованием _
        
    def get_private_variable(self):
        return self._my_private_variable
    
    def set_private_variable(self, value):
        if value > 0:
            self._my_private_variable = value
        else:
            print("Значение должно быть положительным.")
'''
2. Реализуйте старый алгоритм с использованием полиморфизма.

Полиморфизм - это еще один принцип ООП, который позволяет объектам одного класса использовать методы другого класса.
В данном контексте, возможно, нужно создать базовый класс и производные классы, используя полиморфизм.

Пример:
'''
class BaseClass:
    def my_method(self):
        pass  # базовый метод

class DerivedClass1(BaseClass):
    def my_method(self):
        print("Метод из класса DerivedClass1")

class DerivedClass2(BaseClass):
    def my_method(self):
        print("Метод из класса DerivedClass2")
'''
3. Напишите программу с главным классом с текстовым полем и методом для присваивания значения полю.
Объект главного класса создаётся передачей одного текстового аргумента конструктору.
В классе-потомке нужно добавить числовое поле. У конструктора класса-потомка два аргумента.

Пример:
'''
class MainClass:
    def __init__(self, text_field):
        self.text_field = text_field
        
    def set_text_field(self, text):
        self.text_field = text
        
class ChildClass(MainClass):
    def __init__(self, text_field, numeric_field):
        super().__init__(text_field)
        self.numeric_field = numeric_field
'''
В данном примере ChildClass наследуется от MainClass, добавляя при этом новое числовое поле numeric_field.
Конструктор ChildClass принимает два аргумента: text_field и numeric_field. 
С помощью super().__init__(text_field) вызывается конструктор родительского 
класса, чтобы проинициализировать текстовое поле.
'''
'''
ИЛИ Я ЧТО-ТО НЕ ПОНЯЛ и ДЕЛАЮ НЕ ТАК??
'''

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #