# more on functions and argument order
# Python code is executed line by line!

# default value of exponent is set to 1.
def power (num, exp = 1):
	result = 1;
	for i in range(exp):
		result = result * num;

	return result

# Another function
def pow(num, power):
	result = 1
	neg = False

	if power < 0: 
		neg = True
		power = power * -1
	
	for i in range(power):
		result = num * result

	if neg == True:
		return 1/result
	else:
		return result

print(pow(2,-2))
print(pow(3,0))
print(pow(3,2))



# second argument is empty so, exp is 1
print (power(2))

print (power(2,3))

# order of argument doesn't matter if var name are specified in function call
print (power(exp = 10, num = 2))




