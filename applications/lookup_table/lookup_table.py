import math
import random


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
	powers_table = {}
	for i in range(21):
		powers_table[i] = []
	for i in range(len(powers_table)):
		for j in range(1, 7):
			powers_table[i].append(i ** j)

	def get_factorial(n):
		if n == 1:
			return n
		else:
			return n * get_factorial(n - 1)

	print(f'x, y: {x} {y}')
	v = powers_table[x][y - 1]
	print(f'pow: {v}')
	v = get_factorial(v)
	print(f'math.fact: {v}')
	v //= (x + y)
	print(f'//x + y: {v}')
	v %= 982451653
	print(f'%: {v}')
	return v


# print(f'x, y: {x} {y}')
# v = math.pow(x, y)
# print(f'math.pow: {v}')
# v = math.factorial(v)
# print(f'math.fact: {v}')
# v //= (x + y)
# print(f'//x + y: {v}')
# v %= 982451653
# print(f'%: {v}')
# return v

# Do not modify below this line!

for i in range(1):
	x = random.randrange(2, 14)
	y = random.randrange(3, 6)
	print(f'{i}: {x},{y}: {slowfun(x, y)}')

# x = 6
# y = 3
# print(f'{x},{y}: {slowfun(x, y)}')

"""
x, y: 6 3
math.pow: 216.0
math.fact: 10020433703146107793945530580431357292843659510789309313207995121373860606589847385945865560132189286729581631646771816292076748699480508994205891351735346846175840399711009180476263461053865430706302603038547814701315906976472960428480208333486967446000761264392925098038248675260009865190052218097905890960111329206361438189114736515107632937864524405156085760000000000000000000000000000000000000000000000000000
//x + y: 1113381522571789754882836731159039699204851056754367701467555013485984511843316376216207284459132142969953514627419090699119638744386723221578432372415038538463982266634556575608473717894873936745144733670949757189035100775163662269831134259276329716222306807154769455337583186140001096132228024233100654551123481022929048687679415168345292548651613822795120640000000000000000000000000000000000000000000000000000
%: 959638969
6,3: 959638969
"""
