# LESSON_13_06-07-08.12.2023__MY_PW_№12.py
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''''   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓
Дата: 06-07-08 ДЕКАБРЯ 2023
'''''
'''
Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
Дисциплина: Основы программирования на Python
'''
'''
Урок №13 от 06.12.2023
Практическая работа №12: Работа с файлами и каталогами
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполните следующие задания:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Задание №1

Дан текстовый файл. Необходимо создать новый файл, в который требуется переписать из исходного файла все слова,
состоящие не менее чем из семи букв.
Задание №2

Дан текстовый файл. Необходимо переписать его строки в другой файл. Порядок строк во втором файле должен совпадать
с порядком строк в заданном файле.
Задание №3

Дан текстовый файл. Необходимо переписать его строки в другой файл. Порядок строк во втором файле должен быть обратным
по отношению к порядку строк в заданном файле.
Задание №4

Дан текстовый файл. Добавить в него строку из двенадцати звездочек (************), поместив ее после последней
из строк, в которых нет запятой. Если таких строк нет, то новая строка должна быть добавлена после всех строк
имеющегося файла. Результат записать в другой файл.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''

'''
''' ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓

'''
''' ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓
Решение:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Задание №1. ↓ 
'''
# Открываем исходный файл для чтения
with open('E:\PyCharm - IT-Step\CHERNOWICK_+_WORK_IN_CLASS_ROOM\LESSON 12_06.12.2023\PW_HW_12.txt', 'r', encoding='utf-8') as input_file:
    # Читаем содержимое файла
    content = input_file.read()

    # Разбиваем текст на слова
    words = content.split()

    # Отфильтровываем слова, состоящие не менее чем из семи букв
    filtered_words = [word for word in words if len(word) >= 7]

# Открываем новый файл для записи
with open('новый_файл.txt', 'w', encoding='utf-8') as output_file:
    # Записываем отфильтрованные слова в новый файл
    output_file.write(' '.join(filtered_words))
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1. ↓ - Открытие исходного файла для чтения:
'''
with open('E:\PyCharm - IT-Step\CHERNOWICK_+_WORK_IN_CLASS_ROOM\LESSON 12_06.12.2023\PW_HW_12.txt', 'r', encoding='utf-8') as input_file:
'''
Здесь используется конструкция with open(...) as ..., что гарантирует правильное закрытие файла после выполнения 
блока кода внутри. 'E:\PyCharm - IT-Step\CHERNOWICK_+_WORK_IN_CLASS_ROOM\LESSON 12_06.12.2023\PW_HW_12.txt' - это путь 
к исходному файлу. 'r' указывает на режим открытия файла для чтения, а encoding='utf-8' указывает кодировку файла.
'''
'''
Шаг №2. ↓ - Чтение содержимого файла:
'''
content = input_file.read()
'''
Эта строка считывает все содержимое файла и сохраняет его в переменной content.
'''
'''
Шаг №3. ↓ - Разбиение текста на слова:
'''
words = content.split()
'''
Эта строка разбивает текст на слова. split() разбивает строку на подстроки, используя пробел в качестве разделителя,
и возвращает список этих подстрок, который затем сохраняется в переменной words.
'''
'''
Шаг №4. ↓ - Отфильтровывание слов длиной не менее семи букв:
'''
filtered_words = [word for word in words if len(word) >= 7]
'''
Эта строка использует генератор списка для создания нового списка filtered_words,
который содержит только те слова из words, которые имеют длину не менее семи символов.
'''
'''
Шаг №5. ↓ - Открытие нового файла для записи:
'''
with open('новый_файл.txt', 'w', encoding='utf-8') as output_file:
'''
Здесь открывается новый файл 'новый_файл.txt' для записи ('w' - режим записи).
'''
'''
Шаг №6. ↓ - Запись отфильтрованных слов в новый файл:
'''
output_file.write(' '.join(filtered_words))
'''
join() объединяет слова из списка filtered_words в строку, разделяя их пробелами, и записывает эту строку в новый файл.
'''
'''
Пример:
Предположим, исходный файл содержит текст: "Это пример текста для задачи."

