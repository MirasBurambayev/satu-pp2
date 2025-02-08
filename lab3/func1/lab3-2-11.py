def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

s = input()
print(is_palindrome(s))
