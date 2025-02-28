import re 
def xz(words):
    a = words.split('_')
    camel = a[0]
    for c in a[1:]:
        camel += c.capitalize()
    return camel 

test = [
    "hello_world",
    "convert_snake_case_to_camel_case",
    "python_is_awesome",
    "snake",
    "alreadyCamelCase"
]

for s in test:
    print(f"'{s}' --> '{xz(s)}'")