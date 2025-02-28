import re
def xz(words):
    pattern = r'a.b$'
    if re.match(pattern , words): return True
    else : return False

test = ["aggb", 'agb', 'Agb',  'baa' , 'aab']
for a in test:
    print(f"'{a}' : {xz(a)}")