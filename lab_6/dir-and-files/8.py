import os 
path = r"C:\vscode\labs\.vscode\.vscode\lab_6\dir-and-files\gg.txt"
a=(os.access(path, os.F_OK))
b=(os.access(path, os.R_OK))
c =(os.access(path, os.W_OK))
d = (os.access(path, os.X_OK))
if os.path.exists(path):
    if a and b and c and d:
        os.remove(path)

else :
    print("sorry bro , here nothing")

