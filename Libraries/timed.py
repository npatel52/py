from datetime import timedelta
from datetime import datetime
from datetime import date
from datetime import time

# timedelta for span of time
# for eg to calculate expiration date and time
print(timedelta(days = 365, hours = 5, minutes = 1))

# Time arithmetic

# 1 year from now
print("One year from now, it will be: ", datetime.now() + timedelta(days=365))

# 2 weeks and 3 days from now
print("Two weeks and 3 days from now, it will be: ", datetime.now() + timedelta(weeks = 2, days = 3))

# 1 week ago 
d = datetime.now() - timedelta(weeks = 1)
sf = d.strftime("%A,%d %B,%Y")
print("One week ago, it was ", sf)




