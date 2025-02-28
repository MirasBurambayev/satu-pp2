import re


def lowandup(words):
    pattern = r'[a-z][A-Z]'
    match = re.match(pattern, words)
    if match : return True
    else : return False

test= ['aB', 'Ba', 'aBBBB', 'ba']
for a in test:
    print(f"'{a}': {lowandup(a)}")