# Classes like other programming languages are great way to encapsulate
# functionality that can be kept together and can be used in different projects.

# class declaration: class classname():
class math():
	# self is like this it refers to the instance of itself

	# *args is an array
	def add(self,*args):
		result = 0;
		for num in args:
			result = result + num
		return result

def main():
	c = math()
	# When calling method self doesn't to be passed :)
	print(c.add(2))
	print(c.add(3,21,0))
	print(c.add(100,-100))	

if __name__ == "__main__":
	main()
	