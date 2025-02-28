import re 
def somethins(words):
    pattern = r'ab{2,3}'
    match = re.match(pattern, words)
    if match : return True
    else : return False

test_strings = ['a', 'ab', 'abb', 'abbb', 'b', 'ba', 'aa', 'abc']
for s in test_strings:
    print(f"'{s}' : {somethins(s)} ")