После выполнения кода, в новом файле 'новый_файл.txt' будет записан текст: "пример текста задачи." 
(слова "Это" и "для", имеющие менее семи букв, исключены).
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Задание №2. ↓ 
'''
# Открываем исходный файл для чтения
with open('E:\PyCharm - IT-Step\CHERNOWICK_+_WORK_IN_CLASS_ROOM\LESSON 12_06.12.2023\PW_HW_12.txt', 'r') as input_file:
    # Создаем новый файл для записи
    with open('новый_файл_порядок.txt', 'w') as output_file:
        # Читаем и записываем строки второго файла
        for line in input_file:
            output_file.write(line)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1. ↓ - Открытие исходного файла для чтения:
'''
with open('E:\PyCharm - IT-Step\CHERNOWICK_+_WORK_IN_CLASS_ROOM\LESSON 12_06.12.2023\PW_HW_12.txt', 'r') as input_file:
'''
Эта строка открывает исходный файл для чтения. Как и в предыдущем примере, используется конструкция with open(...) 
as ... для гарантии правильного закрытия файла после выполнения блока кода внутри.
'''
'''
Шаг №2. ↓ - Создание нового файла для записи:
'''
with open('новый_файл_порядок.txt', 'w') as output_file:
'''
Здесь создается новый файл 'новый_файл_порядок.txt' для записи. Режим 'w' указывает на запись в файл.
Аналогично, использование with open(...) гарантирует правильное закрытие файла.
'''
'''
Шаг №3. ↓ - Чтение и запись строк:
'''
for line in input_file:
    output_file.write(line)
'''
Этот блок кода использует цикл for для итерации по строкам из исходного файла (input_file). 
Для каждой строки (line) из исходного файла, эта строка записывается в новый файл (output_file). 
Таким образом, весь контент исходного файла копируется в новый файл.
'''
'''
Пример:
Предположим, исходный файл (PW_HW_12.txt) содержит следующий текст:

Это пример
текста
для задачи.
'''

'''
После выполнения этого кода, в новом файле (новый_файл_порядок.txt) будет сохранен тот же текст:

Это пример
текста
для задачи.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Задание №3. ↓ 
'''
# Открываем исходный файл для чтения
with open('E:\PyCharm - IT-Step\CHERNOWICK_+_WORK_IN_CLASS_ROOM\LESSON 12_06.12.2023\PW_HW_12.txt', 'r') as input_file:
    # Создаем новый файл для записи
    with open('новый_файл_обратный_порядок.txt', 'w') as output_file:
        # Читаем и записываем строки второго файла в обратном порядке
        for line in reversed(list(input_file)):
                output_file.write(line)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1. ↓ - Открытие исходного файла для чтения:
'''
with open('E:\PyCharm - IT-Step\CHERNOWICK_+_WORK_IN_CLASS_ROOM\LESSON 12_06.12.2023\PW_HW_12.txt', 'r') as input_file:
'''
Как и в предыдущих примерах, эта строка открывает исходный файл для чтения. Путь к файлу 
указан в строке 'E:\PyCharm - IT-Step\CHERNOWICK_+_WORK_IN_CLASS_ROOM\LESSON 12_06.12.2023\PW_HW_12.txt'.
'''
'''
Шаг №2. ↓ - Создание нового файла для записи:
'''
with open('новый_файл_обратный_порядок.txt', 'w') as output_file:
'''
Эта строка создает новый файл 'новый_файл_обратный_порядок.txt' для записи в него данных.
Режим 'w' указывает на то, что файл будет открыт для записи.
'''
'''
Шаг №3. ↓ - Чтение и запись строк в обратном порядке:
'''
for line in reversed(list(input_file)):
    output_file.write(line)
'''
list(input_file): Эта строка создает список строк из содержимого исходного файла. 
Это необходимо, так как мы хотим прочитать файл в обратном порядке, а reversed работает 
с итерируемыми объектами, такими как список.

