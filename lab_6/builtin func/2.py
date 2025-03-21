a= str(input("give text:"))
a= list(a)

b = sum(map(str.islower,a))
v = sum(map(str.isupper,a))
print(b)
print(v)

