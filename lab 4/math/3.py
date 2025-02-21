import math

num_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))
area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))
print("The area of the polygon is:", area)
