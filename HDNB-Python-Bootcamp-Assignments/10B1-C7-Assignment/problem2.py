# Problem 2: Calculate Future Date

import datetime

# Current date and time
now : datetime = datetime.datetime.now()
print(f"Current date and time: {now}")

# Future date and time (30 days from now)
future : datetime = now + datetime.timedelta(days=30)
print(f"Date and time 30 days from now: {future}")

