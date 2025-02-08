def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

lst = list(map(int, input().split()))
print(unique_elements(lst))
