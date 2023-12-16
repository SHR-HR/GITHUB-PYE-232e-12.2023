# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Дата: 22-23 ноября 2023

# Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
# Дисциплина: Основы программирования на Python

# Урок №8 - от 22.11.2023 - Домашняя работа № 7 Функции. Модули, библиотеки и пакеты

# Выполните следующие задания:~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Задание №1.

# Дано: ↓

# Реализовать инженерный калькулятор, для всех арифметических действий, включая нахождение факториала,
# Фибоначчи, и всех тригонометрических функций, также возведения числа в степени.
# В ходе решения, допустимо использования модуля math, функции определяемой пользователем,
# рекурсивной функции и лямбда-функции.

# Реализуйте диалог с пользователем.

# Решение:

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Вариант №1. ↓ (Думаю ограничусь несколькими вариантами, так как нехватает времени на решения других задач)

import math
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# Добавьте другие необходимые функции для тригонометрии и возведения в степень
def main():
    print("Добро пожаловать в инженерный калькулятор!")
    while True:
        print("\nВыберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Факториал")
        print("7. Число Фибоначчи")
        print("8. Тригонометрические функции")
        print("0. Выход")
        choice = input("Введите номер операции (0-8): ")
        if choice == '0':
            print("До свидания!")
            break
        elif choice in ('1', '2', '3', '4', '5'):
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            if choice == '1':
                result = num1 + num2
            elif choice == '2':
                result = num1 - num2
            elif choice == '3':
                result = num1 * num2
            elif choice == '4':
                result = num1 / num2
            elif choice == '5':
                result = math.pow(num1, num2)
            print(f"Результат: {result}")
        elif choice == '6':
            num = int(input("Введите число для вычисления факториала: "))
            result = factorial(num)
            print(f"Факториал {num}: {result}")
        elif choice == '7':
            num = int(input("Введите порядковый номер числа Фибоначчи: "))
            result = fibonacci(num)
            print(f"Число Фибоначчи под номером {num}: {result}")
        elif choice == '8':
            angle = float(input("Введите угол в градусах: "))
            print(f"Синус: {math.sin(math.radians(angle))}")
            print(f"Косинус: {math.cos(math.radians(angle))}")
            print(f"Тангенс: {math.tan(math.radians(angle))}")
        else:
            print("Неверный ввод. Попробуйте снова.")
if __name__ == "__main__":
    main()

# Шаг №1. - Тут все просто! Нам нужно импортировать библиотеку math
import math
# Эта строка кода импортирует библиотеку math, которая предоставляет различные математические функции,
# такие как тригонометрические, логарифмические, арифметические операции, и другие. Мы будем использовать эту
# библиотеку для выполнения некоторых математических операций в калькуляторе.

# Шаг №2. - Затем нам нужно записать определение функции factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
# Эта функция вычисляет факториал числа n.
# Факториал числа - это произведение всех положительных целых чисел от 1 до этого числа.
# В данной функции используется рекурсия (функция вызывает сама себя), чтобы рассчитать факториал.

# Шаг №3. - Теперь нужно записать определение функции fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
# Эта функция вычисляет число Фибоначчи с использованием рекурсии.
# Числа Фибоначчи - это последовательность чисел, где каждое число равно сумме двух предыдущих чисел
# (последовательность начинается с 0 и 1).

# Шаг №4. - Затем следует определение главной функции main
def main():
    print("Добро пожаловать в инженерный калькулятор!")
    while True:
        # Выводим меню операций
        print("\nВыберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Факториал")
        print("7. Число Фибоначчи")
        print("8. Тригонометрические функции")
        print("0. Выход")
        # Получаем выбор пользователя
        choice = input("Введите номер операции (0-8): ")
# Эта функция представляет главный блок кода, который взаимодействует с пользователем.
# Она содержит бесконечный цикл while, который выполняется, пока пользователь не выберет операцию "0" для выхода.
# Функция выводит меню операций и запрашивает у пользователя выбор.

# Шаг №5. - Обработка выбора
        if choice == '0':
            print("До свидания!")
            break
        elif choice in ('1', '2', '3', '4', '5'):
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            # Выполняем арифметическую операцию в зависимости от выбора пользователя
            if choice == '1':
                result = num1 + num2
            elif choice == '2':
                result = num1 - num2
            elif choice == '3':
                result = num1 * num2
            elif choice == '4':
                result = num1 / num2
            elif choice == '5':
                result = math.pow(num1, num2)
