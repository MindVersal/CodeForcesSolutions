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
POW_26_0 = 1
POW_26_1 = 26
POW_26_2 = 676
POW_26_3 = 17576
POW_26_4 = 456976


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
    if POW_26_0 <= row_temp <= POW_26_1:
        row_first = ALPHABET_ARRAY[row_temp]
    elif POW_26_1 < row_temp <= POW_26_2:
        row_first = ALPHABET_ARRAY[row_temp // ALPHABET_COUNT] + ALPHABET_ARRAY[row_temp % ALPHABET_COUNT]

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
