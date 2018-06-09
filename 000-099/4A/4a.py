"""
Program for solution problem 4A.
"""


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    number_from_input = int(input())
    if 4 < number_from_input < 100 and is_even(number_from_input):
        print('YES')
    else:
        print('NO')
