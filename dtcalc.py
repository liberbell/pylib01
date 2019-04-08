import datetime

dt1 = datetime.datetime(2019, 4, 7, 10)
dt2 = datetime.datetime(2019, 6, 19, 12)

print(dt1 < dt2)
print(dt1 > dt2)

delta = dt2 - dt1
print(delta)
print(delta.days)
print(delta.seconds)

now = datetime.datetime.now()
oneyear = datetime.timedelta(days=365)
oneweek = datetime.timedelta(weeks=1)

print("One year from now will be: ", now + oneyear)
print("One week from now will be: ", now + oneweek)
print("One week ago was: ", now - oneweek)
