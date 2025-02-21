def squares_up_to_n(n):
    for i in range(n + 1):
        yield i * i

for square in squares_up_to_n(10):
    print(square)
