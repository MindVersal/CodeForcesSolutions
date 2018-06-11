"""
Program for solution problem 7A

"""


def parse_input():
    """
    Read 8 lines for problem
    :return:
    """
    temp_string = []
    for i in range(8):
        temp_string.append([x for x in input()])
    return temp_string


def transform_matrix(input_matrix):
    """
    Function for transform matrix from letters to digits
    W -> 1
    B -> 0
    :param input_matrix:
    :return output_matrix:
    """
    output_matrix = []
    for i in range(8):
        temp_row_matrix = []
        for j in range(8):
            if input_matrix[i][j] == 'W':
                temp_row_matrix.append(1)
            else:
                temp_row_matrix.append(0)
        output_matrix.append(temp_row_matrix)
    return output_matrix


def counting_lines(input_strigs):
    """
    Function counting cells for not art,
    and if all cells in row or col then this
    ros or col may art
    But if all cells in rows and cols will be art
    then may only 8 lines for art matrix.
    :param input_strigs:
    :return count_lines for art:
    """
    count_lines_for_art = 0
    # count digit 0 in rows
    for i in range(8):
        count_w_in_row = 0
        for j in range(8):
            count_w_in_row += input_strigs[i][j]
        if count_w_in_row == 0:
            count_lines_for_art += 1
    # count digit 0 in cols
    for j in range(8):
        count_w_in_col = 0
        for i in range(8):
            count_w_in_col += input_strigs[i][j]
        if count_w_in_col == 0:
            count_lines_for_art += 1
    if count_lines_for_art == 16:
        return 8
    else:
        return count_lines_for_art


if __name__ == '__main__':
    count_lines = counting_lines(transform_matrix(parse_input()))
    print(count_lines)
