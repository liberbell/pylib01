import os
import secrets

result = os.urandom(8)
print([hex(b) for b in result])

moves = ["rock", "paper", "scissors"]
