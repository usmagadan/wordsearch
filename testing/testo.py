from helpers import main_helper

main_helper.grid_letters = [['a', 'v', 'd'],
                            ['c', 'e', 'f'],
                            ['g', 'h', 'x'],
                            ['q', 'w', 'l']]

main_helper.grid_diagonals()
print(main_helper.diagonals_letters)

# diagonals_letters = []
#
# for i in range(-1, -(len(grid_letters) - 1), -1):
#     temp = []
#     for j in range(len(grid_letters)):
#         print(i, j)
#         if j == len(grid_letters) + i or j == len(grid_letters[0]): break
#         temp.append(grid_letters[j - i][-1 - j])
#     diagonals_letters.append(temp)
#
#
# print(diagonals_letters)

# diagonals_letters = []
# for i in range(0, len(grid_letters[0]) - 1):
# 	temp = []
# 	for j in range(len(grid_letters)):
# 		if i + j == len(grid_letters[0]): break
# 		temp.append(grid_letters[j][i + j])
# 	diagonals_letters.append(temp)
#
# for i in range(-1, -(len(grid_letters[0])), -1):
# 	temp = []
# 	for j in range(len(grid_letters)):
# 		if i - j < -len(grid_letters[0]): break
# 		temp.append(grid_letters[j][i - j])
# 	diagonals_letters.append(temp)
#
# for i in range(1, len(grid_letters) - 1):
# 	temp = []
# 	for j in range(len(grid_letters)):
# 		if j == len(grid_letters) - i: break
# 		temp.append(grid_letters[j+i][j])
# 	diagonals_letters.append(temp)
#
# for i in range(-1, -(len(grid_letters) - 1), -1):
# 	temp = []
# 	for j in range(len(grid_letters)):
# 		if j  == len(grid_letters) + i: break
# 		temp.append(grid_letters[j-i][-1-j])
# 	diagonals_letters.append(temp)
#
# print(diagonals_letters)

# grid_transpose = []
#
# for i in range(len(grid_letters)):
# 	for row in grid_letters:
# 		grid_transpose.append(row[i])
# print(grid_transpose)
#
# print([row[i] for i in range(len(grid_letters)) for row in grid_letters])
#
#
# grid_transpose = [grid_transpose[x:x+3] for x in range(0, len(grid_transpose), 3)]
# print(grid_transpose)

import random, string, itertools

# letters = string.ascii_lowercase
# # grid_letters = []
# grid_letters = [list(map(lambda let: random.choice(letters), range(15))) for _ in itertools.repeat(object, 15)]
