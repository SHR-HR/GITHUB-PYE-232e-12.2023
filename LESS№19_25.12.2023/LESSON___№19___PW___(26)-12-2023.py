# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
""""
Дата выполнения практической работы: 26 - ДЕКАБРЯ 2023
""""
'''
Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
Дисциплина: Основы программирования на Python
'''
'''
Урок от 25.12.2023
Практическая работа №19: ООП.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполните следующие задания:
'''
'''
В некой игре-стратегии есть солдаты и герои. 
У всех есть свойство, содержащее уникальный номер объекта, и свойство, в котором хранится принадлежность команде.
У солдат есть метод "иду за героем", который в качестве аргумента принимает объект типа "герой". 
У героев есть метод увеличения собственного уровня.

В основной ветке программы создается по одному герою для каждой команды.
В цикле генерируются объекты-солдаты. Их принадлежность команде определяется случайно.
Солдаты разных команд добавляются в разные списки.

Измеряется длина списков солдат противоборствующих команд и выводится на экран. 
У героя, принадлежащего команде с более длинным списком, увеличивается уровень.

Отправьте одного из солдат первого героя следовать за ним. Выведите на экран идентификационные номера этих двух юнитов.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Решение этого Задания ↑   ↑   ↑   ↑   ↑   ↑   ↑
'''
'''
Вариант №1
'''
import random

# Базовый класс для всех юнитов (героев и солдат)
class Unit:
    def __init__(self, unit_id, team):
        self.unit_id = unit_id  # Уникальный номер юнита
        self.team = team  # Принадлежность команде


# Класс солдата, наследуется от класса Unit
class Soldier(Unit):
    def follow_hero(self, hero):
        print(f"Солдат {self.unit_id} идет за героем {hero.unit_id}")


# Класс героя, также наследуется от класса Unit
class Hero(Unit):
    def increase_level(self):
        print(f"Уровень героя {self.unit_id} увеличен!")

    def follow_hero(self, soldier_to_follow):
        print(f"Герой {self.unit_id} ведет с собой солдата {soldier_to_follow.unit_id}")


# Создаем по одному герою для каждой команды
hero_team1 = Hero(unit_id=1, team=1)
hero_team2 = Hero(unit_id=2, team=2)

# Генерируем объекты-солдаты и добавляем их в соответствующие списки команд
soldiers_team1 = [Soldier(unit_id=i, team=1) for i in range(10)]
soldiers_team2 = [Soldier(unit_id=i, team=2) for i in range(8)]

# Измеряем длину списков солдат и выводим на экран
length_team1 = len(soldiers_team1)
length_team2 = len(soldiers_team2)
print(f"Длина списка солдат команды 1: {length_team1}")
print(f"Длина списка солдат команды 2: {length_team2}")

# Увеличиваем уровень героя той команды, у которой больше солдат
if length_team1 > length_team2:
    hero_team1.increase_level()
else:
    hero_team2.increase_level()

# Отправляем первого солдата первого героя следовать за ним
if length_team1 > 0:
    soldier_to_follow = soldiers_team1[0]
    hero_team1.follow_hero(soldier_to_follow)
    # Выводим идентификационные номера этих двух юнитов
    print(f"Идентификационный номер героя: {hero_team1.unit_id}")
    print(f"Идентификационный номер солдата: {soldier_to_follow.unit_id}")
else:
    print("Нет солдат для следования за героем команды 1")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Далее я немножко распишу свои "умозаключения"....
'''
'''
Шаг №1:
Название кода: Инициализация классов и создание объектов

Сам код:
'''
import random

# Базовый класс для всех юнитов (героев и солдат)
class Unit:
    def __init__(self, unit_id, team):
        self.unit_id = unit_id  # Уникальный номер юнита
        self.team = team  # Принадлежность команде

# Класс солдата, наследуется от класса Unit
class Soldier(Unit):
    def follow_hero(self, hero):
        print(f"Солдат {self.unit_id} идет за героем {hero.unit_id}")

# Класс героя, также наследуется от класса Unit
class Hero(Unit):
    def increase_level(self):
        print(f"Уровень героя {self.unit_id} увеличен!")

    def follow_hero(self, soldier_to_follow):
        print(f"Герой {self.unit_id} ведет с собой солдата {soldier_to_follow.unit_id}")

# Создаем по одному герою для каждой команды
hero_team1 = Hero(unit_id=1, team=1)
hero_team2 = Hero(unit_id=2, team=2)

# Генерируем объекты-солдаты и добавляем их в соответствующие списки команд
soldiers_team1 = [Soldier(unit_id=i, team=1) for i in range(10)]
soldiers_team2 = [Soldier(unit_id=i, team=2) for i in range(8)]
'''
Полное и подробное описание:
Этот код создает базовый класс Unit для всех юнитов (героев и солдат). 
Затем определяются классы Soldier и Hero, наследующиеся от Unit. У каждого юнита есть уникальный номер и 
принадлежность к команде.

