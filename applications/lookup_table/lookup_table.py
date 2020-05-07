import math
import random

cache = {}      # Establish cache outside of function to hold lookup list

# 	TODO: Modify to produce the same results, but much faster
def slowfun(x, y):

	if (x, y) not in cache:         # if (x, y) is not cached, do this. If is, go to line 19
		# print(f'x, y: {x} {y}')
		v = math.pow(x, y)
		# print(f'math.pow: {v}')
		v = math.factorial(v)
		# print(f'math.fact: {v}')
		v //= (x + y)
		# print(f'//x + y: {v}')
		cache[(x, y)] = v % 982451653               # This will perform the mod op on the value of x, y from the cache
		print(f'cache[(x, y)]: {cache[(x, y)]}')    # This prints the value of the lookup in the cache
	return cache[(x, y)]                            # Returns value of x,y from within the cache

	# The cache allows you to store the values returned from the function call
	# If the same x, y is passed in, instead of the function needing to run a second time
	# The data can be pulled directly from

# Do not modify below this line!

for i in range(100):
	x = random.randrange(2, 14)
	y = random.randrange(3, 6)
	print(f'{i}: {x},{y}: {slowfun(x, y)}')
print(x, y)

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
