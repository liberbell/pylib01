import zipfile

# zfile = zipfile.ZipFile("archive.zip","w")
# zfile.write("file1.txt")
# zfile.write("file2.txt")
# zfile.write("file3.txt")
#
# zfile.close()

print(zipfile.is_zipfile("archive.zip"))

zfile = zipfile.ZipFile("archive.zip")
# print(zfile.namelist())
# print(zfile.infolist())

zinfo = zfile.getinfo("file1.txt")
print(zinfo.file_size)
print(zfile.read())
