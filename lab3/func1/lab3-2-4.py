def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(lambda x: is_prime(x), numbers))

numbers = list(map(int, input().split()))

prime_numbers = filter_prime(numbers)

print("Prime numbers:", prime_numbers)