# В этой части кода происходит обработка выбора пользователя.
# Если пользователь выбирает операцию от 1 до 5, программа запрашивает два числа (если это необходимо)
# и выполняет соответствующую арифметическую операцию.

# Шаг №6. - Обработка других операций
        elif choice == '6':
            num = int(input("Введите число для вычисления факториала: "))
            result = factorial(num)
            print(f"Факториал {num}: {result}")
        elif choice == '7':
            num = int(input("Введите порядковый номер числа Фибоначчи: "))
            result = fibonacci(num)
            print(f"Число Фибоначчи под номером {num}: {result}")
        elif choice == '8':
            angle = float(input("Введите угол в градусах: "))
            print(f"Синус: {math.sin(math.radians(angle))}")
            print(f"Косинус: {math.cos(math.radians(angle))}")
            print(f"Тангенс: {math.tan(math.radians(angle))}")
# Тут мы обрабатываем другие операции,
# такие как вычисление факториала, числа Фибоначчи и тригонометрических функций.
# Здесь также используются функции, которые мы определили ранее (factorial и fibonacci),
# а также функции из модуля math для тригонометрии.

# Шаг №7. - Обработка ошибочного ввода
        else:
            print("Неверный ввод. Попробуйте снова.")
# Если пользователь вводит что-то, что не соответствует ни одной из операций,
# программа выдаст сообщение об ошибке и попросит пользователя ввести данные снова.

# Шаг №8. - Запуск главной функции
if __name__ == "__main__":
    main()
# Этот блок кода проверяет, запущен ли файл напрямую (а не импортирован как модуль).
# Если он запускается напрямую, программа вызывает функцию main(),
# и весь процесс начинается с вывода приветствия и отображения меню операций.

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Вариант №2. ↓

import math
# Определение функции для вычисления факториала
factorial = lambda n: 1 if n == 0 or n == 1 else n * factorial(n-1)
# Определение функции для вычисления числа Фибоначчи
fibonacci = lambda n: n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
# Словарь с операциями
operations = {
    '1': lambda x, y: x + y,
    '2': lambda x, y: x - y,
    '3': lambda x, y: x * y,
    '4': lambda x, y: x / y,
    '5': lambda x, y: math.pow(x, y),
    '6': lambda x: factorial(x),
    '7': lambda x: fibonacci(x),
    '8': lambda angle: (math.sin(math.radians(angle)), math.cos(math.radians(angle)), math.tan(math.radians(angle)))
}
# Главная функция
def main():
    print("Добро пожаловать в инженерный калькулятор!")
    while True:
        print("\nВыберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Факториал")
        print("7. Число Фибоначчи")
        print("8. Тригонометрические функции")
        print("0. Выход")
        choice = input("Введите номер операции (0-8): ")
        if choice == '0':
            print("До свидания!")
            break
        if choice in operations:
            try:
                if choice in ['6', '7', '8']:
                    num = float(input(f"Введите число для операции {choice}: "))
                    result = operations[choice](num)
                else:
                    num1 = float(input("Введите первое число: "))
                    num2 = float(input("Введите второе число: "))
                    result = operations[choice](num1, num2)
                print(f"Результат: {result}")
            except ValueError:
                print("Ошибка ввода. Введите корректные числа.")
        else:
            print("Неверный ввод. Попробуйте снова.")
if __name__ == "__main__":
    main()

# Шаг №1. - Импорт библиотеки math
import math
# Также, как и в предыдущем примере, мы импортируем библиотеку math, чтобы использовать математические функции.

# Шаг №2. - Определение лямбда-функций
# Определение функции для вычисления факториала
factorial = lambda n: 1 if n == 0 or n == 1 else n * factorial(n-1)
# Определение функции для вычисления числа Фибоначчи
fibonacci = lambda n: n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
# Здесь мы используем лямбда-функции для вычисления факториала и чисел Фибоначчи.
# Лямбда-функции - это анонимные функции, которые можно использовать там, где требуется короткая функция.

