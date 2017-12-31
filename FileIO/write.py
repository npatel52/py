# File class is built-in python, import is not needed

import calendar

def main():
	# w+ for write and for file creation if it doesn't exist
	file = open("2018.txt","w+")
	
	# For writing calendar to file
	cal = calendar.TextCalendar(calendar.MONDAY)

	for month in range(1,13):
		monthstr = cal.formatmonth(2018, month, 0, 0)
		file.write(monthstr)
		
if __name__ == "__main__":
	main()