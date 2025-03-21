a= str(input("give text:"))

print(all(map(str.__eq__ ,a,reversed(a))))
