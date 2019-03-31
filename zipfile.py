import zipfile

zfile = zipfile.zipfile("archive.zip","w")
zfile.write("file1.txt")
zfile.write("file2.txt")
zfile.write("file3.txt")

zfile.close()
