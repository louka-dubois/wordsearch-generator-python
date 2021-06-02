# Created on iPad.
# Created by Louka D.

import random
import string

words_list = open('./words_list.txt')
words = [words_list.readline() for i in words_list]
words_list.close()

words = [random.choice(words).upper().strip() for x in range(20)]

grid_size = 30
grid = [['•' for a in range(grid_size)] for b in range(grid_size)]

def print_grid():
	for i in grid:
		print(' '.join(i))

def display_words_list():
	i = 0
	words.sort()
	for index, value in enumerate(words):
		if index == i:
			words.insert(index, '\n')
			i += 5
	print('\t' + ' • '.join(words) + ' • ')

orientations = ['left_right', 'up_down', 'up_diagonal', 'down_diagonal']

worked = False
while worked == False:
	try:
		for word in words:
			word_length = len(word)

			placed = False
			while not placed:
				chosen_orientation = random.choice(orientations)

				if chosen_orientation == 'left_right':
					step_x = 1
					step_y = 0
				if chosen_orientation == 'up_down':
					step_x = 0
					step_y = 1
				if chosen_orientation == 'up_diagonal':
					step_x = 1
					step_y = -1
				if chosen_orientation == 'down_diagonal':
					step_x = 1
					step_y = 1

				position_x = random.randint(0, grid_size)
				position_y = random.randint(0, grid_size)

				ending_x = position_x + word_length * step_x
				ending_y = position_y + word_length * step_y

				if ending_x < 0 or ending_x >= grid_size: continue
				if ending_y < 0 or ending_y >= grid_size: continue

				failed = False

				for i in range(word_length):
					letter = word[i]
					new_position_x = position_x + i * step_x
					new_position_y = position_y + i * step_y

					letter_at_new_position = grid[new_position_x][new_position_y]
					if letter_at_new_position != '•':
						if letter_at_new_position == letter:
							continue
						else:
							failed = True
							break

				if failed:
					continue
				else:
					for i in range(word_length):
						letter = '\33[31m'+word[i]+'\33[0m'
						new_position_x = position_x + i * step_x
						new_position_y = position_y + i * step_y
						grid[new_position_x][new_position_y] = letter
					placed = True

		for a in range(grid_size):
			for b in range(grid_size):
				if grid[a][b] == '•':
					grid[a][b] = random.choice(string.ascii_uppercase)
		worked = True
	except:
		pass

print_grid()
display_words_list()
