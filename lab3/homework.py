def sublist(lst1, lst2):
    lst2_index = 0
    for item1 in lst1:
        found = False
        for i in range(lst2_index, len(lst2)):
            if lst2[i] == item1:
                lst2_index = i + 1
                found = True
                break
        if not found:
            return False
    return True


print(sublist([], []))
print(sublist([], [1, 2, 3]))
print(sublist([2], [1, 2, 3]))
print(sublist([1, 3, 4], [1, 2, 3, 4, 5]))
print(sublist([1, 4, 3], [1, 2, 3, 4, 5]))