# Шаг №3. - Создание словаря с операциями
# Словарь с операциями
operations = {
    '1': lambda x, y: x + y,
    '2': lambda x, y: x - y,
    '3': lambda x, y: x * y,
    '4': lambda x, y: x / y,
    '5': lambda x, y: math.pow(x, y),
    '6': lambda x: factorial(x),
    '7': lambda x: fibonacci(x),
    '8': lambda angle: (math.sin(math.radians(angle)), math.cos(math.radians(angle)), math.tan(math.radians(angle)))
}
# Мы создаем словарь operations, где каждой операции соответствует лямбда-функция для её выполнения.
# Если пользователь выбирает определенную операцию, мы просто вызываем соответствующую лямбда-функцию из словаря.

# Шаг №4. - Главная функция main
def main():
    print("Добро пожаловать в инженерный калькулятор!")

    while True:
        print("\nВыберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Факториал")
        print("7. Число Фибоначчи")
        print("8. Тригонометрические функции")
        print("0. Выход")

        choice = input("Введите номер операции (0-8): ")
# Это главная функция, которая взаимодействует с пользователем.
# Она выводит меню операций и запрашивает выбор пользователя.

# Шаг №5. - Обработка выбора пользователя
        if choice == '0':
            print("До свидания!")
            break
        if choice in operations:
            try:
                if choice in ['6', '7', '8']:
                    num = float(input(f"Введите число для операции {choice}: "))
                    result = operations[choice](num)
                else:
                    num1 = float(input("Введите первое число: "))
                    num2 = float(input("Введите второе число: "))
                    result = operations[choice](num1, num2)
                print(f"Результат: {result}")
            except ValueError:
                print("Ошибка ввода. Введите корректные числа.")
        else:
            print("Неверный ввод. Попробуйте снова.")
# Если пользователь выбирает операцию, программа проверяет, есть ли такая операция в словаре operations.
# Если есть, она запрашивает необходимые данные (числа или угол) и выполняет соответствующую лямбда-функцию из словаря.
# Обработка ошибок также добавлена с использованием блока try-except, чтобы обработать возможные ошибки ввода данных.

# Шаг №6. - Запуск главной функции
if __name__ == "__main__":
    main()
# Этот блок кода проверяет, запущен ли файл напрямую, и если да, вызывает функцию main().
# Это позволяет использовать этот код как самостоятельную программу или как модуль, если он импортируется в другой файл.


# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Задание №2.

# Дано: ↓

# Написать игру крестики-нолики.
#
#
# Output:
# ********** Игра Крестики-нолики для двух игроков **********
# -------------
# | 1 | 2 | 3 |
# -------------
# | 4 | 5 | 6 |
# -------------
# | 7 | 8 | 9 |
# -------------
# Куда поставим X? 5
# -------------
# | 1 | 2 | 3 |
# -------------
# | 4 | X | 6 |
# -------------
# | 7 | 8 | 9 |
# -------------
# Куда поставим O? 3
# -------------
# | 1 | 2 | O |
# -------------
# | 4 | X | 6 |
# -------------
# | 7 | 8 | 9 |
# -------------
# Куда поставим X? 4
# -------------
# | 1 | 2 | O |
# -------------
# | X | X | 6 |
# -------------
# | 7 | 8 | 9 |
# -------------
# Куда поставим O? 2
# -------------
# | 1 | O | O |
# -------------
# | X | X | 6 |
# -------------
# | 7 | 8 | 9 |
# -------------
# Куда поставим X? 6
# X выиграл!

# Решение:

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Вариант №1. ↓

def print_board(board):
    print("-------------")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("-------------")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("-------------")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("-------------")
def check_winner(board, player):
    # Проверка по горизонтали, вертикали и диагоналям
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False
def is_board_full(board):
    return all(cell == 'X' or cell == 'O' for cell in board)
def tic_tac_toe():
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    player = 'X'
    print("********** Игра Крестики-нолики для двух игроков **********")
    print_board(board)
    while True:
        move = input(f"Куда поставим {player}? ")
        try:
            move = int(move)
            if 1 <= move <= 9 and board[move - 1] != 'X' and board[move - 1] != 'O':
                board[move - 1] = player
                print_board(board)
                if check_winner(board, player):
                    print(f"{player} выиграл!")
                    break
                elif is_board_full(board):
                    print("Ничья!")
                    break
                player = 'O' if player == 'X' else 'X'
            else:
                print("Некорректный ход. Попробуйте еще раз.")
        except ValueError:
            print("Введите число от 1 до 9.")
