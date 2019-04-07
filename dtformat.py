import datetime

now = datetime.datetime.now()
print(now.strftime("%a, %A, %w, %d"))
print(now.strftime("%b, %B, %m"))

output = now.strftime("")
