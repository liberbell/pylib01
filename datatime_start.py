from datetime import date, time, datetime

d1 = date.today()
# print(d1)

t1 = time(12, 30, 00)
# print(t1)

dt1 = datetime.now()
# print(dt1)


print("Day:", d1.day)
print("Year: ", d1.year)

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print("Hour: ", t1.hour)
print("Month: ", dt1.month)
print("Weekday: ", dt1.weekday)
