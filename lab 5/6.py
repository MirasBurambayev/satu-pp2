import re 
def xz(words):
    pattern = r'[ ,.]+'
    return re.sub(pattern, ':' , words)
test= [
    "Hello, world. This is a test.",
    "Python is great. Isn't it?",
    "No punctuation here",
    "   Multiple   spaces   ",
]
for a in test:
    print(f"'{a}' --> {xz(a)}")