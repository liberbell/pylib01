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

with tempfile.TemporaryFile(mode="w+t") as tfp:
    tfp.write("This is some temp data")
    tfp.seek(0)
    print(tfp.read())
