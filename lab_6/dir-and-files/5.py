import os 

path = r"C:\vscode\labs\.vscode\.vscode\lab_6\dir-and-files\test.txt"


hh= [1 , 2 , 'нет не 3']
with open(path, 'w' , encoding='utf-8') as gg:
    for a in hh:
        gg.write(f'{str(a)}'"\n")


