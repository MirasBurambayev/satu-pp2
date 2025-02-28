import re 

def xz(words):
    pattern = r'\b[A-Z][a-z]*\b'
    return re.findall(pattern, words)

test = "This is a Test of Regular Expressions in Python."
print(xz(test))