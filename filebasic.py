

fp = open("testfile.txt", "w")
fp.write("This is some text\n")
fp.close()

with open("testfile.txt", "r") as fp:
    data = fp.read()
    print(data)

with open("testfile.txt", "a") as fp:
    fp.write("This is data added onto the file\n")

with open("testfile.txt", "r") as fp:
    data = fp.read()
    print(data)
