import secrets
import string

def genarateTempPass(numChars=8):
    potentialChars = string.ascii_letters + string.digits + "+=?/!@#%"
    result = ''.join.choice(potentialChars) for i in range(numChars)
    return result

def generateBetterPass(numChars=8):
    pass

print(genarateTempPass(10))