Создаются по одному герою для каждой из двух команд. 
Затем генерируются списки солдат для каждой команды с использованием списковых включений.
'''
'''
Шаг №2:
Название кода: Измерение длины списков солдат и вывод на экран

Сам код:
'''
# Измеряем длину списков солдат и выводим на экран
length_team1 = len(soldiers_team1)
length_team2 = len(soldiers_team2)
print(f"Длина списка солдат команды 1: {length_team1}")
print(f"Длина списка солдат команды 2: {length_team2}")
'''
Полное и подробное описание:
Этот участок кода измеряет длину списков солдат для каждой команды и выводит результат на экран
с использованием функции len и функции print. Таким образом, мы получаем информацию о количестве солдат
в каждой команде.
'''
'''
Шаг №3:
Название кода: Увеличение уровня героя для команды с большим числом солдат

Сам код:
'''
# Увеличиваем уровень героя той команды, у которой больше солдат
if length_team1 > length_team2:
    hero_team1.increase_level()
else:
    hero_team2.increase_level()
'''
Полное и подробное описание:
В этом фрагменте кода сравниваются длины списков солдат для команд 1 и 2.
Если длина списка солдат команды 1 больше, чем у команды 2, увеличивается уровень героя команды 1, вызывая
метод increase_level(). В противном случае увеличивается уровень героя команды 2.
'''
'''
Шаг №4:
Название кода: Отправка солдата следовать за героем и вывод их идентификационных номеров

Сам код:
'''
# Отправляем первого солдата первого героя следовать за ним
if length_team1 > 0:
    soldier_to_follow = soldiers_team1[0]
    hero_team1.follow_hero(soldier_to_follow)
    # Выводим идентификационные номера этих двух юнитов
    print(f"Идентификационный номер героя: {hero_team1.unit_id}")
    print(f"Идентификационный номер солдата: {soldier_to_follow.unit_id}")
else:
    print("Нет солдат для следования за героем команды 1")
'''
Полное и подробное описание:
Этот фрагмент кода проверяет, есть ли солдаты в списке команды 1. 
Если да, то выбирается первый солдат из списка, и метод follow_hero вызывается для первого героя, 
отправляя этого солдата следовать за ним. Затем выводятся идентификационные номера героя и солдата на экран. 
Если в команде 1 нет солдат, выводится сообщение о том, что нет солдат для следования за героем команды 1.
'''
'''
Рекомендации по улучшению кода:

1. Добавьте проверку в методе follow_hero для класса Hero, чтобы удостовериться, что объект,
переданный в качестве аргумента, действительно является экземпляром класса Soldier. 
Это может предотвратить ошибки в случае передачи некорректных объектов.

2. Добавьте комментарии в метод follow_hero для класса Hero, чтобы объяснить его назначение и то, 
что ожидается в качестве аргумента.

3. Можно добавить функциональность для генерации уникальных идентификационных номеров юнитов,
чтобы избежать возможных конфликтов.