if __name__ == "__main__":
    tic_tac_toe()

# Шаг №1. - Функция print_board
def print_board(board):
    print("-------------")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("-------------")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("-------------")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("-------------")
# Эта функция принимает доску в виде списка и отображает текущее состояние игрового поля в текстовом виде.

# Шаг №2. - Функция check_winner
def check_winner(board, player):
    # Проверка по горизонтали, вертикали и диагоналим
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]

    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False
# Эта функция проверяет, есть ли выигрышное состояние для указанного игрока.
# Она проверяет горизонтали, вертикали и диагонали доски.

# Шаг №3. - Функция is_board_full
def is_board_full(board):
    return all(cell == 'X' or cell == 'O' for cell in board)
# Эта функция проверяет, заполнена ли доска, то есть все клетки заняты символами 'X' или 'O'.

# Шаг №4. -  Главная функция tic_tac_toe
def tic_tac_toe():
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    player = 'X'

    print("********** Игра Крестики-нолики для двух игроков **********")
    print_board(board)

    while True:
        move = input(f"Куда поставим {player}? ")

        try:
            move = int(move)
            if 1 <= move <= 9 and board[move - 1] != 'X' and board[move - 1] != 'O':
                board[move - 1] = player
                print_board(board)

                if check_winner(board, player):
                    print(f"{player} выиграл!")
                    break
                elif is_board_full(board):
                    print("Ничья!")
                    break

                player = 'O' if player == 'X' else 'X'
            else:
                print("Некорректный ход. Попробуйте еще раз.")
        except ValueError:
            print("Введите число от 1 до 9.")
# Это главная функция игры. Она инициализирует доску и начинает бесконечный цикл, где каждый игрок (X или O)
# совершает ход. Программа проверяет ввод на корректность, обновляет доску и проверяет, не закончилась ли игра
# (выигрыш или ничья). После завершения игры программа сообщает о результате.

# Шаг №5. - Запуск главной функции
if __name__ == "__main__":
    tic_tac_toe()
# Этот блок кода проверяет, запущен ли файл напрямую, и если да, вызывает функцию tic_tac_toe.
# Это позволяет использовать этот код как самостоятельную программу или как модуль, если он импортируется в другой файл.

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Вариант №2. ↓

class TicTacToe:
    def __init__(self):
        self.board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.current_player = 'X'
    def print_board(self):
        print("-------------")
        for i in range(0, 9, 3):
            print(f"| {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} |")
            print("-------------")
    def make_move(self, position):
        try:
            position = int(position)
            if 1 <= position <= 9 and self.board[position - 1] != 'X' and self.board[position - 1] != 'O':
                self.board[position - 1] = self.current_player
                return True
            else:
                print("Некорректный ход. Попробуйте еще раз.")
                return False
        except ValueError:
            print("Введите число от 1 до 9.")
            return False
    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]

        for condition in win_conditions:
            if all(self.board[i] == self.current_player for i in condition):
                return True
        return False
    def is_board_full(self):
        return all(cell == 'X' or cell == 'O' for cell in self.board)

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
def main():
    game = TicTacToe()
    print("********** Игра Крестики-нолики для двух игроков **********")
    while True:
        game.print_board()
        move = input(f"Куда поставим {game.current_player}? ")
        if game.make_move(move):
            if game.check_winner():
                game.print_board()
                print(f"{game.current_player} выиграл!")
                break
            elif game.is_board_full():
                game.print_board()
                print("Ничья!")
                break
            else:
                game.switch_player()
if __name__ == "__main__":
    main()

# Шаг №1. - Класс TicTacToe и его конструктор
class TicTacToe:
    def __init__(self):
        self.board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.current_player = 'X'
# Здесь создается класс TicTacToe, который будет представлять игру.
# В конструкторе устанавливается начальное состояние игрового поля (self.board) и текущего игрока (self.current_player).

# Шаг №2. - Метод print_board
    def print_board(self):
        print("-------------")
        for i in range(0, 9, 3):
            print(f"| {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} |")
            print("-------------")
# Метод print_board отвечает за вывод текущего состояния игрового поля. Он использует цикл для перебора строк
# и столбцов и выводит содержимое каждой ячейки.

