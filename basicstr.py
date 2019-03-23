import string

# print(string.ascii_letters)
# print(string.digits)
# print(string.hexdigits)
# print(string.punctuation)

test_string1 = "The quick brown fox jumps over the lazy dog on the 1st of December"
test_string2 = "Supercalifraglistic"
test_string3 = "90210"

result = ".join([c for c in test_string1 if c in string.ascii_letters])