4. Рассмотрите возможность создания отдельных методов или классов для различных этапов выполнения задачи,
чтобы сделать код более модульным и легко читаемым.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Код с рекомендациями
'''
import random

class Unit:
    def __init__(self, unit_id, team):
        self.unit_id = unit_id  # Уникальный номер юнита
        self.team = team  # Принадлежность команде


class Soldier(Unit):
    def follow_hero(self, hero):
        if isinstance(hero, Hero):  # Проверка, что объект - экземпляр класса Hero
            print(f"Солдат {self.unit_id} идет за героем {hero.unit_id}")
        else:
            print("Ошибка: Переданный объект не является героем!")


class Hero(Unit):
    def increase_level(self):
        print(f"Уровень героя {self.unit_id} увеличен!")

    def follow_hero(self, soldier_to_follow):
        if isinstance(soldier_to_follow, Soldier):  # Проверка, что объект - экземпляр класса Soldier
            print(f"Герой {self.unit_id} ведет с собой солдата {soldier_to_follow.unit_id}")
        else:
            print("Ошибка: Переданный объект не является солдатом!")


# Создаем по одному герою для каждой команды
hero_team1 = Hero(unit_id=1, team=1)
hero_team2 = Hero(unit_id=2, team=2)

# Генерируем объекты-солдаты и добавляем их в соответствующие списки команд
soldiers_team1 = [Soldier(unit_id=i, team=1) for i in range(10)]
soldiers_team2 = [Soldier(unit_id=i, team=2) for i in range(8)]

# Измеряем длину списков солдат и выводим на экран
length_team1 = len(soldiers_team1)
length_team2 = len(soldiers_team2)
print(f"Длина списка солдат команды 1: {length_team1}")
print(f"Длина списка солдат команды 2: {length_team2}")

# Увеличиваем уровень героя той команды, у которой больше солдат
if length_team1 > length_team2:
    hero_team1.increase_level()
else:
    hero_team2.increase_level()

# Отправляем первого солдата первого героя следовать за ним
if length_team1 > 0:
    soldier_to_follow = soldiers_team1[0]
    hero_team1.follow_hero(soldier_to_follow)
    # Выводим идентификационные номера этих двух юнитов
    print(f"Идентификационный номер героя: {hero_team1.unit_id}")
    print(f"Идентификационный номер солдата: {soldier_to_follow.unit_id}")
else:
    print("Нет солдат для следования за героем команды 1")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Для себя (другого себя через пол года =))) )
'''
'''
Краткое описание:

Данный код представляет собой пример объектно-ориентированного программирования на языке Python.
В нем создаются классы Unit, Soldier, и Hero, представляющие базовый класс юнита, класс солдата и класс героя
 соответственно. Объекты этих классов имеют уникальный идентификационный номер и принадлежат к какой-то команде.

В основной части программы создаются по одному герою для каждой команды, генерируются списки солдат для каждой команды,
измеряется длина этих списков и выводится на экран. 
Уровень героя увеличивается для команды с более длинным списком солдат.

Один из солдат первого героя отправляется следовать за ним, 
и идентификационные номера героя и солдата выводятся на экран.
'''
'''
Подробное описание:

Класс Unit:
__init__: Инициализирует объект класса с уникальным номером (unit_id) и принадлежностью к команде (team).

Класс Soldier (наследуется от Unit):
follow_hero(hero): Метод, который позволяет солдату следовать за героем.
Внутри метода добавлена проверка, что объект, переданный в качестве аргумента, является экземпляром класса Hero.
В случае успеха выводится сообщение о следовании.

Класс Hero (наследуется от Unit):
increase_level(): Увеличивает уровень героя и выводит сообщение.
follow_hero(soldier_to_follow): Метод, который позволяет герою вести с собой солдата. Внутри метода добавлена проверка,
что объект, переданный в качестве аргумента, является экземпляром класса Soldier. 
В случае успеха выводится сообщение о ведении солдата.

Создание героев и солдат:
Создаются по одному герою для каждой команды (например, hero_team1 и hero_team2).
Генерируются списки солдат для каждой команды (например, soldiers_team1 и soldiers_team2) с использованием списковых
включений.

Измерение длины списков солдат и вывод на экран:
Считается длина списков солдат для каждой команды и выводится на экран.

Увеличение уровня героя для команды с большим числом солдат:
Проверяется, у какой команды больше солдат, и соответствующему герою увеличивается уровень.

Отправка солдата следовать за героем и вывод их идентификационных номеров:
Если в команде есть солдаты, выбирается первый солдат из списка, и герой отправляет его следовать за собой.
Идентификационные номера героя и солдата выводятся на экран.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
Рекомендации по улучшению кода:

1. Добавлена проверка в методе follow_hero для класса Hero, чтобы удостовериться, что объект,
переданный в качестве аргумента, действительно является экземпляром класса Soldier.
2. Добавлены комментарии, объясняющие назначение и ожидаемые аргументы для методов follow_hero.
3. Внесены изменения в код согласно рекомендациям.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''

'''
В коде используется конструкция if-else для определения, кому из двух героев увеличить уровень. 
Давайте разберем, почему это нужно:
'''
'''
1. Создание героев:
'''
hero_team1 = Hero(unit_id=1, team=1)
hero_team2 = Hero(unit_id=2, team=2)
'''
2. Генерация солдат:
'''
soldiers_team1 = [Soldier(unit_id=i, team=1) for i in range(10)]
soldiers_team2 = [Soldier(unit_id=i, team=2) for i in range(8)]
'''
3. Измерение длины списков солдат:
'''
length_team1 = len(soldiers_team1)
length_team2 = len(soldiers_team2)
print(f"Длина списка солдат команды 1: {length_team1}")
print(f"Длина списка солдат команды 2: {length_team2}")
'''
4. Увеличение уровня героя той команды, у которой больше солдат:
'''
if length_team1 > length_team2:
    hero_team1.increase_level()
else:
    hero_team2.increase_level()
'''
Здесь проверяется условие: если длина списка солдат команды 1 (length_team1) больше длины списка солдат
команды 2 (length_team2), то вызывается метод increase_level для hero_team1, иначе - для hero_team2. 
Это позволяет увеличить уровень того героя, у которого больше солдат.
'''
'''
5. Отправление одного из солдат первого героя следовать за ним:
'''
if length_team1 > 0:
    soldier_to_follow = random.choice(soldiers_team1)
    hero_team1.follow_hero(soldier_to_follow)
    # Выводим идентификационные номера этих двух юнитов
    print(f"Идентификационный номер героя: {hero_team1.unit_id}")
    print(f"Идентификационный номер солдата: {soldier_to_follow.unit_id}")
else:
    print("Нет солдат для следования за героем команды 1")
'''
Здесь проверяется условие: если длина списка солдат команды 1 больше 0, то выбирается 
случайный солдат из списка soldiers_team1 и вызывается метод follow_hero для героя hero_team1. 
Иначе выводится сообщение о том, что нет солдат для следования за героем команды 1.
'''
'''
Таким образом, конструкция if-else используется для принятия решения в 
зависимости от условия (количество солдат в каждой из команд) в ходе выполнения программы.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Вариант №2
'''
import random

# Базовый класс для всех юнитов
class Unit:
    def __init__(self, id, team):
        self.id = id        # Уникальный номер объекта
        self.team = team    # Принадлежность к команде

# Класс для солдат, наследуется от базового класса Unit
class Soldier(Unit):
    def follow_hero(self, hero):
        print(f"Солдат {self.id} следует за героем {hero.id}.")

# Класс для героев, также наследуется от базового класса Unit
class Hero(Unit):
    def increase_level(self):
        print(f"Уровень героя {self.id} увеличен.")

# Создаем героев
hero_team1 = Hero(id=1, team=1)
hero_team2 = Hero(id=2, team=2)

# Создаем солдат
soldiers_team1 = [Soldier(id=i, team=1) for i in range(1, 6)]
soldiers_team2 = [Soldier(id=i, team=2) for i in range(6, 11)]

# Измеряем длину списков солдат
len_team1 = len(soldiers_team1)
len_team2 = len(soldiers_team2)

# Выводим длину списков на экран
print(f"Длина списка солдат команды 1: {len_team1}")
print(f"Длина списка солдат команды 2: {len_team2}")

# Увеличиваем уровень героя команды с более длинным списком
if len_team1 > len_team2:
    hero_team1.increase_level()
else:
    hero_team2.increase_level()

# Отправляем одного из солдат следовать за героем
random_soldier = random.choice(soldiers_team1 + soldiers_team2)
random_soldier.follow_hero(hero_team1 if random_soldier.team == 1 else hero_team2)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1
'''
class Unit:
''''
Пример кода:
''''
def __init__(self, id, team):
    self.id = id  # Уникальный номер объекта
    self.team = team  # Принадлежность к команде
