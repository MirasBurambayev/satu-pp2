import os 

path = os.getcwd()

if os.path.exists(path):
    dire , file = os.path.split(path)
    print(dire)
    print(file)
else:
    print("Sorry man ,here nothing")