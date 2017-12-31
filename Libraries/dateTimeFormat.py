# Formatting date and time

from datetime import datetime

def main():
	# Current date and time
	now = datetime.now();
	
	# Format year 
	# %y for abbreviate year 
	# %Y for Full year
	print("Year: ",now.strftime("%Y"))
	
	# lower case letters for abbreviation
	# uppercase for full
	# %A full weekday name
	# %d day in month 
	# %B full month name
	print(now.strftime("%A,%d %B,%Y"))

	# locale's date and time format
	
	# %c for locale date and time
	print(now.strftime("%c"))
	
	# %x for locale's date
	print(now.strftime("%x"))
	
	# %X for locale's time
	print(now.strftime("%X"))

	# Format time
	# %I/%H : 12/24 hour
	# %M: minute
	# %S: second
	#p: locale AM/PM
	print(now.strftime("%I:%M:%S %p"))
	print(now.strftime("%H:%M:%S %p"))	

if __name__ == "__main__":
	main()