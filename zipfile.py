import zipfile

zfile = zipfile.ZipFile("archive.zip","w")
zfile.write("file1.txt")
zfile.write("file2.txt")
zfile.write("file3.txt")
