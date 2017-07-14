"""

B. Электронные таблицы
ограничение по времени на тест
10 seconds
ограничение по памяти на тест
64 megabytes
ввод
стандартный ввод
вывод
стандартный вывод

В популярных системах электронных таблиц (например, в программе Excel)
используется следующая нумерация колонок.
Первая колонка имеет номер A, вторая B и т.д. до 26-ой, которая обозначается буквой Z.
Затем идут двухбуквенные обозначения: 27-ая обозначается как AA, 28-ая как AB, а 52-я обозначается парой AZ.
Аналогично, следом за ZZ следуют трехбуквенные обозначения и т.д.

Строки обычно обозначаются целыми числами от 1.
Номер ячейки получается конкатенацией обозначений для столбца и строки.
Например, BC23 это обозначение для ячейки в столбце 55, строке 23.

Иногда используется другая форма записи: RXCY,
где X и Y это целые числа, обозначающие номер строки и столбца, соответственно.
Например, R23C55 это ячейка из примера выше.

Ваша задача написать программу, которая считывает последовательность
обозначений ячеек и выводит каждое из обозначений в другой форме записи.
Входные данные

В первой строке записано целое число n (1 ≤ n ≤ 105), количество обозначений в тесте.
Далее идет n строк, каждая из которых содержит обозначение.
Известно, что все обозначения корректны, и не содержат ячейки с номерами строк или столбцов больших 106.
Выходные данные

Выведите n строк — каждая строка должна содержать обозначение ячейки в отличной форме записи.
Примеры
Входные данные

2
R23C55
BC23

Выходные данные

BC23
R23C55

"""
import re


ALPHABET_ARRAY = ['', 'A', 'B', 'C', 'D', 'E', 'F',
                  'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
ALPHABET_MAP = {'':   0, 'A':  1, 'B':  2, 'C':  3, 'D':  4, 'E':  5, 'F':  6,
                'G':  7, 'H':  8, 'I':  9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
                'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
                'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
ALPHABET_COUNT = 26


def convert_to_rc(raw_row):
    row_first = raw_row[1]
    row_second = 0
    row_temp = raw_row[0]
    for index in range(0, len(row_temp)):
        row_second += ALPHABET_MAP[row_temp[index]] * pow(ALPHABET_COUNT, (len(row_temp) - 1) - index)
    return 'R' + str(row_first) + 'C' + str(row_second)


def convert_from_rc(raw_row):
    row_second = raw_row[0]
    row_temp = int(raw_row[1])
    row_first = ''
    while row_temp != 0:
        row_first = ALPHABET_ARRAY[row_temp % ALPHABET_COUNT] + row_first
        row_temp //= ALPHABET_COUNT
    return row_first + row_second


input_array = []
count_rows = int(input())
for index_row in range(0, count_rows):
    input_array.append(input().upper())
pattern_rc = r'R(\d+)C(\d+)'
pattern_non_rc = r'(\D+)(\d+)'
for row in range(0, count_rows):
    founds_rc = re.findall(pattern_rc, input_array[row])
    founds_non_rc = re.findall(pattern_non_rc, input_array[row])
    if len(founds_rc) != 0:
        founds = list(founds_rc[0])
        print(convert_from_rc(founds))
    else:
        founds = list(founds_non_rc[0])
        print(convert_to_rc(founds))
