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
    new = set_sum(lst1, lst2)
    for i in range(len(new)):
        for j in range(i + 1, len(new)):
            if new[i] > new[j]:
                new[i], new[j] = new[j], new[i]
    return new


if __name__ == "__main__":
    print(sorted_set_sum([-2, 1, 3], [34, -3, -2, 0, 1]))