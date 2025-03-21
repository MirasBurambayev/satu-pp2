import os
path = os.getcwd()

name = "test.txt"
print(os.access(name, os.F_OK))
print(os.access(name, os.R_OK))
print(os.access(name, os.W_OK))
print(os.access(name, os.X_OK))