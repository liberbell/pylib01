import os
import secrets

result = os.urandom(8)
# print([hex(b) for b in result])

moves = ["rock", "paper", "scissors"]
print(secrets.choice(moves))

result = secrets.token_bytes(8)
print(result)