'''
Описание кода или функции:
Этот код определяет базовый класс Unit для всех юнитов в игре. У него есть конструктор __init__, 
который инициализирует уникальный номер объекта (id) и принадлежность к команде (team).
'''
'''
Шаг №2
'''
class Soldier(Unit):
''''
Пример кода:
''''
def follow_hero(self, hero):
    print(f"Солдат {self.id} следует за героем {hero.id}.")
'''
Описание кода или функции:
Этот код определяет класс Soldier, который наследуется от класса Unit. У него есть метод follow_hero,
который принимает объект типа "герой" и выводит сообщение о том, что солдат следует за героем.
'''
'''
Шаг №3
'''
class Hero(Unit):
''''
Пример кода:
''''
def increase_level(self):
    print(f"Уровень героя {self.id} увеличен.")
'''
Описание кода или функции:
Этот код определяет класс Hero, также наследуемый от класса Unit.
У него есть метод increase_level, который выводит сообщение о том, что уровень героя увеличен.
'''
'''
Шаг №4
'''
hero_team1 = Hero(id=1, team=1)
hero_team2 = Hero(id=2, team=2)
'''
Описание кода:
Создаются два объекта героев, представляющих команды 1 и 2.
'''
'''
Шаг №5
'''
soldiers_team1 = [Soldier(id=i, team=1) for i in range(1, 6)]
soldiers_team2 = [Soldier(id=i, team=2) for i in range(6, 11)]
'''
Описание кода:
Создаются списки солдат для каждой команды. В цикле создаются объекты солдат с уникальными номерами и 
принадлежностью к команде.
'''
'''
Шаг №6
'''
len_team1 = len(soldiers_team1)
len_team2 = len(soldiers_team2)
'''
Описание кода:
Измеряется длина списков солдат для обеих команд.
'''
'''
Шаг №7
'''
print(f"Длина списка солдат команды 1: {len_team1}")
print(f"Длина списка солдат команды 2: {len_team2}")
'''
Описание кода:
Выводится на экран длина списков солдат для обеих команд.
'''
'''
Шаг №8
'''
if len_team1 > len_team2:
    hero_team1.increase_level()
else:
    hero_team2.increase_level()
