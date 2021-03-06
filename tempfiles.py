import os
import tempfile

print("gettempdir: ", tempfile.gettempdir())
print("gettempprefix: ", tempfile.gettempprefix())

# (tempfh, tempfp) = tempfile.mkstemp(".tmp","testtemp",None,True)
# f = os.fdopen(tempfh,"w+t")
# f.write("This is some temp data")
# f.seek(0)
# print(f.read())
# f.close()
# os.remove(tempfp)

# with tempfile.TemporaryFile(mode="w+t") as tfp:
#     tfp.write("This is some temp data")
#     tfp.seek(0)
#     print(tfp.read())

with tempfile.TemporaryDirectory() as tdp:
    path = os.path.join(tdp,"tempfile.txt")
    tfp = open(path,"w+t")
    tfp.write("This is a temp file in a dir")
    tfp.seek(0)
    print(tfp.read())
