import re 
def matchingsom(words):
    pattern = r"ab*"
    match = re.match(pattern , words)
    if match :
        return True
    else:
        return False

test_strings = ['a', 'ab', 'abb', 'abbb', 'b', 'ba']
for s in test_strings:
    print(f"'{s}': {matchingsom(s)}")