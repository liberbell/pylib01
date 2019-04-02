import random

# print(random.random())
# print(random.random())
# print(random.random())

for i in range(10):
    if (random.random() <= 0.5):
        print(i)
        print("Heads")
    else:
        print(i)
        print("Tails")