# Шаг №3. - Метод make_move
    def make_move(self, position):
        try:
            position = int(position)
            if 1 <= position <= 9 and self.board[position - 1] != 'X' and self.board[position - 1] != 'O':
                self.board[position - 1] = self.current_player
                return True
            else:
                print("Некорректный ход. Попробуйте еще раз.")
                return False
        except ValueError:
            print("Введите число от 1 до 9.")
            return False
# Метод make_move отвечает за обработку хода игрока. Он проверяет, является ли введенная позиция числом от 1 до 9 и не
# занята ли уже. Если все условия выполняются, ход совершается, и метод возвращает True, иначе - False.

# Шаг №4. - Метод check_winner
    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]

        for condition in win_conditions:
            if all(self.board[i] == self.current_player for i in condition):
                return True
        return False
# Метод check_winner проверяет, есть ли выигрышное состояние для текущего игрока.
# Он проверяет горизонтали, вертикали и диагонали.

# Шаг №5. - Метод is_board_full
    def is_board_full(self):
        return all(cell == 'X' or cell == 'O' for cell in self.board)
# Метод is_board_full проверяет, заполнено ли игровое поле, то есть все ячейки заняты.

# Шаг №6. -  Метод switch_player
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
# Метод switch_player переключает текущего игрока между 'X' и 'O'.

# Шаг №7. - Функция main
def main():
    game = TicTacToe()
    print("********** Игра Крестики-нолики для двух игроков **********")

    while True:
        game.print_board()
        move = input(f"Куда поставим {game.current_player}? ")

        if game.make_move(move):
            if game.check_winner():
                game.print_board()
                print(f"{game.current_player} выиграл!")
                break
            elif game.is_board_full():
                game.print_board()
                print("Ничья!")
                break
            else:
                game.switch_player()
# Это функция main, которая представляет собой основной цикл игры. Внутри цикла выводится текущее состояние доски,
# запрашивается ход от текущего игрока, и программа проверяет, закончена ли игра. Если игра закончена,
# выводится соответствующее сообщение. В противном случае переключается текущий игрок.

# Шаг №8. - Запуск главной функции
if __name__ == "__main__":
    main()
# Этот блок кода проверяет, запущен ли файл напрямую, и если да, вызывает функцию main. Это позволяет использовать
# этот код как самостоятельную программу или как модуль, если он импортируется в другой файл.



# Модули и пакеты: ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Задание №1. - Спроектировать программу для определения победителя на выборах.

# Дано: ↓

# Пользователю предоставляется список кандидатов, каждый из голосующих делает свой выбор.
# Выбранный кандидат добавляется в список. В итоге имеется неизменяемый список кандидатов.

# Определить победителя, в зависимости от количества встречаемости в списке кандидата.
# Определить количество голосов победителя.
# В случае, если будет двое победителей, сделать сортировку по длине слова между ними и выбрать
# победителя с минимальным количеством букв в имени.

# Кандидаты в выборы: Шаунин, Новичихина, Калиев, Цой, Шудабаев, Кадырова, Исабекова, Сариев, Изденов, Ким, Смагулова,
# Әбілхайыр, Зуев, Сериккалиев, Годун, Камбарбаев, Жабыков, Токаев, Путин, Лукашенко, Трамп и т.д.
# Вы отдаете голос за:
# Победитель выборов: Шаунин.
# Решение:

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Вариант №1. ↓

def get_candidates():
    """
    Функция, возвращающая список кандидатов.
    """
    return ["Шаунин", "Новичихина", "Калиев", "Цой", "Шудабаев", "Кадырова", "Исабекова",
            "Сариев", "Изденов", "Ким", "Смагулова", "Әбілхайыр", "Зуев", "Сериккалиев",
            "Годун", "Камбарбаев", "Токаев", "Путин", "Лукашенко", "Трамп"]
def vote(candidates, votes):
    """
    Функция для голосования. Возвращает обновленный словарь голосов.
    """
    print("Кандидаты в выборах:", ", ".join(candidates))
    choice = input("На кого вы отдаете голос? ")
    while choice not in candidates:
        print("Некорректный выбор. Попробуйте еще раз.")
        choice = input("На кого вы отдаете голос? ")
    votes[choice] = votes.get(choice, 0) + 1
    return votes
