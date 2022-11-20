import os

oldname = ""
newname = "renamed_by_python.txt"

with open(oldname) as f:
    content = f.read()

with open(newname, 'w'):
    f.write(content)

os.remove(oldname)