'''
Описание кода:
Увеличивается уровень героя той команды, у которой больше длина списка солдат.
'''
'''
Шаг №9
'''
random_soldier = random.choice(soldiers_team1 + soldiers_team2)
random_soldier.follow_hero(hero_team1 if random_soldier.team == 1 else hero_team2)
'''
Описание кода:
Случайным образом выбирается один солдат из общего списка, и он отправляется следовать
за героем соответствующей команды. Выводится сообщение о следовании.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Рекомендации к рассмотрению:
В коде уже используется наследование и полиморфизм, что хорошо соответствует принципам ООП.

Можно добавить проверки на валидность входных данных при создании объектов 
(например, что id и team являются корректными значениями).

Для более строгой инкапсуляции можно было бы объявить атрибуты id и team в классе Unit как приватные с помощью
двойного подчеркивания (__id, __team).

Рассмотрите возможность использования стандартного модуля enum для удобного представления команд.

Комментарии в коде облегчают его понимание, но их можно расширить, если у вас есть более сложная логика или
особенности, которые стоит выделить.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
import random
from enum import Enum

class Team(Enum):
    TEAM1 = 1
    TEAM2 = 2

class Unit:
    def __init__(self, id, team):
        """
        Конструктор базового класса для всех юнитов.

        :param id: Уникальный номер объекта
        :param team: Принадлежность к команде (используется enum Team)
        """
        self.__id = id
        self.__team = team

class Soldier(Unit):
    def follow_hero(self, hero):
        """
        Метод для солдата, который следует за героем.

        :param hero: Объект типа Hero
        """
        print(f"Солдат {self._Unit__id} следует за героем {hero._Unit__id}.")

class Hero(Unit):
    def increase_level(self):
        """
        Метод для увеличения уровня героя.
        """
        print(f"Уровень героя {self._Unit__id} увеличен.")

# Создаем героев
hero_team1 = Hero(id=1, team=Team.TEAM1)
hero_team2 = Hero(id=2, team=Team.TEAM2)

# Создаем солдат
soldiers_team1 = [Soldier(id=i, team=Team.TEAM1) for i in range(1, 6)]
soldiers_team2 = [Soldier(id=i, team=Team.TEAM2) for i in range(6, 11)]

# Измеряем длину списков солдат
len_team1 = len(soldiers_team1)
len_team2 = len(soldiers_team2)

# Выводим длину списков на экран
print(f"Длина списка солдат команды 1: {len_team1}")
print(f"Длина списка солдат команды 2: {len_team2}")

# Увеличиваем уровень героя команды с более длинным списком
if len_team1 > len_team2:
    hero_team1.increase_level()
else:
    hero_team2.increase_level()

# Отправляем одного из солдат следовать за героем
random_soldier = random.choice(soldiers_team1 + soldiers_team2)
random_soldier.follow_hero(hero_team1 if random_soldier._Unit__team == Team.TEAM1 else hero_team2)
'''
Изменения включают в себя:

1. Использование enum Team для более читаемого представления команд.
2. Добавление комментариев к конструктору и методам классов.
3. Приватизация атрибутов id и team с использованием двойного подчеркивания.
4. Обновление вывода сообщений в методах для использования приватных атрибутов.


Эти изменения делают код более читаемым и обеспечивают более строгую инкапсуляцию.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
                              '''     ООП. Множественное наследование     '''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполните следующие задания:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание № 1
'''
'''
Задан класс Point, описывающий точку с координатами x, y на координатной плоскости.

Используя механизм наследования, нужно расширить возможности класса Point путем добавления нового атрибута цвета.
Для этого реализовать подкласс PointColor.

В классе Point реализовать следующие атрибуты:
− координаты точки;
− метод инициализации, который получает 2 параметра — координаты точки x, y;
− метод вычисления расстояния от точки до начала координат;
− метод getPoint(), который возвращает точку в виде списка.

В подклассе PointColor реализовать следующие атрибуты:
− цвет точки color;
− метод начальной инициализации, который получает 3 параметра: координаты точки и цвет;
− метод доступа к цвету color с именем getColor().
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание № 2
'''
'''
Создать базовый класс «Домашнее животное» и производные классы «Собака», «Кошка», «Попугай», «Хомяк».
С помощью конструктора установить имя каждого животного и его характеристики.

Реализуйте для каждого из классов методы:
• Sound — издает звук животного (пишем текстом в консоль);
• Show — отображает имя животного;
• Type — отображает название его подвида.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание № 3
'''
'''
Создать базовый класс Employer (служащий) с функцией Print().

Она должна выводить информацию о служащем. 
В случае базового класса это может быть строка с надписью This is Employer class.

