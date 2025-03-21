import os 
path =  r"C:\vscode\labs\.vscode\.vscode\lab_6\dir-and-files\files6"
name = 'xz.txt'
alpha = [chr(i) for i in range(65, 91)]
for lettrs in alpha:
    hh = os.path.join(path, lettrs + ".txt")
    with open(hh, 'x') as gg:
        pass

    