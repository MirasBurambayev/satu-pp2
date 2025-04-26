import os 

path = r"C:\vscode\labs\.vscode\.vscode\lab_6\dir-and-files\test.txt"
name = "test.txt"

with open(path, "r") as file:
    lines = file.readlines()
    print(lines)    