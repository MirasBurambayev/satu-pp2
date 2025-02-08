from itertools import permutations

def print_permutations(s):
    perms = permutations(s)
    for p in perms:
        print("".join(p))

s = input()
print_permutations(s)