def determine_winner(votes):
    """
    Функция для определения победителя и количества голосов.
    """
    sorted_votes = sorted(votes.items(), key=lambda x: (-x[1], len(x[0])))
    if len(sorted_votes) == 1 or sorted_votes[0][1] > sorted_votes[1][1]:
        winner, votes_count = sorted_votes[0]
    else:
        # В случае двух победителей с одинаковым количеством голосов, выбираем с меньшим количеством букв в имени
        winner, votes_count = min(sorted_votes, key=lambda x: len(x[0]))
    return winner, votes_count
def main():
    candidates = get_candidates()
    votes = {}
    while True:
        votes = vote(candidates, votes)
        another_vote = input("Желаете проголосовать еще? (да/нет) ").lower()
        if another_vote != 'да':
            break
    winner, votes_count = determine_winner(votes)
    print(f"Победитель выборов: {winner} с количеством голосов: {votes_count}")
if __name__ == "__main__":
    main()

# Хух! Преступим!

# Шаг №1. - Функция get_candidates
def get_candidates():
    """
    Функция, возвращающая список кандидатов.
    """
    return ["Шаунин", "Новичихина", "Калиев", "Цой", "Шудабаев", "Кадырова", "Исабекова",
            "Сариев", "Изденов", "Ким", "Смагулова", "Әбілхайыр", "Зуев", "Сериккалиев",
            "Годун", "Камбарбаев", "Токаев", "Путин", "Лукашенко", "Трамп"]
# Эта функция возвращает список кандидатов.
# Он используется для определения, за кого пользователь может отдать свой голос.

# Шаг №2. - Функция vote
def vote(candidates, votes):
    """
    Функция для голосования. Возвращает обновленный словарь голосов.
    """
    print("Кандидаты в выборах:", ", ".join(candidates))
    choice = input("На кого вы отдаете голос? ")

    while choice not in candidates:
        print("Некорректный выбор. Попробуйте еще раз.")
        choice = input("На кого вы отдаете голос? ")

    votes[choice] = votes.get(choice, 0) + 1
    return votes
# Эта функция предоставляет возможность пользователю отдать голос за кандидата.
# Она запрашивает выбор пользователя, проверяет его корректность, обновляет словарь голосов и возвращает его.

# Шаг №3. - Функция determine_winner
def determine_winner(votes):
    """
    Функция для определения победителя и количества голосов.
    """
    sorted_votes = sorted(votes.items(), key=lambda x: (-x[1], len(x[0])))

    if len(sorted_votes) == 1 or sorted_votes[0][1] > sorted_votes[1][1]:
        winner, votes_count = sorted_votes[0]
    else:
        # В случае двух победителей с одинаковым количеством голосов, выбираем с меньшим количеством букв в имени
        winner, votes_count = min(sorted_votes, key=lambda x: len(x[0]))

    return winner, votes_count
# Эта функция определяет победителя и количество голосов. Она сначала сортирует словарь голосов в порядке убывания
# количества голосов и, если есть два победителя с одинаковым количеством голосов,
# выбирает того, у кого меньше букв в имени.

# Шаг №4. - Главная функция main
def main():
    candidates = get_candidates()
    votes = {}

    while True:
        votes = vote(candidates, votes)
        another_vote = input("Желаете проголосовать еще? (да/нет) ").lower()
        if another_vote != 'да':
            break

    winner, votes_count = determine_winner(votes)
    print(f"Победитель выборов: {winner} с количеством голосов: {votes_count}")
# Эта функция является основной. Она инициализирует список кандидатов и словарь голосов, затем в цикле предлагает
# пользователям голосовать и обновляет результаты голосования.
# По завершении цикла определяется победитель и выводится результат.

# Шаг №5. - Запуск программы
if __name__ == "__main__":
    main()
# Этот блок кода проверяет, запущен ли файл напрямую, и если да, вызывает функцию main().
# Это обеспечивает запуск программы при выполнении скрипта.

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Вариант №2. ↓ - Чуть-чуть попытался доработать и добавил "Блеска"

