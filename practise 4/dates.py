#1
from datetime import date, timedelta

current_date = date.today()
new_date = current_date - timedelta(days=5)

print("Current date:", current_date)
print("Date 5 days ago:", new_date)

#2
from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#3
from datetime import datetime

now = datetime.now().replace(microsecond=0)

print(now)

from datetime import datetime

date1 = datetime(2026, 9, 27, 20, 0, 0)
date2 = datetime(2026, 9, 27, 21, 30, 0)

difference = date2 - date1

print(difference.total_seconds())