Создайте от него три производных класса: President, Manager, Worker.
Переопределите функцию Print() для вывода информации, соответствующей каждому типу служащего.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание № 1: Классы Point и PointColor
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Этот код моделирует два класса, представляющих точки на координатной плоскости, 
иллюстрируя концепцию наследования в объектно-ориентированном программировании (ООП).
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
import math

class Point:
    def __init__(self, x, y):
        """
        Конструктор класса Point.

        :param x: Координата x
        :param y: Координата y
        """
        self.x = x
        self.y = y

    def distance_to_origin(self):
        """
        Метод для вычисления расстояния от точки до начала координат.

        :return: Расстояние от точки до начала координат
        """
        return math.sqrt(self.x**2 + self.y**2)

    def get_point(self):
        """
        Метод, возвращающий точку в виде списка.

        :return: Список [x, y]
        """
        return [self.x, self.y]

class PointColor(Point):
    def __init__(self, x, y, color):
        """
        Конструктор класса PointColor.

        :param x: Координата x
        :param y: Координата y
        :param color: Цвет точки
        """
        super().__init__(x, y)
        self.color = color

    def get_color(self):
        """
        Метод доступа к цвету точки.

        :return: Цвет точки
        """
        return self.color

# Пример использования классов
point1 = Point(3, 4)
print("Point1 - Distance to origin:", point1.distance_to_origin())
print("Point1 - Point:", point1.get_point())

point_color1 = PointColor(1, 2, "red")
print("PointColor1 - Distance to origin:", point_color1.distance_to_origin())
print("PointColor1 - Point:", point_color1.get_point())
print("PointColor1 - Color:", point_color1.get_color())
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1. Описание класса Point:
'''
import math

class Point:
    def __init__(self, x, y):
        """
        Конструктор класса Point.

        :param x: Координата x
        :param y: Координата y
        """
        self.x = x
        self.y = y

    def distance_to_origin(self):
        """
        Метод для вычисления расстояния от точки до начала координат.

        :return: Расстояние от точки до начала координат
        """
        return math.sqrt(self.x**2 + self.y**2)

    def get_point(self):
        """
        Метод, возвращающий точку в виде списка.

        :return: Список [x, y]
        """
        return [self.x, self.y]
'''
Описание:

Конструктор __init__: Инициализирует объект класса Point с переданными координатами x и y.
Метод distance_to_origin: Вычисляет расстояние от точки до начала координат по формуле sqrt(x^2 + y^2).
Метод get_point: Возвращает координаты точки в виде списка [x, y].
'''
'''
Шаг №2. Описание класса PointColor (подкласс Point):
'''
class PointColor(Point):
    def __init__(self, x, y, color):
        """
        Конструктор класса PointColor.

        :param x: Координата x
        :param y: Координата y
        :param color: Цвет точки
        """
        super().__init__(x, y)
        self.color = color

    def get_color(self):
        """
        Метод доступа к цвету точки.

        :return: Цвет точки
        """
        return self.color
'''
Описание:

Конструктор __init__: Инициализирует объект класса PointColor, вызывая конструктор родительского класса Point и 
добавляя атрибут цвета.
Метод get_color: Возвращает цвет точки.
'''
'''
Шаг №3. Пример использования классов:
'''
# Пример использования классов
point1 = Point(3, 4)
print("Point1 - Distance to origin:", point1.distance_to_origin())
print("Point1 - Point:", point1.get_point())

point_color1 = PointColor(1, 2, "red")
print("PointColor1 - Distance to origin:", point_color1.distance_to_origin())
print("PointColor1 - Point:", point_color1.get_point())
print("PointColor1 - Color:", point_color1.get_color())
'''
Описание:

Создаются объекты point1 типа Point и point_color1 типа PointColor.
Выводятся результаты вызова методов: distance_to_origin(), get_point(), get_color() для обоих объектов.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание № 2: Классы "Домашнее животное", "Собака", "Кошка", "Попугай", "Хомяк"
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
class Pet:
    def __init__(self, name, age, breed, is_vaccinated):
        # Конструктор класса
        self.name = name
        self.__age = age  # Приватное поле для возраста
        self.breed = breed
        self.is_vaccinated = is_vaccinated

    def set_age(self, age):
        # Метод для установки возраста
        if 250 > age > 0:
            self.__age = age

    def get_age(self):
        # Метод для получения возраста
        return self.__age

    def inc_age(self, n=1):
        # Метод для увеличения возраста на n лет
        self.__age += n

    def make_sound(self):
        # Общий метод для издания звука животного
        print('Generic pet sound')

    def show(self):
        # Метод для отображения имени животного
        print(f"Name: {self.name}")

    def animal_type(self):
        # Метод для отображения общего типа животного
        print("Generic animal type")


