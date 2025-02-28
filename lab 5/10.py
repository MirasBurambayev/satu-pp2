import re

def xz(words):
    pattern = '([a-z])([A-Z])'
    return re.sub(pattern , r'\1_\2' , words)


test = [
    "HelloWorld",
    "CamelCaseString",
    "InsertSpacesBetweenWords",
    "JustOneWord",
    "ThisIsATest"
]

for s in test:
    print(f"'{s}' -> '{xz(s).lower()}'")