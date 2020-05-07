import math
import random



# look_up_table = {}
# for i in range(21):
# 	look_up_table[i] = []
# for i in range(len(look_up_table)):
# 	for j in range(1, 6):
# 		look_up_table[i].append(i ** j)
# 	print(f'Look up table {i}: {look_up_table[i]}')
#
# print(look_up_table[3][2])

def slowfun(x, y):
	"""
	Look up table for math.pow()
	Each item[i] should be x
	Each list element should be y
	{1: [1, 1, 1, 1, 1],
	2: [2, 4, 8, 16, 32],
	3: [3, 9, 27, 81, 243]}
	(3, 5) should 243
	"""

	# TODO: Modify to produce the same results, but much faster
	# v = math.pow(x, y)
	# v = math.factorial(v)
	# v //= (x + y)
	# v %= 982451653
	# return v

	powers_table = {}
	for i in range(21):
		powers_table[i] = []
	for i in range(len(powers_table)):
		for j in range(1, 7):
			powers_table[i].append(i ** j)
		# print(f'Look up table {i}: {look_up_table[i]}')

	# factorial_table = {}
	# for i in range(248832):
	# 	print(i)
	# 	factorial_table[i] = i ** i
		# print((factorial_table[i] // (x + y)) % 982451653)
	# print(look_up_table[x][y])
	v = powers_table[x][y-1]
	print(v)
	v = v ** v
	print(v)
	return v


# Do not modify below this line!
#
for i in range(50000):
	x = random.randrange(2, 14)
	y = random.randrange(3, 6)
	print(f'{i}: {x},{y}: {slowfun(x, y)}')
