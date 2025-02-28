import re

def uppandlow(words):
    pattern = r'[A-Z][a-z]{1,}'
    if re.match(pattern, words): return True
    else: return False

test= ['aB', 'Ba', 'aBBBB', 'ba', 'BbA', 'BBa', 'Baa']
for a in test:
    print(f"'{a}' : {uppandlow(a)}")
