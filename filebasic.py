

# fp = open("testfile.txt", "w")
# fp.write("This is some text\n")
# fp.close()

with open("testfile.txt", "r"):
    data = fp.read()
    print(data)
