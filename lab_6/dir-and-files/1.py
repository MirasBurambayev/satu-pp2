import os
path = os.getcwd()
gg= os.listdir(path)
dirs=[]
files=[]
all=[]
for a in gg:
    if os.path.isdir(os.path.join(path, a)):
        dirs.append(a)

    if os.path.isfile(os.path.join(path, a)):
        files.append(a)
    
print(dirs)
print(files)
print(gg)

