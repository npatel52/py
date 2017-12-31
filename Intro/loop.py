# loops
# Two ways while or for


def main():
	x= 0

	# 1 WHILE LOOP
	# indentation and : required 
	while(x < 5):
		print(x)
		x = x + 1


	# 2 FOR LOOP
	# iterators instead of counters in other languages
	# range(5,10) = [5,10) 10 is excluded
	for x in range(5,10):
		print(x)

	# Iterating over collections
	days = ["M","T","W","R","F","S","SUNDAY"]

	for d in days:
		print(d)

	# break and continue are same as other language

	# To get index of collection use enumerate
	for i,d in enumerate(days):
		print(i," ", d)


if __name__ == "__main__":
	main()