reversed(list(input_file)): Здесь мы используем reversed, чтобы перевернуть порядок строк в списке.

for line in reversed(list(input_file)): Этот цикл for итерируется по каждой строке в обратном порядке.

output_file.write(line): Каждая строка затем записывается в новый файл.
'''

'''
Пример:
Предположим, исходный файл (PW_HW_12.txt) содержит следующий текст:

Это пример
текста
для задачи.


После выполнения этого кода, в новом файле (новый_файл_обратный_порядок.txt) строки будут записаны в обратном порядке:

для задачи.
текста
Это пример

'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Задание №4. ↓ 
'''
# Открываем исходный файл для чтения
with open('E:\PyCharm - IT-Step\CHERNOWICK_+_WORK_IN_CLASS_ROOM\LESSON 12_06.12.2023\PW_HW_12.txt', 'r') as input_file:
    # Создаем новый файл для записи
    with open('новый_файл_со_звездочками.txt', 'w') as output_file:
        lines = input_file.readlines()
        # Находим последнюю строку без запятой
        last_line_index = -1
        for i, line in enumerate(lines):
            if ',' not in line:
                last_line_index = i
        # Вставляем строку с звездочками после найденной строки или в конец файла
        lines.insert(last_line_index + 1, '************\n')
        # Записываем результат в новый файл
        output_file.writelines(lines)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1. ↓ - Открытие исходного файла для чтения:
'''
with open('E:\PyCharm - IT-Step\CHERNOWICK_+_WORK_IN_CLASS_ROOM\LESSON 12_06.12.2023\PW_HW_12.txt', 'r') as input_file:
'''
Эта строка открывает исходный файл для чтения. Как и в предыдущих примерах, 
путь к файлу указан в строке 'E:\PyCharm - IT-Step\CHERNOWICK_+_WORK_IN_CLASS_ROOM\LESSON 12_06.12.2023\PW_HW_12.txt'.
'''
'''
Шаг №2. ↓ - Создание нового файла для записи:
'''
with open('новый_файл_со_звездочками.txt', 'w') as output_file:
'''
Эта строка создает новый файл 'новый_файл_со_звездочками.txt' для записи в него данных. 
Режим 'w' указывает на то, что файл будет открыт для записи.
'''
'''
Шаг №3. ↓ - Чтение строк и поиск последней строки без запятой:
'''
lines = input_file.readlines()
last_line_index = -1
for i, line in enumerate(lines):
    if ',' not in line:
        last_line_index = i
'''
lines = input_file.readlines(): Эта строка читает все строки из исходного файла и сохраняет их в список lines.

for i, line in enumerate(lines):: Этот цикл проходит по каждой строке в списке, и enumerate используется для получения
индекса (i) и самой строки (line).

if ',' not in line:: Условие проверяет, содержит ли строка запятую. Если нет, 
то индекс этой строки сохраняется в last_line_index.
'''
'''
Шаг №4. ↓ - Вставка строки с звездочками после найденной строки или в конец файла:
'''
lines.insert(last_line_index + 1, '************\n')
'''
Эта строка использует метод insert для вставки строки '************\n' после строки,
в которой не найдена запятая (last_line_index).
'''
'''
Шаг №5. ↓ - Запись результатов в новый файл:
'''
output_file.writelines(lines)
'''
Эта строка записывает все строки (включая новую строку с звездочками) обратно в новый файл.
'''
'''
Пример:
Предположим, исходный файл (PW_HW_12.txt) содержит следующий текст:

Это пример,
текста для задачи.

После выполнения этого кода, в новом файле (новый_файл_со_звездочками.txt) будет записан следующий текст:

Это пример,
************
текста для задачи.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''                                             ВСЕ ЗАДАНИЯ В ОДНОМ КОДЕ                                            '''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Задание №1
with open('исходный_файл.txt', 'r', encoding='utf-8') as input_file:
    content = input_file.read()
    words = content.split()
    filtered_words = [word for word in words if len(word) >= 7]
