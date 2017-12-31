# Example illustrating inheritance and method overriding

# parent class
class parent():
	def foo(self):
		print("Parent: foo()")
	def foobar(self):
		print("Parent: foobar()")

# Child inherit from Parent class
class child(parent):
	# This method is overrided
	def foo(self):
		print("Child: foo()")

def main():
	c = child()
	# Calls child method
	c.foo()
	# Child doesn't have this method but it inherits it from parent
	# Parent method foobar() is called
	c.foobar()
	
if __name__ == "__main__":
	main()