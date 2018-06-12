"""
Program for solution problem 9A

"""


def calculate_probability():
    input_numbers = [x for x in input()]
    big_number = input_numbers[0] if input_numbers[0] >= input_numbers[2] else input_numbers[2]
    probability = {
        '1': '1/1',
        '2': '5/6',
        '3': '2/3',
        '4': '1/2',
        '5': '1/3',
        '6': '1/6'
    }
    return probability[big_number]


if __name__ == '__main__':
    print(calculate_probability())