with open('новый_файл.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(' '.join(filtered_words))
# Задание №2
with open('исходный_файл.txt', 'r', encoding='utf-8') as input_file:
    with open('новый_файл_порядок.txt', 'w', encoding='utf-8') as output_file:
        for line in input_file:
            output_file.write(line)
# Задание №3
with open('исходный_файл.txt', 'r', encoding='utf-8') as input_file:
    with open('новый_файл_обратный_порядок.txt', 'w', encoding='utf-8') as output_file:
        for line in reversed(list(input_file)):
            output_file.write(line)
# Задание №4
with open('исходный_файл.txt', 'r', encoding='utf-8') as input_file:
    with open('новый_файл_со_звездочками.txt', 'w', encoding='utf-8') as output_file:
        lines = input_file.readlines()
        last_line_index = -1
        for i, line in enumerate(lines):
            if ',' not in line:
                last_line_index = i
        lines.insert(last_line_index + 1, '************\n')
        output_file.writelines(lines)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Работа с файлами и каталогами
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполните следующие задания:
'''
'''
Задание №1

В текущей папке лежат файлы с расширениями .mp3, .flac и .oga.
Создайте папки mp3, flac, oga и положите туда все файлы с соответствующими расширениями.
'''
'''
Задание №2

В текущей папке лежит две других папки: vasya и mila, причём в этих папках могут лежать файлы с одинаковыми именами,
например vasya/kursovaya.doc и mila/kursovaya.doc. Скопируйте все файлы из этих папок в текущую папку назвав их
следующим образом: vasya_kursovaya.doc, mila_test.pdf.
'''
'''
Задание №3

В текущей папке лежат файлы следующего вида: S01E01.mkv, S01E02.mkv, S02E01.mkv и т.п., 
то есть все файлы начинаются с S01 или S02. Создайте папки S01 и S02 и переложите туда соответствующие файлы.
'''
'''
Задание №4

В текущей папке лежат файлы вида 2019-03-08.jpg, 2019-04-01.jpg и т.п. 
Отсортируйте файлы по имени и переименуйте их в 1.jpg, 2.jpg, …, 10.jpg.
'''
'''
Задание №5

Дан текстовый файл. Необходимо создать новый файл и записать в него следующую статистику по исходному файлу:

Количество символов;
Количество строк;
Количество гласных букв;
Количество согласных букв;
Количество цифр;
'''

''' ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓
Решение:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Задание №1
'''

'''
Этот код представляет собой пример сценария на языке программирования
Python для организации файлов в папки по их расширениям.
'''
import os
import shutil

extensions = ['.mp3', '.flac', '.oga']

for ext in extensions:
    folder_name = ext[1:]  # Имя папки без точки
    os.makedirs(folder_name, exist_ok=True)

    for file in os.listdir():
        if file.endswith(ext):
            shutil.move(file, os.path.join(folder_name, file))
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №0. ↓ Импорт всего что нужно:
'''
import os
import shutil
'''
Шаг №1. ↓ Задание списка расширений:
'''
extensions = ['.mp3', '.flac', '.oga']
'''
В этой строке задаются расширения файлов, которые будут организованы в соответствующие папки.
'''
'''
Шаг №2. ↓ Цикл по расширениям:
'''
for ext in extensions:
'''
Этот цикл итерируется по списку расширений.
'''
'''
Шаг №3. ↓ Создание папки для каждого расширения:
'''
folder_name = ext[1:]  # Имя папки без точки
os.makedirs(folder_name, exist_ok=True)
'''
folder_name = ext[1:]: Создает имя папки, убирая точку из расширения. 
Например, для '.mp3' будет создана папка 'mp3'.
os.makedirs(folder_name, exist_ok=True): Создает папку с указанным именем. 
Флаг exist_ok=True позволяет избежать ошибки, если папка уже существует.
'''
'''
Шаг №4. ↓ Цикл по файлам в текущей директории:
'''
for file in os.listdir():
'''
Этот цикл итерируется по всем файлам в текущей рабочей директории.
'''
'''
Шаг №5. ↓ Условие выбора файлов с нужным расширением:
'''
if file.endswith(ext):
'''
Проверяет, заканчивается ли имя файла на текущее расширение.
'''
'''
Шаг №6. ↓ Перемещение файлов в соответствующую папку:
'''
shutil.move(file, os.path.join(folder_name, file))
'''
shutil.move(file, os.path.join(folder_name, file)): Перемещает файл в папку, созданную для соответствующего расширения.
os.path.join(folder_name, file) используется для создания полного пути к файлу внутри новой папки.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Задание №2
'''
import os
import shutil

folders = ['vasya', 'mila']

for folder in folders:
    for file in os.listdir(folder):
        new_name = f"{folder}_{file}"
        shutil.copy(os.path.join(folder, file), new_name)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1. ↓ Импорт библиотек:
'''
import os
import shutil
'''
Эти строки импортируют модули os (для работы с операционной системой) и shutil (для операций с файлами и папками).
'''
'''
Шаг №2. ↓ Задание списка папок:
'''
ffolders = ['vasya', 'mila']
'''
В этой строке задаются имена папок, из которых будут копироваться файлы.
'''
'''
Шаг №3. ↓ Цикл по папкам:
'''
for folder in folders:
'''
Этот цикл итерируется по каждой папке из списка.
'''
'''
Шаг №4. ↓ Цикл по файлам в каждой папке:
'''
for file in os.listdir(folder):
'''
Этот вложенный цикл итерируется по каждому файлу в текущей папке.
'''
'''
Шаг №5. ↓ Формирование нового имени файла:
'''
new_name = f"{folder}_{file}"
'''
f"{folder}_{file}": Используется для формирования нового имени файла путем добавления префикса folder_ к текущему
имени файла.
'''
'''
Шаг №6. ↓ Копирование файла с новым именем:
'''
shutil.copy(os.path.join(folder, file), new_name)
'''
os.path.join(folder, file): Объединяет имя папки и имя файла для получения полного пути к текущему файлу.
shutil.copy(...): Копирует файл из одного места в другое. В данном случае, он копируется из текущей папки (folder) с 
текущим именем файла (file) в текущую директорию с новым именем (new_name).
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Задание №3
'''
import os
import shutil

seasons = ['S01', 'S02']

for season in seasons:
    os.makedirs(season, exist_ok=True)

    for file in os.listdir():
        if file.startswith(season) and os.path.isfile(file):
            shutil.move(file, os.path.join(season, file))
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1. ↓ Импорт библиотек:
'''
import os
import shutil
'''
Эти строки импортируют модули os (для работы с операционной системой) и shutil (для операций с файлами и папками).
'''
'''
Шаг №2. ↓ Задание списка сезонов:
'''
seasons = ['S01', 'S02']
'''
Это список сезонов, для каждого из которых будет создаваться папка.
'''
'''
Шаг №3. ↓ Цикл по сезонам:
'''
for season in seasons:
'''
Этот цикл итерируется по каждому сезону из списка.
'''
'''
Шаг №4. ↓ Создание папки для каждого сезона:
'''
os.makedirs(season, exist_ok=True)
'''
os.makedirs(season, exist_ok=True): Эта строка создает папку с именем текущего сезона. 
Флаг exist_ok=True позволяет избежать ошибки, если папка уже существует.
'''
'''
Шаг №5. ↓ Цикл по файлам в текущей директории:
'''
for file in os.listdir():
'''
Этот вложенный цикл итерируется по каждому файлу в текущей директории.
'''
'''
Шаг №6. ↓ Условие выбора файлов, начинающихся с текущего сезона и проверка, что это файл:
'''
if file.startswith(season) and os.path.isfile(file):
'''
file.startswith(season): Проверяет, начинается ли имя файла с текущего сезона.
os.path.isfile(file): Проверяет, является ли объект файлом (а не папкой, например).
'''
'''
Шаг №7. ↓ Перемещение файла в соответствующую папку сезона:
'''
shutil.move(file, os.path.join(season, file))
'''
shutil.move(file, os.path.join(season, file)): Перемещает файл из текущей директории в папку,
созданную для текущего сезона. os.path.join(season, file) 
используется для создания полного пути к файлу внутри новой папки.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Задание №4
'''
import os

files = [f for f in os.listdir() if os.path.isfile(f) and f.lower().endswith('.jpg')]
files.sort()

for i, file in enumerate(files, start=1):
    new_name = f"{i}.jpg"
    os.rename(file, new_name)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1. ↓ Импорт библиотек:
'''
import os
'''
Эта строка импортирует модуль os для работы с операционной системой.
'''
'''
Шаг №2. ↓ Формирование списка файлов с расширением .jpg:
'''
files = [f for f in os.listdir() if os.path.isfile(f) and f.lower().endswith('.jpg')]
files.sort()
'''
os.listdir(): Возвращает список файлов и папок в текущей директории.
os.path.isfile(f): Проверяет, является ли объект с именем f файлом (а не папкой, например).
f.lower().endswith('.jpg'): Проверяет, заканчивается ли имя файла на '.jpg', регистронезависимо.
[f for f in os.listdir() if os.path.isfile(f) and f.lower().endswith('.jpg')]: Списковое включение, 
формирующее список файлов, которые являются изображениями в формате JPG.
'''
'''
Шаг №3. ↓ Сортировка списка файлов:
'''
files.sort()
'''
Сортирует список файлов в лексикографическом порядке.
'''
'''
Шаг №4. ↓ Пронумерованный цикл по файлам:
'''
for i, file in enumerate(files, start=1):
'''
enumerate(files, start=1): Пронумерованный цикл по файлам, начиная с 1. В каждой итерации i - номер, file - имя файла.
'''
'''
Шаг №5. ↓ Формирование нового имени файла:
'''
new_name = f"{i}.jpg"
'''
f"{i}.jpg": Формирует новое имя файла путем добавления номера к '.jpg'.
'''
'''
Шаг №6. ↓ Переименование файла:
'''
os.rename(file, new_name)
'''
os.rename(file, new_name): Переименовывает файл из текущей директории с именем file в новое имя new_name.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Задание №5
'''
import string

with open('ваш_текстовый_файл.txt', 'r', encoding='utf-8') as input_file:
    content = input_file.read()

# Статистика
characters_count = len(content)
lines_count = content.count('\n')
vowels_count = sum(1 for char in content if char.lower() in 'aeiouаеёиоуыэюя')
consonants_count = sum(1 for char in content if char.isalpha() and char.lower() not in 'aeiouаеёиоуыэюя')
digits_count = sum(1 for char in content if char.isdigit())

# Запись статистики в новый файл
with open('статистика.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(f"Количество символов: {characters_count}\n")
    output_file.write(f"Количество строк: {lines_count}\n")
    output_file.write(f"Количество гласных букв: {vowels_count}\n")
    output_file.write(f"Количество согласных букв: {consonants_count}\n")
    output_file.write(f"Количество цифр: {digits_count}\n")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №0. ↓ Импорт библиотек:
'''
import string
'''
Шаг №1. ↓ Открытие файла для чтения:
'''
with open('ваш_текстовый_файл.txt', 'r', encoding='utf-8') as input_file:
    content = input_file.read()
'''
open('ваш_текстовый_файл.txt', 'r', encoding='utf-8'): Открывает текстовый файл для чтения с указанной кодировкой.
with ... as ...:: Использует контекстный менеджер, который автоматически закрывает файл после выполнения блока кода
внутри with.
content = input_file.read(): Читает содержимое файла и сохраняет его в переменной content.
'''
'''
Шаг №2. ↓ Статистика:
'''
characters_count = len(content)
lines_count = content.count('\n')
vowels_count = sum(1 for char in content if char.lower() in 'aeiouаеёиоуыэюя')
consonants_count = sum(1 for char in content if char.isalpha() and char.lower() not in 'aeiouаеёиоуыэюя')
digits_count = sum(1 for char in content if char.isdigit())
'''
len(content): Определяет общее количество символов в тексте.
content.count('\n'): Считает количество строк в тексте, используя символ новой строки \n.
sum(1 for char in content if char.lower() in 'aeiouаеёиоуыэюя'): Считает количество гласных букв (регистронезависимо).
sum(1 for char in content if char.isalpha() and char.lower() not in 'aeiouаеёиоуыэюя'): Считает количество согласных
букв (регистронезависимо).
sum(1 for char in content if char.isdigit()): Считает количество цифр в тексте.
'''
'''
Шаг №3. ↓ Запись статистики в новый файл:
'''
with open('статистика.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(f"Количество символов: {characters_count}\n")
    output_file.write(f"Количество строк: {lines_count}\n")
    output_file.write(f"Количество гласных букв: {vowels_count}\n")
    output_file.write(f"Количество согласных букв: {consonants_count}\n")
    output_file.write(f"Количество цифр: {digits_count}\n")
'''
open('статистика.txt', 'w', encoding='utf-8'): Открывает новый текстовый файл для записи статистики.
with ... as ...:: Использует контекстный менеджер для автоматического закрытия файла.
output_file.write(...): Записывает результаты статистики в новый файл.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
                    '''ВСЕ ЗАДАНИЯ (из раздела: "Работа с файлами и каталогами" В ОДНОМ КОДЕ'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
import os
import shutil
import string

# Задание №1
extensions = ['.mp3', '.flac', '.oga']

for ext in extensions:
    folder_name = ext[1:]  # Имя папки без точки
    os.makedirs(folder_name, exist_ok=True)

    for file in os.listdir():
        if file.endswith(ext):
            shutil.move(file, os.path.join(folder_name, file))

# Задание №2
folders = ['vasya', 'mila']

for folder in folders:
    for file in os.listdir(folder):
        new_name = f"{folder}_{file}"
        shutil.copy(os.path.join(folder, file), new_name)

# Задание №3
seasons = ['S01', 'S02']

for season in seasons:
    os.makedirs(season, exist_ok=True)

    for file in os.listdir():
        if file.startswith(season) and os.path.isfile(file):
            shutil.move(file, os.path.join(season, file))

# Задание №4
files = [f for f in os.listdir() if os.path.isfile(f) and f.lower().endswith('.jpg')]
files.sort()

for i, file in enumerate(files, start=1):
    new_name = f"{i}.jpg"
    os.rename(file, new_name)

# Задание №5
with open('ваш_текстовый_файл.txt', 'r', encoding='utf-8') as input_file:
    content = input_file.read()

# Статистика
characters_count = len(content)
lines_count = content.count('\n')
vowels_count = sum(1 for char in content if char.lower() in 'aeiouаеёиоуыэюя')
consonants_count = sum(1 for char in content if char.isalpha() and char.lower() not in 'aeiouаеёиоуыэюя')
digits_count = sum(1 for char in content if char.isdigit())

# Запись статистики в новый файл
with open('статистика.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(f"Количество символов: {characters_count}\n")
    output_file.write(f"Количество строк: {lines_count}\n")
    output_file.write(f"Количество гласных букв: {vowels_count}\n")
    output_file.write(f"Количество согласных букв: {consonants_count}\n")
    output_file.write(f"Количество цифр: {digits_count}\n")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #                             # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
 'РАСПИСЫВАТЬ ДАННЫЙ КОД (думаю) НЕ НАДО - Т.К и так ВСЕ ПОНЯТНО (смотрите подробное по каждому из кода описание выше)'
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #                             # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
                                    'ВСЯ ПРАКТИЧЕСКАЯ РАБОТА В ОДНОМ КОДЕ'
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #

import os
import shutil
import string

# Задание №1
with open('исходный_файл.txt', 'r', encoding='utf-8') as input_file:
    content = input_file.read()
    words = content.split()
    filtered_words = [word for word in words if len(word) >= 7]

with open('новый_файл.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(' '.join(filtered_words))

# Задание №2
with open('исходный_файл.txt', 'r', encoding='utf-8') as input_file:
    with open('новый_файл_порядок.txt', 'w', encoding='utf-8') as output_file:
        for line in input_file:
            output_file.write(line)

# Задание №3
with open('исходный_файл.txt', 'r', encoding='utf-8') as input_file:
    with open('новый_файл_обратный_порядок.txt', 'w', encoding='utf-8') as output_file:
        for line in reversed(list(input_file)):
            output_file.write(line)

# Задание №4
with open('исходный_файл.txt', 'r', encoding='utf-8') as input_file:
    with open('новый_файл_со_звездочками.txt', 'w', encoding='utf-8') as output_file:
        lines = input_file.readlines()
        last_line_index = -1
        for i, line in enumerate(lines):
            if ',' not in line:
                last_line_index = i
        lines.insert(last_line_index + 1, '************\n')
        output_file.writelines(lines)

# Задание №1 (часть 2)
extensions = ['.mp3', '.flac', '.oga']

for ext in extensions:
    folder_name = ext[1:]  # Имя папки без точки
    os.makedirs(folder_name, exist_ok=True)

    for file in os.listdir():
        if file.endswith(ext):
            shutil.move(file, os.path.join(folder_name, file))

# Задание №2 (часть 2)
folders = ['vasya', 'mila']

for folder in folders:
    for file in os.listdir(folder):
        new_name = f"{folder}_{file}"
        shutil.copy(os.path.join(folder, file), new_name)

# Задание №3 (часть 2)
seasons = ['S01', 'S02']

for season in seasons:
    os.makedirs(season, exist_ok=True)

    for file in os.listdir():
        if file.startswith(season) and os.path.isfile(file):
            shutil.move(file, os.path.join(season, file))

# Задание №4 (часть 2)
files = [f for f in os.listdir() if os.path.isfile(f) and f.lower().endswith('.jpg')]
files.sort()

for i, file in enumerate(files, start=1):
    new_name = f"{i}.jpg"
    os.rename(file, new_name)

# Задание №5
with open('ваш_текстовый_файл.txt', 'r', encoding='utf-8') as input_file:
    content = input_file.read()

# Статистика
characters_count = len(content)
lines_count = content.count('\n')
vowels_count = sum(1 for char in content if char.lower() in 'aeiouаеёиоуыэюя')
consonants_count = sum(1 for char in content if char.isalpha() and char.lower() not in 'aeiouаеёиоуыэюя')
digits_count = sum(1 for char in content if char.isdigit())

# Запись статистики в новый файл
with open('статистика.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(f"Количество символов: {characters_count}\n")
    output_file.write(f"Количество строк: {lines_count}\n")
    output_file.write(f"Количество гласных букв: {vowels_count}\n")
    output_file.write(f"Количество согласных букв: {consonants_count}\n")
    output_file.write(f"Количество цифр: {digits_count}\n")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
