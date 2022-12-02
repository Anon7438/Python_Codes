import os

oldname="del.txt"
newname="Renamed_python_file.txt"
with open(oldname) as f:
    content=f.read()
    
with open(newname,'w') as f:
    f.write(content)
os.remove(oldname)
