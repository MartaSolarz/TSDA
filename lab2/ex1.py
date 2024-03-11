# Exercise 1
# Write a function my_sum(lst) that returns the total of numbers from a given (as a parameter) list.
# The total of an empty list is (of course) 0.

# Sample results of the function:

# my_sum([]) == 0
# my_sum([1, 22, 3]) == 26


def my_sum(lst):
    return sum(lst)

# Exercise 2
# Write a function sum_2d(lst) that returns the total of numbers stored in a two-dimensional list  (ie. list of lists)
# of numbers. The component lists do not have to be of the same length.

# Sample results of the function:

# sum_2d([]) == 0
# sum_2d([[],[],[]]) == 0
# sum_2d([[1, 2, 3], [], [-34, 23423, -23425]]) == -30


def sum_2d(lst):
    return sum([sum(x) for x in lst])

# Exercise 3
# Write a function how_many(lst, what) that counts how many times the given element what appears on the list `lst'.

# Sample results of the function:

# how_many([], 13) == 0
# how_many([1, 234, 123, 23, 1, 234, 1, -43], 1) == 3
# how_many(["Mary", "Jenny", "Mary", "Susan"], "Mary") == 2
# how_many(["Mary", "Jenny", "Mary", "Susan"], "Emily") == 0
# how_many("Mary has a little lamb", "a") == 4


def how_many(lst, what):
    return lst.count(what)

# Exercise 4
# Write a function copy(lst) that returns a copy of the list given. Use the list.append(elt) operation.

# Sample results of the function:

# copy([]) == []
# copy([1, 2, 3]) == [1, 2, 3]


def copy(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i)
    return new_lst

# Exercise 5
# Write a function reverse(lst) that returns a reversed copy of the list given. Use the list addition operator +.

# Sample results of the function:

# reverse([]) == []
# reverse([1, 2, 3]) == [3, 2, 1]


def reverse(lst):
    return lst[::-1]


def reverseV2(lst):
    new_lst = []
    for i in lst:
        new_lst = [i] + new_lst
    return new_lst


# Exercise 6
# Write a function reverse2(lst) that returns a reversed copy of the list given.
# This time use only the append operation (no addition of lists is allowed in this exercise).

# Sample results of the function:

# reverse2([]) == []
# reverse2([1, 2, 3]) == [3, 2, 1]


def reverse2(lst):
    new_lst = []
    for i in range(len(lst) - 1, -1, -1):
        new_lst.append(lst[i])
    return new_lst

# Exercise 7
# Write a function set_sum(lst1, lst2) that returns the set-theoretic sum of arguments.
# In this exercise, sets are to be represented as unordered lists of their elements (without duplicates).

# Sample results of the function:

# set_sum([], []) == []
# set_sum([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
# set_sum([], [1, 2, 3]) == [1, 2, 3]
# set_sum([1, 2, 3], []) == [1, 2, 3]
# set_sum([1, 3, -2], [-2, -3, 0, 1, 34]) == [1, 3, -2, -3, 0, 34] (the order maybe different)


def set_sum(lst1, lst2):
    return list(set(lst1 + lst2))

def set_sumV2(lst1, lst2):
    new = copy(lst1)
    for i in lst2:
        if i not in new:
            new.append(i)
    return new

# Exercise 8
# Write a function sorted_set_sum(lst1, lst2) that returns the set-theoretic sum of arguments.
# In this exercise, sets are to be represented as lists of their elements in ascending order
# (hence there are no duplicates on these lists).
# You are allowed to use on lists only indexing and the len and append functions.

# Sample results of the function:

# sorted_set_sum([], []) == []
# sorted_set_sum([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
# sorted_set_sum([], [1, 2, 3]) == [1, 2, 3]
# sorted_set_sum([1, 2, 3], []) == [1, 2, 3]
# sorted_set_sum([-2, 1, 3], [-3, -2, 0, 1, 34]) == [-3, -2, 0, 1, 3, 34]


def sorted_set_sum(lst1, lst2):
    elements = list(set(lst1 + lst2))
    elements.sort()
    return elements


def sorted_set_sumV2(lst1, lst2):
    new = set_sumV2(lst1, lst2)
    for i in range(len(new)):
        for j in range(i + 1, len(new)):
            if new[i] > new[j]:
                new[i], new[j] = new[j], new[i]
    return new

if __name__ == "__main__":
    print(my_sum([]))
    print(my_sum([1, 22, 3]))

    print(sum_2d([]))
    print(sum_2d([[],[],[]]))
    print(sum_2d([[1, 2, 3], [], [-34, 23423, -23425]]))

    print(how_many([], 13))
    print(how_many([1, 234, 123, 23, 1, 234, 1, -43], 1))
    print(how_many(["Mary", "Jenny", "Mary", "Susan"], "Mary"))
    print(how_many(["Mary", "Jenny", "Mary", "Susan"], "Emily"))
    print(how_many("Mary has a little lamb", "a"))

    print(copy([]))
    print(copy([1, 2, 3]))

    print(reverse([]))
    print(reverse([1, 2, 3]))

    print(reverseV2([]))
    print(reverseV2([1, 2, 3]))

    print(reverse2([]))
    print(reverse2([1, 2, 3]))

    print(set_sum([], []))
    print(set_sum([1, 2, 3], [1, 2, 3]))
    print(set_sum([], [1, 2, 3]))
    print(set_sum([1, 2, 3], []))
    print(set_sum([1, 3, -2], [-2, -3, 0, 1, 34]))

    print(sorted_set_sum([], []))
    print(sorted_set_sum([1, 2, 3], [1, 2, 3]))
    print(sorted_set_sum([], [1, 2, 3]))
    print(sorted_set_sum([1, 2, 3], []))
    print(sorted_set_sum([-2, 1, 3], [-3, -2, 0, 1, 34]))

    print(sorted_set_sumV2([], []))
    print(sorted_set_sumV2([1, 2, 3], [1, 2, 3]))
    print(sorted_set_sumV2([], [1, 2, 3]))
    print(sorted_set_sumV2([1, 2, 3], []))
    print(sorted_set_sumV2([-2, 1, 3], [-3, -2, 0, 1, 34]))
