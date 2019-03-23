sampleStr = "The quick brown fox jumps over the lazy dog"

print(sampleStr.startswith("The"))
print(sampleStr.startswith("the"))
print(sampleStr.endswith("dog"))

print(sampleStr.find("the"))
print(sampleStr.rfind("the"))
print("the" in sampleStr)

newStr = sampleStr.replace("lazy", "tired")
print(newStr)

print(sampleStr.count("over"))
