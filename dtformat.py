import datetime

now = datetime.datetime.now()
print(now.strftime("%a, %A, %w, %d"))
print(now.strftime("%b, %B, %m"))

print(now.strftime("%H, %I, %M, %S, %p"))

print(now.strftime("%c"))
print(now.strftime("%X"))

output = now.strftime("")
