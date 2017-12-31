# Calculates number of days until april fool day
# April 1st is april fool day 
from datetime import date

def howmanydayuntilaf():
	# Today's date
	today = date.today()
	# April fools date
	afdate = date(day = 1, month = 4, year = today.year)

	# if april fool has already passed	
	if afdate < today:
		# Next april fool day
		afdate = afdate.replace(year = today.year + 1)

	result = (afdate - today).days
	
	return result

def main():
	print(howmanydayuntilaf())

if __name__ == "__main__":
	main()
	
	