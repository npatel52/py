# importing specific class from module datetime

from datetime import date
from datetime import time
from datetime import datetime

def main():
	# Date Object
	# Get today's date from today() method of class date
	today = date.today()
	print(today)

	# Date components 
	print("Day: ", today.day, " Month: ", today.month, " Year: ", today.year)

	# Weekday [0 = monday,6 = sunday] 
	print("Week Day: ", today.weekday())

	# Date time object
	today = datetime.now()
	print(today)

	# To just get time
	time = datetime.time(datetime.now())
	print(time)

	# Getting week day name 
	days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday","Sunday"]
	print("Today is ", days[date.today().weekday()])


if __name__ == "__main__":
	main()