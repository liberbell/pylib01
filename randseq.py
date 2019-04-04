import random
import string

moves = ["rock", "paper", "scissors"]
# print(random.choice(moves))

roulette_wheel = ["black", "red", "green"]
weight = [18,18,2]
# print(random.choices(roulette_wheel, weight, k=10))

chosen = random.sample(string.ascii_uppercase, 6)
print(chosen)

players = ["Bill", "Jane", "Joe", "Sally", "Mike", "Lynsay"]
