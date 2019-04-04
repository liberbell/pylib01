import secrets
import string

def genarateTempPass(numChars=8):
    potentialChars = string.ascii_letters + string.digits + "+=?/!@#%"
    result = ''.join(secrets.choice(potentialChars) for i in range(numChars))
    return result

def generateBetterPass(numChars=8):
    potentialChars = string.ascii_letters + string.digits + "+=?/!@#%"
    while True:
        result = ''.join(secrets.choice(potentialChars) for i in range(numChars))

        if (any(c.isupper() for c in result) and any(c.isdigit) for c in result):
            break

    return result

resultURL = "http://my.example.com?reset="
resultURL += secrets.token_urlsafe(15)
print(resultURL)

# print(genarateTempPass(10))
# print(generateBetterPass(10))
