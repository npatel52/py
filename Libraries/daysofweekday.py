# Prints out a day of every month's first FRIDAY in 2018
import calendar 

# Loop for each month
for month in range(1,13):
	# First friday must be somwhere in first two weeks
	c = calendar.monthcalendar(2018, month)
	w1 = c[0]
	w2 = c[1]	

	# calendar month starts from sunday
	if w1[calendar.FRIDAY] != 0:
		day = w1[calendar.FRIDAY]
	else:
		day = w2[calendar.FRIDAY]

	print('{:>10} {:>4}'.format(calendar.month_name[month],day))

