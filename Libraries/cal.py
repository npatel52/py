import calendar

# Text calendar
c = calendar.TextCalendar(calendar.MONDAY)
str = c.formatmonth(2018,1,0,0)
print(str)

# HTML based calendar 
# Also include class name attribute for CSS
hc = calendar.HTMLCalendar(calendar.MONDAY)
str = hc.formatmonth(2018,1)
print(str)

# iterate over months
# From sunday to end of the month 
# 0 means that day belong to other month
for day in c.itermonthdays(2018,8):
	print(day)

# Locale month name and days name
for month in calendar.month_name:
	print(month)

for day in calendar.day_name:
	print(day)