from collections import Counter
class Election:
    def __init__(self, candidates):
        self.candidates = candidates
        self.votes = Counter()
    def vote(self, voter):
        print("Кандидаты в выборах:", ", ".join(self.candidates))
        choice = input(f"{voter}, на кого вы отдаете голос? ")
        while choice not in self.candidates:
            print("Некорректный выбор. Попробуйте еще раз.")
            choice = input(f"{voter}, на кого вы отдаете голос? ")
        self.votes[choice] += 1
        print(f"{voter}, ваш голос за {choice} учтен.")
    def determine_winner(self):
        sorted_votes = sorted(self.votes.items(), key=lambda x: (-x[1], len(x[0])))
        if len(sorted_votes) == 1 or sorted_votes[0][1] > sorted_votes[1][1]:
            winner, votes_count = sorted_votes[0]
        else:
            # В случае двух победителей с одинаковым количеством голосов, выбираем с меньшим количеством букв в имени
            winner, votes_count = min(sorted_votes, key=lambda x: len(x[0]))
        return winner, votes_count
    def run_election(self):
        print("********** Игра в выборы **********")
        voters = ["Иван", "Мария", "Александр", "Елена", "Петр", "София"]
        for voter in voters:
            self.vote(voter)
        winner, votes_count = self.determine_winner()
        print(f"Победитель выборов: {winner} с количеством голосов: {votes_count}")
if __name__ == "__main__":
    candidates_list = ["Шаунин", "Новичихина", "Калиев", "Цой", "Шудабаев", "Кадырова", "Исабекова",
                       "Сариев", "Изденов", "Ким", "Смагулова", "Әбілхайыр", "Зуев", "Сериккалиев",
                       "Годун", "Камбарбаев", "Токаев", "Путин", "Лукашенко", "Трамп"]
    election = Election(candidates_list)
    election.run_election()

# Шаг №1. - Класс Election и его конструктор
from collections import Counter
class Election:
    def __init__(self, candidates):
        self.candidates = candidates
        self.votes = Counter()
# В этом шаге создается класс Election, который будет представлять выборы. В конструкторе устанавливаются
# начальные данные: список кандидатов и счетчик голосов, предоставляемый модулем Counter из стандартной библиотеки.

# Шаг №2. - Метод vote
    def vote(self, voter):
        print("Кандидаты в выборах:", ", ".join(self.candidates))
        choice = input(f"{voter}, на кого вы отдаете голос? ")

        while choice not in self.candidates:
            print("Некорректный выбор. Попробуйте еще раз.")
            choice = input(f"{voter}, на кого вы отдаете голос? ")

        self.votes[choice] += 1
        print(f"{voter}, ваш голос за {choice} учтен.")
# Этот метод позволяет избирателю отдать свой голос за одного из кандидатов. Он запрашивает выбор избирателя,
# проверяет корректность выбора и обновляет счетчик голосов.

# Шаг №3. - Метод determine_winner
    def determine_winner(self):
        sorted_votes = sorted(self.votes.items(), key=lambda x: (-x[1], len(x[0])))

        if len(sorted_votes) == 1 or sorted_votes[0][1] > sorted_votes[1][1]:
            winner, votes_count = sorted_votes[0]
        else:
            # В случае двух победителей с одинаковым количеством голосов, выбираем с меньшим количеством букв в имени
            winner, votes_count = min(sorted_votes, key=lambda x: len(x[0]))

        return winner, votes_count
# Этот метод определяет победителя и количество голосов. Сначала он сортирует словарь голосов в порядке убывания
# количества голосов. Если есть два победителя с одинаковым количеством голосов, выбирается тот,
# у кого меньше букв в имени.

# Шаг №4. - Метод run_election
    def run_election(self):
        print("********** Игра в выборы **********")
        voters = ["Иван", "Мария", "Александр", "Елена", "Петр", "София"]
        for voter in voters:
            self.vote(voter)
        winner, votes_count = self.determine_winner()
        print(f"Победитель выборов: {winner} с количеством голосов: {votes_count}")
# Этот метод запускает процесс выборов. Он создает список избирателей и позволяет каждому из них проголосовать.
# После голосования определяется победитель и выводится результат.

# Шаг №5. - Создание экземпляра класса и вызов метода
if __name__ == "__main__":
    candidates_list = ["Шаунин", "Новичихина", "Калиев", "Цой", "Шудабаев", "Кадырова", "Исабекова",
                        "Сариев", "Изденов", "Ким", "Смагулова", "Әбілхайыр", "Зуев", "Сериккалиев",
                        "Годун", "Камбарбаев", "Токаев", "Путин", "Лукашенко", "Трамп"]

    election = Election(candidates_list)
    election.run_election()
# В этом блоке кода создается экземпляр класса Election с передачей ему списка кандидатов.
# Затем вызывается метод run_election, который запускает все выборы.






