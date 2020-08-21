from datetime import date
from datetime import time

now=date.today()

print(now.isoformat())

print(now.isocalendar())

print(now.strftime('%Y-%m-%d'))

print(time.dst())