class Dog(Pet):
    def make_sound(self):
        # Переопределенный метод для издания звука собаки
        print('Woof woof')

    def animal_type(self):
        # Переопределенный метод для отображения типа собаки
        print('Dog')


class Cat(Pet):
    def make_sound(self):
        # Переопределенный метод для издания звука кошки
        print('Meow')

    def animal_type(self):
        # Переопределенный метод для отображения типа кошки
        print('Cat')


class Parrot(Pet):
    def make_sound(self):
        # Переопределенный метод для издания звука попугая
        print('Squawk')

    def animal_type(self):
        # Переопределенный метод для отображения типа попугая
        print('Parrot')


class Hamster(Pet):
    def make_sound(self):
        # Переопределенный метод для издания звука хомяка
        print('Squeak')

    def animal_type(self):
        # Переопределенный метод для отображения типа хомяка
        print('Hamster')


# Пример использования

barky = Dog('Barky', 2, 'Mixed Breed', True)
meowster = Cat('Meowster', 3, 'Siamese', True)
polly = Parrot('Polly', 1, 'Ara', True)
nibbles = Hamster('Nibbles', 1, 'Dwarf', False)

pets = [barky, meowster, polly, nibbles]

for pet in pets:
    # В цикле вызываем методы каждого объекта
    pet.show()
    pet.make_sound()
    pet.animal_type()
    print("\n")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1: Определение базового класса "Домашнее животное" (Pet)
'''
# Пример кода:
class Pet:
    def __init__(self, name, age, breed, is_vaccinated):
        self.name = name
        self.__age = age
        self.breed = breed
        self.is_vaccinated = is_vaccinated

    def set_age(self, age):
        if 250 > age > 0:
            self.__age = age

    def get_age(self):
        return self.__age

    def inc_age(self, n=1):
        self.__age += n

    def make_sound(self):
        print('Generic pet sound')

    def show(self):
        print(f"Name: {self.name}")

    def animal_type(self):
        print("Generic animal type")
'''
Описание:

Создается класс Pet с конструктором для инициализации характеристик животного (имя, возраст, порода, привито ли).
Используется приватное поле __age для возраста, чтобы ограничить доступ извне.
Реализованы методы для установки возраста (set_age), получения возраста (get_age), увеличения возраста (inc_age).
Метод make_sound выводит общий звук животного, а метод show отображает имя животного.
animal_type выводит общий тип животного.
'''
'''
Шаг №2: Создание производных классов для каждого вида животного (Dog, Cat, Parrot, Hamster)
'''
# Пример кода:
class Dog(Pet):
    def make_sound(self):
        print('Woof woof')

    def animal_type(self):
        print('Dog')


class Cat(Pet):
    def make_sound(self):
        print('Meow')

    def animal_type(self):
        print('Cat')


class Parrot(Pet):
    def make_sound(self):
        print('Squawk')

    def animal_type(self):
        print('Parrot')


class Hamster(Pet):
    def make_sound(self):
        print('Squeak')

    def animal_type(self):
        print('Hamster')
'''
Описание:

Создаются отдельные классы для каждого вида домашнего животного (собака, кошка, попугай, хомяк).
Каждый класс наследует характеристики и методы базового класса Pet.
Метод make_sound переопределяется для издания специфичного звука каждого вида животного, а метод animal_type для
отображения конкретного типа.
'''
'''
Шаг №3: Пример использования классов
'''
# Пример кода:
barky = Dog('Barky', 2, 'Mixed Breed', True)
meowster = Cat('Meowster', 3, 'Siamese', True)
polly = Parrot('Polly', 1, 'Ara', True)
nibbles = Hamster('Nibbles', 1, 'Dwarf', False)

pets = [barky, meowster, polly, nibbles]

for pet in pets:
    pet.show()
    pet.make_sound()
    pet.animal_type()
    print("\n")
'''
Описание:

