import os 

path1 = r"C:\vscode\labs\.vscode\.vscode\lab_6\dir-and-files\tst.txt"
path2 = r"C:\vscode\labs\.vscode\.vscode\lab_6\dir-and-files\test.txt"


with open(path2, 'r' , encoding='utf-8') as file:
    content = file.read()

with open(path1, 'w', encoding='utf-8') as gg:
    gg.write(content)