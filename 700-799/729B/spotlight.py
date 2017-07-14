import random
import time


def print_arrary(temp_array):
    for row in range(len(temp_array)):
        print(temp_array[row])


def count_best_positions():
    result = 0
    for i in range(count_rows):
        found = False
        start = -1
        end = -1
        result_hor = 0
        for j in range(count_cols):
            if input_array[i][j] == 1:
                if not found:
                    found = True
                    start = j
                else:
                    result_hor += 1
                end = j
        if found:
            result += count_cols - 1 - start + end - result_hor * 2
            # if start != end:
            #     # result += start + ((count_cols - 1) - end) + ((end - 1) - start - (result_hor - 1)) * 2
            #     result += count_cols - 1 - start + end - result_hor * 2
            # else:
            #     # result += start + ((count_cols - 1) - end)
            #     result += count_cols - 1 + start - end
    for j in range(count_cols):
        found = False
        start = -1
        end = -1
        result_vert = 0
        for i in range(count_rows):
            if input_array[i][j] == 1:
                if not found:
                    found = True
                    start = i
                else:
                    result_vert += 1
                end = i
        if found:
            result += count_rows - 1 - start + end - result_vert * 2
            # if start != end:
            #     # result += start + ((count_rows - 1) - end) + ((end - 1) - start - (result_vert - 1)) * 2
            #     result += count_rows - 1 - start + end - result_vert * 2
            # else:
            #     # result += start + ((count_rows - 1) - end)
            #     result += count_rows - 1 + start - end
    return result


# input_array = []
# # file = open('./input.txt')
# # temp_array_string = file.readline().split()
# temp_array_string = input().split()
# count_rows = int(temp_array_string[0])  # i == n
# count_cols = int(temp_array_string[1])  # j == m
# for row in range(count_rows):
#     # temp_array_string = [int(cell) for cell in file.readline().split()]
#     temp_array_string = [int(cell) for cell in input().split()]
#     temp_row = []
#     for col in range(count_cols):
#         temp_row.append(temp_array_string[col])
#     input_array.append(temp_row)
# file.close()
# print(count_best_positions())
input_array = []
count_rows = 4
count_cols = 4
for i in range(count_rows):
    input_array.append([])
    for j in range(count_cols):
        input_array[i].append(random.randint(0, 1))
input_array[2][2] = 1
print_arrary(input_array)
start_time = time.time()
print(count_best_positions())
end_time = time.time()
print('Time = %s ms' % ((end_time - start_time) * 1000))


print()