Создаются объекты различных классов, представляющих собой разные виды домашних животных.
Объекты добавляются в список pets.
В цикле выводятся информация о каждом животном с использованием методов show, make_sound, animal_type.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Еще один вариант для Задания № 2: Классы "Домашнее животное", "Собака", "Кошка", "Попугай", "Хомяк"
'''
class Pet:
    def __init__(self, name, breed):
        """
        Конструктор базового класса "Домашнее животное".

        :param name: Имя животного
        :param breed: Подвид животного
        """
        self.name = name
        self.breed = breed

    def sound(self):
        """
        Метод для издания звука животного.

        :return: Звук животного
        """
        print("Generic pet sound")

    def show(self):
        """
        Метод для отображения имени животного.

        :return: Имя животного
        """
        print(f"Name: {self.name}")

    def animal_type(self):
        """
        Метод для отображения подвида животного.

        :return: Подвид животного
        """
        print("Generic animal type")


class Dog(Pet):
    def sound(self):
        print("Woof woof")

    def animal_type(self):
        print("Dog")


class Cat(Pet):
    def sound(self):
        print("Meow")

    def animal_type(self):
        print("Cat")


class Parrot(Pet):
    def sound(self):
        print("Squawk")

    def animal_type(self):
        print("Parrot")


class Hamster(Pet):
    def sound(self):
        print("Squeak")

    def animal_type(self):
        print("Hamster")


# Пример использования

dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Siamese")
parrot = Parrot("Polly", "Ara")
hamster = Hamster("Nibbles", "Dwarf")

pets = [dog, cat, parrot, hamster]

for pet in pets:
    pet.show()
    pet.sound()
    pet.animal_type()
    print("\n")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1: Создание базового класса "Домашнее животное" (Pet):
'''
class Pet:
    def __init__(self, name, breed):
        """
        Конструктор базового класса "Домашнее животное".

        :param name: Имя животного
        :param breed: Подвид животного
        """
        self.name = name
        self.breed = breed

    def sound(self):
        """
        Метод для издания звука животного.

        :return: Звук животного
        """
        print("Generic pet sound")

    def show(self):
        """
        Метод для отображения имени животного.

        :return: Имя животного
        """
        print(f"Name: {self.name}")

    def animal_type(self):
        """
        Метод для отображения подвида животного.

        :return: Подвид животного
        """
        print("Generic animal type")
'''
Описание:

Создается базовый класс Pet с конструктором для инициализации имени и подвида животного.
Метод sound возвращает общий звук животного, show отображает имя, а animal_type отображает подвид.
'''
'''
Шаг №2: Создание производных классов для каждого вида животного (Dog, Cat, Parrot, Hamster):
'''
class Dog(Pet):
    def sound(self):
        print("Woof woof")

    def animal_type(self):
        print("Dog")


class Cat(Pet):
    def sound(self):
        print("Meow")

    def animal_type(self):
        print("Cat")


class Parrot(Pet):
    def sound(self):
        print("Squawk")

    def animal_type(self):
        print("Parrot")


class Hamster(Pet):
    def sound(self):
        print("Squeak")

    def animal_type(self):
        print("Hamster")
'''
Описание:

Создаются отдельные классы для каждого вида домашнего животного (собака, кошка, попугай, хомяк).
Каждый класс наследует характеристики и методы базового класса Pet.
Метод sound переопределяется для издания специфичного звука каждого вида животного, а метод animal_type для
отображения конкретного типа.
'''
'''
Шаг №3: Пример использования классов:
'''
# Пример использования

dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Siamese")
parrot = Parrot("Polly", "Ara")
hamster = Hamster("Nibbles", "Dwarf")

pets = [dog, cat, parrot, hamster]

for pet in pets:
    pet.show()
    pet.sound()
    pet.animal_type()
    print("\n")
'''
Описание:

Создаются объекты различных классов, представляющих собой разные виды домашних животных.
Объекты добавляются в список pets.
В цикле выводятся информация о каждом животном с использованием методов show, sound, animal_type.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Задание № 3: Классы Классы Employer, President, Manager, Worker
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# Определение базового класса Employer
class Employer:
    def print_info(self):
        """
        Функция для вывода информации о служащем.
        """
        print("This is Employer class.")

# Определение производного класса President, наследующего от Employer
class President(Employer):
    def print_info(self):
        # Переопределение метода print_info для класса President
        print("This is President class.")

# Определение производного класса Manager, наследующего от Employer
class Manager(Employer):
    def print_info(self):
        # Переопределение метода print_info для класса Manager
        print("This is Manager class.")

# Определение производного класса Worker, наследующего от Employer
class Worker(Employer):
    def print_info(self):
        # Переопределение метода print_info для класса Worker
        print("This is Worker class.")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Так как у нас есть комментарии, Мы можем попытаться разъяснить каждую часть кода:
'''
'''
1. Базовый класс Employer:

class Employer:: Определяет базовый класс Employer.
def print_info(self):: Определяет метод print_info для вывода информации о служащем.

2. Производные классы (President, Manager, Worker):

class President(Employer):, class Manager(Employer):, class Worker(Employer):: Определяют три производных класса, 
каждый из которых наследует от базового класса Employer.
def print_info(self):: Каждый производный класс переопределяет метод print_info базового класса для вывода информации, 
соответствующей своему типу служащего.

3. Пример использования:

employer = Employer()
president = President()
manager = Manager()
worker = Worker()

employers = [employer, president, manager, worker]

for emp in employers:
    emp.print_info()


Созданы объекты каждого класса.
Объекты добавлены в список employers.
В цикле вызывается метод print_info() для каждого объекта, что приводит к выводу соответствующей информации
о типе служащего.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #


# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #




