from datetime import datetime

time = "Jan 15, 2023 - 12:05:33"

date = datetime.strptime(time, "%b %d, %Y - %H:%M:%S")
month = date.strftime("%B")
Full_date = date.strftime("%d.%m.%Y, %H:%M")

print(date)
print(month)
print(Full_date)
