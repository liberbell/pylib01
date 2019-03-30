import os
import tempfile

print("gettempdir: ", tempfile.gettempdir())
print("gettempprefix: ", tempfile.gettempprefix())

(tempfh, tempfp) = tempfile.mkstemp(".tmp","testtemp",None,True)
f = os.fdopen(tempfh,"w+t")
f.write("This is some temp data")
f.close()
