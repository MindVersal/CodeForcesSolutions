"""
Program for solving problem 7C

"""
import math


def find_point_belongs_to_line(numbers):
    limit_number = 5 * 100
    answer = '-1'
    koef_a = int(numbers[0])
    koef_b = int(numbers[1])
    koef_c = int(numbers[2])
    d = abs(koef_c) / math.sqrt(math.pow(koef_a, 2) + math.pow(koef_b, 2))
    answer = str(d)
    return answer


if __name__ == '__main__':
    input_numbers = [x for x in input() if x != ' ']
    print(find_point_belongs_to_line(input_numbers))
