from datetime import date, time, datetime

d1 = date.today()
# print(d1)

t1 = time(12, 30, 00)
# print(t1)

dt1 = datetime.now()
# print(dt1)


# print("Day:", d1.day)
# print("Year: ", d1.year)

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# print("Hour: ", t1.hour)
# print("Month: ", dt1.month)
# print("Weekday Num: ", dt1.weekday())
# print("Weekday: ", days[dt1.weekday()])

d1 = d1.replace(year=2020, month=6, day=19)
t1 = t1.replace(hour=5)
dt1 = dt1.replace(year=1976, month=7)

print(d1)
print(t1)
print(dt1)
