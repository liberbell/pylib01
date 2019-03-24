

test_string1 = "The quick brown fox jumps over the lazy dog on the 1st of December"

print(test_string1.upper())
print(test_string1.lower())

result = test_string1.split(" ")
print(result)

letters = ["a", "b", "c", "d", "e"]
print(", ".join(letters))

names = ["Amy", "John", "George", "Michels", "Penelope"]
biggest = max(len(name) for name in names)

for name in names:
    print(name.ljust(biggest+2,"-") + ":")

# print(biggest)

sampleStr = "The quick brown fox jumps over the lazy dog"
