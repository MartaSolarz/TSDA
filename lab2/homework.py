def copy(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i)
    return new_lst


def set_sum(lst1, lst2):
    new_lst2 = copy(lst2)
    for i in lst1:
        if i not in new_lst2:
            new_lst2.append(i)
    return new_lst2


def sorted_set_sum(lst1, lst2):
    set_of_lists = set_sum(lst1, lst2)
    sorted_set_of_lists = []
    while len(set_of_lists) > 0:
        min_value = min(set_of_lists)
        sorted_set_of_lists.append(min_value)
        set_of_lists.remove(min_value)
    return sorted_set_of_lists


if __name__ == "__main__":
    print(sorted_set_sum([-2, 1, 3], [-3, -2, 0, 1, 34]))