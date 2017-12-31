# Reading files
def main():
	# r for read mode. open file
	file = open("2018.txt","r")
	
	
	# Check to see if the file was opened
	if file.mode == 'r':
		# Reading entire content
		content = file.read()
		print (content)
	
	#if file.mode == 'r':
		# Reading content line by line
	#	filelines = file.readlines()
	#	for line in filelines:
	#		print(filelines)

	# Close file
	file.close()
	
if __name__ == "__main__":
	main()