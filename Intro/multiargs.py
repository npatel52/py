# Function can take multiple arguments by declaring * before argument name
def multi_add(*args):
	result = 0;
	for i in args:
		result = result + i
	return result

# adding 1 through 10
print(multi_add(1,2,3,4,5,6,7,8,9,10))

	

