import zipfile

zfile = zipfile.ZipFile("archive.zip","w")
zfile.write("file1.txt")
